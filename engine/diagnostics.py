import json
import math

class DiagnosticEngine:
    def __init__(self, syllabus_path="data/syllabus.json", questions_path="data/questions.json"):
        self.syllabus = self._load_json(syllabus_path)
        self.questions = self._load_json(questions_path)

    def _load_json(self, path):
        try:
            with open(path, "r") as f:
                return json.load(f)
        except Exception as e:
            print(f"Error loading {path}: {e}")
            return {}

    def calculate_predicted_score(self, session_history):
        """
        Computes the weighted JAMB predicted score (out of 400) based on student history.
        session_history is a dict: { question_id: {"selected": "B", "is_correct": True, "time_seconds": 32} }
        """
        if not session_history:
            return {
                "total_predicted_score": 180,
                "confidence": "Preliminary (Need at least 5 questions)",
                "subject_breakdown": {},
                "readiness_level": "High Risk (< 200)",
                "readiness_color": "#ef4444"
            }

        subject_scores = {}
        subject_counts = {}

        for q_id, record in session_history.items():
            # Find question in database
            q = next((item for item in self.questions if item["id"] == q_id), None)
            if not q:
                continue

            subj = q["subject"]
            if subj not in subject_scores:
                subject_scores[subj] = {"correct": 0, "total": 0, "total_time": 0}

            subject_scores[subj]["total"] += 1
            subject_scores[subj]["total_time"] += record.get("time_seconds", 40)
            if record.get("is_correct"):
                subject_scores[subj]["correct"] += 1

        # Calculate subject marks scaled to 100
        total_score = 0
        breakdown = {}

        # Default standard 4 subjects for a science/JAMB candidate
        active_subjects = list(subject_scores.keys())
        if not active_subjects:
            active_subjects = ["Use of English", "Mathematics", "Physics", "Chemistry"]

        for subj in active_subjects:
            stats = subject_scores.get(subj, {"correct": 0, "total": 0, "total_time": 0})
            if stats["total"] > 0:
                raw_accuracy = stats["correct"] / stats["total"]
                avg_time = stats["total_time"] / stats["total"]
                # Time penalty if taking longer than 45s per question
                time_multiplier = 1.0 if avg_time <= 45 else max(0.85, 1.0 - ((avg_time - 45) / 100))
                scaled_mark = int(raw_accuracy * 100 * time_multiplier)
            else:
                scaled_mark = 45  # baseline assumption for unattempted subject

            breakdown[subj] = {
                "score": scaled_mark,
                "attempted": stats["total"],
                "correct": stats["correct"],
                "accuracy_pct": int((stats["correct"] / stats["total"] * 100)) if stats["total"] > 0 else 0
            }
            total_score += scaled_mark

        # Normalize to 4 subjects
        if len(active_subjects) < 4:
            missing = 4 - len(active_subjects)
            total_score += missing * 45

        # Cap total between 60 and 390
        total_score = max(60, min(390, total_score))

        if total_score >= 280:
            level = "Elite (Medicine / Law / Top Engineering Ready)"
            color = "#10b981"
        elif total_score >= 230:
            level = "Competitive (Eligible for Most Federal Universities)"
            color = "#3b82f6"
        elif total_score >= 200:
            level = "Average Borderline (At risk for high-demand courses)"
            color = "#f59e0b"
        else:
            level = "High Risk (< 200 - Action Required Immediately)"
            color = "#ef4444"

        return {
            "total_predicted_score": total_score,
            "max_score": 400,
            "readiness_level": level,
            "readiness_color": color,
            "subject_breakdown": breakdown
        }

    def get_leaky_bucket_analysis(self, session_history):
        """
        Identifies the specific micro-topics where the student is bleeding the most marks.
        """
        topic_stats = {}

        for q_id, record in session_history.items():
            q = next((item for item in self.questions if item["id"] == q_id), None)
            if not q:
                continue

            key = (q["subject"], q["topic"], q["subtopic"])
            if key not in topic_stats:
                topic_stats[key] = {"total": 0, "correct": 0, "sample_q": q}

            topic_stats[key]["total"] += 1
            if record.get("is_correct"):
                topic_stats[key]["correct"] += 1

        leaks = []
        for (subj, topic, subtopic), data in topic_stats.items():
            fail_count = data["total"] - data["correct"]
            if fail_count > 0:
                # Calculate estimated JAMB mark loss
                estimated_mark_loss = fail_count * 4  # 4 marks per question in JAMB
                leaks.append({
                    "subject": subj,
                    "topic": topic,
                    "subtopic": subtopic,
                    "fails": fail_count,
                    "accuracy_pct": int((data["correct"] / data["total"]) * 100),
                    "estimated_mark_loss": estimated_mark_loss,
                    "sample_question_id": data["sample_q"]["id"],
                    "pedagogical_concept": data["sample_q"]["pedagogical_concept"]
                })

        # Sort by biggest mark loss
        leaks.sort(key=lambda x: x["estimated_mark_loss"], reverse=True)
        return leaks

    def generate_whatsapp_status_card(self, candidate_name, target_course, target_uni, predicted_data, leaks):
        """
        Generates a viral text format optimized for sharing to WhatsApp Status / Groups.
        """
        score = predicted_data["total_predicted_score"]
        status_emoji = "🔥" if score >= 250 else "⚡"

        top_leaks_str = ""
        if leaks:
            top_leaks_str = f"⚠️ Leaky Topics to fix: {leaks[0]['subtopic']} (-{leaks[0]['estimated_mark_loss']} marks)"

        card_text = (
            f"🎯 *MY OFFICIAL JAMB 2025/2026 READINESS SCORE*\n"
            f"👤 Candidate: {candidate_name}\n"
            f"🎓 Target: {target_course} at {target_uni}\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"{status_emoji} *Predicted Score: {score} / 400*\n"
            f"📊 Status: {predicted_data['readiness_level']}\n"
            f"{top_leaks_str}\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"💡 Tested with *PassMaster AI* — Socratic Exam Coach.\n"
            f"👉 Test your own score for FREE: passmaster.ng/diagnostic"
        )
        return card_text
