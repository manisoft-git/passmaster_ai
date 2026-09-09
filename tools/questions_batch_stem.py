# STEM questions batch: Mathematics, Physics, Chemistry, Biology

math_questions = [
    {
        "id": "mth_012",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Logarithms",
        "year": 2024,
        "question": "If log₁₀ 2 = 0.3010 and log₁₀ 3 = 0.4771, evaluate log₁₀ 18 without using tables.",
        "options": {"A": "1.2552", "B": "0.9542", "C": "1.5563", "D": "0.7781"},
        "correct_option": "A",
        "traps": {
            "B": "You evaluated 2 × log 3 without adding log 2.",
            "C": "You incorrectly multiplied log values instead of adding: log(a × b) = log a + log b.",
            "D": "You simply added log 2 + log 3 = log 6, missing that 18 = 2 × 3²."
        },
        "pedagogical_concept": "Logarithmic Expansion: log(18) = log(2 × 3²) = log 2 + 2 log 3 = 0.3010 + 2(0.4771) = 0.3010 + 0.9542 = 1.2552.",
        "socratic_prompt": "How can 18 be expressed as a product of prime factors involving 2 and 3?"
    },
    {
        "id": "mth_013",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Progressions",
        "year": 2023,
        "question": "The 3rd term of an arithmetic progression (AP) is 10 and the 8th term is 25. Find the first term (a) and common difference (d).",
        "options": {"A": "a = 4, d = 3", "B": "a = 3, d = 4", "C": "a = 2, d = 5", "D": "a = 5, d = 2"},
        "correct_option": "A",
        "traps": {
            "B": "You inverted the values of a and d.",
            "C": "You set 8 - 3 = 6 instead of 5.",
            "D": "Arithmetic error in solving simultaneous linear equations."
        },
        "pedagogical_concept": "AP nth Term: T_n = a + (n - 1)d. T₃ = a + 2d = 10; T₈ = a + 7d = 25. Subtracting gives 5d = 15 => d = 3. Then a + 2(3) = 10 => a = 4.",
        "socratic_prompt": "If moving from the 3rd term to the 8th term takes 5 common differences (5d), what is the value of d?"
    },
    {
        "id": "mth_014",
        "subject": "Mathematics",
        "topic": "Calculus",
        "subtopic": "Stationary Points",
        "year": 2024,
        "question": "Find the coordinates of the turning point of the curve y = 2x² - 8x + 5 and determine its nature.",
        "options": {
            "A": "(2, -3), Minimum",
            "B": "(2, -3), Maximum",
            "C": "(-2, 29), Minimum",
            "D": "(4, 5), Maximum"
        },
        "correct_option": "A",
        "traps": {
            "B": "Second derivative is positive (+4), which corresponds to a MINIMUM, not a maximum!",
            "C": "You made a sign error when solving 4x - 8 = 0, getting x = -2 instead of x = 2.",
            "D": "You set dy/dx = 2x - 8 instead of 4x - 8."
        },
        "pedagogical_concept": "Turning Points & Second Derivative: dy/dx = 4x - 8 = 0 => x = 2. When x = 2, y = 2(4) - 8(2) + 5 = 8 - 16 + 5 = -3. d²y/dx² = +4 > 0, confirming a local minimum.",
        "socratic_prompt": "When the second derivative d²y/dx² is positive, is the curve concave up (minimum) or concave down (maximum)?"
    },
    {
        "id": "mth_015",
        "subject": "Mathematics",
        "topic": "Calculus",
        "subtopic": "Definite Integration",
        "year": 2023,
        "question": "Evaluate the definite integral ∫ [1 to 3] (3x² - 2x + 1) dx.",
        "options": {"A": "20", "B": "26", "C": "18", "D": "22"},
        "correct_option": "A",
        "traps": {
            "B": "You evaluated only at the upper limit 3 without subtracting the lower limit evaluation at 1.",
            "C": "Arithmetic slip when computing 3³ - 3² + 3.",
            "D": "You forgot the integral of the constant term 1."
        },
        "pedagogical_concept": "Definite Integral: ∫ (3x² - 2x + 1) dx = [x³ - x² + x]. At 3: 27 - 9 + 3 = 21. At 1: 1 - 1 + 1 = 1. Value = 21 - 1 = 20.",
        "socratic_prompt": "What is the antiderivative of 3x² - 2x + 1, and what do you get when you subtract F(1) from F(3)?"
    },
    {
        "id": "mth_016",
        "subject": "Mathematics",
        "topic": "Geometry & Trigonometry",
        "subtopic": "Circle Theorems",
        "year": 2024,
        "question": "In a circle with center O, chords AB and CD intersect at right angles at point P. If angle BAC = 35°, find angle ABD.",
        "options": {"A": "55°", "B": "35°", "C": "70°", "D": "45°"},
        "correct_option": "A",
        "traps": {
            "B": "You assumed angles in alternate positions must be equal without using the right triangle property.",
            "C": "You doubled the angle, confusing angle at circumference with angle at center.",
            "D": "You guessed an arbitrary acute angle."
        },
        "pedagogical_concept": "Circle Geometry: Triangle APB is a right-angled triangle at P (since chords intersect at 90°). In right triangle APB, ∠PAB = 35°, therefore ∠PBA = 90° - 35° = 55°.",
        "socratic_prompt": "In a right-angled triangle where one acute angle is 35°, what must the other acute angle be?"
    },
    {
        "id": "mth_017",
        "subject": "Mathematics",
        "topic": "Geometry & Trigonometry",
        "subtopic": "Trigonometric Identities",
        "year": 2023,
        "question": "If sin θ = 3/5 and θ is acute, find the exact value of tan θ + sec θ.",
        "options": {"A": "2", "B": "7/4", "C": "1/2", "D": "4/3"},
        "correct_option": "A",
        "traps": {
            "B": "Arithmetic addition error: 3/4 + 5/4 = 8/4 = 2, not 7/4.",
            "C": "You inverted the trigonometric ratios.",
            "D": "You calculated only tan θ = 3/4 without adding sec θ = 5/4."
        },
        "pedagogical_concept": "Pythagorean Triplet: Opposite = 3, Hypotenuse = 5 => Adjacent = √(25 - 9) = 4. tan θ = 3/4, sec θ = 1/cos θ = 5/4. Sum = 3/4 + 5/4 = 8/4 = 2.",
        "socratic_prompt": "Using a 3-4-5 right triangle, what are the values of tan θ (opp/adj) and sec θ (hyp/adj)?"
    },
    {
        "id": "mth_018",
        "subject": "Mathematics",
        "topic": "Statistics & Probability",
        "subtopic": "Permutations & Combinations",
        "year": 2024,
        "question": "In how many distinct ways can the letters of the word 'NIGERIA' be arranged?",
        "options": {"A": "2520", "B": "5040", "C": "1260", "D": "720"},
        "correct_option": "A",
        "traps": {
            "B": "You evaluated 7! (5040) without dividing by 2! for the repeated letter 'I'.",
            "C": "You mistakenly divided by 4 instead of 2!.",
            "D": "You calculated 6! instead of 7! / 2!."
        },
        "pedagogical_concept": "Permutation of Repeated Elements: Total letters n = 7. The letter 'I' appears 2 times. Total unique arrangements = 7! / 2! = 5040 / 2 = 2520.",
        "socratic_prompt": "When letters in a word repeat, do you multiply or divide the total factorial by the factorial of the repeated count?"
    },
    {
        "id": "mth_019",
        "subject": "Mathematics",
        "topic": "Statistics & Probability",
        "subtopic": "Standard Deviation",
        "year": 2023,
        "question": "Find the variance of the numbers 2, 4, 6, 8, 10.",
        "options": {"A": "8", "B": "2.83", "C": "10", "D": "4"},
        "correct_option": "A",
        "traps": {
            "B": "2.83 is the standard deviation (√8), not the variance!",
            "C": "You computed the range (10 - 2 = 8) or added incorrectly.",
            "D": "You divided by n - 1 or made an arithmetic error in squaring deviations."
        },
        "pedagogical_concept": "Variance Calculation: Mean = (2+4+6+8+10)/5 = 30/5 = 6. Deviations from mean: -4, -2, 0, 2, 4. Squared deviations: 16, 4, 0, 4, 16. Sum of squares = 40. Variance = 40 / 5 = 8.",
        "socratic_prompt": "What is the formula for population variance: is it the average of the squared deviations from the mean?"
    },
    {
        "id": "mth_020",
        "subject": "Mathematics",
        "topic": "Algebra",
        "subtopic": "Matrices",
        "year": 2024,
        "question": "Find the determinant of the 2x2 matrix A = [[3, -2], [5, 4]].",
        "options": {"A": "22", "B": "2", "C": "-2", "D": "14"},
        "correct_option": "A",
        "traps": {
            "B": "You computed 12 - 10 = 2, forgetting that (-2) × 5 = -10, so subtracting gives 12 - (-10) = +22.",
            "C": "Sign confusion in the diagonal multiplication formula.",
            "D": "You subtracted the columns instead of cross-multiplying diagonals."
        },
        "pedagogical_concept": "2x2 Matrix Determinant: det(A) = ad - bc = (3 × 4) - (-2 × 5) = 12 - (-10) = 12 + 10 = 22.",
        "socratic_prompt": "In det(A) = ad - bc, what happens when bc is a negative product (-10)?"
    }
]

