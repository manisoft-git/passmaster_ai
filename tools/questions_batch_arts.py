# Arts & Social Sciences questions batch: English, Economics, Government, Literature

english_questions = [
    {
        "id": "eng_016",
        "subject": "Use of English",
        "topic": "Concord & Grammar",
        "subtopic": "Parenthetical Concord",
        "year": 2024,
        "question": "The Vice-Chancellor, together with the members of the university senate, _______ to address the press today.",
        "options": {"A": "is expected", "B": "are expected", "C": "were expected", "D": "have been expected"},
        "correct_option": "A",
        "traps": {
            "B": "You were tricked by the plural noun 'members' inside the parenthetical phrase 'together with...'. The true subject is the singular 'The Vice-Chancellor'!",
            "C": "Past plural tense violates both number and present relevance ('today').",
            "D": "Plural present perfect auxiliary violates the singular subject."
        },
        "pedagogical_concept": "Intervening Modifiers: Phrases introduced by 'together with', 'as well as', 'in addition to', 'accompanied by' are parenthetical prepositions. The verb must agree with the head noun before the comma ('The Vice-Chancellor' = singular).",
        "socratic_prompt": "If you remove everything between the two commas, what is the main subject and should it take a singular or plural verb?"
    },
    {
        "id": "eng_017",
        "subject": "Use of English",
        "topic": "Concord & Grammar",
        "subtopic": "Indefinite Pronouns",
        "year": 2023,
        "question": "Each of the scholarship applicants _______ expected to present an original certificate during the oral interview.",
        "options": {"A": "is", "B": "are", "C": "were", "D": "have been"},
        "correct_option": "A",
        "traps": {
            "B": "You matched the verb to the plural noun 'applicants' instead of the true distributive head pronoun 'Each'.",
            "C": "Past tense plural form.",
            "D": "Plural perfect verb."
        },
        "pedagogical_concept": "Distributive Pronoun Concord: Indefinite pronouns like 'each', 'either', 'neither', 'everyone', 'nobody' are grammatically singular and require singular verbs.",
        "socratic_prompt": "What grammatical number does the distributive word 'Each' take in formal English?"
    },
    {
        "id": "eng_018",
        "subject": "Use of English",
        "topic": "Lexis & Structure",
        "subtopic": "Fixed Collocations",
        "year": 2024,
        "question": "The presiding judge found the accused innocent and acquitted him _______ all charges of embezzlement.",
        "options": {"A": "of", "B": "from", "C": "for", "D": "against"},
        "correct_option": "A",
        "traps": {
            "B": "'Acquitted from' is Nigerian vernacular interference. In standard English, the collocation is 'acquit of'.",
            "C": "'Acquit for' is grammatically incorrect.",
            "D": "'Acquit against' is unidiomatic."
        },
        "pedagogical_concept": "Fixed Preposition: The legal verb 'acquit' pairs exclusively with the preposition 'of' (acquit someone OF a crime).",
        "socratic_prompt": "When a court clears a person of legal guilt, do they acquit them 'from' or 'of' the crime?"
    },
    {
        "id": "eng_019",
        "subject": "Use of English",
        "topic": "Lexis & Structure",
        "subtopic": "Tautology Avoidance",
        "year": 2023,
        "question": "Choose the sentence that does NOT contain a tautology or redundant expression:",
        "options": {
            "A": "The committee will revert with the official resolution tomorrow.",
            "B": "The committee will revert back with the official resolution tomorrow.",
            "C": "Please repeat the statement again for clarity.",
            "D": "The two companies decided to merge together into a single corporation."
        },
        "correct_option": "A",
        "traps": {
            "B": "'Revert back' is a tautology because 'revert' already means to return or turn back.",
            "C": "'Repeat again' is a tautology because 'repeat' means to say again.",
            "D": "'Merge together' is redundant because 'merge' means to join together."
        },
        "pedagogical_concept": "Redundancy Elimination: 'Revert' already contains the backward direction, making 'back' redundant. Correct formal usage is simply 'revert'.",
        "socratic_prompt": "Does the word 'revert' already mean to return back to a topic or person?"
    },
    {
        "id": "eng_020",
        "subject": "Use of English",
        "topic": "Oral Forms & Phonology",
        "subtopic": "Vowel Length Contrast",
        "year": 2024,
        "question": "Which of the following words contains the long vowel sound /iː/ as in 'LEAP'?",
        "options": {"A": "Key", "B": "Kip", "C": "Myth", "D": "Busy"},
        "correct_option": "A",
        "traps": {
            "B": "'Kip' contains the short vowel /ɪ/.",
            "C": "'Myth' contains the short vowel /ɪ/.",
            "D": "'Busy' contains short /ɪ/ in both syllables (/ˈbɪzi/)."
        },
        "pedagogical_concept": "Phonetic Vowel Quality: 'Key' is pronounced /kiː/ with a long close front unrounded vowel, sharing the exact vowel phoneme of 'leap' (/liːp/).",
        "socratic_prompt": "How do you pronounce 'key'—does it have the short /ɪ/ of 'fit' or the long /iː/ of 'feet'?"
    }
]

