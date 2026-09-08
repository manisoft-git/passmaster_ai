import json

QUESTIONS_PATH = "data/questions.json"

with open(QUESTIONS_PATH, "r", encoding="utf-8") as f:
    questions = json.load(f)

existing_ids = {q["id"] for q in questions}

new_batch = [
    # --- USE OF ENGLISH ---
    {
        "id": "eng_005",
        "subject": "Use of English",
        "topic": "Concord & Grammar",
        "subtopic": "Relative Clause Agreement",
        "year": 2023,
        "question": "He is one of the brilliant students who _______ awarded national scholarships last semester.",
        "options": {
            "A": "was",
            "B": "were",
            "C": "is",
            "D": "has been"
        },
        "correct_option": "B",
        "traps": {
            "A": "You focused on 'He is one' (singular). But the relative pronoun 'who' refers to the antecedent plural noun 'the brilliant students'. Therefore, the relative clause requires plural 'were'!",
            "C": "You chose singular present tense. The time indicator 'last semester' requires past tense.",
            "D": "'Has been' is singular and present perfect, missing both the plural requirement and the past event marker."
        },
        "pedagogical_concept": "Relative Pronoun Concord with 'One of the [Plural Noun] Who': When 'one of the + plural noun' is followed by a relative pronoun (who, which, that), the verb in the relative clause agrees with the plural noun antecedent ('students who were'), unless preceded by 'the only one'.",
        "socratic_prompt": "Who was awarded the scholarships? Was it only him, or was he among a group of brilliant students who were awarded?"
    },
    {
        "id": "eng_006",
        "subject": "Use of English",
        "topic": "Oral Forms & Phonology",
        "subtopic": "Word Stress Patterns",
        "year": 2024,
        "question": "Which syllable receives the primary stress in the word 'PHOTOGRAPHY'?",
        "options": {
            "A": "First syllable: PHO-to-gra-phy",
            "B": "Second syllable: pho-TO-gra-phy",
            "C": "Third syllable: pho-to-GRA-phy",
            "D": "Fourth syllable: pho-to-gra-PHY"
        },
        "correct_option": "B",
        "traps": {
            "A": "You confused photography with the base noun 'PHOtograph' where stress is on the 1st syllable. Adding suffix '-y' shifts stress to the antepenultimate (3rd from end) syllable.",
            "C": "You placed stress on 'gra', which is typical of words ending in '-ic' (e.g. photoGRAPHic), not '-graphy'.",
            "D": "English polysyllabic words ending in '-y' almost never place primary stress on the final weak vowel."
        },
        "pedagogical_concept": "Stress Shift with Suffixes: In English, words ending in '-graphy', '-logy', and '-meter' take primary stress on the antepenultimate syllable (third syllable from the end): pho-TO-gra-phy, bi-O-lo-gy, ther-MO-me-ter.",
        "socratic_prompt": "Say the word naturally aloud: do you say PHO-tograph or pho-TO-graphy? Where is the highest vocal pitch and energy placed?"
    },
    {
        "id": "eng_007",
        "subject": "Use of English",
        "topic": "Comprehension & Prescribed Text",
        "subtopic": "The Life Changer Themes",
        "year": 2023,
        "question": "In Khadija Abubakar Jalli's 'The Life Changer', what did Salma's initial attitude toward university dress codes reflect before her encounter with the disciplinary panel?",
        "options": {
            "A": "Profound adherence to conservative cultural norms",
            "B": "Rebellious defiance and sophisticated pretension",
            "C": "Complete ignorance of the university handbook guidelines",
            "D": "Fear of intimidation by campus cult groups"
        },
        "correct_option": "B",
        "traps": {
            "A": "Salma actively mocked conservative dress and dressed in revealing, flashy western attire upon arriving on campus.",
            "C": "Salma was fully aware of the dress rules but consciously chose to disregard them to assert modern sophistication.",
            "D": "Cult groups did not intimidate Salma; her downfall began with arrogance and academic malpractice."
        },
        "pedagogical_concept": "Character Arc in 'The Life Changer': Salma represents the trap of campus arrogance, false pride, and rebellion against established norms before facing the humbling reality of disciplinary sanction and personal redemption.",
        "socratic_prompt": "Recall how Salma treated her roommates and how she dressed during her registration. Was she timid or boastful and defiant?"
    },

    # --- MATHEMATICS ---
    {
        "id": "mth_004",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Logarithms & Indices",
        "year": 2023,
        "question": "If log₁₀(x) + 2 log₁₀(3) = 1, find the value of x.",
        "options": {
            "A": "10/9",
            "B": "9/10",
            "C": "1/9",
            "D": "5/9"
        },
        "correct_option": "A",
        "traps": {
            "A": None,
            "B": "You inverted the quotient: x = 9 / 10 instead of 10 / 9.",
            "C": "You set log₁₀(9x) = 0 instead of 1, yielding 9x = 1 -> x = 1/9.",
            "D": "You treated 2 log₁₀(3) as log₁₀(6) instead of log₁₀(3²) = log₁₀(9), getting 6x = 10 -> x = 5/3."
        },
        "pedagogical_concept": "Logarithm Power & Product Laws: 2 log₁₀(3) = log₁₀(3²) = log₁₀(9). Thus: log₁₀(x) + log₁₀(9) = log₁₀(9x) = 1. In exponential form: 9x = 10¹ = 10, so x = 10/9.",
        "socratic_prompt": "What does the power rule of logarithms do to the coefficient 2 in front of log₁₀(3)? What is 3²? Then combine the sum into a single product!"
    },
    {
        "id": "mth_005",
        "subject": "Mathematics",
        "topic": "Geometry & Trigonometry",
        "subtopic": "Coordinate Geometry",
        "year": 2024,
        "question": "Find the equation of the line perpendicular to 2x - 3y + 6 = 0 which passes through the point (2, -1).",
        "options": {
            "A": "3x + 2y - 4 = 0",
            "B": "2x - 3y - 7 = 0",
            "C": "3x + 2y + 4 = 0",
            "D": "-3x + 2y - 8 = 0"
        },
        "correct_option": "A",
        "traps": {
            "B": "You used the PARALLEL slope (m = 2/3) instead of the negative reciprocal perpendicular slope (m = -3/2).",
            "C": "You made a sign error when expanding y - (-1) = -3/2(x - 2): 2(y + 1) = -3x + 6 -> 3x + 2y - 4 = 0, not +4.",
            "D": "You inverted the signs incorrectly."
        },
        "pedagogical_concept": "Perpendicular Lines Slope Rule: If line L₁ has slope m₁, the perpendicular line L₂ has slope m₂ = -1/m₁. Line 2x - 3y + 6 = 0 has slope m₁ = 2/3. Therefore, m₂ = -3/2. Equation: y - (-1) = -3/2 (x - 2) => 2y + 2 = -3x + 6 => 3x + 2y - 4 = 0.",
        "socratic_prompt": "What is the slope of the given line 2x - 3y + 6 = 0? For two lines to be perpendicular, what is the product of their slopes (m₁ * m₂)?"
    },
    {
        "id": "mth_006",
        "subject": "Mathematics",
        "topic": "Statistics & Probability",
        "subtopic": "Independent vs Dependent Events",
        "year": 2023,
        "question": "A bag contains 5 red balls and 3 green balls. Two balls are drawn one after the other WITHOUT replacement. What is the probability that both balls are red?",
        "options": {
            "A": "25/64",
            "B": "5/14",
            "C": "15/56",
            "D": "10/28"
        },
        "correct_option": "B",
        "traps": {
            "A": "You calculated WITH replacement: (5/8) * (5/8) = 25/64. The problem explicitly states WITHOUT replacement!",
            "C": "15/56 is the probability of drawing one red AND one green (5/8 * 3/7), not two red balls.",
            "D": "10/28 reduces to 5/14, but B is already in lowest standard fraction form."
        },
        "pedagogical_concept": "Conditional Probability without Replacement: First draw P(R₁) = 5/8. After removing one red ball, 4 red balls and 7 total balls remain. Second draw P(R₂|R₁) = 4/7. P(both red) = (5/8) * (4/7) = 20/56 = 5/14.",
        "socratic_prompt": "After you draw the first red ball without returning it, how many red balls are left in the bag? How many total balls are left?"
    },

    # --- PHYSICS ---
    {
        "id": "phy_005",
        "subject": "Physics",
        "topic": "Electricity & Magnetism",
        "subtopic": "Ohms Law & Resistivity",
        "year": 2024,
        "question": "A cell of EMF 2.0 V and internal resistance 0.5 Ω is connected to an external resistor of 3.5 Ω. Calculate the terminal potential difference across the cell.",
        "options": {
            "A": "2.00 V",
            "B": "1.75 V",
            "C": "0.25 V",
            "D": "1.50 V"
        },
        "correct_option": "B",
        "traps": {
            "A": "2.00 V is the open-circuit EMF. In a closed circuit, lost volts across the internal resistance reduce terminal voltage!",
            "C": "0.25 V is the lost voltage inside the cell (v = I * r = 0.5 * 0.5 = 0.25 V), not the external terminal potential difference.",
            "D": "You subtracted 0.5 from 2.0 directly without calculating circuit current first."
        },
        "pedagogical_concept": "EMF and Internal Resistance: Total resistance R_total = R + r = 3.5 + 0.5 = 4.0 Ω. Circuit current I = E / R_total = 2.0 / 4.0 = 0.5 A. Terminal p.d. V = I * R = 0.5 * 3.5 = 1.75 V (or V = E - Ir = 2.0 - 0.25 = 1.75 V).",
        "socratic_prompt": "What is the total resistance of the circuit including internal resistance? Once you calculate current I = E / (R + r), what voltage drops across the external load R?"
    },
    {
        "id": "phy_006",
        "subject": "Physics",
        "topic": "Thermal Physics",
        "subtopic": "Heat Capacity & Latent Heat",
        "year": 2023,
        "question": "How much heat energy is required to completely melt 200 g of pure ice at 0°C to water at 0°C? (Specific latent heat of fusion of ice = 3.36 × 10⁵ J/kg)",
        "options": {
            "A": "6.72 × 10⁴ J",
            "B": "6.72 × 10⁷ J",
            "C": "1.68 × 10⁵ J",
            "D": "3.36 × 10⁴ J"
        },
        "correct_option": "A",
        "traps": {
            "B": "You used mass in grams (200) without converting to SI kilograms: 200 * 3.36 × 10⁵ = 6.72 × 10⁷ J. In physics, mass MUST be in kg!",
            "C": "You divided by 2 instead of multiplying by mass in kg (0.2 kg).",
            "D": "You used 100 g instead of 200 g."
        },
        "pedagogical_concept": "Latent Heat of Phase Change: Q = m * L_f. Mass must be in kilograms: m = 200 g = 0.2 kg. Q = 0.2 kg × (3.36 × 10⁵ J/kg) = 6.72 × 10⁴ J (67.2 kJ). Temperature does not change during phase transition.",
        "socratic_prompt": "What is 200 grams expressed in standard SI kilograms? During melting at 0°C, do you use Q = mcΔθ or Q = mL?"
    },

    # --- CHEMISTRY ---
    {
        "id": "chm_004",
        "subject": "Chemistry",
        "topic": "Organic Chemistry",
        "subtopic": "Hydrocarbons & IUPAC",
        "year": 2024,
        "question": "What is the correct IUPAC systematic name for the compound CH₃-CH(CH₃)-CH₂-CH=CH₂?",
        "options": {
            "A": "4-methylpent-1-ene",
            "B": "2-methylpent-4-ene",
            "C": "4-methylpent-2-ene",
            "D": "isohexane"
        },
        "correct_option": "A",
        "traps": {
            "B": "You numbered from the methyl branch end instead of the double bond. IUPAC rules state double bonds have higher priority and MUST receive the lowest possible locant number!",
            "C": "The double bond is between carbon 1 and 2, not 2 and 3.",
            "D": "Isohexane is an informal trivial name, not the systematic IUPAC nomenclature."
        },
        "pedagogical_concept": "IUPAC Priority Rules for Alkenes: The principal functional group (the double bond) takes precedence over alkyl substituents. Number the 5-carbon chain from the end closest to the alkene: C1=C2-C3-C4(CH3)-C5. The methyl group is at C4, giving 4-methylpent-1-ene.",
        "socratic_prompt": "Which end of the carbon chain must you start numbering from: the double bond end or the alkyl branch end?"
    },
    {
        "id": "chm_005",
        "subject": "Chemistry",
        "topic": "Inorganic Chemistry",
        "subtopic": "Periodic Table Trends",
        "year": 2023,
        "question": "Why does Nitrogen (atomic number 7) have a HIGHER first ionization energy than Oxygen (atomic number 8), contrary to the general across-period trend?",
        "options": {
            "A": "Oxygen has a larger nuclear charge than Nitrogen",
            "B": "Nitrogen possesses a stable half-filled 2p³ subshell",
            "C": "Nitrogen is more electronegative than Oxygen",
            "D": "Oxygen has fewer electron energy levels than Nitrogen"
        },
        "correct_option": "B",
        "traps": {
            "A": "Oxygen does have a larger nuclear charge (Z=8 vs Z=7), which is why students expect Oxygen to be higher, making this an anomaly!",
            "C": "Oxygen is MORE electronegative than Nitrogen (3.44 vs 3.04), not less.",
            "D": "Both Nitrogen and Oxygen are in Period 2 and possess exactly two electron shells."
        },
        "pedagogical_concept": "Half-Filled Subshell Stability: Nitrogen has electronic configuration 1s² 2s² 2p³, where the three 2p orbitals are each singly occupied (half-filled), providing extra quantum exchange stability. In Oxygen (2p⁴), paired electrons in the same orbital experience inter-electronic repulsion, requiring less energy to remove.",
        "socratic_prompt": "Draw the orbital diagram for Nitrogen's 2p electrons vs Oxygen's 2p electrons. Which orbital contains paired electrons experiencing electron-electron repulsion?"
    },

    # --- BIOLOGY ---
    {
        "id": "bio_004",
        "subject": "Biology",
        "topic": "Physiology & Systems",
        "subtopic": "Excretion & Kidneys",
        "year": 2024,
        "question": "In the mammalian kidney nephron, in which region does selective reabsorption of ALL glucose and amino acids normally take place?",
        "options": {
            "A": "Bowman's capsule",
            "B": "Proximal convoluted tubule (PCT)",
            "C": "Loop of Henle",
            "D": "Collecting duct"
        },
        "correct_option": "B",
        "traps": {
            "A": "Bowman's capsule is the site of non-selective ultrafiltration under high hydrostatic pressure, not reabsorption.",
            "C": "The Loop of Henle is responsible for osmoregulation and establishing a sodium concentration gradient in the medulla.",
            "D": "The collecting duct reabsorbs water under the influence of ADH (antidiuretic hormone)."
        },
        "pedagogical_concept": "Nephron Physiology: Ultrafiltration occurs at the glomerulus into Bowman's capsule. Active selective reabsorption of 100% of vital nutrients (glucose, amino acids, vitamins) occurs in the Proximal Convoluted Tubule (PCT), lined with microvilli and dense mitochondria.",
        "socratic_prompt": "Which part of the renal tubule is covered with microvilli and rich in mitochondria to actively pump all glucose back into the surrounding capillaries?"
    },
    {
        "id": "bio_005",
        "subject": "Biology",
        "topic": "Ecology",
        "subtopic": "Trophic Levels & Food Chains",
        "year": 2023,
        "question": "According to Lindeman's Ten Percent Law of trophic efficiency, what percentage of chemical energy is typically transferred from one trophic level to the next higher level?",
        "options": {
            "A": "90%",
            "B": "50%",
            "C": "10%",
            "D": "1%"
        },
        "correct_option": "C",
        "traps": {
            "A": "90% is the energy LOST as metabolic heat, respiration, and unconsumed waste at each trophic stage!",
            "B": "50% is far too high; energy dissipation prevents long food chains in nature.",
            "D": "1% is approximately the fraction of incoming solar radiation captured by primary producers during photosynthesis, not trophic transfer."
        },
        "pedagogical_concept": "Lindeman's 10% Ecological Efficiency: Only about 10% of the energy stored as biomass in one trophic level is converted into biomass at the next level. The remaining 90% is expended in cellular respiration, bodily maintenance, heat, and excretory waste.",
        "socratic_prompt": "Do food chains usually have 10 or more links, or only 3 to 4? Why does available energy diminish so rapidly between herbivores and carnivores?"
    },

    # --- ECONOMICS ---
    {
        "id": "eco_005",
        "subject": "Economics",
        "topic": "Price Theory & Elasticity",
        "subtopic": "Price Ceiling & Floors",
        "year": 2024,
        "question": "When the government imposes an effective maximum price (Price Ceiling) below the market equilibrium price to protect consumers, the immediate economic consequence is _______.",
        "options": {
            "A": "an excess supply (glut) of the commodity",
            "B": "an excess demand (shortage) leading to hoarding and black markets",
            "C": "an automatic expansion in domestic production",
            "D": "a rise in producer profit margins"
        },
        "correct_option": "B",
        "traps": {
            "A": "Excess supply occurs when a minimum price (Price Floor) is set ABOVE equilibrium, such as minimum wage legislation.",
            "C": "Suppliers produce LESS at the lower capped price, while consumers demand MORE, triggering shortages.",
            "D": "Producers receive a lower price per unit and reduce output, diminishing profits."
        },
        "pedagogical_concept": "Price Ceilings vs Price Floors: A price ceiling legally caps prices BELOW equilibrium. Quantity demanded (Qd) exceeds quantity supplied (Qs), resulting in chronic shortages, queuing, rationing, and informal black market trading.",
        "socratic_prompt": "If the government forces landlords or traders to sell far below market rate, will sellers supply more goods or withhold goods from the market?"
    },
    {
        "id": "eco_006",
        "subject": "Economics",
        "topic": "National Income & Macroeconomics",
        "subtopic": "Inflation Causes & Control",
        "year": 2023,
        "question": "Cost-push inflation in an economy is typically triggered by which of the following events?",
        "options": {
            "A": "An increase in consumer disposable income from tax cuts",
            "B": "A sharp rise in fuel pump prices, electricity tariffs, and imported raw materials",
            "C": "Excessive growth in broad money supply (M2) by the Central Bank",
            "D": "Surplus agricultural harvest causing food gluts"
        },
        "correct_option": "B",
        "traps": {
            "A": "Increased consumer income increases aggregate demand, driving Demand-Pull inflation, not Cost-Push.",
            "C": "Monetary expansion is the primary driver of demand-side monetary inflation.",
            "D": "Food gluts cause prices to fall (deflationary pressure), not rise."
        },
        "pedagogical_concept": "Cost-Push Inflation: Occurs when aggregate supply shifts leftward due to sudden increases in costs of key factors of production (wages, fuel, electricity, transport, import duties), forcing firms to hike prices to maintain solvency.",
        "socratic_prompt": "When petrol subsidy is removed and transport fares triple across Nigeria, why do food prices rise even if consumer demand hasn't increased?"
    },

    # --- GOVERNMENT ---
    {
        "id": "gov_005",
        "subject": "Government",
        "topic": "Constitutional Development in Nigeria",
        "subtopic": "1999 Constitution Provisions",
        "year": 2024,
        "question": "Under the Exclusive Legislative List of the 1999 Nigerian Constitution, which of the following subjects can ONLY be legislated upon by the Federal National Assembly?",
        "options": {
            "A": "Health services and state universities",
            "B": "Defense, currency, foreign affairs, and maritime shipping",
            "C": "Secondary education and local agricultural development",
            "D": "Collection of tenement rates and market stall licenses"
        },
        "correct_option": "B",
        "traps": {
            "A": "Health and higher education are on the Concurrent Legislative List, where both Federal and State governments can make laws.",
            "C": "Secondary education is concurrent; local agriculture is residual/local government jurisdiction.",
            "D": "Tenement rates and market licenses belong exclusively to Local Government Councils under the Fourth Schedule."
        },
        "pedagogical_concept": "Division of Powers in Federalism: The Exclusive List contains 68 items reserved strictly for the Federal Government (Defense, Armed Forces, Currency/Coinage, External Affairs, Customs). The Concurrent List allows both Federal and State jurisdiction.",
        "socratic_prompt": "Can a State Governor establish their own military force or print their own state currency? Why are national security and money reserved exclusively for the Federal Government?"
    },
    {
        "id": "gov_006",
        "subject": "Government",
        "topic": "Basic Concepts in Political Science",
        "subtopic": "Separation of Powers",
        "year": 2023,
        "question": "Baron de Montesquieu formulated the doctrine of the Separation of Powers primarily to _______.",
        "options": {
            "A": "speed up legislative bill passage without parliamentary debates",
            "B": "prevent tyranny and safeguard citizens' political liberties by distributing governmental functions across distinct organs",
            "C": "enable the judiciary to dictate national economic policies to the executive",
            "D": "subordinate local governments to centralized military control"
        },
        "correct_option": "B",
        "traps": {
            "A": "Separation of powers often slows legislation down due to deliberate checks and balances.",
            "C": "The judiciary does not dictate economic policy; its role is interpreting the constitution and statute laws.",
            "D": "Montesquieu was an ardent opponent of centralized military autocracy."
        },
        "pedagogical_concept": "Montesquieu's Separation of Powers (1748): In 'The Spirit of the Laws', Montesquieu argued that concentrating executive, legislative, and judicial powers in one person or body results in tyranny. Liberty exists only when power checks power.",
        "socratic_prompt": "What happens when the person making the laws is also the sole prosecutor and the judge who delivers the sentence? What does dividing these roles prevent?"
    },

    # --- LITERATURE IN ENGLISH ---
    {
        "id": "lit_003",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Tone, Mood & Atmosphere",
        "year": 2024,
        "question": "What is the critical distinction between 'Tone' and 'Mood' in literary analysis?",
        "options": {
            "A": "Tone refers to the reader's emotional feeling; Mood refers to the author's personal attitude toward the subject",
            "B": "Tone reflects the writer or speaker's attitude toward the subject matter; Mood describes the atmosphere and emotional feeling evoked within the reader",
            "C": "Tone is exclusively used in drama; Mood is exclusively used in poetry",
            "D": "Tone and Mood are identical terms with zero analytical difference"
        },
        "correct_option": "B",
        "traps": {
            "A": "You inverted Tone and Mood! Tone is the WRITER's voice and attitude; Mood is the READER's emotional response.",
            "C": "Both devices are foundational elements across poetry, prose fiction, and dramatic plays.",
            "D": "Conflating Tone and Mood is one of the most penalizing mistakes on the JAMB Literature paper."
        },
        "pedagogical_concept": "Tone vs Mood: Tone is the writer's attitude (e.g. satirical, somber, reverent, indignant). Mood is the emotional atmosphere created for the reader (e.g. eerie, jubilant, melancholic).",
        "socratic_prompt": "Think about tone of voice: whose voice is it? The author's! And who feels the mood when entering a room or reading a text?"
    },
    {
        "id": "lit_004",
        "subject": "Literature in English",
        "topic": "Poetry Analysis",
        "subtopic": "Sonnets (Shakespearean vs Italian)",
        "year": 2023,
        "question": "A traditional Shakespearean (English) sonnet is structurally organized into _______.",
        "options": {
            "A": "an octave (8 lines) rhyming ABBAABBA followed by a sestet (6 lines)",
            "B": "three quatrains (4 lines each) and a final rhyming couplet (2 lines) with rhyme scheme ABAB CDCD EFEF GG",
            "C": "two septets with unrhymed free verse iambic pentameter",
            "D": "four tercets and a concluding heroic quatrain"
        },
        "correct_option": "B",
        "traps": {
            "A": "An octave and sestet (ABBAABBA CDECDE) defines the Italian / Petrarchan sonnet, not the Shakespearean sonnet.",
            "C": "Sonnets are strictly 14-line structured rhymed lyric poems, never unrhymed free verse septets.",
            "D": "A Shakespearean sonnet consists of 3 quatrains (12 lines) and 1 couplet (2 lines) = 14 lines."
        },
        "pedagogical_concept": "Shakespearean Sonnet Architecture: Comprises 14 lines of iambic pentameter arranged into three quatrains and a terminal couplet (ABAB CDCD EFEF GG). The couplet delivers the emotional resolution or thematic pivot (volta).",
        "socratic_prompt": "How many lines are in a quatrain? If there are 3 quatrains (3 * 4 = 12 lines), how many lines make up the rhyming couplet at the end to make 14 lines total?"
    }
]

added = 0
for q in new_batch:
    if q["id"] not in existing_ids:
        questions.append(q)
        existing_ids.add(q["id"])
        added += 1

with open(QUESTIONS_PATH, "w", encoding="utf-8") as f:
    json.dump(questions, f, indent=2)

print(f"Successfully added {added} new high-yield past questions! Total questions now: {len(questions)}")
