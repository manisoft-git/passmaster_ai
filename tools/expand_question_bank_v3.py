import json

QUESTIONS_PATH = "data/questions.json"

with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

existing_ids = {q["id"] for q in questions}

v3_batch = [
    # --- USE OF ENGLISH ---
    {
        "id": "eng_008",
        "subject": "Use of English",
        "topic": "Lexis & Structure",
        "subtopic": "Synonyms & Antonyms",
        "year": 2024,
        "question": "Choose the option nearest in meaning to the capitalized word: The defense attorney presented a METICULOUS reconstruction of the events on the night of the incident.",
        "options": {
            "A": "Hasty and superficial",
            "B": "Painstaking and thorough",
            "C": "Aggressive and combative",
            "D": "Fabricated and imaginative"
        },
        "correct_option": "B",
        "traps": {
            "A": "'Hasty and superficial' is the direct antonym (opposite) of meticulous.",
            "C": "'Meticulous' refers to careful precision, not emotional aggression.",
            "D": "'Fabricated' implies dishonesty, whereas meticulous denotes rigorous factual detail."
        },
        "pedagogical_concept": "Lexis: 'Meticulous' (from Latin 'meticulosus') means showing extreme care about minute details; thorough, painstaking, and precise.",
        "socratic_prompt": "When someone checks every tiny detail three times to ensure perfection, what adjective describes that high degree of precision?"
    },
    {
        "id": "eng_009",
        "subject": "Use of English",
        "topic": "Oral Forms & Phonology",
        "subtopic": "Vowel Contrasts / Silent Letters",
        "year": 2023,
        "question": "Which of the following words contains the same vowel sound as the one represented in 'LEAP' (/iː/)?",
        "options": {
            "A": "Live",
            "B": "Deceive",
            "C": "Dead",
            "D": "Breadth"
        },
        "correct_option": "B",
        "traps": {
            "A": "'Live' contains the short lax vowel /ɪ/ (as in sit, pit).",
            "C": "'Dead' contains the short monophthong /e/ (as in bed, pen).",
            "D": "'Breadth' also contains /e/ (/bredθ/)."
        },
        "pedagogical_concept": "English Phonology (/iː/ vs /ɪ/ vs /e/): The digraph 'ei' in 'deceive' (/dɪˈsiːv/) produces the long close front unrounded vowel /iː/, identical to 'leap' (/liːp/).",
        "socratic_prompt": "Elongate the vowel sound in 'leap': is it a short clipped sound like 'bit', or a long tense vowel like 'meet' and 'deceive'?"
    },

    # --- MATHEMATICS ---
    {
        "id": "mth_007",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Quadratic Equations",
        "year": 2024,
        "question": "If α and β are the roots of the quadratic equation 2x² - 6x + 3 = 0, find the value of (α² + β²).",
        "options": {
            "A": "6",
            "B": "9",
            "C": "3/2",
            "D": "12"
        },
        "correct_option": "A",
        "traps": {
            "B": "You calculated (α + β)² = 3² = 9, but forgot to subtract 2αβ: α² + β² = (α + β)² - 2αβ!",
            "C": "3/2 is the product of roots (αβ = c/a = 3/2), not the sum of squares.",
            "D": "You added 2αβ instead of subtracting: 9 + 3 = 12."
        },
        "pedagogical_concept": "Symmetric Properties of Quadratic Roots: For ax² + bx + c = 0, sum of roots α + β = -b/a = -(-6)/2 = 3. Product of roots αβ = c/a = 3/2. Using algebraic identity: α² + β² = (α + β)² - 2αβ = (3)² - 2(3/2) = 9 - 3 = 6.",
        "socratic_prompt": "What is (α + β)² expanded? Notice that (α + β)² = α² + 2αβ + β². How do you isolate α² + β²?"
    },
    {
        "id": "mth_008",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Polynomials",
        "year": 2023,
        "question": "The 4th term of an Arithmetic Progression (A.P.) is 15 and the 9th term is 35. Find the first term (a) and common difference (d).",
        "options": {
            "A": "a = 3, d = 4",
            "B": "a = 4, d = 3",
            "C": "a = 5, d = 4",
            "D": "a = 2, d = 5"
        },
        "correct_option": "A",
        "traps": {
            "B": "You swapped the values of the first term a and common difference d.",
            "C": "You set T₄ = a + 4d instead of a + (4-1)d = a + 3d.",
            "D": "You made an arithmetic substitution error solving the simultaneous equations."
        },
        "pedagogical_concept": "Arithmetic Progression: T_n = a + (n-1)d. T₄ = a + 3d = 15; T₉ = a + 8d = 35. Subtracting equations: (8d - 3d) = (35 - 15) => 5d = 20 => d = 4. Substitute d = 4 into first eq: a + 3(4) = 15 => a = 15 - 12 = 3.",
        "socratic_prompt": "Recall the nth term formula: Tn = a + (n-1)d. What is the expression for T4 and T9? Subtract them to eliminate 'a'!"
    },

    # --- PHYSICS ---
    {
        "id": "phy_007",
        "subject": "Physics",
        "topic": "Mechanics",
        "subtopic": "Circular Motion",
        "year": 2024,
        "question": "A simple pendulum of length 1.0 m swings with small amplitude at a location where g = π² m/s². What is the period of oscillation?",
        "options": {
            "A": "1.0 s",
            "B": "2.0 s",
            "C": "4.0 s",
            "D": "0.5 s"
        },
        "correct_option": "B",
        "traps": {
            "A": "You forgot the factor of 2 in front of the formula: T = π √(L/g) instead of 2π √(L/g).",
            "C": "You squared the period.",
            "D": "You inverted the period to find frequency (f = 1/T = 0.5 Hz)."
        },
        "pedagogical_concept": "Period of a Simple Pendulum: T = 2π √(L/g). Since g = π², √(L/g) = √(1/π²) = 1/π. Thus, T = 2π × (1/π) = 2.0 seconds.",
        "socratic_prompt": "Substitute L = 1 and g = π² into T = 2π √(L/g). Notice how π cleanly cancels out!"
    },
    {
        "id": "phy_008",
        "subject": "Physics",
        "topic": "Electricity & Magnetism",
        "subtopic": "Capacitance",
        "year": 2023,
        "question": "Two capacitors of capacitances 4 µF and 6 µF are connected in SERIES across a 100 V DC source. What is the equivalent capacitance of the combination?",
        "options": {
            "A": "10.0 µF",
            "B": "2.4 µF",
            "C": "5.0 µF",
            "D": "0.42 µF"
        },
        "correct_option": "B",
        "traps": {
            "A": "10.0 µF is the equivalent capacitance in PARALLEL (C_p = C₁ + C₂ = 4 + 6 = 10 µF). Capacitors in series combine inversely!",
            "C": "You averaged the capacitances: (4 + 6) / 2 = 5.",
            "D": "0.42 is the reciprocal: 1/C = 5/12 = 0.417. You forgot to invert to find C = 12/5 = 2.4 µF."
        },
        "pedagogical_concept": "Series Capacitors: 1/C_eq = 1/C₁ + 1/C₂ = (C₁ * C₂) / (C₁ + C₂). Here: C_eq = (4 * 6) / (4 + 6) = 24 / 10 = 2.4 µF. Notice series capacitance is always less than the smallest individual capacitor.",
        "socratic_prompt": "Do capacitors in series add up directly like resistors in series, or do they combine as reciprocals: product over sum?"
    },

    # --- CHEMISTRY ---
    {
        "id": "chm_006",
        "subject": "Chemistry",
        "topic": "Inorganic Chemistry",
        "subtopic": "Acids, Bases & Salts",
        "year": 2024,
        "question": "What is the oxidation state of Chromium in potassium dichromate, K₂Cr₂O₇?",
        "options": {
            "A": "+3",
            "B": "+6",
            "C": "+7",
            "D": "+12"
        },
        "correct_option": "B",
        "traps": {
            "A": "+3 is the oxidation state of Chromium after reduction in acidic titration (Cr³⁺ green).",
            "C": "+7 is the oxidation state of Manganese in KMnO₄, not Chromium in K₂Cr₂O₇.",
            "D": "+12 is the total oxidation charge shared across both Chromium atoms (2 * +6 = +12)."
        },
        "pedagogical_concept": "Oxidation State Rules: Neutral compound total charge = 0. Potassium K = +1; Oxygen O = -2. 2(+1) + 2(Cr) + 7(-2) = 0 => +2 + 2Cr - 14 = 0 => 2Cr = 12 => Cr = +6.",
        "socratic_prompt": "What is the charge on K (+1) and O (-2)? Set up the algebraic equation 2(+1) + 2x + 7(-2) = 0 and solve for x!"
    },
    {
        "id": "chm_007",
        "subject": "Chemistry",
        "topic": "Physical Chemistry",
        "subtopic": "Rates of Reactions",
        "year": 2023,
        "question": "Why does granulated zinc react faster with dilute hydrochloric acid than a solid zinc block of identical mass?",
        "options": {
            "A": "Granulated zinc has a lower activation energy",
            "B": "Granulated zinc presents a vastly greater total surface area for effective molecular collisions",
            "C": "Granulated zinc increases the enthalpy change (ΔH) of the reaction",
            "D": "Granulated zinc functions as a homogeneous catalyst"
        },
        "correct_option": "B",
        "traps": {
            "A": "Surface area changes collision frequency, NOT activation energy (only catalysts lower activation energy).",
            "C": "Enthalpy change (ΔH) is a state function independent of particle size or reaction rate.",
            "D": "Zinc is a consumable reactant, not a catalyst."
        },
        "pedagogical_concept": "Collision Theory & Surface Area: Breaking a solid reactant into smaller granules increases the exposed surface area, increasing the frequency of collisions between reactant particles per second without altering activation energy or ΔH.",
        "socratic_prompt": "Does breaking a solid into powder change the chemical nature of the substance or does it expose more atoms on the outside to collide with acid ions?"
    },

    # --- BIOLOGY ---
    {
        "id": "bio_006",
        "subject": "Biology",
        "topic": "Physiology & Systems",
        "subtopic": "Photosynthesis",
        "year": 2024,
        "question": "During the light-dependent stage of photosynthesis in plant chloroplasts, oxygen gas (O₂) is released as a direct byproduct of _______.",
        "options": {
            "A": "the reduction of carbon dioxide in the Calvin cycle",
            "B": "the photolysis of water molecules",
            "C": "the oxidative breakdown of glucose",
            "D": "the synthesis of ATP from ADP"
        },
        "correct_option": "B",
        "traps": {
            "A": "CO₂ is fixed during the light-independent (dark) Calvin cycle to synthesize glucose; it does not yield oxygen gas.",
            "C": "Oxidative breakdown of glucose is cellular respiration, not photosynthesis.",
            "D": "ATP synthesis is driven by the proton gradient created during electron transport, not direct oxygen splitting."
        },
        "pedagogical_concept": "Photolysis of Water: 2H₂O + light energy → 4H⁺ + 4e⁻ + O₂↑. Oxygen produced in photosynthesis originates entirely from water molecules split by light-energized chlorophyll in the thylakoid membrane, not from CO₂.",
        "socratic_prompt": "Where does the oxygen released by trees come from: carbon dioxide (CO2) or the water (H2O) absorbed through the roots?"
    },
    {
        "id": "bio_007",
        "subject": "Biology",
        "topic": "Genetics & Heredity",
        "subtopic": "Variation & Mutation",
        "year": 2023,
        "question": "Which of the following human physical traits represents an example of DISCONTINUOUS variation?",
        "options": {
            "A": "Body height",
            "B": "Skin color",
            "C": "ABO blood group system",
            "D": "Body weight"
        },
        "correct_option": "C",
        "traps": {
            "A": "Height shows a smooth continuous spectrum influenced by polygenes and nutrition.",
            "B": "Skin color is a classic polygenic trait exhibiting continuous gradation across populations.",
            "D": "Weight is continuous and heavily modified by diet and environment."
        },
        "pedagogical_concept": "Continuous vs Discontinuous Variation: Discontinuous variation features distinct, discrete categories with no intermediates (e.g. ABO blood groups: A, B, AB, O; tongue rolling). Continuous variation shows a normal distribution curve (height, weight, skin tone).",
        "socratic_prompt": "Can someone have a blood group that is halfway between A and B, or are you strictly one distinct blood type?"
    },

    # --- ECONOMICS ---
    {
        "id": "eco_007",
        "subject": "Economics",
        "topic": "Production & Market Structures",
        "subtopic": "Monopoly vs Perfect Competition",
        "year": 2024,
        "question": "For a pure monopolist to practice first-degree or third-degree price discrimination profitably, which condition MUST be satisfied?",
        "options": {
            "A": "Consumers must be able to resell the product easily between markets",
            "B": "The monopolist must be able to prevent arbitrage (resale) and identify sub-markets with differing price elasticities of demand",
            "C": "The product must have thousands of close substitutes in competing stores",
            "D": "Marginal Cost must exceed Marginal Revenue across all market segments"
        },
        "correct_option": "B",
        "traps": {
            "A": "If consumers can resell (arbitrage), low-price buyers will undercut the monopolist by selling to high-price buyers, destroying the discrimination scheme!",
            "C": "Close substitutes destroy monopoly power; monopolies require unique products without close substitutes.",
            "D": "Profit maximization always requires MR = MC, not MC > MR."
        },
        "pedagogical_concept": "Conditions for Price Discrimination: 1. Monopoly power. 2. Separation of markets with zero possibility of resale (no arbitrage). 3. Different price elasticities of demand in each sub-market (higher prices charged to inelastic buyers).",
        "socratic_prompt": "Why can an airline charge student discounts without businessmen buying the cheap student tickets? How does the firm prevent one group from reselling to another?"
    },
    {
        "id": "eco_008",
        "subject": "Economics",
        "topic": "National Income & Macroeconomics",
        "subtopic": "Fiscal Policy Instruments",
        "year": 2023,
        "question": "A tax system in which higher-income earners pay a HIGHER percentage of their income in tax than lower-income earners is classified as _______.",
        "options": {
            "A": "Regressive tax",
            "B": "Progressive tax",
            "C": "Proportional tax",
            "D": "Specific excise duty"
        },
        "correct_option": "B",
        "traps": {
            "A": "A regressive tax takes a HIGHER proportion from the poor (e.g. flat sales tax on staple bread).",
            "C": "A proportional tax takes the EXACT same percentage (e.g. flat 10%) from all income levels regardless of wealth.",
            "D": "Specific duties are fixed monetary amounts per physical unit, not percentage-based income taxes."
        },
        "pedagogical_concept": "Taxation Systems: Progressive taxation (like Pay-As-You-Earn / PAYE) increases the marginal tax rate as taxable income brackets rise, functioning as an automatic fiscal stabilizer and wealth redistribution mechanism.",
        "socratic_prompt": "If someone earning ₦100,000 pays 5% tax, while someone earning ₦5,000,000 pays 25% tax, is the tax rate progressing upward with wealth?"
    },

    # --- GOVERNMENT ---
    {
        "id": "gov_007",
        "subject": "Government",
        "topic": "Constitutional Development in Nigeria",
        "subtopic": "1999 Constitution Provisions",
        "year": 2023,
        "question": "The 1963 Republican Constitution of Nigeria was historically significant primarily because it _______.",
        "options": {
            "A": "established the Supreme Court as the final court of appeal, replacing appeals to the British Privy Council",
            "B": "introduced the presidential system of government headed by an executive president",
            "C": "amalgamated the Northern and Southern protectorates",
            "D": "created the first regional Houses of Assembly"
        },
        "correct_option": "A",
        "traps": {
            "B": "The 1963 Constitution retained the Parliamentary (Westminster) system with a ceremonial President (Nnamdi Azikiwe) and Prime Minister (Tafawa Balewa). Executive presidency came in 1979!",
            "C": "Amalgamation occurred in 1914 under Lord Lugard.",
            "D": "Regional houses were introduced under the 1946 Richards and 1951 Macpherson Constitutions."
        },
        "pedagogical_concept": "1963 Republican Constitution: Severed Nigeria's last constitutional ties to the British Crown: 1. Queen Elizabeth II ceased to be Nigeria's head of state. 2. The Judicial Committee of the Privy Council in London was abolished as Nigeria's apex appellate body, making the Supreme Court of Nigeria sovereign and final.",
        "socratic_prompt": "What does 'Republican' mean? Can a republic still have a foreign Queen as head of state or appeal its legal cases to London courts?"
    },

    # --- LITERATURE IN ENGLISH ---
    {
        "id": "lit_005",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Dramatic Irony & Catharsis",
        "year": 2024,
        "question": "When the audience in a theater possesses vital information that the characters on stage are completely oblivious to, creating acute tension, this device is known as _______.",
        "options": {
            "A": "Comic relief",
            "B": "Dramatic irony",
            "C": "Deus ex machina",
            "D": "Anagnorisis"
        },
        "correct_option": "B",
        "traps": {
            "A": "Comic relief provides humorous respite during intense tragedy (e.g. the Porter scene in Macbeth).",
            "C": "Deus ex machina is an unexpected artificial plot intervention that abruptly resolves a tangled dilemma.",
            "D": "Anagnorisis is the moment of critical discovery or realization experienced BY THE CHARACTER."
        },
        "pedagogical_concept": "Dramatic Irony: A literary device where the audience understands the true reality of a situation while characters act in ignorance (e.g., Oedipus vowing to hunt down the murderer of King Laius, unaware that he himself is the murderer).",
        "socratic_prompt": "When watching a suspenseful play where you know the villain poisoned the drink, but the hero smilingly picks up the glass, what type of irony is that?"
    }
]

added_v3 = 0
for q in v3_batch:
    if q["id"] not in existing_ids:
        questions.append(q)
        existing_ids.add(q["id"])
        added_v3 += 1

with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully added {added_v3} new questions! Grand total questions in bank: {len(questions)}")
