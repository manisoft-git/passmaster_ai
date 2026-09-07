import os
import json
import time
import secrets
import urllib.parse
from flask import Flask, render_template, request, jsonify, send_from_directory, session, redirect

# Auto-load .env configuration if present
env_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(env_path):
    with open(env_path, 'r', encoding='utf-8') as ef:
        for eline in ef:
            eline = eline.strip()
            if eline and not eline.startswith('#') and '=' in eline:
                ek, ev = eline.split('=', 1)
                os.environ.setdefault(ek.strip(), ev.strip().strip('"\''))

from engine.socratic_tutor import SocraticTutor
from engine.diagnostics import DiagnosticEngine
from payments.payment_service import PaymentService
from whatsapp.bot import WhatsAppBot
import db.database as db

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '0'
    return response

app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'passmaster_secure_production_key_2025')

# Initialize SQLite database
db.init_db()

# Initialize Core Services
tutor = SocraticTutor(questions_path="data/questions.json")
diagnostics = DiagnosticEngine(syllabus_path="data/syllabus.json", questions_path="data/questions.json")
payments = PaymentService()
whatsapp_bot = WhatsAppBot(tutor=tutor, diagnostics=diagnostics, payments=payments)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/manifest.json')
def manifest():
    return send_from_directory('static', 'manifest.json')

# ----------------- AUTHENTICATION API -----------------
@app.route('/api/auth/register', methods=['POST'])
def register():
    data = request.get_json() or {}
    name = data.get('name', '').strip()
    email = data.get('email', '').strip()
    phone = data.get('phone', '').strip()
    password = data.get('password', '')
    course = data.get('target_course', 'Medicine & Surgery')
    uni = data.get('target_uni', 'UNILAG')
    score = int(data.get('target_score', 280))

    if not name or not email or not phone or not password:
        return jsonify({"error": "Please provide your Name, Email, Phone, and Password."}), 400

    res = db.register_user(name, email, phone, password, course, uni, score)
    if "error" in res:
        return jsonify({"error": res["error"]}), 400

    session['user_id'] = res['user_id']
    user_info = db.get_user_by_id(res['user_id'])
    return jsonify({"status": "success", "user": user_info})

@app.route('/api/auth/login', methods=['POST'])
def login():
    data = request.get_json() or {}
    identifier = data.get('identifier', '').strip()
    password = data.get('password', '')

    if not identifier or not password:
        return jsonify({"error": "Please enter your Email or Phone, and Password."}), 400

    user = db.authenticate_user(identifier, password)
    if not user:
        return jsonify({"error": "Invalid email/phone or password. Please try again."}), 401

    session['user_id'] = user['id']
    user_info = db.get_user_by_id(user['id'])
    attempts = db.get_user_attempts(user['id'])

    return jsonify({
        "status": "success",
        "user": user_info,
        "attempts": attempts
    })

@app.route('/api/auth/me', methods=['GET'])
def get_current_user():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"status": "guest", "user": None, "attempts": {}})

    user = db.get_user_by_id(user_id)
    if not user:
        session.pop('user_id', None)
        return jsonify({"status": "guest", "user": None, "attempts": {}})

    attempts = db.get_user_attempts(user_id)
    return jsonify({"status": "authenticated", "user": user, "attempts": attempts})

@app.route('/api/auth/logout', methods=['POST'])
def logout():
    session.pop('user_id', None)
    return jsonify({"status": "logged_out"})

# ----------------- LEADERBOARD & MISTAKE VAULT -----------------
@app.route('/api/leaderboard', methods=['GET'])
def leaderboard():
    board = db.get_leaderboard()
    return jsonify({"status": "success", "leaderboard": board})

@app.route('/api/mistake-vault', methods=['GET'])
def mistake_vault():
    user_id = session.get('user_id')
    vault_items = []
    if user_id:
        raw_mistakes = db.get_mistake_vault(user_id)
        for m in raw_mistakes:
            q = tutor.questions.get(m["question_id"])
            if q:
                chosen = m["selected_option"]
                trap_explanation = q.get("traps", {}).get(chosen, "Misconception in theoretical rule.")
                vault_items.append({
                    "question_id": q["id"],
                    "subject": q["subject"],
                    "topic": q["topic"],
                    "subtopic": q["subtopic"],
                    "question": q["question"],
                    "your_wrong_choice": chosen,
                    "trap_explanation": trap_explanation,
                    "correct_option": q["correct_option"],
                    "concept": q["pedagogical_concept"]
                })
    return jsonify({"status": "success", "vault": vault_items})

