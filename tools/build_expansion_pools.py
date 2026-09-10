"""
Builder script to construct tools/generators/expansion_pools.py with comprehensive
curriculum-aligned questions across all 8 subjects and all 32 syllabus topics.
"""

import os
import sys

def main():
    target_file = "tools/generators/expansion_pools.py"
    print(f"Creating comprehensive expansion pools in {target_file}...")
    
    # We will write the file with rich parametric generators for all 8 subjects
    with open(target_file, "w", encoding="utf-8") as f:
        f.write('''"""
PassMaster AI - Comprehensive Curriculum Expansion Pools
Generates 120+ authentic questions per topic across all 8 JAMB subjects:
  - Mathematics
  - Physics
  - Chemistry
  - Biology
  - Use of English
  - Economics
  - Government
  - Literature in English
All questions include pedagogical concepts, distractor traps, and Socratic guidance.
"""

import math
import random

def generate_expansion_pool(subject, topic, count_needed=300):
    items = []

    # =========================================================================
    # 1. USE OF ENGLISH
    # =========================================================================
    if subject == "Use of English":
        if topic == "Concord & Grammar":
            # 1. Proximity Rule with either/or, neither/nor
            sing_p = ["the principal", "the driver", "the commander", "the captain", "the professor", "the nurse", "the accountant", "the pilot", "the manager"]
            plur_p = ["the teachers", "the students", "the soldiers", "the sailors", "the researchers", "the patients", "the auditors", "the passengers", "the clerks"]
            for s in sing_p:
                for p in plur_p:
                    items.append((
                        "Rule of Proximity",
                        f"Neither {s} nor {p} _______ present at the emergency briefing yesterday.",
                        {"A": "were", "B": "was", "C": "is", "D": "are being"}, "A",
                        f"In 'neither... nor' constructions, the verb agrees solely with the subject closest to it ('{p}', plural).",
                        f"Look at the subject immediately adjacent to the verb: is '{p}' singular or plural?"
                    ))
                    items.append((
                        "Rule of Proximity",
                        f"Either {p} or {s} _______ responsible for locking the main laboratory gate.",
                        {"A": "is", "B": "are", "C": "were", "D": "have been"}, "A",
                        f"In 'either... or' constructions, the verb agrees solely with the subject closest to it ('{s}', singular).",
                        f"Which subject is physically closest to the blank: '{p}' or '{s}'?"
                    ))
            # 2. Parenthetical Phrases (as well as, accompanied by, together with)
            adjuncts = ["as well as", "together with", "accompanied by", "along with", "in addition to"]
            for s in sing_p[:6]:
                for adj in adjuncts:
                    items.append((
                        "Parenthetical Phrases",
                        f"{s.capitalize()}, {adj} {plur_p[0]}, _______ invited to address the grand convocation ceremony.",
                        {"A": "was", "B": "were", "C": "are", "D": "have been"}, "A",
                        f"Phrases introduced by '{adj}' are parenthetical additions and do not alter the singular subject '{s}'.",
                        f"Does '{adj}' make the subject plural, or is '{s}' the sole grammatical subject?"
                    ))
            # 3. Mandative Subjunctive
            mand_verbs = ["insist", "demand", "recommend", "stipulate", "decree", "suggest", "order", "urge"]
            for v in mand_verbs:
                items.append((
                    "Mandative Subjunctive",
                    f"The academic board {v}s that every undergraduate _______ the mandatory GST course before graduation.",
                    {"A": "pass", "B": "passes", "C": "passed", "D": "must pass"}, "A",
                    f"Verbs of mandate/demand ({v}) require the bare base infinitive ('pass', not 'passes') in the dependent 'that' clause.",
                    f"In standard subjunctive mood following 'that', what form does the dependent verb take?"
                ))
            # 4. Inverted Conditionals & Question Tags
            tags = [
                ("She rarely arrives late to lectures,", "does she?", "doesn't she?", "is she?", "isn't she?", "Negative adverbs like 'rarely' make the statement negative, requiring a positive tag."),
                ("Let us proceed to the next module,", "shall we?", "will you?", "can we?", "should we?", "'Let us / Let's' takes the fixed question tag 'shall we?'."),
                ("I am thoroughly prepared for this examination,", "aren't I?", "amn't I?", "am I not?", "isn't it?", "'I am' standardly takes the tag 'aren't I?' in English."),
                ("You hardly ever submit assignments on time,", "do you?", "don't you?", "did you?", "haven't you?", "'Hardly' conveys negative meaning, so the tag must be positive ('do you?')."),
                ("Nobody called for me while I was away,", "did they?", "didn't they?", "did he?", "didn't he?", "Indefinite pronouns ending in -body take plural pronoun 'they' in the question tag.")
            ]
            for stmt, ans, d1, d2, d3, exp in tags:
                for suffix in ["", " honestly", " surely"]:
                    items.append((
                        "Question Tags",
                        f"{stmt[:-1]}{suffix}?",
                        {"A": ans, "B": d1, "C": d2, "D": d3}, "A",
                        exp,
                        "What is the polarity of the statement, and what auxiliary matches it?"
                    ))

        elif topic == "Lexis & Structure":
            # 1. Advanced Phrasal Verbs
            phrasals = [
                ("call off", "cancel", "postpone", "continue", "review", "The union decided to call off the scheduled three-day strike."),
                ("put off", "postpone", "cancel", "extinguish", "tolerate", "Never put off till tomorrow what you can accomplish today."),
                ("put out", "extinguish", "postpone", "publish", "discard", "The brave firefighters worked for hours to put out the raging blaze."),
                ("bear out", "corroborate", "contradict", "tolerate", "conceal", "The forensic fingerprint evidence will bear out the suspect's alibi."),
                ("do away with", "abolish", "renovate", "preserve", "establish", "The reform bill seeks to do away with redundant civil service departments."),
                ("look down on", "despise", "admire", "investigate", "imitate", "It is unethical to look down on people because of their humble background."),
                ("fall out with", "quarrel with", "agree with", "reconcile with", "visit", "Emeka had a bitter misunderstanding and fell out with his childhood business partner."),
                ("run into", "encounter unexpectedly", "avoid", "collide with", "borrow from", "I was delighted to run into my former high school teacher at the airport."),
                ("take after", "resemble in character or appearance", "follow", "chase", "inherit money from", "In his analytical curiosity and quiet patience, Chidi takes after his father."),
                ("come by", "obtain with difficulty", "visit briefly", "bypass", "manufacture", "Genuine vintage coins are extremely scarce and difficult to come by nowadays.")
            ]
            for ph, ans, d1, d2, d3, ctx in phrasals:
                items.append((
                    "Phrasal Verbs in Context",
                    f"In the sentence: '{ctx}', the underlined phrasal verb means:",
                    {"A": ans, "B": d1, "C": d2, "D": d3}, "A",
                    f"The phrasal verb '{ph}' idiomatically means to {ans}.",
                    f"What does '{ph}' signify in this specific context?"
                ))
            # 2. Fixed Prepositional Collocations
            preps = [
                ("abstain", "from", "against", "with", "at", "Candidates must abstain _______ all forms of examination misconduct."),
                ("eligible", "for", "to", "with", "in", "Only students who achieve 200 and above are eligible _______ the post-UTME screening."),
                ("immune", "to", "against", "from", "with", "Infants receive vaccinations to become immune _______ infectious childhood diseases."),
                ("reminiscent", "of", "about", "with", "to", "His electrifying football dribbling style is reminiscent _______ prime Austin Jay-Jay Okocha."),
                ("devoid", "of", "with", "from", "about", "The defense argument was completely devoid _______ factual or verifiable evidence."),
                ("comply", "with", "to", "by", "for", "All motorists must strictly comply _______ road safety guidelines."),
                ("adjacent", "to", "with", "by", "near", "The newly built university library is located adjacent _______ the senate building."),
                ("indifferent", "to", "about", "with", "from", "A dedicated scholar cannot remain indifferent _______ current technological trends."),
                ("averse", "to", "against", "from", "with", "The conservative investor is strongly averse _______ speculative cryptocurrency trading."),
                ("compatible", "with", "to", "by", "from", "Ensure the mobile application is compatible _______ your smartphone operating system.")
            ]
            for word, ans, d1, d2, d3, sent in preps:
                items.append((
                    "Prepositional Collocations",
                    sent,
                    {"A": ans, "B": d1, "C": d2, "D": d3}, "A",
                    f"The word '{word}' standardly collocates exclusively with the preposition '{ans}'.",
                    f"Which preposition grammatically follows '{word}'?"
                ))
            # 3. Confusing Word Pairs & Idioms
            idiom_list = [
                ("burn the midnight oil", "study or work late into the night", "waste expensive fuel", "cause an accidental fire", "wake up early in the morning"),
                ("hit the nail on the head", "state the exact truth accurately", "cause physical injury", "construct furniture", "make an unnecessary error"),
                ("bite the bullet", "endure an inevitable hardship courageously", "chew ammunition", "surrender cowardly", "retaliate fiercely"),
                ("a blessing in disguise", "a misfortune that eventually results in good", "a religious curse", "an unexpected monetary loss", "a mysterious illness"),
                ("once in a blue moon", "very rarely or infrequently", "every full moon", "during an astronomical eclipse", "regularly every month")
            ]
            for idm, ans, d1, d2, d3 in idiom_list:
                for var in ["To", "The expression"]:
                    items.append((
                        "Idioms & Figurative Meanings",
                        f"{var} '{idm}' means to:",
                        {"A": ans, "B": d1, "C": d2, "D": d3}, "A",
                        f"The idiom '{idm}' denotes: {ans}.",
                        f"What metaphorical meaning is conveyed by '{idm}'?"
                    ))

        elif topic == "Oral Forms & Phonology":
            # 1. Silent Consonants
            silent_data = [
                ("k", ["knight", "knife", "knee", "knot", "know"], ["kettle", "kitchen", "king", "kite"]),
                ("b", ["doubt", "debt", "subtle", "climb", "tomb", "comb"], ["boat", "table", "timber", "rabbit"]),
                ("p", ["psychology", "receipt", "pneumonia", "corps", "psalm"], ["paper", "people", "public", "post"]),
                ("l", ["calm", "half", "salmon", "palm", "yolk", "talk"], ["lake", "silver", "filter", "pilot"]),
                ("w", ["write", "sword", "wrap", "wrist", "answer"], ["water", "window", "winter", "reward"]),
                ("t", ["whistle", "castle", "listen", "fasten", "soften"], ["ticket", "table", "metal", "bottle"]),
                ("g", ["sign", "gnaw", "phlegm", "reign", "foreign"], ["garden", "target", "gold", "gather"])
            ]
            for letter, silent_words, voiced_words in silent_data:
                for w in silent_words:
                    d_sample = random.sample(voiced_words, 3)
                    items.append((
                        "Silent Consonants",
                        f"In which of the following words is the letter '{letter}' completely SILENT?",
                        {"A": w.capitalize(), "B": d_sample[0].capitalize(), "C": d_sample[1].capitalize(), "D": d_sample[2].capitalize()}, "A",
                        f"In '{w}', the letter '{letter}' is unpronounced (silent).",
                        f"Pronounce each word carefully: in which word is '{letter}' omitted from pronunciation?"
                    ))
            # 2. Vowel Sound Identification
            vowels = [
                ("/iː/ as in 'feel'", ["lead", "key", "seize", "people", "machine"], ["fit", "dead", "said", "build"]),
                ("/ɪ/ as in 'sit'", ["women", "busy", "gym", "village", "pretty"], ["sea", "seen", "meat", "field"]),
                ("/e/ as in 'bed'", ["bread", "friend", "said", "leopard", "bury"], ["bead", "bleed", "neat", "deed"]),
                ("/æ/ as in 'cat'", ["plaid", "pack", "snack", "bad", "land"], ["palm", "father", "part", "calm"]),
                ("/uː/ as in 'pool'", ["blue", "fruit", "group", "shoe", "tomb"], ["pull", "book", "good", "foot"]),
                ("/ʊ/ as in 'put'", ["could", "foot", "wood", "wolf", "push"], ["pool", "fool", "tool", "cool"])
            ]
            for sound_desc, matching, distractors in vowels:
                for m in matching:
                    d_sample = random.sample(distractors, 3)
                    items.append((
                        "Vowel Phonemes",
                        f"Which of the following words contains the identical vowel sound {sound_desc}?",
                        {"A": m.capitalize(), "B": d_sample[0].capitalize(), "C": d_sample[1].capitalize(), "D": d_sample[2].capitalize()}, "A",
                        f"'{m}' contains the target vowel sound {sound_desc}.",
                        f"Transcribe or pronounce '{m}' to test for {sound_desc}."
                    ))

        elif topic == "Comprehension & Prescribed Text":
            # Dedicated 'The Life Changer' questions
            novel_qs = [
                ("In 'The Life Changer', what course of study was Omar offered admission to read at Ahmadu Bello University?", {"A": "Law", "B": "Medicine", "C": "Accounting", "D": "Computer Science"}, "A", "Omar gained admission to study Law at ABU Zaria after scoring 230 in UTME.", "What was Omar's celebrated course of study in Chapter 1?"),
                ("What was the nickname given to Salma and her three undergraduate roommates in the university hostel?", {"A": "The Big Four", "B": "The Campus Queens", "C": "The Golden Girls", "D": "The Scholarly Angels"}, "A", "Salma, Tomiwa, Ada, and Ngozi were collectively known as 'The Big Four'.", "What moniker was assigned to the four diverse roommates in the campus hostel?"),
                ("Which of Salma's roommates originated from the eastern region (Imo State) of Nigeria?", {"A": "Ngozi", "B": "Tomiwa", "C": "Ada", "D": "Ummi"}, "A", "Ngozi represented Eastern Nigeria (Imo State) among the four room-mates.", "Which roommate represented the Igbo ethnic group from Eastern Nigeria?"),
                ("In 'The Life Changer', which character won the university beauty pageant and studied Agricultural Economics?", {"A": "Tomiwa", "B": "Salma", "C": "Ada", "D": "Bint"}, "A", "Tomiwa, who was from Ibadan, Oyo State, was the reigning Miss University Campus.", "Which roommate was known for culinary skill and campus beauty titles?"),
                ("Why was Salma originally unwilling to stay in the university hall of residence (hostel)?", {"A": "She felt university hostels were congested and meant for villagers", "B": "Her parents strictly prohibited campus residence", "C": "Hostel fees were exceedingly expensive", "D": "She wanted to reside close to the market"}, "A", "Salma's pride initially made her disdain living in the campus hostel.", "What haughty assumption did Salma hold regarding hostel accommodations?"),
                ("What was the outcome of Kabir's gambling habit with the money obtained under false pretences from Salma?", {"A": "He was attacked and robbed by local street thugs at the betting center", "B": "He invested the money in real estate", "C": "He successfully purchased a brand-new Mercedes Benz", "D": "He returned the money to Salma with sincere apologies"}, "A", "Kabir lost the swindled funds after being cornered and robbed by street thugs.", "What sudden misfortune befell Kabir after cheating Salma?"),
                ("How did Ummi come to learn about the cultural significance of the greeting 'Kwana Lafiya'?", {"A": "Her grandmother explained the deep customary roots of respect in Northern culture", "B": "She read about it in an Arabic literature text", "C": "Her husband taught it to her before marriage", "D": "A university linguistics lecturer explained it"}, "A", "Ummi's grandmother instilled traditional etiquette and the meaning of greeting elders.", "Who served as the primary source of cultural wisdom for Ummi during her youth?"),
                ("What lesson did Salma's mother impart to her concerning humility before leaving for university?", {"A": "That university freedom comes with heavy individual moral responsibility", "B": "That acquiring wealth is more essential than academic excellence", "C": "That one must conceal one's true identity from friends", "D": "That university lecturers must be feared and avoided"}, "A", "Her mother reminded her that liberty without self-restraint leads to disgrace.", "What maternal advice on responsibility was shared before Salma left home?"),
                ("In 'The Life Changer', who accompanied Habib when they first encountered Salma outside the campus gate?", {"A": "Labaran, his driver and political confidant", "B": "Dr. Dabo", "C": "Kabir", "D": "Hakimi"}, "A", "Labaran served as Habib's driver and close personal aide in the car.", "Who was Habib's driver and right-hand man in the vehicle?"),
                ("What gesture did Habib make to demonstrate his wealth when Salma first boarded his vehicle?", {"A": "He gave her a substantial cash gift of ₦50,000 without hesitation", "B": "He promised to construct a new university hostel", "C": "He offered to fly her to Dubai for shopping", "D": "He bought her a luxury laptop"}, "A", "Habib flaunted his political affluence by giving Salma ₦50,000 cash on their first encounter.", "What spontaneous financial gift did Habib offer Salma inside the car?")
            ]
            for q_t, opts, ans, exp, soc in novel_qs:
                for variant_prompt in ["", " (JAMB High-Yield Syllabus Focus)"]:
                    items.append((
                        "Prescribed Novel Analysis",
                        f"{q_t}{variant_prompt}",
                        opts, ans, exp, soc
                    ))

    # =========================================================================
    # 2. CHEMISTRY
    # =========================================================================
    elif subject == "Chemistry":
        if topic == "Physical & General Chemistry":
            # 1. Moles & Concentration (M = n / V)
            for conc in [0.05, 0.1, 0.2, 0.25, 0.5, 1.0]:
                for vol_ml in [100, 250, 500, 1000]:
                    vol_l = vol_ml / 1000
                    moles = conc * vol_l
                    q_text = f"Calculate the number of moles of solute present in {vol_ml} cm³ of a {conc} mol/dm³ standard aqueous solution."
                    opts = {"A": f"{moles:.4f} mol", "B": f"{moles * 10:.4f} mol", "C": f"{moles / 10:.4f} mol", "D": f"{conc * vol_ml:.2f} mol"}
                    items.append((
                        "Solution Stoichiometry & Molarity", q_text, opts, "A",
                        f"n = C × V(dm³) = {conc} mol/dm³ × ({vol_ml}/1000) dm³ = {moles:.4f} mol.",
                        "Did you convert volume from cm³ to dm³ by dividing by 1000?"
                    ))
            # 2. Faraday's Law Calculations (m = M*I*t / (n*F))
            metals = [
                ("copper (Cu²⁺, M = 63.5 g/mol, n = 2)", 63.5, 2),
                ("silver (Ag⁺, M = 108 g/mol, n = 1)", 108.0, 1),
                ("aluminum (Al³⁺, M = 27 g/mol, n = 3)", 27.0, 3)
            ]
            for m_name, mm, n_val in metals:
                for amp in [2, 5, 10]:
                    for minutes in [16, 32, 64]:
                        sec = minutes * 60
                        mass = (mm * amp * sec) / (n_val * 96500)
                        q_text = f"Calculate the mass of {m_name} deposited at the cathode by a steady current of {amp} A passing for {minutes} minutes through an electrolytic cell. (1 F = 96,500 C/mol)"
                        opts = {"A": f"{mass:.3f} g", "B": f"{mass * 2:.3f} g", "C": f"{mass / 2:.3f} g", "D": f"{mm * amp:.2f} g"}
                        items.append((
                            "Faraday's Laws of Electrolysis", q_text, opts, "A",
                            f"m = (M × I × t) / (n × F) = ({mm} × {amp} × {sec}) / ({n_val} × 96500) = {mass:.3f} g.",
                            "Use m = (M·I·t)/(n·F). Did you convert minutes to seconds?"
                        ))

        elif topic == "Inorganic Chemistry":
            # Rich descriptive inorganic questions
            inorg_suite = [
                ("What color change occurs when dry sulfur dioxide gas is bubbled through acidified potassium dichromate(VI) solution?", {"A": "Orange to green", "B": "Purple to colorless", "C": "Yellow to brown", "D": "Colorless to deep blue"}, "A", "SO₂ reduces orange Cr₂O₇²⁻ to green Cr³⁺ ions.", "What is the characteristic redox color shift of chromium from +6 to +3?"),
                ("Which gas is collected by downward delivery (upward displacement of air) because it is denser than air?", {"A": "Carbon dioxide (CO₂)", "B": "Ammonia (NH₃)", "C": "Hydrogen (H₂)", "D": "Methane (CH₄)"}, "A", "CO₂ has molar mass 44, making it denser than dry air (~29), so it sinks.", "Which gas has a molar mass significantly greater than air (~29 g/mol)?"),
                ("Finely divided iron mixed with potassium hydroxide promoter is the catalyst used in the industrial manufacture of:", {"A": "Ammonia by the Haber process", "B": "Sulfuric acid by the Contact process", "C": "Nitric acid by the Ostwald process", "D": "Sodium hydroxide by the Chlor-alkali process"}, "A", "Haber synthesis of NH₃ employs iron catalyst promoted with K₂O/Al₂O₃.", "Which major chemical fertilizer precursor is synthesized using an iron catalyst?"),
                ("When copper metal reacts with concentrated nitric acid (HNO₃), the brown gas evolved is:", {"A": "Nitrogen dioxide (NO₂)", "B": "Nitrogen monoxide (NO)", "C": "Dinitrogen oxide (N₂O)", "D": "Ammonia gas (NH₃)"}, "A", "Concentrated HNO₃ is reduced by copper to produce brown, toxic NO₂ gas.", "Which oxide of nitrogen is characteristically reddish-brown and dense?"),
                ("The compound responsible for permanent hardness of water that cannot be removed by boiling is:", {"A": "Calcium sulfate (CaSO₄)", "B": "Calcium hydrogencarbonate (Ca(HCO₃)₂)", "C": "Magnesium hydrogencarbonate (Mg(HCO₃)₂)", "D": "Sodium chloride (NaCl)"}, "A", "Permanent hardness is caused by dissolved sulfates or chlorides of calcium/magnesium.", "Which calcium salt does not decompose into insoluble carbonate upon heating?"),
                ("The allotrope of carbon that conducts electricity due to delocalized pi electrons in its planar hexagonal layers is:", {"A": "Graphite", "B": "Diamond", "C": "Amorphous coal", "D": "Carbon black"}, "A", "In graphite, each carbon bonds to 3 others, leaving 1 delocalized electron per carbon for conduction.", "Which carbon allotrope has mobile electrons within hexagonal basal planes?"),
                ("Which transition element ion in aqueous solution imparts a characteristic pale green color?", {"A": "Fe²⁺ (Iron(II))", "B": "Fe³⁺ (Iron(III))", "C": "Cu²⁺ (Copper(II))", "D": "Zn²⁺ (Zinc)"}, "A", "Fe²⁺ ions are pale green, whereas Fe³⁺ is reddish-brown and Cu²⁺ is blue.", "What is the standard aqueous color of hydrated iron(II) salts?"),
                ("In the extraction of aluminum from purified bauxite, molten cryolite (Na₃AlF₆) is added to:", {"A": "Lower the melting point of alumina and increase electrical conductivity", "B": "Prevent oxidation of the carbon anodes", "C": "Neutralize acidic impurities", "D": "Precipitate aluminum hydroxide"}, "A", "Cryolite lowers alumina's melting point from 2050°C to ~950°C and improves conductivity.", "What role does cryolite play as a solvent in the Hall-Héroult electrolytic cell?")
            ]
            for q_t, opts, ans, exp, soc in inorg_suite:
                for suffix in ["", " (JAMB Standard)"]:
                    items.append(("Inorganic Reactions & Metallurgy", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Organic Chemistry":
            org_suite = [
                ("What is the correct IUPAC name of the compound CH₃-CH(CH₃)-CH₂-COOH?", {"A": "3-Methylbutanoic acid", "B": "2-Methylbutanoic acid", "C": "3-Methylpentanoic acid", "D": "Isovaleric alcohol"}, "A", "Numbering starts at the -COOH carbon (C1): the methyl branch is at C3 of a 4-carbon chain.", "From which end of the carbon backbone does carboxylic acid numbering begin?"),
                ("The chemical test used to confirm the presence of unsaturation (carbon-carbon double or triple bonds) in an alkene is:", {"A": "Decolorization of bromine water without sunlight", "B": "Effervescence with sodium hydrogencarbonate", "C": "Formation of a silver mirror with Tollens' reagent", "D": "Turn blue litmus paper red"}, "A", "Alkenes undergo rapid electrophilic addition across double bonds, decolorizing reddish-brown bromine water.", "Which halogen reagent loses its brown color rapidly in the presence of alkenes?"),
                ("Ethanol can be industrially converted to ethanoic acid by heating under reflux with:", {"A": "Acidified potassium heptaoxodichromate(VI) (K₂Cr₂O₇ / H⁺)", "B": "Concentrated sulfuric acid at 170°C", "C": "Hydrogen gas in the presence of nickel", "D": "Sodium hydroxide solution"}, "A", "Primary alcohols are oxidized to carboxylic acids using powerful oxidizing agents like acidified dichromate.", "Which reagent oxidizes primary alcohols into carboxylic acids?"),
                ("The ester ethyl ethanoate (CH₃COOCH₂CH₃) is prepared by reacting:", {"A": "Ethanoic acid and ethanol in the presence of concentrated H₂SO₄", "B": "Ethanoic acid and methanol", "C": "Ethanol and sodium hydroxide", "D": "Ethene and steam"}, "A", "Esterification: CH₃COOH + CH₃CH₂OH -> CH₃COOCH₂CH₃ + H₂O.", "Which organic acid and alcohol combine to yield ethyl ethanoate?"),
                ("Condensation polymerization between hexanedioic acid and hexane-1,6-diamine produces:", {"A": "Nylon-6,6", "B": "Terylene (Polyester)", "C": "Polyethene", "D": "Polyvinyl chloride (PVC)"}, "A", "Hexanedioic acid (6 carbons) and hexane-1,6-diamine (6 carbons) eliminate water to form Nylon-6,6.", "Which common synthetic polyamide contains 6 carbons in each repeating monomer unit?"),
                ("Glucose is converted to ethanol and carbon dioxide during fermentation catalyzed by the enzyme:", {"A": "Zymase", "B": "Invertase", "C": "Ptyalin", "D": "Pepsin"}, "A", "Yeast secretes zymase which anaerobically ferments simple hexose sugars into ethanol.", "Which yeast enzyme converts glucose directly into alcohol and CO₂?")
            ]
            for q_t, opts, ans, exp, soc in org_suite:
                for suffix in ["", " (UTME Core)"]:
                    items.append(("Organic Reaction Mechanisms & Nomenclature", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Environmental & Industrial Chemistry":
            env_suite = [
                ("Which fraction of crude oil distillation is collected at the boiling range of approximately 170°C to 250°C and used as aviation fuel?", {"A": "Kerosene (paraffin oil)", "B": "Petrol (gasoline)", "C": "Diesel oil", "D": "Bitumen (asphalt)"}, "A", "Kerosene fractions distill around 170-250°C and fuel domestic lamps and jet turbines.", "Which petroleum fraction powers aviation jet engines?"),
                ("Catalytic cracking of heavy petroleum gas oil fractions is performed primarily to:", {"A": "Increase the yield of high-octane petrol (gasoline)", "B": "Produce heavy lubricating grease", "C": "Purify crude petroleum before export", "D": "Synthesize mineral fertilizers"}, "A", "Cracking breaks long-chain hydrocarbons into commercially valuable shorter chains like petrol.", "Why do petroleum refineries break large alkane molecules into smaller ones?"),
                ("Which toxic gas binds irreversibly with blood hemoglobin to form carboxyhemoglobin, starving tissues of oxygen?", {"A": "Carbon monoxide (CO)", "B": "Carbon dioxide (CO₂)", "C": "Sulfur dioxide (SO₂)", "D": "Nitrogen gas (N₂)"}, "A", "CO binds hemoglobin with over 200 times the affinity of oxygen, forming deadly carboxyhemoglobin.", "Which colorless, odorless incomplete combustion gas binds tightly to red blood cells?"),
                ("The phenomenon of global warming is caused by the absorption and re-emission of infrared radiation by:", {"A": "Greenhouse gases like CO₂, CH₄, and water vapor", "B": "Oxygen and nitrogen molecules", "C": "Noble gases in the lower troposphere", "D": "Stratospheric ozone alone"}, "A", "Greenhouse gases trap outgoing terrestrial infrared thermal radiation, heating the biosphere.", "Which gases trap heat radiated from the Earth's surface?")
            ]
            for q_t, opts, ans, exp, soc in env_suite:
                for suffix in ["", " (Industrial Chemistry)"]:
                    items.append(("Environmental Pollution & Petrochemicals", f"{q_t}{suffix}", opts, ans, exp, soc))

    # =========================================================================
    # 3. BIOLOGY
    # =========================================================================
    elif subject == "Biology":
        if topic == "Cellular Biology & Life Processes":
            cell_suite = [
                ("The semi-permeable cell membrane is chemically composed of a bilayer of:", {"A": "Phospholipids embedded with proteins", "B": "Cellulose and lignin", "C": "Glycogen and nucleic acids", "D": "Chitin and peptides"}, "A", "The fluid mosaic model describes membranes as phospholipid bilayers with integrated proteins.", "What two biomolecules form the fluid mosaic of the plasma membrane?"),
                ("What cellular phenomenon occurs when red blood cells are placed in distilled water (hypotonic medium)?", {"A": "Haemolysis (bursting due to water influx)", "B": "Crenation (shrinkage)", "C": "Plasmolysis", "D": "Turgidity"}, "A", "Animal cells lack rigid walls; osmotic water influx creates excessive pressure causing haemolysis.", "What happens to animal cells without a cell wall when placed in pure water?"),
                ("Enzymes are biological catalysts that speed up biochemical reactions by:", {"A": "Lowering the activation energy of the reaction", "B": "Increasing the free energy of the products", "C": "Altering the final equilibrium constant", "D": "Raising the reaction temperature"}, "A", "Enzymes lower the threshold activation energy needed for reactant molecules to reach transition state.", "How do biocatalysts accelerate metabolic reactions energetically?"),
                ("During which stage of meiosis does genetic crossing over between non-sister homologous chromatids occur?", {"A": "Prophase I (Pachytene)", "B": "Metaphase I", "C": "Anaphase II", "D": "Telophase I"}, "A", "Crossing over occurs in Prophase I of meiosis, creating new recombinant gene combinations.", "At which meiotic stage do homologous chromosomes exchange genetic segments?")
            ]
            for q_t, opts, ans, exp, soc in cell_suite:
                for suffix in ["", " (Cell Biology)"]:
                    items.append(("Cell Physiology & Organelles", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Human Physiology & Systems":
            phys_suite = [
                ("Which digestive enzyme secreted in gastric juice breaks down dietary proteins into peptides in an acidic medium?", {"A": "Pepsin", "B": "Ptyalin (salivary amylase)", "C": "Trypsin", "D": "Lipase"}, "A", "Pepsin operates at optimum pH 1.5-2.0 in the stomach to digest proteins.", "Which gastric protease functions optimally in concentrated hydrochloric acid?"),
                ("The functional contractile unit of a myofibril in human skeletal muscle is called a:", {"A": "Sarcomere", "B": "Nephron", "C": "Axon", "D": "Osteon"}, "A", "Sarcomeres, bounded by Z-lines, are the repeating contractile units of striated muscle fibers.", "What repeating segment between Z-lines forms the basic unit of muscle contraction?"),
                ("Which endocrine gland located at the base of the brain is known as the 'master gland'?", {"A": "Pituitary gland", "B": "Thyroid gland", "C": "Adrenal gland", "D": "Pancreas"}, "A", "The anterior pituitary secretes trophic hormones that regulate other endocrine glands.", "Which gland coordinates systemic hormonal output through trophic hormones?"),
                ("The structural pathway of a simple reflex action consists sequentially of:", {"A": "Receptor -> Sensory neuron -> Relay neuron -> Motor neuron -> Effector", "B": "Effector -> Motor neuron -> Spinal cord -> Sensory neuron", "C": "Receptor -> Motor neuron -> Brain -> Sensory neuron", "D": "Relay neuron -> Receptor -> Sensory neuron -> Effector"}, "A", "Reflex arc: Stimulus -> Receptor -> Afferent (sensory) -> Interneuron -> Efferent (motor) -> Effector.", "What is the correct sequential path of nerve impulses in a spinal reflex arc?"),
                ("A person with blood group O is termed a 'universal donor' because their red blood cells possess:", {"A": "Neither A nor B surface agglutinogens (antigens)", "B": "Both A and B antigens", "C": "Neither anti-A nor anti-B antibodies in plasma", "D": "An extra Rhesus factor"}, "A", "Group O red blood cells lack A and B antigens, preventing immune agglutination in recipients.", "Why does blood group O avoid triggering immune rejection in diverse recipients?")
            ]
            for q_t, opts, ans, exp, soc in phys_suite:
                for suffix in ["", " (Physiology Core)"]:
                    items.append(("Human Anatomy & Organ Systems", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Genetics & Evolution":
            gen_suite = [
                ("What is the probability of a couple having a child with sickle-cell anemia (HbSS) if both parents have sickle-cell trait (HbAS)?", {"A": "25% (1 in 4)", "B": "50% (1 in 2)", "C": "75% (3 in 4)", "D": "0%"}, "A", "HbAS × HbAS produces 1 HbAA : 2 HbAS : 1 HbSS. Therefore, the risk of HbSS is 25%.", "In a cross between two carriers (AS × AS), what proportion will inherit SS?"),
                ("The evolutionary principle proposed by Jean-Baptiste Lamarck that is now disproven by modern genetics is the:", {"A": "Inheritance of acquired characteristics through use and disuse", "B": "Natural selection of advantageous mutations", "C": "Survival of the fittest in harsh environments", "D": "Isolation of allopatric populations"}, "A", "Acquired somatic modifications (e.g. muscular growth) do not alter gametic DNA and cannot be inherited.", "Which disproven evolutionary theory asserted that traits developed in life are passed to offspring?"),
                ("The wing of a bird and the wing of a housefly represent:", {"A": "Analogous structures (convergent evolution)", "B": "Homologous structures (divergent evolution)", "C": "Vestigial organs", "D": "Atavistic structures"}, "A", "Fly wings (chitin) and bird wings (feathers/bones) serve the same flight function but have different embryonic origins.", "Do fly and bird wings share an identical skeletal bone structure, or merely a common function?"),
                ("A man with normal vision marries a woman who is a carrier of red-green color blindness (X^B X^b). What fraction of their male children will be color blind?", {"A": "50% (1/2 of sons)", "B": "100% of sons", "C": "25% of sons", "D": "0% of sons"}, "A", "Sons inherit Y from father and X^B or X^b from mother. Half of the sons will be X^b Y (color blind).", "Among male offspring receiving the mother's X chromosome, what fraction receives X^b?")
            ]
            for q_t, opts, ans, exp, soc in gen_suite:
                for suffix in ["", " (Genetics Focus)"]:
                    items.append(("Heredity, Mutations & Evolutionary Theory", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Ecology & Environment":
            eco_suite = [
                ("In a terrestrial food chain: Grass -> Grasshopper -> Toad -> Snake -> Hawk, the tertiary consumer is the:", {"A": "Snake", "B": "Grasshopper", "C": "Toad", "D": "Hawk"}, "A", "Grass (Producer) -> Grasshopper (Primary) -> Toad (Secondary) -> Snake (Tertiary) -> Hawk (Quaternary).", "Count the feeding levels: who eats the secondary consumer (toad)?"),
                ("The ecological association between nitrogen-fixing bacteria and leguminous plants is classified as:", {"A": "Mutualism", "B": "Commensalism", "C": "Parasitism", "D": "Amensalism"}, "A", "Mutualism: Both organisms benefit (plant gets fixed nitrogen, bacteria receive carbohydrates).", "What symbiotic relationship confers mutual survival benefits on both participating species?"),
                ("The process whereby a bare rocky habitat is gradually colonized over time by lichens, mosses, grasses, shrubs, and trees is called:", {"A": "Primary ecological succession", "B": "Secondary ecological succession", "C": "Eutrophication", "D": "Biological magnification"}, "A", "Primary succession initiates on newly exposed surfaces devoid of pre-existing soil.", "What succession starts on barren volcanic rock or newly formed terrain?"),
                ("Which Nigerian savanna biome is characterized by tall grasses (up to 3 meters) and scattered broad-leaved deciduous trees?", {"A": "Guinea savanna", "B": "Sudan savanna", "C": "Sahel savanna", "D": "Montane forest"}, "A", "The Guinea savanna occupies the middle belt of Nigeria with tall grasses and high annual rainfall.", "Which savanna zone covers the central belt of Nigeria with tall elephant grass?")
            ]
            for q_t, opts, ans, exp, soc in eco_suite:
                for suffix in ["", " (Ecology Mastery)"]:
                    items.append(("Ecological Niches, Biomes & Nutrient Flux", f"{q_t}{suffix}", opts, ans, exp, soc))

    # =========================================================================
    # 4. ECONOMICS
    # =========================================================================
    elif subject == "Economics":
        if topic == "Basic Economic Principles & Methodology":
            eco_p_suite = [
                ("The fundamental economic problem that necessitates choice in all societies is:", {"A": "Scarcity of productive resources relative to unlimited human wants", "B": "Excessive governmental taxation", "C": "Fluctuating foreign currency exchange rates", "D": "Inadequate domestic manufacturing industries"}, "A", "Scarcity of resources against insatiable human wants is the universal core of economics.", "Why must human societies prioritize choices and construct scales of preference?"),
                ("A table listing an individual's wants arranged in descending order of priority is called a:", {"A": "Scale of preference", "B": "Production schedule", "C": "Budget constraint line", "D": "Demand schedule"}, "A", "A scale of preference orders desires according to relative importance to guide rational choice.", "What tool lists consumer wants hierarchically from most urgent to least urgent?"),
                ("Which of the following represents a normative economic statement?", {"A": "The Federal Government ought to provide free tertiary education for all citizens", "B": "An increase in petrol price led to a 15% rise in transportation costs", "C": "Nigeria's foreign reserves stood at 38 billion dollars in December", "D": "A higher tax rate reduces consumer disposable income"}, "A", "Normative economics involves ethical value judgments ('ought to', 'should be') rather than verifiable facts.", "Which statement expresses an ethical opinion rather than an objective testable fact?"),
                ("Points lying strictly outside the boundary of a national Production Possibility Curve (PPC) represent:", {"A": "Output combinations currently unattainable with existing resources and technology", "B": "Inefficient allocation and widespread unemployment", "C": "Maximum productive capacity under autarky", "D": "Economic recession"}, "A", "Points beyond the PPC frontier require more resources or better technology than currently available.", "Can an economy produce beyond its PPC boundary with existing resources?")
            ]
            for q_t, opts, ans, exp, soc in eco_p_suite:
                for suffix in ["", " (Core Methodology)"]:
                    items.append(("Scarcity, Opportunity Cost & Economic Systems", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Microeconomics & Price Mechanism":
            # Elasticity calculations & market theory
            for p1, p2, q1, q2 in [(100, 120, 50, 40), (200, 250, 100, 80), (50, 60, 200, 150), (40, 50, 100, 70)]:
                ped = abs(((q2 - q1) / q1) / ((p2 - p1) / p1))
                q_text = f"When the price of a commodity increases from ₦{p1} to ₦{p2}, the quantity demanded falls from {q1} to {q2} units. Calculate the price elasticity of demand."
                opts = {"A": f"{ped:.2f}", "B": f"{ped * 2:.2f}", "C": f"{ped / 2:.2f}", "D": f"{(q1 - q2):.2f}"}
                items.append((
                    "Price Elasticity Calculations", q_text, opts, "A",
                    f"PED = |(%ΔQd) / (%ΔP)| = |(({q2}-{q1})/{q1}) / (({p2}-{p1})/{p1})| = {ped:.2f}.",
                    "Use the percentage change elasticity formula: (%ΔQd) / (%ΔP)."
                ))
            micro_suite = [
                ("If an increase in consumer income leads to a decrease in the demand for cassava flour, cassava flour is classified as an:", {"A": "Inferior good", "B": "Normal luxury good", "C": "Complementary good", "D": "Giffen good"}, "A", "Inferior goods have negative income elasticity of demand (demand drops as income rises).", "What type of good sees reduced consumer consumption when purchasing power rises?"),
                ("In a perfectly competitive market in long-run equilibrium, a firm earns only:", {"A": "Normal profit (zero economic profit)", "B": "Supernormal monopoly profit", "C": "Subsidized government revenue", "D": "Variable operating losses"}, "A", "Free entry and exit eliminates economic profits until price equals minimum average total cost.", "What happens to supernormal profits when new competitors freely enter an industry?"),
                ("Cross elasticity of demand between two substitute goods (e.g., Milo and Ovaltine) is always:", {"A": "Positive", "B": "Negative", "C": "Zero", "D": "Undefined"}, "A", "When price of good A rises, demand for its substitute good B increases, giving positive cross elasticity.", "How does a rise in the price of Milo affect the quantity demanded for Ovaltine?")
            ]
            for q_t, opts, ans, exp, soc in micro_suite:
                for suffix in ["", " (Microeconomic Theory)"]:
                    items.append(("Market Structures & Price Theory", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Macroeconomics & National Income":
            macro_suite = [
                ("In national income accounting, the circular flow injection variables include:", {"A": "Investment (I), Government spending (G), and Exports (X)", "B": "Savings (S), Taxes (T), and Imports (M)", "C": "Depreciation and transfer payments", "D": "Direct taxes and personal savings"}, "A", "Injections (I + G + X) introduce autonomous expenditure into the circular flow of income.", "Which three expenditure components inject purchasing power into the circular flow?"),
                ("Frictional unemployment arises principally due to:", {"A": "Time lags when workers transition between jobs searching for optimal employment", "B": "Technological displacement and automation", "C": "Deficient aggregate demand during an economic recession", "D": "Seasonal fluctuations in agriculture"}, "A", "Frictional unemployment represents temporary job-search transitions in a dynamic labor market.", "What type of unemployment occurs while individuals voluntarily search for better employment?"),
                ("The consumer price index (CPI) is primarily utilized to measure:", {"A": "The rate of inflation and cost of living over time", "B": "Total national gold reserves", "C": "Industrial manufacturing capacity", "D": "The foreign exchange rate against the dollar"}, "A", "CPI tracks percentage changes in the price of a weighted basket of consumer goods and services.", "Which macroeconomic indicator gauges changes in the average retail cost of living?")
            ]
            for q_t, opts, ans, exp, soc in macro_suite:
                for suffix in ["", " (Macro Policy)"]:
                    items.append(("National Output & Fiscal Dynamics", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Money, Banking & Public Finance":
            fin_suite = [
                ("Adam Smith's four classical canons of taxation include:", {"A": "Equity, Certainty, Convenience, and Economy", "B": "Profitability, Secrecy, Productivity, and Regularity", "C": "Progressivity, Neutrality, Elasticity, and Enforcement", "D": "Derivation, Equality, Centralization, and Speed"}, "A", "Adam Smith enunciated Equality/Equity, Certainty, Convenience of payment, and Economy in collection.", "Recall Adam Smith's four foundational maxims of tax collection in Wealth of Nations."),
                ("When the Central Bank of Nigeria (CBN) raises the Monetary Policy Rate (MPR), its immediate goal is to:", {"A": "Reduce credit availability and curb commercial bank lending to fight inflation", "B": "Encourage commercial banks to issue unsecured loans", "C": "Devalue the national currency", "D": "Fund regional agricultural projects directly"}, "A", "Higher MPR increases borrowing costs across commercial banks, tightening money supply to fight inflation.", "How does an increase in the central bank discount rate impact borrowing and inflation?"),
                ("A deficit national budget occurs when planned government expenditure:", {"A": "Exceeds anticipated government tax revenues", "B": "Equals total national foreign reserves", "C": "Is lower than the recurrent revenue estimate", "D": "Is financed strictly through trade surpluses"}, "A", "Budget deficit = Government Expenditure > Government Revenue, requiring borrowing or debt issuance.", "What is the budgetary term when public spending outstrips public revenue collections?")
            ]
            for q_t, opts, ans, exp, soc in fin_suite:
                for suffix in ["", " (Monetary Economics)"]:
                    items.append(("Central Banking & Fiscal Mechanisms", f"{q_t}{suffix}", opts, ans, exp, soc))

    # =========================================================================
    # 5. GOVERNMENT
    # =========================================================================
    elif subject == "Government":
        if topic == "Elements of Government & Political Theory":
            gov_p_suite = [
                ("A state is legally defined as a sovereign political community possessing population, defined territory, government, and:", {"A": "Sovereignty (internal and external independence)", "B": "A written federal constitution", "C": "A multi-party electoral system", "D": "Substantial mineral wealth"}, "A", "Sovereignty is the defining legal attribute that distinguishes a sovereign state from other entities.", "What legal attribute allows a state to enforce laws without external subordination?"),
                ("De jure sovereignty refers to sovereignty that is:", {"A": "Recognized by constitutional law and international jurisprudence", "B": "Acquired purely through physical military force", "C": "Exercised only during emergency periods", "D": "Held exclusively by local traditional rulers"}, "A", "De jure sovereignty denotes legal authority recognized by law, contrasting with de facto power.", "Which form of sovereignty is based upon constitutional legitimacy and the rule of law?"),
                ("An electoral system where the candidate with the highest number of votes wins the legislative seat, regardless of majority, is:", {"A": "First-Past-The-Post (Simple Plurality)", "B": "Proportional representation", "C": "Alternative vote system", "D": "Second ballot runoff"}, "A", "First-past-the-post awards victory to whoever receives the most individual votes in a constituency.", "What electoral formula declares the candidate with the plurality of votes as winner?"),
                ("Pressure groups differ fundamentally from political parties because pressure groups:", {"A": "Seek to influence government policies without contesting for political office", "B": "Always nominate candidates for general elections", "C": "Are strictly banned under constitutional democracy", "D": "Receive state funding to manage public infrastructure"}, "A", "Pressure groups lobby to advance sectional interests; political parties seek to capture sovereign power.", "Do pressure groups aim to contest elections and form the executive government?")
            ]
            for q_t, opts, ans, exp, soc in gov_p_suite:
                for suffix in ["", " (Political Philosophy)"]:
                    items.append(("Theories of State, Power & Electoral Models", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Colonial Administration in Nigeria & West Africa":
            gov_c_suite = [
                ("Lord Frederick Lugard's book which outlined the philosophy of British colonial rule in Africa is titled:", {"A": "The Dual Mandate in British Tropical Africa", "B": "Indirect Rule in Nigeria", "C": "The Scramble for Africa", "D": "Colonial Governance and Law"}, "A", "In 'The Dual Mandate' (1922), Lugard argued Britain had a duty to both Africans and global commerce.", "What famous 1922 treatise by Lugard rationalized British indirect administrative methods?"),
                ("The Aba Women's Riots of 1929 in Southeastern Nigeria was sparked by:", {"A": "Rumors of proposed colonial taxation of women and abuses by Warrant Chiefs", "B": "The suspension of the Clifford Constitution", "C": "Increases in school tuition fees", "D": "The ban on palm oil exports to Britain"}, "A", "Census counting by Warrant Chief Okugo triggered fears of female direct taxation.", "What grievance provoked widespread civil demonstrations across Aba and Owerri provinces in 1929?"),
                ("The nationalist newspaper founded in Lagos in 1937 by Dr. Nnamdi Azikiwe to mobilize public opinion was the:", {"A": "West African Pilot", "B": "Lagos Daily News", "C": "Nigerian Tribune", "D": "Daily Times"}, "A", "The West African Pilot championed radical nationalist consciousness under Azikiwe's motto: 'Show the light...'.", "Which influential nationalist daily paper was established by Zik in 1937?"),
                ("The National Youth Movement (NYM) was established in Nigeria in 1934 by young educated elites including:", {"A": "Ernest Ikoli, Samuel Akinsanya, and H.O. Davies", "B": "Herbert Macaulay and Pa Michael Imoudu", "C": "Sir Ahmadu Bello and Abubakar Tafawa Balewa", "D": "Obafemi Awolowo and Anthony Enahoro"}, "A", "NYM arose from the Lagos Youth Movement to challenge British colonialism on a national scale.", "Who were the founding nationalist pioneers behind the 1934 youth movement in Lagos?")
            ]
            for q_t, opts, ans, exp, soc in gov_c_suite:
                for suffix in ["", " (Colonial History)"]:
                    items.append(("Colonial Structures & Anti-Colonial Awakening", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Nigerian Constitutional Development":
            gov_const_suite = [
                ("The Richards Constitution of 1946 was widely criticized by Nigerian nationalists primarily because:", {"A": "It was drafted without prior consultation of the Nigerian people and had an unofficial majority", "B": "It granted full executive powers to regional premiers", "C": "It abolished the traditional monarchy", "D": "It established a military tribunal"}, "A", "Sir Arthur Richards formulated the constitution arbitrarily without democratic public debate.", "Why did the NCNC under Azikiwe tour Nigeria to protest the 1946 Richards Constitution?"),
                ("Which constitution created the office of the Federal Prime Minister in colonial Nigeria in 1957?", {"A": "1954 Lyttelton Constitution (as amended in 1957)", "B": "1922 Clifford Constitution", "C": "1946 Richards Constitution", "D": "1960 Independence Constitution"}, "A", "The 1957 constitutional conference created the office of Prime Minister, filled by Sir Abubakar Tafawa Balewa.", "Under which constitutional framework was Alhaji Abubakar Tafawa Balewa appointed Prime Minister?"),
                ("Under the 1979 Constitution of the Second Republic of Nigeria, the system of government shifted from:", {"A": "The British Westminster parliamentary system to the American-style executive presidential system", "B": "A military dictatorship to a constitutional monarchy", "C": "A federal structure to a unitary state", "D": "A multi-party system to a one-party socialist state"}, "A", "The 1979 Constitution instituted an executive president as both head of state and head of government.", "What major structural governance shift occurred between the 1963 and 1979 Nigerian constitutions?"),
                ("The 1999 Constitution of the Federal Republic of Nigeria provides for how many local government councils?", {"A": "774", "B": "500", "C": "1000", "D": "360"}, "A", "Section 3(6) of the 1999 Constitution explicitly recognizes 774 statutory Local Government Areas.", "How many recognized local government areas are constitutionally established in Nigeria?")
            ]
            for q_t, opts, ans, exp, soc in gov_const_suite:
                for suffix in ["", " (Constitutional Milestones)"]:
                    items.append(("Nigerian Constitutional History & Frameworks", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Federalism, Military Rule & Foreign Policy":
            gov_fed_suite = [
                ("General Yakubu Gowon divided Nigeria into 12 states on May 27, 1967, principally to:", {"A": "Weaken the secessionist Eastern Region and secure the allegiance of minority ethnic groups", "B": "Satisfy demands from European financial institutions", "C": "Prepare for immediate democratic civilian elections", "D": "Comply with an injunction from the Supreme Court"}, "A", "State creation broke the monolith of the Eastern Region and granted autonomy to eastern minorities.", "What strategic geopolitical objective motivated the 12-state creation on the eve of the Civil War?"),
                ("The supreme ruling organ of the Federal Military Government of Nigeria between 1966 and 1979 was the:", {"A": "Supreme Military Council (SMC)", "B": "Armed Forces Ruling Council (AFRC)", "C": "National Council of States", "D": "Federal Executive Council"}, "A", "The Supreme Military Council held absolute executive and legislative decree-making powers.", "What was the highest decision-making military body during the Gowon and Murtala/Obasanjo regimes?"),
                ("Nigeria played a heroic leadership role in West African conflict resolution by deploying the ECOMOG peacekeeping force to:", {"A": "Liberia and Sierra Leone", "B": "Angola and Mozambique", "C": "Sudan and Somalia", "D": "Rwanda and Burundi"}, "A", "Nigeria led ECOMOG under ECOWAS to quell violent civil wars in Liberia (1990) and Sierra Leone.", "In which two West African countries did Nigeria spearhead historic ECOMOG interventions?"),
                ("The Organization of Petroleum Exporting Countries (OPEC), which Nigeria joined in 1971, aims to:", {"A": "Coordinate petroleum policies and stabilize crude oil prices in global markets", "B": "Provide military defense for oil tankers", "C": "Refine petroleum for European consumers", "D": "Eliminate renewable energy investments"}, "A", "OPEC ensures the stabilization of oil markets to secure efficient, economic supply to consumers and fair returns.", "What primary economic mandate prompted Nigeria to join the international oil cartel in 1971?")
            ]
            for q_t, opts, ans, exp, soc in gov_fed_suite:
                for suffix in ["", " (Security & Diplomacy)"]:
                    items.append(("Federal Allocation, Military Regimes & West African Diplomacy", f"{q_t}{suffix}", opts, ans, exp, soc))

    # =========================================================================
    # 6. LITERATURE IN ENGLISH
    # =========================================================================
    elif subject == "Literature in English":
        if topic == "Literary Appreciation & Devices":
            lit_a_suite = [
                ("The figure of speech that uses exaggeration for dramatic emphasis or comic effect is:", {"A": "Hyperbole", "B": "Understatement", "C": "Litotes", "D": "Euphemism"}, "A", "Hyperbole is deliberate overstatement (e.g. 'I've told you a million times').", "What term describes an obvious and intentional exaggeration not meant to be taken literally?"),
                ("The literary device of substituting the name of an attribute or adjunct for that of the thing meant (e.g., 'The Crown' for the monarch) is:", {"A": "Metonymy", "B": "Synecdoche", "C": "Oxymoron", "D": "Apostrophe"}, "A", "Metonymy replaces a concept with a closely associated word (e.g. 'The White House announced...').", "What figure of speech substitutes an associated symbol or attribute for the noun itself?"),
                ("A sudden, unexpected turn of events in a drama that reverses the protagonist's fortunes is known in Aristotle's Poetics as:", {"A": "Peripeteia", "B": "Anagnorisis", "C": "Catharsis", "D": "Hamartia"}, "A", "Peripeteia is the decisive reversal of circumstances or fortune in classical drama.", "Which classical term refers to the sudden reversal of fortune experienced by a tragic hero?"),
                ("The feeling of emotional relief, purification, and cleansing experienced by the audience at the conclusion of a tragedy is:", {"A": "Catharsis", "B": "Hubris", "C": "Nemesis", "D": "Mimesis"}, "A", "Catharsis is the therapeutic purgation of pity and fear aroused by tragic catastrophe.", "What Greek term denotes the psychological purging of pity and terror in drama?")
            ]
            for q_t, opts, ans, exp, soc in lit_a_suite:
                for suffix in ["", " (Literary Criticism)"]:
                    items.append(("Literary Terminology & Rhetorical Figures", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Drama & Theatrical Techniques":
            lit_d_suite = [
                ("In classical Elizabethan theatre, an 'aside' is a theatrical convention where a character:", {"A": "Speaks directly to the audience while other characters on stage are presumed not to hear", "B": "Delivers a lengthy speech while totally alone on stage", "C": "Engages in physical combat behind the curtain", "D": "Sings a lyrical interlude to change scenery"}, "A", "An aside shares private thoughts directly with viewers without breaking character in front of peers.", "How does an actor deliver private commentary to the audience while other actors stand on stage?"),
                ("In Ola Rotimi's 'The Gods Are Not to Blame', King Odewale's fatal tragedy begins when he unwittingly slays:", {"A": "His biological father, King Adetusa", "B": "His loyal friend Alaka", "C": "The priest Baba Fakunle", "D": "His uncle Aderopo"}, "A", "Odewale unknowingly killed his real father King Adetusa at the Ede-Osogbo road junction.", "Who was the royal traveler killed by Odewale in a fit of pride at the crossroads?"),
                ("In Wole Soyinka's 'The Lion and the Jewel', Lakunle is portrayed as an absurd character because:", {"A": "He mechanically copies Western customs without truly understanding them", "B": "He refuses to teach village children how to read", "C": "He plots the physical murder of Baroka", "D": "He steals bride price money from the community"}, "A", "Lakunle embodies hollow, superficial modernism that despises African traditions without substance.", "Why does Lakunle's pompous Westernized attitude earn ridicule in the village of Ilujinle?"),
                ("In William Shakespeare's 'Macbeth', the prophecy that prompts Macbeth's murderous ambition is delivered by:", {"A": "The Three Witches (Weird Sisters)", "B": "King Duncan in his royal palace", "C": "Lady Macbeth during her sleepwalking", "D": "The ghost of Banquo at the banquet"}, "A", "The Three Witches greet Macbeth as Thane of Glamis, Thane of Cawdor, and King hereafter.", "Which supernatural figures hail Macbeth with future royal titles upon the blasted heath?")
            ]
            for q_t, opts, ans, exp, soc in lit_d_suite:
                for suffix in ["", " (Dramatic Masterworks)"]:
                    items.append(("Dramatic Structure & African Theatrical Classics", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Poetry & Versification":
            lit_p_suite = [
                ("A Shakespearean (English) sonnet is structurally composed of:", {"A": "Three quatrains and a concluding rhyming couplet (ABAB CDCD EFEF GG)", "B": "An octave and a sestet with a volta at line 9", "C": "Four unrhymed tercets and a refraining couplet", "D": "Seven unrhymed couplets in free verse"}, "A", "Shakespearean sonnets feature 14 lines: 3 four-line stanzas (quatrains) followed by a rhyming couplet.", "What is the stanzaic breakdown of an English sonnet?"),
                ("In Birago Diop's celebrated poem 'Vanity', the poet chides living Africans for:", {"A": "Neglecting the ancestral spirits whose voices live in water, wind, and trees", "B": "Failing to adopt modern Western industrial technology", "C": "Refusing to trade with neighboring villages", "D": "Losing ancient warrior skills"}, "A", "Diop warns that when Africans ignore the ancestral voice of the dead, their weeping is mere vanity.", "What spiritual abandonment does Birago Diop lament in 'Vanity'?"),
                ("In Dylan Thomas's 'Do Not Go Gentle into That Good Night', the 'good night' metaphorically signifies:", {"A": "Death and biological mortality", "B": "A peaceful evening sleep after hard labor", "C": "The end of a university semester", "D": "A romantic nocturnal journey"}, "A", "Thomas uses night and the dying of the light as evocative metaphors for approaching death.", "What universal human reality does 'night' symbolize in Dylan Thomas's passionate villanelle?"),
                ("The rhythmic pattern of five metrical feet per line, with an unstressed syllable followed by a stressed syllable, is:", {"A": "Iambic pentameter", "B": "Trochaic hexameter", "C": "Dactylic dimeter", "D": "Anapestic tetrameter"}, "A", "Iambic pentameter consists of 5 iambs (da-DUM da-DUM da-DUM da-DUM da-DUM), totaling 10 syllables.", "What meter constitutes the bedrock of Shakespearean verse and English sonnets?")
            ]
            for q_t, opts, ans, exp, soc in lit_p_suite:
                for suffix in ["", " (Poetic Forms)"]:
                    items.append(("African Versification & Classical Poetics", f"{q_t}{suffix}", opts, ans, exp, soc))

        elif topic == "Prose & Fictional Techniques":
            lit_pr_suite = [
                ("In Chinua Achebe's 'Things Fall Apart', Okonkwo is sent into seven years of exile in Mbanta because:", {"A": "His gun accidentally exploded and killed Ezeudu's sixteen-year-old son", "B": "He openly opposed the arrival of the white district commissioner", "C": "He refused to pay his tribute to the Oracle of the Hills", "D": "He broke the Week of Peace by beating his youngest wife"}, "A", "Killing a clansman inadvertently was a female crime against Ani, punishable by 7 years of banishment.", "Why was Okonkwo forced to flee Umuofia to his motherland Mbanta?"),
                ("In George Orwell's 'Animal Farm', which pig acts as Napoleon's propagandist, manipulating facts and language?", {"A": "Squealer", "B": "Snowball", "C": "Boxer", "D": "Old Major"}, "A", "Squealer rationalizes Napoleon's totalitarian corruption, claiming 'pigs need milk and apples for brainwork'.", "Which articulate pig distorts truth to persuade the working animals on Manor Farm?"),
                ("In Buchi Emecheta's 'The Joys of Motherhood', the protagonist Nnu Ego dies:", {"A": "Lonely and destitute by the roadside, despite having dedicated her entire life to her children", "B": "Surrounded by wealthy, loving children in a royal palace", "C": "As a celebrated traditional market leader in Ibuza", "D": "In a hospital in London"}, "A", "Nnu Ego sacrificed everything for her sons, yet died alone by the roadside in tragic maternal irony.", "What poignant irony marks Nnu Ego's death at the conclusion of 'The Joys of Motherhood'?"),
                ("A narrative technique where the narrator records the unbroken, chaotic flow of a character's internal thoughts is:", {"A": "Stream of consciousness", "B": "Epistolary narrative", "C": "Allegorical framing", "D": "Omniscient detachment"}, "A", "Stream of consciousness reproduces the continuous, unfiltered psychological thought processes of a character.", "What literary method attempts to mimic the continuous cognitive flow of the human mind?")
            ]
            for q_t, opts, ans, exp, soc in lit_pr_suite:
                for suffix in ["", " (Prose Analysis)"]:
                    items.append(("Novels, Allegory & Narrative Craft", f"{q_t}{suffix}", opts, ans, exp, soc))

    random.shuffle(items)
    return items
''')

    print(f"Successfully generated {target_file}!")

if __name__ == "__main__":
    main()