physics_questions = [
    {
        "id": "phy_011",
        "subject": "Physics",
        "topic": "Mechanics",
        "subtopic": "Linear Momentum",
        "year": 2024,
        "question": "A bullet of mass 0.05 kg is fired horizontally with a speed of 400 m/s into a stationary wooden block of mass 1.95 kg. If the bullet becomes embedded in the block, calculate the common velocity of the combination.",
        "options": {"A": "10 m/s", "B": "20 m/s", "C": "10.25 m/s", "D": "5 m/s"},
        "correct_option": "A",
        "traps": {
            "B": "You divided momentum by 1.0 kg instead of the combined mass (0.05 + 1.95 = 2.0 kg).",
            "C": "You neglected the bullet's mass in the combined system denominator.",
            "D": "Arithmetic division error."
        },
        "pedagogical_concept": "Conservation of Linear Momentum (Inelastic Collision): m₁u₁ + m₂u₂ = (m₁ + m₂)v. (0.05 × 400) + 0 = (0.05 + 1.95)v => 20 = 2.0v => v = 10 m/s.",
        "socratic_prompt": "When an object embeds into another, what is the total mass of the moving system after impact?"
    },
    {
        "id": "phy_012",
        "subject": "Physics",
        "topic": "Mechanics",
        "subtopic": "Work-Energy Theorem",
        "year": 2023,
        "question": "A force of 50 N acts on a 4 kg body initially at rest over a distance of 8 m. Calculate the final kinetic energy acquired by the body.",
        "options": {"A": "400 J", "B": "200 J", "C": "100 J", "D": "800 J"},
        "correct_option": "A",
        "traps": {
            "B": "You divided by 2 assuming KE = 1/2 W.",
            "C": "You multiplied mass by distance instead of force by distance.",
            "D": "You multiplied by mass unnecessarily."
        },
        "pedagogical_concept": "Work-Energy Theorem: Work done by the net force equals the change in kinetic energy: W = F × d = ΔKE. W = 50 N × 8 m = 400 J. Since initial KE = 0, final KE = 400 J.",
        "socratic_prompt": "Does the work-energy theorem state that net work done directly equals change in kinetic energy?"
    },
    {
        "id": "phy_013",
        "subject": "Physics",
        "topic": "Thermal Physics & Waves",
        "subtopic": "Specific Heat Capacity",
        "year": 2024,
        "question": "An electric heater rated at 1000 W heats 2 kg of water for 420 seconds. If specific heat capacity of water is 4200 J/kg·K, find the temperature rise (assuming no heat loss).",
        "options": {"A": "50 K", "B": "25 K", "C": "100 K", "D": "42 K"},
        "correct_option": "A",
        "traps": {
            "B": "You forgot the mass of 2 kg or divided twice.",
            "C": "You neglected the factor of 2 in mass (420,000 / 4200 = 100).",
            "D": "You confused time (420 s) with specific heat (4200)."
        },
        "pedagogical_concept": "Electrical Heat Transfer: Electrical energy E = P × t = 1000 × 420 = 420,000 J. Heat absorbed Q = mcΔθ => 420,000 = 2 × 4200 × Δθ = 8400 × Δθ => Δθ = 420,000 / 8400 = 50 K.",
        "socratic_prompt": "What is the total electrical energy delivered in 420 seconds by a 1000 W heater, and how is it related to mcΔθ?"
    },
    {
        "id": "phy_014",
        "subject": "Physics",
        "topic": "Thermal Physics & Waves",
        "subtopic": "Wave Refraction & Critical Angle",
        "year": 2023,
        "question": "The refractive index of a dense glass prism is 1.50. Calculate the critical angle for total internal reflection at the glass-air interface.",
        "options": {"A": "41.8°", "B": "48.6°", "C": "30.0°", "D": "60.0°"},
        "correct_option": "A",
        "traps": {
            "B": "You calculated sin⁻¹(1.50 - 1) or used water's refractive index (1.33).",
            "C": "sin(30°) = 0.5, which would correspond to n = 2.0, not 1.50.",
            "D": "You inverted the angle from 90° - 30°."
        },
        "pedagogical_concept": "Critical Angle: sin c = 1 / n = 1 / 1.50 = 0.6667. c = sin⁻¹(0.6667) = 41.8°.",
        "socratic_prompt": "What is the relationship between critical angle c and refractive index n when light travels from a denser medium into air?"
    },
    {
        "id": "phy_015",
        "subject": "Physics",
        "topic": "Electricity & Magnetism",
        "subtopic": "Electrical Power",
        "year": 2024,
        "question": "An electric iron has a resistance of 44 Ω and is connected to a 220 V mains supply. Calculate the electrical energy consumed in 30 minutes in kilowatt-hours (kWh).",
        "options": {"A": "0.55 kWh", "B": "1.10 kWh", "C": "33 kWh", "D": "0.28 kWh"},
        "correct_option": "A",
        "traps": {
            "B": "You calculated for 1 full hour (60 minutes) instead of 30 minutes (0.5 hour).",
            "C": "You multiplied power in watts by minutes without converting to kW and hours.",
            "D": "You used 15 minutes instead of 30."
        },
        "pedagogical_concept": "Electrical Energy in kWh: Power P = V² / R = (220)² / 44 = 48,400 / 44 = 1100 W = 1.1 kW. Time t = 30 min = 0.5 h. Energy = P × t = 1.1 kW × 0.5 h = 0.55 kWh.",
        "socratic_prompt": "How many kilowatts is 1100 W, and what fraction of an hour is 30 minutes?"
    },
    {
        "id": "phy_016",
        "subject": "Physics",
        "topic": "Electricity & Magnetism",
        "subtopic": "Magnetic Force",
        "year": 2023,
        "question": "A straight wire of length 0.5 m carrying a current of 4 A is placed in a uniform magnetic field of 0.8 T at an angle of 30° to the field lines. Find the magnetic force on the wire.",
        "options": {"A": "0.80 N", "B": "1.60 N", "C": "0.40 N", "D": "1.38 N"},
        "correct_option": "A",
        "traps": {
            "B": "You forgot sin(30°) = 0.5, calculating F = BIL.",
            "C": "You divided by 2 twice.",
            "D": "You used cos(30°) instead of sin(30°)."
        },
        "pedagogical_concept": "Magnetic Force on Current-Carrying Conductor: F = B × I × L × sin θ = 0.8 × 4 × 0.5 × sin(30°) = 1.6 × 0.5 = 0.80 N.",
        "socratic_prompt": "What is the formula for the magnetic force on a wire at an angle θ to a magnetic field?"
    },
    {
        "id": "phy_017",
        "subject": "Physics",
        "topic": "Modern & Atomic Physics",
        "subtopic": "Photoelectric Effect",
        "year": 2024,
        "question": "The work function of a metal surface is 2.5 eV. If light of photon energy 4.1 eV strikes the surface, what is the maximum kinetic energy of emitted photoelectrons?",
        "options": {"A": "1.6 eV", "B": "6.6 eV", "C": "2.5 eV", "D": "0.6 eV"},
        "correct_option": "A",
        "traps": {
            "B": "You added the energies instead of subtracting: E = W₀ + KE => KE = E - W₀.",
            "C": "You picked the work function value.",
            "D": "Arithmetic subtraction error."
        },
        "pedagogical_concept": "Photoelectric Equation: KE_max = E_photon - W₀ = 4.1 eV - 2.5 eV = 1.6 eV.",
        "socratic_prompt": "If an incident photon provides 4.1 eV and the metal requires 2.5 eV to release the electron, how much excess energy remains as kinetic energy?"
    },
    {
        "id": "phy_018",
        "subject": "Physics",
        "topic": "Modern & Atomic Physics",
        "subtopic": "Radioactive Half-Life",
        "year": 2023,
        "question": "After 24 days, the activity of a radioactive isotope has dropped to 1/16 of its initial value. What is the half-life of the isotope?",
        "options": {"A": "6 days", "B": "4 days", "C": "8 days", "D": "12 days"},
        "correct_option": "A",
        "traps": {
            "B": "4 is the number of half-lives elapsed (2⁴ = 16), not the half-life in days!",
            "C": "You divided 24 by 3 instead of 4.",
            "D": "You divided 24 by 2."
        },
        "pedagogical_concept": "Half-Life Calculation: Fraction remaining = (1/2)^n = 1/16 = (1/2)⁴ => n = 4 half-lives. Total time t = n × T_half => 24 days = 4 × T_half => T_half = 24 / 4 = 6 days.",
        "socratic_prompt": "If a sample decays to 1/16 of its initial amount, how many half-lives have passed?"
    }
]

