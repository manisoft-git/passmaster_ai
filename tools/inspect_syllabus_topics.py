import json

with open(r"F:\Antigravity\passmaster_ai\data\syllabus.json", "r", encoding="utf-8") as f:
    syl = json.load(f)

for subj, data in syl.items():
    print(f"\n=== {subj} ===")
    topics = data.get("topics", [])
    for t in topics:
        if isinstance(t, dict):
            print(f"  - {t.get('name')} (weight: {t.get('weight')}, questions: {t.get('typical_questions')})")
            subtopics = t.get("subtopics", [])
            if subtopics:
                print(f"      Subtopics ({len(subtopics)}): {', '.join(subtopics[:6])}...")
        else:
            print(f"  - {t}")
