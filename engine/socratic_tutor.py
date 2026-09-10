import json
import os
import re
import random
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

        api_key = self.gemini_api_key or os.getenv("GEMINI_API_KEY", "")
        # If Gemini API Key is available, attempt live LLM call for question
        if api_key:
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

                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
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

        # If Gemini API Key is available, answer via LLM
        if api_key:
            try:
                prompt = (
                    "You are 'Coach Kalu', a brilliant, encouraging master Nigerian tutor specializing in JAMB & WAEC. "
                    "The student is preparing for the 2026/2027 JAMB exam and asked an academic or syllabus question. "
                    "Provide a direct, crystal-clear, structured explanation with rules/formulas, worked examples, and key traps to watch out for. "
                    f"Student Question: {user_message}"
                )
                url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={api_key}"
                payload = {"contents": [{"role": "user", "parts": [{"text": prompt}]}]}
                res = requests.post(url, json=payload, timeout=8)
                if res.status_code == 200:
                    data = res.json()
                    ai_text = data["candidates"][0]["content"]["parts"][0]["text"]
                    return {"reply": ai_text, "source": "gemini_live", "topic": "General Academic"}
            except Exception as ex:
                print(f"LLM general chat fallback: {ex}")

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

        # Physics
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

        # Chemistry
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
