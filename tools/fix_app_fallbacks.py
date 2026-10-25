with open("app.py", "r", encoding="utf-8") as f:
    content = f.read()

content = content.replace("\r\n", "\n")

top_block = """# ----------------- QUESTIONS & SYLLABUS API -----------------
TOPIC_DRILL_FALLBACKS = {
    # Use of English
    "Parts of Speech Foundations": "Lexis & Structure",
    "Clause & Sentence Foundations": "Concord & Grammar",
    # Mathematics
    "Arithmetic & Algebraic Foundations": "Algebra",
    "Coordinate & Function Foundations": "Algebra",
    # Physics
    "Units, Dimensions & Vectors": "Mechanics",
    "Kinetic Theory & Heat Fundamentals": "Thermal Physics & Waves",
    # Chemistry
    "Atomic & Bonding Foundations": "Physical & General Chemistry",
    "Chemical Equations & Stoichiometric Foundations": "Physical & General Chemistry",
    # Biology
    "Biological Molecules & Cell Foundations": "Cellular Biology & Life Processes",
    "Chromosomes & Cell Division Foundations": "Genetics & Evolution",
    # Economics
    "Foundational Economic Reasoning": "Basic Economic Principles & Methodology",
    "Economic Graphing & Elasticity Foundations": "Microeconomics & Price Mechanism",
    # Government
    "Political Concepts & The State Foundations": "Elements of Government & Political Theory",
    "Pre-Colonial Heritage Foundations": "Colonial Administration in Nigeria & West Africa",
    # Literature in English
    "Literary Genres & Fundamentals": "Literary Appreciation & Devices",
    "Figurative Devices & Tropes Foundations": "Literary Appreciation & Devices",
}
"""

content = content.replace("# ----------------- QUESTIONS & SYLLABUS API -----------------\n", top_block)

# Clean up duplicate inside get_questions
duplicate_block = """        TOPIC_DRILL_FALLBACKS = {
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
        if len(matched_questions) < 5 and topic in TOPIC_DRILL_FALLBACKS:"""

cleaned_block = """        if len(matched_questions) < 5 and topic in TOPIC_DRILL_FALLBACKS:"""

if duplicate_block in content:
    content = content.replace(duplicate_block, cleaned_block, 1)

with open("app.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Successfully organized TOPIC_DRILL_FALLBACKS in app.py!")
