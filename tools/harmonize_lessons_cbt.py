import json
import os

TOPIC_DRILL_MAP = {
    # Use of English
    "Concord & Grammar": "Concord & Grammar",
    "Lexis & Structure": "Lexis & Structure",
    "Oral Forms & Phonology": "Oral Forms & Phonology",
    "Comprehension & Prescribed Text": "Comprehension & Prescribed Text",
    "Parts of Speech Foundations": "Lexis & Structure",
    "Clause & Sentence Foundations": "Concord & Grammar",
    
    # Mathematics
    "Algebra": "Algebra",
    "Calculus": "Calculus",
    "Geometry & Trigonometry": "Geometry & Trigonometry",
    "Statistics & Probability": "Statistics & Probability",
    "Arithmetic & Algebraic Foundations": "Algebra",
    "Coordinate & Function Foundations": "Algebra",
    
    # Physics
    "Mechanics": "Mechanics",
    "Thermal Physics & Waves": "Thermal Physics & Waves",
    "Electricity & Magnetism": "Electricity & Magnetism",
    "Modern & Atomic Physics": "Modern & Atomic Physics",
    "Units, Dimensions & Vectors": "Mechanics",
    "Kinetic Theory & Heat Fundamentals": "Thermal Physics & Waves",
    
    # Chemistry
    "Physical & General Chemistry": "Physical & General Chemistry",
    "Inorganic Chemistry": "Inorganic Chemistry",
    "Organic Chemistry": "Organic Chemistry",
    "Environmental & Industrial Chemistry": "Environmental & Industrial Chemistry",
    "Atomic & Bonding Foundations": "Physical & General Chemistry",
    "Chemical Equations & Stoichiometric Foundations": "Physical & General Chemistry",
    
    # Biology
    "Cellular Biology & Life Processes": "Cellular Biology & Life Processes",
    "Human Physiology & Systems": "Human Physiology & Systems",
    "Genetics & Evolution": "Genetics & Evolution",
    "Ecology & Environment": "Ecology & Environment",
    "Biological Molecules & Cell Foundations": "Cellular Biology & Life Processes",
    "Chromosomes & Cell Division Foundations": "Genetics & Evolution",
    
    # Economics
    "Basic Economic Principles & Methodology": "Basic Economic Principles & Methodology",
    "Microeconomics & Price Mechanism": "Microeconomics & Price Mechanism",
    "Macroeconomics & National Income": "Macroeconomics & National Income",
    "Money, Banking & Public Finance": "Money, Banking & Public Finance",
    "Foundational Economic Reasoning": "Basic Economic Principles & Methodology",
    "Economic Graphing & Elasticity Foundations": "Microeconomics & Price Mechanism",
    
    # Government
    "Elements of Government & Political Theory": "Elements of Government & Political Theory",
    "Colonial Administration in Nigeria & West Africa": "Colonial Administration in Nigeria & West Africa",
    "Nigerian Constitutional Development": "Nigerian Constitutional Development",
    "Federalism, Military Rule & Foreign Policy": "Federalism, Military Rule & Foreign Policy",
    "Political Concepts & The State Foundations": "Elements of Government & Political Theory",
    "Pre-Colonial Heritage Foundations": "Colonial Administration in Nigeria & West Africa",
    
    # Literature in English
    "Literary Appreciation & Devices": "Literary Appreciation & Devices",
    "Drama & Theatrical Techniques": "Drama & Theatrical Techniques",
    "Poetry & Versification": "Poetry & Versification",
    "Prose & Fictional Techniques": "Prose & Fictional Techniques",
    "Literary Genres & Fundamentals": "Literary Appreciation & Devices",
    "Figurative Devices & Tropes Foundations": "Literary Appreciation & Devices",
}

target_path = os.path.join(os.path.dirname(__file__), "..", "data", "lessons.json")
with open(target_path, "r", encoding="utf-8") as f:
    lessons = json.load(f)

for subj, topic_list in lessons.items():
    for les in topic_list:
        les["subject"] = subj
        top_name = les["topic"]
        mapped_cbt = TOPIC_DRILL_MAP.get(top_name, top_name)
        les["cbt_drill_topic"] = mapped_cbt

with open(target_path, "w", encoding="utf-8") as f:
    json.dump(lessons, f, indent=2, ensure_ascii=False)

print(f"Successfully harmonized lessons with explicit subject and cbt_drill_topic!")