economics_questions = [
    {
        "id": "eco_011",
        "subject": "Economics",
        "topic": "Basic Economic Principles & Methodology",
        "subtopic": "Opportunity Cost",
        "year": 2024,
        "question": "A farmer has enough savings to purchase either a modern tractor or 50 bags of fertilizer. If he chooses the tractor, the opportunity cost of his decision is:",
        "options": {
            "A": "The satisfaction and farm yield forgone from the 50 bags of fertilizer",
            "B": "The monetary purchase price of the tractor",
            "C": "The depreciation and maintenance costs of the tractor",
            "D": "The market selling price of the crops produced"
        },
        "correct_option": "A",
        "traps": {
            "B": "The price of the tractor is the financial money cost, NOT the opportunity cost!",
            "C": "Depreciation is an accounting overhead expense.",
            "D": "Crop revenue is the expected reward, not the sacrificed alternative."
        },
        "pedagogical_concept": "Real Opportunity Cost: Opportunity cost is the next best alternative sacrificed when a choice is made. It is the real physical benefit forgone, never the money spent.",
        "socratic_prompt": "What did the farmer directly give up when he decided to buy the tractor?"
    },
    {
        "id": "eco_012",
        "subject": "Economics",
        "topic": "Microeconomics & Price Mechanism",
        "subtopic": "Price Elasticity of Supply",
        "year": 2023,
        "question": "In the immediate short run (market period), the price elasticity of supply for perishable agricultural produce (like fresh tomatoes) is typically:",
        "options": {
            "A": "Perfectively inelastic (Es = 0)",
            "B": "Perfectively elastic (Es = ∞)",
            "C": "Highly elastic (Es > 1)",
            "D": "Unitary elastic (Es = 1)"
        },
        "correct_option": "A",
        "traps": {
            "B": "Perfect elasticity would mean suppliers can instantly produce infinite quantities, which is impossible.",
            "C": "Agricultural produce requires a biological gestation period and cannot be expanded in the immediate short run.",
            "D": "Unitary elasticity requires proportional responsiveness."
        },
        "pedagogical_concept": "Momentary Market Supply: In the immediate market period, harvest is already fixed. Because tomatoes perish quickly and storage is limited, supply cannot respond to price surges, resulting in a vertical, perfectly inelastic supply curve (Es = 0).",
        "socratic_prompt": "Can a tomato farmer instantly increase the quantity of tomatoes harvested today just because the price tripled this morning?"
    },
    {
        "id": "eco_013",
        "subject": "Economics",
        "topic": "Macroeconomics & National Income",
        "subtopic": "GDP vs GNP",
        "year": 2024,
        "question": "If a country's Gross Domestic Product (GDP) is ₦500 billion and the Net Factor Income from Abroad (NFIA) is -₦30 billion, its Gross National Product (GNP) is:",
        "options": {"A": "₦470 billion", "B": "₦530 billion", "C": "₦500 billion", "D": "₦440 billion"},
        "correct_option": "A",
        "traps": {
            "B": "You added the negative NFIA as a positive number: 500 - (-30) = 530.",
            "C": "You assumed GDP always equals GNP.",
            "D": "You subtracted 30 twice."
        },
        "pedagogical_concept": "GNP Formula: GNP = GDP + NFIA = ₦500B + (-₦30B) = ₦500B - ₦30B = ₦470 billion.",
        "socratic_prompt": "When Net Factor Income from Abroad is negative, is GNP smaller or larger than GDP?"
    },
    {
        "id": "eco_014",
        "subject": "Economics",
        "topic": "Money, Banking & Public Finance",
        "subtopic": "Monetary Policy Rate",
        "year": 2023,
        "question": "When the Central Bank of Nigeria increases the Monetary Policy Rate (MPR), the immediate expected economic effect is:",
        "options": {
            "A": "Commercial banks raise lending interest rates, discouraging borrowing and reducing money supply",
            "B": "Commercial banks reduce lending rates, encouraging business expansion",
            "C": "Inflation increases due to excess consumer liquidity",
            "D": "The Cash Reserve Ratio automatically falls to zero"
        },
        "correct_option": "A",
        "traps": {
            "B": "Higher policy rates increase the cost of bank funds, forcing banks to RAISE, not lower, lending rates.",
            "C": "Raising MPR is contractionary and aims to REDUCE inflation.",
            "D": "CRR is independently set and does not fall to zero."
        },
        "pedagogical_concept": "Contractionary Monetary Policy: Increasing the MPR raises the cost of commercial banks borrowing from the Central Bank. Commercial banks pass this cost on by raising loan interest rates, which dampens credit demand and combats inflation.",
        "socratic_prompt": "If the Central Bank makes borrowing more expensive for commercial banks, what happens to the interest rate charged to ordinary borrowers?"
    }
]

