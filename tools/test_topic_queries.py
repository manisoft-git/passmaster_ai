import sys, os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import urllib.parse
from app import app

client = app.test_client()

# Unencoded test
res = client.get('/api/questions?subject=Use of English&topic=Clause & Sentence Foundations')
print('Unencoded count:', res.json.get('count'))

# Encoded test
res2 = client.get(f'/api/questions?subject={urllib.parse.quote("Use of English")}&topic={urllib.parse.quote("Clause & Sentence Foundations")}')
print('Encoded count:', res2.json.get('count'))

# Test all 48 topics unencoded
import json
with open('data/syllabus.json', 'r', encoding='utf-8') as f:
    syl = json.load(f)

failures = []
for subj, d in syl.items():
    for t in d['topics']:
        name = t['name']
        r = client.get(f'/api/questions?subject={subj}&topic={name}')
        c = r.json.get('count', 0)
        if c < 5:
            failures.append((subj, name, c))

if not failures:
    print('ALL 48 SYLLABUS TOPICS RETURN AT LEAST 5 QUESTIONS WITH RAW (UNENCODED) QUERY STRINGS!')
else:
    print('Failures:', failures)
