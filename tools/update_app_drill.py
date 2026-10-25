import re

with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

target = """        questions = matched_questions if matched_questions else [
            q for q in questions if q.get('topic', '').lower() == topic.lower()
        ]"""

replacement = """        TOPIC_DRILL_FALLBACKS = {
            "Parts of Speech Foundations": "Lexis & Structure",
            "Clause & Sentence Foundations": "Concord & Grammar",
            "Arithmetic & Algebraic Foundations": "Algebra",
            "Coordinate & Function Foundations": "Algebra",
            "Units, Dimensions & Vectors": "Mechanics",
            "Kinetic Theory & Heat Fundamentals": "Thermal Physics & Waves",
            "Atomic & Bonding Foundations": "Physical & General Chemistry",
            "Chemical Equations & Stoichiometric Foundations": "Physical & General Chemistry",
            "Biological Molecules & Cell Foundations": "Cellular Biology & Life Processes",
            "Chromosomes & Cell Division Foundations": "Genetics & Evolution",
            "Foundational Economic Reasoning": "Basic Economic Principles & Methodology",
            "Economic Graphing & Elasticity Foundations": "Microeconomics & Price Mechanism",
            "Political Concepts & The State Foundations": "Elements of Government & Political Theory",
            "Pre-Colonial Heritage Foundations": "Colonial Administration in Nigeria & West Africa",
            "Literary Genres & Fundamentals": "Literary Appreciation & Devices",
            "Figurative Devices & Tropes Foundations": "Literary Appreciation & Devices",
        }
        if len(matched_questions) < 5 and topic in TOPIC_DRILL_FALLBACKS:
            fallback_target = TOPIC_DRILL_FALLBACKS[topic]
            matched_questions = [
                q for q in questions if q.get('topic', '').lower() == fallback_target.lower()
            ]

        questions = matched_questions if matched_questions else [
            q for q in questions if q.get('topic', '').lower() == topic.lower()
        ]"""

content = content.replace("\r\n", "\n")
target = target.replace("\r\n", "\n")
replacement = replacement.replace("\r\n", "\n")

if target in content:
    content = content.replace(target, replacement, 1)
    with open("app.py", "w", encoding="utf-8") as f:
        f.write(content)
    print("Successfully patched app.py with TOPIC_DRILL_FALLBACKS!")
else:
    print("Target not found in app.py!")
