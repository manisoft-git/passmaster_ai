import json
import os

SYLLABUS_PATH = "data/syllabus.json"
QUESTIONS_PATH = "data/questions.json"

# Load existing syllabus
with open(SYLLABUS_PATH, "r", encoding="utf-8") as f:
    syllabus = json.load(f)

# Add Economics
syllabus["Economics"] = {
    "weight_in_jamb": 40,
    "topics": [
        {
            "name": "Price Theory & Elasticity",
            "weight_pct": 25,
            "subtopics": [
                "Price Elasticity of Demand",
                "Cross & Income Elasticity",
                "Price Ceiling & Floors",
                "Market Equilibrium"
            ]
        },
        {
            "name": "National Income & Macroeconomics",
            "weight_pct": 25,
            "subtopics": [
                "GDP, GNP & Net National Income",
                "The Multiplier Concept",
                "Inflation Causes & Control",
                "Fiscal Policy Instruments"
            ]
        },
        {
            "name": "Money, Banking & Monetary Policy",
            "weight_pct": 25,
            "subtopics": [
                "Central Bank Monetary Tools",
                "Commercial Bank Credit Multiplier",
                "Inflation vs Deflation",
                "Foreign Exchange & Devaluation"
            ]
        },
        {
            "name": "Production & Market Structures",
            "weight_pct": 25,
            "subtopics": [
                "Law of Diminishing Returns",
                "Cost Concepts (MC, AC, TC)",
                "Monopoly vs Perfect Competition",
                "Economies of Scale"
            ]
        }
    ]
}

# Add Government
syllabus["Government"] = {
    "weight_in_jamb": 40,
    "topics": [
        {
            "name": "Basic Concepts in Political Science",
            "weight_pct": 25,
            "subtopics": [
                "Sovereignty & Rule of Law",
                "Separation of Powers",
                "Political Ideologies (Socialism, Capitalism)",
                "Citizenship, Rights & Duties"
            ]
        },
        {
            "name": "Constitutional Development in Nigeria",
            "weight_pct": 30,
            "subtopics": [
                "1999 Constitution Provisions",
                "Richards, Macpherson & Lyttelton Constitutions",
                "Federalism in Nigeria",
                "Indirect Rule in Northern vs Southern Nigeria"
            ]
        },
        {
            "name": "Organs of Government & Electoral Process",
            "weight_pct": 25,
            "subtopics": [
                "Legislative Process & Presidential Veto",
                "Judicial Independence & Judicial Review",
                "Electoral Systems (PR vs Simple Majority)",
                "Civil Service Principles & Bureaucracy"
            ]
        },
        {
            "name": "International Relations & Organizations",
            "weight_pct": 20,
            "subtopics": [
                "Nigeria Foreign Policy (Afrocentricism)",
                "ECOWAS & African Union",
                "United Nations Structure & Security Council",
                "Commonwealth of Nations"
            ]
        }
    ]
}

# Add Literature in English
syllabus["Literature in English"] = {
    "weight_in_jamb": 40,
    "topics": [
        {
            "name": "Literary Appreciation & Devices",
            "weight_pct": 30,
            "subtopics": [
                "Dramatic Irony & Catharsis",
                "Figures of Speech (Metaphor, Paradox, Oxymoron)",
                "Metre, Rhyme & Stanzaic Forms",
                "Tone, Mood & Atmosphere"
            ]
        },
        {
            "name": "African Prose & Drama",
            "weight_pct": 25,
            "subtopics": [
                "Themes of Cultural Conflict & Colonial Heritage",
                "Characterization & Tragic Flaw",
                "Folkloric & Oral Tradition Elements",
                "Feminism & Gender Dynamics"
            ]
        },
        {
            "name": "Non-African Prose & Drama",
            "weight_pct": 25,
            "subtopics": [
                "Shakespearean Dramatic Conventions",
                "Soliloquy vs Monologue vs Aside",
                "Satire & Allegory",
                "Gothic & Romantic Movements"
            ]
        },
        {
            "name": "Poetry Analysis",
            "weight_pct": 20,
            "subtopics": [
                "Sonnets (Shakespearean vs Italian)",
                "Odes & Elegies",
                "Diction, Enjambment & Imagery",
                "Tone & Point of View"
            ]
        }
    ]
}

with open(SYLLABUS_PATH, "w", encoding="utf-8") as f:
    json.dump(syllabus, f, indent=2)