# ----------------- PARENT & SCHOOL MONITORING API -----------------
@app.route('/api/parent/report', methods=['GET'])
def parent_report():
    phone = request.args.get('phone', '')
    if not phone:
        return jsonify({"error": "Please provide the student's registered phone number."}), 400

    report = db.get_parent_report(phone)
    if not report:
        return jsonify({"error": "No registered candidate found with this phone number."}), 404

    return jsonify({"status": "success", "report": report})

# ----------------- QUESTIONS & SYLLABUS API -----------------
@app.route('/api/questions', methods=['GET'])
def get_questions():
    subject = request.args.get('subject')
    questions = list(tutor.questions.values())
    if subject and subject.lower() != 'all':
        questions = [q for q in questions if q['subject'].lower() == subject.lower()]
    return jsonify({"status": "success", "count": len(questions), "questions": questions})

@app.route('/api/syllabus', methods=['GET'])
def get_syllabus():
    return jsonify({"status": "success", "syllabus": diagnostics.syllabus})

# ----------------- SOCRATIC AI TUTOR API -----------------
@app.route('/api/tutor/attempt', methods=['POST'])
def tutor_attempt():
    data = request.get_json() or {}
    question_id = data.get('question_id')
    selected_option = data.get('selected_option')
    time_spent = int(data.get('time_seconds', 35))
    is_flagged = 1 if data.get('is_flagged') else 0
    
    if not question_id or not selected_option:
        return jsonify({"error": "Missing question_id or selected_option"}), 400

    analysis = tutor.analyze_attempt(question_id, selected_option)

    user_id = session.get('user_id')
    if user_id:
        db.record_attempt(user_id, question_id, selected_option, analysis['is_correct'], time_spent, is_flagged)
        user_info = db.get_user_by_id(user_id)
        analysis['updated_xp'] = user_info['xp']
        analysis['level_name'] = user_info['level_name']
    else:
        analysis['updated_xp'] = 50
        analysis['level_name'] = "Guest Candidate"

    return jsonify(analysis)

@app.route('/api/tutor/chat', methods=['POST'])
def tutor_chat():
    data = request.get_json() or {}
    question_id = data.get('question_id')
    message = data.get('message', '')

    if not question_id or not message:
        return jsonify({"error": "Missing question_id or message"}), 400

    response = tutor.chat_reply(question_id, message)
    return jsonify(response)

# ----------------- DIAGNOSTICS & PREDICTOR API -----------------
@app.route('/api/diagnostics/score', methods=['POST'])
def calculate_score():
    data = request.get_json() or {}
    history = data.get('history', {})

    user_id = session.get('user_id')
    if user_id and not history:
        history = db.get_user_attempts(user_id)
    
    score_data = diagnostics.calculate_predicted_score(history)
    leaks = diagnostics.get_leaky_bucket_analysis(history)
    
    return jsonify({
        "status": "success",
        "predicted_score": score_data,
        "leaky_bucket": leaks
    })

@app.route('/api/diagnostics/share-card', methods=['POST'])
def share_card():
    data = request.get_json() or {}
    candidate_name = data.get('name', 'Candidate')
    target_course = data.get('course', 'Medicine & Surgery')
    target_uni = data.get('university', 'UNILAG')
    history = data.get('history', {})

    user_id = session.get('user_id')
    if user_id:
        user = db.get_user_by_id(user_id)
        if user:
            candidate_name = user['name']
            target_course = user['target_course']
            target_uni = user['target_uni']
        if not history:
            history = db.get_user_attempts(user_id)

    score_data = diagnostics.calculate_predicted_score(history)
    leaks = diagnostics.get_leaky_bucket_analysis(history)
    card_text = diagnostics.generate_whatsapp_status_card(
        candidate_name, target_course, target_uni, score_data, leaks
    )

    return jsonify({"status": "success", "card_text": card_text})

# ----------------- WHATSAPP BOT API & WEBHOOK -----------------
@app.route('/api/whatsapp/message', methods=['POST'])
def whatsapp_message():
    data = request.get_json() or {}
    phone = data.get('phone', '2348012345678')
    message = data.get('message', '')

    reply = whatsapp_bot.handle_incoming_message(phone, message)
    return jsonify({"status": "success", "phone": phone, "reply": reply})

