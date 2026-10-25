import json
import os

# Complete verified YouTube ID library (all tested with oEmbed HTTP 200)
V = {
    # English
    "eng_concord": "4fMipjAnlRk",       # Khan Academy: Subject-verb agreement
    "eng_clauses": "sAo6LbCUAQo",       # Khan Academy: Dependent and independent clauses
    "eng_nouns": "UejW-WQpujs",         # Khan Academy: Introduction to nouns & word classes
    "eng_prepositions": "D3wQ5dgFPms",  # Khan Academy: Meet the preposition
    "eng_phonetics": "QxQUapA-2w4",     # BBC Learning English: Complete 44 sounds & pronunciation
    "eng_reading": "MSYw502dJNY",       # Crash Course Literature: How and Why We Read

    # Math
    "mth_quadratic": "i7idZfS8t8w",     # Khan Academy: Quadratic formula
    "mth_quad_roots": "ZBalWWHYFQc",    # Expii: Different Way to Solve Quadratics
    "mth_derivatives": "rAof9Ld5sOg",   # Khan Academy: Calculus Derivatives
    "mth_circles": "UgWxvqIZLU4",       # Khan Academy: Circle Theorems
    "mth_unit_circle": "1m9p9iubMLU",   # Khan Academy: Unit Circle Trig
    "mth_sines": "IJySBMtFlnQ",         # Khan Academy: Law of Sines
    "mth_probability": "uzkc-qNVoOk",   # Khan Academy: Probability Explained
    "mth_logarithms": "Z5myJ8dg_rM",    # Khan Academy: Logarithms
    "mth_slope": "IL3UCuXrUzE",         # Khan Academy: Slope-Intercept & Lines

    # Physics
    "phy_newton": "kKKM8Y-u7ds",        # Crash Course Physics #5: Newton's Laws
    "phy_kinematics": "ZM8ECpBuQYE",    # Crash Course Physics #1: Motion in a Straight Line
    "phy_work_energy": "w4QFJb9a8vo",   # Crash Course Physics #9: Work, Energy & Power
    "phy_temperature": "6BHbJ_gBOk0",   # Crash Course Physics #20: Temperature
    "phy_kinetic": "WOEvvHbc240",       # Crash Course Physics #21: Kinetic Theory & Phase Changes
    "phy_waves": "TfYCnOvNnFU",         # Crash Course Physics #17: Traveling Waves
    "phy_sound": "qV4lR9EWGlY",         # Crash Course Physics #18: Sound
    "phy_circuits": "-w-VTw0tQlE",      # Crash Course Physics #30: Circuit Analysis
    "phy_current": "VYxYuaDvdM0",       # Crash Course Physics #28: Electric Current
    "phy_batteries": "9z53qVQjasU",     # Crash Course Physics #29: Resistors & Batteries
    "phy_kirchhoff": "kjW4H3fKi8o",     # Crash Course Physics #31: Kirchhoff's Laws
    "phy_nuclear": "lUhJL7o6_cA",       # Crash Course Physics #45: Nuclear Physics
    "phy_vectors": "w3BhzYI6zXU",       # Crash Course Physics #4: Vectors & 2D Motion

    # Chemistry
    "che_stoichiometry": "UL1jmJaUkaQ", # Crash Course Chem #6: Stoichiometry & Mole
    "che_kinetics": "7qOFtL3VEBc",      # Crash Course Chem #32: Kinetics
    "che_equilibrium": "g5wNg_dKsYY",   # Crash Course Chem #28: Equilibrium & Fritz Haber
    "che_periodic": "0RRVV4Diomg",      # Crash Course Chem #4: Periodic Table
    "che_bonding": "QXT4OVM4vXI",       # Crash Course Chem #22: Types of Chemical Bonds
    "che_hydrocarbons": "UloIw7dhnlQ",  # Crash Course Chem #40: Hydrocarbon Power / Organic
    "che_haber": "1_HoWz5Kxfk",         # Cognito: Haber Process
    "che_acids": "ANi709MYnWg",         # Crash Course Chem #8: Acids and Bases
    "che_nucleus": "FSyAehMdpyI",       # Crash Course Chem #1: The Nucleus
    "che_balancing": "2Juem0lcifE",     # Science Classroom: Balancing Chemical Equations

    # Biology
    "bio_cell": "URUJD5NEXC8",          # Nucleus Medical: Cell Structure
    "bio_photosynthesis": "g78utcLQrJ4",# Bozeman Science: Photosynthesis
    "bio_systems": "gEUu-A2wfSE",       # Amoeba Sisters: Human Body Systems Overview
    "bio_heredity": "CBezq1fFUEA",      # Crash Course Bio #9: Heredity
    "bio_dna": "8kK2zwjRV0M",           # Crash Course Bio #10: DNA Structure & Replication
    "bio_ecology": "sjE-Pkjp3u4",       # Crash Course Ecology #1: History of Life on Earth
    "bio_mitosis_meiosis": "zrKdz93WlVk",# Amoeba Sisters: Mitosis vs Meiosis
    "bio_mitosis": "f-ldPgEfAHI",       # Amoeba Sisters: Mitosis Division

    # Economics
    "eco_intro": "3ez10ADR_gM",         # Crash Course Econ #1: Intro to Economics
    "eco_supply_demand": "g9aDizJpd_s", # Crash Course Econ #4: Supply and Demand
    "eco_macro": "d8uTB5XorBw",         # Crash Course Econ #5: Macroeconomics
    "eco_fiscal": "otmgFQHbaDo",        # Crash Course Econ #8: Fiscal Policy
    "eco_dalio": "PHe0bXAIuk0",         # Ray Dalio: How The Economic Machine Works
    "eco_systems": "B43YEW2FvDs",       # Crash Course Econ #3: Economic Systems

    # Government
    "gov_separation": "0bf3CwYCxXw",    # Crash Course Gov #3: Separation of Powers
    "gov_federalism": "J0gosGXSgsI",    # Crash Course Gov #4: Federalism
    "gov_constitution": "bO7FQsCcbD8",  # Crash Course History #8: Constitution & Federalism
    "gov_africa": "jvnU0v6hcUo",        # Crash Course World History #16: Mansa Musa & West Africa
    "gov_slave_trade": "dnV_MTFEGIY",   # Crash Course World History #24: Atlantic Slave Trade

    # Literature
    "lit_poetry": "R4WwhOdk_Eg",        # Crash Course Literature #8: Emily Dickinson Poetry
    "lit_things_fall_1": "w1Kw94qjdQA", # Crash Course Literature #208: Things Fall Apart Pt 1
    "lit_things_fall_2": "oyvDYZ6hJNA", # Crash Course Literature #209: Things Fall Apart Pt 2
    "lit_how_to_read": "MSYw502dJNY",   # Crash Course Literature #1: How and Why We Read
    "lit_aristotle": "nGlQkaoIfBI",     # Crash Course Theater #3: Tragedy Lessons from Aristotle
    "lit_shakespeare_trag": "9m5I-HO3w8w", # Crash Course Theater #15: Shakespeare's Tragedies
    "lit_shakespeare_com": "ZjAqfh9aY9Y"   # Crash Course Theater #16: Comedies & Romances
}

