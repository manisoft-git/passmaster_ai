import json
import os

def build_all_lessons():
    lessons = {
        # ==================== 1. USE OF ENGLISH ====================
        "Use of English": [
            {
                "id": "eng_lesson_1",
                "topic": "Concord & Grammar",
                "title": "Grammatical Concord, Rule of Proximity & Subjunctive Mood",
                "jamb_weight": "25% of English Section (~15 Questions)",
                "overview": "Concord is the formal grammatical agreement between a subject and its verb, or between a pronoun and its antecedent. JAMB examiners deliberately construct sentences with intervening prepositional phrases, correlative conjunctions, and indefinite pronouns to trick students into selecting the wrong verb number.",
                "key_concepts": [
                    {
                        "concept": "Rule of Proximity (Either... or / Neither... nor / Not only... but also)",
                        "explanation": "When two subjects are joined by correlatives ('or', 'nor', 'but also'), the verb agrees ONLY with the subject physically closest to it, completely ignoring the earlier noun.",
                        "examples": [
                            "Neither the principal nor the teachers WERE present yesterday. ('teachers' is plural and closest)",
                            "Either the players or the coach IS responsible for the strategy. ('coach' is singular and closest)",
                            "Not only the senator but also his aides HAVE arrived. ('aides' is plural and adjacent to verb)"
                        ]
                    },
                    {
                        "concept": "Intervening Modifiers & Parenthetical Phrases",
                        "explanation": "Phrases introduced by 'as well as', 'together with', 'in collaboration with', 'no less than', 'accompanied by', or 'including' are prepositional adjuncts, NOT coordinating conjunctions. They do NOT change the number of the subject. The verb agrees strictly with the primary subject before the commas.",
                        "examples": [
                            "The governor, together with his commissioners, HAS arrived. ('The governor' is the sole subject)",
                            "The students, as well as the headmaster, ARE attending the national symposium."
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
                        "explanation": "After verbs of command, demand, recommendation, or decree (demand, insist, recommend, suggest, mandate, urge, decree that...), the verb in the dependent clause remains in its bare infinitive form (no 's', 'es', or past inflection), regardless of whether the subject is he/she/it.",
                        "examples": [
                            "The court decreed that the suspect REMAIN in detention. (NOT remains)",
                            "The doctor recommended that she TAKE the medication daily. (NOT takes)",
                            "The constitution demands that every citizen BE treated with dignity. (NOT is)"
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Looking at the first subject instead of the closest subject in 'neither... nor' and 'either... or' constructions.",
                    "Trap 2: Treating 'together with' or 'as well as' like 'and'. They are parenthetical prepositions, not conjunctions!",
                    "Trap 3: Adding an 's' to subjunctive verbs because the subject is 'he', 'she', or 'it'.",
                    "Trap 4: Treating indefinite pronouns like 'everyone', 'somebody', 'each of' as plural. They take singular verbs!"
                ],
                "worked_examples": [
                    {
                        "question": "Neither the captain nor the sailors _______ able to control the vessel during the ferocious storm.",
                        "options": ["A. was", "B. were", "C. is", "D. has been"],
                        "solution": "Apply the Rule of Proximity. The nearest subject to the blank is 'the sailors' (plural). Because 'during the ferocious storm' marks a completed past event, the verb must be plural past tense. Correct Option: B (were)."
                    }
                ],
                "golden_rule": "In 'Neither/Either/Nor', look immediately to the LEFT of the verb. In 'As well as/Together with', ignore everything between the commas and match the very first noun."
            },
            {
                "id": "eng_lesson_2",
                "topic": "Lexis & Structure",
                "title": "Collocations, Idiomatic Phrasal Verbs & Prepositional Traps",
                "jamb_weight": "30% of English Section (~18 Questions)",
                "overview": "Lexis & Structure tests your command of native English idiom, fixed prepositional collocations, redundancy avoidance, and contextual vocabulary. JAMB examiners specifically prey on Nigerian vernacular interference errors.",
                "key_concepts": [
                    {
                        "concept": "Fixed Prepositional Collocations",
                        "explanation": "Certain verbs and adjectives can ONLY pair with specific prepositions. Substituting another preposition constitutes a severe grammatical error in standard English.",
                        "examples": [
                            "Preside OVER (not at, not on)",
                            "Congratulate ON (not for)",
                            "Acquit OF (not from)",
                            "Confer ON / UPON (to bestow an honor - contrast with 'confer with' meaning to consult)",
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
                        "explanation": "Idioms cannot be interpreted literally. 'To wash one's dirty linen in public' means discussing private disputes publicly; 'To throw down the gauntlet' means issuing a formal challenge.",
                        "examples": [
                            "'Cut the Gordian knot' = Solve a complex dilemma decisively by bold action.",
                            "'Bite the bullet' = Endure an inevitable painful situation with courage."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Using 'congratulate for'—in standard English you congratulate someone ON their achievement.",
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
                        "concept": "Stress Rules for Suffixes (-tion, -ic, -ity, -graphy)",
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
                "golden_rule": "Words ending in -ic, -tion, -sion place primary stress on the syllable IMMEDIATELY BEFORE the suffix."
            },
            {
                "id": "eng_lesson_4",
                "topic": "Comprehension & Prescribed Text",
                "title": "Analytical Comprehension & JAMB Prescribed Novel Analysis",
                "jamb_weight": "25% of English Section (~15 Questions)",
                "overview": "Mastering tone, mood, authorial intent, figurative language in reading passages, and in-depth character and plot dissection of the current JAMB prescribed novel ('The Life Changer' by Khadija Abubakar Jalli).",
                "key_concepts": [
                    {
                        "concept": "Core Themes of 'The Life Changer'",
                        "explanation": "The novel examines the transition from sheltered secondary school life to university autonomy. Major motifs: parental guidance vs peer pressure, campus deception (Habib, Jack, and Salma), moral steadfastness (Ummi, Bintu, Omar), and the redemptive power of truth.",
                        "examples": [
                            "Salma's downfall: Arrogance and superficial sophistication lead to academic dishonesty and expulsion.",
                            "Talle's redemption: The quiet man who fell into complicity with kidnappers, demonstrating that naivety can be as dangerous as malice."
                        ]
                    },
                    {
                        "concept": "Comprehension Question Decoding",
                        "explanation": "Distinguish between explicit factual recall, implicit thematic inference, and tone/attitude identification (critical, satirical, eulogistic, objective, cynical).",
                        "examples": [
                            "When asked for the 'author's attitude', locate evaluative adjectives and adverbs.",
                            "Inference questions require deducing unstated truths from premise evidence."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Picking an option that is true in real life but NOT stated or supported in the reading passage.",
                    "Trap 2: Confusing characters in the prescribed novel (e.g. confusing Habib with Kabir, or Salma with Tomiwa).",
                    "Trap 3: Confusing 'tone' (author's attitude) with 'mood' (reader's emotional atmosphere)."
                ],
                "worked_examples": [
                    {
                        "question": "In 'The Life Changer', what primary factor led to Salma's initial refusal to respect the university dress code?",
                        "options": ["A. Ignorance of institutional regulations", "B. A desire to display financial affluence and superior modern sophistication", "C. Financial inability to purchase prescribed attire", "D. Influence from her roommate Tomiwa"],
                        "solution": "Salma believed herself to be more worldly and sophisticated than her peers and lecturers, displaying arrogance until humbled by consequences. Correct Option: B."
                    }
                ],
                "golden_rule": "Never bring outside assumptions into comprehension questions—the answer exists ONLY between the passage's lines."
            }
        ],

        # ==================== 2. MATHEMATICS ====================
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
                            "If T₄ = 15 and T₉ = 35 in AP => 5d = 20 => d = 4, a = 3.",
                            "For GP with a = 6, r = 1/3: S_inf = 6 / (1 - 1/3) = 6 / (2/3) = 9."
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
                        "explanation": "At a stationary point, dy/dx = 0. To classify: If d²y/dx² < 0, it is a LOCAL MAXIMUM. If d²y/dx² > 0, it is a LOCAL MINIMUM. If d²y/dx² = 0, check higher derivatives.",
                        "examples": [
                            "For a curve y = 2x³ - 9x² + 12x: dy/dx = 6x² - 18x + 12 = 0 => x² - 3x + 2 = 0 => x = 1 or x = 2."
                        ]
                    },
                    {
                        "concept": "Definite Integration & Area Under Curves",
                        "explanation": "∫ [a to b] f(x) dx = F(b) - F(a). The arbitrary constant 'C' cancels out in definite integrals.",
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
                            "Line perpendicular to 2x - 4y = 7: Gradient of given line = 1/2. Perpendicular gradient = -2."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Assuming opposite angles of a cyclic quad are equal (they sum to 180°, NOT equal!).",
                    "Trap 2: Forgetting the negative reciprocal for perpendicular lines (m₂ = -1/m₁).",
                    "Trap 3: Mixing up sine rule (a/sinA = b/sinB) with cosine rule (a² = b² + c² - 2bc cosA)."
                ],
                "worked_examples": [
                    {
                        "question": "Find the gradient of a straight line perpendicular to the line 3x + 6y = 10.",
                        "options": ["A. -1/2", "B. 2", "C. -2", "D. 1/2"],
                        "solution": "Rearrange to y = mx + c: 6y = -3x + 10 => y = -1/2x + 5/3. m₁ = -1/2. For perpendicular line: m₁ × m₂ = -1 => (-1/2) × m₂ = -1 => m₂ = 2. Correct Option: B."
                    }
                ],
                "golden_rule": "Opposite angles of cyclic quad SUM to 180°. Perpendicular gradient is negative reciprocal."
            },
            {
                "id": "mth_lesson_4",
                "topic": "Statistics & Probability",
                "title": "Permutations, Combinations, Probability Laws & Standard Deviation",
                "jamb_weight": "25% of Mathematics Section (~10 Questions)",
                "overview": "Mastering counting principles: nPr (order matters) vs nCr (selection without order), mutually exclusive vs independent events, and dispersion measures (variance, standard deviation).",
                "key_concepts": [
                    {
                        "concept": "Permutations vs Combinations",
                        "explanation": "Permutation: nPr = n! / (n - r)! (Arrangement where ORDER matters). Combination: nCr = n! / [r!(n - r)!] (Selection where ORDER does NOT matter).",
                        "examples": [
                            "Choosing committee of 3 from 8: 8C3 = (8 × 7 × 6) / (3 × 2 × 1) = 56.",
                            "Arranging letters in 'COMMITTEE': 9! / (2! × 2! × 2!) for repeated M, T, E."
                        ]
                    },
                    {
                        "concept": "Probability Addition & Multiplication Rules",
                        "explanation": "Independent events (A and B): P(A ∩ B) = P(A) × P(B). Mutually exclusive events (A or B): P(A ∪ B) = P(A) + P(B).",
                        "examples": [
                            "Tossing a die and coin: P(6 and Head) = (1/6) × (1/2) = 1/12."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Using nPr when order does not matter (selecting team members is combination nCr!).",
                    "Trap 2: Forgetting to divide by factorials of repeated elements in anagram questions.",
                    "Trap 3: Adding probabilities of independent events instead of multiplying."
                ],
                "worked_examples": [
                    {
                        "question": "In how many ways can a delegation of 3 students be selected from a class of 7 students?",
                        "options": ["A. 210", "B. 35", "C. 42", "D. 70"],
                        "solution": "Order does not matter, so use combination: 7C3 = 7! / (3! × 4!) = (7 × 6 × 5) / (3 × 2 × 1) = 35. Correct Option: B."
                    }
                ],
                "golden_rule": "Selection without order = Combination (nCr). Arrangement with order = Permutation (nPr)."
            }
        ],

        # ==================== 3. PHYSICS ====================
        "Physics": [
            {
                "id": "phy_lesson_1",
                "topic": "Mechanics",
                "title": "Newton's Laws, Projectiles, Gravitation & Simple Harmonic Motion",
                "jamb_weight": "30% of Physics Section (~12 Questions)",
                "overview": "Mechanics accounts for nearly a third of your JAMB Physics score. Key areas include kinematic equations under constant acceleration, trajectory parabolas, momentum conservation, and oscillatory spring/pendulum motion.",
                "key_concepts": [
                    {
                        "concept": "Equations of Linear Motion under Gravity",
                        "explanation": "v = u + at, s = ut + 1/2 at², v² = u² + 2as. For upward vertical motion: a = -g.",
                        "examples": [
                            "At maximum height: final velocity v = 0. Time to max height t = u/g.",
                            "Maximum height reached: H = u² / 2g."
                        ]
                    },
                    {
                        "concept": "Projectile Motion Parameters",
                        "explanation": "Time of flight: T = 2u sinθ / g. Maximum height: H = u² sin²θ / 2g. Range: R = u² sin(2θ) / g. Range is maximized at launch angle θ = 45°.",
                        "examples": [
                            "If launch angle is 30°, range equals launch at 60° (complementary angles)."
                        ]
                    },
                    {
                        "concept": "Simple Harmonic Motion (SHM)",
                        "explanation": "Period of simple pendulum: T = 2π√(l / g). Period of mass on spring: T = 2π√(m / k). Notice pendulum period is INDEPENDENT of bob mass!",
                        "examples": [
                            "Quadrupling length l doubles period T."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing a heavier pendulum bob swings slower—mass has zero effect on pendulum period!",
                    "Trap 2: Forgetting to take the component of velocity: vertical is u sinθ, horizontal is u cosθ.",
                    "Trap 3: Forgetting the negative sign of g when calculating upward throw."
                ],
                "worked_examples": [
                    {
                        "question": "A body is projected with an initial velocity of 40 m/s at an angle of 30° to the horizontal. Calculate the maximum height attained (g = 10 m/s²).",
                        "options": ["A. 80 m", "B. 20 m", "C. 40 m", "D. 10 m"],
                        "solution": "H = (u² sin²θ) / (2g). u = 40, θ = 30° => sin(30°) = 0.5. sin²(30°) = 0.25. H = (1600 × 0.25) / (2 × 10) = 400 / 20 = 20 m. Correct Option: B."
                    }
                ],
                "golden_rule": "Maximum height uses sin²θ / 2g. Pendulum period does NOT depend on bob mass."
            },
            {
                "id": "phy_lesson_2",
                "topic": "Thermal Physics & Waves",
                "title": "Gas Laws, Heat Capacities, Wave Optics & Sound Resonance",
                "jamb_weight": "25% of Physics Section (~10 Questions)",
                "overview": "Thermal physics requires absolute temperature calculations in Kelvin (never Celsius!). Waves cover Snell's refraction law, total internal reflection, resonance in closed/open acoustic tubes, and Doppler frequency shifts.",
                "key_concepts": [
                    {
                        "concept": "Ideal Gas Law & Mandatory Kelvin Scale",
                        "explanation": "P₁V₁ / T₁ = P₂V₂ / T₂. Temperature T MUST ALWAYS be converted to Kelvin: T(K) = θ(°C) + 273.",
                        "examples": [
                            "Charles's Law: V₁/T₁ = V₂/T₂ at constant pressure.",
                            "Boyle's Law: P₁V₁ = P₂V₂ at constant temperature."
                        ]
                    },
                    {
                        "concept": "Specific Heat Capacity & Latent Heat",
                        "explanation": "Heat for temperature change: Q = mcΔθ. Heat for phase change at constant temperature: Q = mL (latent heat of fusion/vaporization).",
                        "examples": [
                            "Melting 1 kg ice at 0°C requires Q = mL_f (no temperature change occurs!)."
                        ]
                    },
                    {
                        "concept": "Acoustic Resonance in Pipes",
                        "explanation": "Closed pipe (closed at one end): First resonance occurs at L = λ/4, third harmonic at L = 3λ/4. Open pipe: First resonance at L = λ/2.",
                        "examples": [
                            "Closed pipes only produce odd harmonics (f, 3f, 5f)."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Calculating gas volume using Celsius temperature instead of converting to Kelvin (fatal 70% error!).",
                    "Trap 2: Adding mcΔθ during a phase change when temperature remains strictly constant.",
                    "Trap 3: Forgetting that a closed pipe produces only ODD harmonics."
                ],
                "worked_examples": [
                    {
                        "question": "A fixed mass of gas occupies 500 cm³ at 27°C. If temperature rises to 127°C at constant pressure, find its new volume.",
                        "options": ["A. 1000 cm³", "B. 666.7 cm³", "C. 2351.8 cm³", "D. 375 cm³"],
                        "solution": "Convert temperatures to Kelvin: T₁ = 27 + 273 = 300 K. T₂ = 127 + 273 = 400 K. Charles's Law: V₁/T₁ = V₂/T₂ => 500/300 = V₂/400 => V₂ = (500 × 400) / 300 = 666.67 cm³. Option A (1000 cm³) is the Celsius trap: 500 × (127/27) = 2351. Correct Option: B."
                    }
                ],
                "golden_rule": "NEVER calculate gas laws in Celsius! Always add 273 to get Kelvin."
            },
            {
                "id": "phy_lesson_3",
                "topic": "Electricity & Magnetism",
                "title": "Ohm's Law, Circuit Analysis, Internal Resistance & Induction",
                "jamb_weight": "25% of Physics Section (~10 Questions)",
                "overview": "Circuit analysis in JAMB hinges on series vs parallel resistors, internal battery resistance (lost volts), electric power dissipation, and transformer voltage/current ratios.",
                "key_concepts": [
                    {
                        "concept": "Ohm's Law & Internal Resistance",
                        "explanation": "E = I(R + r) = V_terminal + Ir. Lost volts = Ir (voltage dropped across internal resistance).",
                        "examples": [
                            "If battery emf E = 12V, terminal voltage V = 10V when delivering 2A, then lost volts = 2V => r = 2V / 2A = 1 Ω."
                        ]
                    },
                    {
                        "concept": "Equivalent Resistance in Networks",
                        "explanation": "Series: R_s = R₁ + R₂. Parallel: 1/R_p = 1/R₁ + 1/R₂ => R_p = (R₁ × R₂) / (R₁ + R₂).",
                        "examples": [
                            "Two 6 Ω resistors in parallel: R_p = 36 / 12 = 3 Ω."
                        ]
                    },
                    {
                        "concept": "Ideal Transformer Equations",
                        "explanation": "V_p / V_s = N_p / N_s = I_s / I_p. Note the INVERSE relationship with current!",
                        "examples": [
                            "Step-down transformer reduces voltage but increases secondary current."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Equating emf to terminal voltage without subtracting lost volts (Ir).",
                    "Trap 2: Assuming current ratio matches voltage ratio in transformers (current is INVERSE: I_s/I_p = V_p/V_s).",
                    "Trap 3: Using P = I²R when voltage across that specific resistor is unknown."
                ],
                "worked_examples": [
                    {
                        "question": "A cell of emf 6.0 V and internal resistance 1.0 Ω is connected across an external 5.0 Ω resistor. Find the terminal potential difference.",
                        "options": ["A. 6.0 V", "B. 5.0 V", "C. 1.0 V", "D. 7.2 V"],
                        "solution": "Total circuit resistance = R + r = 5.0 + 1.0 = 6.0 Ω. Circuit current I = E / (R + r) = 6.0 / 6.0 = 1.0 A. Terminal p.d. V = I × R = 1.0 × 5.0 = 5.0 V (or V = E - Ir = 6.0 - 1.0 = 5.0 V). Correct Option: B."
                    }
                ],
                "golden_rule": "Lost volts = Ir. In ideal transformers: Voltage is direct to turns, current is INVERSE."
            },
            {
                "id": "phy_lesson_4",
                "topic": "Modern & Atomic Physics",
                "title": "Photoelectric Effect, Half-Life Decay, De Broglie & Nuclear Reactions",
                "jamb_weight": "20% of Physics Section (~8 Questions)",
                "overview": "Modern physics tests Einstein's photoelectric equation (hf = W₀ + KE_max), radioactive half-life calculations, nuclear mass-energy equivalence (E = mc²), and wave-particle duality.",
                "key_concepts": [
                    {
                        "concept": "Einstein's Photoelectric Equation",
                        "explanation": "E = hf = W₀ + KE_max = hf₀ + 1/2 mv_max². W₀ is work function = hf₀ (threshold frequency). If incident frequency f < f₀, NO electrons are emitted, no matter how bright the light!",
                        "examples": [
                            "Increasing light intensity increases the NUMBER of photoelectrons emitted per second, but does NOT change their maximum kinetic energy!"
                        ]
                    },
                    {
                        "concept": "Radioactive Half-Life & Exponential Decay",
                        "explanation": "N(t) = N₀ × (1/2)^(t / T_half). Number of half-lives n = t / T_half. Fraction remaining = (1/2)^n.",
                        "examples": [
                            "After 3 half-lives: Fraction remaining = (1/2)³ = 1/8. Fraction decayed = 7/8."
                        ]
                    },
                    {
                        "concept": "De Broglie Wavelength",
                        "explanation": "Matter has wave-like properties: λ = h / p = h / (mv).",
                        "examples": [
                            "Higher velocity results in a shorter de Broglie wavelength."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing that increasing light intensity increases the kinetic energy of emitted photoelectrons (intensity only increases electron COUNT!).",
                    "Trap 2: Confusing the fraction REMAINING with the fraction DECAYED in half-life problems.",
                    "Trap 3: Forgetting to convert electron-volts (eV) to Joules: 1 eV = 1.6 × 10⁻¹⁹ J."
                ],
                "worked_examples": [
                    {
                        "question": "A radioactive substance has a half-life of 4 days. If a sample initially contains 80 g, how much will remain after 16 days?",
                        "options": ["A. 20 g", "B. 5 g", "C. 10 g", "D. 2.5 g"],
                        "solution": "Number of half-lives n = 16 / 4 = 4. Amount remaining = 80 × (1/2)⁴ = 80 / 16 = 5 g. Correct Option: B."
                    }
                ],
                "golden_rule": "Light intensity = number of electrons; Light frequency = energy of electrons. Half-life fraction = (1/2)^n."
            }
        ],

        # ==================== 4. CHEMISTRY ====================
        "Chemistry": [
            {
                "id": "che_lesson_1",
                "topic": "Physical & General Chemistry",
                "title": "Gas Laws, Mole Concept, Stoichiometry & Le Chatelier's Equilibrium",
                "jamb_weight": "25% of Chemistry Section (~10 Questions)",
                "overview": "Physical Chemistry forms the quantitative core of JAMB Chemistry. Key areas include Graham's Law of Diffusion, molar volume stoichiometry (22.4 dm³ at s.t.p.), dynamic chemical equilibrium (Kc), and Le Chatelier's shifts under temperature, pressure, and concentration changes.",
                "key_concepts": [
                    {
                        "concept": "Graham's Law of Diffusion",
                        "explanation": "The rate of diffusion of a gas is inversely proportional to the square root of its molar mass or vapor density: R₁ / R₂ = √(M₂ / M₁) = √(d₂ / d₁). Lighter gases always diffuse faster than denser gases under identical conditions.",
                        "examples": [
                            "Molar mass of CH₄ = 16 g/mol, SO₂ = 64 g/mol => R_CH₄ / R_SO₂ = √(64/16) = √4 = 2. CH₄ diffuses twice as fast as SO₂."
                        ]
                    },
                    {
                        "concept": "Mole Concept & Molar Gas Volume",
                        "explanation": "1 mole of any ideal gas occupies 22.4 dm³ (22,400 cm³) at standard temperature and pressure (s.t.p.: 273 K, 1 atm). Number of moles n = Mass / Molar Mass = Volume / 22.4 dm³ = Concentration (mol/dm³) × Volume (dm³).",
                        "examples": [
                            "4.4 g of CO₂ (M = 44 g/mol) at s.t.p.: n = 4.4 / 44 = 0.1 mol => Volume = 0.1 × 22.4 = 2.24 dm³."
                        ]
                    },
                    {
                        "concept": "Le Chatelier's Principle & Dynamic Equilibrium",
                        "explanation": "When an external stress (temperature, pressure, concentration) is applied to a system at dynamic equilibrium, the system shifts in the direction that offsets the disturbance. For an EXOTHERMIC reaction (ΔH < 0), increasing temperature shifts equilibrium to the LEFT (reducing yield). Increasing pressure shifts equilibrium toward the side with FEWER gas moles.",
                        "examples": [
                            "N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol): 4 gas moles on left, 2 on right. Increasing pressure shifts equilibrium RIGHT, increasing NH₃ yield."
                        ]
                    },
                    {
                        "concept": "Catalysts & Equilibrium Constant",
                        "explanation": "A catalyst accelerates both forward and reverse reaction rates equally by providing an alternative pathway with lower activation energy (Ea). It NEVER shifts equilibrium position and NEVER alters the equilibrium constant (Kc) or enthalpy change (ΔH).",
                        "examples": [
                            "Adding iron catalyst in the Haber process increases the speed to reach equilibrium, but does not increase the percentage of NH₃ at equilibrium."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Graham's law inversion error: R₁/R₂ = √(M₂/M₁), NOT √(M₁/M₂)! Lighter gas has the higher rate.",
                    "Trap 2: Believing a catalyst increases the yield or changes Kc—catalysts only decrease the time required to reach equilibrium.",
                    "Trap 3: Forgetting to convert volume to dm³ when calculating molar concentration (divide cm³ by 1000)."
                ],
                "worked_examples": [
                    {
                        "question": "Under identical conditions of temperature and pressure, gas X with molar mass 16 g/mol diffuses at 40 cm³/s. What is the rate of diffusion of gas Y with molar mass 64 g/mol?",
                        "options": ["A. 80 cm³/s", "B. 20 cm³/s", "C. 10 cm³/s", "D. 160 cm³/s"],
                        "solution": "Apply Graham's Law: R_X / R_Y = √(M_Y / M_X) => 40 / R_Y = √(64 / 16) = √4 = 2. Therefore, R_Y = 40 / 2 = 20 cm³/s. Option A (80 cm³/s) is the trap from direct ratio. Correct Option: B."
                    }
                ],
                "golden_rule": "Graham's law is an INVERSE square root: 4x heavier gas moves half as fast! Catalysts change reaction rate, never yield or Kc."
            },
            {
                "id": "che_lesson_2",
                "topic": "Inorganic Chemistry",
                "title": "Periodic Trends, Transition Metals, Halogens & Metallurgy Extraction",
                "jamb_weight": "25% of Chemistry Section (~10 Questions)",
                "overview": "Inorganic chemistry in JAMB focuses on periodic trends across periods and groups, transition metal electronic configurations and complex ions, halogen displacement orders, and industrial extraction of iron and aluminum.",
                "key_concepts": [
                    {
                        "concept": "Periodic Table Trends",
                        "explanation": "Across a period (left to right): Effective nuclear charge increases, atomic radius decreases, electronegativity and ionization energy generally increase. Down a group: Extra electron shells increase screening/shielding, atomic radius increases, electronegativity and ionization energy decrease.",
                        "examples": [
                            "First ionization energy anomaly: Nitrogen (half-filled 2p³) has a higher first ionization energy than Oxygen (2p⁴) due to extra stability of half-filled subshells."
                        ]
                    },
                    {
                        "concept": "Transition Elements Characteristics",
                        "explanation": "Transition elements have partially filled d-orbitals which confer: (a) Variable oxidation states (Fe²⁺/Fe³⁺, Mn²⁺ to Mn⁷⁺), (b) Colored hydrated ions due to d-d electron transitions, (c) Complex ion formation, (d) Catalytic properties. Exception: Zn²⁺ (3d¹⁰) and Sc³⁺ (3d⁰) have no d-d transitions and form COLORLESS compounds!",
                        "examples": [
                            "Cu²⁺ solutions are blue; Fe²⁺ pale green; Fe³⁺ reddish-brown; Zn²⁺ completely colorless."
                        ]
                    },
                    {
                        "concept": "Extraction of Aluminum (Hall-Héroult Process)",
                        "explanation": "Bauxite (Al₂O₃·2H₂O) is purified to pure Al₂O₃, dissolved in molten cryolite (Na₃AlF₆) at 950°C, and electrolyzed using carbon (graphite) electrodes. Cryolite acts as a solvent to lower the melting point from 2050°C to 950°C and greatly enhance electrical conductivity.",
                        "examples": [
                            "Carbon anodes are gradually consumed by oxygen gas to form CO₂ and must be replaced periodically."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Assuming all transition metal ions are colored—Zn²⁺ has a full d¹⁰ subshell and is completely COLORLESS in water!",
                    "Trap 2: Believing cryolite is an oxidizing agent in aluminum extraction—it functions purely as an electrolyte solvent to lower melting point.",
                    "Trap 3: Confusing halogen displacement: Chlorine can displace Bromide and Iodide, but Bromine CANNOT displace Chloride!"
                ],
                "worked_examples": [
                    {
                        "question": "Which of the following transition metal ions is colorless in aqueous solution?",
                        "options": ["A. Fe²⁺", "B. Cu²⁺", "C. Zn²⁺", "D. Cr³⁺"],
                        "solution": "Color in transition metal ions arises from d-d electron transitions. Zn²⁺ has an electron configuration of [Ar] 3d¹⁰. Because its 3d subshell is completely filled, no d-d transitions are possible, rendering its aqueous solutions colorless. Correct Option: C."
                    }
                ],
                "golden_rule": "Full d¹⁰ (Zn²⁺) and empty d⁰ (Sc³⁺) are colorless! Cryolite lowers bauxite's melting point in aluminum extraction."
            },
            {
                "id": "che_lesson_3",
                "topic": "Organic Chemistry",
                "title": "IUPAC Nomenclature, Isomerism, Hydrocarbons, Alkanols & Esterification",
                "jamb_weight": "30% of Chemistry Section (~12 Questions)",
                "overview": "Organic Chemistry is the highest-weighted topic in JAMB Chemistry. Questions rigorously test IUPAC systematic naming, structural and geometric (cis/trans) isomerism, oxidation of alkanols, and condensation esterification.",
                "key_concepts": [
                    {
                        "concept": "IUPAC Nomenclature Precedence Rules",
                        "explanation": "Select the longest continuous carbon chain containing the principal functional group. Number the chain from the end that gives functional groups (double/triple bonds, -OH, -COOH) the lowest possible position locant. Substituents are cited alphabetically (ethyl before methyl).",
                        "examples": [
                            "CH₃-CH(CH₃)-CH=CH₂ is 3-methylbut-1-ene (NOT 2-methylbut-3-ene, because double bond takes lowest locant 1)."
                        ]
                    },
                    {
                        "concept": "Types of Isomerism",
                        "explanation": "Structural: Chain, Positional, Functional group (e.g. ethanol C₂H₅OH and methoxymethane CH₃OCH₃ have identical formula C₂H₆O). Geometric (cis-trans): Requires a rigid C=C double bond where each double-bonded carbon is attached to two DIFFERENT atoms or groups.",
                        "examples": [
                            "But-2-ene exhibits cis-trans isomerism; But-1-ene CANNOT because carbon-1 has two identical hydrogen atoms!"
                        ]
                    },
                    {
                        "concept": "Alkanol Classification & Oxidation Pathways",
                        "explanation": "Primary alkanol (RCH₂OH) oxidizes to aldehyde, then carboxylic acid. Secondary alkanol (R₂CHOH) oxidizes to ketone. Tertiary alkanol (R₃COH) resists oxidation under normal laboratory conditions because it lacks a hydrogen on the carbinol carbon.",
                        "examples": [
                            "Propan-1-ol -> propanal -> propanoic acid.",
                            "Propan-2-ol -> propanone (ketone).",
                            "2-Methylpropan-2-ol resists oxidation with acidified KMnO₄ or K₂Cr₂O₇."
                        ]
                    },
                    {
                        "concept": "Esterification Reaction",
                        "explanation": "Alkanoic acid + Alkanol in presence of concentrated H₂SO₄ catalyst yields Ester + Water. Esters possess characteristic sweet, fruity aromas and undergo alkaline hydrolysis (saponification) to produce soap and glycerol.",
                        "examples": [
                            "CH₃COOH + C₂H₅OH ⇌ CH₃COOC₂H₅ (ethyl ethanoate) + H₂O."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Numbering the carbon chain to give alkyl branches lowest numbers instead of prioritizing the double or triple bond!",
                    "Trap 2: Believing tertiary alcohols oxidize to ketones—tertiary alcohols resist oxidation completely!",
                    "Trap 3: Assuming but-1-ene has cis-trans isomers (carbon-1 has two identical hydrogens, preventing stereoisomerism)."
                ],
                "worked_examples": [
                    {
                        "question": "Which of the following organic compounds will resist oxidation when heated with acidified potassium heptaoxodichromate(VI)?",
                        "options": ["A. Propan-1-ol", "B. Propan-2-ol", "C. 2-Methylpropan-2-ol", "D. Ethanol"],
                        "solution": "2-Methylpropan-2-ol is a tertiary alcohol: (CH₃)₃C-OH. The carbon atom carrying the hydroxyl (-OH) group has no hydrogen atom directly attached to it, making it resistant to oxidation under normal conditions. Primary and secondary alcohols are readily oxidized. Correct Option: C."
                    }
                ],
                "golden_rule": "Double and triple bonds dictate carbon chain numbering. Tertiary alcohols resist oxidation! Esters smell fruity."
            },
            {
                "id": "che_lesson_4",
                "topic": "Environmental & Industrial Chemistry",
                "title": "Water Hardness, Industrial Processes (Haber & Contact) & Electrolysis Laws",
                "jamb_weight": "20% of Chemistry Section (~8 Questions)",
                "overview": "Covers temporary vs permanent water hardness remediation, industrial chemical production (Haber for ammonia, Contact for sulfuric acid), Faraday's electrochemical laws, and environmental pollutant mechanisms (acid rain, greenhouse gases).",
                "key_concepts": [
                    {
                        "concept": "Temporary vs Permanent Water Hardness",
                        "explanation": "Temporary hardness is caused by dissolved calcium and magnesium hydrogen trioxocarbonate(IV) [Ca(HCO₃)₂, Mg(HCO₃)₂] and is removed by simple BOILING: Ca(HCO₃)₂ -> CaCO₃↓ + H₂O + CO₂. Permanent hardness is caused by CaSO₄ and MgSO₄; boiling does NOT remove it. It requires washing soda (Na₂CO₃) or ion-exchange zeolite resins.",
                        "examples": [
                            "Washing soda removes BOTH temporary and permanent hardness by precipitating insoluble carbonates: Ca²⁺ + CO₃²⁻ -> CaCO₃↓."
                        ]
                    },
                    {
                        "concept": "Industrial Chemical Synthesis Conditions",
                        "explanation": "Haber Process (N₂ + 3H₂ ⇌ 2NH₃, ΔH = -92 kJ/mol): 450°C, 200 atm, finely divided iron catalyst with Al₂O₃ promoter. Contact Process (2SO₂ + O₂ ⇌ 2SO₃, ΔH = -197 kJ/mol): 450°C, 1-2 atm, V₂O₅ catalyst. SO₃ is dissolved in conc. H₂SO₄ to form Oleum (H₂S₂O₇), which is diluted with water.",
                        "examples": [
                            "Direct addition of SO₃ to water is dangerous because it produces an uncontrollable, dense acid mist."
                        ]
                    },
                    {
                        "concept": "Faraday's Laws of Electrolysis",
                        "explanation": "First Law: Mass m = (I × t × M) / (n × F), where F = 96,500 C/mol, n is the valence/charge on the ion. Second Law: Masses of different elements liberated by the same quantity of charge are proportional to their chemical equivalent weights (M / n).",
                        "examples": [
                            "1 Faraday (96,500 C) deposits 1 mole of Ag⁺ (108 g), 0.5 mole of Cu²⁺ (32 g), and 0.33 mole of Al³⁺ (9 g)."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Trying to boil water to remove permanent hardness (CaSO₄ does not decompose upon boiling!).",
                    "Trap 2: Forgetting the valence charge 'n' in Faraday's formula: Cu²⁺ requires 2 Faradays per mole, Al³⁺ requires 3 Faradays!",
                    "Trap 3: Believing SO₃ is added directly to water in the Contact process (it must be absorbed in H₂SO₄ to form Oleum)."
                ],
                "worked_examples": [
                    {
                        "question": "What mass of copper (M = 64 g/mol) is deposited at the cathode when a steady current of 5.0 A is passed through a CuSO₄ solution for 3860 seconds? (1 F = 96,500 C)",
                        "options": ["A. 3.20 g", "B. 6.40 g", "C. 12.80 g", "D. 1.60 g"],
                        "solution": "Charge Q = I × t = 5.0 A × 3860 s = 19,300 C. Number of Faradays = 19,300 / 96,500 = 0.2 F. Reaction: Cu²⁺ + 2e⁻ -> Cu. 2 Faradays deposit 1 mole (64 g) of Cu. Therefore, 0.2 F deposits (0.2 / 2) × 64 = 0.1 × 64 = 6.40 g. Correct Option: B."
                    }
                ],
                "golden_rule": "Boiling cures temporary hardness, washing soda cures both! Always divide Faradays by ion charge n."
            }
        ],

        # ==================== 5. BIOLOGY ====================
        "Biology": [
            {
                "id": "bio_lesson_1",
                "topic": "Cellular Biology & Life Processes",
                "title": "Cell Organelles, Osmosis, Plasmolysis & Enzyme Catalysis Mechanisms",
                "jamb_weight": "25% of Biology Section (~10 Questions)",
                "overview": "Cell biology covers organelle ultrastructure and specialization, differences between plant and animal cells, water relations (osmosis, turgidity, plasmolysis, crenation), and the kinetic lock-and-key properties of biological enzymes.",
                "key_concepts": [
                    {
                        "concept": "Organelle Functions & Ultrastructure",
                        "explanation": "Mitochondria: Site of cellular respiration (Krebs cycle and oxidative phosphorylation) to generate ATP; has folded inner cristae to maximize surface area. Ribosomes: Sites of protein synthesis (translation). Lysosomes: Contain digestive hydrolytic enzymes for intracellular digestion and autolysis ('suicide bags'). Plant vs Animal: Plant cells possess cellulose cell wall, large central vacuole, and plastids/chloroplasts; animal cells have centrioles.",
                        "examples": [
                            "Active tissues like liver and flight muscle cells contain exceptionally high densities of mitochondria."
                        ]
                    },
                    {
                        "concept": "Osmosis, Plasmolysis & Turgor Pressure",
                        "explanation": "Osmosis is the net movement of water from high water potential (hypotonic) to lower water potential (hypertonic) across a selectively permeable membrane. In animal cells: Hypotonic -> Lysis/bursting; Hypertonic -> Crenation/shrinking. In plant cells: Hypotonic -> Turgid (rigid cell wall prevents bursting); Hypertonic -> Plasmolysis (protoplast pulls away from the cell wall).",
                        "examples": [
                            "Red blood cell in distilled water bursts (hemolysis); plant cell in distilled water becomes turgid and does not burst."
                        ]
                    },
                    {
                        "concept": "Enzyme Kinetics & Denaturation",
                        "explanation": "Enzymes are specific protein catalysts that accelerate biochemical reactions by lowering activation energy. High temperatures (>45-50°C) irreversibly break hydrogen/disulfide tertiary bonds, causing denaturation. Freezing temperatures INACTIVATE enzymes reversibly without destroying their structure.",
                        "examples": [
                            "Enzymes have optimal pH: Pepsin in stomach functions at acidic pH 1.5-2.0; Trypsin in small intestine operates at alkaline pH 7.5-8.0."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Stating that plant cells burst in pure water—the cellulose cell wall exerts turgor pressure that prevents bursting!",
                    "Trap 2: Believing freezing denatures enzymes—cold temperatures inactivate enzymes reversibly; only heat or extreme pH denatures them.",
                    "Trap 3: Confusing chloroplasts (photosynthesis) with chromoplasts (coloring petals and fruits)."
                ],
                "worked_examples": [
                    {
                        "question": "What happens when a fresh plant epidermal cell is placed in a concentrated (hypertonic) sucrose solution for two hours?",
                        "options": ["A. The cell swells and lyses", "B. The cytoplasm and cell membrane shrink away from the rigid cell wall", "C. The vacuole actively absorbs sucrose molecules", "D. The cell wall becomes turgid and firm"],
                        "solution": "In a hypertonic solution, water moves out of the plant vacuole by exosmosis down the water potential gradient. The protoplast shrinks away from the cell wall, resulting in plasmolysis. The rigid cell wall prevents the cell from collapsing entirely. Correct Option: B."
                    }
                ],
                "golden_rule": "Plant cells plasmolyze, animal cells crenate! Heat denatures enzymes permanently, cold only inactivates reversibly."
            },
            {
                "id": "bio_lesson_2",
                "topic": "Human Physiology & Systems",
                "title": "Circulation, Excretion (The Nephron), Nervous Reflexes & Digestion",
                "jamb_weight": "30% of Biology Section (~12 Questions)",
                "overview": "Human physiology is heavily tested in JAMB. Master the double circulatory system, blood group antigens/antibodies, nephron filtration and selective reabsorption, the unidirectional reflex arc, and digestive enzyme action.",
                "key_concepts": [
                    {
                        "concept": "Circulatory Dynamics & Blood Groups",
                        "explanation": "Mammals have a double circulatory system: Pulmonary (heart to lungs) and Systemic (heart to body). Blood Group O is Universal Donor (no A or B antigens on RBCs); Group AB is Universal Recipient (no anti-A or anti-B antibodies in plasma). Rhesus incompatibility: Rh-negative mother carrying Rh-positive fetus can cause hemolytic disease of the newborn (Erythroblastosis Fetalis) in subsequent pregnancies.",
                        "examples": [
                            "Arteries carry blood away from heart under high pressure; veins have valves to prevent backflow."
                        ]
                    },
                    {
                        "concept": "Renal Physiology & Nephron Function",
                        "explanation": "Ultrafiltration occurs in the glomerulus and Bowman's capsule under high hydrostatic pressure; blood cells and plasma proteins are retained. Selective Reabsorption: 100% of glucose and amino acids are actively reabsorbed in the Proximal Convoluted Tubule (PCT). Loop of Henle maintains osmotic gradient. ADH increases water reabsorption in the collecting duct.",
                        "examples": [
                            "In a healthy human, glucose is completely absent from urine because of 100% reabsorption in the PCT."
                        ]
                    },
                    {
                        "concept": "Reflex Arc & Synaptic Transmission",
                        "explanation": "Pathway: Receptor -> Sensory neuron -> Relay/Interneuron in spinal cord -> Motor neuron -> Effector muscle. Synaptic transmission is strictly unidirectional because neurotransmitter vesicles (acetylcholine) exist solely in the presynaptic terminal.",
                        "examples": [
                            "Knee-jerk reflex and withdrawing hand from a hot flame are involuntary spinal reflexes."
                        ]
                    },
                    {
                        "concept": "Digestive Biochemistry",
                        "explanation": "Mouth: Salivary amylase breaks starch to maltose (pH 6.8). Stomach: Pepsin breaks proteins to peptones (acidic pH 2.0 via HCl). Duodenum: Bile contains NO enzymes; it only emulsifies fats into micro-droplets. Pancreatic juice supplies amylase, trypsin, and lipase.",
                        "examples": [
                            "Without bile emulsification, lipase cannot efficiently hydrolyze lipids because surface area is too small."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing bile contains digestive enzymes—bile has zero enzymes; it only emulsifies fats mechanically!",
                    "Trap 2: Assuming glucose is found in normal human urine—100% of glucose is reabsorbed in the proximal tubule in healthy individuals!",
                    "Trap 3: Confusing pulmonary artery (carries deoxygenated blood) with pulmonary vein (carries oxygenated blood)."
                ],
                "worked_examples": [
                    {
                        "question": "In a healthy human kidney, which of the following substances present in the glomerular filtrate is completely absent from normal urine?",
                        "options": ["A. Urea", "B. Sodium chloride", "C. Glucose", "D. Water"],
                        "solution": "In healthy individuals, 100% of filtered glucose is actively reabsorbed by secondary active transport in the proximal convoluted tubule (PCT) back into the bloodstream. Finding glucose in urine indicates diabetes mellitus. Correct Option: C."
                    }
                ],
                "golden_rule": "Glucose is 100% reabsorbed in the PCT! Bile has NO enzymes, only emulsifies fats."
            },
            {
                "id": "bio_lesson_3",
                "topic": "Genetics & Evolution",
                "title": "Mendelian Crosses, Sex-Linkage, Sickle-Cell Inheritance & Natural Selection",
                "jamb_weight": "25% of Biology Section (~10 Questions)",
                "overview": "Genetics covers Mendel's Laws of Segregation and Independent Assortment, Punnett square inheritance ratios, sex-linked disorders on the X chromosome (hemophilia and color blindness), sickle cell balanced polymorphism, and Darwinian natural selection.",
                "key_concepts": [
                    {
                        "concept": "Mendelian Genetic Ratios",
                        "explanation": "Monohybrid heterozygous cross (Aa × Aa) yields a 3:1 phenotypic ratio and 1:2:1 genotypic ratio (1 AA : 2 Aa : 1 aa). Dihybrid cross (AaBb × AaBb) yields a 9:3:3:1 phenotypic ratio.",
                        "examples": [
                            "Test cross: Crossing an organism displaying the dominant phenotype with a homozygous recessive (aa) to determine if it is homozygous (AA) or heterozygous (Aa)."
                        ]
                    },
                    {
                        "concept": "Sex-Linked Inheritance (X-Chromosome Linkage)",
                        "explanation": "Genes for hemophilia and red-green color blindness are carried on the non-homologous region of the X chromosome. Males (XY) have only one X chromosome; if it carries the recessive allele (X^h Y), the male is affected! Females (XX) require two recessive alleles (X^h X^h) to be affected; heterozygous females (X^H X^h) are phenotypically normal carriers.",
                        "examples": [
                            "A father CANNOT pass an X-linked trait to his son because he transmits only his Y chromosome to male offspring!"
                        ]
                    },
                    {
                        "concept": "Sickle Cell Gene & Heterozygote Advantage",
                        "explanation": "HbA HbA: Normal hemoglobin, susceptible to severe malaria. HbA HbS: Sickle cell trait (carrier), normal life with resistance to fatal Plasmodium falciparum malaria (balanced polymorphism). HbS HbS: Sickle cell anemia, suffers painful vaso-occlusive crises.",
                        "examples": [
                            "Two carriers (HbA HbS × HbA HbS) have a 25% chance of an HbA HbA child, 50% carrier HbA HbS, and 25% sickle cell anemia HbS HbS."
                        ]
                    },
                    {
                        "concept": "Theories of Evolution (Darwin vs Lamarck)",
                        "explanation": "Lamarckism: Inheritance of acquired characteristics through use and disuse (disproven—lifting weights does not produce muscular babies). Darwinism: Natural selection acts on existing heritable variations; individuals with advantageous traits survive and reproduce more successfully (survival of the fittest).",
                        "examples": [
                            "Industrial melanism in the peppered moth (Biston betularia) during the industrial revolution in England."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing a father can transmit an X-linked disorder like hemophilia to his son (sons inherit only the Y chromosome from their father!).",
                    "Trap 2: Confusing the 3:1 phenotypic ratio with the 1:2:1 genotypic ratio in a monohybrid cross.",
                    "Trap 3: Assuming acquired traits can be inherited (Lamarckian fallacy)."
                ],
                "worked_examples": [
                    {
                        "question": "A woman who is a carrier for hemophilia (X^H X^h) marries a normal man (X^H Y). What percentage of their male children will have hemophilia?",
                        "options": ["A. 0%", "B. 25%", "C. 50%", "D. 100%"],
                        "solution": "Sons receive the Y chromosome from the father and either X^H or X^h from the mother with equal probability. The male offspring genotypes are X^H Y (normal, 50%) and X^h Y (hemophiliac, 50%). Therefore, 50% of the sons will be affected. Correct Option: C."
                    }
                ],
                "golden_rule": "Fathers NEVER pass X-linked traits to sons! Sickle trait (HbA HbS) provides malaria resistance."
            },
            {
                "id": "bio_lesson_4",
                "topic": "Ecology & Environment",
                "title": "Trophic Pyramids, Biogeochemical Cycles, Biomes & Ecological Succession",
                "jamb_weight": "20% of Biology Section (~8 Questions)",
                "overview": "Ecology explores trophic levels, the 10% energy transfer law, nitrogen and carbon cycles, primary vs secondary ecological succession, African biomes (rainforest, savanna, desert), and biotic relationships (mutualism, parasitism, commensalism).",
                "key_concepts": [
                    {
                        "concept": "Trophic Levels & The 10% Energy Law",
                        "explanation": "Energy flows unidirectionally: Producers (plants) -> Primary consumers (herbivores) -> Secondary consumers (carnivores). Approximately 90% of energy is lost at each trophic level through metabolic respiration, heat loss, and excretion; only ~10% is incorporated into new biomass. Consequently, Pyramids of Energy are ALWAYS upright and can NEVER be inverted!",
                        "examples": [
                            "If producers capture 10,000 kJ of solar energy, herbivores receive 1,000 kJ, and primary carnivores receive only 100 kJ."
                        ]
                    },
                    {
                        "concept": "Nitrogen Cycle Transformations",
                        "explanation": "Nitrogen Fixation: N₂ -> NH₃/NH₄⁺ by free-living bacteria (Azotobacter, Clostridium) and symbiotic Rhizobium in leguminous root nodules. Nitrification: NH₄⁺ -> NO₂⁻ by Nitrosomonas; NO₂⁻ -> NO₃⁻ by Nitrobacter. Denitrification: NO₃⁻ -> N₂ gas by anaerobic Pseudomonas denitrificans in waterlogged soils.",
                        "examples": [
                            "Legumes enrich soil nitrogen without requiring synthetic nitrogenous fertilizers."
                        ]
                    },
                    {
                        "concept": "Ecological Succession",
                        "explanation": "Primary Succession: Starts on completely sterile surfaces devoid of soil (bare rock, hardened volcanic lava). Pioneer species are lichens and mosses. Secondary Succession: Begins in an area where an existing community was destroyed (cleared farmland, burnt forest) but where SOIL is already present. Secondary succession proceeds much faster.",
                        "examples": [
                            "Pioneers on bare rock secrete organic acids that erode mineral rock into primitive soil."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing energy pyramids can be inverted—energy pyramids are NEVER inverted because energy is lost at every trophic transfer!",
                    "Trap 2: Confusing Nitrosomonas (converts ammonia to nitrite) with Nitrobacter (converts nitrite to nitrate).",
                    "Trap 3: Thinking primary succession starts with grasses (it begins with pioneer lichens and mosses on bare rock)."
                ],
                "worked_examples": [
                    {
                        "question": "In a terrestrial ecosystem where producers fix 10,000 kJ of energy, approximately how much energy is available to secondary consumers?",
                        "options": ["A. 1,000 kJ", "B. 100 kJ", "C. 10 kJ", "D. 5,000 kJ"],
                        "solution": "Apply Lindeman's 10% rule: Producer level = 10,000 kJ. Primary consumers receive 10% of 10,000 kJ = 1,000 kJ. Secondary consumers receive 10% of 1,000 kJ = 100 kJ. Correct Option: B."
                    }
                ],
                "golden_rule": "Energy pyramids NEVER invert! Nitrosomonas makes nitrite (NO₂⁻), Nitrobacter makes nitrate (NO₃⁻)."
            }
        ],

        # ==================== 6. ECONOMICS ====================
        "Economics": [
            {
                "id": "eco_lesson_1",
                "topic": "Basic Economic Principles & Methodology",
                "title": "Scarcity, Choice, Opportunity Cost & Production Possibility Curve (PPC)",
                "jamb_weight": "25% of Economics Section (~10 Questions)",
                "overview": "Economics investigates how society manages scarce resources. Core concepts include scarcity vs shortage, scale of preference, opportunity cost (real cost) vs monetary cost, and interpreting movements along vs outward shifts of the Production Possibility Curve.",
                "key_concepts": [
                    {
                        "concept": "Scarcity, Choice & Scale of Preference",
                        "explanation": "Scarcity is the fundamental economic reality: human wants are limitless while productive resources (land, labor, capital, enterprise) are finite. Because of scarcity, choices must be made. A Scale of Preference is an individual's list of unsatisfied wants ranked in order of their relative importance to facilitate rational choice.",
                        "examples": [
                            "Scarcity is universal and permanent across both developed and developing economies."
                        ]
                    },
                    {
                        "concept": "Opportunity Cost (Real Cost)",
                        "explanation": "Opportunity cost is the next best alternative forgone when a choice is made. It is the real sacrifice made, NOT the financial price paid. If a student chooses to buy a textbook instead of shoes, the shoes are the opportunity cost.",
                        "examples": [
                            "Building a new highway means the government sacrifices funding for hospital renovations."
                        ]
                    },
                    {
                        "concept": "Production Possibility Curve (PPC/PPF)",
                        "explanation": "A graphical boundary showing the maximum combination of two goods an economy can produce when all resources are fully and efficiently employed. Points ON the curve: Full employment and productive efficiency. Points INSIDE the curve: Inefficient underutilization or unemployment of resources. Points OUTSIDE the curve: Currently unattainable. An OUTWARD SHIFT of the PPC represents economic growth driven by technological advancement, discovery of resources, or labor expansion.",
                        "examples": [
                            "A war or natural disaster destroys capital and shifts the PPC inward to the left."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing money cost with opportunity cost—money spent is accounting cost; opportunity cost is the sacrificed alternative good!",
                    "Trap 2: Believing points outside the PPC represent inefficient production—points outside are UNATTAINABLE with current technology!",
                    "Trap 3: Confusing permanent scarcity with temporary market shortages."
                ],
                "worked_examples": [
                    {
                        "question": "An economy operating at a point located inside its Production Possibility Curve is experiencing:",
                        "options": ["A. Maximum productive efficiency", "B. Rapid economic growth", "C. Unemployment or underutilization of available productive resources", "D. Unattainable consumer production targets"],
                        "solution": "Points on the boundary of the PPC indicate full employment of resources. Any point inside the PPC represents productive inefficiency, where resources like labor and capital are idle or misallocated. Correct Option: C."
                    }
                ],
                "golden_rule": "Opportunity cost is the forgone alternative, NOT the price tag! Points inside the PPC indicate underemployment."
            },
            {
                "id": "eco_lesson_2",
                "topic": "Microeconomics & Price Mechanism",
                "title": "Elasticity of Demand & Supply, Price Ceilings/Floors & Market Equilibrium",
                "jamb_weight": "30% of Economics Section (~12 Questions)",
                "overview": "Microeconomics explores price determination through supply and demand interaction, price elasticity formulas, cross and income elasticity, consumer surplus, and the market distortion effects of government price controls.",
                "key_concepts": [
                    {
                        "concept": "Price Elasticity of Demand (PED)",
                        "explanation": "PED measures the responsiveness of quantity demanded to a change in price: Ed = (%ΔQd) / (%ΔP) = (ΔQ / ΔP) × (P₁ / Q₁). Ed > 1: Elastic (luxuries, many substitutes; lowering price increases total revenue). Ed < 1: Inelastic (necessities, addictive goods; raising price increases total revenue). Ed = 1: Unitary elastic.",
                        "examples": [
                            "Petrol and salt have highly inelastic demand because they are necessities with few substitutes."
                        ]
                    },
                    {
                        "concept": "Cross Elasticity & Income Elasticity",
                        "explanation": "Cross Elasticity of Demand (Exy): Measures responsiveness of Good X to price changes of Good Y. Positive (>0) for Substitutes (butter and margarine); Negative (<0) for Complements (car and petrol); Zero for independent goods. Income Elasticity (Ey): Positive (>0) for Normal goods; Negative (<0) for Inferior goods.",
                        "examples": [
                            "If bread price rises and yam demand increases, cross elasticity is positive (substitutes)."
                        ]
                    },
                    {
                        "concept": "Government Price Legislation",
                        "explanation": "Price Ceiling (Maximum Price): Legally imposed maximum price set BELOW equilibrium to protect consumers during inflation. Leads to excess demand (shortages), queues, and black markets. Price Floor (Minimum Price): Legally imposed minimum price set ABOVE equilibrium to protect producers or workers (minimum wage). Leads to excess supply (surpluses).",
                        "examples": [
                            "A rent control ceiling set below market rent creates a shortage of rental apartments."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Placing a price ceiling above equilibrium—a ceiling must be BELOW equilibrium to have legal effect! A floor is placed ABOVE.",
                    "Trap 2: Confusing cross elasticity signs: Substitutes have POSITIVE cross elasticity; Complements have NEGATIVE cross elasticity.",
                    "Trap 3: Confusing change in quantity demanded (movement along curve) with change in demand (shift of entire curve)."
                ],
                "worked_examples": [
                    {
                        "question": "If a 10% increase in the price of butter leads to a 15% increase in the quantity demanded of margarine, the cross elasticity of demand is:",
                        "options": ["A. -1.5 (Complements)", "B. +1.5 (Substitutes)", "C. +0.67 (Substitutes)", "D. -0.67 (Complements)"],
                        "solution": "Cross Elasticity Exy = (%ΔQ_margarine) / (%ΔP_butter) = (+15%) / (+10%) = +1.5. A positive coefficient confirms that the two goods are substitutes in consumption. Correct Option: B."
                    }
                ],
                "golden_rule": "Price ceiling below equilibrium causes shortages! Positive cross elasticity = Substitutes."
            },
            {
                "id": "eco_lesson_3",
                "topic": "Macroeconomics & National Income",
                "title": "GDP vs GNP, Circular Flow, The Multiplier Effect & Types of Inflation",
                "jamb_weight": "25% of Economics Section (~10 Questions)",
                "overview": "Macroeconomics focuses on economy-wide indicators: GDP vs GNP vs NNI, the Keynesian investment multiplier (k = 1/MPS), the three national income measurement approaches, and causes of demand-pull vs cost-push inflation.",
                "key_concepts": [
                    {
                        "concept": "National Income Aggregates (GDP vs GNP)",
                        "explanation": "Gross Domestic Product (GDP): Total monetary value of all final goods and services produced within the geographical boundaries of a nation in a year, regardless of producer nationality. Gross National Product (GNP): GDP + Net Factor Income from Abroad (NFIA) (earnings of citizens abroad minus foreigners' domestic repatriations). Net National Product (NNP): GNP - Depreciation.",
                        "examples": [
                            "Income earned by a Nigerian engineer working in Dubai is included in Nigeria's GNP, but excluded from Nigeria's GDP."
                        ]
                    },
                    {
                        "concept": "Measurement Methods & Avoiding Double Counting",
                        "explanation": "Output Method: Sum of Value Added at each production stage (Output value minus intermediate inputs). Income Method: Sum of factor rewards (Wages + Rent + Interest + Profit). Transfer payments (pensions, student gifts, unemployment benefits) are EXCLUDED. Expenditure Method: Y = C + I + G + (X - M).",
                        "examples": [
                            "Excluding intermediate goods prevents double counting in the output method."
                        ]
                    },
                    {
                        "concept": "The Keynesian Investment Multiplier",
                        "explanation": "MPC + MPS = 1. The investment multiplier k = 1 / MPS = 1 / (1 - MPC) = ΔY / ΔI. Any initial autonomous injection into investment generates an amplified increase in aggregate national income.",
                        "examples": [
                            "If MPC = 0.8, then MPS = 0.2 => k = 1 / 0.2 = 5. A ₦10B investment increases national income by ₦50B."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Including transfer payments (pensions, pocket money) in national income calculations—transfer payments produce no output!",
                    "Trap 2: Calculating the multiplier as 1/MPC instead of 1/(1 - MPC) or 1/MPS.",
                    "Trap 3: Confusing GDP (territorial location) with GNP (citizen ownership)."
                ],
                "worked_examples": [
                    {
                        "question": "In a closed economy with no government intervention, the marginal propensity to save (MPS) is 0.25. If investment expenditure increases by ₦40 million, national income will increase by:",
                        "options": ["A. ₦10 million", "B. ₦40 million", "C. ₦160 million", "D. ₦100 million"],
                        "solution": "Multiplier k = 1 / MPS = 1 / 0.25 = 4. Change in national income ΔY = k × ΔI = 4 × ₦40 million = ₦160 million. Correct Option: C."
                    }
                ],
                "golden_rule": "GNP = GDP + Net Factor Income from Abroad. Exclude transfer payments! Multiplier is 1/MPS."
            },
            {
                "id": "eco_lesson_4",
                "topic": "Money, Banking & Public Finance",
                "title": "Central Bank Tools (MPR, CRR, OMO), Credit Multiplier & Taxation Principles",
                "jamb_weight": "20% of Economics Section (~8 Questions)",
                "overview": "Examines central bank monetary instruments to combat inflation, commercial bank fractional credit creation, Adam Smith's canons of taxation, and progressive vs regressive tax incidence.",
                "key_concepts": [
                    {
                        "concept": "Central Bank Monetary Policy Instruments",
                        "explanation": "Central Bank controls money supply to stabilize inflation. Contractionary tools (fight inflation): Raise Monetary Policy Rate (MPR), increase Cash Reserve Ratio (CRR), and SELL treasury bills through Open Market Operations (OMO) to mop up excess bank liquidity. Expansionary tools (fight recession): Lower MPR, decrease CRR, and BUY securities.",
                        "examples": [
                            "Selling treasury bills in OMO withdraws cash from commercial bank vaults into the central bank."
                        ]
                    },
                    {
                        "concept": "Commercial Bank Credit Multiplier",
                        "explanation": "Commercial banks create credit through fractional reserves. Credit Multiplier = 1 / Cash Reserve Ratio (CRR). Total credit/deposits created = Initial Cash Deposit × (1 / CRR).",
                        "examples": [
                            "With an initial deposit of ₦200,000 and CRR of 10% (0.10): Total deposit created = ₦200,000 × (1 / 0.10) = ₦2,000,000."
                        ]
                    },
                    {
                        "concept": "Taxation Types & Adam Smith's Canons",
                        "explanation": "Canons: Equity (ability to pay), Certainty, Convenience, Economy. Tax Structures: Progressive (tax rate increases as income increases—PAYE income tax); Proportional (flat rate for all); Regressive (takes a higher percentage of income from low earners—VAT/sales taxes on basic goods).",
                        "examples": [
                            "VAT is regressive because poorer households spend a larger fraction of their total income on basic consumed goods."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Thinking the Central Bank buys securities to reduce inflation—the Central Bank SELLS securities in OMO to reduce liquidity!",
                    "Trap 2: Believing VAT is progressive—Value Added Tax is regressive relative to income.",
                    "Trap 3: Forgetting that the Central Bank acts as lender of last resort to commercial banks, NOT to private individuals."
                ],
                "worked_examples": [
                    {
                        "question": "If the Central Bank fixes the cash reserve ratio at 10%, an initial cash deposit of ₦200,000 in a commercial bank can lead to a maximum total deposit creation of:",
                        "options": ["A. ₦20,000", "B. ₦2,000,000", "C. ₦200,000", "D. ₦1,800,000"],
                        "solution": "Credit Multiplier = 1 / CRR = 1 / 0.10 = 10. Maximum total deposit creation = Initial Deposit × Multiplier = ₦200,000 × 10 = ₦2,000,000. Correct Option: B."
                    }
                ],
                "golden_rule": "To curb inflation: CBN SELLS securities and RAISES interest rates. Total money created = Initial Deposit / CRR."
            }
        ],

        # ==================== 7. GOVERNMENT ====================
        "Government": [
            {
                "id": "gov_lesson_1",
                "topic": "Elements of Government & Political Theory",
                "title": "Sovereignty, Rule of Law, Separation of Powers, Parliamentary vs Presidential",
                "jamb_weight": "25% of Government Section (~10 Questions)",
                "overview": "Explores fundamental political concepts: attributes of the State vs Government, legal and political sovereignty (Dicey, Bodin), Montesquieu's separation of powers and checks/balances, and parliamentary vs presidential institutional architectures.",
                "key_concepts": [
                    {
                        "concept": "The State vs Government & Sovereignty",
                        "explanation": "A State is a permanent sovereign political community comprising Population, Territory, Government, and Sovereignty. Government is the temporary agency through which the will of the state is formulated and executed. Sovereignty is the supreme, absolute power of the state. Legal sovereignty belongs to the legislature; Political sovereignty resides in the electorate/citizens.",
                        "examples": [
                            "Governments change through elections or coups, but the Nigerian State remains permanent."
                        ]
                    },
                    {
                        "concept": "Rule of Law (A.V. Dicey)",
                        "explanation": "Three pillars: 1. Absolute supremacy of the law (no arbitrary power or detention without trial). 2. Equality before the law (all citizens subject to the same regular courts). 3. Protection of fundamental human rights by an independent judiciary.",
                        "examples": [
                            "Immunity clauses and military decrees with ouster clauses represent limitations to the Rule of Law."
                        ]
                    },
                    {
                        "concept": "Parliamentary vs Presidential Systems",
                        "explanation": "Parliamentary: Fusion of executive and legislative powers. Head of State (Monarch/Ceremonial President) is distinct from Head of Government (Prime Minister, chosen from Parliament). Cabinet exercises collective responsibility. Parliament can dismiss the government via a Vote of No Confidence. Presidential: Strict separation of powers. President is both Head of State and Head of Government, elected directly, with fixed tenure, removed only through constitutional impeachment.",
                        "examples": [
                            "Britain operates a Parliamentary system; Nigeria (1979/1999) and the United States operate Presidential systems."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing Parliamentary with Presidential: In a Parliamentary system, the Prime Minister is an elected MP, NOT an outside executive!",
                    "Trap 2: Believing political sovereignty lies with the President—political sovereignty belongs to the ELECTORATE (the voters)!",
                    "Trap 3: Assuming separation of powers means zero interaction—checks and balances necessitate mutual oversight."
                ],
                "worked_examples": [
                    {
                        "question": "In a parliamentary system of government, a vote of no confidence passed by the legislature results in:",
                        "options": ["A. Immediate impeachment of the ceremonial president", "B. Resignation of the prime minister and the entire cabinet", "C. Dissolution of the judicial service commission", "D. Declaration of a state of emergency by the chief justice"],
                        "solution": "In a parliamentary system, the executive is fused with the legislature and is collectively responsible to parliament. If a vote of no confidence is passed, the Prime Minister and the entire cabinet must resign or dissolve parliament. Correct Option: B."
                    }
                ],
                "golden_rule": "Parliamentary = Fusion of powers & Vote of No Confidence; Presidential = Separation of powers & Impeachment."
            },
            {
                "id": "gov_lesson_2",
                "topic": "Colonial Administration in Nigeria & West Africa",
                "title": "Indirect Rule in Northern vs Eastern Nigeria, Warrant Chiefs & Assimilation",
                "jamb_weight": "25% of Government Section (~10 Questions)",
                "overview": "Covers British colonial Indirect Rule under Lord Lugard, regional variations across Northern Emirates, Yoruba kingdoms, and Igbo segmentary communities, the 1929 Aba Women's Riot, and French direct Assimilation vs Association.",
                "key_concepts": [
                    {
                        "concept": "British Indirect Rule System & Rationale",
                        "explanation": "Governing colonized peoples through their traditional rulers and institutions under British supervision. Reasons for adoption: 1. Acute shortage of British personnel and financial resources. 2. Language and cultural barriers. 3. Harsh tropical climate ('White Man's Grave'). 4. Existing organized traditional structures in Northern Emirates.",
                        "examples": [
                            "Lord Lugard first tested Indirect Rule in the Sokoto Caliphate following the 1900-1903 conquest."
                        ]
                    },
                    {
                        "concept": "Regional Disparities & The Eastern Failure",
                        "explanation": "Northern Nigeria: Highly successful due to the centralized, autocratic Emirate system with established taxation and Alkali courts. Western Nigeria: Moderately successful; traditional checks and balances on Obas created friction. Eastern Nigeria: An absolute failure. Traditional Igbo society was acephalous (stateless/egalitarian, 'Igbo enwe eze'). The British appointed artificial 'Warrant Chiefs' who abused tax powers, sparking the 1929 Aba Women's Riot.",
                        "examples": [
                            "The 1929 Aba Women's Riot was organized entirely by women protesting oppressive Warrant Chiefs and rumors of direct taxation on women."
                        ]
                    },
                    {
                        "concept": "French Policy of Assimilation vs Association",
                        "explanation": "Assimilation: Aimed to turn Africans into culturally French citizens ('evolués') in the Four Communes of Senegal (Dakar, Gorée, Saint-Louis, Rufisque). Failed due to fierce African cultural resistance, huge financial cost, and French reluctance to grant full equality. Replaced by Association, which respected indigenous institutions while maintaining colonial dominance.",
                        "examples": [
                            "In the Four Communes, assimilated Africans enjoyed full French voting rights in the French National Assembly."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Believing Indirect Rule succeeded in Eastern Nigeria—it failed completely because the Igbo political structure was acephalous!",
                    "Trap 2: Believing men led the 1929 Aba Riots—it was organized and executed entirely by women!",
                    "Trap 3: Confusing French Assimilation (cultural conversion) with Association (indirect collaboration)."
                ],
                "worked_examples": [
                    {
                        "question": "The British system of Indirect Rule failed completely in Eastern Nigeria primarily because:",
                        "options": ["A. British officers refused to visit the region", "B. The traditional society was acephalous and lacked centralized executive monarchies", "C. Christian missionaries had already abolished all traditional worship", "D. French colonial forces interfered with eastern administrative boundaries"],
                        "solution": "Traditional Igbo society was decentralized, republican, and segmented into village assemblies without an autocratic king ('Igbo enwe eze'). Imposing artificial Warrant Chiefs violated democratic norms and provoked rebellion. Correct Option: B."
                    }
                ],
                "golden_rule": "Northern Indirect Rule succeeded due to centralized Emirs; Eastern failed because Igbos had NO kings (acephalous)!"
            },
            {
                "id": "gov_lesson_3",
                "topic": "Nigerian Constitutional Development",
                "title": "Clifford (1922), Richards (1946), Macpherson (1951), Lyttelton (1954) & 1963 Republic",
                "jamb_weight": "30% of Government Section (~12 Questions)",
                "overview": "Chronological mastery of constitutional milestones: Clifford (elective principle), Richards (regionalism), Macpherson (quasi-federalism), Lyttelton (true federalism), 1960 Independence, and 1963 Republican Constitution.",
                "key_concepts": [
                    {
                        "concept": "Clifford Constitution (1922) & Elective Principle",
                        "explanation": "Introduced the Elective Principle for the first time in Nigeria, allowing 4 elected African members into the Legislative Council (3 for Lagos, 1 for Calabar). Led directly to the formation of Nigeria's first political party: Herbert Macaulay's NNDP in 1923. Defect: Completely excluded Northern Nigeria from the Legislative Council.",
                        "examples": [
                            "Franchise was restricted to males earning at least £100 per annum residing in Lagos or Calabar."
                        ]
                    },
                    {
                        "concept": "Richards (1946) vs Lyttelton (1954) Constitutions",
                        "explanation": "Richards Constitution (1946): Introduced Regionalism (Northern, Western, Eastern regions) and unified North and South in one legislative council for the first time. Lyttelton Constitution (1954): Formally established True Federalism in Nigeria by creating Exclusive, Concurrent, and Residual legislative lists, creating regional premiers and autonomous regional civil services/judiciaries.",
                        "examples": [
                            "Lyttelton made Lagos the independent Federal Capital Territory."
                        ]
                    },
                    {
                        "concept": "1960 Independence vs 1963 Republican Constitution",
                        "explanation": "1960 Constitution: Queen Elizabeth II remained ceremonial Head of State represented by Governor-General Azikiwe; British Privy Council was the highest court of appeal. 1963 Republican Constitution: Severed monarchical ties; Dr. Nnamdi Azikiwe became Nigeria's first President; Nigerian Supreme Court became the final appellate court. Created the Mid-Western Region.",
                        "examples": [
                            "In 1963, appeals to the British Judicial Committee of the Privy Council were permanently abolished."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Thinking the Richards Constitution introduced federalism—it introduced Regionalism; TRUE federalism was established by Lyttelton (1954)!",
                    "Trap 2: Believing Clifford's elective principle applied nationwide—it applied ONLY to Lagos (3 seats) and Calabar (1 seat)!",
                    "Trap 3: Confusing 1960 and 1963: 1960 kept the Queen as Head of State; 1963 made Nigeria a Republic with a Nigerian President."
                ],
                "worked_examples": [
                    {
                        "question": "True federalism was formally established in Nigeria by which colonial constitution?",
                        "options": ["A. Clifford Constitution of 1922", "B. Richards Constitution of 1946", "C. Macpherson Constitution of 1951", "D. Lyttelton Constitution of 1954"],
                        "solution": "The Lyttelton Constitution of 1954 formally established true federalism by sharing legislative powers between the central and regional governments through Exclusive, Concurrent, and Residual lists, and creating autonomous regional premier offices. Correct Option: D."
                    }
                ],
                "golden_rule": "Clifford = Elective Principle; Richards = Regionalism; Lyttelton = True Federalism; 1963 = Republic."
            },
            {
                "id": "gov_lesson_4",
                "topic": "Federalism, Military Rule & Foreign Policy",
                "title": "Revenue Allocation, Creation of States, Military Decrees & Afrocentric Policy",
                "jamb_weight": "20% of Government Section (~8 Questions)",
                "overview": "Analyzes revenue allocation principles (derivation, population), state creation trajectory (1963 to 1996), characteristics and decrees of military regimes, and Nigeria's Afrocentric foreign policy architecture.",
                "key_concepts": [
                    {
                        "concept": "Revenue Allocation Principles & State Creation",
                        "explanation": "Principles: Derivation (returning oil revenue to source), Population, Equality of States, Landmass/Terrain. State Creation Milestones: 1963: Mid-West Region created via plebiscite. 1967 (Gowon): 12 states (broke regional power before Civil War). 1976 (Murtala): 19 states + planned Abuja FCT. 1987 (Babangida): 21 states. 1991 (Babangida): 30 states. 1996 (Abacha): 36 states.",
                        "examples": [
                            "Derivation was dominant during the First Republic (50%) and reduced under military rule."
                        ]
                    },
                    {
                        "concept": "Military Rule Dynamics & Legislation",
                        "explanation": "Characteristics: Suspension of the constitution, rule by Decrees (federal level) and Edicts (state level), centralization of power under the Supreme Military Council / AFRC, inclusion of ouster clauses prohibiting judicial review.",
                        "examples": [
                            "Decrees overrode all existing constitutional laws and could not be challenged in civilian courts."
                        ]
                    },
                    {
                        "concept": "Nigeria's Afrocentric Foreign Policy",
                        "explanation": "Core doctrine: Africa as the Centerpiece. Objectives: Eradication of apartheid and colonialism, fostering regional economic integration (ECOWAS in 1975), and initiating peacekeeping missions (ECOMOG in Liberia and Sierra Leone). Member of Non-Aligned Movement (NAM), AU, Commonwealth, and UN.",
                        "examples": [
                            "Nigeria spearheaded the boycott of the 1976 Montreal Olympics over New Zealand's sporting ties with apartheid South Africa."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing military legislative terms: Federal military laws are DECREES; State military laws are EDICTS!",
                    "Trap 2: Believing General Gowon created 19 states—Gowon created 12 states in 1967; Murtala Mohammed created 19 states in 1976!",
                    "Trap 3: Believing civil courts could invalidate military decrees—ouster clauses barred judicial review."
                ],
                "worked_examples": [
                    {
                        "question": "Under military administration in Nigeria, legislative enactments at the federal level were formally known as:",
                        "options": ["A. Edicts", "B. Acts of Parliament", "C. Decrees", "D. Official Gazettes"],
                        "solution": "Federal military regimes ruled by issuing Decrees signed by the Head of the Federal Military Government. At the state level, military governors promulgated Edicts. Correct Option: C."
                    }
                ],
                "golden_rule": "Federal military = Decrees; State military = Edicts. Africa is the centerpiece of Nigeria's foreign policy."
            }
        ],

        # ==================== 8. LITERATURE IN ENGLISH ====================
        "Literature in English": [
            {
                "id": "lit_lesson_1",
                "topic": "Literary Appreciation & Devices",
                "title": "Literary Devices: Metaphor, Synecdoche, Metonymy, Irony & Dramatic Elements",
                "jamb_weight": "25% of Literature Section (~10 Questions)",
                "overview": "Literary appreciation tests figures of speech (synecdoche vs metonymy, oxymoron vs paradox, litotes, irony) and dramatic conventions (dramatic irony, soliloquy, aside, hamartia, catharsis, hubris).",
                "key_concepts": [
                    {
                        "concept": "Figures of Association: Synecdoche vs Metonymy",
                        "explanation": "Synecdoche: Using a PART to represent the whole, or the whole for a part (e.g. 'All hands on deck' - hands represent crew; 'Give us this day our daily bread' - bread represents food). Metonymy: Using an ASSOCIATED symbol or attribute to represent the entity (e.g. 'The Crown issued a royal pardon' - Crown represents the monarch/government; 'The pen is mightier than the sword').",
                        "examples": [
                            "'He bought a new set of wheels' = Synecdoche (wheels = car).",
                            "'Aso Rock released a statement' = Metonymy (Aso Rock = Nigerian Presidency)."
                        ]
                    },
                    {
                        "concept": "Dramatic Conventions: Irony, Soliloquy & Catharsis",
                        "explanation": "Dramatic Irony: The audience knows vital plot information that the characters on stage are ignorant of. Soliloquy: A character speaks their innermost honest thoughts alone on stage. Aside: A short remark directed to the audience or another character that others on stage cannot hear. Hamartia: The tragic flaw that brings down the protagonist. Catharsis: Purging of pity and fear experienced by the audience.",
                        "examples": [
                            "In Hamlet, Hamlet's 'To be or not to be' is a classic soliloquy."
                        ]
                    },
                    {
                        "concept": "Paradox vs Oxymoron",
                        "explanation": "Oxymoron: Placing two contradictory words directly adjacent (e.g. 'deafening silence', 'cruel kindness'). Paradox: An entire statement that appears self-contradictory on the surface but conveys a profound philosophical truth upon reflection (e.g. 'The child is father of the man').",
                        "examples": [
                            "'Cowards die many times before their deaths' is a paradox."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing Synecdoche with Metonymy: Synecdoche uses a physical PART; Metonymy uses an ASSOCIATED symbol!",
                    "Trap 2: Confusing Soliloquy with Monologue: A monologue can be delivered to other characters; a soliloquy is spoken ALONE on stage.",
                    "Trap 3: Confusing Litotes with Hyperbole: Hyperbole exaggerates; Litotes understates by negating the opposite ('no small achievement')."
                ],
                "worked_examples": [
                    {
                        "question": "The literary device in the sentence 'The White House has announced new bilateral trade tariffs' is an example of:",
                        "options": ["A. Synecdoche", "B. Metonymy", "C. Hyperbole", "D. Personification"],
                        "solution": "'The White House' is a physical building symbolically associated with the executive administration of the United States. Substituting an associated symbol for the institution is Metonymy. Correct Option: B."
                    }
                ],
                "golden_rule": "Part of the whole = Synecdoche; Associated symbol = Metonymy. Alone on stage = Soliloquy."
            },
            {
                "id": "lit_lesson_2",
                "topic": "Drama & Theatrical Techniques",
                "title": "African Drama: Soyinka, Osofisan, Tragedy, Comedy, Stage Directions & Hamartia",
                "jamb_weight": "25% of Literature Section (~10 Questions)",
                "overview": "Deep dive into theatrical genre analysis, dramatic irony, character foils, stagecraft, and textual appreciation of African drama (Wole Soyinka's 'The Lion and the Jewel', Femi Osofisan's 'Women of Owu').",
                "key_concepts": [
                    {
                        "concept": "Dramatic Structure & Character Foils",
                        "explanation": "Dramatic arc: Exposition -> Rising Action -> Climax -> Falling Action -> Denouement. Character Foil: A character whose traits sharply contrast with another to highlight specific attributes. Stage directions guide actors' movements, sound effects, and lighting, offering crucial thematic subtext.",
                        "examples": [
                            "In 'The Lion and the Jewel', Lakunle's superficial modernism serves as a direct foil to Baroka's cunning traditionalism."
                        ]
                    },
                    {
                        "concept": "Wole Soyinka: 'The Lion and the Jewel'",
                        "explanation": "Set in Ilujinle. Central conflict: The battle for Sidi (the village belle) between Baroka (the Bale, representing virile traditional power) and Lakunle (the schoolteacher, representing shallow European mimicry). Baroka tricks Sidi by feigning impotence, then outwits her. Sidi marries Baroka because he understands African reality and respects bride price, whereas Lakunle offers only empty words.",
                        "examples": [
                            "Soyinka satirizes Lakunle's pretentious mimicry of Western culture rather than celebrating uncritical modernization."
                        ]
                    },
                    {
                        "concept": "Femi Osofisan: 'Women of Owu'",
                        "explanation": "Adaptation of Euripides' 'Trojan Women'. Depicts the fall and destruction of Owu kingdom by the allied Ife and Ijebu armies. Focuses on the suffering, displacement, and grief of women and children who bear the ultimate brunt of male warmongering.",
                        "examples": [
                            "Themes: The senselessness of war, betrayal of kindred blood, and female resilience in tragedy."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Assuming Soyinka favors Lakunle over Baroka—Soyinka mercilessly mocks Lakunle's superficial Western mimicry!",
                    "Trap 2: Ignoring stage directions—JAMB frequently asks questions whose answers are found strictly in the italicized stage notes.",
                    "Trap 3: Confusing Hubris (excessive pride) with general Hamartia (tragic flaw)."
                ],
                "worked_examples": [
                    {
                        "question": "In Wole Soyinka's 'The Lion and the Jewel', why does Sidi ultimately choose to marry Baroka instead of Lakunle?",
                        "options": ["A. Baroka promised to send her to study in Europe", "B. Lakunle was far too wealthy for her village status", "C. Baroka demonstrated traditional virility and cunning, while Lakunle refused to pay the bride price", "D. The village elders threatened Sidi with banishment"],
                        "solution": "Sidi rejected Lakunle because he viewed the bride price as an uncivilized savage custom, which Sidi interpreted as an insult to her virginity and worth. Baroka outwitted her through cunning and proved his masculine vitality. Correct Option: C."
                    }
                ],
                "golden_rule": "Lakunle represents hollow Western mimicry; Baroka represents cunning traditional virility. Watch stage directions!"
            },
            {
                "id": "lit_lesson_3",
                "topic": "Poetry & Versification",
                "title": "Poetic Forms: Petrarchan vs Shakespearean Sonnets, Meter, Enjambment & Imagery",
                "jamb_weight": "25% of Literature Section (~10 Questions)",
                "overview": "Covers poetic structures: Italian/Petrarchan vs English/Shakespearean sonnets, meter and rhythm (iambic pentameter), enjambment, caesura, sound devices (alliteration, assonance, consonance), and tone vs mood.",
                "key_concepts": [
                    {
                        "concept": "The Sonnet: Petrarchan vs Shakespearean",
                        "explanation": "A 14-line poem written in iambic pentameter (10 syllables per line: da-DUM da-DUM da-DUM da-DUM da-DUM). Petrarchan (Italian): Octave (8 lines: abbaabba) stating a problem + Sestet (6 lines: cdecde or cdcdcd) resolving it. The turn at line 9 is the Volta. Shakespearean (English): 3 Quatrains (abab cdcd efef) + Rhyming Couplet (gg) delivering a concluding twist.",
                        "examples": [
                            "Petrarchan volta occurs at Line 9; Shakespearean turn occurs at the final Couplet (Line 13)."
                        ]
                    },
                    {
                        "concept": "Enjambment & Caesura",
                        "explanation": "Enjambment (Run-on line): The continuation of a sentence without terminal punctuation across line breaks or stanzas, creating rapid forward momentum. Caesura: A deliberate grammatical pause in the middle of a line indicated by a dash, comma, or semi-colon.",
                        "examples": [
                            "Enjambment mimics breathlessness, running water, or unstoppable emotional passion."
                        ]
                    },
                    {
                        "concept": "Sound Devices: Assonance vs Consonance",
                        "explanation": "Alliteration: Repetition of initial consonant sounds ('fair is foul'). Assonance: Repetition of internal vowel sounds in neighboring words ('hear the mellow wedding bells'). Consonance: Repetition of consonant sounds within or at word ends ('stroke of luck').",
                        "examples": [
                            "Assonance creates musicality and enhances emotional resonance."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing the Volta position: In a Petrarchan sonnet, the Volta is at Line 9; in a Shakespearean sonnet, it is at the final couplet (Line 13).",
                    "Trap 2: Confusing Assonance with Rhyme: Assonance is internal vowel repetition; rhyme requires matching word endings.",
                    "Trap 3: Believing all 14-line poems are Shakespearean—always check the rhyme scheme (abbaabba is Petrarchan!)."
                ],
                "worked_examples": [
                    {
                        "question": "A 14-line poem consisting of an octave rhyming ABBAABBA and a sestet rhyming CDECDE, with a thematic turn at line 9, is known as a:",
                        "options": ["A. Shakespearean Sonnet", "B. Petrarchan Sonnet", "C. Spenserian Sonnet", "D. Ballad Stanza"],
                        "solution": "An octave-sestet division with the abbaabba rhyme scheme and a volta at line 9 defines the Italian or Petrarchan Sonnet. Shakespearean sonnets consist of three quatrains and a rhyming couplet. Correct Option: B."
                    }
                ],
                "golden_rule": "Octave + Sestet (Volta at line 9) = Petrarchan; 3 Quatrains + Couplet = Shakespearean."
            },
            {
                "id": "lit_lesson_4",
                "topic": "Prose & Fictional Techniques",
                "title": "African & Non-African Prose: Narrative Point of View, Achebe, Themes & Characterization",
                "jamb_weight": "25% of Literature Section (~10 Questions)",
                "overview": "Mastering narrative perspectives (first person vs third person omniscient vs third person limited), characterization, motifs, and close critical study of African and non-African prose (Chinua Achebe's 'Things Fall Apart', Buchi Emecheta's 'The Joys of Motherhood').",
                "key_concepts": [
                    {
                        "concept": "Narrative Points of View",
                        "explanation": "First-Person ('I'/'we'): Narrator is a character inside the story; provides intimate emotional access, but is inherently limited and potentially unreliable. Third-Person Omniscient: All-knowing external narrator who can enter the minds of any character and move freely across time and space. Third-Person Limited: Follows the perspective and consciousness of only ONE character.",
                        "examples": [
                            "Things Fall Apart is narrated in the third-person omniscient voice, weaving traditional folklore and authorial wisdom."
                        ]
                    },
                    {
                        "concept": "Chinua Achebe: 'Things Fall Apart'",
                        "explanation": "Set in Umuofia. Explores the tragic collision between traditional Igbo culture and British colonial-missionary intrusion. Okonkwo's personal tragedy mirrors the communal tragedy of Umuofia. Okonkwo's tragic flaw (hamartia) is his overwhelming, morbid fear of failure and weakness—a fear born of shame toward his gentle, lazy father, Unoka.",
                        "examples": [
                            "Okonkwo kills Ikemefuna, despite the boy calling him father, solely because he is terrified of being perceived as weak."
                        ]
                    },
                    {
                        "concept": "Buchi Emecheta: 'The Joys of Motherhood'",
                        "explanation": "Depicts Nnu Ego's life in colonial Lagos and Ibuza. Satirizes the traditional patriarchal belief that a woman's entire joy, fulfillment, and identity depend on bearing sons. Despite sacrificing all her health and wealth for her children, Nnu Ego dies neglected and alone by the roadside in Lagos.",
                        "examples": [
                            "The title is profoundly ironic: motherhood brings Nnu Ego unending labor, poverty, and isolation rather than joyous fulfillment."
                        ]
                    }
                ],
                "fatal_traps": [
                    "Trap 1: Confusing Third-Person Omniscient with Third-Person Limited: Omniscient knows ALL characters' minds; Limited follows ONLY ONE.",
                    "Trap 2: Believing Okonkwo's downfall was solely caused by white colonizers—his internal tragic flaw (fear of appearing weak) was equally decisive!",
                    "Trap 3: Interpreting the title 'The Joys of Motherhood' literally—it is heavy structural irony."
                ],
                "worked_examples": [
                    {
                        "question": "In Chinua Achebe's 'Things Fall Apart', Okonkwo's internal tragic flaw that drives his actions and ultimate downfall is:",
                        "options": ["A. Extreme greed for material wealth", "B. The terrifying fear of failure and appearing weak like his father Unoka", "C. Deep-seated hatred for his wives and children", "D. Jealousy toward the clan elders"],
                        "solution": "Achebe explicitly emphasizes that Okonkwo's entire existence was dominated by fear: the fear of failure and of weakness, terrified of being perceived as soft or resembling his father Unoka, who died a debtor without titles. Correct Option: B."
                    }
                ],
                "golden_rule": "Okonkwo's flaw is fear of appearing weak! Omniscient knows all; first-person is limited and subjective."
            }
        ]
    }
    return lessons

if __name__ == "__main__":
    data = build_all_lessons()
    out_file = "data/lessons.json"
    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    
    total = sum(len(v) for v in data.values())
    print(f"Generated {total} comprehensive lessons across {len(data)} subjects in {out_file}")