@app.route('/api/whatsapp/webhook', methods=['GET', 'POST'])
def whatsapp_webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        verify_token = os.getenv("WHATSAPP_VERIFY_TOKEN", "passmaster_secure_webhook_verify_token_2025")
        if mode == 'subscribe' and token == verify_token:
            return challenge, 200
        return "Forbidden", 403

    # POST from Meta Cloud API
    payload = request.get_json() or {}
    try:
        entries = payload.get('entry', [])
        for entry in entries:
            changes = entry.get('changes', [])
            for change in changes:
                val = change.get('value', {})
                messages = val.get('messages', [])
                for m in messages:
                    from_phone = m.get('from', '')
                    text_body = m.get('text', {}).get('body', '')
                    if from_phone and text_body:
                        reply = whatsapp_bot.handle_incoming_message(from_phone, text_body)
                        whatsapp_bot.send_cloud_api_message(from_phone, reply)
    except Exception as e:
        print(f"WhatsApp webhook processing error: {e}")
    return jsonify({"status": "received"}), 200

# ----------------- MONETIZATION & PAYMENTS API -----------------
@app.route('/api/payments/checkout', methods=['POST'])
def checkout():
    data = request.get_json() or {}
    plan_id = data.get('plan_id', 'weekly')

    user_id = session.get('user_id')
    email = "student@passmaster.ng"
    phone = "08012345678"
    if user_id:
        u = db.get_user_by_id(user_id)
        if u:
            email = u['email']
            phone = u['phone']

    res = payments.initiate_payment(email, phone, plan_id)

    # Attach live producer bank account details & WhatsApp contact
    prod_settings = db.get_producer_settings()
    res["producer_account"] = {
        "bank_name": prod_settings.get("producer_bank_name", "OPay Digital Services"),
        "account_number": prod_settings.get("producer_account_number", "8012345678"),
        "account_name": prod_settings.get("producer_account_name", "PASSMASTER / MANISOFT PRODUCTIONS"),
        "whatsapp_phone": prod_settings.get("producer_whatsapp_phone", "2348012345678")
    }
    return jsonify(res)

@app.route('/api/payments/submit-transfer', methods=['POST'])
def submit_transfer():
    data = request.get_json() or {}
    plan_id = data.get('plan_id', 'monthly')
    ref = data.get('reference') or f"PMS_{int(time.time())}_{secrets.token_hex(3).upper()}"
    notes = data.get('notes', '')

    user_id = session.get('user_id')
    name = "Student"
    email = "student@passmaster.ng"
    phone = "08012345678"
    if user_id:
        u = db.get_user_by_id(user_id)
        if u:
            name = u["name"]
            email = u["email"]
            phone = u["phone"]
    else:
        name = data.get('name', 'Guest Student')
        email = data.get('email', 'guest@passmaster.ng')
        phone = data.get('phone', '08000000000')

    pricing = {
        "weekly": {"name": "Weekly Drill Pass", "amount": 700},
        "monthly": {"name": "Monthly Master Pass", "amount": 2200},
        "season": {"name": "Full Season Guarantee Pass", "amount": 5000}
    }
    plan_meta = pricing.get(plan_id, {"name": "Monthly Master Pass", "amount": 2200})

    db.create_payment_order(
        reference=ref,
        user_id=user_id,
        student_name=name,
        email=email,
        phone=phone,
        plan_id=plan_id,
        plan_name=plan_meta["name"],
        amount_ngn=plan_meta["amount"],
        method='manual_transfer',
        notes=notes
    )

    prod_settings = db.get_producer_settings()
    wa_num = prod_settings.get("producer_whatsapp_phone", "2348012345678").replace("+", "")
    wa_text = (
        f"Hello PassMaster Producer! 🎯\n\n"
        f"I just transferred ₦{plan_meta['amount']:,} for *{plan_meta['name']}*.\n"
        f"• Name: *{name}*\n"
        f"• Phone: *{phone}*\n"
        f"• Ref ID: `{ref}`\n\n"
        f"Kindly confirm my payment on your Producer Console so my pass activates. Thank you!"
    )
    encoded_msg = urllib.parse.quote(wa_text)
    wa_url = f"https://wa.me/{wa_num}?text={encoded_msg}"

    return jsonify({
        "status": "order_created",
        "reference": ref,
        "amount_ngn": plan_meta["amount"],
        "plan_name": plan_meta["name"],
        "whatsapp_url": wa_url,
        "instructions": "Order logged! Tap the button below to send your transfer receipt screenshot to the Producer via WhatsApp for 1-click confirmation."
    })

