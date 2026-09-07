import json
import os
import requests

class SocraticTutor:
    def __init__(self, questions_path="data/questions.json"):
        self.questions_path = questions_path
        self.questions = self._load_questions()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")

    def _load_questions(self):
        try:
            with open(self.questions_path, "r") as f:
                data = json.load(f)
                return {q["id"]: q for q in data}
        except Exception as e:
            print(f"Error loading questions: {e}")
            return {}

    def analyze_attempt(self, question_id, selected_option):
        """
        Evaluates a student's initial answer attempt Socratically.
        """
        question = self.questions.get(question_id)
        if not question:
            return {"error": "Question not found"}

        is_correct = (selected_option.upper() == question["correct_option"].upper())
        correct_opt = question["correct_option"]

        if is_correct:
            return {
                "status": "correct",
                "is_correct": True,
                "selected_option": selected_option,
                "correct_option": correct_opt,
                "feedback_type": "reinforcement",
                "message": (
                    f"🎯 Brilliant! Option {selected_option} is 100% correct.\n\n"
                    f"**Why you succeeded:** You avoided the trap. {question['pedagogical_concept']}"
                ),
                "concept": question["pedagogical_concept"],
                "can_retry": False
            }
        else:
            trap_analysis = question.get("traps", {}).get(
                selected_option.upper(),
                "You selected an incorrect option that does not satisfy the theoretical rule."
            )
            socratic_prompt = question.get("socratic_prompt", "Think carefully about the underlying rule.")

            return {
                "status": "incorrect",
                "is_correct": False,
                "selected_option": selected_option,
                "correct_option": None,  # Do not give away the correct answer yet!
                "feedback_type": "socratic_challenge",
                "trap_detected": trap_analysis,
                "socratic_prompt": socratic_prompt,
                "message": (
                    f"⚠️ Hold on! Option {selected_option} is not correct.\n\n"
                    f"**The Cognitive Trap:** {trap_analysis}\n\n"
                    f"💡 **Coaching Question:** {socratic_prompt}\n\n"
                    f"👉 *Reply to this tutor with your thought, or pick another option!*"
                ),
                "concept": question["pedagogical_concept"],
                "can_retry": True
            }

    def chat_reply(self, question_id, user_message, previous_attempts=None):
        """
        Handles interactive follow-up dialogue between the student and the AI tutor.
        """
        question = self.questions.get(question_id)
        if not question:
            return {"reply": "I couldn't locate this specific question. Please select a question from the menu."}

        # If Gemini API Key is available, attempt live LLM call
        if self.gemini_api_key:
            try:
                system_prompt = (
                    "You are 'Coach Kalu', a brilliant, encouraging, sharp Nigerian master tutor specializing in JAMB/WAEC. "
                    "Your goal is Socratic coaching: NEVER just blurt out the answer. Guide the student to see the solution. "
                    "Use crisp, clear language, occasional friendly Nigerian educational warmth, and solid scientific/mathematical rigor. "
                    f"Current Question: {question['question']}\n"
                    f"Options: {json.dumps(question['options'])}\n"
                    f"Correct Option: {question['correct_option']}\n"
                    f"Underlying Rule: {question['pedagogical_concept']}\n"
                    f"Common Traps: {json.dumps(question['traps'])}"
                )

                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.gemini_api_key}"
                payload = {
                    "contents": [
                        {"role": "user", "parts": [{"text": f"{system_prompt}\n\nStudent Message: {user_message}"}]}
                    ]
                }
                res = requests.post(url, json=payload, timeout=8)
                if res.status_code == 200:
                    data = res.json()
                    ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return {"reply": ai_text, "source": "gemini_live"}
            except Exception as ex:
                print(f"LLM API fallback triggered: {ex}")

        # Intelligent Built-in Pedagogical Logic (Fast, deterministic & zero latency)
        msg_lower = user_message.lower()
        correct_opt = question["correct_option"]
        correct_text = question["options"][correct_opt]

        # Case 1: Student is asking for the direct answer ("tell me the answer", "i give up", "what is it")
        if any(w in msg_lower for w in ["give up", "tell me", "what is the answer", "surrender", "just show"]):
            return {
                "reply": (
                    f"Alright, let's break it down fully!\n\n"
                    f"The correct option is **{correct_opt}: {correct_text}**.\n\n"
                    f"📌 **Full Master Explanation:** {question['pedagogical_concept']}\n\n"
                    f"Remember: In JAMB, examiners love setting this exact trap. Now you know how to defeat it!"
                ),
                "revealed": True,
                "correct_option": correct_opt
            }

        # Case 2: Student mentions numbers / keywords relevant to the question
        if question["subject"] == "Physics" and "kelvin" in msg_lower or any(k in msg_lower for k in ["300", "400", "273"]):
            return {
                "reply": (
                    "Spot on! 27 + 273 = 300 K, and 127 + 273 = 400 K.\n\n"
                    "Now apply Charles's Law: V₁ / T₁ = V₂ / T₂\n"
                    "500 / 300 = V₂ / 400\n"
                    "V₂ = (500 × 400) / 300 = **666.7 cm³** (Option B)!\n\n"
                    "See how easy it is once you use Absolute Temperature?"
                ),
                "revealed": True,
                "correct_option": "B"
            }

        if question["subject"] == "Use of English" and any(k in msg_lower for k in ["teachers", "closer", "plural", "yesterday", "proximity"]):
            return {
                "reply": (
                    "Exactly right! 'The teachers' is right next to the verb, so it takes the plural form. "
                    "And because it says 'yesterday morning', it must be past tense ('were'). "
                    "Hence, the correct answer is **Option B (were)**. Excellent deduction!"
                ),
                "revealed": True,
                "correct_option": "B"
            }

        if question["subject"] == "Mathematics" and any(k in msg_lower for k in ["chain rule", "6x", "inside", "derivative"]):
            return {
                "reply": (
                    "Yes! You got the crucial step. Differentiating the inner term (3x² - 5) yields 6x. "
                    "Multiplying that by the outer power derivative 4(3x² - 5)³ gives **24x(3x² - 5)³** (Option B)!\n\n"
                    "Never leave the inner derivative behind."
                ),
                "revealed": True,
                "correct_option": "B"
            }

        # Default Socratic encouragement
        return {
            "reply": (
                f"You're thinking along the right lines! Let's zero in:\n\n"
                f"Here is your guiding hint: {question['socratic_prompt']}\n\n"
                f"Look at the options: {', '.join([f'[{k}] {v}' for k, v in question['options'].items()])}. Which one aligns with this logic?"
            ),
            "revealed": False
        }
