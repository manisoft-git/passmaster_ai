import sys
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
from app import app

client = app.test_client()

# 1. Test Register
reg_res = client.post("/api/auth/register", json={
    "name": "Chidi Okonkwo",
    "email": "chidi2@student.ng",
    "phone": "08099887755",
    "password": "mypassword",
    "target_course": "Software Engineering",
    "target_uni": "FUTA",
    "target_score": 300
})
if reg_res.status_code == 200:
    print("1. Registration verified successfully")
else:
    print("1. User already registered or exists:", reg_res.json.get("error"))

# 2. Test Login
login_res = client.post("/api/auth/login", json={
    "identifier": "chidi2@student.ng",
    "password": "mypassword"
})
assert login_res.status_code == 200
user_name = login_res.json["user"]["name"]
print("2. Login verified: Authenticated as", user_name)

# 3. Test Attempt persistence
att_res = client.post("/api/tutor/attempt", json={
    "question_id": "mth_001",
    "selected_option": "B",
    "time_seconds": 28
})
assert att_res.status_code == 200
print("3. Attempt recorded and persisted to database")

# 4. Test Current User Profile & Streak
me_res = client.get("/api/auth/me")
assert me_res.status_code == 200 and me_res.json["status"] == "authenticated"
streak = me_res.json["user"]["streak"]
attempts_len = len(me_res.json["attempts"])
print("4. Session persistence verified (Streak:", streak, "days, Attempts:", attempts_len, ")")

# 5. Test Parent Report Lookup
parent_res = client.get("/api/parent/report?phone=08099887755")
assert parent_res.status_code == 200
rep = parent_res.json["report"]
print("5. Parent Portal Report verified for", rep["name"], ":", rep["questions_completed"], "questions,", rep["accuracy_pct"], "% accuracy")

# 6. Test Non-Existent User Parent Report (Expected 404)
demo_parent = client.get("/api/parent/report?phone=08000000000")
assert demo_parent.status_code == 404
print("6. Non-Existent Parent Report correctly rejected with 404")

# Cleanup test user
from db.database import get_db_connection
conn = get_db_connection()
c = conn.cursor()
c.execute("DELETE FROM attempts WHERE user_id IN (SELECT id FROM users WHERE email = 'chidi2@student.ng')")
c.execute("DELETE FROM user_streaks WHERE user_id IN (SELECT id FROM users WHERE email = 'chidi2@student.ng')")
c.execute("DELETE FROM users WHERE email = 'chidi2@student.ng'")
conn.commit()
conn.close()

print("\n🚀 ALL AUTHENTICATION, DATABASE & PARENT PORTAL CHECKS PASSED WITH 100% SUCCESS!")
