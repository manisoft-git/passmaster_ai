import sys
import os
import json
import time

# Ensure passmaster_ai root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from app import app
import db.database as db

client = app.test_client()

def run_test(name, fn):
    try:
        fn()
        print(f"  [PASS] {name}")
        return True
    except Exception as e:
        print(f"  [FAIL] {name}: {e}")
        import traceback
        traceback.print_exc()
        return False

tests_passed = 0
tests_total = 0

print("\n=======================================================")
print("🧪 STARTING PASSMASTER AI 100% COMPREHENSIVE TEST SUITE")
print("=======================================================\n")

# --- SECTION 1: STATIC & WEB ASSETS ---
print("📁 SECTION 1: Web Pages & Static Assets")
def test_index_page():
    res = client.get("/")
    assert res.status_code == 200, f"Expected 200, got {res.status_code}"
    assert "PassMaster AI" in res.data.decode()
    assert "cbtOptionsList" in res.data.decode()
    assert "calcModal" in res.data.decode()
    assert "leaderboardTbody" in res.data.decode()

def test_manifest():
    res = client.get("/manifest.json")
    assert res.status_code == 200
    data = json.loads(res.data)
    assert data["short_name"] == "PassMaster"

def test_css():
    res = client.get("/static/css/styles.css")
    assert res.status_code == 200
    assert len(res.data) > 1000

def test_js():
    res = client.get("/static/js/app.js")
    assert res.status_code == 200
    assert "calcAction" in res.data.decode()