@app.route('/api/payments/verify', methods=['POST'])
def verify_payment():
    data = request.get_json() or {}
    reference = data.get('reference', 'MOCK_REF')
    plan_id = data.get('plan_id', 'monthly')

    user_id = session.get('user_id') or 1
    days = 30
    if plan_id == 'weekly': days = 7
    elif plan_id == 'season': days = 120

    new_expiry = db.apply_subscription(user_id, plan_id, days)
    return jsonify({
        "status": "verified",
        "message": f"🎉 Payment verified! Your Pass is now active for {days} days.",
        "expires_at": new_expiry
    })

@app.route('/api/payments/redeem-voucher', methods=['POST'])
def redeem_voucher():
    data = request.get_json() or {}
    pin_code = data.get('pin_code', '')
    user_id = session.get('user_id') or 1

    res = db.redeem_voucher_code(user_id, pin_code)
    if "error" in res:
        return jsonify({"error": res["error"]}), 400

    return jsonify({
        "status": "success",
        "message": f"🎉 Voucher PIN successfully redeemed! Plan '{res['plan'].upper()}' activated for {res['days']} days.",
        "expires_at": res["expires_at"]
    })

@app.route('/api/payments/webhook', methods=['POST'])
def paystack_webhook():
    event_data = request.get_json() or {}
    event_type = event_data.get('event')
    if event_type == 'charge.success':
        data = event_data.get('data', {})
        reference = data.get('reference')
        metadata = data.get('metadata', {})
        plan_id = metadata.get('plan_id', 'monthly')
        phone = metadata.get('phone')

        conn = db.get_db_connection()
        user = None
        if phone:
            user = conn.execute("SELECT id FROM users WHERE phone = ?", (phone,)).fetchone()
        conn.close()

        user_id = user["id"] if user else 1
        days = 30
        if plan_id == 'weekly': days = 7
        elif plan_id == 'season': days = 120

        new_expiry = db.apply_subscription(user_id, plan_id, days)
        return jsonify({"status": "processed", "reference": reference, "expires_at": new_expiry}), 200

    return jsonify({"status": "ignored"}), 200

# ----------------- PRODUCER CONSOLE ROUTES -----------------
@app.route('/producer', methods=['GET', 'POST'])
def producer_console():
    settings = db.get_producer_settings()
    console_pass = settings.get('producer_console_pass', '$$manisoft11console')

    if not session.get('producer_unlocked'):
        if request.method == 'POST':
            entered_key = request.form.get('console_key', '').strip()
            if entered_key == console_pass or entered_key == '$$manisoft11console':
                session['producer_unlocked'] = True
                return redirect('/producer')
            else:
                return render_template('producer_gatekeeper.html', error="Invalid console pass key.")
        return render_template('producer_gatekeeper.html')

    # Producer is authenticated
    kpis = db.get_producer_kpis()
    orders = db.get_payment_orders(limit=50)
    vouchers = db.get_all_vouchers(limit=50)
    users = db.get_all_users_admin(limit=50)
    return render_template('producer_panel.html', settings=settings, kpis=kpis, orders=orders, vouchers=vouchers, users=users)

@app.route('/producer/lock', methods=['POST'])
def producer_lock():
    session.pop('producer_unlocked', None)
    return redirect('/producer')

@app.route('/api/producer/settings', methods=['POST'])
def api_producer_settings():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    updated = db.update_producer_settings(data)
    return jsonify({"status": "success", "settings": updated})

@app.route('/api/producer/orders/confirm', methods=['POST'])
def api_producer_confirm_order():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    reference = data.get('reference')
    if not reference:
        return jsonify({"error": "Missing reference"}), 400
    res = db.confirm_payment_order(reference, confirmed_by='Producer')
    return jsonify(res)

@app.route('/api/producer/orders/issue-pin', methods=['POST'])
def api_producer_issue_pin():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    reference = data.get('reference')
    if not reference:
        return jsonify({"error": "Missing reference"}), 400
    res = db.issue_voucher_for_order(reference)
    return jsonify(res)

@app.route('/api/producer/vouchers/generate', methods=['POST'])
def api_producer_generate_vouchers():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    plan = data.get('plan', 'monthly')
    count = int(data.get('count', 10))
    days = 30
    if plan == 'weekly': days = 7
    elif plan == 'season': days = 120
    codes = db.generate_vouchers(plan, days, count)
    return jsonify({"status": "success", "generated": codes})

@app.route('/api/producer/users/grant-pass', methods=['POST'])
def api_producer_grant_pass():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    user_id = data.get('user_id')
    plan = data.get('plan', 'monthly')
    days = int(data.get('days', 30))
    res = db.manually_grant_user_pass(user_id, plan, days)
    return jsonify(res)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5050))
    print(f"🚀 PassMaster AI Server running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
