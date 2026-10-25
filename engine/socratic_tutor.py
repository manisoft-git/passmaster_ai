import json
import os
import re
import random
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_QUESTIONS = os.path.join(BASE_DIR, "data", "questions.json")

class SocraticTutor:
    def __init__(self, questions_path=None):
        questions_path = questions_path or DEFAULT_QUESTIONS
        self.questions_path = questions_path
        self.questions = self._load_questions()
        self.gemini_api_key = os.getenv("GEMINI_API_KEY", "")

    def _load_questions(self):
        try:
            with open(self.questions_path, "r", encoding="utf-8") as f:
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

    def _call_gemini(self, prompt, context_system=None):
        """
        Invokes the Google Gemini API with the highest feasible reasoning model.
        Defaults to gemini-2.5-pro (or GEMINI_MODEL env), cascading gracefully through:
        gemini-2.5-pro -> gemini-1.5-pro -> gemini-2.5-flash -> gemini-1.5-flash.
        Returns: (text_reply, model_used) or (None, None) if unreachable.
        """
        api_key = self.gemini_api_key or os.getenv("GEMINI_API_KEY", "")
        if not api_key:
            return None, None

        preferred_model = os.getenv("GEMINI_MODEL", "gemini-2.5-pro").strip()
        cascade_models = [preferred_model]
        for m in ["gemini-2.5-pro", "gemini-1.5-pro", "gemini-2.5-flash", "gemini-1.5-flash"]:
            if m not in cascade_models:
                cascade_models.append(m)

        parts = []
        if context_system:
            parts.append({"text": context_system})
        parts.append({"text": prompt})

        payload = {
            "contents": [{"role": "user", "parts": parts}],
            "generationConfig": {
                "temperature": 0.65,
                "maxOutputTokens": 1024
            }
        }

        for model in cascade_models:
            try:
                url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={api_key}"
                res = requests.post(url, json=payload, timeout=9)
                if res.status_code == 200:
                    data = res.json()
                    candidates = data.get("candidates", [])
                    if candidates and "content" in candidates[0] and "parts" in candidates[0]["content"]:
                        ai_text = candidates[0]["content"]["parts"][0].get("text", "").strip()
                        if ai_text:
                            return ai_text, model
                elif res.status_code in (400, 404, 429, 503):
                    print(f"Gemini model {model} returned HTTP {res.status_code}, falling back...")
                    continue
            except Exception as ex:
                print(f"Gemini API model {model} error: {ex}")
                continue

        return None, None

    def chat_reply(self, question_id, user_message, previous_attempts=None):
        """
        Handles interactive follow-up dialogue between the student and the AI tutor.
        Supports both question-specific trap coaching AND free-form academic inquiries across any subject.
        """
        question = self.questions.get(question_id) if question_id else None

        # Free-form General Academic Inquiry Handling
        if not question or question_id == "general":
            return self.general_academic_reply(user_message)

        # If Gemini API Key is available, attempt live LLM call with highest model (gemini-2.5-pro)
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
        ai_text, model_used = self._call_gemini(f"Student Message: {user_message}", context_system=system_prompt)
        if ai_text:
            return {"reply": ai_text, "source": "gemini_live", "model": model_used}

        # Intelligent Built-in Pedagogical Logic (Fast, deterministic, conversational & zero latency)
        msg_lower = user_message.lower().strip()
        correct_opt = question["correct_option"].upper()
        correct_text = question["options"].get(correct_opt, "")

        # Conversational greetings
        if any(w in msg_lower for w in ["hello", "hi kalu", "hey coach", "good morning", "good afternoon", "coach kalu"]):
            return {
                "reply": (
                    f"Hello scholar! 🎯 Coach Kalu is right here with you.\n\n"
                    f"We are looking at **{question.get('subject', 'JAMB')}**: *\"{question.get('topic', 'General')} ({question.get('subtopic', '')})\"*.\n\n"
                    f"How can I coach you through this? You can:\n"
                    f"• Ask me why a specific option is a trap (e.g. *'Why is Option A wrong?'*)\n"
                    f"• Ask for a guiding hint (*'Give me a hint'*) \n"
                    f"• Ask for a step-by-step breakdown (*'Explain how to solve this'*)"
                ),
                "revealed": False
            }

        # Gratitude & Affirmation
        if any(w in msg_lower for w in ["thank", "thanks", "i get it", "understood", "makes sense", "clever", "awesome", "got it now", "clear now"]):
            return {
                "reply": (
                    f"Fantastic! 🎉 That's the exact mindset of a 280+ JAMB scholar.\n\n"
                    f"Once you understand *why* the rule works, examiners cannot confuse you on exam day.\n\n"
                    f"👉 Select **Option {correct_opt}** or click **Next ➡️** to conquer the next question!"
                ),
                "revealed": False
            }

        # Direct answer request or surrender
        if any(w in msg_lower for w in ["give up", "tell me", "what is the answer", "surrender", "just show", "reveal", "which option is correct"]):
            return {
                "reply": (
                    f"Alright, let's break it down fully so you master it forever!\n\n"
                    f"The correct option is **{correct_opt}: {correct_text}**.\n\n"
                    f"📌 **Full Master Explanation:**\n{question['pedagogical_concept']}\n\n"
                    f"⚠️ **Why other choices were traps:**\n" +
                    "\n".join([f"• Option {k}: {v}" for k, v in question.get("traps", {}).items() if k != correct_opt]) +
                    f"\n\nNow you know how examiners design this. You will never miss it in JAMB!"
                ),
                "revealed": True,
                "correct_option": correct_opt
            }

        # Inquiring about a specific option (e.g. "why is A wrong", "is it B?", "explain option C")
        opt_match = re.search(r'\b(?:option|choice|is\s+it|why\s+not|why\s+is)?\s*([a-d])\b', msg_lower)
        if opt_match and any(w in msg_lower for w in ["why", "wrong", "trap", "option", "choice", "is it", "explain", "think", "what about"]):
            target_opt = opt_match.group(1).upper()
            if target_opt == correct_opt:
                return {
                    "reply": (
                        f"🎯 You are right on the money! **Option {target_opt}** is indeed the CORRECT answer.\n\n"
                        f"**Here is why:** {question['pedagogical_concept']}\n\n"
                        f"Go ahead and select **Option {target_opt}** on the left screen to record your score!"
                    ),
                    "revealed": True,
                    "correct_option": correct_opt
                }
            else:
                trap_explanation = question.get("traps", {}).get(
                    target_opt,
                    f"Option {target_opt} contradicts the fundamental scientific/linguistic rule for {question.get('topic', 'this topic')}."
                )
                return {
                    "reply": (
                        f"⚠️ Excellent inquiry! Here is why **Option {target_opt}** is an examiner's trap:\n\n"
                        f"**The Trap:** {trap_explanation}\n\n"
                        f"💡 **Coach Kalu's Socratic Clue:** {question['socratic_prompt']}\n\n"
                        f"Now that Option {target_opt} is eliminated, examine the remaining choices. Which one satisfies the rule?"
                    ),
                    "revealed": False
                }

        # Requesting step-by-step breakdown or formula
        if any(w in msg_lower for w in ["step by step", "how to solve", "how do i", "solve this", "formula", "working", "calculation", "break down", "teach me", "explain how"]):
            return {
                "reply": (
                    f"🧠 **Coach Kalu's Step-by-Step Breakdown:**\n\n"
                    f"**Topic:** {question.get('topic', '')} — {question.get('subtopic', '')}\n\n"
                    f"**Guiding Principle:**\n{question['pedagogical_concept']}\n\n"
                    f"💡 **Key Clue:** {question['socratic_prompt']}\n\n"
                    f"Apply this sequence to the options. Which one delivers the correct result?"
                ),
                "revealed": False
            }

        # Requesting a hint or clue
        if any(w in msg_lower for w in ["hint", "clue", "help", "guide", "confused", "lost", "where do i start", "assist"]):
            return {
                "reply": (
                    f"💡 **Coach Kalu's Guiding Hint:**\n\n"
                    f"{question['socratic_prompt']}\n\n"
                    f"🔍 **Look closely at:** \"{question['question']}\"\n\n"
                    f"Can you eliminate the two options that obviously violate this condition?"
                ),
                "revealed": False
            }

        # Contextual subject-specific keyword matching
        if question["subject"] == "Physics" and ("kelvin" in msg_lower or any(k in msg_lower for k in ["300", "400", "273"])):
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

        # If student asked an open academic question or greeting during this CBT question
        gen_res = self.general_academic_reply(user_message)
        if gen_res.get("topic") != "Academic Coaching":
            return {
                "reply": (
                    f"{gen_res['reply']}\n\n"
                    f"━━━━━━━━━━━━━━━━━━━━━\n"
                    f"📝 *Active CBT Question ({question.get('subject', 'JAMB')}):*\n"
                    f"\"{question['question']}\"\n\n"
                    f"👉 *Reply with A, B, C, or D to answer, or type NEXT to skip.*"
                ),
                "revealed": False
            }

        # Dynamic Socratic dialogue fallback
        return {
            "reply": (
                f"You are thinking in the right direction! Let's zero in:\n\n"
                f"This question tests: **{question.get('topic', 'this concept')}** ({question.get('subtopic', '')}).\n\n"
                f"💡 **Examiner's Rule:** {question['socratic_prompt']}\n\n"
                f"Options available:\n" +
                "\n".join([f"• [{k}] {v}" for k, v in question['options'].items()]) +
                f"\n\nWhich of these options directly follows this rule?"
            ),
            "revealed": False
        }

    def general_academic_reply(self, user_message):
        """
        Handles free-form academic, curriculum, or syllabus questions asked by students.
        Covers all 8 JAMB subjects and essential exam strategies.
        """
        msg_lower = (user_message or "").lower().strip()
        api_key = self.gemini_api_key or os.getenv("GEMINI_API_KEY", "")

        # If Gemini API Key is available, answer via highest model (gemini-2.5-pro)
        system_prompt = (
            "You are 'Coach Kalu', a brilliant, encouraging master Nigerian tutor specializing in JAMB & WAEC. "
            "The student is preparing for the 2026/2027 JAMB exam and asked an academic or syllabus question. "
            "Provide a direct, crystal-clear, structured explanation with rules/formulas, worked examples, and key traps to watch out for."
        )
        ai_text, model_used = self._call_gemini(f"Student Question: {user_message}", context_system=system_prompt)
        if ai_text:
            return {"reply": ai_text, "source": "gemini_live", "model": model_used, "topic": "General Academic"}

        # Identity & Bot Persona
        if any(w in msg_lower for w in ["who are you", "who is coach kalu", "what is passmaster", "tell me about yourself", "what can you do", "introduce yourself"]):
            return {
                "reply": (
                    "👋 **I am Coach Kalu**, your 24/7 Socratic AI mentor for JAMB and WAEC!\n\n"
                    "Here is how I help you score 280+:\n"
                    "• **Socratic Coaching:** I guide you step-by-step through tough questions instead of just giving away the answers.\n"
                    "• **Trap Buster:** I reveal examiner distractors across English, Math, Physics, Chemistry, Biology, Economics, Government, and Literature.\n"
                    "• **Leaky Bucket Diagnostics:** I detect topics where you're leaking marks and give targeted drills.\n"
                    "• **Masterclasses & Formulas:** Ask me to explain any law, formula, or syllabus concept anytime!\n\n"
                    "What would you like to master today, scholar?"
                ),
                "topic": "Identity"
            }

        # Warm Greetings & Social Interaction
        if any(w in msg_lower for w in ["good morning", "good afternoon", "good evening", "how are you", "how far", "whats up", "what's up", "hey coach"]):
            return {
                "reply": (
                    "Hello scholar! 🎯 Coach Kalu is right here with you and pumped to get you ready for JAMB 2026/2027.\n\n"
                    "Every question you practice and every concept you master today brings you closer to your dream admission.\n\n"
                    "How can I coach you right now? Ask me any syllabus topic, request a formula breakdown, or type `DRILL` to practice!"
                ),
                "topic": "Greeting"
            }

        # Gratitude & Affirmation
        if any(w in msg_lower for w in ["thank you", "thanks coach", "i appreciate", "you are good", "you are awesome", "well done", "nice one"]):
            return {
                "reply": (
                    "You're very welcome! 🌟 Keep that hunger for knowledge alive. Hard work plus strategic diagnosis equals 280+ in JAMB.\n\n"
                    "What concept or subject shall we conquer next?"
                ),
                "topic": "Gratitude"
            }

        # Exam Anxiety & Motivation
        if any(w in msg_lower for w in ["afraid", "scared", "nervous", "anxiety", "fail jamb", "hard exam", "too difficult", "can i pass"]):
            return {
                "reply": (
                    "Take a deep breath, champion. 💪 It is completely normal to feel nervous, but remember this:\n\n"
                    "JAMB is not an IQ test—it is a game of pattern recognition and speed. Candidates don't fail because they aren't smart; they fail because they practice without fixing their leaky topics.\n\n"
                    "With consistent 20-minute daily drills and our Socratic guidance, you WILL cross 280+.\n\n"
                    "Let's take it one question at a time. Ready to drill?"
                ),
                "topic": "Motivation"
            }

        # English Grammar & Lexis
        if any(w in msg_lower for w in ["proximity", "neither", "either", "not only"]):
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

        if any(w in msg_lower for w in ["subjunctive", "command", "insist", "decreed", "recommend", "mandate"]):
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

        if any(w in msg_lower for w in ["question tag", "tag", "isn't it", "shall we"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Question Tags:**\n\n"
                    "1. Positive statement => Negative tag: *She is coming, isn't she?*\n"
                    "2. Negative statement => Positive tag: *They didn't see us, did they?*\n"
                    "3. 'Let's' takes **shall we?**: *Let's go, shall we?*\n"
                    "4. 'I am' takes **aren't I?**: *I am right, aren't I?* (Never 'amn't I')\n"
                    "5. Negative words like *hardly, scarcely, barely, seldom* make the statement negative, so use a POSITIVE tag: *He hardly works, DOES he?*"
                ),
                "topic": "English Grammar"
            }

        if any(w in msg_lower for w in ["metaphor", "simile", "personification", "hyperbole", "oxymoron", "euphemism", "paradox", "figure of speech"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Key Figures of Speech:**\n\n"
                    "• **Simile:** Comparison using 'like' or 'as' (*He was as brave as a lion*).\n"
                    "• **Metaphor:** Direct equation asserting one thing IS another (*He is a pillar of strength*).\n"
                    "• **Personification:** Giving human traits to inanimate concepts (*The sea raged with fury*).\n"
                    "• **Hyperbole:** Deliberate exaggeration (*I've cried an ocean of tears*).\n"
                    "• **Oxymoron:** Pairing opposite words (*deafening silence, open secret*).\n"
                    "• **Paradox:** A statement seeming absurd yet true (*The child is father of the man*)."
                ),
                "topic": "Figures of Speech"
            }

        if any(w in msg_lower for w in ["stress", "syllable", "vowel sound", "diphthong", "oral english", "phonetics"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on JAMB Stress & Oral English:**\n\n"
                    "• **Noun vs Verb Stress:**\n"
                    "  - 2-syllable NOUNS stressed on **1st syllable**: **CON**duct, **IM**port, **PRO**ject, **RE**cord.\n"
                    "  - 2-syllable VERBS stressed on **2nd syllable**: con**DUCT**, im**PORT**, pro**JECT**, re**CORD**.\n"
                    "• **Suffix Stress Rules:**\n"
                    "  - Words ending in *-tion, -sion, -ic, -ical* are stressed on **penultimate (2nd to last)**: e-xam-i-**NA**-tion, dra-**MA**-tic.\n"
                    "  - Words ending in *-ate, -ise, -ify, -ity* are stressed on **antepenultimate (3rd from last)**: par-**TI**-ci-pate, elec-**TRI**-ci-ty."
                ),
                "topic": "Oral English & Stress"
            }

        # Physics
        if any(w in msg_lower for w in ["newton", "first law", "second law", "third law", "inertia", "action and reaction", "f=ma", "laws of motion"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Newton's Laws of Motion:**\n\n"
                    "• **1st Law (Law of Inertia):** A body remains at rest or uniform velocity in a straight line unless acted on by an external net force.\n"
                    "• **2nd Law (F = ma):** Net force equals the time rate of change of linear momentum (F = Δp/Δt = m(v - u)/t = ma).\n"
                    "• **3rd Law (Action & Reaction):** For every action, there is an EQUAL and OPPOSITE reaction (F_AB = -F_BA).\n\n"
                    "⚠️ **JAMB Trap:** Action and reaction forces NEVER cancel out because they act on TWO DIFFERENT bodies!"
                ),
                "topic": "Mechanics"
            }

        if any(w in msg_lower for w in ["work done", "kinetic energy", "potential energy", "conservation of energy", "mechanical energy", "joule"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Work, Energy & Power:**\n\n"
                    "• **Work (W):** W = F × d × cos θ (in Joules). If force is perpendicular to displacement (θ = 90°), Work = 0!\n"
                    "• **Kinetic Energy (K.E):** ½mv² (Double the velocity => K.E quadruples!).\n"
                    "• **Potential Energy (P.E):** mgh.\n"
                    "• **Conservation of Energy:** K.E + P.E = Constant in a closed, frictionless system.\n"
                    "• **Power (P):** Rate of work: P = W / t = F × v (in Watts)."
                ),
                "topic": "Work and Energy"
            }

        if any(w in msg_lower for w in ["ohm", "resistor", "resistance", "parallel", "series circuit", "v=ir", "voltage", "current"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Ohm's Law & Circuit Calculations:**\n\n"
                    "• **Ohm's Law:** **V = I × R** (Potential difference = Current × Resistance).\n"
                    "• **Series Resistors:** R_eq = R₁ + R₂ + R₃ (Current is identical; Voltages add up).\n"
                    "• **Parallel Resistors:** 1/R_eq = 1/R₁ + 1/R₂. For two resistors: **R_eq = (R₁ × R₂) / (R₁ + R₂)** (Voltage is identical; Currents add up).\n"
                    "• **Electric Power:** P = IV = I²R = V² / R."
                ),
                "topic": "Current Electricity"
            }

        if any(w in msg_lower for w in ["snell", "refraction", "reflection", "critical angle", "total internal reflection", "wave speed", "v = f"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Waves & Optics:**\n\n"
                    "• **Wave Equation:** **v = f × λ** (Speed = Frequency × Wavelength).\n"
                    "• **Snell's Law:** n₁ sin θ₁ = n₂ sin θ₂ => Refractive index n = c / v = Real depth / Apparent depth.\n"
                    "• **Total Internal Reflection (TIR):** Occurs only when light moves from optically DENSE to RARE medium at angle of incidence > critical angle (sin C = 1/n).\n"
                    "• **Sound Waves:** Longitudinal mechanical waves (require a material medium; cannot travel in a vacuum!)."
                ),
                "topic": "Waves and Optics"
            }

        if any(w in msg_lower for w in ["kelvin", "charles", "gas law", "boyle", "pressure law"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu's Gas Law Warning:**\n\n"
                    "In ANY gas calculation (Charles's Law: V₁/T₁ = V₂/T₂, Boyle's: P₁V₁ = P₂V₂, Combined: P₁V₁/T₁ = P₂V₂/T₂), temperature MUST ALWAYS be in **Kelvin**!\n\n"
                    "📌 Formula: **T(K) = θ(°C) + 273**\n\n"
                    "⚠️ **The Fatal Trap:** If 27°C (300 K) is heated to 127°C (400 K), the volume increases by ratio 400/300 (4/3), NOT 127/27! Never plug Celsius into gas equations!"
                ),
                "topic": "Thermal Physics"
            }

        if any(w in msg_lower for w in ["projectile", "trajectory", "maximum height", "time of flight", "range"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Projectiles & Trajectory:**\n\n"
                    "For an initial velocity u at angle θ:\n"
                    "• **Time of Flight (T):** T = (2u sin θ) / g\n"
                    "• **Maximum Height (H):** H = (u² sin² θ) / (2g)\n"
                    "• **Horizontal Range (R):** R = (u² sin 2θ) / g\n\n"
                    "⚡ **Top JAMB Secrets:**\n"
                    "1. Maximum range occurs at θ = 45° (since sin 90° = 1).\n"
                    "2. Complementary angles (e.g. 30° and 60°, 20° and 70°) give the EXACT same horizontal range!"
                ),
                "topic": "Mechanics"
            }

        if any(w in msg_lower for w in ["shm", "simple harmonic", "pendulum", "period", "acceleration"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Simple Harmonic Motion (SHM):**\n\n"
                    "• Simple Pendulum Period: **T = 2π √(L/g)** (independent of mass or amplitude!).\n"
                    "• Spring-Mass System: **T = 2π √(m/k)**.\n"
                    "• **At Equilibrium Position (center):** Velocity is MAXIMUM; Acceleration & Net Force are ZERO.\n"
                    "• **At Extreme Amplitude:** Velocity is ZERO; Acceleration & Restoring Force are MAXIMUM (a = -ω²x)."
                ),
                "topic": "Waves & Oscillations"
            }

        # Mathematics
        if any(w in msg_lower for w in ["chain rule", "derivative", "differentiate", "calculus", "dy/dx"]):
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

        if any(w in msg_lower for w in ["quadratic", "roots", "alpha", "beta", "α", "discriminant"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Quadratic Roots (α and β):**\n\n"
                    "For ax² + bx + c = 0 with roots α and β:\n"
                    "• **Sum of roots (α + β) = -b/a**\n"
                    "• **Product of roots (αβ) = c/a**\n\n"
                    "Golden Identities for JAMB:\n"
                    "• α² + β² = (α + β)² - 2αβ\n"
                    "• 1/α + 1/β = (α + β) / αβ\n"
                    "• Discriminant Δ = b² - 4ac: Real & distinct if Δ > 0; Equal if Δ = 0; Imaginary if Δ < 0."
                ),
                "topic": "Algebra"
            }

        if any(w in msg_lower for w in ["matrix", "determinant", "singular matrix"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Matrices & Determinants:**\n\n"
                    "For 2×2 matrix A = [[a, b], [c, d]]:\n"
                    "• **Determinant |A| = ad - bc**\n"
                    "• **Singular Matrix:** A matrix whose determinant is ZERO (|A| = 0). It has NO inverse!\n"
                    "⚠️ Common JAMB question: *Find x if [[2x, 4], [3, 6]] is singular.* Set (2x)(6) - (4)(3) = 0 => 12x = 12 => x = 1!"
                ),
                "topic": "Matrices"
            }

        if any(w in msg_lower for w in ["logarithm", "indices", "index", "log rule", "laws of indices"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Laws of Indices & Logarithms:**\n\n"
                    "• **Laws of Indices:**\n"
                    "  1. xᵃ × xᵇ = xᵃ⁺ᵇ | 2. xᵃ / xᵇ = xᵃ⁻ᵇ | 3. (xᵃ)ᵇ = xᵃᵇ\n"
                    "  4. x⁰ = 1 | 5. x⁻ᵃ = 1 / xᵃ | 6. x^(1/n) = ⁿ√x\n\n"
                    "• **Laws of Logarithms:**\n"
                    "  1. log(AB) = log A + log B\n"
                    "  2. log(A/B) = log A - log B\n"
                    "  3. log(Aⁿ) = n log A\n"
                    "  4. Change of Base: log_b(A) = (log_c A) / (log_c b)."
                ),
                "topic": "Logarithms and Indices"
            }

        if any(w in msg_lower for w in ["arithmetic progression", "geometric progression", "ap and gp", "sum to infinity", "progression"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on AP & GP Formulas:**\n\n"
                    "• **Arithmetic Progression (AP):**\n"
                    "  - n-th term: **Tₙ = a + (n - 1)d**\n"
                    "  - Sum: **Sₙ = (n/2)[2a + (n - 1)d] = (n/2)[a + L]**\n\n"
                    "• **Geometric Progression (GP):**\n"
                    "  - n-th term: **Tₙ = a × rⁿ⁻¹**\n"
                    "  - Sum: **Sₙ = a(1 - rⁿ) / (1 - r)**\n"
                    "  - **Sum to Infinity (S_∞):** **S_∞ = a / (1 - r)** (converges only when -1 < r < 1)."
                ),
                "topic": "Sequences and Series"
            }

        if any(w in msg_lower for w in ["trigonometry", "soh cah toa", "pythagoras", "sine rule", "cosine rule"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Trigonometry & Triangles:**\n\n"
                    "• **Right-angled Triangles (SOH CAH TOA):**\n"
                    "  - sin θ = Opp/Hyp | cos θ = Adj/Hyp | tan θ = Opp/Adj\n"
                    "  - Pythagoras Theorem: Hyp² = Opp² + Adj²\n"
                    "• **Non-right Triangles:**\n"
                    "  - **Sine Rule:** a / sin A = b / sin B = c / sin C\n"
                    "  - **Cosine Rule:** a² = b² + c² - 2bc cos A\n"
                    "• **Key Values:** sin 30° = ½, cos 60° = ½, sin 45° = 1/√2, tan 45° = 1."
                ),
                "topic": "Trigonometry"
            }

        if any(w in msg_lower for w in ["probability", "mutually exclusive", "independent event", "standard deviation"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Probability & Statistics:**\n\n"
                    "• **Probability Rule:** P(E) = (Favorable outcomes) / (Total possible outcomes) | 0 ≤ P(E) ≤ 1\n"
                    "• **Mutually Exclusive Events:** P(A or B) = P(A) + P(B)\n"
                    "• **Independent Events:** P(A and B) = P(A) × P(B)\n"
                    "• **Statistics:** Mean x̄ = Σx / N | Standard Deviation σ = √(Σ(x - x̄)² / N)."
                ),
                "topic": "Probability and Statistics"
            }

        # Chemistry
        if any(w in msg_lower for w in ["periodic table", "atomic radius", "ionization energy", "electronegativity", "electron affinity"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Periodic Trends:**\n\n"
                    "• **Across a Period (Left to Right):**\n"
                    "  - Nuclear charge increases => **Atomic Radius DECREASES**.\n"
                    "  - **Electronegativity, Ionization Energy, & Electron Affinity INCREASE**.\n"
                    "• **Down a Group (Top to Bottom):**\n"
                    "  - Extra shells added => **Atomic Radius INCREASES**.\n"
                    "  - **Electronegativity & Ionization Energy DECREASE**.\n"
                    "⚠️ **JAMB Secret:** Fluorine (F) is the MOST electronegative element; Francium (Fr) / Cesium (Cs) are most electropositive."
                ),
                "topic": "Periodic Chemistry"
            }

        if any(w in msg_lower for w in ["acid", "base", "ph scale", "neutralization", "buffer", "strong acid", "alkali"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Acids, Bases & pH Calculations:**\n\n"
                    "• **pH Formula:** **pH = -log₁₀[H⁺]** | **pOH = -log₁₀[OH⁻]** | **pH + pOH = 14** (at 25°C).\n"
                    "• **Strong Acids:** HCl, HNO₃, H₂SO₄ (dissociate completely).\n"
                    "• **Weak Acids:** CH₃COOH (ethanoic acid), H₂CO₃, H₃PO₄.\n"
                    "• **JAMB Shortcut:** If [H⁺] = 1 × 10⁻³ mol/dm³, pH = 3. If [OH⁻] = 1 × 10⁻⁴, pOH = 4 => pH = 14 - 4 = **10**!"
                ),
                "topic": "Acids and Bases"
            }

        if any(w in msg_lower for w in ["alkane", "alkene", "alkyne", "hydrocarbon", "functional group", "iupac", "isomer"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Hydrocarbons & Functional Groups:**\n\n"
                    "• **Alkanes (CₙH₂ₙ₊₂):** Saturated, undergo substitution (e.g. halogenation under sunlight).\n"
                    "• **Alkenes (CₙH₂ₙ):** Unsaturated (C=C), undergo addition, decolorize reddish-brown bromine water.\n"
                    "• **Alkynes (CₙH₂ₙ₋₂):** Triple bond (C≡C). Terminal alkynes give precipitates with ammoniacal AgNO₃.\n"
                    "• **Key Functional Groups:** Alkanols (-OH), Alkanals (-CHO), Alkanones (>C=O), Alkanoic acids (-COOH), Esters (-COO-)."
                ),
                "topic": "Organic Chemistry"
            }

        if any(w in msg_lower for w in ["redox", "oxidation number", "oil rig", "reducing agent", "oxidizing agent", "faraday", "electrolysis"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Redox & Electrochemistry:**\n\n"
                    "• **OIL RIG:** **O**xidation **I**s **L**oss of electrons (increase in oxidation number); **R**eduction **I**s **G**ain (decrease in oxidation number).\n"
                    "• **Oxidizing Agent:** Electron acceptor (is itself reduced).\n"
                    "• **Reducing Agent:** Electron donor (is itself oxidized).\n"
                    "• **Faraday's 1st Law:** **m = ZIt = (M × I × t) / (n × F)** (F = 96,500 C/mol)."
                ),
                "topic": "Redox and Electrochemistry"
            }

        if any(w in msg_lower for w in ["stoichiometry", "mole", "avogadro", "molar mass"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Stoichiometry & The Mole:**\n\n"
                    "• **Moles (n) = Mass (g) / Molar Mass (g/mol)**\n"
                    "• **Moles for gases at s.t.p = Volume (dm³) / 22.4 dm³**\n"
                    "• **Concentration (mol/dm³) = Moles / Volume (dm³)**\n"
                    "• **Avogadro's Number = 6.02 × 10²³ particles/mol**\n\n"
                    "Remember: 1 dm³ = 1000 cm³. Always convert cm³ to dm³ by dividing by 1000 before calculating molarity!"
                ),
                "topic": "Physical Chemistry"
            }

        if any(w in msg_lower for w in ["le chatelier", "equilibrium", "catalyst", "exothermic"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Le Chatelier's Principle:**\n\n"
                    "If a dynamic equilibrium is disturbed, the position of equilibrium moves to counteract the disturbance:\n"
                    "• **Temperature:** Increasing temperature favors the ENDOTHERMIC direction (+ΔH); decreasing favors EXOTHERMIC (-ΔH).\n"
                    "• **Pressure:** Increasing pressure shifts equilibrium toward the side with FEWER gas moles.\n"
                    "• **Catalyst:** Speeds up BOTH forward and reverse reactions equally. It does NOT change equilibrium position or yield!"
                ),
                "topic": "Chemical Equilibrium"
            }

        # Biology
        if any(w in msg_lower for w in ["photosynthesis", "chloroplast", "chlorophyll", "aerobic", "anaerobic", "glycolysis", "atp", "respiration"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Photosynthesis vs Cellular Respiration:**\n\n"
                    "• **Photosynthesis:** 6CO₂ + 6H₂O + light -> C₆H₁₂O₆ + 6O₂.\n"
                    "  - **Light Phase (Granum/Thylakoid):** Photolysis of water generates ATP, NADPH, and O₂ gas.\n"
                    "  - **Dark Phase / Calvin Cycle (Stroma):** Fixes CO₂ into glucose.\n"
                    "• **Cellular Respiration:** C₆H₁₂O₆ + 6O₂ -> 6CO₂ + 6H₂O + 38 ATP.\n"
                    "  - Glycolysis in **Cytoplasm** (anaerobic); Krebs Cycle in **Mitochondria** (aerobic)."
                ),
                "topic": "Bioenergetics"
            }

        if any(w in msg_lower for w in ["mitosis", "meiosis", "chromosome", "diploid", "haploid", "crossing over", "cell division"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Mitosis vs Meiosis:**\n\n"
                    "• **Mitosis:** 1 division => **2 identical diploid (2n)** daughter cells. For somatic growth and repair.\n"
                    "• **Meiosis:** 2 divisions => **4 genetically varied haploid (n)** gametes. For sexual reproduction.\n"
                    "• **Crossing Over:** Occurs in **Prophase I (Pachytene)** between non-sister chromatids, driving genetic variation."
                ),
                "topic": "Cell Division"
            }

        if any(w in msg_lower for w in ["circulatory", "heart", "artery", "arteries", "vein", "veins", "xylem", "phloem"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Animal & Plant Transport Systems:**\n\n"
                    "• **Arteries:** Thick muscular walls, narrow lumen, high pressure, carry blood AWAY from heart (Pulmonary artery carries deoxygenated blood).\n"
                    "• **Veins:** Thin walls, wide lumen, have **VALVES** to prevent backflow, carry blood TOWARD heart (Pulmonary vein carries oxygenated blood).\n"
                    "• **Plants:** **Xylem** transports water/minerals upward; **Phloem** translocates sugars/amino acids bidirectionally."
                ),
                "topic": "Transport Systems"
            }

        if any(w in msg_lower for w in ["osmosis", "plasmolysis", "turgid", "flaccid", "crenation"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Osmosis & Plasmolysis:**\n\n"
                    "• **Hypotonic Solution (Dilute/pure water):** Water enters cell => Plant cell becomes **TURGID**; Animal cell swells and undergoes **LYSIS (bursts)**.\n"
                    "• **Hypertonic Solution (Concentrated salt/sugar):** Water leaves cell => Plant protoplasm shrinks away from cell wall (**PLASMOLYSIS**); Animal cell shrinks (**CRENATION**).\n"
                    "• Plant cells don't burst because they possess a rigid cellulose cell wall!"
                ),
                "topic": "Cell Biology"
            }

        if any(w in msg_lower for w in ["genetics", "mendel", "allele", "blood group", "rhesus"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Genetics & Blood Groups:**\n\n"
                    "• Blood Group Alleles: Iᴬ and Iᴮ are CO-DOMINANT; both dominate over i (recessive).\n"
                    "• Group A: IᴬIᴬ or Iᴬi | Group B: IᴮIᴮ or Iᴮi | Group AB: IᴬIᴮ | Group O: ii\n"
                    "• **Universal Donor:** O Negative (no A/B antigens & no Rh antigen).\n"
                    "• **Universal Recipient:** AB Positive (possesses all antigens, produces no antibodies)."
                ),
                "topic": "Genetics"
            }

        # Economics
        if any(w in msg_lower for w in ["demand and supply", "law of demand", "shift in demand", "equilibrium price", "price ceiling", "price floor"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Demand & Supply Mechanics:**\n\n"
                    "• **Law of Demand:** Price and quantity demanded move in OPPOSITE directions.\n"
                    "• **Change in Quantity Demanded (Movement):** Caused ONLY by commodity's own price change.\n"
                    "• **Change in Demand (Shift):** Caused by income, tastes, population, or substitutes/complements.\n"
                    "• **Price Ceiling:** Set BELOW equilibrium => creates **Shortage / Scarcity**.\n"
                    "• **Price Floor:** Set ABOVE equilibrium (e.g. minimum wage) => creates **Surplus**."
                ),
                "topic": "Price Theory"
            }

        if any(w in msg_lower for w in ["elasticity", "ped", "inelastic", "unitary"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Price Elasticity of Demand (PED):**\n\n"
                    "📌 **PED = (% Change in Quantity Demanded) / (% Change in Price)**\n\n"
                    "• **|PED| > 1 (Elastic):** Quantity changes by a larger % than price. Total Revenue rises if price is reduced.\n"
                    "• **|PED| < 1 (Inelastic):** Necessities (salt, fuel). Total Revenue rises if price is increased.\n"
                    "• **|PED| = 1 (Unitary):** Total Revenue remains constant when price changes."
                ),
                "topic": "Economics"
            }

        if any(w in msg_lower for w in ["gdp", "gnp", "national income", "nni"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on National Income Accounting:**\n\n"
                    "• **GDP (Gross Domestic Product):** Total output produced WITHIN the borders of Nigeria, regardless of citizenship.\n"
                    "• **GNP = GDP + Net Property Income from Abroad (NPIA)** (Output by Nigerian nationals globally minus foreigners in Nigeria).\n"
                    "• **NNP = GNP - Depreciation (Capital Consumption Allowance)**.\n"
                    "• Expenditure Approach: **Y = C + I + G + (X - M)**."
                ),
                "topic": "National Income"
            }

        # Government
        if any(w in msg_lower for w in ["rule of law", "separation of powers", "checks and balances", "dicey", "montesquieu"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Rule of Law & Separation of Powers:**\n\n"
                    "• **Rule of Law (A.V. Dicey):** Supremacy of law, equality before the law, and protection of fundamental human rights.\n"
                    "• **Separation of Powers (Montesquieu):** Distinct division into **Legislature** (makes law), **Executive** (enforces law), and **Judiciary** (interprets law).\n"
                    "• **Checks and Balances:** Prevents tyranny by giving each arm constitutional powers to check abuses in the other two."
                ),
                "topic": "Constitutional Law"
            }

        if any(w in msg_lower for w in ["constitution", "1963", "1979", "1999", "lugard", "indirect rule", "clifford"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Nigerian Government & History:**\n\n"
                    "• **1922 Clifford Constitution:** Introduced the Elective Principle (4 elected seats: 3 Lagos, 1 Calabar).\n"
                    "• **1946 Richards Constitution:** Introduced Regionalism (North, West, East).\n"
                    "• **1954 Lyttelton Constitution:** Established true Federalism in Nigeria and autonomy for regions.\n"
                    "• **1963 Republican Constitution:** Severed last ties to the British Crown. Queen ceased to be Head of State and Supreme Court became final appellate court.\n"
                    "• **1979 Constitution:** Replaced British Parliamentary system with American Executive Presidential system."
                ),
                "topic": "Nigerian Government"
            }

        # Literature in English
        if any(w in msg_lower for w in ["irony", "catharsis", "soliloquy", "metonymy", "synecdoche", "apostrophe"]):
            return {
                "reply": (
                    "🧠 **Coach Kalu on Literary Devices:**\n\n"
                    "• **Dramatic Irony:** The audience knows vital truth that characters on stage are oblivious to.\n"
                    "• **Catharsis:** The emotional purging/cleansing of pity and fear felt by the audience at tragic catastrophe.\n"
                    "• **Soliloquy:** A character speaking alone on stage revealing innermost thoughts.\n"
                    "• **Metonymy:** Substituting an object with an associated attribute ('The pen is mightier than the sword').\n"
                    "• **Synecdoche:** A part representing the whole ('All hands on deck')."
                ),
                "topic": "Literature Devices"
            }

        # JAMB Exam Strategy
        if any(w in msg_lower for w in ["280", "score", "pass", "jamb tip", "how to prepare", "strategy"]):
            return {
                "reply": (
                    "🎯 **Coach Kalu's Blueprint to 280+ in JAMB 2026/2027:**\n\n"
                    "1. **Stop Memorizing, Start Diagnosing:** 76% of candidates fail because they memorize past answers without understanding distractor traps.\n"
                    "2. **Eliminate Your Leaky Topics:** Check our Leaky Bucket tab to diagnose exactly where your marks are leaking.\n"
                    "3. **Target 40 Seconds per Question:** 180 questions in 120 minutes means you must never get stuck on any single question for over 60 seconds.\n"
                    "4. **Study Topic Masterclasses:** Review the 32 syllabus masterclasses right here in PassMaster AI to master core concepts from scratch."
                ),
                "topic": "JAMB Strategy"
            }

        # Warm conversational fallback
        return {
            "reply": (
                f"Great question! As Coach Kalu, I am here to help you conquer every angle of your SS3 syllabus and JAMB 2026/2027.\n\n"
                f"You asked about: *\"{user_message}\"*\n\n"
                f"To give you the sharpest breakdown, tell me the specific subject (Use of English, Math, Physics, Chemistry, Biology, Economics, Government, Literature) or ask me to explain a concept or formula!"
            ),
            "topic": "Academic Coaching"
        }
