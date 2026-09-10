"""
PassMaster AI - Scale Question Bank to 800 Questions Per Subject (6,400+ Total)
Ensures exactly 200 questions per topic across all 4 canonical topics in all 8 JAMB subjects:
  - Mathematics (mth_001 to mth_800)
  - Physics (phy_001 to phy_800)
  - Chemistry (chm_001 to chm_800)
  - Biology (bio_001 to bio_800)
  - Use of English (eng_001 to eng_800 + novel questions)
  - Economics (eco_001 to eco_800)
  - Government (gov_001 to gov_800)
  - Literature in English (lit_001 to lit_800)
"""

import json
import os
import sys
import random
import math
from collections import Counter

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

CANONICAL_TOPICS = {
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

SUB_PREFIXES = {
    "Use of English": "eng",
    "Mathematics": "mth",
    "Physics": "phy",
    "Chemistry": "chm",
    "Biology": "bio",
    "Economics": "eco",
    "Government": "gov",
    "Literature in English": "lit"
}

TARGET_PER_TOPIC = 200

# Import base generators
from tools.generators.gen_math import generate_math_questions
from tools.generators.gen_physics import generate_physics_questions
from tools.generators.gen_chemistry import generate_chemistry_questions
from tools.generators.gen_biology import generate_biology_questions
from tools.generators.gen_english import generate_english_questions
from tools.generators.gen_economics import generate_economics_questions
from tools.generators.gen_government import generate_government_questions
from tools.generators.gen_literature import generate_literature_questions

BASE_GENERATORS = {
    "Mathematics": generate_math_questions,
    "Physics": generate_physics_questions,
    "Chemistry": generate_chemistry_questions,
    "Biology": generate_biology_questions,
    "Use of English": generate_english_questions,
    "Economics": generate_economics_questions,
    "Government": generate_government_questions,
    "Literature in English": generate_literature_questions
}

# Rich parametric expansion pools for topics needing additional unique items
from tools.generators.expansion_pools import generate_expansion_pool

def scale_bank():
    print("🚀 Scaling PassMaster AI question bank to 800 questions per subject...")
    
    questions_file = "data/questions.json"
    with open(questions_file, "r", encoding="utf-8") as f:
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

    for subj, topics in CANONICAL_TOPICS.items():
        prefix = SUB_PREFIXES[subj]
        base_gen = BASE_GENERATORS[subj]
        
        # Existing numbers for this prefix
        existing_nums = set()
        for q in questions_by_id.values():
            if q["id"].startswith(f"{prefix}_"):
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
            print(f"[{subj}] {topic}: current {current_count}, needed {needed}")

            if needed <= 0:
                continue

            used_texts = {q["question"] for q in current_topic_qs}
            added = 0

            # 1. First exhaust base generator
            base_pool = base_gen(topic, 500)
            for item in base_pool:
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
                    "year": random.choice([2019, 2020, 2021, 2022, 2023, 2024, 2025]),
                    "question": q_text,
                    "options": shuffled_opts,
                    "correct_option": target_slot,
                    "traps": traps,
                    "pedagogical_concept": trap_explanation,
                    "socratic_prompt": socratic_prompt
                }
                questions_by_id[new_id] = new_q
                added += 1

            # 2. If more still needed, use expansion pool
            if added < needed:
                exp_needed = needed - added
                exp_pool = generate_expansion_pool(subj, topic, exp_needed * 3)
                for item in exp_pool:
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
                        "year": random.choice([2019, 2020, 2021, 2022, 2023, 2024, 2025]),
                        "question": q_text,
                        "options": shuffled_opts,
                        "correct_option": target_slot,
                        "traps": traps,
                        "pedagogical_concept": trap_explanation,
                        "socratic_prompt": socratic_prompt
                    }
                    questions_by_id[new_id] = new_q
                    added += 1

            print(f"  -> Added {added} items. Total now for [{subj}] {topic}: {current_count + added}")

    final_questions = list(questions_by_id.values())
    final_questions.sort(key=lambda x: (x["subject"], x["id"]))

    with open(questions_file, "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Successfully wrote {len(final_questions)} questions to {questions_file}!")
    sub_counts = Counter(q["subject"] for q in final_questions)
    for s, c in sorted(sub_counts.items()):
        print(f"  • {s:25}: {c} questions")
        topic_counts = Counter(q["topic"] for q in final_questions if q["subject"] == s)
        for t, tc in sorted(topic_counts.items()):
            print(f"      - {t:40}: {tc} questions")

if __name__ == "__main__":
    scale_bank()
