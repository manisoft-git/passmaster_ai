import json

with open("data/syllabus.json", "r", encoding="utf-8") as f:
    syl = json.load(f)

for subj, data in syl.items():
    print(f"\n=== {subj} ===")
    for t in data["topics"]:
        print(f"  [{t['name']}] (weight: {t.get('weight_pct')}%)")
        for st in t.get("subtopics", []):
            print(f"    - {st}")
