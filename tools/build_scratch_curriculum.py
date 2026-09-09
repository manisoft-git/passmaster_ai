import json
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from tools.build_deep_lessons import build_all_lessons

def build_scratch_and_prerequisite_curriculum():
    base_lessons = build_all_lessons()
    
    # Prerequisite mappings and From-Scratch guides for Core Lessons
    prerequisite_map = {
        ("Use of English", "Concord & Grammar"): [
            {"topic": "Parts of Speech Foundations", "reason": "You must understand noun number, auxiliary verbs, and pronoun-antecedent logic before applying proximity and subjunctive rules."},
            {"topic": "Clause & Sentence Foundations", "reason": "Knowing independent vs dependent clauses is required to navigate parenthetical intervening phrases."}
        ],
        ("Use of English", "Lexis & Structure"): [
            {"topic": "Parts of Speech Foundations", "reason": "Prepositions, phrasal verb particles, and semantic modifiers depend on grammatical parts of speech."},
            {"topic": "Clause & Sentence Foundations", "reason": "Contextual meaning and idioms require parsing complex sentence syntax."}
        ],
        ("Use of English", "Oral Forms & Phonology"): [
            {"topic": "Parts of Speech Foundations", "reason": "Identifying noun-verb stress shifts (e.g., RE-cord vs re-CORD) requires parts-of-speech classification."},
            {"topic": "Clause & Sentence Foundations", "reason": "Sentence intonation and rhythm depend on clause boundaries and stress patterns."}
        ],
        ("Use of English", "Comprehension & Prescribed Text"): [
            {"topic": "Clause & Sentence Foundations", "reason": "Inferential comprehension requires analyzing subtle clause structures and tonal markers."},
            {"topic": "Parts of Speech Foundations", "reason": "Diction and register analysis depend on understanding lexical word choices."}
        ],
        ("Mathematics", "Algebra"): [
            {"topic": "Arithmetic & Algebraic Foundations", "reason": "Mastery of directed numbers, BODMAS, fractional indices, and expanding brackets is essential before handling quadratic roots and logarithms."}
        ],
        ("Mathematics", "Calculus"): [
            {"topic": "Arithmetic & Algebraic Foundations", "reason": "Differentiation rules require rapid polynomial simplification, negative exponents, and algebraic substitution."},
            {"topic": "Coordinate & Function Foundations", "reason": "Derivatives represent the tangent gradient to a curve on the Cartesian coordinate plane."}
        ],
        ("Mathematics", "Geometry & Trigonometry"): [
            {"topic": "Coordinate & Function Foundations", "reason": "Coordinate geometry, distances, and angles require Cartesian plane literacy (x, y axes and quadrants)."},
            {"topic": "Arithmetic & Algebraic Foundations", "reason": "Solving sine/cosine equations and circle theorems requires quadratic and algebraic manipulation."}
        ],
        ("Mathematics", "Statistics & Probability"): [
            {"topic": "Arithmetic & Algebraic Foundations", "reason": "Calculating permutations, factorials (n!), and probabilities requires fractional and algebraic arithmetic."}
        ],
        ("Physics", "Mechanics"): [
            {"topic": "Units, Dimensions & Vectors", "reason": "Newtonian mechanics requires resolving vectors into horizontal and vertical components and checking SI unit dimensions."}
        ],
        ("Physics", "Thermal Physics & Waves"): [
            {"topic": "Kinetic Theory & Heat Fundamentals", "reason": "Understanding Charles's Law and calorimetry requires understanding molecular kinetic theory and Kelvin temperature scales."},
            {"topic": "Units, Dimensions & Vectors", "reason": "Wave frequency, wavelength, and mechanical oscillations require kinematic motion principles."}
        ],
        ("Physics", "Electricity & Magnetism"): [
            {"topic": "Units, Dimensions & Vectors", "reason": "Electric field lines, magnetic flux, and Lorentz forces are vector quantities requiring directional analysis."}
        ],
        ("Physics", "Modern & Atomic Physics"): [
            {"topic": "Units, Dimensions & Vectors", "reason": "Momentum, kinetic energy of photoelectrons, and Planck's equation rely on foundational mechanics."}
        ],
        ("Chemistry", "Physical & General Chemistry"): [
            {"topic": "Atomic & Bonding Foundations", "reason": "Chemical equilibrium and reaction rates depend on atomic collisions, valency, and molecular structure."},
            {"topic": "Chemical Equations & Stoichiometric Foundations", "reason": "The mole concept, gas volumes, and titrations require balancing chemical reaction equations first."}
        ],
        ("Chemistry", "Inorganic Chemistry"): [
            {"topic": "Atomic & Bonding Foundations", "reason": "Periodic trends, ionization energies, and complex ions require electron shell configurations (s, p, d, f orbitals)."},
            {"topic": "Chemical Equations & Stoichiometric Foundations", "reason": "Qualitative salt precipitation and metal extractions require writing net ionic equations."}
        ],
        ("Chemistry", "Organic Chemistry"): [
            {"topic": "Atomic & Bonding Foundations", "reason": "Carbon tetravalency, sp³-sp²-sp hybridization, and covalent bond polarity govern all organic reaction mechanisms."}
        ],
        ("Chemistry", "Environmental & Industrial Chemistry"): [
            {"topic": "Chemical Equations & Stoichiometric Foundations", "reason": "Faraday electrolysis calculations and industrial chemical yields require balanced redox equations."}
        ],
        ("Biology", "Cellular Biology & Life Processes"): [
            {"topic": "Biological Molecules & Cell Foundations", "reason": "Enzyme action, active transport, and cell membrane permeability depend on lipids, proteins, and carbohydrates."}
        ],
        ("Biology", "Human Physiology & Systems"): [
            {"topic": "Biological Molecules & Cell Foundations", "reason": "Digestion, blood transport, and hormones require understanding biological polymers and cell organelle functions."}
        ],
        ("Biology", "Genetics & Evolution"): [
            {"topic": "Chromosomes & Cell Division Foundations", "reason": "Mendel's laws of segregation and assortment depend on understanding homologous chromosome separation in meiosis."}
        ],
        ("Biology", "Ecology & Environment"): [
            {"topic": "Biological Molecules & Cell Foundations", "reason": "Trophic energy transfer and nutrient cycles depend on understanding photosynthesis and organic carbon/nitrogen synthesis."}
        ],
        ("Economics", "Basic Economic Principles & Methodology"): [
            {"topic": "Foundational Economic Reasoning", "reason": "Understanding economic systems and production requires first understanding scarcity, choice, and opportunity cost from first principles."}
        ],
        ("Economics", "Microeconomics & Price Mechanism"): [
            {"topic": "Foundational Economic Reasoning", "reason": "Demand and supply laws require understanding consumer utility and rational choice under scarcity."},
            {"topic": "Economic Graphing & Elasticity Foundations", "reason": "Calculating price elasticity and market equilibrium requires plotting and interpreting supply-demand curves."}
        ],
        ("Economics", "Macroeconomics & National Income"): [
            {"topic": "Economic Graphing & Elasticity Foundations", "reason": "Understanding aggregate demand and multiplier shifts requires graphing national income circular flow loops."}
        ],
        ("Economics", "Money, Banking & Public Finance"): [
            {"topic": "Foundational Economic Reasoning", "reason": "Monetary policy and credit creation require understanding the transition from barter trade to currency units."}
        ],
        ("Government", "Elements of Government & Political Theory"): [
            {"topic": "Political Concepts & The State Foundations", "reason": "Analyzing democracy, separation of powers, and rule of law requires defining the State, power, authority, and legitimacy."}
        ],
        ("Government", "Colonial Administration in Nigeria & West Africa"): [
            {"topic": "Pre-Colonial Heritage Foundations", "reason": "Understanding British Indirect Rule requires knowing how the pre-colonial Hausa-Fulani, Yoruba, and Igbo societies governed themselves."}
        ],
        ("Government", "Nigerian Constitutional Development"): [
            {"topic": "Pre-Colonial Heritage Foundations", "reason": "Constitutional reforms from Clifford (1922) to 1999 reflect the historical regional tensions rooted in the 1914 Amalgamation."},
            {"topic": "Political Concepts & The State Foundations", "reason": "Constitutional provisions depend on legal sovereignty and federal legislative lists."}
        ],
        ("Government", "Federalism, Military Rule & Foreign Policy"): [
            {"topic": "Political Concepts & The State Foundations", "reason": "Federalism and military decrees require understanding federal power division and constitutional supremacy."}
        ],
        ("Literature in English", "Literary Appreciation & Devices"): [
            {"topic": "Literary Genres & Fundamentals", "reason": "Analyzing figures of speech requires distinguishing poetry, prose, and dramatic conventions."},
            {"topic": "Figurative Devices & Tropes Foundations", "reason": "Distinguishing paradox from oxymoron and metonymy from synecdoche requires foundational semantic tropes."}
        ],
        ("Literature in English", "Drama & Theatrical Techniques"): [
            {"topic": "Literary Genres & Fundamentals", "reason": "Theatrical staging, blocking, and dramatic irony require understanding dramatic text vs prose narrative."},
            {"topic": "Figurative Devices & Tropes Foundations", "reason": "Character dialogue analysis requires interpreting verbal irony and poetic conceits."}
        ],
        ("Literature in English", "Poetry & Versification"): [
            {"topic": "Literary Genres & Fundamentals", "reason": "Scansion, meter, and stanza forms require understanding poetic lines vs prose paragraphs."},
            {"topic": "Figurative Devices & Tropes Foundations", "reason": "Analyzing sonnets and elegies requires recognizing sensory imagery and sound devices (assonance, alliteration)."}
        ],
        ("Literature in English", "Prose & Fictional Techniques"): [
            {"topic": "Literary Genres & Fundamentals", "reason": "Analyzing narrative perspectives (first person vs omniscient) requires prose structure fundamentals."}
        ]
    }

    # Plain everyday Nigerian analogies & from-scratch explanations
    from_scratch_guide_map = {
        ("Use of English", "Concord & Grammar"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Imagine two passengers fighting over an empty seat in a Danfo bus. Who gets the seat? The passenger sitting closest to it! "
            "That is the exact principle behind the Rule of Proximity: when two subjects are joined by 'or' or 'nor', ignore whoever is far away, "
            "and match your verb ONLY to the noun closest to the verb. If the closest word is singular, use a singular verb (is/was/has). "
            "If it is plural, use a plural verb (are/were/have). It is that simple!"
        ),
        ("Use of English", "Lexis & Structure"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "English words are like ingredients in a pot of authentic jollof rice: you cannot swap salt for sugar and expect it to taste right. "
            "Certain words always travel together in pairs (Collocations). You don't 'make' a photo, you 'take' a photo. You don't take exception 'against' someone, "
            "you take exception 'TO' an insult. Once you learn the fixed pairs, these questions become free marks!"
        ),
        ("Use of English", "Oral Forms & Phonology"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "English spelling is notoriously deceitful. The letters you write are NOT the sounds you pronounce! In words like 'subtle' or 'debt', "
            "the letter 'b' is completely silent. In stress patterns, think of capital syllables like beating a loud drum: RE-cord is the object in your hand, "
            "while re-CORD is the action you perform with a microphone. Listening for the loudest drum beat solves 100% of JAMB stress questions."
        ),
        ("Use of English", "Comprehension & Prescribed Text"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Comprehension is NOT memorization; it is detective work. The examiner gives you a passage and leaves clues. "
            "Whenever a question asks 'The author implies that...', never guess from your personal feelings! Look strictly at the textual evidence. "
            "In 'The Life Changer', observe how characters like Salma and Habib interact to deduce the novel's central warnings about campus independence."
        ),
        ("Mathematics", "Algebra"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Algebra is simply solving everyday riddles. If 2 loaves of bread cost ₦1,000, 1 loaf costs ₦500. "
            "In quadratic equations (ax² + bx + c = 0), the roots α and β are simply the two hidden solutions. "
            "JAMB will ask for (α + β) or (αβ). You don't need to solve the whole equation! Just remember: sum = -b/a and product = c/a. "
            "You can crack these questions in under 15 seconds without even touching your pencil!"
        ),
        ("Mathematics", "Calculus"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Think of differentiation as the speedometer in your car. Distance tells you WHERE you are, but the derivative tells you HOW FAST you are moving right at this split second. "
            "To differentiate any power of x (like x³), follow the 2-step dance: multiply by the power, then decrease the power by 1 (3x²). "
            "Integration is simply driving in reverse: increase the power by 1, then divide by the new power!"
        ),
        ("Mathematics", "Geometry & Trigonometry"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Trigonometry is the science of right-angled triangles. Remember SOH-CAH-TOA like a rhythm: Sine = Opposite/Hypotenuse, Cosine = Adjacent/Hypotenuse, "
            "Tangent = Opposite/Adjacent. When dealing with circles, remember the butterfly theorem (angles subtended by the same arc in the same segment are equal) "
            "and the cyclic quadrilateral rule (opposite interior angles always add up to 180°)."
        ),
        ("Mathematics", "Statistics & Probability"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Probability is the math of chance. If you roll a fair 6-sided die, what is the chance of getting a 4? Exactly 1 out of 6. "
            "The golden rule: 'AND' means multiply, while 'OR' means add. If you want a 4 AND a 6 on two rolls: (1/6) × (1/6) = 1/36. "
            "Permutations care about order (like first and second place in a race), while Combinations do NOT care about order (like picking 3 friends for lunch)."
        ),
        ("Physics", "Mechanics"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Have you ever stood in a Danfo bus when the driver suddenly slammed on the brakes? You lurched forward! "
            "That is Newton's First Law (Inertia): your body wanted to keep moving at the same speed. "
            "Mechanics simply puts numbers to what your body experiences every day: Force = mass × acceleration, Work = Force × distance, and "
            "Momentum is conserved in every collision in the universe."
        ),
        ("Physics", "Thermal Physics & Waves"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Heat is microscopic kinetic energy. When you boil water, water molecules start vibrating and bouncing like dancers in a crowded concert. "
            "In Boyle's Law, squeezing a gas into half the volume doubles the pressure because the molecules hit the walls twice as often. "
            "For waves: Speed = Frequency × Wavelength (v = fλ). If you know this simple equation, you can solve half of the wave problems in JAMB."
        ),
        ("Physics", "Electricity & Magnetism"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Think of electrical current like water flowing through pipes. Voltage is the water pump pressure pushing the water, Current is the volume of water flowing per second, "
            "and Resistance is sand or narrow pipes slowing it down. Ohm's Law states: Voltage = Current × Resistance (V = IR). "
            "In parallel circuits, electricity gets multiple paths, so the total resistance drops!"
        ),
        ("Physics", "Modern & Atomic Physics"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Imagine shining light onto a metal plate like throwing ping-pong balls at coins to knock them off a table. "
            "In Einstein's Photoelectric Effect, light travels in tiny energy packets called photons (E = hf). "
            "If a photon has enough energy, it knocks an electron clean out of the metal. If it doesn't have enough frequency, even shining a million lights won't knock out a single electron!"
        ),
        ("Chemistry", "Physical & General Chemistry"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Think of a chemical reaction like baking a cake. If the recipe calls for 2 eggs and 1 cup of flour, you cannot bake a cake with 0.5 eggs. "
            "That is the Mole Concept (Stoichiometry): atoms always react in fixed whole-number ratios. "
            "One mole of anything contains exactly 6.02 × 10²³ particles (Avogadro's number). Once you convert grams to moles, solving any chemistry problem becomes simple arithmetic."
        ),
        ("Chemistry", "Inorganic Chemistry"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "The Periodic Table is the ultimate family tree of the elements. Elements in the same vertical group behave like siblings because they have the exact same number of valence electrons. "
            "Group 1 alkali metals are desperate to give away 1 electron, while Group 7 halogens are hungry to snatch 1 electron. "
            "Knowing this allows you to predict whether a reaction will explode, form salt, or do nothing at all."
        ),
        ("Chemistry", "Organic Chemistry"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Carbon is the Lego brick of life because it has 4 arms (tetravalency) that can hold hands with other carbon atoms indefinitely. "
            "Single bonds are Alkanes (-ane), double bonds are Alkenes (-ene), and triple bonds are Alkynes (-yne). "
            "Add an -OH group and you get an Alcohol; add a -COOH group and you get a Carboxylic acid. Mix them together with an acid catalyst and you get sweet-smelling Esters!"
        ),
        ("Chemistry", "Environmental & Industrial Chemistry"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Electrolysis is using electricity to force stubborn chemical reactions to happen. "
            "At the Cathode, positive cations gain electrons (Reduction). At the Anode, negative anions lose electrons (Oxidation). "
            "Faraday's First Law: The mass deposited is directly proportional to the total electrical charge passed (m = ZIt)."
        ),
        ("Biology", "Cellular Biology & Life Processes"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Your body is built from trillions of microscopic biological factories called cells. "
            "The Nucleus is the managing director's office holding the blueprints (DNA); the Mitochondria are the diesel generators producing energy (ATP); "
            "and Ribosomes are the workers building proteins. Enzymes are biological catalysts that speed up digestion from 50 years to 2 seconds without getting used up!"
        ),
        ("Biology", "Human Physiology & Systems"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Your body is a masterfully automated engineering machine. Your heart beats 100,000 times a day to pump oxygen-rich blood through arteries to your brain. "
            "Your kidneys filter 180 liters of fluid every day through microscopic nephrons, reabsorbing 99% of the water and dumping toxins as urine. "
            "Mastering the flow charts of circulation and excretion makes JAMB questions effortless."
        ),
        ("Biology", "Genetics & Evolution"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Why do children look like their parents? Because you inherit one set of 23 chromosomes from your mother and one set from your father. "
            "Gregor Mendel discovered that traits come in pairs of alleles: Dominant (shouts loudly) and Recessive (whispers quietly). "
            "A Punnett square is just a 2×2 multiplication table that predicts the exact probability of an offspring inheriting brown eyes or sickle-cell trait."
        ),
        ("Biology", "Ecology & Environment"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Ecology is the study of who eats whom in nature. Plants (Producers) trap sunlight through photosynthesis. "
            "Herbivores eat plants, carnivores eat herbivores, and decomposers recycle the nutrients back into the soil. "
            "Because 90% of energy is lost as heat at every step, food chains rarely exceed 4 or 5 trophic levels."
        ),
        ("Economics", "Basic Economic Principles & Methodology"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "If money grew on trees, there would be no economics! Economics exists because human wants are infinite, but the resources (money, land, time) to satisfy them are scarce. "
            "Every time you choose to buy a ₦1,000 data bundle instead of a plate of rice, the rice is your Opportunity Cost: the alternative forgone. "
            "Mastering this trade-off is the foundation of all economic theory."
        ),
        ("Economics", "Microeconomics & Price Mechanism"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Think of the Balogun market in Lagos: When tomatoes are in abundance during harvest season, sellers drop the price. When tomatoes become scarce, prices skyrocket! "
            "Where the buyer's willingness to pay meets the seller's willingness to sell is the Market Equilibrium. "
            "Elasticity simply measures how violently buyers react when prices change."
        ),
        ("Economics", "Macroeconomics & National Income"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Macroeconomics looks at the entire country like a single giant household. "
            "Gross Domestic Product (GDP) is the total cash value of all goods and services produced inside Nigeria in a year. "
            "When the government builds a ₦10 billion highway, that money pays construction workers, who spend it on food, which pays farmers. "
            "This chain reaction is called the Keynesian Multiplier: one naira injected multiplies into many nairas of national income!"
        ),
        ("Economics", "Money, Banking & Public Finance"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Before paper money existed, if you had a goat and wanted yams, you had to find someone who had yams AND wanted a goat! "
            "Money solved this 'double coincidence of wants' by acting as a universal medium of exchange. "
            "The Central Bank of Nigeria (CBN) acts as the boss of all commercial banks, raising the Monetary Policy Rate (MPR) to fight inflation or lowering it to stimulate business loans."
        ),
        ("Government", "Elements of Government & Political Theory"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Imagine living in a town with no laws, no police, and no courts: pure chaos! "
            "The State exists to maintain order, security, and justice. Sovereignty is the supreme, absolute power of a state to make laws without foreign interference. "
            "Under the Separation of Powers, the Legislature makes the law, the Executive enforces the law, and the Judiciary interprets the law to prevent tyranny."
        ),
        ("Government", "Colonial Administration in Nigeria & West Africa"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "When Lord Lugard took control of Nigeria, the British had very few officers and very little money. "
            "So Lugard used the existing traditional rulers (Emirs and Obas) to collect taxes and run local courts. This system was called Indirect Rule. "
            "It worked smoothly in the centralized Northern Emirates, but caused fierce riots in the East because traditional Igbo society was egalitarian with no kings!"
        ),
        ("Government", "Nigerian Constitutional Development"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Nigeria's constitutions are the milestones of our journey to nationhood. "
            "The Clifford Constitution (1922) introduced the Elective Principle for the first time in Lagos and Calabar. "
            "The Richards Constitution (1946) created regional councils. The Lyttelton Constitution (1954) established true Federalism, "
            "and the 1963 Republican Constitution severed all ties with Queen Elizabeth II to make Nigeria a sovereign republic."
        ),
        ("Government", "Federalism, Military Rule & Foreign Policy"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Because Nigeria has over 250 diverse ethnic nationalities, a unitary system would tear the country apart. "
            "Federalism shares power between the central Federal Government in Abuja and the 36 State governments. "
            "In foreign policy, Nigeria champions 'Afrocentricism': placing the liberation, peace, and economic prosperity of Africa at the center of all diplomatic relations."
        ),
        ("Literature in English", "Literary Appreciation & Devices"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Literature is art painted with words. Instead of saying 'He is very brave', a writer writes 'He is a lion in battle' (Metaphor). "
            "Instead of saying 'The classroom was quiet', an author writes 'There was a deafening silence' (Oxymoron). "
            "Learning literary devices is simply learning how to spot the poetic tools writers use to make ideas stick in your imagination."
        ),
        ("Literature in English", "Drama & Theatrical Techniques"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Drama is a story written to be performed by live actors on a stage. "
            "When an actor speaks alone on stage revealing their deepest thoughts to the audience, it is a Soliloquy. "
            "When the audience knows the villain has poisoned the cup, but the hero drinks it cheerfully, that agonizing tension is Dramatic Irony!"
        ),
        ("Literature in English", "Poetry & Versification"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Poetry is music for the mind. It uses meter, rhythm, and rhyme to evoke intense emotions. "
            "A Sonnet is always exactly 14 lines long. A Shakespearean sonnet has 3 four-line stanzas (quatrains) and ends with a punchy rhyming couplet (abab cdcd efef gg). "
            "An Elegy is a poem of sorrow written to mourn the dead, while an Ode is a poem of joyful praise."
        ),
        ("Literature in English", "Prose & Fictional Techniques"): (
            "💡 LEARN FROM SCRATCH (Zero Prior Jargon):\n"
            "Prose is storytelling in continuous sentences and paragraphs. "
            "When the narrator uses 'I' and was part of the events, that is First-Person point of view. "
            "When the narrator is an all-knowing, god-like voice who knows what every single character is feeling, that is Third-Person Omniscient. "
            "In Achebe's 'Things Fall Apart', Okonkwo's tragic flaw (Hamartia) was his crippling fear of being thought weak like his father Unoka."
        )
    }

    # 16 Brand New Foundational Prerequisite Lessons (2 per subject)
    foundational_modules = {
        "Use of English": [
            {
                "id": "eng_found_1",
                "topic": "Parts of Speech Foundations",
                "title": "Mastering English Word Classes: Nouns, Pronouns, Verbs & Prepositions",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of English)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Every single English sentence is composed from eight fundamental word classes (parts of speech). Before tackling complex concord rules, phrasal idioms, or subjunctive clauses, you must be able to infallibly identify nouns, pronouns, transitive/intransitive verbs, and prepositional particles.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of parts of speech like players on a football pitch: Nouns are the strikers who score goals, Pronouns are the substitute players who take the striker's place when they are tired (John -> He), "
                    "Verbs are the action and movement across the pitch, Adjectives decorate the players with team jerseys, and Prepositions tell you where the ball is on the field (in, on, under, between)."
                ),
                "key_concepts": [
                    {
                        "concept": "Noun Classification & Number Agreement",
                        "explanation": "Countable nouns have plural forms (book -> books). Uncountable nouns (information, luggage, equipment, advice, furniture) NEVER take 's' and always take singular verbs.",
                        "examples": ["The advice WAS helpful (NOT advices were).", "All the baggage HAS arrived (NOT baggages have)."]
                    },
                    {
                        "concept": "Transitive vs Intransitive Verbs",
                        "explanation": "Transitive verbs require a direct object to complete their meaning (raise, lay). Intransitive verbs do not take an object (rise, lie).",
                        "examples": ["He RAISED the flag (Transitive).", "The sun RISES in the east (Intransitive)."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Pluralizing uncountable nouns (e.g. 'furnitures', 'equipments', 'informations').",
                    "Trap 2: Confusing transitive 'lay/laid' (to put down) with intransitive 'lie/lay/lain' (to recline)."
                ],
                "worked_examples": [
                    {
                        "question": "The customs official inspected our _______ thoroughly before clearing our flight.",
                        "options": ["A. luggages", "B. luggage", "C. pieces of luggages", "D. baggages"],
                        "solution": "'Luggage' is an uncountable mass noun in English and cannot take a plural suffix '-s'. Correct Option: B (luggage)."
                    }
                ],
                "golden_rule": "Golden Rule: Mass nouns (luggage, equipment, information, advice) are NEVER pluralized with '-s'.",
                "prepares_for": ["Concord & Grammar", "Lexis & Structure"]
            },
            {
                "id": "eng_found_2",
                "topic": "Clause & Sentence Foundations",
                "title": "Clause Architecture: Independent vs Dependent Clauses & Sentence Syntax",
                "jamb_weight": "Foundational Prerequisite (Essential for Syntax & Comprehension)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "A clause contains a subject and a finite predicate. An independent clause can stand alone as a complete thought, whereas a dependent (subordinate) clause requires an independent clause. Mastering clause boundaries prevents comma splices, sentence fragments, and concord confusion.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "An independent clause is an adult who can live alone in their own apartment ('The rain fell heavily'). "
                    "A dependent clause is a child who cannot survive without a parent ('Because the rain fell heavily...'). "
                    "Notice that when you start with 'Because', your ear waits for the rest of the story! You must join the child to the parent to make a complete sentence."
                ),
                "key_concepts": [
                    {
                        "concept": "Subordinating vs Coordinating Conjunctions",
                        "explanation": "Coordinating conjunctions (FANBOYS: For, And, Nor, But, Or, Yet, So) join equal independent clauses. Subordinating conjunctions (although, because, since, while, if) create dependent clauses.",
                        "examples": ["Although he studied hard (Dependent), he missed the bus (Independent)."]
                    },
                    {
                        "concept": "Parenthetical Adjuncts vs Sentence Subjects",
                        "explanation": "Parenthetical phrases enclosed by commas or dashes provide extra information but do not alter the main clause subject-verb relationship.",
                        "examples": ["Dr. Okon, who treats pediatric patients in Ikeja, is retiring today."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Treating dependent clauses introduced by 'although' or 'since' as complete sentences.",
                    "Trap 2: Allowing subordinate clause nouns to disrupt the main clause subject-verb concord."
                ],
                "worked_examples": [
                    {
                        "question": "Although the team practiced diligently for months, _______ to secure the championship trophy.",
                        "options": ["A. but they failed", "B. they failed", "C. yet they failed", "D. and they failed"],
                        "solution": "'Although' already introduces a subordinate adverbial clause. The main clause must NOT start with a coordinating conjunction like 'but' or 'yet'. Correct Option: B (they failed)."
                    }
                ],
                "golden_rule": "Golden Rule: Never pair 'Although' with 'But' in the same sentence; let the independent clause stand unhindered.",
                "prepares_for": ["Concord & Grammar", "Comprehension & Prescribed Text"]
            }
        ],
        "Mathematics": [
            {
                "id": "mth_found_1",
                "topic": "Arithmetic & Algebraic Foundations",
                "title": "Foundational Number Operations, Indices & Algebraic Simplification",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of JAMB Math)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Every advanced topic in JAMB Mathematics—from calculus and logarithms to trigonometry and circle theorems—assumes absolute fluency in basic arithmetic, directed negative numbers, fraction operations, exponent index laws, and polynomial expansion.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Negative numbers are like debts. If you have ₦500 and owe someone ₦700, your net position is -₦200 (500 - 700 = -200). "
                    "Multiplying two negative numbers is like cancelling a debt: (-3) × (-4) = +12. "
                    "Index laws are simply counting how many times you multiply: x³ × x² = (x·x·x) · (x·x) = x⁵. You simply add the powers!"
                ),
                "key_concepts": [
                    {
                        "concept": "Fundamental Laws of Indices",
                        "explanation": "a^m × a^n = a^(m+n); a^m ÷ a^n = a^(m-n); (a^m)^n = a^(mn); a^0 = 1; a^(-n) = 1/(a^n); a^(1/n) = n-th root of a.",
                        "examples": ["8^(2/3) = (∛8)² = 2² = 4.", "5^(-2) = 1/(5²) = 1/25."]
                    },
                    {
                        "concept": "Factorization & Difference of Two Squares",
                        "explanation": "a² - b² = (a - b)(a + b). This algebraic shortcut appears in almost every single JAMB exam paper.",
                        "examples": ["98² - 2² = (98 - 2)(98 + 2) = 96 × 100 = 9,600 (solved in 2 seconds without a calculator!)."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Thinking (-2)² is negative. (-2)² = +4, whereas -2² = -4.",
                    "Trap 2: Forgetting that any non-zero number raised to the power 0 equals 1."
                ],
                "worked_examples": [
                    {
                        "question": "Simplify: (27)^(2/3) × (16)^(-1/4).",
                        "options": ["A. 9/2", "B. 4.5", "C. 18", "D. 3/2"],
                        "solution": "27^(2/3) = (∛27)² = 3² = 9. 16^(-1/4) = 1 / (⁴√16) = 1/2. Therefore: 9 × (1/2) = 9/2. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Always evaluate fractional roots before raising to powers: a^(m/n) = (ⁿ√a)ᵐ.",
                "prepares_for": ["Algebra", "Calculus"]
            },
            {
                "id": "mth_found_2",
                "topic": "Coordinate & Function Foundations",
                "title": "The Cartesian Plane, Linear Slopes & Function Notations",
                "jamb_weight": "Foundational Prerequisite (Essential for Geometry & Calculus)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "René Descartes revolutionized mathematics by connecting algebra with geometry using the Cartesian coordinate system (x, y). Understanding gradients, midpoints, intercepts, and function mappings f(x) is compulsory before tackling tangents, derivatives, and conic sections.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of the Cartesian coordinate plane like giving directions in Abuja or Lagos: 'Go 3 streets East (x-axis), then 4 streets North (y-axis)' gives the point (3, 4). "
                    "The gradient (slope m) tells you how steep a hill is: Rise over Run (change in y divided by change in x). "
                    "If a line slopes upward from left to right, the gradient is positive; if it slopes downward, it is negative!"
                ),
                "key_concepts": [
                    {
                        "concept": "Gradient and Straight Line Equation",
                        "explanation": "Slope m = (y₂ - y₁) / (x₂ - x₁). The equation of a straight line is y = mx + c, where c is the y-intercept.",
                        "examples": ["For points (1, 2) and (3, 8): m = (8 - 2)/(3 - 1) = 6/2 = 3. Equation: y - 2 = 3(x - 1) => y = 3x - 1."]
                    },
                    {
                        "concept": "Perpendicular Lines Condition",
                        "explanation": "Two non-vertical lines are perpendicular if and only if the product of their gradients is -1 (m₁ × m₂ = -1). That is, m₂ = -1/m₁.",
                        "examples": ["If a line has gradient 2, any line perpendicular to it has gradient -1/2."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Subtracting coordinates in reverse order when finding gradient: (y₂ - y₁) / (x₁ - x₂) gives the opposite sign!",
                    "Trap 2: Forgetting the negative reciprocal for perpendicular lines."
                ],
                "worked_examples": [
                    {
                        "question": "Find the gradient of a line perpendicular to the line 2x + 4y = 9.",
                        "options": ["A. 2", "B. -1/2", "C. 1/2", "D. -2"],
                        "solution": "Rearrange into y = mx + c: 4y = -2x + 9 => y = -1/2 x + 9/4. The gradient m₁ = -1/2. The perpendicular gradient m₂ = -1/(-1/2) = +2. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Parallel lines share equal slopes (m₁ = m₂); perpendicular lines have negative reciprocal slopes (m₁ × m₂ = -1).",
                "prepares_for": ["Geometry & Trigonometry", "Calculus"]
            }
        ],
        "Physics": [
            {
                "id": "phy_found_1",
                "topic": "Units, Dimensions & Vectors",
                "title": "Fundamental Units, Dimensional Consistency & Vector Resolution",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of JAMB Physics)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Physics is an exact quantitative science. All physical formulas must be dimensionally homogeneous across length [L], mass [M], and time [T]. Furthermore, quantities possessing both magnitude and direction (vectors like velocity, force, and momentum) cannot be added like ordinary numbers; they must be resolved into orthogonal components.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "If someone says 'walk 5 kilometers', you have no idea where you'll end up. You could end up in the lagoon! That is a Scalar (magnitude only). "
                    "If they say 'walk 5 kilometers North', you will arrive safely at your destination. That is a Vector (magnitude + direction). "
                    "When pulling a heavy suitcase by a strap at an angle θ, only the horizontal piece (F cos θ) drags the bag forward along the ground."
                ),
                "key_concepts": [
                    {
                        "concept": "Dimensional Analysis",
                        "explanation": "Express quantities in fundamental dimensions: Velocity = [LT⁻¹], Acceleration = [LT⁻²], Force = [MLT⁻²], Work/Energy = [ML²T⁻²], Pressure = [ML⁻¹T⁻²].",
                        "examples": ["Check: Kinetic energy E = 1/2 mv² => [M][LT⁻¹]² = [ML²T⁻²], identical to Work = Force × distance."]
                    },
                    {
                        "concept": "Vector Resolution",
                        "explanation": "Any vector F acting at angle θ to the horizontal resolves into F_x = F cos θ and F_y = F sin θ.",
                        "examples": ["A force of 50 N at 60° to the horizontal: F_x = 50 cos(60°) = 25 N; F_y = 50 sin(60°) = 43.3 N."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Adding vectors like scalars: 3 N East + 4 N North is NOT 7 N; by Pythagoras it is √(3² + 4²) = 5 N!",
                    "Trap 2: Forgetting to convert minutes or hours into SI seconds before calculating velocity or power."
                ],
                "worked_examples": [
                    {
                        "question": "Which of the following physical quantities has the dimensional formula [ML²T⁻²]?",
                        "options": ["A. Torque and Work", "B. Momentum and Impulse", "C. Force and Power", "D. Pressure and Stress"],
                        "solution": "Work = Force × distance = [MLT⁻²] × [L] = [ML²T⁻²]. Torque = Force × perpendicular distance = [ML²T⁻²]. Both have identical dimensions. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Horizontal component always takes COSINE (F cos θ) and vertical component takes SINE (F sin θ) when angle θ is measured from the horizontal.",
                "prepares_for": ["Mechanics", "Electricity & Magnetism"]
            },
            {
                "id": "phy_found_2",
                "topic": "Kinetic Theory & Heat Fundamentals",
                "title": "Molecular Motion, Kinetic Theory of Matter & Absolute Temperature Scales",
                "jamb_weight": "Foundational Prerequisite (Essential for Thermal Physics & Gas Laws)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "The Kinetic Theory asserts that all matter consists of tiny sub-microscopic particles in continuous random motion. Temperature is the direct macroscopic measure of the average translational kinetic energy of these molecules. The absolute Kelvin scale (T = °C + 273.15) is compulsory for all thermodynamic calculations.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Imagine a room packed with 1,000 hyperactive toddlers bouncing in every direction. That is gas! "
                    "If you turn up the heat, the toddlers run twice as fast, smashing into the walls with immense force. That is Pressure! "
                    "At Absolute Zero (-273°C or 0 Kelvin), the toddlers freeze completely still. You can never get colder than absolute zero because molecules cannot move slower than completely stopped!"
                ),
                "key_concepts": [
                    {
                        "concept": "The Kelvin Absolute Temperature Scale",
                        "explanation": "Temperature in thermodynamic formulas must ALWAYS be converted to Kelvin: T(K) = θ(°C) + 273.",
                        "examples": ["0°C = 273 K; 27°C = 300 K; 100°C = 373 K."]
                    },
                    {
                        "concept": "Microscopic Basis of Gas Pressure",
                        "explanation": "Pressure is the average force per unit area exerted by gas molecules bombarding the container walls: P = 1/3 ρ c̅².",
                        "examples": ["Increasing temperature increases molecular root-mean-square speed c̅, directly boosting pressure."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Using Celsius directly in Charles's Law (V₁/T₁ = V₂/T₂). If you double temperature from 20°C to 40°C, the gas does NOT double in volume! (293 K to 313 K is only a 6.8% increase!)."
                ],
                "worked_examples": [
                    {
                        "question": "A fixed mass of gas occupies 300 cm³ at 27°C. What volume will it occupy at 127°C at constant pressure?",
                        "options": ["A. 400 cm³", "B. 1,411 cm³", "C. 600 cm³", "D. 350 cm³"],
                        "solution": "Convert temperatures to Kelvin: T₁ = 27 + 273 = 300 K; T₂ = 127 + 273 = 400 K. Charles's Law: V₁/T₁ = V₂/T₂ => 300 / 300 = V₂ / 400 => V₂ = 400 cm³. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Never plug Celsius into gas laws; always add 273 to convert to Kelvin!",
                "prepares_for": ["Thermal Physics & Waves", "Modern & Atomic Physics"]
            }
        ],
        "Chemistry": [
            {
                "id": "chm_found_1",
                "topic": "Atomic & Bonding Foundations",
                "title": "Subatomic Particles, Electronic Configurations (s,p,d,f) & Chemical Bonds",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of Chemistry)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "All chemical behavior is governed by the electronic structure of atoms. Atoms consist of a dense positive nucleus (protons and neutrons) surrounded by electrons occupying s, p, d, and f orbitals according to the Aufbau principle, Hund's rule, and Pauli's exclusion principle. Chemical bonds (ionic, covalent, metallic, hydrogen) form to achieve stable noble-gas electron configurations.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of an atom like a hotel where electrons are guests. The s-room holds 2 guests, the p-suite holds 6 guests, and the d-floor holds 10 guests. "
                    "Electrons fill the lowest floors first (1s, 2s, 2p, 3s, 3p, 4s, 3d). "
                    "Every atom dreams of a full outer shell (the Octet Rule: 8 valence electrons). Atoms will beg, borrow, steal (Ionic bond) or share (Covalent bond) electrons to get that full shell!"
                ),
                "key_concepts": [
                    {
                        "concept": "Aufbau Principle and Orbital Filling",
                        "explanation": "Orbitals fill in order of increasing energy: 1s² 2s² 2p⁶ 3s² 3p⁶ 4s² 3d¹⁰.",
                        "examples": ["Sodium (Z=11): 1s² 2s² 2p⁶ 3s¹ (1 valence electron in 3s).", "Calcium (Z=20): 1s² 2s² 2p⁶ 3s² 3p⁶ 4s²."]
                    },
                    {
                        "concept": "Ionic vs Covalent Bonding",
                        "explanation": "Ionic bonds form between metals (low electronegativity) and non-metals (high electronegativity) via electron transfer. Covalent bonds form between non-metals via electron sharing.",
                        "examples": ["NaCl is ionic with high melting point; CH₄ is non-polar covalent gas."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Filling 3d before 4s. 4s has lower energy than 3d and fills first (except anomalies in Cr and Cu).",
                    "Trap 2: Confusing covalent bonds within molecules with intermolecular hydrogen bonds between molecules."
                ],
                "worked_examples": [
                    {
                        "question": "What is the ground-state electronic configuration of an iron(III) ion (Fe³⁺)? (Atomic number of Fe = 26)",
                        "options": ["A. [Ar] 3d⁵", "B. [Ar] 4s² 3d³", "C. [Ar] 3d⁶", "D. [Ar] 4s¹ 3d⁴"],
                        "solution": "Neutral Fe is [Ar] 4s² 3d⁶. When transition metals ionize, electrons are lost FIRST from the outermost 4s subshell: Fe²⁺ is [Ar] 3d⁶, and Fe³⁺ loses one more 3d electron to become [Ar] 3d⁵ (stable half-filled d subshell). Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Transition metals ALWAYS lose their 4s electrons before losing 3d electrons during ionization.",
                "prepares_for": ["Physical & General Chemistry", "Inorganic Chemistry", "Organic Chemistry"]
            },
            {
                "id": "chm_found_2",
                "topic": "Chemical Equations & Stoichiometric Foundations",
                "title": "Balancing Chemical Equations, Ionic Charges & The Law of Conservation of Mass",
                "jamb_weight": "Foundational Prerequisite (Essential for Quantitative Chemistry)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "The Law of Conservation of Mass dictates that atoms are neither created nor destroyed during chemical reactions. Balancing equations by ensuring equal numbers of each atom on both sides of the reaction arrow is the non-negotiable foundation for every quantitative chemistry calculation in JAMB.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of a chemical reaction like an accounting balance sheet: what goes in MUST come out! "
                    "If you put 4 hydrogen atoms into a reaction, 4 hydrogen atoms must emerge in the products. "
                    "You can change the BIG coefficient in front of a formula (e.g. 2H₂O), but NEVER change the small subscript numbers (H₂O₂ is hydrogen peroxide, which will poison you if you drink it instead of water!)."
                ),
                "key_concepts": [
                    {
                        "concept": "Systematic Balancing of Combustion Reactions",
                        "explanation": "For hydrocarbons (C_x H_y), balance in the strict order: Carbon first, Hydrogen second, Oxygen last.",
                        "examples": ["Combustion of propane: C₃H₈ + 5O₂ -> 3CO₂ + 4H₂O."]
                    },
                    {
                        "concept": "Net Ionic Equations",
                        "explanation": "Spectator ions that remain dissolved in aqueous solution without participating in the reaction are canceled out.",
                        "examples": ["Precipitation of silver chloride: Ag⁺(aq) + Cl⁻(aq) -> AgCl(s)."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Changing chemical subscripts inside formulas while attempting to balance equations.",
                    "Trap 2: Forgetting that diatomic elements exist as pairs in nature (H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂)."
                ],
                "worked_examples": [
                    {
                        "question": "In the balanced equation: a Al + b H₂SO₄ -> c Al₂(SO₄)₃ + d H₂, what is the coefficient 'b'?",
                        "options": ["A. 3", "B. 2", "C. 6", "D. 1"],
                        "solution": "To provide 3 sulfate (SO₄) groups for Al₂(SO₄)₃ on the right, we must have 3 H₂SO₄ on the left (b = 3). Balanced equation: 2Al + 3H₂SO₄ -> Al₂(SO₄)₃ + 3H₂. Therefore b = 3. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Balance carbon first, hydrogen second, and oxygen last when balancing combustion reactions.",
                "prepares_for": ["Physical & General Chemistry", "Environmental & Industrial Chemistry"]
            }
        ],
        "Biology": [
            {
                "id": "bio_found_1",
                "topic": "Biological Molecules & Cell Foundations",
                "title": "Biochemistry of Life: Carbohydrates, Lipids, Proteins & Membrane Permeability",
                "jamb_weight": "Foundational Prerequisite (Essential for Cell Biology & Physiology)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "All living organisms are constructed from four major macromolecules: carbohydrates, lipids, proteins, and nucleic acids. Understanding peptide bonds, phospholipid bilayers, and membrane selectivity is compulsory before studying digestion, cellular respiration, and enzyme kinetics.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of your body like building a house: Carbohydrates are the electricity powering the lights (quick energy); "
                    "Lipids (fats) are the battery bank in the garage storing backup energy for a power outage; "
                    "Proteins are the concrete pillars, doors, and plumbing pipes that hold the building together; "
                    "and Enzymes are the specialized electricians and handymen who keep the systems running smoothly!"
                ),
                "key_concepts": [
                    {
                        "concept": "Biochemical Food Tests",
                        "explanation": "Starch: Iodine turns blue-black. Reducing Sugars: Benedict's/Fehling's turns brick-red. Protein: Biuret reagent turns violet/purple. Fats: Sudan III or grease spot on paper.",
                        "examples": ["A positive Biuret test confirms peptide bonds between amino acids in a protein."]
                    },
                    {
                        "concept": "Fluid Mosaic Membrane Model",
                        "explanation": "Cell membranes comprise a phospholipid bilayer with hydrophilic heads pointing outward and hydrophobic fatty acid tails pointing inward, studded with transport proteins.",
                        "examples": ["Small uncharged molecules (O₂, CO₂) diffuse freely; ions and glucose require protein channels."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing reducing sugars (glucose, maltose) with non-reducing sugars (sucrose). Sucrose requires boiling with dilute acid before yielding a positive Benedict's test."
                ],
                "worked_examples": [
                    {
                        "question": "A sample of food substance boiled with Fehling's solutions A and B produced a brick-red precipitate. This confirms the presence of:",
                        "options": ["A. Reducing sugar (e.g. glucose)", "B. Non-reducing sugar (sucrose)", "C. Starch", "D. Protein"],
                        "solution": "Reduction of copper(II) ions to insoluble copper(I) oxide (brick-red precipitate) by free aldehyde/ketone groups is specific to reducing sugars. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Benedict's and Fehling's tests detect REDUCING sugars; sucrose is non-reducing and requires prior acid hydrolysis.",
                "prepares_for": ["Cellular Biology & Life Processes", "Human Physiology & Systems"]
            },
            {
                "id": "bio_found_2",
                "topic": "Chromosomes & Cell Division Foundations",
                "title": "DNA Architecture, Mitosis, Meiosis & Chromosomal Inheritance",
                "jamb_weight": "Foundational Prerequisite (Essential for Genetics & Evolution)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "The preservation and generational transmission of life depends on cell division. Mitosis produces 2 genetically identical diploid daughter cells for somatic growth and repair. Meiosis produces 4 genetically unique haploid gametes (sperm/egg) through independent assortment and homologous crossing over.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of Mitosis like a photocopying machine: If you put in a 46-page document, you get two exact 46-page copies. Your skin cells use mitosis to heal a cut! "
                    "Think of Meiosis like dealing a deck of cards to make a brand-new game: It splits the 46 pages into two sets of 23, and shuffles the cards (crossing over). "
                    "That is why you look like a unique blend of both your parents, rather than an identical clone of either one!"
                ),
                "key_concepts": [
                    {
                        "concept": "Mitosis vs Meiosis Comparison",
                        "explanation": "Mitosis: 1 division, 2 diploid (2n) cells, zero genetic variation, somatic cells. Meiosis: 2 divisions, 4 haploid (n) cells, massive genetic variation via crossing over, germ cells.",
                        "examples": ["Human somatic cell: 46 chromosomes (2n). Human gamete: 23 chromosomes (n)."]
                    },
                    {
                        "concept": "DNA Complementary Base Pairing",
                        "explanation": "Adenine pairs strictly with Thymine (A=T via 2 hydrogen bonds), and Guanine pairs strictly with Cytosine (G≡C via 3 hydrogen bonds). In RNA, Uracil replaces Thymine.",
                        "examples": ["If a DNA strand has sequence 5'-AGTC-3', the complementary strand is 3'-TCAG-5'."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing chromatids with homologous chromosomes. Crossing over occurs between non-sister chromatids of homologous pairs in Prophase I of meiosis."
                ],
                "worked_examples": [
                    {
                        "question": "If an organism has a diploid chromosome number of 2n = 16, how many chromosomes will be present in its sperm cell?",
                        "options": ["A. 8", "B. 16", "C. 32", "D. 4"],
                        "solution": "Sperm cells are gametes formed through meiosis and contain the haploid (n) number of chromosomes: n = 16 / 2 = 8. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Mitosis creates 2 identical diploid clones; Meiosis creates 4 unique haploid gametes.",
                "prepares_for": ["Genetics & Evolution", "Cellular Biology & Life Processes"]
            }
        ],
        "Economics": [
            {
                "id": "eco_found_1",
                "topic": "Foundational Economic Reasoning",
                "title": "Scarcity, Choice, Opportunity Cost & The Production Possibility Curve",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of Economics)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Economics is the study of how scarce resources with alternative uses are allocated to satisfy unlimited human wants. Every economic decision involves Scarcity -> Choice -> Opportunity Cost. The Production Possibility Curve (PPC) illustrates potential maximum output combinations and the law of increasing opportunity cost.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "You have ₦2,000 in your pocket and 2 hours of free time. You want to watch a movie at the cinema (₦2,000) AND you want to buy a textbook (₦2,000). "
                    "You cannot have both because your money is scarce! You must CHOOSE. "
                    "If you choose the textbook, the enjoyment of the cinema you sacrificed is your Opportunity Cost. All economics is about understanding these real-life trade-offs!"
                ),
                "key_concepts": [
                    {
                        "concept": "The Production Possibility Curve (PPC)",
                        "explanation": "Points ON the frontier represent productive efficiency. Points INSIDE represent inefficiency or underutilized resources. Points OUTSIDE are currently unattainable without economic growth.",
                        "examples": ["A concave PPC bow-shape reflects increasing opportunity cost: shifting resources to guns means sacrificing more and more butter."]
                    },
                    {
                        "concept": "Scale of Preference",
                        "explanation": "A list of unsatisfied human wants arranged in strict order of relative priority or importance, ensuring rational decision-making under resource constraints.",
                        "examples": ["A student prioritizes tuition and books above video games and designer shoes."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing money cost with opportunity cost. Opportunity cost is NOT the cash you paid; it is the alternative goods you gave up!"
                ],
                "worked_examples": [
                    {
                        "question": "A student spends ₦5,000 on a textbook instead of attending a musical concert. The opportunity cost of this decision is:",
                        "options": ["A. The musical concert forgone", "B. The ₦5,000 spent", "C. The textbook acquired", "D. Zero"],
                        "solution": "Opportunity cost is defined strictly as the next best alternative forgone (the musical concert). Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Opportunity cost is the real alternative sacrificed, never the money price paid.",
                "prepares_for": ["Basic Economic Principles & Methodology", "Microeconomics & Price Mechanism"]
            },
            {
                "id": "eco_found_2",
                "topic": "Economic Graphing & Elasticity Foundations",
                "title": "Visualizing Economic Curves, Slopes & Calculating Elasticity Ratios",
                "jamb_weight": "Foundational Prerequisite (Essential for Micro & Macroeconomics)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Economic relationships are analyzed visually using two-dimensional price-quantity graphs. Demand curves slope downward (negative gradient); supply curves slope upward (positive gradient). Calculating percentage changes and elasticity ratios (|%ΔQ / %ΔP|) is fundamental for price policy analysis.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of an elastic band: If you pull it and it stretches easily, it is ELASTIC. "
                    "If a small 10% price increase causes buyers to run away and sales crash by 50%, demand is Elastic (E > 1)! "
                    "If a commodity is essential like life-saving insulin or petrol, people have to buy it even if the price doubles. That demand is INELASTIC (E < 1)!"
                ),
                "key_concepts": [
                    {
                        "concept": "Price Elasticity of Demand (PED) Formula",
                        "explanation": "PED = (% Change in Quantity Demanded) / (% Change in Price) = (ΔQ / Q₁) / (ΔP / P₁).",
                        "examples": ["If price drops by 10% and quantity rises by 20%, PED = 20 / 10 = 2.0 (Elastic)."]
                    },
                    {
                        "concept": "Shifts vs Movements Along Curves",
                        "explanation": "A change in PRICE causes a movement ALONG the curve (change in quantity demanded). A change in NON-PRICE factors (income, tastes, taxes) SHIFTS the entire curve left or right.",
                        "examples": ["An increase in consumer income shifts the normal good demand curve to the right."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing a change in 'quantity demanded' (price change) with a change in 'demand' (curve shift).",
                    "Trap 2: Forgetting that price elasticity is conventionally interpreted as an absolute positive value."
                ],
                "worked_examples": [
                    {
                        "question": "When the price of bread rises from ₦500 to ₦600, demand falls from 1,000 loaves to 700 loaves. What is the price elasticity of demand?",
                        "options": ["A. 1.5 (Elastic)", "B. 0.5 (Inelastic)", "C. 1.0 (Unitary)", "D. 3.0"],
                        "solution": "%ΔP = (600 - 500) / 500 = +20%. %ΔQ = (700 - 1000) / 1000 = -30%. PED = |-30% / +20%| = 1.5. Since PED > 1, demand is elastic. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Price changes cause movements ALONG the curve; non-price factors SHIFT the entire curve.",
                "prepares_for": ["Microeconomics & Price Mechanism", "Macroeconomics & National Income"]
            }
        ],
        "Government": [
            {
                "id": "gov_found_1",
                "topic": "Political Concepts & The State Foundations",
                "title": "The Nature of the State: Power, Authority, Sovereignty & Legitimacy",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of Government)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Government is the agency through which the political will of the state is formulated, expressed, and realized. To understand constitutions and international relations, you must clearly distinguish Power (ability to enforce obedience), Authority (legal right to command), Legitimacy (public recognition of that right), and Sovereignty.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "If an armed robber points a gun at you and takes your wallet, he has POWER (brute force), but zero authority or legitimacy. "
                    "When a uniformed police officer at a checkpoint asks for your driver's license, she has AUTHORITY backed by the law of the state. "
                    "When citizens willingly vote and accept election results, the government enjoys LEGITIMACY. Government cannot survive on guns alone; it needs legitimacy to govern!"
                ),
                "key_concepts": [
                    {
                        "concept": "Essential Characteristics of the State",
                        "explanation": "A state must possess four non-negotiable attributes: Defined Territory, Permanent Population, Organized Government, and Sovereignty.",
                        "examples": ["Sovereignty distinguishes the State from ordinary clubs, provinces, or commercial enterprises."]
                    },
                    {
                        "concept": "Max Weber's Types of Authority",
                        "explanation": "Traditional (customs, hereditary chiefs), Charismatic (exceptional personal magnetism, e.g. Mandela), Legal-Rational (constitutional laws and bureaucratic offices).",
                        "examples": ["Modern democratic civil services operate strictly on legal-rational authority."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing the 'State' (permanent legal entity) with the 'Government' (temporary administrative body that changes with elections).",
                    "Trap 2: Confusing de jure sovereignty (legal right to rule) with de facto sovereignty (actual physical control)."
                ],
                "worked_examples": [
                    {
                        "question": "Which of the following is the defining characteristic that separates the State from all other human associations?",
                        "options": ["A. Sovereignty", "B. Population", "C. Territory", "D. Leadership"],
                        "solution": "Only the State possesses absolute, supreme internal and external legal power (Sovereignty). Other associations have members, territory, and leaders, but lack sovereignty. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: The State is permanent; the Government is temporary; Sovereignty is supreme.",
                "prepares_for": ["Elements of Government & Political Theory", "Nigerian Constitutional Development"]
            },
            {
                "id": "gov_found_2",
                "topic": "Pre-Colonial Heritage Foundations",
                "title": "Pre-Colonial Political Systems in Nigeria: Hausa-Fulani, Yoruba & Igbo Systems",
                "jamb_weight": "Foundational Prerequisite (Essential for Colonial History & Federalism)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Before British colonial intervention, the territories comprising modern Nigeria possessed sophisticated indigenous political institutions: the highly centralized theocratic Hausa-Fulani Emirates, the constitutional monarchy of the Yoruba kingdoms with institutional checks and balances (Oyomesi, Ogboni), and the republican, acephalous village democracies of the Igbo.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of pre-colonial Nigeria like three different models of leadership: "
                    "The Hausa-Fulani had an absolute executive monarch (The Emir) with unquestioned religious and judicial authority. "
                    "The Yoruba had a constitutional king (The Alaafin) checked by a council of seven chiefs (The Oyomesi). If the king abused power, they sent him a calabash of parrot eggs ordering him to commit suicide! "
                    "The Igbo had no king at all ('Igbo enwe eze')! Every adult male met in the village square (Oha-na-eze) to debate and vote democratically."
                ),
                "key_concepts": [
                    {
                        "concept": "Yoruba Checks and Balances System",
                        "explanation": "The Alaafin was checked by the Oyomesi (council of kingmakers headed by the Bashorun), who were in turn checked by the Ogboni secret society.",
                        "examples": ["Rejection by the Oyomesi required the Alaafin to take his own life, preventing despotism."]
                    },
                    {
                        "concept": "Igbo Acephalous Democracy",
                        "explanation": "Decentralized, stateless political structure governed by the Village Assembly (Amala), Age Grades, and Title Holders (Ozo).",
                        "examples": ["Decisions were reached through consensus building, which made British appointed Warrant Chiefs deeply offensive to the population."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing that all pre-colonial Nigerian societies had hereditary monarchies. Igbo societies were decentralized and democratic!",
                    "Trap 2: Forgetting the role of the Ogboni cult in mediating between the Alaafin and the Oyomesi in the Oyo Empire."
                ],
                "worked_examples": [
                    {
                        "question": "In the pre-colonial Oyo empire, which institution had the constitutional authority to reject a tyrannical Alaafin?",
                        "options": ["A. The Oyomesi", "B. The Ogboni", "C. The Are Ona Kakanfo", "D. The Ilari"],
                        "solution": "The Oyomesi (the council of seven supreme noble chiefs led by the Bashorun) had the constitutional mandate to reject an abusive Alaafin. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Oyo had checks and balances; Sokoto was centralized theocracy; Igbo was acephalous direct democracy.",
                "prepares_for": ["Colonial Administration in Nigeria & West Africa", "Nigerian Constitutional Development"]
            }
        ],
        "Literature in English": [
            {
                "id": "lit_found_1",
                "topic": "Literary Genres & Fundamentals",
                "title": "The Three Pillars of Literature: Drama, Prose & Poetry Analysis",
                "jamb_weight": "Foundational Prerequisite (Essential for 100% of Literature)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Literature is imaginative creative writing divided into three broad genres: Drama (dialogue meant for stage performance), Prose (narrative fiction written in paragraphs and chapters), and Poetry (rhythmic verse written in stanzas). Distinguishing structural elements like acts/scenes, chapters, and stanzas is essential.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Think of the 3 genres like three different camera lenses: "
                    "Drama is a live television camera watching actors talk and move right in front of you (Dialogue + Action). "
                    "Prose is a novelist sitting in an armchair whispering an epic story into your ear chapter by chapter. "
                    "Poetry is an acoustic guitar song where every single word, beat, and pause carries heavy emotional electricity!"
                ),
                "key_concepts": [
                    {
                        "concept": "Genre Distinctive Elements",
                        "explanation": "Drama: Script, cast, stage directions, acts, scenes, dramatis personae. Prose: Plot, characters, narrator, paragraphs, chapters. Poetry: Persona, lines, stanzas, meter, rhyme, rhythm.",
                        "examples": ["A poem does NOT have a 'narrator'; it has a 'poetic persona' or 'speaker'."]
                    },
                    {
                        "concept": "Aristotelian Dramatic Structure (Freytag's Pyramid)",
                        "explanation": "Exposition -> Rising Action -> Climax -> Falling Action -> Denouement (Resolution).",
                        "examples": ["The climax is the highest point of psychological tension and turning point for the protagonist."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Referring to the speaker in a poem as the 'author' or 'narrator'. In poetry, it is ALWAYS the 'speaker' or 'persona'!",
                    "Trap 2: Confusing a soliloquy (speaking alone on stage) with a monologue (a long speech spoken to other characters onstage)."
                ],
                "worked_examples": [
                    {
                        "question": "The voice or fictional character created by a poet through which a poem's emotions are expressed is called the:",
                        "options": ["A. Persona (or Speaker)", "B. Narrator", "C. Playwright", "D. Protagonist"],
                        "solution": "In poetry, the speaking voice is strictly termed the 'persona' or 'speaker', which is distinct from the biographical author. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Stories have narrators; plays have characters; poems have personas.",
                "prepares_for": ["Literary Appreciation & Devices", "Drama & Theatrical Techniques", "Poetry & Versification"]
            },
            {
                "id": "lit_found_2",
                "topic": "Figurative Devices & Tropes Foundations",
                "title": "Mastering Metaphors, Irony, Paradox & Figurative Associations",
                "jamb_weight": "Foundational Prerequisite (Essential for Literary Appreciation)",
                "category": "Foundational Prerequisite Masterclass",
                "overview": "Figurative language transcends literal meaning to generate profound aesthetic pleasure, sensory imagery, and psychological resonance. Distinguishing tropes of comparison (metaphor, simile), association (metonymy, synecdoche), and contradiction (paradox, oxymoron) guarantees high scores in JAMB literary appreciation.",
                "from_scratch_guide": (
                    "💡 LEARN FROM SCRATCH:\n"
                    "Literal language says: 'The sun was bright and hot'. Boring! "
                    "Figurative language says: 'The angry sun was a golden hammer beating against our skulls'. Wow! "
                    "Notice that 'simile' always waves a flag saying 'LIKE' or 'AS' ('She was brave like a lion'). "
                    "A 'metaphor' jumps straight in with no flag ('She was a lion in battle'). "
                    "An 'oxymoron' places two contradictory words side-by-side ('a bitter-sweet memory')."
                ),
                "key_concepts": [
                    {
                        "concept": "Paradox vs Oxymoron",
                        "explanation": "Oxymoron: Two opposing words side-by-side ('deafening silence', 'living dead'). Paradox: A whole statement that seems contradictory at first glance but reveals a profound underlying truth ('The child is father of the man').",
                        "examples": ["'Parting is such sweet sorrow' (Oxymoron). 'Those who save their life will lose it' (Paradox)."]
                    },
                    {
                        "concept": "Synecdoche vs Metonymy",
                        "explanation": "Synecdoche uses a physical PART of something to represent the whole ('All hands on deck' => hands represent sailors). Metonymy substitutes an ASSOCIATED symbol or object for the thing itself ('The Crown decided' => crown represents the king/monarchy).",
                        "examples": ["'Fifty sails' for 50 ships (Synecdoche). 'The Pen is mightier than the sword' (Metonymy)."]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing synecdoche (part for whole) with metonymy (symbol/association for whole).",
                    "Trap 2: Confusing verbal irony (saying the opposite of what you mean) with sarcasm (irony used intentionally to hurt or ridicule someone)."
                ],
                "worked_examples": [
                    {
                        "question": "The literary statement 'War is peace, freedom is slavery, ignorance is strength' (George Orwell) is an example of:",
                        "options": ["A. Paradox", "B. Oxymoron", "C. Hyperbole", "D. Onomatopoeia"],
                        "solution": "These are complete contradictory statements that reveal deep totalitarian political commentary (philosophical truth under apparent contradiction). Thus, it is a paradox. Correct Option: A."
                    }
                ],
                "golden_rule": "Golden Rule: Oxymoron is two words paired side-by-side; Paradox is a full contradictory statement conveying truth.",
                "prepares_for": ["Literary Appreciation & Devices", "Poetry & Versification"]
            }
        ]
    }

    # Merge into the ultimate 48-lesson database
    final_lessons = {}
    for subj in base_lessons.keys():
        subj_core = base_lessons[subj]
        
        # Enrich core lessons with prerequisites, from-scratch guides, and CBT drill topics
        enriched_core = []
        for l in subj_core:
            item = dict(l)
            item["category"] = "Core JAMB Syllabus Masterclass"
            item["cbt_drill_topic"] = item["topic"]
            
            # Add prerequisites
            reqs = prerequisite_map.get((subj, item["topic"]), [])
            item["prerequisites"] = reqs
            
            # Add from-scratch guide
            item["from_scratch_guide"] = from_scratch_guide_map.get((subj, item["topic"]), "Master core principles right from scratch.")
            
            enriched_core.append(item)
            
        # Get foundational prerequisite lessons
        subj_found = foundational_modules.get(subj, [])
        for f in subj_found:
            f["cbt_drill_topic"] = f["topic"]
            f["prerequisites"] = []
            
        # Core lessons first, foundational lessons next
        final_lessons[subj] = enriched_core + subj_found

    with open("data/lessons.json", "w", encoding="utf-8") as f:
        json.dump(final_lessons, f, indent=2, ensure_ascii=False)

    print(f"🎉 Successfully built 48 exhaustive masterclasses in data/lessons.json!")
    total = sum(len(ls) for ls in final_lessons.values())
    print(f"Total Lessons: {total} (6 per subject across 8 subjects)")
    for s, ls in final_lessons.items():
        print(f"  • {s:25}: {len(ls)} lessons (4 Core + 2 Foundational Prerequisites)")

if __name__ == "__main__":
    build_scratch_and_prerequisite_curriculum()
