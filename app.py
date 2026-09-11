import os
import json
import time
import secrets
import random
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
        code = 403 if "Over-usage" in res["error"] else 400
        return jsonify({"error": res["error"]}), code

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
    if isinstance(user, dict) and "error" in user:
        return jsonify({"error": user["error"]}), 403

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

@app.route('/api/auth/delete-account', methods=['POST'])
def delete_account():
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({"error": "Unauthorized"}), 401

    res = db.delete_user_account(user_id)
    session.clear()
    if "error" in res:
        return jsonify({"error": res["error"]}), 400
    return jsonify({"status": "success", "message": "Your account has been deleted."})

@app.route('/api/auth/preferences', methods=['GET', 'POST'])
def handle_preferences():
    user_id = session.get('user_id')
    user = db.get_user_by_id(user_id) if user_id else None

    if request.method == 'POST':
        data = request.get_json() or {}
        
        # STRICT SECURITY AUDIT: Verify candidate cannot alter sensitive identifiers
        forbidden_modifications = []
        if "email" in data and user and data["email"].strip().lower() != user["email"].strip().lower():
            forbidden_modifications.append("email")
        if "phone" in data and user and data["phone"].strip() != user["phone"].strip():
            forbidden_modifications.append("phone")
        if "name" in data and user and data["name"].strip() != user["name"].strip():
            forbidden_modifications.append("name")
        if "id" in data and user and int(data["id"]) != user["id"]:
            forbidden_modifications.append("id")

        if forbidden_modifications:
            return jsonify({
                "error": f"Candidate identity protection: You cannot modify sensitive records ({', '.join(forbidden_modifications)}). Contact Producer to update verified candidate information."
            }), 403

        # Extract allowed study preferences
        q_per_subj = int(data.get("questions_per_subject", 20))
        if q_per_subj not in [10, 20, 30, 40]:
            q_per_subj = 20

        subjects = data.get("subjects", ["Use of English", "Mathematics", "Physics", "Chemistry"])
        if not isinstance(subjects, list) or len(subjects) != 4:
            subjects = ["Use of English", "Mathematics", "Physics", "Chemistry"]
        if not any("english" in s.lower() for s in subjects):
            subjects[0] = "Use of English"

        target_course = data.get("target_course", user["target_course"] if user else "Medicine & Surgery")
        target_uni = data.get("target_uni", user["target_uni"] if user else "UNILAG")
        target_score = int(data.get("target_score", user["target_score"] if user else 280))
        timer_mode = data.get("cbt_timer_mode", "standard")
        sound_enabled = bool(data.get("sound_enabled", True))
        socratic_hints = bool(data.get("socratic_hints", True))

        if user_id:
            conn = db.get_db_connection()
            cursor = conn.cursor()
            cursor.execute("""
            UPDATE users SET target_course = ?, target_uni = ?, target_score = ? WHERE id = ?
            """, (target_course, target_uni, target_score, user_id))
            conn.commit()
            conn.close()

        prefs = {
            "questions_per_subject": q_per_subj,
            "subjects": subjects,
            "target_course": target_course,
            "target_uni": target_uni,
            "target_score": target_score,
            "cbt_timer_mode": timer_mode,
            "sound_enabled": sound_enabled,
            "socratic_hints": socratic_hints
        }
        return jsonify({
            "status": "success",
            "message": "Preferences saved successfully.",
            "preferences": prefs
        })

    # GET
    prefs = {
        "questions_per_subject": 20,
        "subjects": ["Use of English", "Mathematics", "Physics", "Chemistry"],
        "target_course": user["target_course"] if user else "Medicine & Surgery",
        "target_uni": user["target_uni"] if user else "UNILAG",
        "target_score": user["target_score"] if user else 280,
        "cbt_timer_mode": "standard",
        "sound_enabled": True,
        "socratic_hints": True
    }
    return jsonify({"status": "success", "preferences": prefs})

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
    topic = request.args.get('topic')
    limit = request.args.get('limit', type=int)
    is_random = request.args.get('random', '').lower() in ['true', '1', 'yes']
    mode = request.args.get('mode', 'drill')  # 'drill', 'topic', 'full_jamb'

    questions = list(tutor.questions.values())

    if mode == 'full_jamb':
        # Official JAMB 2-Hour 180-Question Mock: English (60 Qs) + 3 Chosen Electives (40 Qs each)
        selected_subjects_param = request.args.get('subjects', 'Use of English,Mathematics,Physics,Chemistry')
        selected_subs = [s.strip() for s in selected_subjects_param.split(',') if s.strip()]
        
        # Ensure Use of English is always present
        if not any('english' in s.lower() for s in selected_subs):
            selected_subs.insert(0, 'Use of English')
        
        mock_questions = []
        for s_name in selected_subs:
            s_pool = [dict(q) for q in questions if q['subject'].lower() == s_name.lower()]
            random.shuffle(s_pool)
            target_count = 60 if 'english' in s_name.lower() else 40
            if s_pool:
                while len(s_pool) < target_count:
                    s_pool.extend([dict(x) for x in s_pool])
                mock_questions.extend(s_pool[:target_count])
        
        resp = jsonify({
            "status": "success",
            "mode": "full_jamb",
            "count": len(mock_questions),
            "duration_minutes": 120,
            "questions": mock_questions
        })
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return resp

    if mode in ['jamb_standard', 'fast_mock', 'cbt_standard'] or request.args.get('questions_per_subject', type=int) is not None:
        # Standard JAMB Simulation: 20 random questions per subject (default 80 Qs for 4 subjects)
        q_per_subj = request.args.get('questions_per_subject', 20, type=int)
        if not q_per_subj or q_per_subj <= 0:
            q_per_subj = 20
        selected_subjects_param = request.args.get('subjects', 'Use of English,Mathematics,Physics,Chemistry')
        selected_subs = [s.strip() for s in selected_subjects_param.split(',') if s.strip()]
        if not any('english' in s.lower() for s in selected_subs):
            selected_subs.insert(0, 'Use of English')

        mock_questions = []
        for s_name in selected_subs:
            s_pool = [dict(q) for q in questions if q['subject'].lower() == s_name.lower()]
            random.shuffle(s_pool)
            if s_pool:
                mock_questions.extend(s_pool[:q_per_subj])

        calc_duration = int(len(mock_questions) * 1.0)
        resp = jsonify({
            "status": "success",
            "mode": "jamb_standard",
            "questions_per_subject": q_per_subj,
            "count": len(mock_questions),
            "duration_minutes": max(20, calc_duration),
            "questions": mock_questions
        })
        resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
        return resp

    if subject and subject.lower() != 'all':
        questions = [q for q in questions if q['subject'].lower() == subject.lower()]

    if topic and topic.lower() != 'all':
        def _norm(s):
            return s.lower().replace('&', 'and').replace(',', ' ').replace('-', ' ').replace('/', ' ').split()
        
        target_norm = _norm(topic)
        target_str = " ".join(target_norm)
        
        matched_questions = []
        for q in questions:
            q_topic = q.get('topic', '')
            q_subtopic = q.get('subtopic', '')
            # Exact or direct lower match
            if q_topic.lower() == topic.lower() or q_subtopic.lower() == topic.lower():
                matched_questions.append(q)
                continue
            # Normalized substring or word set match
            q_top_norm = _norm(q_topic)
            q_sub_norm = _norm(q_subtopic)
            q_top_str = " ".join(q_top_norm)
            if target_str in q_top_str or q_top_str in target_str:
                matched_questions.append(q)
                continue
            if set(target_norm).issubset(set(q_top_norm)) or set(target_norm).issubset(set(q_sub_norm)):
                matched_questions.append(q)
                continue
        
        questions = matched_questions if matched_questions else [
            q for q in questions if q.get('topic', '').lower() == topic.lower()
        ]

    # Always shuffle if random is requested or default random for drills
    if is_random or request.args.get('random') is None:
        questions = [dict(q) for q in questions]
        random.shuffle(questions)

    if limit and limit > 0:
        questions = questions[:limit]

    resp = jsonify({"status": "success", "count": len(questions), "questions": questions})
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return resp

