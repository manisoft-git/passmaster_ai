import json
import os
import requests
from engine.socratic_tutor import SocraticTutor
from engine.diagnostics import DiagnosticEngine
from payments.payment_service import PaymentService

class WhatsAppBot:
    def __init__(self, tutor: SocraticTutor, diagnostics: DiagnosticEngine, payments: PaymentService):
        self.tutor = tutor
        self.diagnostics = diagnostics
        self.payments = payments
        # State: { phone_number: { "state": "MENU", "subject": None, "current_q": None, "history": {} } }
        self.sessions = {}

    def send_cloud_api_message(self, recipient_phone, message_text):
        token = os.getenv("WHATSAPP_TOKEN", "")
        phone_id = os.getenv("WHATSAPP_PHONE_NUMBER_ID", "")
        if not token or not phone_id or "replace_with" in token or "replace_with" in phone_id:
            return {"status": "simulated", "recipient": recipient_phone}
        
        url = f"https://graph.facebook.com/v19.0/{phone_id}/messages"
        headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }
        payload = {
            "messaging_product": "whatsapp",
            "to": recipient_phone,
            "type": "text",
            "text": {"body": message_text}
        }
        try:
            res = requests.post(url, json=payload, headers=headers, timeout=8)
            return res.json()
        except Exception as e:
            print(f"Failed to dispatch WhatsApp Cloud message: {e}")
            return {"error": str(e)}

    def get_session(self, phone):
        if phone not in self.sessions:
            self.sessions[phone] = {
                "state": "MENU",
                "subject": "Use of English",
                "current_q": None,
                "history": {},
                "name": "Candidate"
            }
        return self.sessions[phone]

    def handle_incoming_message(self, phone, raw_text):
        """
        Processes incoming WhatsApp message and returns the bot's response text.
        """
        text = raw_text.strip()
        msg_upper = text.upper()
        session = self.get_session(phone)

        # Global command: MENU / RESET / START
        if msg_upper in ["MENU", "START", "HI", "HELLO", "HELP"]:
            session["state"] = "MENU"
            session["current_q"] = None
            return (
                "👋 *Welcome to PassMaster AI Coach!*\n"
                "The #1 Socratic Exam Tutor for JAMB & WAEC.\n\n"
                "Reply with a number:\n"
                "1️⃣ *Practice Questions* (English, Math, Physics, Chem, Bio)\n"
                "2️⃣ *Check My Predicted Score* (out of 400)\n"
                "3️⃣ *Leaky Bucket Diagnostic* (Find marks you are losing)\n"
                "4️⃣ *Activate Full AI Pass* (from ₦700/week)\n\n"
                "💡 *Or type a subject directly:* `ENG`, `MATH`, `PHY`, `CHM`, `BIO`"
            )

        # Global command: SCORE
        if msg_upper in ["2", "SCORE", "MY SCORE"]:
            score_data = self.diagnostics.calculate_predicted_score(session["history"])
            leaks = self.diagnostics.get_leaky_bucket_analysis(session["history"])
            card = self.diagnostics.generate_whatsapp_status_card(
                session["name"], "Medicine & Surgery", "UNILAG", score_data, leaks
            )
            return f"{card}\n\n*Type MENU to return or DRILL to fix weak topics!*"

        # Global command: LEAKS
        if msg_upper in ["3", "LEAKS", "LEAKY BUCKET"]:
            leaks = self.diagnostics.get_leaky_bucket_analysis(session["history"])
            if not leaks:
                return (
                    "📊 *No Leaky Topics Detected Yet!*\n"
                    "Practice at least 3 questions first so our AI can detect your weak spots.\n"
                    "Type `ENG` or `MATH` to start now!"
                )
            top = leaks[0]
            return (
                f"🚨 *TOP LEAKY TOPIC IDENTIFIED*\n\n"
                f"📚 Subject: *{top['subject']}*\n"
                f"🔍 Topic: *{top['topic']}* ({top['subtopic']})\n"
                f"📉 Accuracy: {top['accuracy_pct']}%\n"
                f"⚠️ Estimated Marks Lost in JAMB: *{top['estimated_mark_loss']} marks*\n\n"
                f"💡 *Key Rule to Review:* {top['pedagogical_concept']}\n\n"
                f"Type `DRILL` to practice questions on this topic right now!"
            )

        # Global command: BUY / UPGRADE
        if msg_upper in ["4", "BUY", "PLANS", "PRICING"]:
            return (
                "💳 *PASSMASTER AI SUBSCRIPTION PLANS*\n\n"
                "1. *Weekly Drill Pass* — ₦1,500 (7 days unlimited coaching)\n"
                "2. *Monthly Master Pass* — ₦3,500 (30 days + full mock exams)\n"
                "3. *Full Season Pass* — ₦8,500 (valid until JAMB day)\n\n"
                "To activate instantly, reply:\n"
                "`PAY WEEKLY` or `PAY MONTHLY`\n"
                "Or redeem a voucher PIN: `PIN <YOUR-CODE>`"
            )

        if msg_upper.startswith("PIN "):
            pin_code = text[4:].strip()
            res = self.payments.redeem_voucher(pin_code, phone)
            if "error" in res:
                return f"❌ {res['error']}"
            return f"{res['message']}\n\nType `START` to start practicing!"

        if msg_upper in ["PAY WEEKLY", "PAY MONTHLY", "PAY SEASON"]:
            plan = msg_upper.split()[1].lower()
            res = self.payments.initiate_payment(f"{phone}@passmaster.ng", phone, plan)
            va = res["virtual_account"]
            return (
                f"🏦 *INSTANT PAYMENT DETAILS*\n\n"
                f"Plan: *{res['plan_name']}*\n"
                f"Amount: *₦{res['amount_ngn']:,}*\n"
                f"Bank: *{va['bank_name']}*\n"
                f"Account No: *{va['account_number']}*\n"
                f"Account Name: *{va['account_name']}*\n\n"
                f"⏰ Transfer within 30 minutes for instant automated activation!"
            )

        # Handle Subject Selection
        subject_map = {
            "1": "Use of English",
            "ENG": "Use of English",
            "ENGLISH": "Use of English",
            "MATH": "Mathematics",
            "MATHEMATICS": "Mathematics",
            "PHY": "Physics",
            "PHYSICS": "Physics",
            "CHM": "Chemistry",
            "CHEMISTRY": "Chemistry",
            "BIO": "Biology",
            "BIOLOGY": "Biology",
            "ECO": "Economics",
            "ECONOMICS": "Economics",
            "GOV": "Government",
            "GOVERNMENT": "Government",
            "LIT": "Literature in English",
            "LITERATURE": "Literature in English"
        }

        if msg_upper in subject_map:
            session["subject"] = subject_map[msg_upper]
            return self._serve_next_question(session)

        # If currently answering a question
        if session.get("current_q"):
            q_id = session["current_q"]
            # Check if user picked an option A, B, C, D
            if msg_upper in ["A", "B", "C", "D"]:
                result = self.tutor.analyze_attempt(q_id, msg_upper)
                # Record to history
                session["history"][q_id] = {
                    "selected": msg_upper,
                    "is_correct": result["is_correct"],
                    "time_seconds": 35
                }

                if result["is_correct"]:
                    session["current_q"] = None
                    return (
                        f"{result['message']}\n\n"
                        f"━━━━━━━━━━━━━━━━━━━━━\n"
                        f"Type `NEXT` for another question, or `MENU` to view options."
                    )
                else:
                    return f"{result['message']}"
            else:
                # Student is asking a question or responding Socratically to Coach Kalu!
                chat_res = self.tutor.chat_reply(q_id, text)
                reply_text = chat_res["reply"]
                if chat_res.get("revealed"):
                    session["current_q"] = None
                    reply_text += "\n\n━━━━━━━━━━━━━━━━━━━━━\nType `NEXT` for the next question!"
                return reply_text

        if msg_upper in ["NEXT", "DRILL"]:
            return self._serve_next_question(session)

        # Fallback
        return (
            "🤔 I didn't quite catch that. "
            "Reply with `A`, `B`, `C`, or `D` to answer the question, or type `MENU` to see main options."
        )

    def _serve_next_question(self, session):
        subj = session.get("subject", "Use of English")
        # Find an unattempted question in this subject
        candidates = [q for q in self.tutor.questions.values() if q["subject"].lower() == subj.lower()]
        if not candidates:
            candidates = list(self.tutor.questions.values())

        # Pick one that wasn't correctly answered yet
        unanswered = [q for q in candidates if not session["history"].get(q["id"], {}).get("is_correct")]
        q = unanswered[0] if unanswered else candidates[0]

        session["current_q"] = q["id"]
        session["state"] = "QUESTION"

        opts_text = "\n".join([f"*{k}*) {v}" for k, v in q["options"].items()])
        return (
            f"📝 *[{q['subject']} - {q['year']}]*\n"
            f"Topic: _{q['topic']} ({q['subtopic']})_\n\n"
            f"{q['question']}\n\n"
            f"{opts_text}\n\n"
            f"👉 *Reply with A, B, C, or D:*"
        )
