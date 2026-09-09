import json
import os
import sys
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def generate_3200_question_bank():
    # Load existing questions to preserve backwards compatibility
    with open("data/questions.json", "r", encoding="utf-8") as f:
        existing_questions = json.load(f)
    
    questions_by_id = {}
    existing_by_subject_topic = {}
    
    for q in existing_questions:
        questions_by_id[q["id"]] = q
        s = q["subject"]
        t = q["topic"]
        if s not in existing_by_subject_topic:
            existing_by_subject_topic[s] = {}
        if t not in existing_by_subject_topic[s]:
            existing_by_subject_topic[s][t] = []
        existing_by_subject_topic[s][t].append(q)

    canonical_topics = {
        "Use of English": [
            "Concord & Grammar", "Lexis & Structure", "Oral Forms & Phonology", "Comprehension & Prescribed Text"
        ],
        "Mathematics": [
            "Algebra", "Calculus", "Geometry & Trigonometry", "Statistics & Probability"
        ],
        "Physics": [
            "Mechanics", "Thermal Physics & Waves", "Electricity & Magnetism", "Modern & Atomic Physics"
        ],
        "Chemistry": [
            "Physical & General Chemistry", "Inorganic Chemistry", "Organic Chemistry", "Environmental & Industrial Chemistry"
        ],
        "Biology": [
            "Cellular Biology & Life Processes", "Human Physiology & Systems", "Genetics & Evolution", "Ecology & Environment"
        ],
        "Economics": [
            "Basic Economic Principles & Methodology", "Microeconomics & Price Mechanism", "Macroeconomics & National Income", "Money, Banking & Public Finance"
        ],
        "Government": [
            "Elements of Government & Political Theory", "Colonial Administration in Nigeria & West Africa", "Nigerian Constitutional Development", "Federalism, Military Rule & Foreign Policy"
        ],
        "Literature in English": [
            "Literary Appreciation & Devices", "Drama & Theatrical Techniques", "Poetry & Versification", "Prose & Fictional Techniques"
        ]
    }

    sub_prefixes = {
        "Use of English": "eng",
        "Mathematics": "mth",
        "Physics": "phy",
        "Chemistry": "chm",
        "Biology": "bio",
        "Economics": "eco",
        "Government": "gov",
        "Literature in English": "lit"
    }

    # Import modular question generators for each subject
    from tools.generators.gen_math import generate_math_questions
    from tools.generators.gen_physics import generate_physics_questions
    from tools.generators.gen_chemistry import generate_chemistry_questions
    from tools.generators.gen_biology import generate_biology_questions
    from tools.generators.gen_english import generate_english_questions
    from tools.generators.gen_economics import generate_economics_questions
    from tools.generators.gen_government import generate_government_questions
    from tools.generators.gen_literature import generate_literature_questions

    generators = {
        "Mathematics": lambda t, c: generate_math_questions(t, c),
        "Physics": lambda t, c: generate_physics_questions(t, c),
        "Chemistry": lambda t, c: generate_chemistry_questions(t, c),
        "Biology": lambda t, c: generate_biology_questions(t, c),
        "Use of English": lambda t, c: generate_english_questions(t, c),
        "Economics": lambda t, c: generate_economics_questions(t, c),
        "Government": lambda t, c: generate_government_questions(t, c),
        "Literature in English": lambda t, c: generate_literature_questions(t, c)
    }

    # Target: 100 questions per topic * 4 topics = 400 questions per subject
    TARGET_PER_TOPIC = 100

    print("Generating comprehensive 3,200 question bank (400 per subject, 100 per topic)...")

    for subj, topics in canonical_topics.items():
        prefix = sub_prefixes[subj]
        gen_fn = generators[subj]
        
        # Determine current allocated question numbers for this subject
        existing_nums = set()
        for q in questions_by_id.values():
            if q["subject"] == subj and q["id"].startswith(f"{prefix}_"):
                try:
                    num = int(q["id"].split("_")[1])
                    existing_nums.add(num)
                except ValueError:
                    pass

        next_id_num = 1
        
        for topic in topics:
            current_topic_qs = existing_by_subject_topic.get(subj, {}).get(topic, [])
            current_count = len(current_topic_qs)
            needed = TARGET_PER_TOPIC - current_count
            print(f"  [{subj}] {topic}: current {current_count}, needed {needed}")
            
            if needed <= 0:
                continue

            # Generate pool of candidate items for this topic
            pool = gen_fn(topic, needed * 2)
            used_texts = {q["question"] for q in current_topic_qs}
            
            added = 0
            for item in pool:
                if added >= needed:
                    break
                
                subtop, q_text, opts, correct_opt, trap_explanation, socratic_prompt = item
                if q_text in used_texts:
                    continue
                used_texts.add(q_text)
                
                while next_id_num in existing_nums:
                    next_id_num += 1
                
                new_id = f"{prefix}_{next_id_num:03d}"
                existing_nums.add(next_id_num)
                
                # Balanced option distribution (rotate correct answers across A, B, C, D)
                target_slot = ["A", "B", "C", "D"][next_id_num % 4]
                shuffled_opts = dict(opts)
                if target_slot != correct_opt:
                    c_text = shuffled_opts[correct_opt]
                    d_text = shuffled_opts[target_slot]
                    shuffled_opts[target_slot] = c_text
                    shuffled_opts[correct_opt] = d_text
                
                traps = {}
                for k in ["A", "B", "C", "D"]:
                    if k != target_slot:
                        traps[k] = f"You selected option {k}. {trap_explanation}"
                
                new_q = {
                    "id": new_id,
                    "subject": subj,
                    "topic": topic,
                    "subtopic": subtop,
                    "year": random.choice([2019, 2020, 2021, 2022, 2023, 2024]),
                    "question": q_text,
                    "options": shuffled_opts,
                    "correct_option": target_slot,
                    "traps": traps,
                    "pedagogical_concept": trap_explanation,
                    "socratic_prompt": socratic_prompt
                }
                questions_by_id[new_id] = new_q
                added += 1

    final_questions = list(questions_by_id.values())
    final_questions.sort(key=lambda x: (x["subject"], x["id"]))

    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Successfully wrote {len(final_questions)} questions to data/questions.json!")
    
    from collections import Counter
    sub_counts = Counter(q["subject"] for q in final_questions)
    for s, c in sorted(sub_counts.items()):
        print(f"  • {s:25}: {c} questions")
        topic_counts = Counter(q["topic"] for q in final_questions if q["subject"] == s)
        for t, tc in sorted(topic_counts.items()):
            print(f"      - {t:40}: {tc} questions")

if __name__ == "__main__":
    generate_3200_question_bank()
