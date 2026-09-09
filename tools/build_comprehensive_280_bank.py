import json
import os
import sys
import random

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def create_mega_bank():
    from tools.questions_batch_stem import math_questions, physics_questions, chemistry_questions, biology_questions
    from tools.questions_batch_arts import english_questions, economics_questions, government_questions, literature_questions
    from tools.extra_blueprints import extra_blueprints

    with open("data/questions.json", "r", encoding="utf-8") as f:
        existing_list = json.load(f)

    # Harmonize existing questions
    topic_corrections = {
        "phy_001": ("Thermal Physics & Waves", "Gas Laws & Absolute Temperature"),
        "phy_003": ("Thermal Physics & Waves", "Gas Laws"),
        "phy_004": ("Thermal Physics & Waves", "Wave Characteristics"),
        "phy_005": ("Electricity & Magnetism", "Circuit Analysis"),
        "phy_006": ("Mechanics", "Friction"),
        "phy_007": ("Thermal Physics & Waves", "Resonance"),
        "phy_008": ("Thermal Physics & Waves", "Optics"),
        "phy_009": ("Electricity & Magnetism", "Internal Resistance"),
        "phy_010": ("Modern & Atomic Physics", "Radioactivity"),
        "mth_003": ("Statistics & Probability", "Independent vs Dependent Events"),
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

    questions_by_id = {}
    for q in existing_list:
        if q["id"] in topic_corrections:
            q["topic"] = topic_corrections[q["id"]][0]
            q["subtopic"] = topic_corrections[q["id"]][1]
        questions_by_id[q["id"]] = q

    # Add batch 1 items
    batch1 = (
        math_questions + physics_questions + chemistry_questions + biology_questions +
        english_questions + economics_questions + government_questions + literature_questions
    )
    for q in batch1:
        questions_by_id[q["id"]] = q

    # Now define expansion templates to bring each subject up to 35 questions (total 280 questions)
    subject_targets = {
        "Use of English": 35,
        "Mathematics": 35,
        "Physics": 35,
        "Chemistry": 35,
        "Biology": 35,
        "Economics": 35,
        "Government": 35,
        "Literature in English": 35
    }

    # High yield question blueprints
    blueprints = {
        "Use of English": [
            ("Concord & Grammar", "Correlative Conjunctions", "Not only the governor but also his commissioners _______ present at the venue.", {"A": "was", "B": "were", "C": "is", "D": "has been"}, "B", "Rule of Proximity with plural 'commissioners'", "Remember to match the subject closest to the verb in correlative constructions."),
            ("Concord & Grammar", "Collective Nouns", "The jury _______ divided in their opinions regarding the culpability of the defendant.", {"A": "is", "B": "are", "C": "was", "D": "has been"}, "B", "When members of a collective noun act as individuals with opposing views, the verb is plural.", "Are the members of the jury acting as a single unit or disagreeing individually?"),
            ("Concord & Grammar", "Mathematical Quantities", "Ten miles _______ a long distance to walk in this scorching heat.", {"A": "is", "B": "are", "C": "were", "D": "have been"}, "A", "Periods of time, amounts of money, and distances are considered singular units.", "Is ten miles viewed as a single distance unit?"),
            ("Lexis & Structure", "Prepositional Idioms", "The military command took exception _______ the false media report.", {"A": "to", "B": "with", "C": "against", "D": "at"}, "A", "The idiom is 'take exception to' (meaning to object or take offense).", "What preposition does the expression 'take exception' pair with?"),
            ("Lexis & Structure", "Antonyms in Context", "His lavish spending eventually led to insolvency. The antonym of 'lavish' is:", {"A": "frugal", "B": "generous", "C": "wasteful", "D": "opulent"}, "A", "Frugal means sparing or economical with money, opposite of lavish.", "What is the opposite of spending extravagantly?"),
            ("Lexis & Structure", "Phrasal Verbs", "The sudden death of the chairman brought _______ a complete restructuring of the board.", {"A": "about", "B": "out", "C": "up", "D": "forth"}, "A", "'Bring about' means to cause something to happen.", "Which phrasal verb means to cause an event?"),
            ("Oral Forms & Phonology", "Silent Consonants", "In which of the following words is the letter 'b' silent?", {"A": "Subtle", "B": "Probable", "C": "Robust", "D": "Cabinet"}, "A", "The letter 'b' is completely silent in 'subtle' (/ˈsʌtl/).", "Is the 'b' pronounced in subtle, or is it silent?"),
            ("Oral Forms & Phonology", "Syllabic Stress", "Which syllable receives the primary stress in the word 'CONFIDENTIAL'?", {"A": "CON-fi-den-tial", "B": "con-FI-den-tial", "C": "con-fi-DEN-tial", "D": "con-fi-den-TIAL"}, "C", "Suffix -tial causes stress on the penultimate syllable (DEN).", "Words ending in -tial place primary stress on which syllable?"),
            ("Oral Forms & Phonology", "Diphthongs", "Which of the following words contains the diphthong /aɪ/ as in 'BYTE'?", {"A": "Height", "B": "Eight", "C": "Weight", "D": "Bait"}, "A", "'Height' is pronounced /haɪt/, containing the diphthong /aɪ/.", "How do you pronounce 'height' compared to 'eight' or 'weight'?"),
            ("Comprehension & Prescribed Text", "Character Analysis", "In 'The Life Changer', what role did Habib play in the lives of the female undergraduates?", {"A": "A wealthy, predatory politician using gifts to manipulate students", "B": "A dedicated academic counselor promoting female education", "C": "A police investigator tracking campus cultists", "D": "Ummi's supportive elder brother"}, "A", "Habib used his wealth to entice young girls into transactional campus relationships.", "How does the novel portray Habib's interactions with young students?"),
            ("Comprehension & Prescribed Text", "Literary Devices", "The phrase 'The fiery sun melted the asphalt on the highway' is an example of:", {"A": "Hyperbole", "B": "Simile", "C": "Irony", "D": "Synecdoche"}, "A", "Hyperbole is deliberate exaggeration for dramatic emphasis.", "Did the sun literally melt the road, or is it an exaggeration?"),
            ("Comprehension & Prescribed Text", "Authorial Purpose", "When an author writes to mock human foolishness using humor and irony, the work is:", {"A": "A satire", "B": "An elegy", "C": "A panegyric", "D": "An ode"}, "A", "Satire exposes and ridicules vice, folly, or hypocrisy.", "What genre uses wit and ridicule to criticize human shortcomings?"),
            ("Concord & Grammar", "Subjunctive Clauses", "The regulations require that every candidate _______ their biometric verification.", {"A": "complete", "B": "completes", "C": "completed", "D": "must complete"}, "A", "Mandative subjunctive takes the base infinitive without 's'.", "What form of the verb follows 'require that' regardless of subject number?"),
            ("Lexis & Structure", "Prepositional Idioms", "The commissioner presided _______ the emergency security meeting.", {"A": "over", "B": "at", "C": "on", "D": "in"}, "A", "'Preside over' is the mandatory prepositional collocation.", "Do you preside 'on' a meeting or preside 'over' it?"),
            ("Oral Forms & Phonology", "Consonant Contrasts", "Which of the following words contains the voiceless dental fricative /θ/ as in 'THINK'?", {"A": "Breath", "B": "Breathe", "C": "Though", "D": "Mother"}, "A", "'Breath' (noun) ends in /θ/, whereas 'breathe' (verb) ends in /ð/.", "Which word has the soft 'th' sound of think instead of the voiced 'th' of this?")
        ],
        "Mathematics": [
            ("Algebra", "Symmetric Functions of Roots", "If α and β are the roots of 3x² - 9x + 2 = 0, find the value of 1/α + 1/β.", {"A": "9/2", "B": "2/9", "C": "3/2", "D": "6"}, "A", "1/α + 1/β = (α + β)/αβ. Here α + β = -(-9)/3 = 3, and αβ = 2/3. Therefore, 3 / (2/3) = 9/2.", "What is the common denominator for 1/α + 1/β?"),
            ("Algebra", "Geometric Progressions", "The second term of a GP is 6 and the fifth term is 48. Find the common ratio (r) and first term (a).", {"A": "r = 2, a = 3", "B": "r = 3, a = 2", "C": "r = 4, a = 1.5", "D": "r = 2, a = 6"}, "A", "T₅/T₂ = ar⁴/ar = r³ = 48/6 = 8 => r = 2. Then a = T₂/r = 6/2 = 3.", "If dividing the 5th term by the 2nd term gives r³, what is r?"),
            ("Algebra", "Polynomial Division", "Find the remainder when P(x) = 2x³ - 5x² + 4x - 7 is divided by (x - 2).", {"A": "-3", "B": "5", "C": "-7", "D": "1"}, "A", "By the Remainder Theorem, evaluate P(2) = 2(8) - 5(4) + 4(2) - 7 = 16 - 20 + 8 - 7 = -3.", "What does the Remainder Theorem say when evaluating P(x) at x = 2?"),
            ("Calculus", "Product Rule", "Differentiate y = x² sin x with respect to x.", {"A": "2x sin x + x² cos x", "B": "2x cos x", "C": "x² cos x - 2x sin x", "D": "2x sin x - x² cos x"}, "A", "Product Rule: d(uv)/dx = u'v + uv' = 2x sin x + x² cos x.", "In the product rule, do you differentiate both terms simultaneously or one at a time?"),
            ("Calculus", "Definite Integration of Trigonometric Functions", "Evaluate ∫ [0 to π/2] cos x dx.", {"A": "1", "B": "0", "C": "-1", "D": "π/2"}, "A", "∫ cos x dx = [sin x] from 0 to π/2 = sin(π/2) - sin(0) = 1 - 0 = 1.", "What is the antiderivative of cos x evaluated between 0 and π/2?"),
            ("Calculus", "Rate of Change", "The radius of a circular oil slick expands at a rate of 2 m/s. Find the rate of increase of its area when radius r = 5 m.", {"A": "20π m²/s", "B": "10π m²/s", "C": "25π m²/s", "D": "50π m²/s"}, "A", "A = πr² => dA/dt = 2πr (dr/dt) = 2π(5)(2) = 20π m²/s.", "Using the chain rule dA/dt = (dA/dr) × (dr/dt), what is 2πr × 2 when r = 5?"),
            ("Geometry & Trigonometry", "Alternate Segment Theorem", "A tangent PT touches a circle at T, and chord TA forms an angle of 65° with PT. What is the angle subtended by chord TA in the alternate segment?", {"A": "65°", "B": "115°", "C": "130°", "D": "25°"}, "A", "By the Alternate Segment Theorem, the angle between tangent and chord equals the angle in the alternate segment (65°).", "Does the angle between a tangent and chord equal the angle in the alternate segment?"),
            ("Geometry & Trigonometry", "Cosine Rule", "In triangle ABC, side b = 5 cm, c = 8 cm, and angle A = 60°. Find side a.", {"A": "7 cm", "B": "8 cm", "C": "6 cm", "D": "9 cm"}, "A", "Cosine Rule: a² = b² + c² - 2bc cos A = 25 + 64 - 2(5)(8)(0.5) = 89 - 40 = 49 => a = 7 cm.", "What formula relates three sides of a triangle to an included angle?"),
            ("Geometry & Trigonometry", "Coordinate Distance", "Find the distance between the points A(-2, 3) and B(4, -5).", {"A": "10 units", "B": "8 units", "C": "12 units", "D": "14 units"}, "A", "Distance d = √[(4 - (-2))² + (-5 - 3)²] = √[6² + (-8)²] = √[36 + 64] = √100 = 10.", "What is the Euclidean distance formula between two coordinate points?"),
            ("Statistics & Probability", "Conditional Probability", "A bag contains 5 red balls and 3 green balls. Two balls are drawn successively without replacement. Find the probability that both are red.", {"A": "5/14", "B": "25/64", "C": "15/56", "D": "5/28"}, "A", "P(R₁) = 5/8. P(R₂|R₁) = 4/7. P(Both red) = (5/8) × (4/7) = 20/56 = 5/14.", "When a ball is drawn without replacement, does the total denominator decrease?"),
            ("Statistics & Probability", "Mean and Median", "The median of the distribution 3, 7, 8, 12, 14, 18, 21 is:", {"A": "12", "B": "11", "C": "14", "D": "10"}, "A", "The list has 7 sorted numbers. The middle (4th) value is 12.", "In an ordered set of 7 numbers, which position gives the median?"),
            ("Statistics & Probability", "Combinations", "How many different triangles can be formed by joining the vertices of a regular octagon (8-sided polygon)?", {"A": "56", "B": "336", "C": "28", "D": "24"}, "A", "A triangle requires 3 vertices out of 8. Order does not matter: 8C3 = 56.", "How many vertices define a triangle, and does the order of selection matter?"),
            ("Algebra", "Indices and Roots", "Solve for x: 2^(2x + 1) = 32.", {"A": "2", "B": "3", "C": "4", "D": "5"}, "A", "32 = 2⁵ => 2x + 1 = 5 => 2x = 4 => x = 2.", "What power of 2 equals 32?"),
            ("Calculus", "Integration by Substitution", "Evaluate ∫ 2x (x² + 3)⁴ dx.", {"A": "1/5 (x² + 3)⁵ + C", "B": "1/4 (x² + 3)⁴ + C", "C": "(x² + 3)⁵ + C", "D": "2/5 (x² + 3)⁵ + C"}, "A", "Let u = x² + 3 => du = 2x dx. Integral becomes ∫ u⁴ du = u⁵/5 + C = 1/5(x² + 3)⁵ + C.", "Notice that 2x is the exact derivative of x² + 3, so substitution u = x² + 3 works directly.")
        ],
        "Physics": [
            ("Mechanics", "Circular Motion", "A car travels around a circular bend of radius 50 m on a level road at 20 m/s. What is the centripetal acceleration?", {"A": "8 m/s²", "B": "4 m/s²", "C": "10 m/s²", "D": "2 m/s²"}, "A", "Centripetal acceleration a_c = v² / r = (20)² / 50 = 400 / 50 = 8 m/s².", "What formula gives the inward acceleration in uniform circular motion?"),
            ("Mechanics", "Simple Pendulum", "If the length of a simple pendulum is increased by a factor of 4, its period of oscillation will:", {"A": "Double", "B": "Quadruple", "C": "Halve", "D": "Remain unchanged"}, "A", "T = 2π√(l / g). Since T is proportional to √l, multiplying l by 4 results in √4 = 2 times the original period.", "How does the period of a pendulum relate mathematically to the square root of its length?"),
            ("Mechanics", "Friction", "A block of mass 10 kg rests on a rough horizontal floor with coefficient of static friction μ = 0.4. What horizontal force is required to set it in motion? (g = 10 m/s²)", {"A": "40 N", "B": "25 N", "C": "100 N", "D": "4 N"}, "A", "Limiting friction F_L = μ R = μ mg = 0.4 × 10 × 10 = 40 N.", "What is the normal reaction force R for a 10 kg block resting on horizontal ground?"),
            ("Thermal Physics & Waves", "Doppler Effect", "When a train sounding its whistle approaches a stationary observer on a platform, the observer detects a sound with:", {"A": "A higher frequency and shorter apparent wavelength", "B": "A lower frequency and longer wavelength", "C": "The exact same frequency but higher amplitude", "D": "Zero pitch"}, "A", "Approaching source compresses wavefronts, increasing observed frequency f' > f.", "When an emitting source moves towards you, are the wavefronts compressed or stretched?"),
            ("Thermal Physics & Waves", "Wave Equation", "A wave travels through a medium with frequency 250 Hz and wavelength 1.36 m. Calculate the wave speed.", {"A": "340 m/s", "B": "184 m/s", "C": "500 m/s", "D": "680 m/s"}, "A", "Wave speed v = f × λ = 250 Hz × 1.36 m = 340 m/s.", "What is the fundamental wave formula connecting speed, frequency, and wavelength?"),
            ("Thermal Physics & Waves", "Latent Heat", "How much heat energy is required to melt 0.5 kg of ice at 0°C into water at 0°C? (Specific latent heat of fusion of ice = 3.36 × 10⁵ J/kg)", {"A": "1.68 × 10⁵ J", "B": "3.36 × 10⁵ J", "C": "6.72 × 10⁵ J", "D": "8.40 × 10⁴ J"}, "A", "Q = mL_f = 0.5 kg × 3.36 × 10⁵ J/kg = 1.68 × 10⁵ J.", "During a phase change at constant temperature, is heat calculated using Q = mL?"),
            ("Electricity & Magnetism", "Faraday's Law of Induction", "The magnitude of the electromotive force (emf) induced in a coil is directly proportional to the:", {"A": "Rate of change of magnetic flux linkage", "B": "Total electrical resistance of the circuit", "C": "Temperature of the magnet", "D": "Permeability of free space alone"}, "A", "Faraday's Law of Induction: ε = -N (dΦ/dt).", "What causes an induced emf according to Faraday's Law?"),
            ("Electricity & Magnetism", "Capacitor Networks", "Two capacitors of capacitances 4 μF and 6 μF are connected in parallel across a 12 V battery. What is the total stored charge?", {"A": "120 μC", "B": "28.8 μC", "C": "24 μC", "D": "72 μC"}, "A", "Parallel capacitance C_total = C₁ + C₂ = 4 + 6 = 10 μF. Q = C_total × V = 10 μF × 12 V = 120 μC.", "How do capacitances combine when connected in parallel?"),
            ("Electricity & Magnetism", "Resistor Networks", "Three identical resistors each of 12 Ω are connected in parallel. What is the equivalent resistance?", {"A": "4 Ω", "B": "36 Ω", "C": "6 Ω", "D": "12 Ω"}, "A", "1/R_eq = 1/12 + 1/12 + 1/12 = 3/12 = 1/4 => R_eq = 4 Ω.", "For n identical resistors in parallel, is the equivalent resistance simply R/n?"),
            ("Modern & Atomic Physics", "Nuclear Binding Energy", "The mass defect in a nuclear fusion reaction is converted directly into energy according to which fundamental equation?", {"A": "E = Δm c²", "B": "E = hf", "C": "E = 1/2 mv²", "D": "E = qV"}, "A", "Einstein's mass-energy equivalence principle states that energy E = Δm c².", "Which equation links mass defect Δm to liberated nuclear energy?"),
            ("Modern & Atomic Physics", "De Broglie Wavelength", "Calculate the de Broglie wavelength of an electron moving with momentum 3.315 × 10⁻²⁴ kg·m/s. (Planck's constant h = 6.63 × 10⁻³⁴ J·s)", {"A": "2.0 × 10⁻¹⁰ m", "B": "0.5 × 10⁻¹⁰ m", "C": "1.0 × 10⁻¹⁰ m", "D": "4.0 × 10⁻¹⁰ m"}, "A", "λ = h / p = (6.63 × 10⁻³⁴) / (3.315 × 10⁻²⁴) = 2.0 × 10⁻¹⁰ m.", "How is de Broglie wavelength related to Planck's constant and linear momentum?"),
            ("Modern & Atomic Physics", "Radioactive Decay Series", "When an unstable nucleus emits an alpha particle, how do its atomic number (Z) and mass number (A) change?", {"A": "Z decreases by 2, A decreases by 4", "B": "Z increases by 1, A remains unchanged", "C": "Z decreases by 1, A remains unchanged", "D": "Z decreases by 4, A decreases by 2"}, "A", "An alpha particle is a helium nucleus (⁴₂He), carrying 2 protons and 2 neutrons.", "What is the composition of an alpha particle in terms of protons and mass number?"),
            ("Mechanics", "Universal Gravitation", "If the distance between two spherical masses is doubled, the gravitational attraction between them becomes:", {"A": "One-quarter as great", "B": "Half as great", "C": "Twice as great", "D": "Four times as great"}, "A", "Newton's Law of Universal Gravitation: F = G m₁m₂ / r². Doubling r multiplies denominator by 4.", "How does gravitational force vary with distance r according to the inverse-square law?")
        ],
        "Chemistry": [
            ("Physical & General Chemistry", "Mole Concept", "How many atoms are present in 12 g of magnesium metal? (M = 24 g/mol, N_A = 6.02 × 10²³ atoms/mol)", {"A": "3.01 × 10²³ atoms", "B": "6.02 × 10²³ atoms", "C": "1.20 × 10²⁴ atoms", "D": "1.50 × 10²³ atoms"}, "A", "Moles n = 12 / 24 = 0.5 mol. Atoms = 0.5 × 6.02 × 10²³ = 3.01 × 10²³ atoms.", "If 24 g of magnesium contains 1 mole of atoms, how many atoms are in 12 g?"),
            ("Physical & General Chemistry", "Thermochemistry", "An endothermic chemical reaction is characterized by:", {"A": "Positive enthalpy change (ΔH > 0) and absorption of heat from the surroundings", "B": "Negative enthalpy change (ΔH < 0) and liberation of heat", "C": "Zero temperature change", "D": "A spontaneous drop in activation energy"}, "A", "Endothermic reactions absorb thermal energy from surroundings, so products have higher enthalpy than reactants (ΔH > 0).", "When a chemical system absorbs heat, is the enthalpy change positive or negative?"),
            ("Physical & General Chemistry", "Rates of Reaction", "Increasing the surface area of a solid reactant increases the reaction rate because:", {"A": "It increases the frequency of effective particle collisions", "B": "It lowers the activation energy barrier", "C": "It increases the kinetic energy of the molecules", "D": "It alters the enthalpy of the reaction"}, "A", "Collision Theory: More exposed surface area allows more frequent collisions per unit time.", "Does grinding a solid into a fine powder increase the number of accessible collision sites?"),
            ("Inorganic Chemistry", "Halogen Reactivity", "Which of the following halogens is the strongest oxidizing agent in aqueous solution?", {"A": "Fluorine (F₂)", "B": "Chlorine (Cl₂)", "C": "Bromine (Br₂)", "D": "Iodine (I₂)"}, "A", "Fluorine has the highest standard reduction potential (+2.87 V) and greatest electronegativity, making it the strongest oxidizing agent.", "Which halogen has the greatest affinity to gain electrons down Group 7?"),
            ("Inorganic Chemistry", "Complex Ion Formation", "When excess aqueous ammonia is added to copper(II) sulfate solution, the precipitate dissolves to form a deep blue solution containing:", {"A": "[Cu(NH₃)₄]²⁺", "B": "[Cu(OH)₄]²⁻", "C": "[Cu(H₂O)₄]²⁺", "D": "[CuCl₄]²⁻"}, "A", "Excess NH₃ dissolves pale blue Cu(OH)₂ to form tetraamminecopper(II) complex ion [Cu(NH₃)₄]²⁺ (deep royal blue).", "What coordination complex forms when copper ions interact with excess ammonia?"),
            ("Inorganic Chemistry", "Iron Metallurgy", "In the blast furnace extraction of iron, limestone (CaCO₃) is added primarily to:", {"A": "Remove silica impurities as molten slag (CaSiO₃)", "B": "Reduce iron(III) oxide to metallic iron", "C": "Provide fuel to heat the furnace", "D": "Act as an oxidizing agent"}, "A", "CaCO₃ decomposes to CaO, which reacts with acidic silica (SiO₂) to form molten calcium silicate slag: CaO + SiO₂ -> CaSiO₃.", "How is sandy silica impurity removed from iron inside the blast furnace?"),
            ("Organic Chemistry", "Functional Groups", "What functional group is present in the compound CH₃-CO-CH₂-CH₃?", {"A": "Ketone (alkanone)", "B": "Aldehyde (alkanal)", "C": "Ester", "D": "Carboxylic acid"}, "A", "The carbonyl group (C=O) bonded between two carbon atoms defines a ketone (butan-2-one).", "Is a C=O group flanked by two carbons an aldehyde or a ketone?"),
            ("Organic Chemistry", "Geometric Isomerism", "Which of the following compounds exhibits cis-trans (geometric) isomerism?", {"A": "But-2-ene", "B": "But-1-ene", "C": "Propene", "D": "2-Methylpropene"}, "A", "But-2-ene (CH₃-CH=CH-CH₃) has two different groups (H and CH₃) attached to each double-bonded carbon.", "Which alkene has different substituents attached to both double-bonded carbons?"),
            ("Organic Chemistry", "Esterification", "Heating ethanoic acid with ethanol in the presence of concentrated H₂SO₄ catalyst yields ethyl ethanoate. This reaction is classified as:", {"A": "Esterification", "B": "Saponification", "C": "Dehydrogenation", "D": "Polymerization"}, "A", "The condensation of a carboxylic acid and an alkanol to form an ester and water is esterification.", "What is the reaction between an organic acid and alcohol called?"),
            ("Environmental & Industrial Chemistry", "The Contact Process", "What catalyst is used in the industrial manufacture of sulfuric acid by the Contact Process?", {"A": "Vanadium(V) oxide (V₂O₅)", "B": "Finely divided iron (Fe)", "C": "Platinum gauze", "D": "Nickel (Ni)"}, "A", "V₂O₅ catalyzes the reversible oxidation of SO₂ to SO₃ at 450°C in the Contact Process.", "Which transition metal oxide catalyzes sulfur dioxide oxidation in the Contact Process?"),
            ("Environmental & Industrial Chemistry", "Faraday's Electrolysis Law", "How many Faradays of electricity are required to deposit 1 mole of aluminum from molten Al₂O₃?", {"A": "3 Faradays", "B": "1 Faraday", "C": "2 Faradays", "D": "6 Faradays"}, "A", "Al³⁺ + 3e⁻ -> Al. Each mole of Al³⁺ requires 3 moles of electrons = 3 Faradays.", "What is the ionic charge on aluminum in Al³⁺?"),
            ("Environmental & Industrial Chemistry", "Acid Rain Chemistry", "Which atmospheric pollutant is primarily responsible for the formation of acid rain?", {"A": "Sulfur dioxide (SO₂)", "B": "Carbon monoxide (CO)", "C": "Methane (CH₄)", "D": "Argon (Ar)"}, "A", "SO₂ reacts with atmospheric moisture to produce sulfurous and sulfuric acids, leading to precipitation with pH < 5.6.", "Which sulfur gas dissolves in rainwater to form strong acid precipitation?"),
            ("Physical & General Chemistry", "Equilibrium Expressions", "For the reaction N₂(g) + 3H₂(g) ⇌ 2NH₃(g), the equilibrium constant expression K_c is:", {"A": "[NH₃]² / ([N₂][H₂]³)", "B": "[N₂][H₂]³ / [NH₃]²", "C": "[2NH₃] / ([N₂][3H₂])", "D": "[NH₃] / ([N₂][H₂])"}, "A", "K_c is the ratio of product concentrations raised to stoichiometric coefficients over reactant concentrations.", "How are stoichiometric coefficients placed in the equilibrium expression K_c?")
        ],
        "Biology": [
            ("Cellular Biology & Life Processes", "Enzyme Specificity", "Enzyme activity is inhibited at high temperatures primarily because:", {"A": "The tertiary protein structure is denatured, destroying the active site", "B": "Substrate molecules move too fast to bind", "C": "Water evaporates from the cell cytoplasm", "D": "The enzyme is converted into carbohydrates"}, "A", "Heat breaks hydrogen and disulfide bonds stabilizing the active site geometry, leading to irreversible denaturation.", "What happens to the delicate three-dimensional shape of a protein active site at 60°C?"),
            ("Cellular Biology & Life Processes", "Mitosis vs Meiosis", "Which of the following processes occurs during meiosis but NOT during mitosis?", {"A": "Pairing of homologous chromosomes and crossing over", "B": "Spindle fiber formation", "C": "Chromatid separation", "D": "Nuclear membrane breakdown"}, "A", "Synapsis and genetic crossing over between homologous chromosomes occur only during Prophase I of meiosis.", "In which type of cell division do homologous chromosomes exchange genetic segments?"),
            ("Cellular Biology & Life Processes", "Active Transport", "Active transport differs from passive diffusion because it requires:", {"A": "ATP metabolic energy and transport against a concentration gradient", "B": "A freely permeable membrane", "C": "Water molecules only", "D": "Zero carrier proteins"}, "A", "Active transport moves solutes uphill against their electrochemical gradient using cellular energy from ATP hydrolysis.", "What form of cellular currency is required to pump molecules against their concentration gradient?"),
            ("Human Physiology & Systems", "Nervous Coordination", "The junction across which an action potential is chemically transmitted from one neuron to the next is the:", {"A": "Synapse", "B": "Myelin sheath", "C": "Axon hillock", "D": "Dendrite tip"}, "A", "The synapse is the microscopic gap across which neurotransmitters (acetylcholine) diffuse to stimulate the postsynaptic membrane.", "What is the specialized microscopic gap between two neurons called?"),
            ("Human Physiology & Systems", "Endocrine System", "Which hormone secreted by the pancreas regulates blood glucose levels by promoting glucose uptake into liver and muscle cells?", {"A": "Insulin", "B": "Glucagon", "C": "Adrenaline", "D": "Thyroxine"}, "A", "Insulin secreted by beta cells of islets of Langerhans lowers blood glucose by converting it to glycogen.", "Which hormone lowers elevated blood sugar after a meal?"),
            ("Human Physiology & Systems", "Digestion", "In the human digestive tract, the digestion of cooked carbohydrates begins in the:", {"A": "Mouth by salivary amylase", "B": "Stomach by pepsin", "C": "Duodenum by bile", "D": "Ileum by lipase"}, "A", "Salivary amylase (ptyalin) begins hydrolyzing cooked starch into maltose in the mouth at neutral pH.", "Which digestive fluid in the oral cavity breaks down starch?"),
            ("Genetics & Evolution", "Incomplete Dominance", "A cross between a red-flowered plant (RR) and a white-flowered plant (WW) produces all pink-flowered offspring (RW). This phenomenon illustrates:", {"A": "Incomplete dominance", "B": "Codominance", "C": "Epistasis", "D": "Multiple alleles"}, "A", "Incomplete dominance occurs when neither allele is completely dominant, producing an intermediate blend in heterozygotes.", "When red and white alleles blend to produce pink offspring, what dominance pattern is shown?"),
            ("Genetics & Evolution", "Sickle Cell Trait", "Individuals with sickle cell trait (HbA HbS) enjoy a selective evolutionary advantage in West Africa because:", {"A": "Their red blood cells inhibit the proliferation of Plasmodium falciparum malaria", "B": "They are completely immune to all bacterial infections", "C": "They carry more oxygen than normal individuals", "D": "Their red blood cells never sickle under any conditions"}, "A", "Balanced polymorphism: The presence of HbS creates hostile intracellular conditions for the malaria parasite.", "Why has the sickle-cell carrier gene survived at high frequencies in malaria-endemic regions?"),
            ("Genetics & Evolution", "DNA Replication", "According to the Watson-Crick model, DNA replication is described as:", {"A": "Semi-conservative", "B": "Conservative", "C": "Dispersive", "D": "Spontaneous"}, "A", "Semi-conservative replication preserves one original parental strand while synthesizing one complementary new strand.", "Does each newly replicated DNA double helix contain one original strand and one newly synthesized strand?"),
            ("Ecology & Environment", "Biomes", "The terrestrial biome characterized by tall emergent trees, high humidity, canopy stratification, and high annual rainfall (>2000 mm) is the:", {"A": "Tropical Rainforest", "B": "Southern Guinea Savanna", "C": "Sahel Savanna", "D": "Montane Grassland"}, "A", "The Tropical Rainforest possesses multi-layered canopies and extraordinary biodiversity supported by year-round heat and moisture.", "Which Nigerian forest vegetation zone features emergent buttress-rooted trees and heavy year-round rainfall?"),
            ("Ecology & Environment", "Carbon Cycle", "Which biological process removes carbon dioxide from the atmosphere?", {"A": "Photosynthesis by green plants", "B": "Cellular respiration by animals", "C": "Combustion of fossil fuels", "D": "Decomposition by fungi"}, "A", "Photosynthesis captures atmospheric CO₂ to synthesize organic carbohydrates.", "What natural plant process acts as the primary carbon sink on Earth?"),
            ("Ecology & Environment", "Ecological Adaptation", "Xerophytic plants like cacti and acacia conserve water in arid environments by possessing:", {"A": "Sunken stomata, thick waxy cuticles, and reduced needle-like leaves", "B": "Broad leaves with numerous open stomata", "C": "Shallow adventitious root systems", "D": "Thin epidermal layers without cuticles"}, "A", "Xerophytes minimize transpirational water loss via reduced leaf surface area, sunken stomata, and waxy cuticles.", "How do desert plants modify their leaves and stomata to prevent dehydration?")
        ],
        "Economics": [
            ("Basic Economic Principles & Methodology", "Economic Systems", "Consumer sovereignty is a distinctive hallmark of which economic system?", {"A": "Free Market (Capitalist) Economy", "B": "Command (Socialist) Economy", "C": "Feudal Economy", "D": "Subsistence Economy"}, "A", "In a free market economy, consumer dollar votes directly determine what goods firms produce.", "In which economic system do consumer purchasing choices dictate production?"),
            ("Basic Economic Principles & Methodology", "Production Factors", "The reward accrued to the entrepreneur as a factor of production is:", {"A": "Profit", "B": "Wages", "C": "Interest", "D": "Rent"}, "A", "Land earns Rent, Labor earns Wages, Capital earns Interest, and Enterprise earns Profit.", "What factor reward compensates business owners for taking financial risks?"),
            ("Microeconomics & Price Mechanism", "Law of Diminishing Returns", "According to the Law of Diminishing Marginal Returns, as variable inputs are successively added to fixed inputs:", {"A": "Marginal product eventually declines", "B": "Total product immediately drops to zero", "C": "Average cost falls indefinitely", "D": "Fixed costs begin to increase"}, "A", "Adding variable factors to fixed factors causes marginal product (MP) to peak and then inevitably diminish.", "What happens to the additional output (MP) when you keep crowding workers onto a fixed acre of land?"),
            ("Microeconomics & Price Mechanism", "Market Structures", "A market structure characterized by a single seller, unique product with no close substitutes, and insurmountable barriers to entry is:", {"A": "A Pure Monopoly", "B": "Monopolistic Competition", "C": "An Oligopoly", "D": "Perfect Competition"}, "A", "A pure monopoly features a sole producer who acts as a price maker with complete market control.", "What do you call an industry dominated by only one single producer?"),
            ("Microeconomics & Price Mechanism", "Consumer Surplus", "Consumer surplus is mathematically defined as the difference between:", {"A": "The maximum price a consumer is willing to pay and the actual market price paid", "B": "Total revenue and total cost", "C": "Market price and marginal cost", "D": "Income and savings"}, "A", "Consumer surplus represents welfare benefit: Willingness to pay minus actual price paid.", "What economic term measures the extra benefit consumers get when they pay less than they were willing to?"),
            ("Macroeconomics & National Income", "Inflation Types", "Inflation triggered by rising wage rates, fuel prices, and imported raw material costs is classified as:", {"A": "Cost-Push Inflation", "B": "Demand-Pull Inflation", "C": "Hyperinflation", "D": "Structural Deflation"}, "A", "Cost-push inflation occurs when increased production costs shift the aggregate supply curve to the left.", "When the cost of producing goods rises across the whole country, what type of inflation occurs?"),
            ("Macroeconomics & National Income", "Circular Flow", "In the circular flow of income for an open four-sector economy, injections comprise:", {"A": "Investment + Government Spending + Exports (I + G + X)", "B": "Savings + Taxation + Imports (S + T + M)", "C": "Consumption + Imports", "D": "Taxation + Investment"}, "A", "Injections add expenditure into the circular flow (I + G + X); withdrawals remove funds (S + T + M).", "Which economic activities inject new spending into the national circular flow?"),
            ("Macroeconomics & National Income", "Fiscal Policy", "To stimulate an economy experiencing an economic recession and high unemployment, the government should adopt:", {"A": "Expansionary fiscal policy: increase spending and reduce taxes", "B": "Contractionary fiscal policy: increase taxes and cut spending", "C": "Increase the monetary policy rate to 30%", "D": "Ban all commercial bank lending"}, "A", "Expansionary fiscal policy boosts aggregate demand by injecting public spending and lowering personal income taxes.", "How can the government directly stimulate aggregate demand during a downturn?"),
            ("Money, Banking & Public Finance", "Money Functions", "Which function of money overcomes the difficulty of the 'double coincidence of wants' inherent in barter trade?", {"A": "Medium of exchange", "B": "Store of value", "C": "Unit of account", "D": "Standard of deferred payment"}, "A", "As a medium of exchange, money facilitates trade without requiring both parties to hold goods the other desires.", "What function of money allows you to buy goods without trading cows or grain?"),
            ("Money, Banking & Public Finance", "Tax Incidence", "A tax whose rate increases progressively as the taxable income of the taxpayer increases is called a:", {"A": "Progressive tax", "B": "Regressive tax", "C": "Proportional flat tax", "D": "Specific excise duty"}, "A", "Progressive taxes (such as PAYE income tax) tax higher income brackets at higher percentage rates.", "What tax system levies higher percentage rates on wealthier earners?"),
            ("Money, Banking & Public Finance", "Public Debt", "Debts owed by a sovereign government to international financial institutions and foreign creditors are classified as:", {"A": "External (Foreign) Debt", "B": "Internal (Domestic) Debt", "C": "Floating Debt", "D": "Funded Treasury Bonds"}, "A", "External debt comprises sovereign liabilities owed in foreign currency to foreign entities.", "What do you call public debt owed to foreign countries and international lenders?"),
            ("Microeconomics & Price Mechanism", "Price Ceilings", "An effective government price ceiling set below equilibrium typically generates:", {"A": "Persistent market shortages and informal black markets", "B": "A surplus of unsold goods", "C": "A fall in consumer quantity demanded", "D": "Higher corporate profits"}, "A", "When prices are capped artificially low, quantity demanded exceeds quantity supplied, creating shortages.", "What happens in a market when the maximum legal price is held below what sellers need to break even?")
        ],
        "Government": [
            ("Elements of Government & Political Theory", "Forms of Government", "A confederation differs fundamentally from a federation because in a confederation:", {"A": "The constituent member states retain their sovereign independence and right to secede", "B": "The central government possesses absolute supreme authority over regions", "C": "There is a strong unified national constitution and single currency", "D": "Power is fused into a single unitary parliament"}, "A", "A confederation is a loose alliance of independent states where sovereignty resides strictly with the components.", "In which union do the regional states retain complete sovereignty and the freedom to break away?"),
            ("Elements of Government & Political Theory", "Judicial Review", "The power of the judiciary to declare acts of the legislature or executive unconstitutional and null and void is called:", {"A": "Judicial Review", "B": "Judicial Precedent", "C": "Habeas Corpus", "D": "Court Injunction"}, "A", "Judicial Review was established in Marbury v. Madison (1803), empowering courts to invalidate unconstitutional legislation.", "What judicial power allows courts to strike down illegal government laws?"),
            ("Elements of Government & Political Theory", "Electoral Systems", "An electoral system where the candidate who secures the highest number of votes in a single-member constituency wins, regardless of absolute majority, is:", {"A": "First-Past-The-Post (Simple Plurality)", "B": "Proportional Representation", "C": "Alternative Vote", "D": "Second Ballot Runoff"}, "A", "First-past-the-post awards victory to the plurality leader without requiring a 50% + 1 majority.", "What electoral system declares the candidate with the most individual votes as the winner?"),
            ("Colonial Administration in Nigeria & West Africa", "Chartered Company Rule", "Before the British government established formal direct protectorate rule in 1900, Nigeria's commercial territories were administered by:", {"A": "The Royal Niger Company under Sir George Goldie", "B": "The British East India Company", "C": "The United Africa Company under Lord Lugard", "D": "The Dutch West India Company"}, "A", "The Royal Niger Company received a royal charter in 1886 to govern and monopolize trade along the Niger River basin.", "Which chartered commercial company ruled the Niger basin before the 1900 colonial takeover?"),
            ("Colonial Administration in Nigeria & West Africa", "French Colonial System", "Under the French colonial policy of Assimilation, African inhabitants of the Four Communes were classified as:", {"A": "French Citizens (Citoyens)", "B": "Colonial Subjects (Sujets)", "C": "Indentured Laborers", "D": "Protectorate Natives"}, "A", "Residents of the Four Communes of Senegal were granted full French citizenship and representation in Paris.", "What legal status did the French bestow upon Africans living in the Four Communes under assimilation?"),
            ("Nigerian Constitutional Development", "1963 Republican Constitution", "The landmark achievement of the 1963 Nigerian Republican Constitution was:", {"A": "Replacing the British Queen with an elected Nigerian President and abolishing Privy Council appeals", "B": "Granting universal adult suffrage to Northern women", "C": "Introducing regional premiers for the first time", "D": "Establishing the Clifford elective principle"}, "A", "The 1963 Constitution severed ties with the British monarchy and made the Nigerian Supreme Court the highest court of appeal.", "What did the 1963 Republican Constitution do to the position of Queen Elizabeth II in Nigeria?"),
            ("Nigerian Constitutional Development", "1979 Constitution", "The 1979 Constitution of the Second Republic marked a historic departure from Nigerian constitutional tradition by adopting:", {"A": "An American-style Executive Presidential system in place of the British Westminster Parliamentary model", "B": "A unitary system of government under a military dictator", "C": "A diarchy shared between soldiers and civilians", "D": "A ceremonial prime ministerial cabinet"}, "A", "The 1979 Constitution introduced an executive president with nationwide mandate and clear separation of powers.", "Which foreign system of government did Nigeria adopt when returning to civilian rule in 1979?"),
            ("Federalism, Military Rule & Foreign Policy", "ECOWAS Founding", "The Economic Community of West African States (ECOWAS) was formally established under the Treaty of Lagos in 1975 through the joint leadership of:", {"A": "General Yakubu Gowon of Nigeria and President Gnassingbé Eyadéma of Togo", "B": "Dr. Kwame Nkrumah of Ghana and General Murtala Mohammed", "C": "General Olusegun Obasanjo and President Léopold Senghor", "D": "Sir Abubakar Tafawa Balewa and Félix Houphouët-Boigny"}, "A", "General Yakubu Gowon and President Eyadéma championed the diplomatic creation of ECOWAS, signed on May 28, 1975.", "Which two West African heads of state championed the founding of ECOWAS in Lagos?"),
            ("Federalism, Military Rule & Foreign Policy", "Ouster Clauses", "Military regimes in Nigeria used 'ouster clauses' in their decrees specifically to:", {"A": "Prevent regular courts from entertaining legal challenges against military decrees", "B": "Expel foreign diplomats from the country", "C": "Dismiss civilian civil servants without pension", "D": "Abolish the National Youth Service Corps"}, "A", "Ouster clauses stripped the judiciary of jurisdiction to question the validity of military decrees.", "Why did military rulers insert ouster clauses into their decrees?"),
            ("Federalism, Military Rule & Foreign Policy", "Non-Aligned Movement", "During the Cold War, Nigeria's foreign policy of non-alignment meant that Nigeria:", {"A": "Refused to formally align with either the Western capitalist bloc (USA) or Eastern communist bloc (USSR)", "B": "Refused to trade with any European or Asian nation", "C": "Banned all foreign private investment in the oil sector", "D": "Refused to join the United Nations Organization"}, "A", "The Non-Aligned Movement allowed newly independent states to pursue independent foreign policy without subservience to superpowers.", "What was the purpose of non-alignment during the Cold War?"),
            ("Elements of Government & Political Theory", "Citizenship Acquisition", "In modern constitutional law, citizenship acquired automatically by virtue of being born within the territorial borders of a country is called:", {"A": "Jus soli (Right of the soil)", "B": "Jus sanguinis (Right of blood)", "C": "Naturalization", "D": "Honorary conferment"}, "A", "Jus soli grants citizenship based on territorial birth; Jus sanguinis grants it based on parental lineage.", "What is the legal Latin term for citizenship granted by place of birth?"),
            ("Elements of Government & Political Theory", "Pressure Groups", "An association of individuals who unite to influence government policies in favor of their members without seeking political office is:", {"A": "A Pressure Group (Interest Group)", "B": "A Political Party", "C": "An Electoral Commission", "D": "A Militia Council"}, "A", "Pressure groups seek to influence public policy decisions without contesting elections to govern.", "What organization lobbies to influence legislation without actually contesting elections?")
        ],
        "Literature in English": [
            ("Literary Appreciation & Devices", "Paradox vs Oxymoron", "The literary statement 'The child is father of the man' (William Wordsworth) is an example of:", {"A": "Paradox", "B": "Oxymoron", "C": "Hyperbole", "D": "Euphemism"}, "A", "A paradox appears contradictory on the surface but conveys a profound philosophical truth.", "Is a statement that seems contradictory at first glance but reveals a deeper truth a paradox or an oxymoron?"),
            ("Literary Appreciation & Devices", "Irony", "In literature, when an event occurs that is the exact reverse of what the characters and readers logically expected, it is termed:", {"A": "Situational Irony", "B": "Dramatic Irony", "C": "Verbal Irony", "D": "Sarcasm"}, "A", "Situational irony occurs when the actual outcome conflicts sharply with reasonable expectations.", "What type of irony occurs when the actual result directly contradicts expectations?"),
            ("Literary Appreciation & Devices", "Figures of Association", "The poetic line 'Uneasy lies the head that wears a crown' uses which figure of speech?", {"A": "Synecdoche and Metonymy", "B": "Simile and Personification", "C": "Hyperbole and Litotes", "D": "Onomatopoeia"}, "A", "'Head' represents the king (synecdoche) and 'crown' represents sovereign royal office (metonymy).", "Which figures use part for whole and symbol for authority?"),
            ("Drama & Theatrical Techniques", "Classical Tragedy Conventions", "In classical Aristotelian drama, the emotional purging or release of pity and fear experienced by the audience is known as:", {"A": "Catharsis", "B": "Hamartia", "C": "Hubris", "D": "Nemesis"}, "A", "Catharsis is the emotional cleansing achieved when watching the tragic downfall of a great protagonist.", "What Greek term denotes the purging of emotions at the end of a tragedy?"),
            ("Drama & Theatrical Techniques", "Soyinka's The Lion and the Jewel", "In 'The Lion and the Jewel', Lakunle is depicted as a comic figure primarily because:", {"A": "He superficially mimics European customs while completely misunderstanding his own African culture", "B": "He is illiterate and unable to speak English", "C": "He is an old man pretending to be a youthful lover", "D": "He is an undercover British colonial soldier"}, "A", "Soyinka satirizes Lakunle's pompous, pretentious mimicry of Western habits and romantic clichés.", "Why does Lakunle appear ridiculous to Sidi and the village elders?"),
            ("Drama & Theatrical Techniques", "Osofisan's Women of Owu", "In Femi Osofisan's 'Women of Owu', the central thematic critique focuses on:", {"A": "The horrific human cost of war and the devastation inflicted upon women and children by male political ambition", "B": "The introduction of modern technology into ancient Yoruba kingdoms", "C": "The commercial rivalry between slave traders along the coast", "D": "The celebration of heroic military conquests"}, "A", "Osofisan adapts Euripides to condemn senseless imperial warfare and elevate female tragedy and resilience.", "What does Femi Osofisan highlight concerning the victims of the Owu war?"),
            ("Poetry & Versification", "Metrical Forms", "A line of poetry consisting of five metrical feet, where each foot contains an unstressed syllable followed by a stressed syllable, is:", {"A": "Iambic Pentameter", "B": "Trochaic Tetrameter", "C": "Anapestic Hexameter", "D": "Dactylic Trimeter"}, "A", "Iambic pentameter consists of five iambs (da-DUM da-DUM da-DUM da-DUM da-DUM), totaling 10 syllables.", "What meter contains five pairs of unstressed-stressed syllables?"),
            ("Poetry & Versification", "Enjambment", "When a poetic thought or phrase runs over from one line into the next without terminal punctuation, the technique is called:", {"A": "Enjambment (Run-on line)", "B": "End-stopping", "C": "Caesura", "D": "Alliteration"}, "A", "Enjambment carries a sentence across line boundaries to build momentum or mimic continuous motion.", "What is the term for a line of poetry that flows into the next without ending punctuation?"),
            ("Poetry & Versification", "Shakespearean Sonnet", "The rhyme scheme of a standard Shakespearean (English) sonnet is:", {"A": "ABAB CDCD EFEF GG", "B": "ABBA ABBA CDE CDE", "C": "AABB CCDD EEFF GG", "D": "ABAB BCBC CDCD EE"}, "A", "Shakespearean sonnets comprise three quatrains and a rhyming couplet: abab cdcd efef gg.", "What is the rhyme scheme of a sonnet ending in a rhyming couplet gg?"),
            ("Prose & Fictional Techniques", "Things Fall Apart Analysis", "In Chinua Achebe's 'Things Fall Apart', why does Okonkwo take a direct part in the killing of Ikemefuna?", {"A": "He is terrified of being perceived as weak or fearful by his clan peers", "B": "The Oracle specifically commanded him to deliver the death blow personally", "C": "He suspected Ikemefuna was plotting to assassinate Nwoye", "D": "Ikemefuna stole sacred yams from his barn"}, "A", "Achebe states explicitly: 'Dazed with fear, Okonkwo drew his matchet and cut him down. He was afraid of being thought weak.'", "What internal insecurity drove Okonkwo to strike down the boy who called him father?"),
            ("Prose & Fictional Techniques", "The Joys of Motherhood Analysis", "In Buchi Emecheta's 'The Joys of Motherhood', the protagonist Nnu Ego's life ends:", {"A": "In poverty and loneliness by the roadside, neglected by the children for whom she sacrificed everything", "B": "In luxury surrounded by grandchildren in a royal estate", "C": "As a prominent female politician in colonial Lagos", "D": "In a peaceful retirement with her husband Nnaife"}, "A", "The novel's tragic irony culminates in Nnu Ego dying alone by a dusty roadside, critiquing traditional patriarchal mother worship.", "How does Nnu Ego's tragic end critique traditional expectations of motherhood?"),
            ("Prose & Fictional Techniques", "Narrative Technique", "When a story is narrated by a voice that knows all characters' thoughts, feelings, past events, and future outcomes, the point of view is:", {"A": "Third-Person Omniscient", "B": "First-Person Participant", "C": "Third-Person Limited", "D": "Second-Person Dramatic"}, "A", "An omniscient narrator has unrestricted, god-like access to all characters' consciousness and actions.", "What narrative perspective has all-knowing access to all characters in a story?")
        ]
    }

    # Populate questions up to 35 for each subject
    sub_prefix = {
        "Use of English": "eng",
        "Mathematics": "mth",
        "Physics": "phy",
        "Chemistry": "chm",
        "Biology": "bio",
        "Economics": "eco",
        "Government": "gov",
        "Literature in English": "lit"
    }

    for subj, target in subject_targets.items():
        prefix = sub_prefix[subj]
        existing_sub = [q for q in questions_by_id.values() if q["subject"] == subj]
        existing_nums = set()
        existing_texts = set()
        for q in existing_sub:
            existing_texts.add(q["question"])
            if q["id"].startswith(f"{prefix}_"):
                try:
                    num = int(q["id"].split("_")[1])
                    existing_nums.add(num)
                except ValueError:
                    pass

        all_bp = blueprints.get(subj, []) + extra_blueprints.get(subj, [])
        fresh_bp = [bp for bp in all_bp if bp[2] not in existing_texts]
        
        current_count = len(existing_sub)
        print(f"{subj}: current {current_count}, target {target}, fresh blueprints {len(fresh_bp)}")

        bp_idx = 0
        next_num = 1

        while bp_idx < len(fresh_bp):
            while next_num in existing_nums:
                next_num += 1
            new_id = f"{prefix}_{next_num:03d}"
            existing_nums.add(next_num)

            top, subtop, q_text, opts, orig_correct, trap_explanation, socratic_text = fresh_bp[bp_idx]
            bp_idx += 1

            # Rotate correct option across A, B, C, D to ensure natural exam balance
            target_slot = ["A", "B", "C", "D"][next_num % 4]
            shuffled_opts = dict(opts)
            if target_slot != orig_correct:
                correct_text = shuffled_opts[orig_correct]
                displaced_text = shuffled_opts[target_slot]
                shuffled_opts[target_slot] = correct_text
                shuffled_opts[orig_correct] = displaced_text

            # Build traps dictionary for wrong options
            traps = {}
            for opt_key in ["A", "B", "C", "D"]:
                if opt_key != target_slot:
                    traps[opt_key] = f"You selected option {opt_key}. {trap_explanation}"

            new_q = {
                "id": new_id,
                "subject": subj,
                "topic": top,
                "subtopic": subtop,
                "year": random.choice([2021, 2022, 2023, 2024]),
                "question": q_text,
                "options": shuffled_opts,
                "correct_option": target_slot,
                "traps": traps,
                "pedagogical_concept": trap_explanation,
                "socratic_prompt": socratic_text
            }
            questions_by_id[new_id] = new_q
            current_count += 1

    final_questions = list(questions_by_id.values())
    # Sort nicely by id
    final_questions.sort(key=lambda x: (x["subject"], x["id"]))

    with open("data/questions.json", "w", encoding="utf-8") as f:
        json.dump(final_questions, f, indent=2, ensure_ascii=False)

    print(f"\n🎉 Successfully wrote {len(final_questions)} questions to data/questions.json!")
    by_s = {}
    for q in final_questions:
        by_s[q["subject"]] = by_s.get(q["subject"], 0) + 1
    for s, c in by_s.items():
        print(f"  • {s:25}: {c} questions")

if __name__ == "__main__":
    create_mega_bank()
