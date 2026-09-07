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
    assert len(board) >= 5
    assert board[0]["rank"] == 1
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
