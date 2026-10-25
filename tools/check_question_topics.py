import json

with open(r"F:\Antigravity\passmaster_ai\data\questions.json", "r", encoding="utf-8") as f:
    questions = json.load(f)

print(f"Total questions: {len(questions)}")
by_subj = {}
for q in questions:
    s = q.get("subject")
    t = q.get("topic")
    if s not in by_subj:
        by_subj[s] = set()
    by_subj[s].add(t)

for s, topics in by_subj.items():
    print(f"\n=== {s} ({len(topics)} question topics) ===")
    for t in sorted(topics):
        print(f"  - {t}")
