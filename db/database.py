import sqlite3
import time
import os
import secrets
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

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payment_orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        reference TEXT UNIQUE NOT NULL,
        user_id INTEGER,
        student_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        plan_id TEXT NOT NULL,
        plan_name TEXT NOT NULL,
        amount_ngn INTEGER NOT NULL,
        status TEXT DEFAULT 'pending',
        method TEXT DEFAULT 'manual_transfer',
        receipt_notes TEXT,
        issued_pin TEXT,
        confirmed_by TEXT,
        confirmed_at REAL,
        created_at REAL NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users(id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS producer_settings (
        key TEXT PRIMARY KEY,
        value TEXT NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS account_deletions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL,
        phone TEXT NOT NULL,
        name TEXT,
        deleted_at REAL NOT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS banned_identifiers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        identifier TEXT UNIQUE NOT NULL,
        reason TEXT NOT NULL,
        is_active INTEGER DEFAULT 1,
        banned_at REAL NOT NULL
    )
    """)

    # Attempt migration for is_locked column if not existing
    try:
        cursor.execute("ALTER TABLE users ADD COLUMN is_locked INTEGER DEFAULT 0")
    except sqlite3.OperationalError:
        pass

    # Seed default producer account, WhatsApp settings and founder support story
    default_settings = [
        ("producer_bank_name", "First Bank"),
        ("producer_account_number", "3050550518"),
        ("producer_account_name", "Manifest Subeno"),
        ("producer_whatsapp_phone", "2348091977795"),
        ("producer_console_pass", "$$manisoft11console"),
        ("producer_support_bio", "Hi! I am Manifest Subeno, an SS3 student at Good Shepherd Catholic College, Oyede, and the founder & lead developer of Mani$oft. I built PassMaster AI entirely on an Android mobile phone using Termux, night shifts, and pure grit. While coding full-stack architectures and AI engines on a phone screen is possible, scaling PassMaster AI to support millions of candidates preparing for JAMB 2026/2027 urgently requires a proper coding laptop/computer. Every subscription and voluntary sponsorship directly powers this mission. Thank you for empowering a Nigerian student builder!")
    ]
    for k, v in default_settings:
        cursor.execute("INSERT OR IGNORE INTO producer_settings (key, value) VALUES (?, ?)", (k, v))

    # Purge any demo vouchers so ONLY real producer vouchers work
    cursor.execute("DELETE FROM vouchers WHERE code IN ('PASS-2025-DEMO-WEEK', 'PASS-2025-VIP-MONTH', 'PASS-2025-FULL-SEASON', 'JAMB-2025-SCHOLAR', 'UNILAG-MED-2025')")

    # Production ready: No dummy/mock users seeded - leaderboard is strictly populated by real students
    conn.commit()
    conn.close()

def register_user(name, email, phone, password, target_course="Medicine & Surgery", target_uni="UNILAG", target_score=280):
    # Check over-usage abuse ban
    allowed, ban_err = can_register(email, phone)
    if not allowed:
        return {"error": ban_err}

    conn = get_db_connection()
    cursor = conn.cursor()
    try:
        pwd_hash = generate_password_hash(password)
        cursor.execute("""
        INSERT INTO users (name, email, phone, password_hash, target_course, target_uni, target_score, plan, plan_expires_at, xp, created_at, is_locked)
        VALUES (?, ?, ?, ?, ?, ?, ?, 'free', 0, 50, ?, 0)
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
        if user["is_locked"]:
            return {"error": "Account is locked/suspended by Administrator. Contact Producer on WhatsApp to resolve."}
        update_user_streak(user["id"])
        return dict(user)
    return None

def get_user_by_id(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, phone, target_course, target_uni, target_score, plan, plan_expires_at, xp, created_at, is_locked FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return None
    user_dict = dict(user)

    cursor.execute("SELECT streak_count FROM user_streaks WHERE user_id = ?", (user_id,))
    streak_row = cursor.fetchone()
    user_dict["streak"] = streak_row["streak_count"] if streak_row else 1
    
    now = time.time()
    is_sub = bool(user_dict["plan_expires_at"] and user_dict["plan_expires_at"] > now)
    user_dict["is_subscribed"] = is_sub
    user_dict["days_left"] = max(0, int((user_dict["plan_expires_at"] - now) // 86400)) if is_sub else 0
    user_dict["hours_left"] = max(0, int((user_dict["plan_expires_at"] - now) // 3600)) if is_sub else 0
    user_dict["is_locked"] = bool(user_dict.get("is_locked", 0))
    
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

# ----------------- PRODUCER SETTINGS & DIRECT PAYMENTS -----------------
def get_producer_settings():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT key, value FROM producer_settings")
    rows = cursor.fetchall()
    conn.close()
    return {r["key"]: r["value"] for r in rows}

def update_producer_settings(settings_dict):
    conn = get_db_connection()
    cursor = conn.cursor()
    for k, v in settings_dict.items():
        cursor.execute("INSERT OR REPLACE INTO producer_settings (key, value) VALUES (?, ?)", (k, str(v).strip()))
    conn.commit()
    conn.close()
    return get_producer_settings()

def create_payment_order(reference, user_id, student_name, email, phone, plan_id, plan_name, amount_ngn, method='manual_transfer', notes=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO payment_orders (reference, user_id, student_name, email, phone, plan_id, plan_name, amount_ngn, status, method, receipt_notes, created_at)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?, ?, ?)
    """, (reference, user_id, student_name, email, phone, plan_id, plan_name, amount_ngn, method, notes, time.time()))
    conn.commit()
    conn.close()
    return reference

def get_payment_orders(status=None, limit=100):
    conn = get_db_connection()
    cursor = conn.cursor()
    if status:
        cursor.execute("SELECT * FROM payment_orders WHERE status = ? ORDER BY created_at DESC LIMIT ?", (status, limit))
    else:
        cursor.execute("SELECT * FROM payment_orders ORDER BY created_at DESC LIMIT ?", (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_payment_order_by_ref(reference):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_orders WHERE reference = ?", (reference.strip(),))
    row = cursor.fetchone()
    conn.close()
    return dict(row) if row else None

def confirm_payment_order(reference, confirmed_by='Producer'):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_orders WHERE reference = ?", (reference.strip(),))
    order = cursor.fetchone()
    if not order:
        conn.close()
        return {"error": "Order not found."}
    
    order = dict(order)
    plan_id = order["plan_id"]
    days = 30
    if plan_id == "weekly": days = 7
    elif plan_id == "season": days = 120

    user_id = order["user_id"]
    if not user_id and order.get("phone"):
        # Match user by phone or email
        u = cursor.execute("SELECT id FROM users WHERE phone = ? OR email = ?", (order["phone"], order["email"])).fetchone()
        if u:
            user_id = u["id"]

    now = time.time()
    cursor.execute("""
    UPDATE payment_orders
    SET status = 'confirmed', confirmed_by = ?, confirmed_at = ?
    WHERE reference = ?
    """, (confirmed_by, now, reference))
    conn.commit()
    conn.close()

    new_expiry = None
    if user_id:
        new_expiry = apply_subscription(user_id, plan_id, days)

    return {
        "status": "confirmed",
        "reference": reference,
        "student_name": order["student_name"],
        "plan_id": plan_id,
        "days": days,
        "user_id": user_id,
        "expires_at": new_expiry
    }

import secrets

def issue_voucher_for_order(reference):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM payment_orders WHERE reference = ?", (reference.strip(),))
    order = cursor.fetchone()
    if not order:
        conn.close()
        return {"error": "Order not found"}
    order = dict(order)
    plan_id = order["plan_id"]
    days = 30
    if plan_id == "weekly": days = 7
    elif plan_id == "season": days = 120

    code = f"PASS-2025-{plan_id.upper()}-{secrets.token_hex(3).upper()}"
    cursor.execute("INSERT OR REPLACE INTO vouchers (code, plan, days, is_used) VALUES (?, ?, ?, 0)", (code, plan_id, days))
    cursor.execute("UPDATE payment_orders SET issued_pin = ? WHERE reference = ?", (code, reference))
    conn.commit()
    conn.close()
    return {"status": "success", "pin_code": code, "plan_id": plan_id, "days": days}

def generate_vouchers(plan_id, days, count=10):
    conn = get_db_connection()
    cursor = conn.cursor()
    generated = []
    for _ in range(count):
        code = f"PASS-2025-{plan_id.upper()}-{secrets.token_hex(3).upper()}"
        cursor.execute("INSERT INTO vouchers (code, plan, days, is_used) VALUES (?, ?, ?, 0)", (code, plan_id, days))
        generated.append(code)
    conn.commit()
    conn.close()
    return generated

def get_all_vouchers(limit=200):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT v.*, u.name as redeemed_by_name, u.phone as redeemed_by_phone
    FROM vouchers v
    LEFT JOIN users u ON v.redeemed_by = u.id
    ORDER BY v.is_used ASC, v.redeemed_at DESC
    LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def get_all_users_admin(limit=100):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
    SELECT u.id, u.name, u.email, u.phone, u.target_course, u.target_uni, u.target_score,
           u.plan, u.plan_expires_at, u.xp, u.created_at, COALESCE(u.is_locked, 0) as is_locked,
           COUNT(a.id) as total_attempts,
           SUM(CASE WHEN a.is_correct = 1 THEN 1 ELSE 0 END) as correct_attempts,
           s.streak_count
    FROM users u
    LEFT JOIN attempts a ON u.id = a.user_id
    LEFT JOIN user_streaks s ON u.id = s.user_id
    GROUP BY u.id
    ORDER BY u.created_at DESC
    LIMIT ?
    """, (limit,))
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def manually_grant_user_pass(user_id, plan_id, days):
    new_expiry = apply_subscription(user_id, plan_id, days)
    return {"status": "success", "user_id": user_id, "plan_id": plan_id, "expires_at": new_expiry}

def lock_user_account(user_id, is_locked=1):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET is_locked = ? WHERE id = ?", (int(is_locked), user_id))
    conn.commit()
    conn.close()
    return {"success": True, "user_id": user_id, "is_locked": bool(is_locked)}

def strip_user_privileges(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE users SET plan = 'free', plan_expires_at = 0 WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return {"success": True, "user_id": user_id, "plan": "free", "plan_expires_at": 0}

def delete_user_by_producer(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM attempts WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM user_streaks WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    conn.close()
    return {"success": True, "user_id": user_id}

def can_register(email, phone):
    conn = get_db_connection()
    cursor = conn.cursor()
    e_clean = email.lower().strip()
    p_clean = phone.strip()
    
    # Check if explicitly in banned_identifiers
    cursor.execute("""
    SELECT * FROM banned_identifiers WHERE (LOWER(identifier) = ? OR identifier = ?) AND is_active = 1
    """, (e_clean, p_clean))
    banned = cursor.fetchone()
    if banned:
        conn.close()
        return False, "Over-usage abuse detected: This email or phone has been deleted more than 2 times and is banned. Contact Producer on WhatsApp to review and unban."

    # Check deletion count in account_deletions
    cursor.execute("""
    SELECT COUNT(*) as count FROM account_deletions WHERE LOWER(email) = ? OR phone = ?
    """, (e_clean, p_clean))
    row = cursor.fetchone()
    del_count = row["count"] if row else 0
    if del_count > 2:
        now = time.time()
        cursor.execute("INSERT OR REPLACE INTO banned_identifiers (identifier, reason, is_active, banned_at) VALUES (?, ?, 1, ?)",
                       (e_clean, "Account deleted >2 times (recycled abuse)", now))
        cursor.execute("INSERT OR REPLACE INTO banned_identifiers (identifier, reason, is_active, banned_at) VALUES (?, ?, 1, ?)",
                       (p_clean, "Account deleted >2 times (recycled abuse)", now))
        conn.commit()
        conn.close()
        return False, "Over-usage abuse detected: This email or phone has been deleted more than 2 times and is banned. Contact Producer on WhatsApp to review and unban."

    conn.close()
    return True, None

def delete_user_account(user_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, email, phone FROM users WHERE id = ?", (user_id,))
    user = cursor.fetchone()
    if not user:
        conn.close()
        return {"error": "User not found."}

    e_clean = user["email"].lower().strip()
    p_clean = user["phone"].strip()
    name = user["name"]
    now = time.time()

    # Log into account_deletions
    cursor.execute("""
    INSERT INTO account_deletions (email, phone, name, deleted_at) VALUES (?, ?, ?, ?)
    """, (e_clean, p_clean, name, now))

    # Check if this email or phone is now deleted > 2 times
    cursor.execute("SELECT COUNT(*) as count FROM account_deletions WHERE LOWER(email) = ? OR phone = ?", (e_clean, p_clean))
    count = cursor.fetchone()["count"]
    if count > 2:
        cursor.execute("INSERT OR REPLACE INTO banned_identifiers (identifier, reason, is_active, banned_at) VALUES (?, ?, 1, ?)",
                       (e_clean, "Recycled deletion limit reached (>2 times)", now))
        cursor.execute("INSERT OR REPLACE INTO banned_identifiers (identifier, reason, is_active, banned_at) VALUES (?, ?, 1, ?)",
                       (p_clean, "Recycled deletion limit reached (>2 times)", now))

    # Delete related user records
    cursor.execute("DELETE FROM attempts WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM user_streaks WHERE user_id = ?", (user_id,))
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))

    conn.commit()
    conn.close()
    return {"success": True, "message": "Account successfully deleted."}

def get_banned_identifiers():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM banned_identifiers ORDER BY banned_at DESC")
    rows = cursor.fetchall()
    conn.close()
    return [dict(r) for r in rows]

def toggle_banned_identifier(identifier, is_active=None):
    conn = get_db_connection()
    cursor = conn.cursor()
    ident = identifier.strip().lower()
    if is_active is None:
        cursor.execute("SELECT is_active FROM banned_identifiers WHERE LOWER(identifier) = ?", (ident,))
        row = cursor.fetchone()
        new_active = 0 if (row and row["is_active"] == 1) else 1
    else:
        new_active = 1 if is_active else 0

    cursor.execute("UPDATE banned_identifiers SET is_active = ? WHERE LOWER(identifier) = ?", (new_active, ident))
    if cursor.rowcount == 0:
        cursor.execute("INSERT INTO banned_identifiers (identifier, reason, is_active, banned_at) VALUES (?, 'Manually added by Producer', ?, ?)",
                       (ident, new_active, time.time()))
    conn.commit()
    conn.close()
    return {"success": True, "identifier": ident, "is_active": bool(new_active)}

def get_producer_kpis():
    conn = get_db_connection()
    cursor = conn.cursor()
    now = time.time()

    cursor.execute("SELECT COUNT(*) as count FROM users")
    total_users = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count FROM users WHERE plan_expires_at > ?", (now,))
    active_subscribers = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count, SUM(amount_ngn) as total_rev FROM payment_orders WHERE status = 'confirmed'")
    rev_row = cursor.fetchone()
    confirmed_orders = rev_row["count"] or 0
    total_revenue = rev_row["total_rev"] or 0

    cursor.execute("SELECT COUNT(*) as count FROM payment_orders WHERE status = 'pending'")
    pending_orders = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count, SUM(is_correct) as correct FROM attempts")
    att_row = cursor.fetchone()
    total_attempts = att_row["count"] or 0
    correct_attempts = att_row["correct"] or 0

    cursor.execute("SELECT COUNT(*) as count FROM vouchers WHERE is_used = 0")
    available_vouchers = cursor.fetchone()["count"]

    cursor.execute("SELECT COUNT(*) as count FROM banned_identifiers WHERE is_active = 1")
    banned_count = cursor.fetchone()["count"]

    conn.close()

    accuracy = int((correct_attempts / total_attempts * 100)) if total_attempts > 0 else 0

    return {
        "total_users": total_users,
        "active_subscribers": active_subscribers,
        "confirmed_orders": confirmed_orders,
        "total_revenue_ngn": total_revenue,
        "pending_orders": pending_orders,
        "total_attempts": total_attempts,
        "accuracy_pct": accuracy,
        "available_vouchers": available_vouchers,
        "banned_identifiers_count": banned_count
    }