chemistry_questions = [
    {
        "id": "chm_010",
        "subject": "Chemistry",
        "topic": "Physical & General Chemistry",
        "subtopic": "Gas Stoichiometry",
        "year": 2024,
        "question": "What volume of oxygen gas measured at s.t.p. is required for the complete combustion of 5.6 dm³ of methane (CH₄) gas at s.t.p.?",
        "options": {"A": "11.2 dm³", "B": "5.6 dm³", "C": "22.4 dm³", "D": "2.8 dm³"},
        "correct_option": "A",
        "traps": {
            "B": "You used a 1:1 mole ratio, forgetting that combustion requires 2 moles of O₂ per mole of CH₄.",
            "C": "You calculated for 1 full mole of methane at s.t.p.",
            "D": "You divided by 2 instead of multiplying by 2."
        },
        "pedagogical_concept": "Gay-Lussac's Law of Combining Volumes: CH₄(g) + 2O₂(g) -> CO₂(g) + 2H₂O(l). 1 volume of CH₄ requires 2 volumes of O₂. Therefore, 5.6 dm³ CH₄ requires 5.6 × 2 = 11.2 dm³ O₂.",
        "socratic_prompt": "In the balanced equation for the complete combustion of methane, how many moles of oxygen react with 1 mole of CH₄?"
    },
    {
        "id": "chm_011",
        "subject": "Chemistry",
        "topic": "Physical & General Chemistry",
        "subtopic": "Le Chatelier's Principle",
        "year": 2023,
        "question": "For the endothermic synthesis: 2NO₂(g) [brown] ⇌ N₂O₄(g) [colorless], ΔH = -57 kJ/mol. What will happen to the color when the mixture is heated?",
        "options": {
            "A": "The brown color deepens because equilibrium shifts to the left",
            "B": "The mixture turns completely colorless because equilibrium shifts right",
            "C": "No change in color occurs because temperature does not affect equilibrium",
            "D": "The mixture turns blue"
        },
        "correct_option": "A",
        "traps": {
            "B": "The forward reaction is exothermic (ΔH is negative). Heating an exothermic reaction shifts equilibrium to the LEFT, producing more brown NO₂!",
            "C": "Temperature always shifts dynamic chemical equilibrium when ΔH ≠ 0.",
            "D": "Blue is an irrelevant distractor."
        },
        "pedagogical_concept": "Le Chatelier's Temperature Shift: The forward reaction is exothermic (releases heat). Adding heat shifts equilibrium in the endothermic direction (reverse), increasing the concentration of brown NO₂ gas.",
        "socratic_prompt": "When heat is added to an exothermic reaction (ΔH < 0), which direction relieves the heat stress?"
    },
    {
        "id": "chm_012",
        "subject": "Chemistry",
        "topic": "Inorganic Chemistry",
        "subtopic": "Periodic Table Trends",
        "year": 2024,
        "question": "Why does Nitrogen (atomic number 7) have a higher first ionization energy than Oxygen (atomic number 8)?",
        "options": {
            "A": "Nitrogen has a stable half-filled 2p³ subshell",
            "B": "Nitrogen has a smaller atomic radius than oxygen",
            "C": "Nitrogen has more electron shells than oxygen",
            "D": "Oxygen has fewer protons in its nucleus"
        },
        "correct_option": "A",
        "traps": {
            "B": "Oxygen is further to the right in Period 2, so oxygen has a smaller atomic radius than nitrogen, not larger!",
            "C": "Both nitrogen and oxygen reside in Period 2 with exactly 2 electron shells.",
            "D": "Oxygen has 8 protons while nitrogen has 7 protons."
        },
        "pedagogical_concept": "Half-Filled Subshell Stability: Nitrogen has electronic configuration 1s² 2s² 2p³. A half-filled p-subshell (one electron in each p_x, p_y, p_z orbital) confers exceptional exchange energy stability, requiring more energy to remove an electron than from oxygen (2p⁴), which has electron pairing repulsion.",
        "socratic_prompt": "What extra stability does Hund's rule grant to an atom with a half-filled p³ orbital subshell?"
    },
    {
        "id": "chm_013",
        "subject": "Chemistry",
        "topic": "Inorganic Chemistry",
        "subtopic": "Qualitative Analysis",
        "year": 2023,
        "question": "Which of the following gases turns moist red litmus paper blue and forms dense white fumes when exposed to a glass rod dipped in concentrated HCl?",
        "options": {"A": "Ammonia (NH₃)", "B": "Sulfur dioxide (SO₂)", "C": "Chlorine (Cl₂)", "D": "Carbon dioxide (CO₂)"},
        "correct_option": "A",
        "traps": {
            "B": "SO₂ is acidic and turns blue litmus red.",
            "C": "Cl₂ bleaches litmus paper white.",
            "D": "CO₂ is an acidic oxide, not an alkaline gas."
        },
        "pedagogical_concept": "Confirmatory Test for Ammonia: NH₃ is the only common alkaline gas (turns red litmus blue). It reacts with HCl fumes to form solid ammonium chloride smoke: NH₃(g) + HCl(g) -> NH₄Cl(s) (dense white fumes).",
        "socratic_prompt": "What common laboratory gas is basic/alkaline and reacts with hydrochloric acid vapor to produce white smoke?"
    },
    {
        "id": "chm_014",
        "subject": "Chemistry",
        "topic": "Organic Chemistry",
        "subtopic": "Alkanol Oxidation",
        "year": 2024,
        "question": "The complete oxidation of propan-1-ol with excess acidified potassium tetraoxomanganate(VII) produces:",
        "options": {"A": "Propanoic acid", "B": "Propanone", "C": "Propanal", "D": "Propene"},
        "correct_option": "A",
        "traps": {
            "B": "Propanone is a ketone formed by oxidation of the secondary alcohol propan-2-ol, not primary propan-1-ol.",
            "C": "Propanal is the intermediate aldehyde, but with EXCESS strong oxidizing agent, oxidation proceeds fully to carboxylic acid.",
            "D": "Propene is formed by dehydration with concentrated H₂SO₄, not oxidation."
        },
        "pedagogical_concept": "Primary Alkanol Oxidation: Primary alcohols undergo two-stage oxidation: RCH₂OH -> RCHO (aldehyde) -> RCOOH (carboxylic acid). Propan-1-ol oxidizes fully to propanoic acid.",
        "socratic_prompt": "When a primary alcohol is heated with excess strong oxidizing agent like KMnO₄, what is the terminal organic product?"
    },
    {
        "id": "chm_015",
        "subject": "Chemistry",
        "topic": "Organic Chemistry",
        "subtopic": "Isomerism",
        "year": 2023,
        "question": "Which of the following pairs of compounds are functional group isomers?",
        "options": {
            "A": "Ethanol and Methoxymethane",
            "B": "But-1-ene and But-2-ene",
            "C": "Pentane and 2-Methylbutane",
            "D": "Ethanoic acid and Propanoic acid"
        },
        "correct_option": "A",
        "traps": {
            "B": "But-1-ene and but-2-ene are positional isomers (different position of double bond).",
            "C": "Pentane and 2-methylbutane are chain (skeletal) isomers.",
            "D": "Ethanoic and propanoic acids are successive members of a homologous series, not isomers (different molecular formulas!)."
        },
        "pedagogical_concept": "Functional Group Isomerism: Compounds sharing identical molecular formulas but having different functional groups. Ethanol (alcohol: C₂H₅OH) and methoxymethane (ether: CH₃OCH₃) both have molecular formula C₂H₆O.",
        "socratic_prompt": "Do ethanol and dimethyl ether share the same molecular formula C₂H₆O while possessing completely different functional groups?"
    },
    {
        "id": "chm_016",
        "subject": "Chemistry",
        "topic": "Environmental & Industrial Chemistry",
        "subtopic": "Electrolysis",
        "year": 2024,
        "question": "During the electrolysis of dilute sodium chloride (NaCl) solution using inert platinum electrodes, what products are discharged at the cathode and anode respectively?",
        "options": {
            "A": "Hydrogen gas at cathode, Oxygen gas at anode",
            "B": "Sodium metal at cathode, Chlorine gas at anode",
            "C": "Sodium metal at cathode, Oxygen gas at anode",
            "D": "Hydrogen gas at cathode, Chlorine gas at anode"
        },
        "correct_option": "A",
        "traps": {
            "B": "Sodium has a very high standard reduction potential and is never discharged in dilute aqueous solution; H⁺ is preferentially reduced.",
            "D": "Chlorine is discharged in CONCENTRATED brine, but in DILUTE NaCl, OH⁻ is preferentially discharged over Cl⁻ to release O₂!",
            "C": "Metallic sodium reacts violently with water and cannot deposit in aqueous solution."
        },
        "pedagogical_concept": "Preferential Discharge in Dilute Electrolytes: In dilute NaCl, water ions dominate. At cathode: 2H⁺ + 2e⁻ -> H₂(g) (H⁺ is lower than Na⁺ in electrochemical series). At anode: 4OH⁻ - 4e⁻ -> 2H₂O + O₂(g) (OH⁻ is preferentially discharged over dilute Cl⁻).",
        "socratic_prompt": "In a very dilute aqueous solution, are water ions (H⁺ and OH⁻) preferentially discharged over salt ions?"
    },
    {
        "id": "chm_017",
        "subject": "Chemistry",
        "topic": "Environmental & Industrial Chemistry",
        "subtopic": "Water Hardness",
        "year": 2023,
        "question": "Which chemical compound is responsible for permanent water hardness?",
        "options": {
            "A": "Calcium sulfate (CaSO₄)",
            "B": "Calcium hydrogen carbonate (Ca(HCO₃)₂)",
            "C": "Sodium carbonate (Na₂CO₃)",
            "D": "Potassium nitrate (KNO₃)"
        },
        "correct_option": "A",
        "traps": {
            "B": "Ca(HCO₃)₂ causes TEMPORARY water hardness, which is removed by boiling.",
            "C": "Sodium carbonate (washing soda) is used to REMOVE hardness, not cause it.",
            "D": "KNO₃ does not cause water hardness."
        },
        "pedagogical_concept": "Permanent Water Hardness: Caused by dissolved sulfates or chlorides of calcium and magnesium (CaSO₄, MgSO₄, CaCl₂, MgCl₂). These cannot be decomposed by boiling.",
        "socratic_prompt": "What salt of calcium causes hardness that CANNOT be removed by boiling?"
    }
]

