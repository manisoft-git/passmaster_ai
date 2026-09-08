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
        Supports both question-specific trap coaching AND free-form academic inquiries across any subject.
        """
        question = self.questions.get(question_id) if question_id else None

        # Free-form General Academic Inquiry Handling
        if not question or question_id == "general":
            return self.general_academic_reply(user_message)

        # If Gemini API Key is available, attempt live LLM call for question
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

    def general_academic_reply(self, user_message):
        """
        Handles free-form academic, curriculum, or syllabus questions asked by students.
        """
        msg_lower = (user_message or "").lower().strip()

        # If Gemini API Key is available, answer via LLM
        if self.gemini_api_key:
            try:
                prompt = (
                    "You are 'Coach Kalu', a brilliant, encouraging master Nigerian tutor specializing in JAMB & WAEC. "
                    "The student is preparing for the 2026/2027 JAMB exam and asked an academic or syllabus question. "
                    "Provide a direct, crystal-clear, structured explanation with rules/formulas, worked examples, and key traps to watch out for. "
                    f"Student Question: {user_message}"
                )
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={self.gemini_api_key}"
                payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}
                res = requests.post(url, json=payload, timeout=8)
                if res.status_code == 200:
                    data = res.json()
                    ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return {"reply": ai_text, "source": "gemini_live", "topic": "General Academic"}
            except Exception as ex:
                print(f"LLM general chat fallback: {ex}")

        # Intelligent syllabus knowledge base
        if any(w in msg_lower for w in ["proximity", "neither", "either"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu's Master Rule on Proximity:**\n\n"
                    "When two subjects are joined by *either... or*, *neither... nor*, or *not only... but also*, the verb agrees ONLY with the subject physically closest to it!\n\n"
                    "• *Neither the teacher nor the students ARE here.* ('students' is plural & closest)\n"
                    "• *Neither the students nor the teacher IS here.* ('teacher' is singular & closest)\n\n"
                    "⚠️ **JAMB Trap:** Examiners put a singular noun first and a plural second to tempt you to match the first noun. Always look immediately to the LEFT of the verb!"
                ),
                "topic": "Concord & Grammar"
            }

        if any(w in msg_lower for w in ["subjunctive", "command", "insist", "decreed", "recommend"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on the Mandative Subjunctive:**\n\n"
                    "After verbs of recommendation, demand, insistence, or decree (*recommend that, insist that, decree that, mandate that*), the dependent verb MUST be in its base infinitive form (no 's' or 'es'!).\n\n"
                    "• *The committee recommended that the candidate APPEAR before the panel.* (NOT appears!)\n"
                    "• *The doctor suggested that he TAKE the medicine.* (NOT takes!)\n\n"
                    "Always use the bare root form regardless of whether the subject is he, she, or it."
                ),
                "topic": "Concord & Grammar"
            }

        if any(w in msg_lower for w in ["kelvin", "charles", "gas law", "boyle"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu's Gas Law Warning:**\n\n"
                    "In ANY gas calculation (Charles's Law: V₁/T₁ = V₂/T₂, Boyle's: P₁V₁ = P₂V₂, Combined: P₁V₁/T₁ = P₂V₂/T₂), temperature MUST ALWAYS be in **Kelvin**!\n\n"
                    "📌 Formula: **T(K) = θ(°C) + 273**\n\n"
                    "⚠️ **The Fatal Trap:** If 27°C (300 K) is heated to 127°C (400 K), the volume increases by ratio 400/300 (4/3), NOT 127/27! Never plug Celsius into gas equations!"
                ),
                "topic": "Thermal Physics"
            }

        if any(w in msg_lower for w in ["chain rule", "derivative", "differentiate"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Calculus & The Chain Rule:**\n\n"
                    "When differentiating a composite function y = [u(x)]^n:\n"
                    "📌 **dy/dx = n[u(x)]^(n-1) × du/dx**\n\n"
                    "Example: y = (3x² - 5)⁴\n"
                    "1. Outside derivative: 4(3x² - 5)³\n"
                    "2. Inside derivative: d/dx(3x² - 5) = 6x\n"
                    "3. Multiply them: 4(3x² - 5)³ × 6x = **24x(3x² - 5)³**!\n\n"
                    "Rule to live by: Never leave the inner derivative behind!"
                ),
                "topic": "Calculus"
            }

        if any(w in msg_lower for w in ["quadratic", "roots", "alpha", "beta", "α"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Quadratic Roots (α and β):**\n\n"
                    "For ax² + bx + c = 0 with roots α and β:\n"
                    "• **Sum of roots (α + β) = -b/a**\n"
                    "• **Product of roots (αβ) = c/a**\n\n"
                    "Golden Identities for JAMB:\n"
                    "• α² + β² = (α + β)² - 2αβ\n"
                    "• 1/α + 1/β = (α + β) / αβ\n\n"
                    "Never forget the minus sign in -b/a!"
                ),
                "topic": "Algebra"
            }

        if any(w in msg_lower for w in ["osmosis", "plasmolysis", "turgid", "flaccid"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Osmosis & Plasmolysis:**\n\n"
                    "• **Hypotonic Solution (Dilute/pure water):** Water enters cell => Plant cell becomes **TURGID**; Animal cell swells and undergoes **LYSIS (bursts)**.\n"
                    "• **Hypertonic Solution (Concentrated salt/sugar):** Water leaves cell => Plant protoplasm shrinks away from cell wall (**PLASMOLYSIS**); Animal cell shrinks (**CRENATION**).\n"
                    "• Plant cells don't burst because they possess a rigid cellulose cell wall!"
                ),
                "topic": "Cell Biology"
            }

        if any(w in msg_lower for w in ["constitution", "1963", "1979", "lugard", "indirect rule"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Nigerian Government & History:**\n\n"
                    "• **1963 Republican Constitution:** Severed last ties to the British Crown. Abolished Privy Council appeals (Supreme Court became final) and Elizabeth II ceased to be Head of State.\n"
                    "• **1979 Constitution:** First Executive Presidential system (replacing Westminster parliamentary model).\n"
                    "• **Indirect Rule:** Highly successful in Northern Emirates (centralized hierarchy), failed in the East (acephalous/republican Igbo society led to 1929 Aba Riots over Warrant Chiefs)."
                ),
                "topic": "Nigerian Government"
            }

        if any(w in msg_lower for w in ["irony", "catharsis", "soliloquy", "metonymy"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Literary Devices:**\n\n"
                    "• **Dramatic Irony:** The audience knows vital truth that characters on stage are oblivious to.\n"
                    "• **Catharsis:** The emotional purging/cleansing of pity and fear felt by the audience at tragic catastrophe.\n"
                    "• **Soliloquy:** A character speaking alone on stage revealing inner motives.\n"
                    "• **Metonymy:** Substituting an object with an associated attribute ('The pen is mightier than the sword')."
                ),
                "topic": "Literature Devices"
            }

        if any(w in msg_lower for w in ["280", "score", "pass", "jamb tip", "how to"]):
            return {
                "reply": (
                    "🎯 **Coach Kalu's Blueprint to 280+ in JAMB 2026/2027:**\n\n"
                    "1. **Stop Memorizing, Start Diagnosing:** 76% of candidates fail because they memorize answers without understanding why distractors are wrong.\n"
                    "2. **Eliminate Your Leaky Topics:** Use our Leaky Bucket tab to see exactly where you are losing marks.\n"
                    "3. **Target 45 Seconds per Question:** In JAMB, you have 180 questions in 120 minutes. That is 40 seconds per question. Never get stuck on any question for over 1 minute.\n"
                    "4. **Study Topic Master Lessons:** Review the 32 syllabus lessons right here in PassMaster AI to seal your knowledge gaps."
                ),
                "topic": "JAMB Strategy"
            }

        # Friendly contextual fallback
        return {
            "reply": (
                f"Great question! As Coach Kalu, I am here to help you conquer every angle of your SS3 syllabus and JAMB 2026/2027.\n\n"
                f"You asked about: *\"{user_message}\"*\n\n"
                f"To give you the sharpest breakdown, tell me the specific subject (Use of English, Math, Physics, Chemistry, Biology, Economics, Government, Literature) or select a topic from our Topic Lessons menu!"
            ),
            "topic": "Academic Coaching"
        }