print("Updated syllabus with Economics, Government, and Literature!")

# Load existing questions
with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

existing_ids = {q["id"] for q in questions}

new_questions = [
    # --- ECONOMICS ---
    {
        "id": "eco_001",
        "subject": "Economics",
        "topic": "Price Theory & Elasticity",
        "subtopic": "Price Elasticity of Demand",
        "year": 2023,
        "question": "If the price of a bag of rice rises by 20% and the quantity demanded falls by 10%, the price elasticity of demand is _______ and demand is _______.",
        "options": {
            "A": "2.0; elastic",
            "B": "0.5; inelastic",
            "C": "0.5; elastic",
            "D": "-2.0; unitary"
        },
        "correct_option": "B",
        "traps": {
            "A": "You inverted the formula by dividing percentage change in price by percentage change in quantity demanded (20% / 10% = 2.0). Elasticity is %ΔQd / %ΔP!",
            "C": "You correctly computed 0.5, but mistakenly classified values less than 1 (< 1) as elastic rather than inelastic.",
            "D": "You inverted the formula and confused negative signs with unitary elasticity."
        },
        "pedagogical_concept": "Price Elasticity of Demand (PED) = (% Change in Quantity Demanded) / (% Change in Price). Here, PED = 10% / 20% = 0.5. Because PED < 1, the demand is price inelastic (consumers are relatively unresponsive to price changes).",
        "socratic_prompt": "Recall the PED formula: does Quantity go on top (numerator) or Price? When the absolute result is less than 1, does that make demand elastic or inelastic?"
    },
    {
        "id": "eco_002",
        "subject": "Economics",
        "topic": "Money, Banking & Monetary Policy",
        "subtopic": "Central Bank Monetary Tools",
        "year": 2024,
        "question": "To curb runaway demand-pull inflation in the Nigerian economy, the Central Bank of Nigeria (CBN) would most appropriately _______.",
        "options": {
            "A": "reduce the Monetary Policy Rate (MPR)",
            "B": "purchase treasury bills in Open Market Operations (OMO)",
            "C": "increase the Cash Reserve Ratio (CRR)",
            "D": "lower the liquidity ratio of commercial banks"
        },
        "correct_option": "C",
        "traps": {
            "A": "Lowering the MPR encourages borrowing and expands money supply, worsening inflation.",
            "B": "Purchasing treasury bills injects cash into the commercial banking system, which increases liquidity and inflames inflation.",
            "D": "Lowering the liquidity ratio frees up bank deposits for lending, which expands money supply."
        },
        "pedagogical_concept": "Contractionary Monetary Policy: To fight inflation, the central bank must reduce money supply in circulation. Raising the Cash Reserve Ratio (CRR) forces commercial banks to lock away more reserves with the CBN, decreasing loan creation.",
        "socratic_prompt": "To combat high inflation, should the Central Bank make money easier to borrow or tighten credit in the banking system? What happens to bank lending capacity when the CRR is raised?"
    },
    {
        "id": "eco_003",
        "subject": "Economics",
        "topic": "National Income & Macroeconomics",
        "subtopic": "The Multiplier Concept",
        "year": 2022,
        "question": "In a closed economy, if the Marginal Propensity to Consume (MPC) is 0.75, what is the value of the investment multiplier?",
        "options": {
            "A": "1.33",
            "B": "3.0",
            "C": "4.0",
            "D": "0.25"
        },
        "correct_option": "C",
        "traps": {
            "A": "You calculated 1 / MPC = 1 / 0.75 = 1.33. The multiplier formula uses MPS in the denominator (1 - MPC), not MPC directly!",
            "B": "You multiplied 0.75 by 4 or miscalculated the reciprocal of 0.25.",
            "D": "You calculated the Marginal Propensity to Save (MPS = 1 - 0.75 = 0.25) but forgot to take its reciprocal."
        },
        "pedagogical_concept": "Investment Multiplier (K) = 1 / (1 - MPC) = 1 / MPS. Since MPC = 0.75, MPS = 1 - 0.75 = 0.25. Therefore, K = 1 / 0.25 = 4.0.",
        "socratic_prompt": "What is the formula for the investment multiplier in terms of MPC? If households consume 75 kobo of every additional naira (0.75), how much do they save (MPS)?"
    },

    # --- GOVERNMENT ---
    {
        "id": "gov_001",
        "subject": "Government",
        "topic": "Constitutional Development in Nigeria",
        "subtopic": "Indirect Rule in Northern vs Southern Nigeria",
        "year": 2023,
        "question": "The British colonial policy of Indirect Rule was most successful in Northern Nigeria primarily because _______.",
        "options": {
            "A": "the North possessed an existing centralized traditional emirate hierarchy with established taxation systems",
            "B": "the Christian missionaries had established formal schools before colonial administrative arrival",
            "C": "the British deployed a massive standing military force across every northern hamlet",
            "D": "the educated northern elite enthusiastically drafted the local administrative decrees"
        },
        "correct_option": "A",
        "traps": {
            "B": "Christian missionaries were actively barred from the Islamic northern emirates by Lord Lugard's non-interference pact.",
            "C": "The core purpose of Indirect Rule was low-budget governance due to severe shortages of British manpower and funds.",
            "D": "Western-educated elite were virtually absent in Northern Nigeria at the time; governance relied on hereditary Emirs and Waziris."
        },
        "pedagogical_concept": "Indirect Rule Success Factors: Lord Lugard successfully applied Indirect Rule in Northern Nigeria because the Sokoto Caliphate structure provided autocratic, centralized rulers (Emirs) already accustomed to direct taxation and Sharia administration.",
        "socratic_prompt": "Why did Indirect Rule fail in Eastern Nigeria (Igboland) while succeeding in the North? What existing administrative and taxation structure did the Emirs already maintain?"
    },
    {
        "id": "gov_002",
        "subject": "Government",
        "topic": "Basic Concepts in Political Science",
        "subtopic": "Sovereignty & Rule of Law",
        "year": 2024,
        "question": "According to A.V. Dicey, the doctrine of the Rule of Law encompasses which of the following cardinal tenets?",
        "options": {
            "A": "Supremacy of the constitution, military jurisdiction, and diplomatic immunity",
            "B": "Supremacy of regular law, equality before the law, and predominance of legal spirit",
            "C": "Absolute discretion of the sovereign, trial by jury, and parliamentary supremacy",
            "D": "Presumption of guilt, right to appeal, and judicial precedent"
        },
        "correct_option": "B",
        "traps": {
            "A": "Military tribunals and diplomatic immunities represent exceptions/limitations to the rule of law, not Dicey's cardinal tenets.",
            "C": "Dicey explicitly argued against arbitrary power and absolute discretion of rulers.",
            "D": "The law presumes innocence until proven guilty, not guilt."
        },
        "pedagogical_concept": "A.V. Dicey's Three Pillars of Rule of Law (1885): 1. Absolute supremacy of regular law over arbitrary power. 2. Equality before the law (no person is above the law). 3. The primacy of individual liberties guaranteed through ordinary courts.",
        "socratic_prompt": "Think of Professor A.V. Dicey's three fundamental principles. Can any individual or leader have arbitrary discretion under the Rule of Law?"
    },
    {
        "id": "gov_003",
        "subject": "Government",
        "topic": "Organs of Government & Electoral Process",
        "subtopic": "Legislative Process & Presidential Veto",
        "year": 2022,
        "question": "Under the 1999 Constitution of the Federal Republic of Nigeria, if the President withholds assent to a bill passed by the National Assembly, the bill can still become law if _______.",
        "options": {
            "A": "the Chief Justice of Nigeria issues a constitutional writ of mandamus",
            "B": "a simple majority in both the Senate and House of Representatives repasses it",
            "C": "a two-thirds majority in each house of the National Assembly passes it again",
            "D": "the Council of State ratifies the bill during an extraordinary session"
        },
        "correct_option": "C",
        "traps": {
            "A": "The judiciary interprets laws; it cannot override a legislative veto or assent bills into law.",
            "B": "A simple majority (50% + 1) is only needed for initial passage; overriding a presidential veto requires a supermajority.",
            "D": "The Council of State is purely advisory and has no legislative enactment powers."
        },
        "pedagogical_concept": "Veto Override under Section 58(5) of the 1999 Constitution: Where the President withholds assent within 30 days, the bill can become law without assent if passed again by two-thirds majority of each House (Senate and House of Representatives).",
        "socratic_prompt": "What special parliamentary majority is required to overcome a presidential veto in Nigeria's presidential democracy?"
    },

    # --- LITERATURE IN ENGLISH ---
    {
        "id": "lit_001",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Figures of Speech (Metaphor, Paradox, Oxymoron)",
        "year": 2023,
        "question": "\"Parting is such sweet sorrow that I shall say good night till it be morrow.\" The phrase 'sweet sorrow' exemplifies which literary device?",
        "options": {
            "A": "Hyperbole",
            "B": "Oxymoron",
            "C": "Synecdoche",
            "D": "Euphemism"
        },
        "correct_option": "B",
        "traps": {
            "A": "Hyperbole is deliberate exaggeration for dramatic effect (e.g. 'I've cried an ocean of tears').",
            "C": "Synecdoche is using a part to represent the whole (e.g. 'All hands on deck').",
            "D": "Euphemism is a mild expression substituted for a harsh one (e.g. 'passed away' for died)."
        },
        "pedagogical_concept": "Oxymoron: A concise figure of speech where two contradictory or opposing terms appear side-by-side in juxtaposition ('sweet' and 'sorrow', 'deafening silence', 'living death').",
        "socratic_prompt": "Notice how the words 'sweet' (pleasant) and 'sorrow' (grief/pain) are placed right beside each other. What is a two-word contradiction in terms called?"
    },
    {
        "id": "lit_002",
        "subject": "Literature in English",
        "topic": "Non-African Prose & Drama",
        "subtopic": "Soliloquy vs Monologue vs Aside",
        "year": 2024,
        "question": "When an actor on stage speaks their innermost private thoughts aloud while alone, allowing the audience direct access to their psyche, the dramatic device is a _______.",
        "options": {
            "A": "Monologue",
            "B": "Soliloquy",
            "C": "Aside",
            "D": "Dialogue"
        },
        "correct_option": "B",
        "traps": {
            "A": "A monologue is a long uninterrupted speech delivered by one character TO other characters on stage.",
            "C": "An aside is a brief remark directed to the audience or another character that characters on stage pretend not to hear.",
            "D": "A dialogue requires a conversation between two or more characters."
        },
        "pedagogical_concept": "Soliloquy vs Monologue: In a soliloquy (from Latin 'solus' = alone, 'loqui' = speak), the character is ALONE on stage, speaking their inner thoughts to the audience. In a monologue, other characters are present and listening.",
        "socratic_prompt": "Is the character speaking to other characters who are listening, or are they completely alone on stage revealing their private mind to the audience?"
    },

    # --- MATHEMATICS ---
    {
        "id": "mth_002",
        "subject": "Mathematics",
        "topic": "Calculus",
        "subtopic": "Differentiation (Chain Rule)",
        "year": 2023,
        "question": "If y = (3x² - 5)⁴, find the first derivative dy/dx with respect to x.",
        "options": {
            "A": "4(3x² - 5)³",
            "B": "24x(3x² - 5)³",
            "C": "12x(3x² - 5)³",
            "D": "24(3x² - 5)³"
        },
        "correct_option": "B",
        "traps": {
            "A": "You differentiated only the outer power function but forgot to multiply by the derivative of the inner function (d/dx [3x² - 5] = 6x).",
            "C": "You differentiated 3x² to get 3x or made an arithmetic error multiplying 4 by 3x instead of 6x.",
            "D": "You forgot the variable x when differentiating 3x²."
        },
        "pedagogical_concept": "The Chain Rule: dy/dx = (dy/du) * (du/dx). Let u = 3x² - 5, so y = u⁴. dy/du = 4u³ and du/dx = 6x. Thus, dy/dx = 4(3x² - 5)³ * 6x = 24x(3x² - 5)³.",
        "socratic_prompt": "When differentiating a function inside another function, what must you multiply the outer derivative by? What is the derivative of (3x² - 5)?"
    },
    {
        "id": "mth_003",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Matrices & Determinants",
        "year": 2024,
        "question": "Find the determinant of the 2x2 matrix M = [[4, -2], [3, 5]].",
        "options": {
            "A": "14",
            "B": "26",
            "C": "-26",
            "D": "20"
        },
        "correct_option": "B",
        "traps": {
            "A": "You added the terms instead of subtracting: ad + bc = (4*5) + (-6) = 14.",
            "C": "You reversed the subtraction formula: bc - ad = -6 - 20 = -26.",
            "D": "You only multiplied the main diagonal (4 * 5 = 20) and discarded the off-diagonal."
        },
        "pedagogical_concept": "Determinant of [[a, b], [c, d]] = ad - bc. Here: (4 * 5) - (-2 * 3) = 20 - (-6) = 20 + 6 = 26.",
        "socratic_prompt": "What is the formula for the determinant of a 2x2 matrix? Be very careful with the double negative when subtracting (-2 * 3)!"
    },

    # --- PHYSICS ---
    {
        "id": "phy_003",
        "subject": "Physics",
        "topic": "Waves & Optics",
        "subtopic": "Refraction & Critical Angle",
        "year": 2023,
        "question": "A light ray travels from glass (refractive index n = 1.50) into air (n = 1.00). What is the critical angle for total internal reflection to occur?",
        "options": {
            "A": "48.6°",
            "B": "41.8°",
            "C": "30.0°",
            "D": "60.0°"
        },
        "correct_option": "B",
        "traps": {
            "A": "48.6° is the critical angle for water (n = 1.33) into air, not glass (n = 1.50).",
            "C": "sin(30°) = 0.5, which corresponds to n = 2.0, not 1.50.",
            "D": "You calculated arcsin(1.50 - 1.0) or approximated without using sin(c) = 1/n."
        },
        "pedagogical_concept": "Critical Angle: sin(c) = 1 / n. For glass with n = 1.50, sin(c) = 1 / 1.50 = 0.6667. c = arcsin(0.6667) = 41.8°.",
        "socratic_prompt": "What is the relationship between refractive index n and critical angle c? What angle has a sine of 1 / 1.5 (0.667)?"
    },

    # --- CHEMISTRY ---
    {
        "id": "chm_002",
        "subject": "Chemistry",
        "topic": "Physical Chemistry",
        "subtopic": "Chemical Equilibrium & Le Chateliers Principle",
        "year": 2024,
        "question": "For the exothermic Haber process reaction: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol), which condition will shift the equilibrium position to produce MORE ammonia (NH₃)?",
        "options": {
            "A": "Increasing the reaction temperature",
            "B": "Decreasing the total pressure",
            "C": "Increasing the total pressure",
            "D": "Adding an iron catalyst"
        },
        "correct_option": "C",
        "traps": {
            "A": "Because the forward reaction is exothermic, increasing temperature shifts the equilibrium to the left (endothermic direction), reducing NH₃ yield.",
            "B": "Decreasing pressure favors the side with more moles of gas (left has 4 moles vs right has 2 moles).",
            "D": "A catalyst increases the rate of forward and reverse reactions equally; it has ZERO effect on equilibrium position or yield."
        },
        "pedagogical_concept": "Le Chatelier's Principle: 1. Higher pressure shifts equilibrium toward fewer gas moles (4 moles on LHS → 2 moles on RHS). 2. Lower temperature favors exothermic reactions (forward). 3. Catalysts alter rate only, not yield.",
        "socratic_prompt": "Count the number of moles of gas on the left side vs the right side. According to Le Chatelier, which side does higher pressure favor?"
    },

    # --- BIOLOGY ---
    {
        "id": "bio_002",
        "subject": "Biology",
        "topic": "Genetics & Heredity",
        "subtopic": "Sex-Linked Inheritance",
        "year": 2023,
        "question": "A carrier female for hemophilia (XᴴXʰ) marries a normal male (XᴴY). What is the probability that their sons will have hemophilia?",
        "options": {
            "A": "0% (0.0)",
            "B": "25% (0.25)",
            "C": "50% (0.50)",
            "D": "100% (1.0)"
        },
        "correct_option": "C",
        "traps": {
            "A": "You assumed hemophilia cannot be expressed in children if the father is normal.",
            "B": "25% is the probability across ALL children (sons and daughters combined). The question specifically asks about SONS.",
            "D": "You assumed all sons inherit the recessive allele, but the mother has one normal Xᴴ and one mutant Xʰ."
        },
        "pedagogical_concept": "Sex-Linked Inheritance in Sons: The father contributes the Y chromosome to all male offspring. The mother gives either Xᴴ (normal son) or Xʰ (hemophiliac son) with equal probability (50% or 1 in 2).",
        "socratic_prompt": "Carefully read the denominator in the question: it asks 'among their sons', not 'among all children'. What alleles can a son receive from this mother?"
    }
]

added_count = 0
for q in new_questions:
    if q["id"] not in existing_ids:
        questions.append(q)
        existing_ids.add(q["id"])
        added_count += 1

with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully added {added_count} new questions! Total questions in bank: {len(questions)}")