biology_questions = [
    {
        "id": "bio_010",
        "subject": "Biology",
        "topic": "Cellular Biology & Life Processes",
        "subtopic": "Cell Organelles",
        "year": 2024,
        "question": "Which cellular organelle is responsible for packaging, modifying, and sorting proteins for secretion?",
        "options": {
            "A": "Golgi apparatus",
            "B": "Endoplasmic reticulum",
            "C": "Mitochondrion",
            "D": "Nucleolus"
        },
        "correct_option": "A",
        "traps": {
            "B": "The rough ER synthesizes proteins; the Golgi apparatus packages and exports them.",
            "C": "Mitochondria produce ATP via cellular respiration.",
            "D": "The nucleolus synthesizes ribosomal RNA."
        },
        "pedagogical_concept": "Golgi Apparatus: Consists of flattened cisternae that receive proteins from the rough ER, add carbohydrate modifications (glycosylation), and package them into secretory vesicles.",
        "socratic_prompt": "What cellular organelle functions as the distribution and shipping warehouse of the cell?"
    },
    {
        "id": "bio_011",
        "subject": "Biology",
        "topic": "Cellular Biology & Life Processes",
        "subtopic": "Osmosis & Plasmolysis",
        "year": 2023,
        "question": "When red blood cells are placed in a 0.2% sodium chloride solution (hypotonic), they burst. This phenomenon is called:",
        "options": {"A": "Hemolysis", "B": "Crenation", "C": "Plasmolysis", "D": "Turgidity"},
        "correct_option": "A",
        "traps": {
            "B": "Crenation occurs when red blood cells shrink in a hypertonic solution.",
            "C": "Plasmolysis occurs only in plant cells with cell walls.",
            "D": "Turgidity is a state of plant cells, not animal cells."
        },
        "pedagogical_concept": "Hemolysis: Animal cells lack rigid cell walls. In a hypotonic solution, water moves into the cell by endosmosis until hydrostatic pressure bursts the fragile plasma membrane (hemolysis).",
        "socratic_prompt": "What is the biological term for the bursting of red blood cells due to water influx?"
    },
    {
        "id": "bio_012",
        "subject": "Biology",
        "topic": "Human Physiology & Systems",
        "subtopic": "Circulation",
        "year": 2024,
        "question": "A person with blood group O negative is regarded as a universal donor because their red blood cells possess:",
        "options": {
            "A": "Neither A nor B antigens, and no Rhesus antigen",
            "B": "Both anti-A and anti-B antibodies on cell membranes",
            "C": "Both A and B antigens",
            "D": "Only Rhesus antibodies"
        },
        "correct_option": "A",
        "traps": {
            "B": "Antibodies are dissolved in blood plasma, NOT on red blood cell membranes!",
            "C": "Group AB possesses both A and B antigens.",
            "D": "Rh negative means the absence of the Rh antigen, not antibodies on the RBC."
        },
        "pedagogical_concept": "Blood Transfusion Immunology: Blood Group O red blood cells lack both A and B agglutinogens (antigens). Being Rh negative also means the D antigen is absent. Consequently, recipient antibodies cannot agglutinate these transfused RBCs.",
        "socratic_prompt": "Why can Group O negative blood be received by almost anyone without triggering an immune attack?"
    },
    {
        "id": "bio_013",
        "subject": "Biology",
        "topic": "Human Physiology & Systems",
        "subtopic": "Excretion & Nephron",
        "year": 2023,
        "question": "In the human nephron, the selective reabsorption of all amino acids and glucose occurs primarily in the:",
        "options": {
            "A": "Proximal Convoluted Tubule (PCT)",
            "B": "Loop of Henle",
            "C": "Distal Convoluted Tubule (DCT)",
            "D": "Bowman's Capsule"
        },
        "correct_option": "A",
        "traps": {
            "B": "The Loop of Henle is responsible for osmoregulation and water conservation.",
            "C": "The DCT is involved in fine hormonal tuning of sodium and potassium under aldosterone.",
            "D": "Bowman's capsule is the site of non-selective ultrafiltration, not reabsorption."
        },
        "pedagogical_concept": "Proximal Convoluted Tubule: The PCT cells possess extensive microvilli (brush border) and dense mitochondria to actively transport 100% of filtered glucose and amino acids back into the blood capillaries.",
        "socratic_prompt": "In which segment of the nephron does active reabsorption of nutrients like glucose take place?"
    },
    {
        "id": "bio_014",
        "subject": "Biology",
        "topic": "Genetics & Evolution",
        "subtopic": "Sex-Linked Inheritance",
        "year": 2024,
        "question": "Why are sex-linked recessive traits such as red-green color blindness more prevalent in human males than in human females?",
        "options": {
            "A": "Males are hemizygous and have only one X chromosome",
            "B": "The Y chromosome carries a dominant suppressor gene",
            "C": "Females produce more testosterone which masks the trait",
            "D": "The mutated allele is transmitted only from father to son"
        },
        "correct_option": "A",
        "traps": {
            "B": "The Y chromosome is smaller and carries very few genes, none of which suppress X-linked color blindness.",
            "C": "Hormones do not mask X-linked recessive mutations.",
            "D": "Fathers never pass their X chromosome to sons (they pass the Y chromosome)."
        },
        "pedagogical_concept": "Hemizygosity in Males: Human males have XY sex chromosomes. A single recessive allele on the single X chromosome (X^c Y) will inevitably express the phenotype because there is no second X chromosome to carry a dominant masking allele.",
        "socratic_prompt": "Since males have only one X chromosome, what happens if that single X chromosome carries a recessive mutation?"
    },
    {
        "id": "bio_015",
        "subject": "Biology",
        "topic": "Genetics & Evolution",
        "subtopic": "Mendelian Crosses",
        "year": 2023,
        "question": "A cross between two heterozygous tall pea plants (Tt × Tt) produces 400 offspring. Approximately how many offspring are expected to be dwarf?",
        "options": {"A": "100", "B": "300", "C": "200", "D": "50"},
        "correct_option": "A",
        "traps": {
            "B": "300 is the expected number of TALL plants (3/4 of 400).",
            "C": "200 would represent a 1:1 ratio.",
            "D": "Arithmetic error."
        },
        "pedagogical_concept": "Mendelian Monohybrid Ratio: Tt × Tt yields genotypes 1 TT : 2 Tt : 1 tt. The dwarf phenotype (tt) represents 1/4 (25%) of total progeny. Expected dwarfs = 1/4 × 400 = 100 plants.",
        "socratic_prompt": "In a cross between two heterozygotes (Tt × Tt), what fraction of the offspring display the recessive phenotype?"
    },
    {
        "id": "bio_016",
        "subject": "Biology",
        "topic": "Ecology & Environment",
        "subtopic": "Nitrogen Cycle",
        "year": 2024,
        "question": "Which genus of bacteria lives symbiotically in the root nodules of leguminous plants to convert atmospheric nitrogen into ammonium compounds?",
        "options": {"A": "Rhizobium", "B": "Nitrosomonas", "C": "Nitrobacter", "D": "Azotobacter"},
        "correct_option": "A",
        "traps": {
            "B": "Nitrosomonas oxidizes ammonia to nitrite in soil.",
            "C": "Nitrobacter oxidizes nitrite to nitrate.",
            "D": "Azotobacter is a free-living soil bacterium, NOT symbiotic in root nodules!"
        },
        "pedagogical_concept": "Symbiotic Nitrogen Fixation: Rhizobium bacteria form root nodules on legumes (beans, groundnuts), providing organic nitrogen to the plant while receiving carbohydrates.",
        "socratic_prompt": "Which bacterium forms a symbiotic partnership inside root nodules of legumes?"
    },
    {
        "id": "bio_017",
        "subject": "Biology",
        "topic": "Ecology & Environment",
        "subtopic": "Energy Pyramids",
        "year": 2023,
        "question": "Why can an ecological pyramid of energy never be inverted in a stable natural ecosystem?",
        "options": {
            "A": "Energy is progressively lost as heat and metabolic respiration at each successive trophic transfer",
            "B": "Producers always possess smaller biomass than top predators",
            "C": "Decomposers capture 100% of solar radiation",
            "D": "Energy increases as it moves up the food chain"
        },
        "correct_option": "A",
        "traps": {
            "B": "Producers usually have larger biomass, but biomass pyramids can invert in aquatic systems; energy pyramids NEVER invert.",
            "C": "Decomposers do not capture solar radiation.",
            "D": "Energy decreases, never increases, according to thermodynamics."
        },
        "pedagogical_concept": "Second Law of Thermodynamics in Ecology: As energy flows from producers to primary and secondary consumers, roughly 90% is dissipated as heat or used in metabolic maintenance. Only ~10% is stored as new biomass, ensuring energy pyramids remain strictly upright.",
        "socratic_prompt": "What happens to the amount of usable energy as you ascend from plants to herbivores to carnivores?"
    }
]

print(f"STEM batch defined: {len(math_questions)} Math, {len(physics_questions)} Physics, {len(chemistry_questions)} Chemistry, {len(biology_questions)} Biology.")
