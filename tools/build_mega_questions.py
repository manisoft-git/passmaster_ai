import json
import os

QUESTIONS_PATH = "data/questions.json"

# Load existing 80 questions
with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    existing_list = json.load(f)

existing_dict = {q["id"]: q for q in existing_list}

# Harmonize existing questions
topic_corrections = {
    "phy_003": ("Thermal Physics & Waves", "Gas Laws"),
    "phy_004": ("Thermal Physics & Waves", "Wave Characteristics"),
    "phy_005": ("Electricity & Magnetism", "Circuit Analysis"),
    "phy_006": ("Mechanics", "Friction"),
    "phy_007": ("Thermal Physics & Waves", "Resonance"),
    "phy_008": ("Thermal Physics & Waves", "Optics"),
    "phy_009": ("Electricity & Magnetism", "Internal Resistance"),
    "phy_010": ("Modern & Atomic Physics", "Radioactivity"),
    "mth_004": ("Statistics & Probability", "Probability"),
    "mth_005": ("Statistics & Probability", "Permutations"),
    "mth_006": ("Algebra", "Logarithms"),
    "mth_007": ("Calculus", "Integration"),
    "mth_008": ("Geometry & Trigonometry", "Trigonometry"),
    "mth_009": ("Statistics & Probability", "Combinations"),
    "mth_010": ("Algebra", "Progressions"),
    "mth_011": ("Calculus", "Differentiation"),
    "chm_001": ("Physical & General Chemistry", "Gas Laws"),
    "chm_002": ("Inorganic Chemistry", "Periodic Table"),
    "chm_003": ("Organic Chemistry", "Hydrocarbons"),
    "chm_004": ("Physical & General Chemistry", "Equilibrium"),
    "chm_005": ("Inorganic Chemistry", "Extraction of Metals"),
    "chm_006": ("Organic Chemistry", "Isomerism"),
    "chm_007": ("Environmental & Industrial Chemistry", "Electrolysis"),
    "chm_008": ("Environmental & Industrial Chemistry", "Water Hardness"),
    "chm_009": ("Physical & General Chemistry", "Stoichiometry"),
    "bio_001": ("Cellular Biology & Life Processes", "Cell Organelles"),
    "bio_002": ("Human Physiology & Systems", "Circulation"),
    "bio_003": ("Genetics & Evolution", "Mendelian Genetics"),
    "bio_004": ("Ecology & Environment", "Food Chains"),
    "bio_005": ("Cellular Biology & Life Processes", "Osmosis"),
    "bio_006": ("Human Physiology & Systems", "Excretion"),
    "bio_007": ("Genetics & Evolution", "Sex Linkage"),
    "bio_008": ("Ecology & Environment", "Nitrogen Cycle"),
    "bio_009": ("Human Physiology & Systems", "Digestion"),
    "eco_001": ("Basic Economic Principles & Methodology", "Scarcity & Choice"),
    "eco_002": ("Microeconomics & Price Mechanism", "Elasticity"),
    "eco_003": ("Macroeconomics & National Income", "National Income"),
    "eco_004": ("Money, Banking & Public Finance", "Central Banking"),
    "eco_005": ("Microeconomics & Price Mechanism", "Price Controls"),
    "eco_006": ("Microeconomics & Price Mechanism", "Market Structures"),
    "eco_007": ("Macroeconomics & National Income", "The Multiplier"),
    "eco_008": ("Money, Banking & Public Finance", "Credit Creation"),
    "eco_009": ("Basic Economic Principles & Methodology", "PPC"),
    "eco_010": ("Money, Banking & Public Finance", "Taxation"),
    "gov_001": ("Elements of Government & Political Theory", "Sovereignty"),
    "gov_002": ("Colonial Administration in Nigeria & West Africa", "Indirect Rule"),
    "gov_003": ("Nigerian Constitutional Development", "Clifford Constitution"),
    "gov_004": ("Federalism, Military Rule & Foreign Policy", "Revenue Allocation"),
    "gov_005": ("Elements of Government & Political Theory", "Rule of Law"),
    "gov_006": ("Colonial Administration in Nigeria & West Africa", "Assimilation"),
    "gov_007": ("Nigerian Constitutional Development", "Lyttelton Constitution"),
    "gov_008": ("Federalism, Military Rule & Foreign Policy", "Military Rule"),
    "gov_009": ("Federalism, Military Rule & Foreign Policy", "Foreign Policy"),
    "lit_001": ("Literary Appreciation & Devices", "Figures of Speech"),
    "lit_002": ("Drama & Theatrical Techniques", "Dramatic Devices"),
    "lit_003": ("Poetry & Versification", "Sonnet Forms"),
    "lit_004": ("Prose & Fictional Techniques", "Narrative Technique"),
    "lit_005": ("Drama & Theatrical Techniques", "Soyinka Analysis"),
    "lit_006": ("Prose & Fictional Techniques", "Achebe Analysis"),
    "lit_007": ("Poetry & Versification", "Sound Devices")
}

for q_id, (top, subtop) in topic_corrections.items():
    if q_id in existing_dict:
        existing_dict[q_id]["topic"] = top
        existing_dict[q_id]["subtopic"] = subtop

print(f"Harmonized {len(topic_corrections)} existing questions.")