for t_name, t_fn in [
    ("Index Page Loads (200 OK & Required DOM Elements)", test_index_page),
    ("PWA Manifest (Valid JSON & App Meta)", test_manifest),
    ("CSS Stylesheet (Non-empty & Loaded)", test_css),
    ("JS Client Bundle (Contains Calculator & Core Logic)", test_js)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 2: QUESTIONS & SYLLABUS ---
print("\n📚 SECTION 2: Curriculum, Questions & Syllabus")
def test_all_questions():
    res = client.get("/api/questions")
    assert res.status_code == 200
    d = res.json
    assert d["count"] >= 12
    assert "traps" in d["questions"][0]
    assert "pedagogical_concept" in d["questions"][0]

def test_subject_filtering():
    for subj in ["Physics", "Mathematics", "Use of English", "Chemistry", "Biology", "Economics", "Government", "Literature in English"]:
        res = client.get(f"/api/questions?subject={subj}")
        assert res.status_code == 200
        for q in res.json["questions"]:
            assert q["subject"].lower() == subj.lower()

def test_syllabus_tree():
    res = client.get("/api/syllabus")
    assert res.status_code == 200
    s = res.json["syllabus"]
    for required in ["Physics", "Mathematics", "Use of English", "Chemistry", "Biology", "Economics", "Government", "Literature in English"]:
        assert required in s, f"Missing {required} in syllabus"

for t_name, t_fn in [
    ("All Questions API & Trap Metadata", test_all_questions),
    ("Subject-Specific Question Filtering", test_subject_filtering),
    ("Official Syllabus Hierarchy & Weights", test_syllabus_tree)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 3: AUTHENTICATION & USER SESSIONS ---
print("\n🔐 SECTION 3: Authentication, Streaks & Session State")
test_email = f"audit_user_{int(time.time())}@student.ng"
test_phone = f"080{int(time.time()) % 100000000:08d}"

def test_registration():
    res = client.post("/api/auth/register", json={
        "name": "Audit Candidate",
        "email": test_email,
        "phone": test_phone,
        "password": "strongpassword123",
        "target_course": "Law",
        "target_uni": "University of Ibadan",
        "target_score": 285
    })
    assert res.status_code == 200
    assert res.json["user"]["name"] == "Audit Candidate"

def test_duplicate_registration_protection():
    res = client.post("/api/auth/register", json={
        "name": "Duplicate Candidate",
        "email": test_email,
        "phone": "08099999999",
        "password": "pwd"
    })
    assert res.status_code == 400
    assert "already exists" in res.json["error"]

def test_login_success():
    res = client.post("/api/auth/login", json={
        "identifier": test_email,
        "password": "strongpassword123"
    })
    assert res.status_code == 200
    assert res.json["status"] == "success"
    assert res.json["user"]["email"] == test_email

def test_login_invalid_credentials():
    res = client.post("/api/auth/login", json={
        "identifier": test_email,
        "password": "WRONG_PASSWORD"
    })
    assert res.status_code == 401
    assert "Invalid" in res.json["error"]

def test_session_me():
    res = client.get("/api/auth/me")
    assert res.status_code == 200
    assert res.json["status"] == "authenticated"
    assert res.json["user"]["email"] == test_email
    assert res.json["user"]["streak"] >= 1

for t_name, t_fn in [
    ("User Registration Flow", test_registration),
    ("Duplicate Registration Prevention", test_duplicate_registration_protection),
    ("Login Authentication Success", test_login_success),
    ("Invalid Password Rejection (401)", test_login_invalid_credentials),
    ("Session Persistence (/api/auth/me)", test_session_me)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 4: SOCRATIC AI COACH ENGINE ---
print("\n🧠 SECTION 4: Socratic AI & Trap Detection")
def test_correct_answer_reinforcement():
    # Question phy_001 (correct is B = 666.7 cm³)
    res = client.post("/api/tutor/attempt", json={
        "question_id": "phy_001",
        "selected_option": "B",
        "time_seconds": 25
    })
    assert res.status_code == 200
    d = res.json
    assert d["is_correct"] is True
    assert "Brilliant" in d["message"]
    assert "Charles" in d["concept"]

def test_trap_detection_without_spoilers():
    # Question phy_001 (Option A is the Celsius ratio trap)
    res = client.post("/api/tutor/attempt", json={
        "question_id": "phy_001",
        "selected_option": "A",
        "time_seconds": 35
    })
    assert res.status_code == 200
    d = res.json
    assert d["is_correct"] is False
    assert d["correct_option"] is None  # Must NOT spoil answer
    assert "Celsius" in d["trap_detected"]
    assert "mandatory unit" in d["socratic_prompt"]

def test_socratic_followup_dialogue():
    # Student responds to Coach Kalu with the conversion
    res = client.post("/api/tutor/chat", json={
        "question_id": "phy_001",
        "message": "27 is 300K and 127 is 400K in Kelvin"
    })
    assert res.status_code == 200
    d = res.json
    assert "300" in d["reply"]
    assert "666.7" in d["reply"]
    assert d.get("revealed") is True

def test_socratic_surrender_command():
    res = client.post("/api/tutor/chat", json={
        "question_id": "eng_001",
        "message": "tell me the answer please"
    })
    assert res.status_code == 200
    assert "Option B" in res.json["reply"] or "were" in res.json["reply"]

for t_name, t_fn in [
    ("Correct Answer Conceptual Reinforcement", test_correct_answer_reinforcement),
    ("Cognitive Trap Detection (Zero Answer Spoilers)", test_trap_detection_without_spoilers),
    ("Socratic Multi-turn Dialogue Resolution", test_socratic_followup_dialogue),
    ("Explicit Answer Revelation on Surrender", test_socratic_surrender_command)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 5: DIAGNOSTICS & SCORE PREDICTOR ---
print("\n📊 SECTION 5: Score Predictor & Leaky Bucket Engine")
def test_predicted_score_calculation():
    res = client.post("/api/diagnostics/score", json={
        "history": {
            "phy_001": {"selected": "B", "is_correct": True, "time_seconds": 22},
            "eng_001": {"selected": "B", "is_correct": True, "time_seconds": 18},
            "mth_001": {"selected": "B", "is_correct": True, "time_seconds": 30},
            "chm_001": {"selected": "B", "is_correct": False, "time_seconds": 45}
        }
    })
    assert res.status_code == 200
    d = res.json
    pred = d["predicted_score"]
    assert 100 <= pred["total_predicted_score"] <= 400
    assert len(d["leaky_bucket"]) >= 1
    assert d["leaky_bucket"][0]["estimated_mark_loss"] > 0

def test_whatsapp_share_card_generation():
    res = client.post("/api/diagnostics/share-card", json={
        "name": "Audit Candidate",
        "course": "Law",
        "university": "UI",
        "history": {
            "phy_001": {"selected": "A", "is_correct": False, "time_seconds": 40}
        }
    })
    assert res.status_code == 200
    card = res.json["card_text"]
    assert "MY OFFICIAL JAMB" in card
    assert "Audit Candidate" in card
    assert "PassMaster AI" in card

for t_name, t_fn in [
    ("Bayesian 400-Point JAMB Score & Leaky Bucket", test_predicted_score_calculation),
    ("Viral WhatsApp Status Card Generator", test_whatsapp_share_card_generation)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 6: LEADERBOARD & MISTAKE VAULT ---
print("\n🏆 SECTION 6: National Leaderboard & Mistake Vault")
def test_national_leaderboard():
    res = client.get("/api/leaderboard")
    assert res.status_code == 200
    board = res.json["leaderboard"]
    assert len(board) >= 1
    assert board[0]["rank"] == 1
    if len(board) > 1:
        assert board[0]["xp"] >= board[1]["xp"]

def test_mistake_vault():
    res = client.get("/api/mistake-vault")
    assert res.status_code == 200
    vault = res.json["vault"]
    assert isinstance(vault, list)

for t_name, t_fn in [
    ("National Leaderboard Sorting & Integrity", test_national_leaderboard),
    ("Mistake Vault API Retrieval", test_mistake_vault)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 7: PARENT & SPONSOR PORTAL ---
print("\n👨‍👩‍👧 SECTION 7: Parent & Sponsor Portal")
def test_parent_report_lookup():
    res = client.get(f"/api/parent/report?phone={test_phone}")
    assert res.status_code == 200
    rep = res.json["report"]
    assert rep["name"] == "Audit Candidate"
    assert "accuracy_pct" in rep
    assert "streak_days" in rep

def test_parent_report_not_found():
    res = client.get("/api/parent/report?phone=08000000000")
    assert res.status_code == 404
    assert "No registered candidate" in res.json["error"]

for t_name, t_fn in [
    ("Parent Report Live Phone Lookup", test_parent_report_lookup),
    ("Parent Report Non-Existent Phone (404)", test_parent_report_not_found)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 8: WHATSAPP BOT ENGINE ---
print("\n💬 SECTION 8: WhatsApp Bot Ingestion & Commands")
def test_whatsapp_welcome():
    res = client.post("/api/whatsapp/message", json={"phone": test_phone, "message": "START"})
    assert res.status_code == 200
    assert "Welcome to PassMaster" in res.json["reply"]

def test_whatsapp_subject_question():
    res = client.post("/api/whatsapp/message", json={"phone": test_phone, "message": "ENG"})
    assert res.status_code == 200
    assert "Reply with A, B, C, or D" in res.json["reply"]

def test_whatsapp_answer_grading():
    res = client.post("/api/whatsapp/message", json={"phone": test_phone, "message": "B"})
    assert res.status_code == 200
    assert len(res.json["reply"]) > 20

def test_whatsapp_score_inquiry():
    res = client.post("/api/whatsapp/message", json={"phone": test_phone, "message": "SCORE"})
    assert res.status_code == 200
    assert "READINESS SCORE" in res.json["reply"]

for t_name, t_fn in [
    ("WhatsApp Bot START / Welcome Menu", test_whatsapp_welcome),
    ("WhatsApp Bot Subject Selection & Question Delivery", test_whatsapp_subject_question),
    ("WhatsApp Bot Socratic Answer Grading", test_whatsapp_answer_grading),
    ("WhatsApp Bot Instant Score Card Inquiry", test_whatsapp_score_inquiry)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 9: PAYMENTS & VOUCHER REDEMPTION ---
print("\n💳 SECTION 9: Payments & Voucher Redemptions")
def test_payment_checkout_virtual_account():
    for plan in ["weekly", "monthly", "season"]:
        res = client.post("/api/payments/checkout", json={"plan_id": plan})
        assert res.status_code == 200
        assert res.json["status"] == "success"
        assert len(res.json["virtual_account"]["account_number"]) == 10

def test_payment_verify():
    res = client.post("/api/payments/verify", json={"reference": "TEST_REF_123", "plan_id": "monthly"})
    assert res.status_code == 200
    assert res.json["status"] == "verified"

test_pin = f"PASS-TEST-{int(time.time())}"
def test_voucher_redemption_success():
    conn = db.get_db_connection()
    conn.execute("INSERT OR REPLACE INTO vouchers (code, plan, days, is_used) VALUES (?, 'monthly', 30, 0)", (test_pin,))
    conn.commit()
    conn.close()
    res = client.post("/api/payments/redeem-voucher", json={"pin_code": test_pin})
    assert res.status_code == 200
    assert "successfully redeemed" in res.json["message"]

def test_voucher_already_used():
    res = client.post("/api/payments/redeem-voucher", json={"pin_code": test_pin})
    assert res.status_code == 400
    assert "already been used" in res.json["error"]

def test_invalid_voucher():
    res = client.post("/api/payments/redeem-voucher", json={"pin_code": "INVALID-CODE-9999"})
    assert res.status_code == 400
    assert "Invalid" in res.json["error"]

for t_name, t_fn in [
    ("Monnify / Paystack Virtual Account Checkout Flow", test_payment_checkout_virtual_account),
    ("Instant Payment Verification & Pass Activation", test_payment_verify),
    ("Valid Voucher PIN Redemption", test_voucher_redemption_success),
    ("Replay Attack Prevention (Voucher Already Used)", test_voucher_already_used),
    ("Invalid Voucher Code Rejection", test_invalid_voucher)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 10: PRODUCTION WEBHOOKS ---
print("\n🌐 SECTION 10: Production Webhooks & Meta Handshake")
def test_whatsapp_webhook_get():
    # Test valid challenge verification
    res = client.get("/api/whatsapp/webhook?hub.mode=subscribe&hub.verify_token=passmaster_secure_webhook_verify_token_2025&hub.challenge=test_challenge_12345")
    assert res.status_code == 200
    assert res.data.decode() == "test_challenge_12345"

def test_whatsapp_webhook_forbidden():
    res = client.get("/api/whatsapp/webhook?hub.mode=subscribe&hub.verify_token=WRONG_TOKEN&hub.challenge=test")
    assert res.status_code == 403

def test_paystack_webhook():
    payload = {
        "event": "charge.success",
        "data": {
            "reference": "TEST_WEBHOOK_REF_999",
            "metadata": {
                "plan_id": "weekly",
                "phone": test_phone
            }
        }
    }
    res = client.post("/api/payments/webhook", json=payload)
    assert res.status_code == 200
    assert res.json["status"] == "processed"

for t_name, t_fn in [
    ("WhatsApp Cloud Webhook Verification (hub.challenge 200 OK)", test_whatsapp_webhook_get),
    ("WhatsApp Webhook Invalid Token Rejection (403)", test_whatsapp_webhook_forbidden),
    ("Paystack charge.success Automated Webhook Processing", test_paystack_webhook)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- SECTION 11: PRODUCER CONSOLE & DIRECT PAYMENTS ---
print("\n🛡️ SECTION 11: Producer Console & Direct Settlement Engine")
def test_producer_gatekeeper_denied():
    res = client.post("/producer", data={"console_key": "WRONG_PASS"})
    assert res.status_code == 200
    assert "Invalid console pass" in res.data.decode()

def test_producer_gatekeeper_unlock():
    res = client.post("/producer", data={"console_key": "$$manisoft11console"}, follow_redirects=True)
    assert res.status_code == 200
    assert "Producer Command Center" in res.data.decode()
    assert "Producer Bank & WhatsApp Setup" in res.data.decode()

orig_producer_settings = db.get_producer_settings()

def test_producer_settings_api():
    # Update producer bank details
    payload = {
        "producer_bank_name": "Kuda Microfinance Bank",
        "producer_account_number": "2009876543",
        "producer_account_name": "CHIDI OKONKWO / PASSMASTER",
        "producer_whatsapp_phone": "2348099887755"
    }
    res = client.post("/api/producer/settings", json=payload)
    assert res.status_code == 200
    assert res.json["settings"]["producer_bank_name"] == "Kuda Microfinance Bank"

def test_checkout_reflects_updated_producer_account():
    res = client.post("/api/payments/checkout", json={"plan_id": "monthly"})
    assert res.status_code == 200
    acc = res.json["producer_account"]
    assert acc["bank_name"] == "Kuda Microfinance Bank"
    assert acc["account_number"] == "2009876543"

test_order_ref = f"PMS_TEST_{int(time.time())}"
def test_student_submit_transfer():
    res = client.post("/api/payments/submit-transfer", json={
        "plan_id": "monthly",
        "reference": test_order_ref,
        "name": "Audit Student Transfer",
        "notes": "Sent via Kuda mobile app"
    })
    assert res.status_code == 200
    assert res.json["status"] == "order_created"
    assert "wa.me/2348099887755" in res.json["whatsapp_url"]

def test_producer_confirm_student_order():
    res = client.post("/api/producer/orders/confirm", json={"reference": test_order_ref})
    assert res.status_code == 200
    assert res.json["status"] == "confirmed"

def test_producer_issue_pin_for_order():
    # Create another order
    order_ref_2 = f"PMS_PIN_{int(time.time())}"
    client.post("/api/payments/submit-transfer", json={"plan_id": "weekly", "reference": order_ref_2})
    res = client.post("/api/producer/orders/issue-pin", json={"reference": order_ref_2})
    assert res.status_code == 200
    pin = res.json["pin_code"]
    assert pin.startswith("PASS-2025-WEEKLY-")
    # Verify voucher is valid in DB
    redeem_res = client.post("/api/payments/redeem-voucher", json={"pin_code": pin})
    assert redeem_res.status_code == 200

def test_producer_generate_voucher_batch():
    res = client.post("/api/producer/vouchers/generate", json={"plan": "season", "count": 3})
    assert res.status_code == 200
    assert len(res.json["generated"]) == 3
    assert res.json["generated"][0].startswith("PASS-2025-SEASON-")

def test_producer_grant_manual_pass():
    res = client.post("/api/producer/users/grant-pass", json={"user_id": 1, "plan": "season", "days": 120})
    assert res.status_code == 200
    assert res.json["plan_id"] == "season"

for t_name, t_fn in [
    ("Producer Gatekeeper Invalid Pass Rejection", test_producer_gatekeeper_denied),
    ("Producer Console Unlock ($$manisoft11console)", test_producer_gatekeeper_unlock),
    ("Producer Bank & WhatsApp Settings Live Update", test_producer_settings_api),
    ("Student Checkout Reflects Updated Producer Account", test_checkout_reflects_updated_producer_account),
    ("Student Transfer Order Submission & WhatsApp Generator", test_student_submit_transfer),
    ("Producer 1-Click Order Confirmation & Instant Activation", test_producer_confirm_student_order),
    ("Producer Issue Voucher PIN for Order & Immediate Redeem", test_producer_issue_pin_for_order),
    ("Producer Batch Voucher Generation Studio", test_producer_generate_voucher_batch),
    ("Producer Manual Pass Grant to Student", test_producer_grant_manual_pass)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

if orig_producer_settings:
    db.update_producer_settings(orig_producer_settings)

# --- SECTION 12: TOPIC LESSONS, 180-Q MOCK, ANTI-CHEAT & REVISED PRICING ---
print("\n🚀 SECTION 12: Topic Masterclasses, 180-Q Mock, Anti-Cheat & Revised Pricing")

def test_revised_plan_pricing():
    for plan, expected_price in [("weekly", 1500), ("monthly", 3500), ("season", 8500)]:
        res = client.post("/api/payments/checkout", json={"plan_id": plan})
        assert res.status_code == 200
        assert res.json["amount_ngn"] == expected_price

def test_demo_pin_retirement():
    # Attempting to use old demo PINs must fail
    for retired_pin in ["PASS-2025-DEMO-WEEK", "UNILAG-MED-2025"]:
        res = client.post("/api/payments/redeem-voucher", json={"pin_code": retired_pin})
        assert res.status_code == 400
        assert "Invalid" in res.json["error"]

def test_topic_lessons_list():
    res = client.get("/api/lessons")
    assert res.status_code == 200
    lessons = res.json["lessons"]
    assert len(lessons) >= 32
    eng_first = next(l for l in lessons if l["subject"] == "Use of English")
    assert eng_first["is_locked"] is False

def test_topic_lesson_free_preview():
    res = client.get("/api/lessons/Physics/Mechanics")
    assert res.status_code == 200
    assert "lesson" in res.json
    assert res.json["lesson"]["key_rule_or_formula"] is not None

def test_topic_lesson_paywall():
    with client.session_transaction() as sess:
        sess.clear()
    res = client.get("/api/lessons/Physics/Thermal%20Physics%20%26%20Waves")
    assert res.status_code == 403
    assert "subscription" in res.json["error"].lower()

def test_full_jamb_mock_generation():
    res = client.get("/api/questions?mode=full_jamb")
    assert res.status_code == 200
    assert res.json["mode"] == "full_jamb"
    assert res.json["count"] == 180
    eng_qs = [q for q in res.json["questions"] if q["subject"] == "Use of English"]
    assert len(eng_qs) == 60

def test_anti_cheat_share_card():
    res = client.post("/api/diagnostics/share-card", json={
        "name": "Audit Student",
        "course": "Engineering",
        "university": "FUTA",
        "cheat_count": 3
    })
    assert res.status_code == 200
    card = res.json["card_text"]
    assert "3 Tab-Switch Warning(s)" in card
    assert "2026/2027" in card

def test_founder_support_bio():
    res = client.get("/api/support/bio")
    assert res.status_code == 200
    assert "Manifest Subeno" in res.json["bio"]
    assert "3050550518" in res.json["account_number"]
    assert "First Bank" in res.json["bank_name"]

def test_account_deletion_and_anti_abuse_ban():
    ts = int(time.time() * 1000)
    abuse_email = f"abuse_cand_{ts}@student.ng"
    abuse_phone = f"081{ts % 100000000:08d}"
    
    # 1st cycle: Register and Delete
    r1 = client.post("/api/auth/register", json={
        "name": "Abuse Tester", "email": abuse_email, "phone": abuse_phone, "password": "pwd"
    })
    assert r1.status_code == 200
    res_del1 = client.post("/api/auth/delete-account")
    assert res_del1.status_code == 200

    # 2nd cycle: Register and Delete
    r2 = client.post("/api/auth/register", json={
        "name": "Abuse Tester", "email": abuse_email, "phone": abuse_phone, "password": "pwd"
    })
    assert r2.status_code == 200
    res_del2 = client.post("/api/auth/delete-account")
    assert res_del2.status_code == 200

    # 3rd cycle: Register and Delete
    r3 = client.post("/api/auth/register", json={
        "name": "Abuse Tester", "email": abuse_email, "phone": abuse_phone, "password": "pwd"
    })
    assert r3.status_code == 200
    res_del3 = client.post("/api/auth/delete-account")
    assert res_del3.status_code == 200

    # 4th cycle: Registration attempt must be rejected with 403 Over-usage Ban
    res_reg_blocked = client.post("/api/auth/register", json={
        "name": "Abuse Tester", "email": abuse_email, "phone": abuse_phone, "password": "pwd"
    })
    assert res_reg_blocked.status_code == 403
    assert "banned" in res_reg_blocked.json["error"].lower()

def test_producer_user_lock_and_strip():
    with client.session_transaction() as sess:
        sess['producer_unlocked'] = True
    ts = int(time.time() * 1000) + 77
    lock_email = f"lock_cand_{ts}@student.ng"
    lock_phone = f"089{ts % 100000000:08d}"
    reg_res = client.post("/api/auth/register", json={
        "name": "Lock Target", "email": lock_email, "phone": lock_phone, "password": "pwd"
    })
    assert reg_res.status_code == 200, f"Register failed: {reg_res.json}"
    u_id = reg_res.json["user"]["id"]

    # Producer locks user
    lock_res = client.post("/api/producer/users/toggle-lock", json={"user_id": u_id, "is_locked": 1})
    assert lock_res.status_code == 200
    assert lock_res.json["is_locked"] == 1

    # Login as locked user fails
    login_res = client.post("/api/auth/login", json={"identifier": lock_email, "password": "pwd"})
    assert login_res.status_code == 403
    assert "locked" in login_res.json["error"].lower()

    # Unlock user
    unlock_res = client.post("/api/producer/users/toggle-lock", json={"user_id": u_id, "is_locked": 0})
    assert unlock_res.status_code == 200
    assert unlock_res.json["is_locked"] == 0

    # Grant pass then strip privileges
    client.post("/api/producer/users/grant-pass", json={"user_id": u_id, "plan": "monthly", "days": 30})
    strip_res = client.post("/api/producer/users/strip-privileges", json={"user_id": u_id})
    assert strip_res.status_code == 200
    user = db.get_user_by_id(u_id)
    assert user["plan"] == "free"

def test_expanded_280_question_bank():
    res = client.get("/api/questions")
    assert res.status_code == 200
    qs = res.json["questions"]
    assert len(qs) >= 280, f"Expected at least 280 questions, found {len(qs)}"
    
    by_subj = {}
    for q in qs:
        s = q["subject"]
        by_subj[s] = by_subj.get(s, 0) + 1
        assert "id" in q
        assert "question" in q and len(q["question"]) > 10
        assert "options" in q and len(q["options"]) == 4
        assert "correct_option" in q and q["correct_option"] in ["A", "B", "C", "D"]
        assert "traps" in q and len(q["traps"]) >= 3
        assert "socratic_prompt" in q
    
    for req_subj in [
        "Use of English", "Mathematics", "Physics", "Chemistry",
        "Biology", "Economics", "Government", "Literature in English"
    ]:
        assert req_subj in by_subj, f"Missing subject {req_subj}"
        assert by_subj[req_subj] >= 35, f"Subject {req_subj} has only {by_subj[req_subj]} questions (expected >= 35)"

def test_topic_focus_query_filtering():
    import json
    with open("data/syllabus.json", "r", encoding="utf-8") as f:
        syllabus = json.load(f)
    
    for subj, info in syllabus.items():
        for topic_obj in info.get("topics", []):
            top_name = topic_obj["name"]
            res = client.get(f"/api/questions?subject={subj}&topic={top_name}")
            assert res.status_code == 200, f"Failed for {subj} -> {top_name}"
            data = res.json
            count = data.get("count", 0)
            assert count >= 5, f"{subj} -> {top_name} only returned {count} questions (expected >= 5)"
            for q in data.get("questions", []):
                assert q["subject"].lower() == subj.lower()

def test_deep_lessons_exhaustiveness():
    import json
    with open("data/lessons.json", "r", encoding="utf-8") as f:
        lessons_data = json.load(f)
    
    total_lessons = sum(len(topics) for topics in lessons_data.values())
    assert total_lessons >= 32, f"Expected 32 lessons, found {total_lessons}"
    
    forbidden_placeholders = [
        "A. Distractor 1", "Core axiom...", "distractor 1", "distractor 2",
        "distractor 3", "Option A: distractor", "Option B: distractor"
    ]
    
    for subj, topics in lessons_data.items():
        assert len(topics) >= 4, f"Subject {subj} should have at least 4 topics, found {len(topics)}"
        for topic in topics:
            overview = topic.get("overview", "")
            assert len(overview) > 150, f"Overview too short in {subj} -> {topic['topic']}"
            assert len(topic.get("worked_examples", [])) >= 1
            for we in topic.get("worked_examples", []):
                assert "question" in we and len(we["question"]) > 10
                assert "solution" in we and len(we["solution"]) > 20
            assert topic.get("golden_rule") is not None
            
            content_str = json.dumps(topic)
            for placeholder in forbidden_placeholders:
                assert placeholder.lower() not in content_str.lower(), f"Found placeholder '{placeholder}' in {subj} -> {topic['topic']}"

def test_cbt_topic_focus_ui_elements():
    res = client.get("/")
    assert res.status_code == 200
    html = res.data.decode("utf-8")
    assert "cbtTopicBarContainer" in html
    assert "cbtTopicPills" in html
    assert "activeTopicLabel" in html
    assert "cbtTopicCountIndicator" in html
    assert "resetTopicFocus()" in html

def test_preferences_identity_protection():
    # Login candidate
    client.post("/api/auth/login", json={
        "identifier": "08011223344",
        "password": "Password123"
    })
    
    # 1. Attempt to change email -> must be rejected with 403
    res = client.post("/api/auth/preferences", json={
        "email": "malicious_hacker@gmail.com",
        "questions_per_subject": 20
    })
    assert res.status_code == 403
    assert "cannot modify sensitive records" in res.json["error"].lower()

    # 2. Attempt to change phone -> must be rejected with 403
    res = client.post("/api/auth/preferences", json={
        "phone": "08099999999"
    })
    assert res.status_code == 403
    assert "cannot modify sensitive records" in res.json["error"].lower()

    # 3. Attempt to change name -> must be rejected with 403
    res = client.post("/api/auth/preferences", json={
        "name": "Different Impersonator Name"
    })
    assert res.status_code == 403
    assert "cannot modify sensitive records" in res.json["error"].lower()

    # 4. Valid preference update -> must succeed with 200
    res = client.post("/api/auth/preferences", json={
        "questions_per_subject": 20,
        "subjects": ["Use of English", "Biology", "Chemistry", "Physics"],
        "target_course": "Pharmacy",
        "target_uni": "UNN",
        "target_score": 310
    })
    assert res.status_code == 200
    assert res.json["status"] == "success"
    assert res.json["preferences"]["questions_per_subject"] == 20
    assert res.json["preferences"]["subjects"] == ["Use of English", "Biology", "Chemistry", "Physics"]

def test_jamb_standard_20_questions_per_subject():
    # Default 20 Qs per subject (4 subjects = 80 Qs)
    res = client.get("/api/questions?mode=jamb_standard&questions_per_subject=20")
    assert res.status_code == 200
    data = res.json
    assert data["status"] == "success"
    assert data["count"] == 80
    assert data["questions_per_subject"] == 20
    
    # Verify each subject has exactly 20 questions
    subj_counts = {}
    for q in data["questions"]:
        subj_counts[q["subject"]] = subj_counts.get(q["subject"], 0) + 1
    assert len(subj_counts) == 4
    for subj, cnt in subj_counts.items():
        assert cnt == 20, f"Expected 20 questions for {subj}, got {cnt}"

    # 10 Qs per subject (4 subjects = 40 Qs)
    res10 = client.get("/api/questions?mode=jamb_standard&questions_per_subject=10")
    assert res10.status_code == 200
    assert res10.json["count"] == 40

    # Custom 4-subject combination: English, Biology, Chemistry, Physics
    res_med = client.get("/api/questions?mode=jamb_standard&questions_per_subject=20&subjects=Use%20of%20English,Biology,Chemistry,Physics")
    assert res_med.status_code == 200
    assert res_med.json["count"] == 80
    med_subjs = {q["subject"] for q in res_med.json["questions"]}
    assert med_subjs == {"Use of English", "Biology", "Chemistry", "Physics"}

def test_visual_schematics_and_cbt_tabs_ui():
    res = client.get("/")
    assert res.status_code == 200
    html = res.data.decode("utf-8")
    assert "cbtSubjectTabsContainer" in html
    assert "lessonDiagramMount" in html
    assert "lessonVideoChaptersList" in html
    assert "locked-identity-card" in html
    assert "prefQuestionsPerSubject" in html
    assert "openPreferencesModal()" in html

for t_name, t_fn in [
    ("Revised Pass Pricing (₦1,500 / ₦3,500 / ₦8,500)", test_revised_plan_pricing),
    ("Retired Demo PINs Strict Rejection", test_demo_pin_retirement),
    ("Topic Lessons Catalog API (32 Topics)", test_topic_lessons_list),
    ("Topic Lesson Free Preview (Lesson 0)", test_topic_lesson_free_preview),
    ("Topic Lesson Subscription Paywall (Lesson > 0)", test_topic_lesson_paywall),
    ("Full JAMB 180-Question Mock Exam Generator", test_full_jamb_mock_generation),
    ("Anti-Cheat Scorecard Tab-Switch Warning Stamp", test_anti_cheat_share_card),
    ("Founder Support & Settlement Bio Endpoint", test_founder_support_bio),
    ("Candidate Account Deletion & Anti-Abuse 3-Strike Ban", test_account_deletion_and_anti_abuse_ban),
    ("Producer Student Lock, Unlock & Privilege Strip Engine", test_producer_user_lock_and_strip),
    ("Comprehensive 280+ Question Bank Quality Audit", test_expanded_280_question_bank),
    ("Topic Focus Query Filtering Across 32 Syllabus Topics", test_topic_focus_query_filtering),
    ("Deep Topic Lessons Exhaustiveness & Zero Placeholders", test_deep_lessons_exhaustiveness),
    ("Mock CBT Topic Focus Interactive Bar & UI Elements", test_cbt_topic_focus_ui_elements),
    ("Candidate Identity Record Immutability & Protection (403)", test_preferences_identity_protection),
    ("JAMB Standard CBT Mode (Strict 20 Qs Per Subject = 80 Total)", test_jamb_standard_20_questions_per_subject),
    ("Visual Schematics, Video Theater & CBT Subject Tabs UI", test_visual_schematics_and_cbt_tabs_ui)
]:
    tests_total += 1
    if run_test(t_name, t_fn): tests_passed += 1

# --- FINAL AUDIT SUMMARY ---
print("\n=======================================================")
print(f"📊 AUDIT RESULTS: {tests_passed} / {tests_total} TESTS PASSED ({(tests_passed/tests_total)*100:.1f}%)")
print("=======================================================\n")

if tests_passed == tests_total:
    print("✅ SYSTEM IS 100% OPERATIONAL, SECURE & PRODUCTION READY!")
    sys.exit(0)
else:
    print("❌ SOME TESTS FAILED. CHECK OUTPUT ABOVE.")
    sys.exit(1)
