import json
import os

QUESTIONS_PATH = "data/questions.json"

with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    existing_questions = json.load(f)

# Build map of existing questions
existing_map = {q["id"]: q for q in existing_questions}

# Canonical topic mapping to harmonize all questions
canonical_topics = {
    "Use of English": {
        "concord": "Concord & Grammar",
        "grammar": "Concord & Grammar",
        "lexis": "Lexis & Structure",
        "structure": "Lexis & Structure",
        "oral": "Oral Forms & Phonology",
        "phonology": "Oral Forms & Phonology",
        "comprehension": "Comprehension & Prescribed Text",
        "text": "Comprehension & Prescribed Text",
        "life changer": "Comprehension & Prescribed Text"
    },
    "Mathematics": {
        "algebra": "Algebra",
        "calculus": "Calculus",
        "geometry": "Geometry & Trigonometry",
        "trigonometry": "Geometry & Trigonometry",
        "statistics": "Statistics & Probability",
        "probability": "Statistics & Probability"
    },
    "Physics": {
        "mechanics": "Mechanics",
        "thermal": "Thermal Physics & Waves",
        "waves": "Thermal Physics & Waves",
        "optics": "Thermal Physics & Waves",
        "electricity": "Electricity & Magnetism",
        "magnetism": "Electricity & Magnetism",
        "modern": "Modern & Atomic Physics",
        "atomic": "Modern & Atomic Physics"
    },
    "Chemistry": {
        "physical": "Physical & General Chemistry",
        "general": "Physical & General Chemistry",
        "inorganic": "Inorganic Chemistry",
        "organic": "Organic Chemistry",
        "environmental": "Environmental & Industrial Chemistry",
        "applied": "Environmental & Industrial Chemistry",
        "industrial": "Environmental & Industrial Chemistry"
    },
    "Biology": {
        "cell": "Cellular Biology & Life Processes",
        "organization": "Cellular Biology & Life Processes",
        "cellular": "Cellular Biology & Life Processes",
        "physiology": "Human Physiology & Systems",
        "systems": "Human Physiology & Systems",
        "genetics": "Genetics & Evolution",
        "heredity": "Genetics & Evolution",
        "evolution": "Genetics & Evolution",
        "ecology": "Ecology & Environment",
        "environment": "Ecology & Environment"
    },
    "Economics": {
        "basic": "Basic Economic Principles & Methodology",
        "principles": "Basic Economic Principles & Methodology",
        "scarcity": "Basic Economic Principles & Methodology",
        "microeconomics": "Microeconomics & Price Mechanism",
        "price": "Microeconomics & Price Mechanism",
        "elasticity": "Microeconomics & Price Mechanism",
        "production": "Microeconomics & Price Mechanism",
        "market": "Microeconomics & Price Mechanism",
        "macroeconomics": "Macroeconomics & National Income",
        "national": "Macroeconomics & National Income",
        "money": "Money, Banking & Public Finance",
        "banking": "Money, Banking & Public Finance",
        "finance": "Money, Banking & Public Finance"
    },
    "Government": {
        "elements": "Elements of Government & Political Theory",
        "basic": "Elements of Government & Political Theory",
        "theory": "Elements of Government & Political Theory",
        "organs": "Elements of Government & Political Theory",
        "colonial": "Colonial Administration in Nigeria & West Africa",
        "indirect": "Colonial Administration in Nigeria & West Africa",
        "constitutional": "Nigerian Constitutional Development",
        "development": "Nigerian Constitutional Development",
        "federalism": "Federalism, Military Rule & Foreign Policy",
        "military": "Federalism, Military Rule & Foreign Policy",
        "foreign": "Federalism, Military Rule & Foreign Policy",
        "international": "Federalism, Military Rule & Foreign Policy"
    },
    "Literature in English": {
        "appreciation": "Literary Appreciation & Devices",
        "devices": "Literary Appreciation & Devices",
        "drama": "Drama & Theatrical Techniques",
        "theatrical": "Drama & Theatrical Techniques",
        "african prose & drama": "Drama & Theatrical Techniques",
        "poetry": "Poetry & Versification",
        "versification": "Poetry & Versification",
        "prose": "Prose & Fictional Techniques",
        "fictional": "Prose & Fictional Techniques",
        "non-african": "Prose & Fictional Techniques"
    }
}

# Harmonize existing questions' topic field
for q in existing_questions:
    s = q["subject"]
    t = q.get("topic", "").lower()
    if s in canonical_topics:
        for kw, canonical in canonical_topics[s].items():
            if kw in t:
                q["topic"] = canonical
                break

print(f"Existing questions harmonized: {len(existing_questions)}")