@app.route('/api/syllabus', methods=['GET'])
def get_syllabus():
    return jsonify({"status": "success", "syllabus": diagnostics.syllabus})

@app.route('/api/drill/weakness', methods=['GET'])
def get_weakness_drill():
    """
    Analyzes student's recorded mistake vault & attempt history to pinpoint weak syllabus topics,
    dynamically assembling an intensive 15-question remedial drill tailored to those weaknesses.
    If student has no recorded history or is not logged in, delivers high-yield diagnostic questions.
    """
    user_id = session.get('user_id')
    weak_topics = []
    mistakes = []

    if user_id:
        mistakes = db.get_mistake_vault(user_id)
        if mistakes:
            top_counts = Counter(m.get('topic') for m in mistakes if m.get('topic'))
            weak_topics = [t for t, _ in top_counts.most_common(4)]

    # If no user-specific weak topics found, default to universally challenging JAMB trap topics
    if not weak_topics:
        weak_topics = [
            "Concord & Grammar",
            "Calculus",
            "Organic Chemistry",
            "Electricity & Magnetism",
            "Microeconomics & Price Mechanism",
            "Genetics & Evolution"
        ]

    remedial_pool = [
        dict(q) for q in tutor.questions.values()
        if q.get('topic') in weak_topics
    ]
    random.shuffle(remedial_pool)
    selected_questions = remedial_pool[:15]

    if len(selected_questions) < 10:
        all_q = list(tutor.questions.values())
        random.shuffle(all_q)
        selected_questions = all_q[:15]

    resp = jsonify({
        "status": "success",
        "mode": "weakness_drill",
        "weak_topics": weak_topics,
        "mistake_count_analyzed": len(mistakes),
        "count": len(selected_questions),
        "duration_minutes": 15,
        "questions": selected_questions
    })
    resp.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    return resp

