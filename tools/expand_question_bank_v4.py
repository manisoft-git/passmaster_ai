import json

QUESTIONS_PATH = "data/questions.json"

with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

existing_ids = {q["id"] for q in questions}

v4_batch = [
    # ---------------- USE OF ENGLISH ----------------
    {
        "id": "eng_011",
        "subject": "Use of English",
        "topic": "Concord & Grammar",
        "subtopic": "Subjunctive Mood",
        "year": 2024,
        "question": "The university disciplinary committee recommended that the suspended student _______ before the panel immediately.",
        "options": {
            "A": "appears",
            "B": "appear",
            "C": "should have appeared",
            "D": "appeared"
        },
        "correct_option": "B",
        "traps": {
            "A": "You added 's' because the student is singular (he/she). But verbs of recommendation take the subjunctive mood with base infinitive form!",
            "C": "'Should have appeared' creates an unnecessary conditional auxiliary.",
            "D": "'Appeared' uses past indicative, missing the mandative subjunctive requirement."
        },
        "pedagogical_concept": "Mandative Subjunctive: After verbs of demanding, recommending, insisting, or decreeing (recommend that, insist that, decree that), the dependent verb MUST take the base infinitive form (e.g., 'he appear', 'she go', 'it be').",
        "socratic_prompt": "What happens to the verb after formal expressions like 'recommended that he...' or 'insisted that she...'? Does it take an 's'?"
    },
    {
        "id": "eng_012",
        "subject": "Use of English",
        "topic": "Lexis & Structure",
        "subtopic": "Collocations",
        "year": 2023,
        "question": "The board of directors finally agreed to confer the honorary doctorate _______ the visiting diplomat.",
        "options": {
            "A": "to",
            "B": "on",
            "C": "with",
            "D": "at"
        },
        "correct_option": "B",
        "traps": {
            "A": "Transferring an honor takes 'on', not 'to'. 'Confer to' is unidiomatic English.",
            "C": "'Confer with' means to consult or discuss with someone, not to bestow an award.",
            "D": "'Confer at' is grammatically non-existent."
        },
        "pedagogical_concept": "Prepositional Collocation: The verb confer takes 'on' or 'upon' when meaning to bestow an honor, degree, or title upon someone. (Contrast with 'confer with' which means to consult).",
        "socratic_prompt": "When a university gives a degree to someone, do they confer it 'to' or bestow it 'on' them?"
    },
    {
        "id": "eng_013",
        "subject": "Use of English",
        "topic": "Oral Forms & Phonology",
        "subtopic": "Silent Consonants",
        "year": 2024,
        "question": "In which of the following words is the letter 'p' silent in standard pronunciation?",
        "options": {
            "A": "Pencil",
            "B": "Receipt",
            "C": "Puppy",
            "D": "Impact"
        },
        "correct_option": "B",
        "traps": {
            "A": "'Pencil' has an initial voiced plosive /p/.",
            "C": "'Puppy' pronounces both /p/ plosives.",
            "D": "'Impact' clearly articulates /p/ in the middle coda."
        },
        "pedagogical_concept": "Silent Letters: In standard British and West African English, the letter 'p' in 'receipt' (/rɪˈsiːt/) is completely silent. It is also silent in psalm, pneumonia, pseudo, and psyche.",
        "socratic_prompt": "How do you pronounce the document you receive when you pay for goods in a store? Is it re-ceept or re-see-pt?"
    },
    {
        "id": "eng_014",
        "subject": "Use of English",
        "topic": "Comprehension & Prescribed Text",
        "subtopic": "The Life Changer Themes",
        "year": 2024,
        "question": "In the prescribed JAMB novel 'The Life Changer', what vital life lesson does Ummi emphasize to her children before their university departure?",
        "options": {
            "A": "Pursuing academic success at the cost of personal values",
            "B": "Exercising caution in relationships and avoiding premature independence and peer deception",
            "C": "Accumulating material wealth through campus entrepreneurship",
            "D": "Relying entirely on lecturers for personal moral direction"
        },
        "correct_option": "B",
        "traps": {
            "A": "The novel warns strongly against compromising integrity for grades or peer approval.",
            "C": "Material ambition is shown leading characters like Talle and Habib into complications.",
            "D": "The novel stresses personal agency and parental foundations rather than lecturer dependence."
        },
        "pedagogical_concept": "The Life Changer Themes: Khadija Abubakar Jalli's novel centers on freedom, peer pressure, campus morality, and the crucial balance between independence and parental ethical guidance.",
        "socratic_prompt": "What recurring warning does Ummi give concerning campus social circles and sudden freedom?"
    },
    {
        "id": "eng_015",
        "subject": "Use of English",
        "topic": "Concord & Grammar",
        "subtopic": "Tenses & Conditionals",
        "year": 2023,
        "question": "If the candidate had registered before the deadline, she _______ disqualified by the board.",
        "options": {
            "A": "would not be",
            "B": "would not have been",
            "C": "will not be",
            "D": "shall not have been"
        },
        "correct_option": "B",
        "traps": {
            "A": "'Would not be' represents a Second Conditional (hypothetical present), but 'had registered' is past perfect (Third Conditional).",
            "C": "'Will not be' mixes First Conditional with Third Conditional past.",
            "D": "'Shall not have been' is archaic and tense-inconsistent."
        },
        "pedagogical_concept": "Third Conditional (Unfulfilled Past): Structure is: If + past perfect (had + V3) ... would/could/might + have + V3. It describes hypothetical past actions and their impossible past outcomes.",
        "socratic_prompt": "Notice the 'If + had registered' structure. What modal construction must follow in the main clause for unfulfilled past?"
    },

    # ---------------- MATHEMATICS ----------------
    {
        "id": "mth_009",
        "subject": "Mathematics",
        "topic": "Calculus",
        "subtopic": "Integration by Substitution",
        "year": 2024,
        "question": "Evaluate the indefinite integral: ∫ 2x(x² + 1)³ dx.",
        "options": {
            "A": "(x² + 1)⁴ / 4 + C",
            "B": "(x² + 1)⁴ / 2 + C",
            "C": "2(x² + 1)⁴ + C",
            "D": "x²(x² + 1)⁴ / 4 + C"
        },
        "correct_option": "A",
        "traps": {
            "B": "You forgot to divide by the new power 4 properly: ∫ u³ du = u⁴ / 4.",
            "C": "You multiplied by 2 instead of integrating u³.",
            "D": "You left x² in front of the integral instead of recognizing du = 2x dx."
        },
        "pedagogical_concept": "Integration by Substitution: Let u = x² + 1. Then du/dx = 2x => du = 2x dx. The integral simplifies directly to ∫ u³ du = u⁴ / 4 + C = (x² + 1)⁴ / 4 + C.",
        "socratic_prompt": "Notice that 2x is the exact derivative of (x² + 1). If you substitute u = x² + 1, what does the integral become in terms of u?"
    },
    {
        "id": "mth_010",
        "subject": "Mathematics",
        "topic": "Geometry & Trigonometry",
        "subtopic": "Trigonometric Identities",
        "year": 2023,
        "question": "If sin θ = 3/5 and θ is an acute angle, evaluate (1 - cos² θ) / (1 + tan² θ).",
        "options": {
            "A": "9/25",
            "B": "144/625",
            "C": "16/25",
            "D": "81/625"
        },
        "correct_option": "B",
        "traps": {
            "A": "You simplified the numerator to sin²θ = 9/25, but ignored dividing by sec²θ = 1 + tan²θ!",
            "C": "16/25 is cos²θ.",
            "D": "81/625 is (sin²θ)²."
        },
        "pedagogical_concept": "Trigonometric Identities: 1 - cos²θ = sin²θ. Also 1 + tan²θ = sec²θ = 1/cos²θ. Therefore, the expression is sin²θ / sec²θ = sin²θ × cos²θ. For sin θ = 3/5, cos θ = 4/5. Thus (3/5)² × (4/5)² = (9/25) × (16/25) = 144 / 625.",
        "socratic_prompt": "What is 1 - cos²θ equal to? And what is 1 + tan²θ equal to in terms of secant? How do they multiply?"
    },
    {
        "id": "mth_011",
        "subject": "Mathematics",
        "topic": "Statistics & Probability",
        "subtopic": "Permutations & Combinations",
        "year": 2024,
        "question": "A bag contains 5 red balls and 4 blue balls. If two balls are drawn at random without replacement, what is the probability that both are red?",
        "options": {
            "A": "25/81",
            "B": "5/18",
            "C": "20/81",
            "D": "5/9"
        },
        "correct_option": "B",
        "traps": {
            "A": "25/81 assumes replacement: (5/9) × (5/9). But the balls are drawn WITHOUT replacement!",
            "C": "You calculated (5/9) × (4/9). The denominator also decreases by 1 on the second draw: 8, not 9!",
            "D": "5/9 is the probability of the first ball only."
        },
        "pedagogical_concept": "Conditional Probability without Replacement: P(First Red) = 5/9. After drawing 1 red ball, 4 red balls and 8 total balls remain. P(Second Red | First Red) = 4/8 = 1/2. Total P = (5/9) × (4/8) = 20 / 72 = 5 / 18.",
        "socratic_prompt": "If you don't put the first red ball back, how many red balls are left? And how many total balls remain in the bag?"
    },

    # ---------------- PHYSICS ----------------
    {
        "id": "phy_009",
        "subject": "Physics",
        "topic": "Thermal Physics & Waves",
        "subtopic": "Specific Latent Heat",
        "year": 2024,
        "question": "Calculate the quantity of heat required to convert 2 kg of ice at 0°C completely into water at 0°C. (Specific latent heat of fusion of ice = 3.36 × 10⁵ J/kg).",
        "options": {
            "A": "6.72 × 10⁵ J",
            "B": "1.68 × 10⁵ J",
            "C": "3.36 × 10⁵ J",
            "D": "0 J"
        },
        "correct_option": "A",
        "traps": {
            "B": "You divided by mass instead of multiplying: Q = mL, not L/m!",
            "C": "3.36 × 10⁵ J is the latent heat for only 1 kg.",
            "D": "Temperature does not change, but phase change requires latent heat!"
        },
        "pedagogical_concept": "Latent Heat of Phase Change: When a substance changes state at constant temperature, the heat absorbed or released is given by Q = mL. Q = 2 kg × 3.36 × 10⁵ J/kg = 6.72 × 10⁵ J.",
        "socratic_prompt": "What formula relates mass and latent heat during a state change without temperature difference?"
    },
    {
        "id": "phy_010",
        "subject": "Physics",
        "topic": "Electricity & Magnetism",
        "subtopic": "Capacitors in Series & Parallel",
        "year": 2023,
        "question": "Two capacitors of capacitance 6 μF and 3 μF are connected in series across a 12 V battery. Calculate the equivalent capacitance of the combination.",
        "options": {
            "A": "9 μF",
            "B": "2 μF",
            "C": "18 μF",
            "D": "4.5 μF"
        },
        "correct_option": "B",
        "traps": {
            "A": "9 μF adds them like resistors in series! For capacitors in series, capacitances add reciprocally: 1/C = 1/C₁ + 1/C₂.",
            "C": "18 μF is their product without dividing by their sum.",
            "D": "4.5 μF is the arithmetic mean."
        },
        "pedagogical_concept": "Series Capacitance: For series capacitors, 1/C_eq = 1/C₁ + 1/C₂ => C_eq = (C₁ × C₂) / (C₁ + C₂) = (6 × 3) / (6 + 3) = 18 / 9 = 2 μF. (Capacitors in series behave like resistors in parallel).",
        "socratic_prompt": "Remember that capacitors behave the exact opposite of resistors. How do two resistors in parallel combine?"
    },

    # ---------------- CHEMISTRY ----------------
    {
        "id": "chm_008",
        "subject": "Chemistry",
        "topic": "Organic Chemistry",
        "subtopic": "Esterification & Functional Groups",
        "year": 2024,
        "question": "The organic reaction between ethanoic acid (CH₃COOH) and ethanol (C₂H₅OH) in the presence of concentrated tetraoxosulphate(VI) acid produces _______.",
        "options": {
            "A": "Ethyl methanoate and water",
            "B": "Ethyl ethanoate and water",
            "C": "Methyl propanoate and hydrogen",
            "D": "Ethoxymethane and water"
        },
        "correct_option": "B",
        "traps": {
            "A": "Ethanoic acid provides the ethanoate group (2 carbons), not methanoate (1 carbon).",
            "C": "Esterification produces water as a byproduct, not hydrogen gas!",
            "D": "Ethoxymethane is an ether formed by dehydration of alcohols, not an ester from an acid + alcohol."
        },
        "pedagogical_concept": "Esterification: Carboxylic acid + Alkanol -> Ester + Water (catalyzed by conc. H₂SO₄ acting as a dehydrating agent). Ethanoic acid + Ethanol -> Ethyl ethanoate (CH₃COOC₂H₅) + H₂O.",
        "socratic_prompt": "What ester name results from an ETHYL group from the alcohol combining with an ETHANOATE group from the carboxylic acid?"
    },
    {
        "id": "chm_009",
        "subject": "Chemistry",
        "topic": "Physical & General Chemistry",
        "subtopic": "Le Chatelier's Principle",
        "year": 2023,
        "question": "For the exothermic reversible reaction: N₂(g) + 3H₂(g) ⇌ 2NH₃(g), ΔH = -92 kJ/mol. Which change will shift the equilibrium position to favor higher yield of ammonia (NH₃)?",
        "options": {
            "A": "Increasing the temperature",
            "B": "Increasing the total pressure",
            "C": "Decreasing the concentration of N₂",
            "D": "Adding a catalyst"
        },
        "correct_option": "B",
        "traps": {
            "A": "Because the forward reaction is EXOTHERMIC (ΔH < 0), increasing temperature shifts equilibrium to the left (endothermic side), decreasing NH₃ yield!",
            "C": "Removing reactant N₂ shifts equilibrium backwards to replace it.",
            "D": "A catalyst speeds up both forward and backward reactions equally; it NEVER alters equilibrium position or yield!"
        },
        "pedagogical_concept": "Le Chatelier's Principle: On the left, there are 1 + 3 = 4 moles of gas. On the right, there are 2 moles of gas. Increasing pressure shifts equilibrium towards the side with fewer gas molecules (the right), favoring NH₃ production.",
        "socratic_prompt": "Count the total gas molecules on the reactant side vs the product side. How does an increase in pressure affect the side with fewer moles?"
    },

    # ---------------- BIOLOGY ----------------
    {
        "id": "bio_008",
        "subject": "Biology",
        "topic": "Human Physiology & Systems",
        "subtopic": "Renal Excretion & Nephron",
        "year": 2024,
        "question": "In the mammalian kidney, ultrafiltration of blood occurs specifically in the _______.",
        "options": {
            "A": "Loop of Henle",
            "B": "Bowman's capsule and glomerulus",
            "C": "Distal convoluted tubule",
            "D": "Collecting duct"
        },
        "correct_option": "B",
        "traps": {
            "A": "The Loop of Henle is responsible for osmoregulation and water/salt reabsorption, not filtration.",
            "C": "Distal tubule handles selective tubular secretion and pH regulation.",
            "D": "Collecting duct collects concentrated urine for transport to the ureter."
        },
        "pedagogical_concept": "Nephron Ultrafiltration: High hydrostatic pressure in the glomerulus forces water, glucose, urea, and ions across the podocyte basement membrane into the Bowman's capsule, forming the glomerular filtrate.",
        "socratic_prompt": "Where does the knot of capillary vessels meet the cup-shaped structure under high hydrostatic pressure?"
    },
    {
        "id": "bio_009",
        "subject": "Biology",
        "topic": "Genetics & Evolution",
        "subtopic": "Sex-Linked Inheritance",
        "year": 2023,
        "question": "If a carrier woman for hemophilia (XᴴXʰ) marries a normal man (XᴴY), what percentage of their MALE offspring is expected to have hemophilia?",
        "options": {
            "A": "0%",
            "B": "25%",
            "C": "50%",
            "D": "100%"
        },
        "correct_option": "C",
        "traps": {
            "A": "Males only receive one X chromosome (from the mother); receiving Xʰ causes the disease.",
            "B": "25% is the probability of having a hemophiliac child among ALL offspring (male and female combined). The question specifically specifies MALE offspring!",
            "D": "Only half of the sons receive the defective Xʰ chromosome; the other half receive normal Xᴴ."
        },
        "pedagogical_concept": "Sex-Linked Genetics: Sons receive their Y chromosome from father and one X from mother. The mother produces two types of egg: 50% Xᴴ and 50% Xʰ. Therefore, 50% of male offspring (XʰY) will suffer from hemophilia.",
        "socratic_prompt": "Read carefully: The prompt asks for percentage of MALE offspring, not all offspring. Out of the sons, how many inherit the mother's affected X chromosome?"
    },

    # ---------------- ECONOMICS ----------------
    {
        "id": "eco_009",
        "subject": "Economics",
        "topic": "Microeconomics & Price Mechanism",
        "subtopic": "Price Elasticity of Demand",
        "year": 2024,
        "question": "When a 10% increase in the price of a commodity leads to a 25% decrease in the quantity demanded, the price elasticity of demand is classified as _______.",
        "options": {
            "A": "Inelastic (Ed < 1)",
            "B": "Elastic (Ed > 1)",
            "C": "Unitary elastic (Ed = 1)",
            "D": "Perfectively inelastic (Ed = 0)"
        },
        "correct_option": "B",
        "traps": {
            "A": "Ed = %ΔQ / %ΔP = 25% / 10% = 2.5. Since 2.5 > 1, demand is elastic, NOT inelastic!",
            "C": "Unitary elasticity requires %ΔQ = %ΔP (ratio = 1).",
            "D": "Perfect inelasticity occurs when quantity demanded does not change at all (%ΔQ = 0)."
        },
        "pedagogical_concept": "Price Elasticity of Demand: Ed = |% change in quantity demanded / % change in price| = 25 / 10 = 2.5. Since Ed > 1, consumers are highly responsive to price adjustments, characterizing elastic demand.",
        "socratic_prompt": "Calculate the elasticity ratio: 25 divided by 10. Is the result greater than 1 or less than 1?"
    },
    {
        "id": "eco_010",
        "subject": "Economics",
        "topic": "Macroeconomics & National Income",
        "subtopic": "Gross Domestic Product (GDP)",
        "year": 2023,
        "question": "The total monetary value of all final goods and services produced within the geographical boundaries of a country during a specified year, regardless of who produces them, is known as _______.",
        "options": {
            "A": "Gross National Product (GNP)",
            "B": "Gross Domestic Product (GDP)",
            "C": "Net National Product (NNP)",
            "D": "Personal Disposable Income"
        },
        "correct_option": "B",
        "traps": {
            "A": "GNP measures output produced by nationals (citizens) of a country, including abroad. DOMESTIC (GDP) measures output within territorial borders!",
            "C": "NNP equals GNP minus capital depreciation.",
            "D": "Personal Disposable Income is income left to individuals after direct taxes."
        },
        "pedagogical_concept": "National Income Accounting: Gross Domestic Product (GDP) is location-based (within territorial borders). Gross National Product (GNP) is nationality-based (GNP = GDP + Net Property Income from Abroad).",
        "socratic_prompt": "What does the word 'Domestic' signify? Does it refer to the physical territory of the nation?"
    },

    # ---------------- GOVERNMENT ----------------
    {
        "id": "gov_008",
        "subject": "Government",
        "topic": "Nigerian Constitutional Development",
        "subtopic": "1979 Executive Constitution",
        "year": 2024,
        "question": "The 1979 Constitution of Nigeria marked a fundamental departure from previous post-independence constitutions because it _______.",
        "options": {
            "A": "retained Queen Elizabeth II as Head of State",
            "B": "introduced an Executive Presidential system in place of the British Parliamentary system",
            "C": "established regional Houses of Assembly in Kaduna, Ibadan, and Enugu",
            "D": "abolished the federal civil service commission"
        },
        "correct_option": "B",
        "traps": {
            "A": "The British monarch was removed under the 1963 Republican Constitution.",
            "C": "Regional assemblies were established in colonial constitutions (1946 Richards & 1951 Macpherson).",
            "D": "The federal civil service was strengthened, not abolished."
        },
        "pedagogical_concept": "1979 Constitution: Drafted under the military regime of Obasanjo/Murtala Mohammed, it introduced the American-style Executive Presidential system, replacing the British Westminster Parliamentary model.",
        "socratic_prompt": "What system of government did Nigeria adopt in 1979 under President Shehu Shagari?"
    },
    {
        "id": "gov_009",
        "subject": "Government",
        "topic": "Elements of Government & Political Theory",
        "subtopic": "Rule of Law",
        "year": 2023,
        "question": "According to A.V. Dicey, the doctrine of the Rule of Law fundamentally incorporates all of the following principles EXCEPT _______.",
        "options": {
            "A": "Supremacy of regular law over arbitrary power",
            "B": "Equality of all citizens before the law",
            "C": "Immunity of state officials from standard judicial prosecution",
            "D": "Protection of fundamental human rights by the judiciary"
        },
        "correct_option": "C",
        "traps": {
            "A": "Supremacy of law is Dicey's primary pillar.",
            "B": "Equality before the law is Dicey's second pillar.",
            "D": "Predominance of the legal spirit and judicial protection of rights is Dicey's third pillar."
        },
        "pedagogical_concept": "A.V. Dicey's Rule of Law: Consists of three tenets: 1. Absolute supremacy of regular law (no arbitrary arrest). 2. Equality before the law (no man is above the law). 3. The constitution is the result of the ordinary law of the land. Immunity for officials violates equality before the law!",
        "socratic_prompt": "Can a government claim to operate under the Rule of Law if government officials are declared immune from standard judicial trials?"
    },

    # ---------------- LITERATURE IN ENGLISH ----------------
    {
        "id": "lit_006",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Catharsis & Tragedy",
        "year": 2024,
        "question": "In classical dramatic tragedy, the psychological purging or emotional cleansing of pity and fear experienced by the audience at the play's catastrophe is termed _______.",
        "options": {
            "A": "Hamartia",
            "B": "Catharsis",
            "C": "Hubris",
            "D": "Peripeteia"
        },
        "correct_option": "B",
        "traps": {
            "A": "Hamartia is the tragic character flaw (e.g. Macbeth's vaulting ambition).",
            "C": "Hubris is excessive arrogance or pride before the gods.",
            "D": "Peripeteia is the sudden reversal of fortune experienced by the protagonist."
        },
        "pedagogical_concept": "Aristotelian Poetics: Catharsis (from Greek katharsis, meaning purgation or cleansing) refers to the emotional release experienced by spectators during the climax of a tragic play.",
        "socratic_prompt": "When watching a tragic ending that makes you cry and feel deeply relieved and emotionally cleansed, what Greek term describes that emotional purge?"
    },
    {
        "id": "lit_007",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Figures of Speech",
        "year": 2023,
        "question": "'The pen is mightier than the sword.' This famous statement is a classical example of _______.",
        "options": {
            "A": "Synecdoche",
            "B": "Metonymy",
            "C": "Oxymoron",
            "D": "Euphemism"
        },
        "correct_option": "B",
        "traps": {
            "A": "Synecdoche uses a part of an object to represent the whole (e.g. 'all hands on deck'). Metonymy replaces a concept with an associated attribute (pen = the press/writing, sword = military force)!",
            "C": "Oxymoron places two contradictory words adjacent to each other (e.g. deafening silence).",
            "D": "Euphemism substitutes a mild term for a harsh reality (e.g. 'passed away')."
        },
        "pedagogical_concept": "Metonymy vs Synecdoche: Metonymy replaces the name of an entity with something closely associated with it ('the pen' for literature/journalism; 'the sword' for warfare). Synecdoche requires an actual part-to-whole anatomical or physical relationship.",
        "socratic_prompt": "Is a pen an actual physical part of a journalist, or is it an associated object representing the power of writing?"
    }
]

added_count = 0
for q in v4_batch:
    if q["id"] not in existing_ids:
        questions.append(q)
        existing_ids.add(q["id"])
        added_count += 1

with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Added {added_count} new high-yield questions. Total in question bank: {len(questions)}")
