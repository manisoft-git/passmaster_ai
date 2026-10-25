import re

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

target = """    topic = request.args.get('topic')
    limit = request.args.get('limit', type=int)"""

replacement = """    topic = request.args.get('topic')
    # Reconstruct topic if client query contained unencoded ampersand (e.g. ?topic=Clause & Sentence Foundations)
    if topic:
        for k in request.args:
            if k not in ['subject', 'topic', 'limit', 'random', 'mode', 'subjects', 'questions_per_subject', '_t']:
                cand = f"{topic}&{k}".strip()
                if cand in TOPIC_DRILL_FALLBACKS or any(cand.lower() == t.get('name', '').lower() for s in diagnostics.syllabus.values() for t in s.get('topics', [])):
                    topic = cand
                    break

    limit = request.args.get('limit', type=int)"""

content = content.replace("\r\n", "\n")
target = target.replace("\r\n", "\n")
replacement = replacement.replace("\r\n", "\n")

if target in content:
    content = content.replace(target, replacement, 1)
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched app.py with ampersand reconstruction!")
else:
    print("Target not found in app.py!")