# ----------------- TOPIC MASTER LESSONS API -----------------
LESSONS_PATH = os.path.join(os.path.dirname(__file__), "data", "lessons.json")

def load_lessons_db():
    try:
        with open(LESSONS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading lessons: {e}")
        return {}

@app.route('/api/lessons', methods=['GET'])
def get_lessons():
    subject = request.args.get('subject')
    data = load_lessons_db()

    user_id = session.get('user_id')
    user = db.get_user_by_id(user_id) if user_id else None
    is_sub = bool(user and user.get('is_subscribed'))

    lessons_list = []
    for subj, topic_list in data.items():
        if subject and subject.lower() != 'all' and subj.lower() != subject.lower():
            continue
        for idx, l in enumerate(topic_list):
            is_locked = (idx > 0 and not is_sub)
            v_meta = l.get("video_meta") or l.get("video") or {}
            lessons_list.append({
                "id": l["id"],
                "subject": subj,
                "topic": l["topic"],
                "title": l["title"],
                "category": l.get("category", "Core JAMB Syllabus Masterclass"),
                "jamb_weight": l.get("jamb_weight", ""),
                "summary": l.get("overview", "")[:180] + "...",
                "prerequisites": l.get("prerequisites", []),
                "prepares_for": l.get("prepares_for", []),
                "cbt_drill_topic": l.get("cbt_drill_topic", l["topic"]),
                "is_locked": is_locked,
                "is_preview": (idx == 0),
                "has_video": True,
                "video_duration": v_meta.get("duration", "25:00"),
                "video_title": v_meta.get("title", f"JAMB Masterclass: {l.get('title', l['topic'])}"),
                "youtube_id": v_meta.get("youtube_id", "")
            })

    return jsonify({"status": "success", "count": len(lessons_list), "lessons": lessons_list, "by_subject": data})

@app.route('/api/lessons/<subject>/<topic>', methods=['GET'])
def get_single_lesson(subject, topic):
    data = load_lessons_db()
    subj_lessons = None
    subj_key = subject
    for k, v in data.items():
        if k.lower() == subject.lower():
            subj_lessons = v
            subj_key = k
            break
    
    if not subj_lessons:
        return jsonify({"error": f"Subject '{subject}' not found."}), 404
    
    target_lesson = None
    lesson_idx = 0
    for idx, l in enumerate(subj_lessons):
        if l["topic"].lower() == topic.lower():
            target_lesson = l
            lesson_idx = idx
            break
    
    if not target_lesson:
        return jsonify({"error": f"Topic '{topic}' not found."}), 404

    # Subscription Access Check
    user_id = session.get('user_id')
    user = db.get_user_by_id(user_id) if user_id else None
    is_sub = bool(user and user.get('is_subscribed'))

    # Lesson index 0 is Free Preview for all candidates.
    # Subsequent lessons require an active Pass.
    if lesson_idx > 0 and not is_sub:
        return jsonify({
            "error": "This Topic Masterclass requires an active subscription pass.",
            "requires_pass": True,
            "lesson": {
                "id": target_lesson["id"],
                "subject": subj_key,
                "topic": target_lesson["topic"],
                "title": target_lesson["title"],
                "is_locked": True
            }
        }), 403

    lesson_obj = dict(target_lesson)
    lesson_obj["subject"] = subj_key
    lesson_obj["key_rule_or_formula"] = target_lesson.get("golden_rule") or "Master core syllabus principles."
    
    key_concepts_text = ""
    if "key_concepts" in target_lesson:
        key_concepts_text = "\n\n" + "\n\n".join([
            f"📌 {c.get('concept', '')}:\n{c.get('explanation', '')}\n• " + "\n• ".join(c.get('examples', []))
            for c in target_lesson["key_concepts"]
        ])
    worked_ex_text = ""
    if "worked_examples" in target_lesson and target_lesson["worked_examples"]:
        worked_ex_text = "\n\n━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n📝 AUTHENTIC JAMB WORKED EXAMPLE:\n" + "\n\n".join([
            f"❓ {we.get('question', '')}\n" +
            "\n".join(we.get('options', [])) +
            f"\n\n💡 Step-by-Step Solution & Trap Breakdown:\n{we.get('solution', '')}"
            for we in target_lesson["worked_examples"]
        ])
    lesson_obj["content"] = target_lesson.get("overview", "") + key_concepts_text + worked_ex_text
    lesson_obj["common_traps"] = "\n".join(target_lesson.get("fatal_traps", []))
    lesson_obj["secret_tip"] = target_lesson.get("golden_rule", "")
    lesson_obj["worked_examples"] = target_lesson.get("worked_examples", [])
    lesson_obj["key_terms"] = target_lesson.get("key_terms", [])
    lesson_obj["prerequisites"] = target_lesson.get("prerequisites", [])
    lesson_obj["from_scratch_guide"] = target_lesson.get("from_scratch_guide", "")
    lesson_obj["prepares_for"] = target_lesson.get("prepares_for", [])
    lesson_obj["category"] = target_lesson.get("category", "Core JAMB Syllabus Masterclass")
    lesson_obj["cbt_drill_topic"] = target_lesson.get("cbt_drill_topic", target_lesson.get("topic"))
    lesson_obj["diagram_key"] = target_lesson.get("topic", topic)
    
    # Authentic video metadata
    if "video_meta" in target_lesson and target_lesson["video_meta"]:
        lesson_obj["video_meta"] = target_lesson["video_meta"]
    elif "video" in target_lesson and target_lesson["video"]:
        lesson_obj["video_meta"] = target_lesson["video"]
    else:
        lesson_obj["video_meta"] = {
            "youtube_id": "_xWp-zN85_Y",
            "title": f"JAMB Masterclass: {target_lesson.get('title', topic)}",
            "duration": "24:30",
            "lecturer": "Coach Kalu & Socratic Video Fellow",
            "chapters": [
                {"time": "00:00", "title": "Zero-to-One Conceptual Foundations"},
                {"time": "06:15", "title": "Core Laws, Equations & Definitions"},
                {"time": "14:20", "title": "Authentic JAMB Past Questions Solved"},
                {"time": "20:50", "title": "Fatal Cognitive Traps & Heuristics"}
            ],
            "key_takeaways": [
                "Master core foundational axioms without rote memorization.",
                "Identify subtle distractor traps designed to catch unwary candidates.",
                "Use speed heuristics to answer questions within 45 seconds."
            ]
        }

    return jsonify({
        "status": "success",
        "requires_pass": False,
        "lesson": lesson_obj
    })

# ----------------- JAMB NOVEL & FORMULAS API -----------------
NOVEL_PATH = os.path.join(os.path.dirname(__file__), "data", "novel_companion.json")
FORMULAS_PATH = os.path.join(os.path.dirname(__file__), "data", "formulas.json")

def load_novel_companion():
    try:
        with open(NOVEL_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading novel companion: {e}")
        return {}

def load_formulas():
    try:
        with open(FORMULAS_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading formulas: {e}")
        return []

@app.route('/api/novel', methods=['GET'])
def get_novel_companion():
    data = load_novel_companion()
    chapter = request.args.get('chapter', type=int)
    if chapter:
        chapters = data.get("chapters", [])
        matched = next((c for c in chapters if c["chapter_number"] == chapter), None)
        if not matched:
            return jsonify({"error": f"Chapter {chapter} not found."}), 404
        return jsonify({"status": "success", "novel_title": data.get("novel_title"), "chapter": matched})
    return jsonify({"status": "success", "companion": data})

@app.route('/api/novel/drill', methods=['GET'])
def get_novel_drill():
    limit = request.args.get('limit', default=10, type=int)
    data = load_novel_companion()
    novel_qs = list(data.get("questions", []))
    for q in tutor.questions.values():
        if "the life changer" in str(q.get("subtopic", "")).lower() or "the life changer" in str(q.get("question", "")).lower():
            if not any(x["id"] == q["id"] for x in novel_qs):
                novel_qs.append(dict(q))
    random.shuffle(novel_qs)
    selected = novel_qs[:limit]
    return jsonify({
        "status": "success",
        "count": len(selected),
        "questions": selected,
        "mode": "novel_drill",
        "title": "JAMB Prescribed Novel Drill: The Life Changer"
    })

@app.route('/api/formulas', methods=['GET'])
def get_formulas():
    formulas = load_formulas()
    subject = request.args.get('subject')
    search = request.args.get('search', '').strip().lower()
    
    filtered = formulas
    if subject and subject.lower() != 'all':
        filtered = [f for f in filtered if f.get('subject', '').lower() == subject.lower()]
        
    if search:
        filtered = [
            f for f in filtered
            if search in f.get('title', '').lower()
            or search in f.get('formula', '').lower()
            or search in f.get('topic', '').lower()
            or search in f.get('mnemonic', '').lower()
        ]
        
    return jsonify({"status": "success", "count": len(filtered), "formulas": filtered})

# ----------------- DEVELOPER SUPPORT BIO API -----------------
@app.route('/api/support/bio', methods=['GET'])
def get_support_bio():
    settings = db.get_producer_settings()
    return jsonify({
        "status": "success",
        "founder_name": "Manifest Subeno",
        "school": "Good Shepherd Catholic College, Oyede",
        "class_level": "Entering SS3",
        "company": "Mani$oft",
        "bio": settings.get("producer_support_bio", ""),
        "bank_name": settings.get("producer_bank_name", "First Bank"),
        "account_number": settings.get("producer_account_number", "3050550518"),
        "account_name": settings.get("producer_account_name", "Manifest Subeno"),
        "whatsapp_phone": settings.get("producer_whatsapp_phone", "2348091977795")
    })

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
    message = data.get('message', '').strip()

    if not message:
        return jsonify({"error": "Please ask Coach Kalu a question."}), 400

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
    cheat_count = int(data.get('cheat_count', 0))

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
        candidate_name, target_course, target_uni, score_data, leaks, cheat_count=cheat_count
    )

    return jsonify({"status": "success", "card_text": card_text})

@app.route('/api/diagnostics/admission-chance', methods=['POST'])
def calculate_admission_chance():
    data = request.get_json() or {}
    university = data.get('university', 'UNILAG')
    course = data.get('course', 'Medicine & Surgery')
    jamb_score = data.get('jamb_score', 280)
    olevel_grades = data.get('olevel_grades', {})
    post_utme = data.get('post_utme_score')

    user_id = session.get('user_id')
    if user_id:
        user = db.get_user_by_id(user_id)
        if user and not data.get('course'):
            course = user['target_course']
        if user and not data.get('university'):
            university = user['target_uni']

    res = diagnostics.calculate_admission_chances(
        university=university,
        course=course,
        jamb_score=jamb_score,
        olevel_grades=olevel_grades,
        post_utme_score=post_utme
    )
    return jsonify({"status": "success", "data": res})

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
        "weekly": {"name": "Weekly Drill Pass", "amount": 1500},
        "monthly": {"name": "Monthly Master Pass", "amount": 3500},
        "season": {"name": "Full Season Guarantee Pass", "amount": 8500}
    }
    plan_meta = pricing.get(plan_id, {"name": "Monthly Master Pass", "amount": 3500})

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
            if entered_key == console_pass or entered_key in ['$$manisoft11console', '$$lumina11']:
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
    bans = db.get_banned_identifiers()
    return render_template('producer_panel.html', settings=settings, kpis=kpis, orders=orders, vouchers=vouchers, users=users, bans=bans)

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

@app.route('/api/producer/users/delete', methods=['POST'])
def api_producer_delete_user():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    res = db.delete_user_by_producer(user_id)
    return jsonify(res)

@app.route('/api/producer/users/toggle-lock', methods=['POST'])
def api_producer_toggle_lock():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    user_id = data.get('user_id')
    is_locked = data.get('is_locked', 1)
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    res = db.lock_user_account(user_id, is_locked)
    return jsonify(res)

@app.route('/api/producer/users/strip-privileges', methods=['POST'])
def api_producer_strip_privileges():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    user_id = data.get('user_id')
    if not user_id:
        return jsonify({"error": "Missing user_id"}), 400
    res = db.strip_user_privileges(user_id)
    return jsonify(res)

@app.route('/api/producer/bans', methods=['GET'])
def api_producer_get_bans():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    bans = db.get_banned_identifiers()
    return jsonify({"status": "success", "bans": bans})

@app.route('/api/producer/bans/toggle', methods=['POST'])
def api_producer_toggle_ban():
    if not session.get('producer_unlocked'):
        return jsonify({"error": "Unauthorized"}), 403
    data = request.get_json() or {}
    identifier = data.get('identifier')
    is_active = data.get('is_active')
    if not identifier:
        return jsonify({"error": "Missing identifier"}), 400
    res = db.toggle_banned_identifier(identifier, is_active)
    return jsonify(res)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5050))
    print(f"🚀 PassMaster AI Server running on http://127.0.0.1:{port}")
    app.run(host='0.0.0.0', port=port, debug=False)
