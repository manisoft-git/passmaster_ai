import json

lessons = {
    # ==================== USE OF ENGLISH ====================
    "Use of English": [
        {
            "id": "eng_lesson_1",
            "topic": "Concord & Grammar",
            "title": "Grammatical Concord, Rule of Proximity & Subjunctive Mood",
            "jamb_weight": "25% of English Section (~15 Questions)",
            "overview": "Concord is the formal grammatical agreement between a subject and its verb, or between a pronoun and its antecedent. JAMB examiners deliberately construct sentences with intervening prepositional phrases and correlated conjunctions to trick students into selecting the wrong verb number.",
            "key_concepts": [
                {
                    "concept": "Rule of Proximity (Either... or / Neither... nor / Not only... but also)",
                    "explanation": "When two subjects are joined by 'or', 'nor', or 'but also', the verb agrees ONLY with the subject that is physically closest to it.",
                    "examples": [
                        "Neither the principal nor the teachers WERE present yesterday. ('teachers' is plural and closest)",
                        "Either the players or the coach IS responsible for the strategy. ('coach' is singular and closest)"
                    ]
                },
                {
                    "concept": "Intervening Modifiers & Parenthetical Phrases",
                    "explanation": "Phrases introduced by 'as well as', 'together with', 'in collaboration with', 'no less than', or 'including' do NOT change the number of the subject. The verb agrees strictly with the primary subject.",
                    "examples": [
                        "The governor, together with his commissioners, HAS arrived. ('The governor' is singular)",
                        "The students, as well as the headmaster, ARE attending the seminar."
                    ]
                },
                {
                    "concept": "Relative Clause Antecedent Concord ('One of the [Plural] Who')",
                    "explanation": "In 'one of the [plural noun] who...', the relative pronoun 'who' refers to the plural noun antecedent, so the verb MUST be plural. HOWEVER, if preceded by 'the only one of the...', the verb is singular.",
                    "examples": [
                        "She is one of the candidates who HAVE registered. (Plural 'candidates' => 'have')",
                        "He is the ONLY one of the candidates who HAS registered. (Singular 'only one' => 'has')"
                    ]
                },
                {
                    "concept": "The Mandative Subjunctive Mood",
                    "explanation": "After verbs of command, demand, requirement, or recommendation (demand, insist, recommend, suggest, mandate, urge, decree that...), the verb in the dependent clause remains in its bare infinitive form (no 's' or 'es'), regardless of the subject.",
                    "examples": [
                        "The court decreed that the suspect REMAIN in detention. (NOT remains)",
                        "The doctor recommended that she TAKE the medication daily. (NOT takes)"
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Looking at the first subject instead of the closest subject in 'neither... nor' constructions.",
                "Trap 2: Treating 'together with' or 'as well as' like 'and'. They are prepositions, not conjunctions!",
                "Trap 3: Adding an 's' to subjunctive verbs because the subject is 'he', 'she', or 'it'."
            ],
            "worked_examples": [
                {
                    "question": "Neither the captain nor the sailors _______ able to control the vessel during the ferocious storm.",
                    "options": ["A. was", "B. were", "C. is", "D. has been"],
                    "solution": "Apply the Rule of Proximity. The nearest subject to the blank is 'the sailors' (plural). Because 'during the ferocious storm' marks a past event, the verb must be plural past tense. Correct Option: B (were)."
                }
            ],
            "golden_rule": "In 'Neither/Either/Nor', look immediately to the LEFT of the verb. In 'As well as/Together with', ignore everything between the commas and match the very first noun."
        },
        {
            "id": "eng_lesson_2",
            "topic": "Lexis & Structure",
            "title": "Collocations, Idiomatic Phrasal Verbs & Prepositional Traps",
            "jamb_weight": "30% of English Section (~18 Questions)",
            "overview": "Lexis & Structure tests your knowledge of native English idiom, fixed prepositional collocations, redundancy avoidance, and contextual vocabulary. JAMB examiners specifically prey on Nigerian vernacular errors (e.g. 'night bus', 'travelled out', 'preside on', 'complain about').",
            "key_concepts": [
                {
                    "concept": "Fixed Prepositional Collocations",
                    "explanation": "Certain verbs and adjectives can ONLY pair with specific prepositions. Substituting another preposition constitutes a severe grammatical error.",
                    "examples": [
                        "Preside OVER (not at, not on)",
                        "Congratulate ON (not for)",
                        "Acquit OF (not from)",
                        "Confer ON / UPON (not to)",
                        "Different FROM (not than, in standard British/West African English)"
                    ]
                },
                {
                    "concept": "Redundancy & Tautology Avoidance",
                    "explanation": "JAMB penalizes doubling identical meanings in the same sentence.",
                    "examples": [
                        "Incorrect: 'reverse back' -> Correct: 'reverse'",
                        "Incorrect: 'revert back' -> Correct: 'revert'",
                        "Incorrect: 'repeat again' -> Correct: 'repeat'",
                        "Incorrect: 'blend together' -> Correct: 'blend'"
                    ]
                },
                {
                    "concept": "Idiomatic Expressions & Inverted Meanings",
                    "explanation": "Idioms cannot be interpreted literally. 'To wash one's dirty linen in public' means discussing private disputes publicly; 'To smell a rat' means suspecting foul play.",
                    "examples": [
                        "'Cut the Gordian knot' = Solve a complex dilemma decisively by bold action.",
                        "'To throw down the gauntlet' = Issue a challenge or provocation."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Using 'congratulate for'—in English you congratulate someone ON their achievement.",
                "Trap 2: Saying 'The reason is because...'—the correct grammatical construction is 'The reason is that...'.",
                "Trap 3: Confusing 'uninterested' (bored/apathetic) with 'disinterested' (impartial/unbiased)."
            ],
            "worked_examples": [
                {
                    "question": "The university senate congratulated the young scholar _______ breaking the 40-year academic record.",
                    "options": ["A. for", "B. about", "C. on", "D. with"],
                    "solution": "The verb 'congratulate' takes the fixed preposition 'on'. Correct Option: C (on)."
                }
            ],
            "golden_rule": "Prepositions are mathematical: memorize them as pairs (congratulate on, charge with, acquit of, preside over, reason is that)."
        },
        {
            "id": "eng_lesson_3",
            "topic": "Oral Forms & Phonology",
            "title": "Vowel Length, Silent Consonants & Primary Syllabic Stress",
            "jamb_weight": "20% of English Section (~12 Questions)",
            "overview": "Oral English in JAMB tests phonological awareness: long vs short vowels (/iː/ vs /ɪ/, /uː/ vs /ʊ/), diphthongs, silent consonants (debt, subtle, receipt, aisle), and primary syllabic stress patterns in multisyllabic words.",
            "key_concepts": [
                {
                    "concept": "Silent Consonant Diagnostics",
                    "explanation": "Many English words contain orthographic letters that have zero phonetic representation in standard received pronunciation.",
                    "examples": [
                        "Silent 'b': subtle, debt, doubt, plumber, tomb, womb, limb.",
                        "Silent 'p': receipt, psalm, pneumonia, psyche, raspberry.",
                        "Silent 't': mortgage, castle, whistle, listen, soften, depot.",
                        "Silent 's': aisle, island, debris, rendezvous."
                    ]
                },
                {
                    "concept": "Stress Rules for Suffixes (-tion, -ic, -ity, -phy)",
                    "explanation": "Words ending in '-tion', '-sion', '-ic', '-ity', and '-graphy' have predictable stress rules: stress falls on the syllable IMMEDIATELY PRECEDING the suffix (penultimate or antepenultimate).",
                    "examples": [
                        "pho-TOG-ra-phy (ante-penultimate)",
                        "e-co-NOM-ic (syllable right before -ic)",
                        "na-TION, de-ci-SION (penultimate syllable)",
                        "sin-CER-i-ty (syllable right before -ity)"
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Pronouncing the 'b' in plumber or subtle.",
                "Trap 2: Stressing the first syllable in 'photography' (PHO-to-graphy is wrong; it is pho-TOG-ra-phy).",
                "Trap 3: Confusing noun stress (stress first syllable: CON-vict) with verb stress (stress second syllable: con-VICT)."
            ],
            "worked_examples": [
                {
                    "question": "Which syllable receives the primary stress in the word 'DEMOCRATIC'?",
                    "options": ["A. DE-mo-cra-tic", "B. de-MO-cra-tic", "C. de-mo-CRA-tic", "D. de-mo-cra-TIC"],
                    "solution": "Words ending in '-ic' have primary stress on the syllable immediately preceding the suffix: de-mo-CRA-tic (3rd syllable). Correct Option: C."
                }
            ],
            "golden_rule": "Words ending in -ic, -sion, -tion always stress the syllable right before them. In 2-syllable noun/verb pairs: Nouns stress the FRONT, Verbs stress the BACK (RE-cord vs re-CORD)."
        },
        {
            "id": "eng_lesson_4",
            "topic": "Comprehension & Prescribed Text",
            "title": "Analytical Comprehension & JAMB Prescribed Novel Analysis",
            "jamb_weight": "25% of English Section (~15 Questions)",
            "overview": "Comprehension tests speed reading, deductive reasoning, figurative language detection, and deep familiarity with the prescribed literature text for UTME candidates.",
            "key_concepts": [
                {
                    "concept": "Distinction Between Direct Fact and Logical Inference",
                    "explanation": "Direct questions ask 'what happened according to paragraph 2'. Inference questions ask 'what does the author imply'. Never pick an option just because it uses the author's exact words if it doesn't answer the prompt.",
                    "examples": [
                        "Direct: The text states the experiment took 48 hours.",
                        "Inference: The author's sarcastic tone suggests skepticism towards the findings."
                    ]
                },
                {
                    "concept": "Figures of Speech & Rhetorical Devices",
                    "explanation": "Metaphor (direct comparison without like/as), Hyperbole (deliberate exaggeration), Irony (saying the opposite of what is meant), Oxymoron (adjacent contradictory terms), Synecdoche (part representing whole).",
                    "examples": [
                        "Irony: 'He is as gentle as a charging rhinoceros.'",
                        "Synecdoche: 'Nigeria won the match' (meaning the 11 national football players)."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Bringing outside personal knowledge that isn't stated or deduced in the passage.",
                "Trap 2: Picking literal interpretations of ironic or figurative statements.",
                "Trap 3: Rushing through character relationships in the prescribed novel."
            ],
            "worked_examples": [
                {
                    "question": "'The courtroom was a frozen refrigerator of silent tension.' What figure of speech is demonstrated here?",
                    "options": ["A. Simile", "B. Metaphor", "C. Hyperbole", "D. Personification"],
                    "solution": "Direct identification of the courtroom as a frozen refrigerator without using 'like' or 'as' is a direct metaphor. Correct Option: B."
                }
            ],
            "golden_rule": "The answer to every comprehension question is 100% inside the text. Never guess from outside knowledge."
        }
    ],

    # ==================== MATHEMATICS ====================
    "Mathematics": [
        {
            "id": "mth_lesson_1",
            "topic": "Algebra",
            "title": "Quadratic Roots, Symmetric Functions, Logarithms & Progressions",
            "jamb_weight": "25% of Mathematics Section (~10 Questions)",
            "overview": "Algebra constitutes the bedrock of JAMB Mathematics. Questions frequently combine symmetric functions of roots (α and β), logarithmic change-of-base laws, and Arithmetic/Geometric progressions.",
            "key_concepts": [
                {
                    "concept": "Symmetric Properties of Quadratic Roots",
                    "explanation": "For any quadratic equation ax² + bx + c = 0 with roots α and β: Sum of roots (α + β) = -b/a. Product of roots (αβ) = c/a.",
                    "examples": [
                        "α² + β² = (α + β)² - 2αβ",
                        "1/α + 1/β = (α + β) / αβ",
                        "α³ + β³ = (α + β)³ - 3αβ(α + β)"
                    ]
                },
                {
                    "concept": "Arithmetic & Geometric Progressions (AP & GP)",
                    "explanation": "AP nth term: T_n = a + (n-1)d. Sum of n terms: S_n = n/2[2a + (n-1)d]. GP nth term: T_n = ar^(n-1). Sum to infinity (for |r| < 1): S_inf = a / (1 - r).",
                    "examples": [
                        "If T₄ = 15 and T₉ = 35 in AP => 5d = 20 => d = 4, a = 3."
                    ]
                },
                {
                    "concept": "Logarithmic Laws & Change of Base",
                    "explanation": "log_b(A) = log_k(A) / log_k(b). Also: log_a(x) + log_a(y) = log_a(xy), log_a(x) - log_a(y) = log_a(x/y), log_a(x^p) = p log_a(x).",
                    "examples": [
                        "If log₁₀(2) = 0.3010, then log₁₀(5) = log₁₀(10/2) = log₁₀(10) - log₁₀(2) = 1 - 0.3010 = 0.6990."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Forgetting the minus sign in the sum of roots: α + β = -b/a, NOT +b/a!",
                "Trap 2: Assuming α² + β² = (α + β)² without subtracting 2αβ.",
                "Trap 3: Applying S_inf when the common ratio r >= 1 (divergent series)."
            ],
            "worked_examples": [
                {
                    "question": "If α and β are the roots of 2x² - 6x + 3 = 0, find α² + β².",
                    "options": ["A. 6", "B. 9", "C. 3/2", "D. 12"],
                    "solution": "a = 2, b = -6, c = 3. α + β = -(-6)/2 = 3. αβ = 3/2. α² + β² = (α + β)² - 2αβ = (3)² - 2(3/2) = 9 - 3 = 6. Correct Option: A."
                }
            ],
            "golden_rule": "Always memorize the identity: α² + β² = (α + β)² - 2αβ. In logs: log(5) is always 1 - log(2)."
        },
        {
            "id": "mth_lesson_2",
            "topic": "Calculus",
            "title": "Differential Calculus, Chain Rule, Maxima/Minima & Definite Integrals",
            "jamb_weight": "25% of Mathematics Section (~10 Questions)",
            "overview": "Calculus questions in JAMB test procedural speed. Candidates must instantly apply the Chain Rule, Product/Quotient rules, evaluate turning points (dy/dx = 0), and integrate by substitution.",
            "key_concepts": [
                {
                    "concept": "The Chain Rule (Function of a Function)",
                    "explanation": "If y = [u(x)]^n, then dy/dx = n[u(x)]^(n-1) × du/dx. You MUST differentiate the inside function and multiply!",
                    "examples": [
                        "y = (3x² - 5)⁴ => dy/dx = 4(3x² - 5)³ × (6x) = 24x(3x² - 5)³."
                    ]
                },
                {
                    "concept": "Turning Points, Maxima & Minima",
                    "explanation": "At a stationary point, dy/dx = 0. To classify: If d²y/dx² < 0, it is a LOCAL MAXIMUM. If d²y/dx² > 0, it is a LOCAL MINIMUM. If d²y/dx² = 0, check higher derivatives (point of inflection).",
                    "examples": [
                        "For a curve y = 2x³ - 9x² + 12x: dy/dx = 6x² - 18x + 12 = 0 => x² - 3x + 2 = 0 => x = 1 or x = 2."
                    ]
                },
                {
                    "concept": "Definite Integration & Area Under Curves",
                    "explanation": "∫ [a to b] f(x) dx = F(b) - F(a). Constant of integration 'C' cancels out in definite integrals.",
                    "examples": [
                        "∫ [0 to 2] (3x² + 2x) dx = [x³ + x²] from 0 to 2 = (8 + 4) - 0 = 12."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Forgetting to multiply by the internal derivative (du/dx) when applying the chain rule.",
                "Trap 2: Confusing the second derivative test: d²y/dx² < 0 means MAXIMUM (concave down), NOT minimum!",
                "Trap 3: Forgetting limits when substituting u in definite integrals."
            ],
            "worked_examples": [
                {
                    "question": "Find the derivative dy/dx if y = (3x² - 5)⁴.",
                    "options": ["A. 12x(3x² - 5)³", "B. 24x(3x² - 5)³", "C. 4(3x² - 5)³", "D. 6x(3x² - 5)⁴"],
                    "solution": "Let u = 3x² - 5. du/dx = 6x. y = u⁴ => dy/du = 4u³. By Chain Rule: dy/dx = dy/du × du/dx = 4(3x² - 5)³ × 6x = 24x(3x² - 5)³. Correct Option: B."
                }
            ],
            "golden_rule": "Inside times outside: Never leave the inner derivative behind in the Chain Rule. Second derivative < 0 is Maxima!"
        },
        {
            "id": "mth_lesson_3",
            "topic": "Geometry & Trigonometry",
            "title": "Circle Theorems, Trigonometric Identities & Coordinate Geometry",
            "jamb_weight": "25% of Mathematics Section (~10 Questions)",
            "overview": "Geometry in JAMB features cyclic quadrilaterals, angle at center vs circumference, alternate segment theorem, and trigonometric identities: sin²θ + cos²θ = 1, tanθ = sinθ/cosθ.",
            "key_concepts": [
                {
                    "concept": "Key Circle Theorems",
                    "explanation": "1. Angle at center = 2 × angle at circumference standing on the same arc. 2. Angles in the same segment are equal. 3. Opposite angles of a cyclic quadrilateral sum to 180°. 4. Angle between tangent and chord = angle in alternate segment.",
                    "examples": [
                        "If angle at center is 110°, angle at circumference subtended by same arc = 55°.",
                        "In cyclic quadrilateral ABCD, if ∠A = 75°, then opposite ∠C = 180° - 75° = 105°."
                    ]
                },
                {
                    "concept": "Coordinate Geometry: Parallel & Perpendicular Lines",
                    "explanation": "Gradient m = (y₂ - y₁) / (x₂ - x₁). For two parallel lines: m₁ = m₂. For two perpendicular lines: m₁ × m₂ = -1 (m₂ = -1/m₁).",
                    "examples": [
                        "A line perpendicular to 2x - 3y = 6 has gradient -3/2."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Confusing opposite angles of a cyclic quadrilateral (sum = 180°) with adjacent angles.",
                "Trap 2: Forgetting the negative reciprocal rule for perpendicular gradients (m₁m₂ = -1).",
                "Trap 3: Misreading bearing angles (Bearings MUST be 3 digits measured clockwise from North: 045°, 210°)."
            ],
            "worked_examples": [
                {
                    "question": "If line L₁ has equation 3x + 2y = 8, what is the gradient of a line L₂ perpendicular to L₁?",
                    "options": ["A. -3/2", "B. 2/3", "C. -2/3", "D. 3/2"],
                    "solution": "3x + 2y = 8 => 2y = -3x + 8 => y = (-3/2)x + 4. So m₁ = -3/2. For perpendicular line: m₂ = -1 / (-3/2) = +2/3. Correct Option: B."
                }
            ],
            "golden_rule": "Opposite angles in cyclic quad sum to 180°. Perpendicular gradient is 'flip it and switch the sign'."
        },
        {
            "id": "mth_lesson_4",
            "topic": "Statistics & Probability",
            "title": "Permutations, Combinations, Probability Laws & Standard Deviation",
            "jamb_weight": "25% of Mathematics Section (~10 Questions)",
            "overview": "Tests counting techniques: nPr = n! / (n-r)! (when order matters) vs nCr = n! / [r!(n-r)!] (selection where order does not matter), mutually exclusive vs independent probabilities, and variance/standard deviation.",
            "key_concepts": [
                {
                    "concept": "Permutations vs Combinations",
                    "explanation": "Use Permutations (nPr) when order or position matters (e.g. electing President, Secretary; arranging digits). Use Combinations (nCr) when selecting a group where order is irrelevant (e.g. committee, selecting 3 books).",
                    "examples": [
                        "Choosing 3 from 7: 7C3 = (7 × 6 × 5) / (3 × 2 × 1) = 35 ways.",
                        "Arranging letters in 'COMMITTEE': 9! / (2! 2! 2!) ways."
                    ]
                },
                {
                    "concept": "Independent vs Mutually Exclusive Events",
                    "explanation": "Independent: P(A ∩ B) = P(A) × P(B). Mutually Exclusive (cannot happen together): P(A ∪ B) = P(A) + P(B). At least one: P(at least 1) = 1 - P(none).",
                    "examples": [
                        "Throwing two dice: P(getting two 6s) = 1/6 × 1/6 = 1/36."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Using permutations when selecting a committee (order does not matter => combination).",
                "Trap 2: Adding probabilities for independent simultaneous events instead of multiplying.",
                "Trap 3: Forgetting that Standard Deviation = √(Variance)."
            ],
            "worked_examples": [
                {
                    "question": "In how many ways can a committee of 3 students be selected from a class of 8 students?",
                    "options": ["A. 24", "B. 56", "C. 336", "D. 512"],
                    "solution": "Selection where order does not matter is a combination: 8C3 = (8 × 7 × 6) / (3 × 2 × 1) = 56. Correct Option: B."
                }
            ],
            "golden_rule": "'Arrangement/Positions' = Permutation. 'Selection/Committee/Group' = Combination. 'At least one' = 1 - P(none)."
        }
    ],

    # ==================== PHYSICS ====================
    "Physics": [
        {
            "id": "phy_lesson_1",
            "topic": "Mechanics",
            "title": "Newton's Laws, Projectiles, Gravitation & Simple Harmonic Motion",
            "jamb_weight": "30% of Physics Section (~12 Questions)",
            "overview": "Mechanics represents the highest-yield topic in JAMB Physics. Master horizontal/vertical components of projectiles, conservation of linear momentum, centripetal force (mv²/r), and Newton's Universal Law of Gravitation.",
            "key_concepts": [
                {
                    "concept": "Projectile Trajectory Formulas",
                    "explanation": "For an object projected with velocity u at angle θ: Time of Flight T = (2u sinθ)/g. Maximum Height H = (u² sin²θ)/(2g). Range R = (u² sin2θ)/g. Maximum range occurs at θ = 45° where R_max = u²/g.",
                    "examples": [
                        "At peak of trajectory, vertical velocity v_y = 0, but horizontal velocity v_x = u cosθ remains CONSTANT!"
                    ]
                },
                {
                    "concept": "Newton's Gravitational Inverse-Square Law",
                    "explanation": "F = G(m₁m₂)/r². Gravitational field strength g = GM/r². Since g ∝ 1/r², doubling distance from Earth's center reduces g by a factor of 4 (1/2² = 1/4)!",
                    "examples": [
                        "At height h = R (distance = 2R from center), weight becomes W/4."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Thinking projectile acceleration at peak height is zero (acceleration due to gravity g is ALWAYS 9.8 or 10 m/s² downwards!).",
                "Trap 2: Measuring distance from Earth's surface instead of Earth's center in gravitational calculations.",
                "Trap 3: Forgetting vector signs in momentum: momentum is conserved as vectors (m₁u₁ + m₂u₂ = m₁v₁ + m₂v₂)."
            ],
            "worked_examples": [
                {
                    "question": "A body of mass 60 kg on Earth's surface is taken to a height equal to the Earth's radius (R). What is its new weight? (Take g = 10 m/s² on surface)",
                    "options": ["A. 600 N", "B. 300 N", "C. 150 N", "D. 0 N"],
                    "solution": "Distance from Earth's center is r = R + R = 2R. Weight W ∝ 1/r². So W_new = W_surface / (2)² = (60 × 10) / 4 = 600 / 4 = 150 N. Correct Option: C."
                }
            ],
            "golden_rule": "At distance 2R from center, gravity drops to 1/4. In projectiles, horizontal velocity NEVER changes (a_x = 0)."
        },
        {
            "id": "phy_lesson_2",
            "topic": "Thermal Physics & Waves",
            "title": "Gas Laws, Heat Capacities, Wave Optics & Sound Resonance",
            "jamb_weight": "25% of Physics Section (~10 Questions)",
            "overview": "Focuses on absolute temperature (Kelvin), specific heat capacity (Q = mcΔθ), latent heat (Q = mL), Snell's law (n = sin i / sin r), and resonance in closed/open acoustic pipes.",
            "key_concepts": [
                {
                    "concept": "The Fatal Gas Law Kelvin Trap",
                    "explanation": "In ALL gas law equations (P₁V₁/T₁ = P₂V₂/T₂), temperature MUST be converted to Kelvin: T(K) = θ(°C) + 273. Doubling temperature in Celsius does NOT double the volume!",
                    "examples": [
                        "27°C = 300 K; 127°C = 400 K (Ratio is 4/3, NOT 127/27!)."
                    ]
                },
                {
                    "concept": "Acoustic Resonance in Organ Pipes",
                    "explanation": "Closed pipe (closed at one end): Only ODD harmonics exist (f₁, 3f₁, 5f₁...). Fundamental λ₁ = 4L => f₁ = v / (4L). Open pipe (open at both ends): ALL harmonics exist (f₁, 2f₁, 3f₁...). Fundamental λ₁ = 2L => f₁ = v / (2L).",
                    "examples": [
                        "An open pipe is richer in harmonics and has double the fundamental frequency of a closed pipe of identical length."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Substituting Celsius directly into Charles's or Ideal Gas Law.",
                "Trap 2: Assuming closed acoustic pipes produce even harmonics (2nd, 4th harmonics are physically impossible in closed pipes!).",
                "Trap 3: Confusing specific heat capacity (mc) with heat capacity (C = Q/Δθ)."
            ],
            "worked_examples": [
                {
                    "question": "A fixed mass of gas occupies 500 cm³ at 27°C. If the pressure remains constant, what is its volume at 127°C?",
                    "options": ["A. 1000 cm³", "B. 666.7 cm³", "C. 2351.8 cm³", "D. 375 cm³"],
                    "solution": "Convert to Kelvin: T₁ = 27 + 273 = 300 K; T₂ = 127 + 273 = 400 K. Charles's Law: V₁/T₁ = V₂/T₂ => 500/300 = V₂/400 => V₂ = (500 × 400)/300 = 666.7 cm³. Correct Option: B."
                }
            ],
            "golden_rule": "Celsius is forbidden in gas formulas: Add 273 immediately. Closed pipe = 4L (odd harmonics only)."
        },
        {
            "id": "phy_lesson_3",
            "topic": "Electricity & Magnetism",
            "title": "Ohm's Law, Circuit Analysis, Internal Resistance & Electromagnetic Induction",
            "jamb_weight": "25% of Physics Section (~10 Questions)",
            "overview": "Deals with EMF and terminal p.d. (E = V + Ir = I(R + r)), series vs parallel resistor/capacitor combinations, Faraday's & Lenz's laws of induction, and transformer equations (Vp/Vs = Np/Ns = Is/Ip).",
            "key_concepts": [
                {
                    "concept": "EMF vs Terminal Potential Difference",
                    "explanation": "E = I(R + r). When a cell supplies current, the terminal p.d. V = E - Ir is ALWAYS less than the open-circuit EMF due to lost volts (Ir) across the cell's internal resistance.",
                    "examples": [
                        "If E = 2.0 V, r = 0.5 Ω, and external R = 4.5 Ω: I = 2.0 / (4.5 + 0.5) = 0.4 A. Terminal p.d. V = 0.4 × 4.5 = 1.8 V (0.2 V lost internally)."
                    ]
                },
                {
                    "concept": "Resistor vs Capacitor Combination Inversion",
                    "explanation": "Resistors in Series: R_total = R₁ + R₂. Resistors in Parallel: 1/R_total = 1/R₁ + 1/R₂. CAPACITORS ARE INVERTED! Capacitors in Parallel: C_total = C₁ + C₂. Capacitors in Series: 1/C_total = 1/C₁ + 1/C₂.",
                    "examples": [
                        "Two 4 μF capacitors in series yield (4 × 4)/(4 + 4) = 2 μF!"
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Applying the resistor series formula to capacitors (Capacitors in series add reciprocally!).",
                "Trap 2: Forgetting internal resistance r when calculating total circuit current.",
                "Trap 3: Inverting transformer current ratio: Vp/Vs = Is/Ip (Voltage and Current are inverse in ideal transformers)."
            ],
            "worked_examples": [
                {
                    "question": "A cell of EMF 1.5 V and internal resistance 1.0 Ω is connected across a 4.0 Ω resistor. Calculate the terminal p.d. across the resistor.",
                    "options": ["A. 1.5 V", "B. 1.2 V", "C. 0.3 V", "D. 0.8 V"],
                    "solution": "Total resistance R_total = R + r = 4.0 + 1.0 = 5.0 Ω. Circuit current I = E / R_total = 1.5 / 5.0 = 0.3 A. Terminal p.d. V = I × R = 0.3 × 4.0 = 1.2 V. Correct Option: B."
                }
            ],
            "golden_rule": "Capacitors behave the EXACT OPPOSITE of resistors in series and parallel. Terminal p.d. is always EMF minus Ir."
        },
        {
            "id": "phy_lesson_4",
            "topic": "Modern & Atomic Physics",
            "title": "Photoelectric Effect, Half-Life Decay, De Broglie Wavelength & Nuclear Reactions",
            "jamb_weight": "20% of Physics Section (~8 Questions)",
            "overview": "Covers Einstein's Photoelectric Equation (E = hf = W₀ + K.E._max), photon energy, radioactive decay half-life (N = N₀(1/2)^n), and alpha/beta/gamma emission balances.",
            "key_concepts": [
                {
                    "concept": "Einstein's Photoelectric Equation & Threshold Frequency",
                    "explanation": "hf = hf₀ + 1/2 m v²_max. Photoelectrons are emitted ONLY if incident frequency f >= threshold frequency f₀. Increasing light intensity increases the NUMBER of photoelectrons emitted per second, but does NOT increase their kinetic energy!",
                    "examples": [
                        "To increase kinetic energy of photoelectrons, increase the FREQUENCY (or decrease wavelength) of incident radiation."
                    ]
                },
                {
                    "concept": "Half-Life Decay Progression",
                    "explanation": "Remaining fraction after n half-lives is (1/2)^n, where n = total time elapsed / half-life period T_1/2.",
                    "examples": [
                        "If half-life is 5 days, after 20 days (4 half-lives), remaining mass = (1/2)⁴ = 1/16 of original."
                    ]
                }
            ],
            "fatal_traps": [
                "Trap 1: Believing that increasing light intensity gives photoelectrons more speed (Intensity increases count; Frequency increases energy!).",
                "Trap 2: Forgetting that beta emission increases the atomic number Z by 1 while mass number A remains unchanged.",
                "Trap 3: Forgetting to convert electron-volts (eV) to Joules (1 eV = 1.6 × 10⁻¹⁹ J)."
            ],
            "worked_examples": [
                {
                    "question": "A radioactive sample has a half-life of 4 hours. If its initial mass is 64 g, what mass remains after 16 hours?",
                    "options": ["A. 16 g", "B. 8 g", "C. 4 g", "D. 2 g"],
                    "solution": "Number of half-lives n = 16 / 4 = 4. Remaining mass = 64 × (1/2)⁴ = 64 / 16 = 4 g. Correct Option: C."
                }
            ],
            "golden_rule": "Light Intensity = Number of electrons. Light Frequency = Kinetic Energy of electrons. Half-life cuts remaining by half every cycle."
        }
    ]
}

# Add concise master lessons for Chemistry, Biology, Economics, Government, Literature
other_subjects = {
    "Chemistry": [
        ("Physical & General Chemistry", "Gas Laws, Mole Concept, Chemical Equilibrium & Le Chatelier's Principle", "25%"),
        ("Inorganic Chemistry", "Periodic Trends, Transition Metals, Halogens & Extraction of Metallurgy", "25%"),
        ("Organic Chemistry", "IUPAC Nomenclature, Isomerism, Hydrocarbons, Alkanols & Esterification", "30%"),
        ("Environmental & Industrial Chemistry", "Water Hardness, Pollution, Haber & Contact Processes, Electrochemistry", "20%")
    ],
    "Biology": [
        ("Cellular Biology & Life Processes", "Cell Organelles, Osmosis, Plasmolysis & Enzyme Catalysis", "25%"),
        ("Human Physiology & Systems", "Circulation, Excretion (Nephron), Nervous Coordination & Digestion", "30%"),
        ("Genetics & Evolution", "Mendelian Monohybrid/Dihybrid Crosses, Sex-linked Traits & Darwinian Natural Selection", "25%"),
        ("Ecology & Environment", "Biomes, Food Webs, Nutrient Cycles (Nitrogen/Carbon) & Population Dynamics", "20%")
    ],
    "Economics": [
        ("Basic Economic Principles & Methodology", "Scarcity, Choice, Opportunity Cost & Production Possibility Curve (PPC)", "25%"),
        ("Microeconomics & Price Mechanism", "Elasticity of Demand & Supply, Price Ceilings, Consumer Surplus & Market Structures", "30%"),
        ("Macroeconomics & National Income", "GDP, GNP, Multiplier Effect, Inflation Types & Monetary Policy Instruments", "25%"),
        ("Money, Banking & Public Finance", "Central Bank Functions, Commercial Bank Credit Creation, Taxation Principles & Public Debt", "20%")
    ],
    "Government": [
        ("Elements of Government & Political Theory", "Sovereignty, Rule of Law, Separation of Powers, Parliamentary vs Presidential Systems", "25%"),
        ("Colonial Administration in Nigeria & West Africa", "Indirect Rule in Northern vs Eastern Nigeria, Warrant Chiefs & Assimilation Policy", "25%"),
        ("Nigerian Constitutional Development", "Clifford (1922), Richards (1946), Macpherson (1951), Lyttelton (1954), 1963 & 1979 Constitutions", "30%"),
        ("Federalism, Military Rule & Foreign Policy", "Revenue Allocation, Creation of States, Military Decrees & Nigeria's Afrocentric Foreign Policy", "20%")
    ],
    "Literature in English": [
        ("Literary Appreciation & Devices", "Dramatic Irony, Catharsis, Anagnorisis, Metaphor, Synecdoche & Rhyme Schemes", "25%"),
        ("Drama & Theatrical Techniques", "Tragedy vs Comedy, Soliloquy, Aside, Stage Directions & Hamartia", "25%"),
        ("Poetry & Versification", "Stanzaic Forms, Meter (Iambic Pentameter), Free Verse, Enjambment & Tone", "25%"),
        ("Prose & Fictional Techniques", "Narrative Point of View, Characterization, Thematic Development & Prescribed African Prose", "25%")
    ]
}

for subj, topics in other_subjects.items():
    lessons[subj] = []
    for idx, (top, title, weight) in enumerate(topics):
        lessons[subj].append({
            "id": f"{subj[:3].lower()}_lesson_{idx+1}",
            "topic": top,
            "title": f"Mastering {title} in JAMB",
            "jamb_weight": f"{weight} of {subj} Section",
            "overview": f"Comprehensive masterclass on {top}. This topic accounts for roughly {weight} of your raw JAMB score. Mastering these concepts prevents fatal cognitive trap selection.",
            "key_concepts": [
                {
                    "concept": f"First Principles of {top}",
                    "explanation": f"Examiners rigorously evaluate conceptual accuracy in {title}. Focus on theoretical definitions, underlying mechanisms, and common exam distinctions.",
                    "examples": [
                        f"Core axiom: Understand cause-and-effect relationships rather than memorizing surface keywords.",
                        f"Examiner perspective: Pay close attention to exceptions to general rules."
                    ]
                },
                {
                    "concept": f"Analytical Problem Solving in {top}",
                    "explanation": "Systematic breakdown of typical quantitative or structural question formats.",
                    "examples": [
                        "Always identify given parameters before selecting the applicable theorem or formula."
                    ]
                }
            ],
            "fatal_traps": [
                f"Trap 1: Confusing foundational definitions with closely related colloquial terms in {top}.",
                "Trap 2: Failing to account for environmental or boundary conditions specified in the question stem.",
                "Trap 3: Rushing calculations or skipping the step of unit verification."
            ],
            "worked_examples": [
                {
                    "question": f"A standard JAMB examination question testing {top}.",
                    "options": ["A. Distractor 1", "B. Correct Option", "C. Distractor 2", "D. Distractor 3"],
                    "solution": f"Apply the foundational theorem of {top}. Option B is the only logically and scientifically consistent choice."
                }
            ],
            "golden_rule": f"Master the underlying first principles of {top} and you will eliminate 3 out of 4 options in under 15 seconds."
        })

with open("data/lessons.json", "w", encoding="utf-8") as f:
    json.dump(lessons, f, indent=2)

print(f"Successfully generated data/lessons.json with {sum(len(v) for v in lessons.values())} topic lessons across {len(lessons)} subjects.")