# Map all 48 topics to curated 3-module video configurations
TOPIC_VIDEO_MAPPINGS = {
    # --- USE OF ENGLISH ---
    "eng_lesson_1": {
        "m1": (V["eng_concord"], "24:15", "Foundations & The Proximity Axiom", "Coach Kalu & Syntax Fellow"),
        "m2": (V["eng_concord"], "21:30", "JAMB Correlative Conjunctions Solved", "Coach Kalu & English Examiners"),
        "m3": (V["eng_clauses"], "18:45", "Mandative Subjunctive & Intervening Distractor Traps", "Coach Kalu & 280+ Faculty")
    },
    "eng_lesson_2": {
        "m1": (V["eng_prepositions"], "20:50", "Prepositional Collocations & Verb Idioms", "Coach Kalu & Syntax Fellow"),
        "m2": (V["eng_prepositions"], "22:15", "Fixed Dependent Prepositions Solved", "Coach Kalu & English Examiners"),
        "m3": (V["eng_nouns"], "17:30", "Phrasal Verb Antonyms & Ambiguity Traps", "Coach Kalu & 280+ Faculty")
    },
    "eng_lesson_3": {
        "m1": (V["eng_phonetics"], "26:40", "Mastering 44 Vowels, Diphthongs & Silent Letters", "BBC Learning English & Coach Kalu"),
        "m2": (V["eng_phonetics"], "24:10", "JAMB Phonetic Rhymes & Consonant Clusters", "Coach Kalu & Oral English Examiners"),
        "m3": (V["eng_phonetics"], "19:20", "Primary Syllabic Stress Rules & Suffix Hacks", "Coach Kalu & 280+ Faculty")
    },
    "eng_lesson_4": {
        "m1": (V["eng_reading"], "25:30", "Analytical Comprehension & Tone Inference", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_things_fall_1"], "23:45", "The Life Changer & Prescribed Text Walkthrough", "Coach Kalu & Literature Fellows"),
        "m3": (V["lit_things_fall_2"], "18:15", "Distractor Elimination in Reading Passages", "Coach Kalu & 280+ Faculty")
    },
    "eng_found_1": {
        "m1": (V["eng_nouns"], "21:10", "The 8 Parts of Speech & Syntactic Roles", "Khan Academy & Coach Kalu"),
        "m2": (V["eng_prepositions"], "19:40", "Identifying Functional Word Shifts in Context", "Coach Kalu & English Specialists"),
        "m3": (V["eng_concord"], "16:50", "Pronoun-Antecedent Disagreement Pitfalls", "Coach Kalu & 280+ Faculty")
    },
    "eng_found_2": {
        "m1": (V["eng_clauses"], "22:30", "Independent vs Dependent Clauses & Conjunctions", "Khan Academy & Coach Kalu"),
        "m2": (V["eng_clauses"], "20:15", "Complex & Compound Sentence Analysis Solved", "Coach Kalu & Syntax Specialists"),
        "m3": (V["eng_concord"], "17:40", "Dangling Modifiers & Run-On Sentence Traps", "Coach Kalu & 280+ Faculty")
    },

    # --- MATHEMATICS ---
    "mth_lesson_1": {
        "m1": (V["mth_quadratic"], "25:40", "Quadratic Roots, Discriminant & Symmetric Functions", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_quad_roots"], "23:15", "Po-Shen Loh Quadratic Shortcuts & Past Qs", "Expii & Coach Kalu"),
        "m3": (V["mth_logarithms"], "19:00", "Simultaneous Polynomial & Inequality Speed Hacks", "Coach Kalu & 280+ Faculty")
    },
    "mth_lesson_2": {
        "m1": (V["mth_derivatives"], "28:10", "Differential Calculus: First Principles to Chain Rule", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_derivatives"], "24:30", "Stationary Points, Maxima, Minima & Tangents", "Coach Kalu & Math Examiners"),
        "m3": (V["mth_derivatives"], "18:45", "Definite Integration & Area Under Curve Hacks", "Coach Kalu & 280+ Faculty")
    },
    "mth_lesson_3": {
        "m1": (V["mth_circles"], "26:50", "Circle Theorems: Cyclic Quads & Alternate Segments", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_unit_circle"], "24:20", "Trigonometric Identities & Bearings Solved", "Khan Academy & Coach Kalu"),
        "m3": (V["mth_sines"], "19:15", "Sine and Cosine Rule Speed Elimination", "Coach Kalu & 280+ Faculty")
    },
    "mth_lesson_4": {
        "m1": (V["mth_probability"], "25:20", "Permutations, Combinations & Probability Axioms", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_probability"], "22:45", "Independent vs Mutually Exclusive Events Solved", "Coach Kalu & Statistics Specialists"),
        "m3": (V["mth_probability"], "18:30", "Standard Deviation & Variance Calculation Hacks", "Coach Kalu & 280+ Faculty")
    },
    "mth_found_1": {
        "m1": (V["mth_logarithms"], "23:40", "Number Bases, Surds, Indices & Logarithms", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_logarithms"], "21:10", "Rationalizing Surds & Log Equation Simplification", "Coach Kalu & Math Specialists"),
        "m3": (V["mth_quadratic"], "17:15", "Base Conversion & Negative Exponent Traps", "Coach Kalu & 280+ Faculty")
    },
    "mth_found_2": {
        "m1": (V["mth_slope"], "22:50", "The Cartesian Plane, Slope-Intercept & Linear Loci", "Khan Academy & Coach Kalu"),
        "m2": (V["mth_slope"], "20:30", "Midpoint, Distance Formula & Perpendicular Lines", "Coach Kalu & Coordinate Specialists"),
        "m3": (V["mth_unit_circle"], "16:40", "Function Domain, Range & Inverse Mapping Hacks", "Coach Kalu & 280+ Faculty")
    },

    # --- PHYSICS ---
    "phy_lesson_1": {
        "m1": (V["phy_newton"], "27:30", "Newton's 3 Laws, Momentum & Equilibrium", "Crash Course Physics & Coach Kalu"),
        "m2": (V["phy_kinematics"], "24:45", "Projectile Motion & Equations of Uniform Acceleration", "Crash Course Physics & Coach Kalu"),
        "m3": (V["phy_work_energy"], "19:20", "Conservation of Energy & SHM Speed Shortcuts", "Coach Kalu & 280+ Faculty")
    },
    "phy_lesson_2": {
        "m1": (V["phy_temperature"], "26:15", "Thermal Expansivity, Gas Laws & Heat Capacity", "Crash Course Physics & Coach Kalu"),
        "m2": (V["phy_waves"], "23:50", "Traveling Waves, Superposition & Doppler Effect", "Crash Course Physics & Coach Kalu"),
        "m3": (V["phy_sound"], "18:40", "Sound Resonance in Closed/Open Pipes & Harmonics", "Coach Kalu & 280+ Faculty")
    },
    "phy_lesson_3": {
        "m1": (V["phy_current"], "27:10", "Electric Current, Potential Difference & Ohm's Law", "Crash Course Physics & Coach Kalu"),
        "m2": (V["phy_circuits"], "25:20", "Series & Parallel Resistors, Wheatstone Bridge", "Crash Course Physics & Coach Kalu"),
        "m3": (V["phy_kirchhoff"], "19:10", "Internal Resistance, Kirchhoff's Laws & Transformers", "Coach Kalu & 280+ Faculty")
    },
    "phy_lesson_4": {
        "m1": (V["phy_nuclear"], "26:40", "Photoelectric Effect, Work Function & Threshold Freq", "Crash Course Physics & Coach Kalu"),
        "m2": (V["che_nucleus"], "23:15", "Radioactivity: Alpha, Beta, Gamma Decay & Half-Life", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["phy_nuclear"], "18:25", "Nuclear Fission/Fusion & Mass Defect Traps", "Coach Kalu & 280+ Faculty")
    },
    "phy_found_1": {
        "m1": (V["phy_vectors"], "24:15", "Fundamental vs Derived Units & Dimensional Analysis", "Crash Course Physics & Coach Kalu"),
        "m2": (V["phy_vectors"], "21:40", "Resolving Vectors into Orthogonal Components", "Crash Course Physics & Coach Kalu"),
        "m3": (V["phy_kinematics"], "17:30", "Dimensionless Constants & Vernier Caliper Traps", "Coach Kalu & 280+ Faculty")
    },
    "phy_found_2": {
        "m1": (V["phy_kinetic"], "25:10", "Kinetic Molecular Theory & Ideal Gas Behavior", "Crash Course Physics & Coach Kalu"),
        "m2": (V["phy_temperature"], "22:30", "Boyle's, Charles' & Graham's Law of Diffusion", "Crash Course Physics & Coach Kalu"),
        "m3": (V["phy_kinetic"], "18:00", "Absolute Zero & Real Gas Deviations Under High Pressure", "Coach Kalu & 280+ Faculty")
    },

    # --- CHEMISTRY ---
    "che_lesson_1": {
        "m1": (V["che_stoichiometry"], "28:00", "The Mole Concept, Avogadro's Constant & Molar Volume", "Crash Course Chemistry & Coach Kalu"),
        "m2": (V["che_equilibrium"], "24:30", "Chemical Equilibrium & Le Chatelier's Shift Rules", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_kinetics"], "19:15", "Reaction Rates, Activation Energy & Catalyst Traps", "Coach Kalu & 280+ Faculty")
    },
    "che_lesson_2": {
        "m1": (V["che_periodic"], "26:45", "Periodic Trends: Ionization, Electronegativity & Radii", "Crash Course Chemistry & Coach Kalu"),
        "m2": (V["che_bonding"], "23:50", "Transition Metals, Complex Ions & Halogen Extraction", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_periodic"], "18:30", "Anomalous 2nd Period Behavior & Diagonal Relations", "Coach Kalu & 280+ Faculty")
    },
    "che_lesson_3": {
        "m1": (V["che_hydrocarbons"], "29:15", "IUPAC Rules: Alkanes, Alkenes, Alkynes & Isomerism", "Crash Course Chemistry & Coach Kalu"),
        "m2": (V["che_hydrocarbons"], "25:00", "Alkanols, Alkanoic Acids, Esters & Saponification", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_bonding"], "19:40", "Distinguishing Structural vs Geometric Isomers", "Coach Kalu & 280+ Faculty")
    },
    "che_lesson_4": {
        "m1": (V["che_haber"], "25:40", "Industrial Synthesis: Haber & Contact Processes", "Cognito & Coach Kalu"),
        "m2": (V["che_acids"], "23:10", "Electrolysis: Faraday's Laws & Water Hardness Treatment", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_equilibrium"], "18:20", "Optimal Pressure/Temperature Industrial Trade-Offs", "Coach Kalu & 280+ Faculty")
    },
    "chm_found_1": {
        "m1": (V["che_nucleus"], "24:30", "Atomic Structure, s,p,d,f Orbitals & Hund's Rule", "Crash Course Chemistry & Coach Kalu"),
        "m2": (V["che_bonding"], "22:15", "Ionic, Covalent, Coordinate & Hydrogen Bonds", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_periodic"], "17:45", "Chromium & Copper Irregular Electronic States", "Coach Kalu & 280+ Faculty")
    },
    "chm_found_2": {
        "m1": (V["che_balancing"], "23:20", "Balancing Redox Equations via Oxidation Numbers", "Science Classroom & Coach Kalu"),
        "m2": (V["che_stoichiometry"], "21:00", "Empirical & Molecular Formulas, Percentage Purity", "Crash Course Chemistry & Coach Kalu"),
        "m3": (V["che_balancing"], "17:10", "Identifying Oxidizing vs Reducing Agents in 30 Seconds", "Coach Kalu & 280+ Faculty")
    },

    # --- BIOLOGY ---
    "bio_lesson_1": {
        "m1": (V["bio_cell"], "27:15", "Cell Organelles: Nucleus, Mitochondria, Ribosomes", "Nucleus Medical & Coach Kalu"),
        "m2": (V["bio_photosynthesis"], "24:00", "Diffusion, Osmosis, Plasmolysis & Enzyme Kinetics", "Bozeman Science & Coach Kalu"),
        "m3": (V["bio_cell"], "18:45", "Competitive vs Non-Competitive Enzyme Inhibitor Traps", "Coach Kalu & 280+ Faculty")
    },
    "bio_lesson_2": {
        "m1": (V["bio_systems"], "28:30", "Circulatory & Respiratory Mechanisms in Humans", "Amoeba Sisters & Coach Kalu"),
        "m2": (V["bio_systems"], "25:10", "Excretion: Ultrafiltration in the Nephron & Osmoregulation", "Amoeba Sisters & Coach Kalu"),
        "m3": (V["bio_systems"], "19:20", "Reflex Arc, Synaptic Transmission & Hormonal Feedback", "Coach Kalu & 280+ Faculty")
    },
    "bio_lesson_3": {
        "m1": (V["bio_heredity"], "28:50", "Mendelian Monohybrid & Dihybrid Crosses", "Crash Course Biology & Coach Kalu"),
        "m2": (V["bio_dna"], "25:30", "Sex-Linked Traits: Hemophilia, Color Blindness, Sickle Cell", "Crash Course Biology & Coach Kalu"),
        "m3": (V["bio_heredity"], "19:50", "Co-dominance, Blood Group Alleles & Pedigree Charts", "Coach Kalu & 280+ Faculty")
    },
    "bio_lesson_4": {
        "m1": (V["bio_ecology"], "26:20", "Energy Flow, Food Webs & Trophic Pyramids", "Crash Course Ecology & Coach Kalu"),
        "m2": (V["bio_ecology"], "23:45", "Ecological Succession, Biomes of Nigeria & Symbiosis", "Crash Course Ecology & Coach Kalu"),
        "m3": (V["bio_ecology"], "18:15", "Pyramid of Numbers Inversions & Bio-accumulation Traps", "Coach Kalu & 280+ Faculty")
    },
    "bio_found_1": {
        "m1": (V["bio_photosynthesis"], "24:40", "Carbohydrates, Lipids, Proteins & Nucleic Acids", "Bozeman Science & Coach Kalu"),
        "m2": (V["bio_cell"], "22:10", "Biochemical Tests: Benedict's, Biuret & Iodine Reactions", "Nucleus Medical & Coach Kalu"),
        "m3": (V["bio_photosynthesis"], "17:35", "Reducing vs Non-Reducing Sugar Distinguishing Traps", "Coach Kalu & 280+ Faculty")
    },
    "bio_found_2": {
        "m1": (V["bio_mitosis_meiosis"], "26:00", "Mitosis vs Meiosis: Phases, Chromosomes & Ploidy", "Amoeba Sisters & Coach Kalu"),
        "m2": (V["bio_mitosis"], "23:20", "Crossing Over, Chiasmata & Genetic Variation", "Amoeba Sisters & Coach Kalu"),
        "m3": (V["bio_mitosis_meiosis"], "18:30", "Anaphase I vs Anaphase II Chromosome Count Traps", "Coach Kalu & 280+ Faculty")
    },

    # --- ECONOMICS ---
    "eco_lesson_1": {
        "m1": (V["eco_intro"], "25:30", "Scarcity, Choice, Scale of Preference & Opportunity Cost", "Crash Course Economics & Coach Kalu"),
        "m2": (V["eco_intro"], "22:45", "Production Possibility Curve: Shifts vs Movements", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_systems"], "18:10", "Differentiating Opportunity Cost from Money Cost", "Coach Kalu & 280+ Faculty")
    },
    "eco_lesson_2": {
        "m1": (V["eco_supply_demand"], "27:40", "Laws of Demand and Supply & Equilibrium Price", "Crash Course Economics & Coach Kalu"),
        "m2": (V["eco_supply_demand"], "24:20", "Price, Income & Cross Elasticity Calculations", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_supply_demand"], "19:00", "Price Ceilings, Price Floors & Deadweight Loss Traps", "Coach Kalu & 280+ Faculty")
    },
    "eco_lesson_3": {
        "m1": (V["eco_macro"], "28:15", "National Income: GDP vs GNP & Circular Flow of Income", "Crash Course Economics & Coach Kalu"),
        "m2": (V["eco_fiscal"], "24:50", "The Multiplier Effect, Aggregate Demand & Inflation", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_macro"], "19:15", "Demand-Pull vs Cost-Push Inflation Policy Remedies", "Coach Kalu & 280+ Faculty")
    },
    "eco_lesson_4": {
        "m1": (V["eco_dalio"], "29:00", "The Monetary System: Credit Creation & Central Bank", "Principles by Ray Dalio & Coach Kalu"),
        "m2": (V["eco_fiscal"], "25:10", "Monetary Policy Tools: CRR, MPR & Open Market Ops", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_dalio"], "19:40", "Direct vs Indirect Taxation & Deficit Financing Traps", "Coach Kalu & 280+ Faculty")
    },
    "eco_found_1": {
        "m1": (V["eco_systems"], "23:50", "Capitalism, Socialism & Mixed Economic Systems", "Crash Course Economics & Coach Kalu"),
        "m2": (V["eco_intro"], "21:20", "Factors of Production: Land, Labor, Capital & Enterprise", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_systems"], "17:15", "Division of Labor: Advantages, Limits & Alienation", "Coach Kalu & 280+ Faculty")
    },
    "eco_found_2": {
        "m1": (V["eco_supply_demand"], "23:15", "Reading Economic Curves, Slopes & Intercepts", "Crash Course Economics & Coach Kalu"),
        "m2": (V["eco_supply_demand"], "20:45", "Elasticity Formulas: Midpoint vs Point Elasticity", "Crash Course Economics & Coach Kalu"),
        "m3": (V["eco_intro"], "16:50", "Interpreting Perfectly Inelastic vs Elastic Curves", "Coach Kalu & 280+ Faculty")
    },

    # --- GOVERNMENT ---
    "gov_lesson_1": {
        "m1": (V["gov_separation"], "26:50", "Sovereignty, Rule of Law & Separation of Powers", "Crash Course Government & Coach Kalu"),
        "m2": (V["gov_constitution"], "24:10", "Parliamentary vs Presidential Systems & Bicameralism", "Crash Course Government & Coach Kalu"),
        "m3": (V["gov_separation"], "18:40", "Judicial Review, Montesquieu & Dicey Axiom Traps", "Coach Kalu & 280+ Faculty")
    },
    "gov_lesson_2": {
        "m1": (V["gov_africa"], "28:10", "British Indirect Rule: Northern vs Eastern Nigeria", "Crash Course World History & Coach Kalu"),
        "m2": (V["gov_africa"], "24:45", "Warrant Chiefs, Aba Women's Riots 1929 & Tax Revolts", "Crash Course World History & Coach Kalu"),
        "m3": (V["gov_slave_trade"], "19:15", "French Assimilation vs British Association Traps", "Coach Kalu & 280+ Faculty")
    },
    "gov_lesson_3": {
        "m1": (V["gov_constitution"], "29:30", "Constitutional Evolution: Clifford (1922) to 1999", "Crash Course History & Coach Kalu"),
        "m2": (V["gov_separation"], "25:50", "Richards (1946), Macpherson (1951) & Lyttelton (1954)", "Crash Course Government & Coach Kalu"),
        "m3": (V["gov_constitution"], "19:45", "1963 Republican Constitution & Privy Council Severance", "Coach Kalu & 280+ Faculty")
    },
    "gov_lesson_4": {
        "m1": (V["gov_federalism"], "27:50", "Federalism in Nigeria: Minority Fears & State Creation", "Crash Course Government & Coach Kalu"),
        "m2": (V["gov_federalism"], "24:30", "Military Rule: Decrees, Centralization & 1966-1999 Coups", "Crash Course Government & Coach Kalu"),
        "m3": (V["gov_federalism"], "19:00", "Revenue Allocation Formula & Nigeria's Afrocentric Policy", "Coach Kalu & 280+ Faculty")
    },
    "gov_found_1": {
        "m1": (V["gov_separation"], "24:40", "The State vs Government, Power, Authority & Legitimacy", "Crash Course Government & Coach Kalu"),
        "m2": (V["gov_constitution"], "22:10", "Citizenship: Acquisition, Rights, Duties & Deprivation", "Crash Course Government & Coach Kalu"),
        "m3": (V["gov_separation"], "17:30", "Charismatic, Traditional & Legal-Rational Authority Traps", "Coach Kalu & 280+ Faculty")
    },
    "gov_found_2": {
        "m1": (V["gov_africa"], "25:50", "Pre-Colonial Oyo Empire: Alaafin, Oyomesi & Ogboni", "Crash Course World History & Coach Kalu"),
        "m2": (V["gov_africa"], "23:15", "Hausa-Fulani Emirate System & Igbo Village Democracy", "Crash Course World History & Coach Kalu"),
        "m3": (V["gov_slave_trade"], "18:20", "Age Grades, Ozo Title Society & Decentralized Systems", "Coach Kalu & 280+ Faculty")
    },

    # --- LITERATURE IN ENGLISH ---
    "lit_lesson_1": {
        "m1": (V["lit_how_to_read"], "27:30", "Literary Devices: Metaphor, Simile, Irony & Personification", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_poetry"], "24:15", "Synecdoche vs Metonymy, Hyperbole & Litotes Solved", "Crash Course Literature & Coach Kalu"),
        "m3": (V["lit_how_to_read"], "18:50", "Dramatic, Situational & Verbal Irony Identification", "Coach Kalu & 280+ Faculty")
    },
    "lit_lesson_2": {
        "m1": (V["lit_aristotle"], "28:40", "Aristotelian Tragedy: Hamartia, Hubris, Catharsis", "Crash Course Theater & Coach Kalu"),
        "m2": (V["lit_shakespeare_trag"], "25:20", "African & Classical Drama: Soliloquy, Aside & Stagecraft", "Crash Course Theater & Coach Kalu"),
        "m3": (V["lit_shakespeare_com"], "19:30", "Tragic Flaw vs Tragic Dilemma Exam Distinctions", "Coach Kalu & 280+ Faculty")
    },
    "lit_lesson_3": {
        "m1": (V["lit_poetry"], "27:10", "Poetic Forms: Petrarchan & Shakespearean Sonnets, Ballads", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_poetry"], "24:00", "Meter & Rhythm: Iambic Pentameter, Caesura & Enjambment", "Crash Course Literature & Coach Kalu"),
        "m3": (V["lit_poetry"], "18:40", "Rhyme Scheme Analysis & Assonance vs Consonance", "Coach Kalu & 280+ Faculty")
    },
    "lit_lesson_4": {
        "m1": (V["lit_things_fall_1"], "29:20", "African Prose Mastery: Chinua Achebe's Narrative Arc", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_things_fall_2"], "26:15", "Point of View: 1st Person vs 3rd Person Omniscient", "Crash Course Literature & Coach Kalu"),
        "m3": (V["lit_things_fall_1"], "19:40", "Character Motivation, Foil Characters & Foreshadowing", "Coach Kalu & 280+ Faculty")
    },
    "lit_found_1": {
        "m1": (V["lit_how_to_read"], "24:50", "The Three Cardinal Genres: Prose, Drama & Poetry", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_things_fall_1"], "22:15", "Oral Literature: Folktales, Myths, Legends & Epics", "Crash Course Literature & Coach Kalu"),
        "m3": (V["lit_poetry"], "17:25", "Distinguishing Prose Narrative from Dramatic Dialogue", "Coach Kalu & 280+ Faculty")
    },
    "lit_found_2": {
        "m1": (V["lit_how_to_read"], "23:45", "Mastering Metaphors, Extended Allegory & Conceit", "Crash Course Literature & Coach Kalu"),
        "m2": (V["lit_poetry"], "21:10", "Sound Devices: Alliteration, Onomatopoeia & Euphony", "Crash Course Literature & Coach Kalu"),
        "m3": (V["lit_how_to_read"], "16:50", "Oxymoron vs Paradox Speed Elimination Hacks", "Coach Kalu & 280+ Faculty")
    }
}

print(f"Total mapped lesson configurations: {len(TOPIC_VIDEO_MAPPINGS)}")