government_questions = [
    {
        "id": "gov_010",
        "subject": "Government",
        "topic": "Elements of Government & Political Theory",
        "subtopic": "Separation of Powers",
        "year": 2024,
        "question": "Which French political philosopher formulated the classical doctrine of the Separation of Powers in his 1748 treatise 'The Spirit of the Laws'?",
        "options": {"A": "Baron de Montesquieu", "B": "Jean-Jacques Rousseau", "C": "John Locke", "D": "Thomas Hobbes"},
        "correct_option": "A",
        "traps": {
            "B": "Rousseau developed the doctrine of the 'General Will' and direct popular democracy.",
            "C": "John Locke wrote on natural rights (life, liberty, property) and social contract.",
            "D": "Thomas Hobbes advocated absolute sovereign authority in 'Leviathan'."
        },
        "pedagogical_concept": "Montesquieu & Separation of Powers: In 'De l'esprit des lois' (1748), Montesquieu argued that political liberty is preserved only when the legislative, executive, and judicial powers are vested in separate, distinct bodies.",
        "socratic_prompt": "Who wrote 'The Spirit of the Laws' advocating the division of state powers into three independent branches?"
    },
    {
        "id": "gov_011",
        "subject": "Government",
        "topic": "Colonial Administration in Nigeria & West Africa",
        "subtopic": "Aba Women's Riot",
        "year": 2023,
        "question": "The 1929 Aba Women's Riot in colonial Eastern Nigeria was triggered primarily by:",
        "options": {
            "A": "Rumors of direct taxation of women and abuses by appointed Warrant Chiefs",
            "B": "The prohibition of palm oil exports to Britain",
            "C": "The introduction of the Clifford Constitution",
            "D": "A dispute over the selection of the King of Opobo"
        },
        "correct_option": "A",
        "traps": {
            "B": "Palm oil trade was vital, but was not the trigger of the riots.",
            "C": "The Clifford Constitution was enacted in 1922, seven years before the riot.",
            "D": "Jaja of Opobo's exile occurred in the late 19th century (1887)."
        },
        "pedagogical_concept": "Aba Women's Resistance (1929): Stemmed from the oppressive corruption of artificial Warrant Chiefs and British attempts to conduct a tax census on women in Oloko and Aba.",
        "socratic_prompt": "What did the colonial administrators attempt to count that led Igbo women to fear direct taxation?"
    },
    {
        "id": "gov_012",
        "subject": "Government",
        "topic": "Nigerian Constitutional Development",
        "subtopic": "Macpherson Constitution",
        "year": 2024,
        "question": "The Macpherson Constitution of 1951 was distinguished from earlier colonial constitutions because:",
        "options": {
            "A": "It was drafted following unprecedented grassroots consultation from village to regional levels",
            "B": "It established complete Nigerian independence from Britain",
            "C": "It introduced the American-style executive presidency",
            "D": "It created the first 12 states in Nigeria"
        },
        "correct_option": "A",
        "traps": {
            "B": "Independence came in 1960, not 1951.",
            "C": "The executive presidency was introduced by the 1979 Constitution.",
            "D": "General Gowon created 12 states in 1967."
        },
        "pedagogical_concept": "Grassroots Constitutionalism: John Macpherson avoided Arthur Richards' mistake of imposing a constitution without popular input by convening village, district, provincial, and regional conferences before the 1950 Ibadan General Conference.",
        "socratic_prompt": "Why was Sir John Macpherson's constitution praised for its democratic drafting process?"
    },
    {
        "id": "gov_013",
        "subject": "Government",
        "topic": "Federalism, Military Rule & Foreign Policy",
        "subtopic": "Creation of States",
        "year": 2023,
        "question": "Which Nigerian military head of state created 12 states out of the existing four regions on May 27, 1967?",
        "options": {"A": "General Yakubu Gowon", "B": "General Murtala Mohammed", "C": "General Ibrahim Babangida", "D": "Major-General J.T.U. Aguiyi-Ironsi"},
        "correct_option": "A",
        "traps": {
            "B": "Murtala Mohammed created 19 states in 1976.",
            "C": "Ibrahim Babangida created 21 states in 1987 and 30 states in 1991.",
            "D": "Aguiyi-Ironsi promulgated the Unification Decree No. 34, abolishing regions."
        },
        "pedagogical_concept": "State Creation History: General Yakubu Gowon dissolved the four regions (Northern, Western, Eastern, Mid-Western) into 12 states on May 27, 1967, to preserve federal unity and undercut the secessionist Republic of Biafra.",
        "socratic_prompt": "Who was the Head of State who broke Nigeria into 12 states on the eve of the Civil War in 1967?"
    }
]

