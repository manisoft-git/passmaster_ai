import json

with open('data/questions.json', 'r', encoding='utf-8') as f:
    questions = json.load(f)

existing = {q['id'] for q in questions}

more_q = [
    {
        'id': 'eng_004',
        'subject': 'Use of English',
        'topic': 'Concord & Grammar',
        'subtopic': 'Subjunctive Mood',
        'year': 2024,
        'question': 'The disciplinary committee recommended that the suspended student _______ reinstated immediately with a stern warning.',
        'options': {
            'A': 'is',
            'B': 'be',
            'C': 'was',
            'D': 'should be'
        },
        'correct_option': 'B',
        'traps': {
            'A': 'You applied indicative present tense. Verbs of urging, recommending, or demanding (mandative subjunctive) take the base form of the verb without inflection.',
            'C': 'You matched past tense recommended with was. The subjunctive base form be is mandatory regardless of the main clause tense.',
            'D': 'Should be is wordy and less formally standard than the mandated subjunctive base form be in formal examination grammar.'
        },
        'pedagogical_concept': 'Mandative Subjunctive: After verbs and expressions of demand, recommendation, or necessity (e.g., recommend that, demand that, insist that), the subordinate clause verb must be in base form (be, go, do), regardless of subject person or number.',
        'socratic_prompt': 'Notice the verb of recommendation: recommended that... In formal grammar, what is the special subjunctive form of to be used in that-clauses after recommendations?'
    },
    {
        'id': 'chm_003',
        'subject': 'Chemistry',
        'topic': 'Inorganic Chemistry',
        'subtopic': 'Faradays Laws of Electrolysis',
        'year': 2023,
        'question': 'What mass of copper (Cu = 64 g/mol) will be deposited at the cathode by a steady current of 2.0 A passing through a CuSO₄ solution for 965 seconds? (1 Faraday = 96,500 C/mol e⁻)',
        'options': {
            'A': '1.28 g',
            'B': '0.64 g',
            'C': '2.56 g',
            'D': '0.32 g'
        },
        'correct_option': 'B',
        'traps': {
            'A': 'You forgot that copper in CuSO₄ is divalent (Cu²⁺ + 2e⁻ → Cu), requiring 2 moles of electrons per mole of Cu deposited. You used n = 1 instead of n = 2: (2 * 965 * 64)/96500 = 1.28 g.',
            'C': 'You multiplied by 2 instead of dividing by the valency of copper.',
            'D': 'You divided by 4 instead of 2.'
        },
        'pedagogical_concept': "Faraday's Law: Mass = (I * t * Molar Mass) / (n * F). Here: Q = I * t = 2.0 * 965 = 1,930 Coulombs. Number of Faradays = 1,930 / 96,500 = 0.02 F. Since Cu²⁺ needs 2 F per mole, moles of Cu = 0.02 / 2 = 0.01 mol. Mass = 0.01 * 64 = 0.64 g.",
        'socratic_prompt': 'What is the ionic charge on the copper ion in CuSO₄? How many electrons (Faradays) are required to deposit one atom of Cu²⁺?'
    },
    {
        'id': 'phy_004',
        'subject': 'Physics',
        'topic': 'Mechanics',
        'subtopic': 'Projectiles',
        'year': 2024,
        'question': 'A projectile is launched from ground level with an initial velocity of 40 m/s at an angle of 30° to the horizontal. Calculate the maximum height reached. (Take g = 10 m/s²)',
        'options': {
            'A': '80 m',
            'B': '20 m',
            'C': '40 m',
            'D': '60 m'
        },
        'correct_option': 'B',
        'traps': {
            'A': 'You calculated using the full launch speed without taking the vertical component: H = u² / 2g = 1600 / 20 = 80 m. You must use uy = u*sin(θ)!',
            'C': 'You forgot the square on uy: H = uy / 2g or made an arithmetic cancellation error.',
            'D': 'You used cos(30°) instead of sin(30°) for the vertical height component.'
        },
        'pedagogical_concept': 'Maximum Height of a Projectile: H_max = (u * sin θ)² / (2g). Here: u_y = 40 * sin(30°) = 40 * 0.5 = 20 m/s. H_max = (20)² / (2 * 10) = 400 / 20 = 20 m.',
        'socratic_prompt': 'What is the vertical velocity component of a 40 m/s launch at 30 degrees? Once you have the vertical speed (uy), what is (uy)² / (2g)?'
    },
    {
        'id': 'bio_003',
        'subject': 'Biology',
        'topic': 'Cell Biology & Organization',
        'subtopic': 'Osmosis & Plasmolysis',
        'year': 2024,
        'question': 'When red blood cells (erythrocytes) and plant epidermal cells are placed simultaneously in pure distilled water, what happens after 30 minutes?',
        'options': {
            'A': 'Both cell types burst due to continuous endosmosis',
            'B': 'Both cell types become flaccid and undergo plasmolysis',
            'C': 'Red blood cells swell and hemolyze (burst), while plant cells become turgid without bursting',
            'D': 'Plant cells burst, while red blood cells remain crenated'
        },
        'correct_option': 'C',
        'traps': {
            'A': 'Plant cells possess a rigid cellulose cell wall that generates wall pressure (turgor), preventing them from bursting in hypotonic solutions.',
            'B': 'Plasmolysis happens in HYPERTONIC solutions where water leaves the cell, not hypotonic distilled water.',
            'D': 'Red blood cells lack cell walls and burst (hemolysis), plant cells do not burst.'
        },
        'pedagogical_concept': 'Osmotic Balance & Cell Wall Pressure: Animal cells have only a fragile plasma membrane and undergo lysis/hemolysis in hypotonic water. Plant cells take in water until turgor pressure equals osmotic pressure, becoming turgid without bursting due to the cellulose cell wall.',
        'socratic_prompt': 'What cellular structure does a plant cell have that an animal red blood cell lacks? How does that rigid outer wall protect the plant cell from bursting?'
    },
    {
        'id': 'eco_004',
        'subject': 'Economics',
        'topic': 'Production & Market Structures',
        'subtopic': 'Cost Concepts (MC, AC, TC)',
        'year': 2023,
        'question': 'At the point where Marginal Cost (MC) is equal to Average Total Cost (ATC), which of the following statements is ALWAYS true?',
        'options': {
            'A': 'Total Revenue is maximized',
            'B': 'Average Total Cost is at its minimum point',
            'C': 'Average Variable Cost is zero',
            'D': 'The firm is earning supernormal profit'
        },
        'correct_option': 'B',
        'traps': {
            'A': 'Total revenue maximization occurs where MR = 0, which is unrelated to MC = ATC.',
            'C': 'AVC is never zero in positive production.',
            'D': 'Whether a firm earns normal, supernormal, or subnormal profit depends on price (AR), not merely where MC cuts ATC.'
        },
        'pedagogical_concept': 'The MC and AC Intersection Rule: The marginal cost curve always intersects both the Average Variable Cost (AVC) and Average Total Cost (ATC) curves at their respective lowest (minimum) points.',
        'socratic_prompt': 'Think about your grade average: if your next test score (marginal) is lower than your average, average falls. When the next test matches your average, the average stops falling. So where does MC intersect AC?'
    },
    {
        'id': 'gov_004',
        'subject': 'Government',
        'topic': 'Organs of Government & Electoral Process',
        'subtopic': 'Electoral Systems (PR vs Simple Majority)',
        'year': 2023,
        'question': 'The Proportional Representation electoral system is praised primarily because it _______.',
        'options': {
            'A': 'is extremely cheap and simple for illiterate electorates to understand',
            'B': 'guarantees that minority parties secure legislative representation in direct proportion to their total national votes',
            'C': 'always produces stable, single-party majority governments without need for coalitions',
            'D': 'eliminates political parties and allows only non-partisan candidates'
        },
        'correct_option': 'B',
        'traps': {
            'A': 'Proportional Representation is notoriously complex and mathematically demanding to compute compared to First-Past-The-Post.',
            'C': 'PR frequently leads to fragmented parliaments and unstable coalition governments.',
            'D': 'PR relies heavily on party-list tickets, making political parties central to the system.'
        },
        'pedagogical_concept': "Merits of Proportional Representation: Unlike First-Past-The-Post ('winner-takes-all'), Proportional Representation ensures fair representation for minority parties and reduces wasted votes by allocating parliamentary seats strictly proportional to total votes won.",
        'socratic_prompt': 'What does the word "Proportional" mean in elections? If a party wins 15% of the total vote, how many seats do they receive under Proportional Representation?'
    }
]

for q in more_q:
    if q['id'] not in existing:
        questions.append(q)
        existing.add(q['id'])

with open('data/questions.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, indent=2)

print('Updated question bank! Total questions now:', len(questions))
