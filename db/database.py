import sqlite3
import time
import os
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "passmaster.db")

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        phone TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        target_course TEXT DEFAULT 'Medicine & Surgery',
        target_uni TEXT DEFAULT 'UNILAG',
        target_score INTEGER DEFAULT 280,
        plan TEXT DEFAULT 'free',
        plan_expires_at REAL DEFAULT 0,
        xp INTEGER DEFAULT 120,
        created_at REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS attempts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER,
        question_id TEXT NOT NULL,
        selected_option TEXT NOT NULL,
        is_correct INTEGER NOT NULL,
        time_seconds INTEGER NOT NULL,
        is_flagged INTEGER DEFAULT 0,
        timestamp REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS vouchers (
        code TEXT PRIMARY KEY,
        plan TEXT NOT NULL,
        days INTEGER NOT NULL,
        is_used INTEGER DEFAULT 0,
        redeemed_by INTEGER,
        redeemed_at REAL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS user_streaks (
        user_id INTEGER PRIMARY KEY,
        streak_count INTEGER DEFAULT 1,
        last_active_date TEXT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    # Seed demo vouchers
    demo_vouchers = [
        ("PASS-2025-DEMO-WEEK", "weekly", 7),
        ("PASS-2025-VIP-MONTH", "monthly", 30),
        ("PASS-2025-FULL-SEASON", "season", 120),
        ("JAMB-2025-SCHOLAR", "monthly", 30),
        ("UNILAG-MED-2025", "season", 120)
    ]
    for code, plan, days in demo_vouchers:
        cursor.execute("INSERT OR IGNORE INTO vouchers (code, plan, days, is_used) VALUES (?, ?, ?, 0)", (code, plan, days))

    # Seed top leaderboard dummy users if table has few users
    cursor.execute("SELECT COUNT(*) as count FROM users")
    count = cursor.fetchone()["count"]
    if count < 5:
        dummy_users = [
            ("Amina Bello", "amina@kaduna.ng", "08021112233", "Medicine & Surgery", "ABU Zaria", 310, 1420),
            ("Favour Adeyemi", "favour@student.ng", "08012345678", "Medicine & Surgery", "UNILAG", 295, 1180),
            ("Emeka Chukwu", "emeka@enugu.ng", "08034445566", "Software Engineering", "UNN", 285, 950),
            ("Tunde Bakare", "tunde@ibadan.ng", "08047778899", "Law", "UI", 278, 840),
            ("Zainab Umar", "zainab@abuja.ng", "08059990011", "Pharmacy", "BUK", 265, 720)
        ]
        pwd_hash = generate_password_hash("password123")
        for name, email, phone, course, uni, score, xp in dummy_users:
            cursor.execute("""
            INSERT OR IGNORE INTO users (name, email, phone, password_hash, target_course, target_uni, target_score, plan, plan_expires_at, xp, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, 'monthly', ?, ?, ?)
            """, (name, email, phone, pwd_hash, course, uni, score, time.time() + (60 * 86400), xp, time.time()))

    conn.commit()
    conn.close()

def register_user(name, email, phone, password, target_course="Medicine & Surgery", target_uni="UNILAG", target_score=280):
    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        pwd_hash = generate_password_hash(password)
        cursor.execute("""
        INSERT INTO users (name, email, phone, password_hash, target_course, target_uni, target_score, plan, plan_expires_at, xp, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'free', 0, 50, ?)
        """, (name, email.lower().strip(), phone.strip(), pwd_hash, target_course, target_uni, target_score, time.time()))
        
        user_id = cursor.lastrowid
        today_str = datetime.now().strftime("%Y-%m-%d")
        cursor.execute("INSERT INTO user_streaks (user_id, streak_count, last_active_date) VALUES (?, 1, ?)", (user_id, today_str))
        conn.commit()
        return {"success": True, "user_id": user_id}
    except sqlite3.IntegrityError as e:
        if "email" in str(e):
            return {"error": "An account with this email address already exists."}
        elif "phone" in str(e):
            return {"error": "An account with this phone number already exists."}
        return {"error": "Registration failed. User already registered."}
    finally:
        conn.close()

def authenticate_user(login_identifier, password):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT * FROM users WHERE email = ? OR phone = ?
    """, (login_identifier.lower().strip(), login_identifier.strip()))
    user = cursor.fetchone()
    conn.close()

    if user and check_password_hash(user["password_hash"], password):
        update_user_streak(user["id"])
        return dict(user)
    return None

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, phone, target_course, target_uni, target_score, plan, plan_expires_at, xp, created_at FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return None
    user_dict = dict(user)

    cursor.execute("SELECT streak_count FROM user_streaks WHERE user_id = ?", (user_id,))
    streak_row = cursor.fetchone()
    user_dict["streak"] = streak_row["streak_count"] if streak_row else 1
    user_dict["is_subscribed"] = (user_dict["plan_expires_at"] > time.time())
    
    # Calculate Level
    xp = user_dict.get("xp", 50)
    if xp >= 600:
        user_dict["level_name"] = "Merit List Master"
        user_dict["level_tier"] = 4
    elif xp >= 300:
        user_dict["level_name"] = "Scholar Candidate"
        user_dict["level_tier"] = 3
    elif xp >= 100:
        user_dict["level_name"] = "University Aspirant"
        user_dict["level_tier"] = 2
    else:
        user_dict["level_name"] = "Jambite Recruit"
        user_dict["level_tier"] = 1

    conn.close()
    return user_dict

def update_user_streak(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    today_str = datetime.now().strftime("%Y-%m-%d")

    cursor.execute("SELECT * FROM user_streaks WHERE user_id = ?", (user_id,))
    row = cursor.fetchone()
    if not row:
        cursor.execute("INSERT INTO user_streaks (user_id, streak_count, last_active_date) VALUES (?, 1, ?)", (user_id, today_str))
    else:
        last_date = row["last_active_date"]
        if last_date != today_str:
            last_dt = datetime.strptime(last_date, "%Y-%m-%d")
            today_dt = datetime.strptime(today_str, "%Y-%m-%d")
            delta = (today_dt - last_dt).days
            if delta == 1:
                cursor.execute("UPDATE user_streaks SET streak_count = streak_count + 1, last_active_date = ? WHERE user_id = ?", (today_str, user_id))
            elif delta > 1:
                cursor.execute("UPDATE user_streaks SET streak_count = 1, last_active_date = ? WHERE user_id = ?", (today_str, user_id))

    conn.commit()
    conn.close()

def add_user_xp(user_id, points):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET xp = COALESCE(xp, 0) + ? WHERE id = ?", (points, user_id))
    cursor.execute("SELECT xp FROM users WHERE id = ?", (user_id,))
    new_xp = cursor.fetchone()["xp"]
    conn.commit()
    conn.close()
    return new_xp

def record_attempt(user_id, question_id, selected_option, is_correct, time_seconds, is_flagged=0):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO attempts (user_id, question_id, selected_option, is_correct, time_seconds, is_flagged, timestamp)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, question_id, selected_option, 1 if is_correct else 0, time_seconds, is_flagged, time.time()))
    conn.commit()
    conn.close()

    # Award XP: 15 for correct, 5 for taking effort
    if user_id:
        add_user_xp(user_id, 15 if is_correct else 5)

def get_user_attempts(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT question_id, selected_option, is_correct, time_seconds, is_flagged FROM attempts WHERE user_id = ?", (user_id,))
    rows = cursor.fetchall()
    conn.close()
    result = {}
    for r in rows:
        result[r["question_id"]] = {
            "selected": r["selected_option"],
            "is_correct": bool(r["is_correct"]),
            "time_seconds": r["time_seconds"],
            "is_flagged": bool(r["is_flagged"])
        }
    return result

def get_mistake_vault(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT DISTINCT question_id, selected_option, time_seconds 
    FROM attempts 
    WHERE user_id = ? AND is_correct = 0
    ORDER BY timestamp DESC
    """, (user_id,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_leaderboard():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT u.id, u.name, u.target_uni, u.target_course, u.xp,
           COUNT(a.id) as total_attempts,
           SUM(CASE WHEN a.is_correct = 1 THEN 1 ELSE 0 END) as correct_attempts
    FROM users u
    LEFT JOIN attempts a ON u.id = a.user_id
    GROUP BY u.id
    ORDER BY u.xp DESC
    LIMIT 10
    """)
    rows = cursor.fetchall()
    conn.close()

    board = []
    for rank, r in enumerate(rows, start=1):
        xp = r["xp"] or 50
        predicted = min(360, max(180, int(180 + (xp * 0.12))))
        board.append({
            "rank": rank,
            "name": r["name"],
            "target_uni": r["target_uni"],
            "target_course": r["target_course"],
            "xp": xp,
            "predicted_score": predicted
        })
    return board

def get_parent_report(phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE phone = ?", (phone.strip(),))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return None

    user_dict = dict(user)
    user_id = user["id"]

    cursor.execute("SELECT COUNT(*) as total, SUM(is_correct) as correct, AVG(time_seconds) as avg_time FROM attempts WHERE user_id = ?", (user_id,))
    stats = cursor.fetchone()

    cursor.execute("SELECT streak_count FROM user_streaks WHERE user_id = ?", (user_id,))
    streak = cursor.fetchone()

    conn.close()
    total = stats["total"] or 0
    correct = stats["correct"] or 0
    accuracy = int((correct / total * 100)) if total > 0 else 0

    return {
        "name": user_dict["name"],
        "target_course": user_dict["target_course"],
        "target_uni": user_dict["target_uni"],
        "target_score": user_dict["target_score"],
        "plan": user_dict["plan"],
        "is_active": (user_dict["plan_expires_at"] > time.time()),
        "streak_days": streak["streak_count"] if streak else 1,
        "questions_completed": total,
        "accuracy_pct": accuracy,
        "avg_speed_seconds": int(stats["avg_time"] or 40),
        "xp": user_dict.get("xp", 120)
    }

def apply_subscription(user_id, plan_id, days):
    conn = get_db_connection()
    cursor = conn.cursor()
    new_expiry = time.time() + (days * 86400)
    cursor.execute("UPDATE users SET plan = ?, plan_expires_at = ? WHERE id = ?", (plan_id, new_expiry, user_id))
    conn.commit()
    conn.close()
    return new_expiry

def redeem_voucher_code(user_id, code):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vouchers WHERE code = ?", (code.strip().upper(),))
    v = cursor.fetchone()
    if not v:
        conn.close()
        return {"error": "Invalid Voucher PIN. Please check the code."}
    if v["is_used"]:
        conn.close()
        return {"error": "This Voucher PIN has already been used."}

    days = v["days"]
    plan = v["plan"]
    cursor.execute("UPDATE vouchers SET is_used = 1, redeemed_by = ?, redeemed_at = ? WHERE code = ?",
                   (user_id, time.time(), code.strip().upper()))
    conn.commit()
    conn.close()

    new_expiry = apply_subscription(user_id, plan, days)
    return {"success": True, "plan": plan, "days": days, "expires_at": new_expiry}