literature_questions = [
    {
        "id": "lit_008",
        "subject": "Literature in English",
        "topic": "Literary Appreciation & Devices",
        "subtopic": "Dramatic Monologue & Soliloquy",
        "year": 2024,
        "question": "When a character in a drama speaks their innermost thoughts out loud while alone on stage, the device is known as a:",
        "options": {"A": "Soliloquy", "B": "Monologue", "C": "Dialogue", "D": "Aside"},
        "correct_option": "A",
        "traps": {
            "B": "A monologue is a long speech delivered by one person, but usually in the presence of other listening characters.",
            "C": "Dialogue requires conversation between two or more characters.",
            "D": "An aside is a brief remark spoken to the audience while other characters are present on stage."
        },
        "pedagogical_concept": "Dramatic Soliloquy: Derived from Latin 'solus' (alone) + 'loqui' (to speak). It is an extended theatrical speech delivered by a character alone on stage to reveal authentic psychological conflict directly to the audience.",
        "socratic_prompt": "What is the specific dramatic term for speaking your private thoughts completely alone on stage?"
    },
    {
        "id": "lit_009",
        "subject": "Literature in English",
        "topic": "Drama & Theatrical Techniques",
        "subtopic": "Soyinka's The Lion and the Jewel",
        "year": 2023,
        "question": "In Wole Soyinka's 'The Lion and the Jewel', what stratagem does Baroka employ to lure Sidi into his palace?",
        "options": {
            "A": "He circulates a false rumor that his masculine virility has failed",
            "B": "He promises to make her the sole queen of Western Nigeria",
            "C": "He sends Lakunle with expensive European textiles",
            "D": "He threatens to seize her father's farmland"
        },
        "correct_option": "A",
        "traps": {
            "B": "Baroka is Bale of Ilujinle, not a regional governor.",
            "C": "Lakunle is Baroka's rival, not his messenger.",
            "D": "Baroka relies on psychological cunning rather than economic extortion."
        },
        "pedagogical_concept": "Baroka's Ruse: Baroka informs his head wife Sadiku that his manhood has expired. Knowing Sadiku cannot keep a secret, Sidi visits the palace to mock the 'impotent lion', allowing Baroka to trap and seduce her.",
        "socratic_prompt": "What secret did Baroka entrust to Sadiku, knowing she would boast about it to Sidi?"
    },
    {
        "id": "lit_010",
        "subject": "Literature in English",
        "topic": "Poetry & Versification",
        "subtopic": "Petrarchan Sonnet",
        "year": 2024,
        "question": "In an Italian (Petrarchan) sonnet, the transition or turn in thought between the octave and the sestet at line 9 is technically termed the:",
        "options": {"A": "Volta", "B": "Caesura", "C": "Enjambment", "D": "Refrain"},
        "correct_option": "A",
        "traps": {
            "B": "A caesura is a pause or punctuation break in the middle of a single line of poetry.",
            "C": "Enjambment is a run-on line carrying over without terminal punctuation.",
            "D": "A refrain is a repeating chorus line."
        },
        "pedagogical_concept": "The Volta: An Italian word meaning 'turn'. In Petrarchan sonnets, line 9 marks the pivotal shift where the poem moves from presenting an emotional problem (in the octave) to resolving or reflecting upon it (in the sestet).",
        "socratic_prompt": "What is the Italian word for the thematic turn between the octave and sestet in a sonnet?"
    },
    {
        "id": "lit_011",
        "subject": "Literature in English",
        "topic": "Prose & Fictional Techniques",
        "subtopic": "Things Fall Apart Analysis",
        "year": 2023,
        "question": "In Chinua Achebe's 'Things Fall Apart', which tragic incident precipitates Okonkwo's seven-year exile from Umuofia to his motherland Mbanta?",
        "options": {
            "A": "The accidental explosion of his dane gun which kills Ezeudu's son at a funeral",
            "B": "His participation in the ritual execution of Ikemefuna",
            "C": "His physical assault of his wife Ojiugo during the Week of Peace",
            "D": "His public defiance of the British District Commissioner"
        },
        "correct_option": "A",
        "traps": {
            "B": "Killing Ikemefuna earned spiritual condemnation from elders like Obierika, but did not cause legal exile.",
            "C": "Beating his wife in the Week of Peace resulted in a fine to the earth goddess Ani, not exile.",
            "D": "Defying the District Commissioner happens at the very end of the novel."
        },
        "pedagogical_concept": "Inadvertent Manslaughter (Ochu): Okonkwo's gun explodes during Ezeudu's funeral dance, killing a 16-year-old boy. Because the killing was accidental ('female murder'), traditional tribal law mandated a seven-year banishment to his mother's village, Mbanta.",
        "socratic_prompt": "What unexpected accident occurred at Ezeudu's funeral that forced Okonkwo to flee Umuofia?"
    }
]

print(f"Arts batch defined: {len(english_questions)} English, {len(economics_questions)} Economics, {len(government_questions)} Government, {len(literature_questions)} Literature.")
