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

    def generate_whatsapp_status_card(self, candidate_name, target_course, target_uni, predicted_data, leaks, cheat_count=0):
        """
        Generates a viral text format optimized for sharing to WhatsApp Status / Groups.
        """
        score = predicted_data["total_predicted_score"]
        status_emoji = "🔥" if score >= 250 else "⚡"

        top_leaks_str = ""
        if leaks:
            top_leaks_str = f"⚠️ Leaky Topics to fix: {leaks[0]['subtopic']} (-{leaks[0]['estimated_mark_loss']} marks)\n"

        integrity_str = (
            f"🛡️ Anti-Cheat Integrity: ⚠️ {cheat_count} Tab-Switch Warning(s) Logged\n"
            if cheat_count > 0
            else "🛡️ Anti-Cheat Integrity: ✅ 100% Clean Session (Zero Tab Switches)\n"
        )

        card_text = (
            f"🎯 *MY OFFICIAL JAMB 2026/2027 READINESS SCORE*\n"
            f"👤 Candidate: {candidate_name}\n"
            f"🎓 Target: {target_course} at {target_uni}\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"{status_emoji} *Predicted Score: {score} / 400*\n"
            f"📊 Status: {predicted_data['readiness_level']}\n"
            f"{top_leaks_str}"
            f"{integrity_str}"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"💡 Tested with *PassMaster AI* — Socratic Exam Coach.\n"
            f"👉 Test your own score for FREE: passmaster.ng/diagnostic"
        )
        return card_text

    def calculate_admission_chances(self, university, course, jamb_score, olevel_grades, post_utme_score=None):
        """
        Calculates university composite aggregate score and predicts admission probability
        against official historical departmental cut-offs.
        """
        university = (university or "UNILAG").strip()
        course = (course or "Medicine & Surgery").strip()
        jamb_score = max(100, min(400, int(jamb_score or 250)))

        # Standard Grade Values
        grade_points_unilag = {"A1": 4.0, "B2": 3.6, "B3": 3.2, "C4": 2.8, "C5": 2.4, "C6": 2.0}
        grade_points_50 = {"A1": 10.0, "B2": 9.0, "B3": 8.0, "C4": 7.0, "C5": 6.0, "C6": 5.0}

        # Normalize O'Level grades (expecting 5 subjects)
        if isinstance(olevel_grades, list):
            grades_list = olevel_grades[:5]
        elif isinstance(olevel_grades, dict):
            grades_list = list(olevel_grades.values())[:5]
        else:
            grades_list = ["B2", "B3", "A1", "B2", "C4"]

        while len(grades_list) < 5:
            grades_list.append("B3")

        # Compute O'Level aggregate
        unilag_olevel_total = sum(grade_points_unilag.get(str(g).upper().strip(), 3.0) for g in grades_list)
        fifty_olevel_total = sum(grade_points_50.get(str(g).upper().strip(), 7.0) for g in grades_list)

        uni_upper = university.upper()
        if "UNILAG" in uni_upper:
            jamb_pts = (jamb_score / 400.0) * 50.0  # max 50
            olevel_pts = unilag_olevel_total         # max 20
            if post_utme_score is not None and float(post_utme_score) > 0:
                putme_pts = min(30.0, float(post_utme_score))
            else:
                putme_pts = (jamb_score / 400.0) * 30.0  # simulated post-utme
            aggregate = round(jamb_pts + olevel_pts + putme_pts, 2)
            formula_desc = "UNILAG Formula: JAMB (50%) + O'Level 5 Subjects (20%) + Post-UTME (30%)"

        elif any(u in uni_upper for u in ["UI", "OAU", "UNN"]):
            jamb_pts = (jamb_score / 8.0)  # max 50
            if post_utme_score is not None and float(post_utme_score) > 0:
                putme_pts = min(50.0, float(post_utme_score) / 2.0 if float(post_utme_score) > 50 else float(post_utme_score))
            else:
                putme_pts = fifty_olevel_total  # O'Level screening substitute max 50
            aggregate = round(jamb_pts + putme_pts, 2)
            formula_desc = f"{university} Model: JAMB / 8 (50%) + Post-UTME/Screening (50%)"

        elif "FUTA" in uni_upper or "UNIBEN" in uni_upper:
            jamb_pts = (jamb_score / 400.0) * 50.0
            olevel_pts = (fifty_olevel_total / 50.0) * 50.0
            aggregate = round(jamb_pts + olevel_pts, 2)
            formula_desc = f"{university} Model: JAMB 50% + O'Level Points 50%"

        else:
            jamb_pts = (jamb_score / 400.0) * 60.0
            olevel_pts = (fifty_olevel_total / 50.0) * 40.0
            aggregate = round(jamb_pts + olevel_pts, 2)
            formula_desc = "Federal Model: JAMB 60% + O'Level Evaluation 40%"

        aggregate = min(100.0, max(20.0, aggregate))

        # Departmental Cut-Off Standards
        cutoff_dict = {
            "medicine & surgery": 81.5,
            "pharmacy": 76.5,
            "nursing science": 74.0,
            "law": 78.0,
            "computer science": 76.5,
            "software engineering": 75.5,
            "mechanical engineering": 74.5,
            "electrical & electronics engineering": 75.0,
            "civil engineering": 72.0,
            "accounting": 73.0,
            "economics": 71.5,
            "mass communication": 72.5,
            "dentistry": 77.0,
            "medical laboratory science": 73.5,
            "biochemistry": 68.0,
            "microbiology": 67.5,
            "business administration": 70.0,
            "political science": 69.5
        }

        course_lower = course.lower()
        target_cutoff = 66.0
        for k, v in cutoff_dict.items():
            if k in course_lower or course_lower in k:
                target_cutoff = v
                break

        catchment_cutoff = round(target_cutoff - 2.5, 2)
        diff = round(aggregate - target_cutoff, 2)

        if aggregate >= target_cutoff + 2.0:
            status = "Guaranteed Merit Admission Zone"
            color = "#10b981"
            prob_pct = min(99, int(86 + (aggregate - target_cutoff) * 3))
            advice = (
                f"Coach Kalu's Strategic Advice: 🌟 Outstanding merit position! Your composite aggregate of {aggregate}% comfortably surpasses "
                f"the historical {target_cutoff}% merit benchmark for {course} at {university}. Maintain your CBT "
                f"drills to protect your exam-day execution."
            )
        elif aggregate >= target_cutoff:
            status = "Highly Competitive (Merit Contender)"
            color = "#3b82f6"
            prob_pct = int(76 + (aggregate - target_cutoff) * 4)
            advice = (
                f"Coach Kalu's Strategic Advice: 🎯 Strong standing! At {aggregate}%, you meet the historical {target_cutoff}% merit cut-off for {course}. "
                f"To be 100% immune from annual cut-off inflation, target an extra 8-12 marks in your JAMB mock drills."
            )
        elif aggregate >= catchment_cutoff:
            status = "Catchment / Discretionary Range"
            color = "#f59e0b"
            prob_pct = int(52 + (aggregate - catchment_cutoff) * 6)
            advice = (
                f"Coach Kalu's Strategic Advice: ⚠️ Borderline alert: Your {aggregate}% aggregate is near the catchment threshold ({catchment_cutoff}%), "
                f"but trails the {target_cutoff}% open merit line. You need approximately {max(4, int(abs(diff) * 8))} "
                f"more marks in JAMB to leapfrog into the safe merit zone."
            )
        else:
            status = "High Risk (Action Required Immediately)"
            color = "#ef4444"
            prob_pct = max(18, int(45 - abs(diff) * 4))
            advice = (
                f"Coach Kalu's Strategic Advice: 🚨 Critical gap: Your aggregate of {aggregate}% is {abs(diff)}% below the required {target_cutoff}% "
                f"merit line for {course} at {university}. Master your top 3 leaky topics in PassMaster AI immediately to boost your "
                f"score by at least {int(abs(diff) * 8)} marks!"
            )

        whatsapp_share = (
            f"🎓 *MY JAMB & UNIVERSITY ADMISSION PROBABILITY*\n"
            f"🏛️ University: {university}\n"
            f"📚 Course: {course}\n"
            f"🎯 Composite Aggregate: *{aggregate}%* (Cut-off: {target_cutoff}%)\n"
            f"📊 Admission Status: {status} ({prob_pct}% Chance)\n"
            f"━━━━━━━━━━━━━━━━━━━━━\n"
            f"💡 Calculated with *PassMaster AI* — Socratic Exam Coach.\n"
            f"👉 Calculate your university chance: passmaster.ng/aggregate"
        )

        return {
            "university": university,
            "course": course,
            "jamb_score": jamb_score,
            "aggregate_score": aggregate,
            "target_cutoff": target_cutoff,
            "catchment_cutoff": catchment_cutoff,
            "difference": diff,
            "status": status,
            "probability_pct": prob_pct,
            "status_color": color,
            "formula_used": formula_desc,
            "coach_advice": advice,
            "whatsapp_share_text": whatsapp_share
        }


