import random

def generate_english_questions(topic, count_needed=150):
    items = []

    if topic == "Concord & Grammar":
        # 1. Proximity concord with neither... nor / either... or
        prox_cases = [
            ("the principal", "the teachers", "are", "is", "was", "has been", "plural"),
            ("the captain", "the players", "were", "was", "is", "has been", "plural"),
            ("the senator", "his constituents", "are", "is", "was", "has been", "plural"),
            ("the doctor", "the nurses", "were", "was", "is", "has been", "plural"),
            ("the manager", "the accountants", "have", "has", "is having", "was having", "plural"),
            ("the students", "the lecturer", "is", "are", "were", "have been", "singular"),
            ("the soldiers", "the commander", "was", "were", "are", "have been", "singular"),
            ("the workers", "the director", "has", "have", "are having", "were having", "singular"),
            ("the prefects", "the headmistress", "is", "are", "were", "have been", "singular"),
            ("the boys", "their mother", "was", "were", "are", "have been", "singular")
        ]
        for s1, s2, cor, d1, d2, d3, s2_num in prox_cases:
            verb_type = "ready to commence the program" if cor in ["is", "are", "was", "were"] else "completed the annual evaluation"
            q_text = f"Neither {s1} nor {s2} _______ {verb_type}."
            opts = {"A": cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Rule of Proximity", q_text, opts, "A",
                f"In 'neither... nor' constructions, the verb agrees solely with the closest subject ('{s2}', which is {s2_num}).",
                f"Which subject is immediately adjacent to the verb: '{s1}' or '{s2}'?"
            ))

        # 2. Parenthetical additions: as well as, together with, accompanied by
        parenth_cases = [
            ("The President", "together with his security aides", "is", "are", "were", "have been"),
            ("The Governor", "as well as his cabinet commissioners", "has", "have", "were having", "are"),
            ("The Vice-Chancellor", "accompanied by the university deans", "was", "were", "are", "have been"),
            ("The school principal", "in conjunction with the teachers", "is", "are", "were", "have been"),
            ("The chief engineer", "along with the contractors", "has", "have", "are having", "were"),
            ("The headmaster", "no less than the students", "was", "were", "are", "have been"),
            ("The pilot", "including the entire flight crew", "is", "are", "were", "have been"),
            ("The captain", "besides his active teammates", "has", "have", "are having", "were")
        ]
        for subj, adjunct, cor, d1, d2, d3 in parenth_cases:
            q_text = f"{subj}, {adjunct}, _______ present at the national award ceremony today."
            opts = {"A": cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Parenthetical Intervening Phrases", q_text, opts, "A",
                f"Parenthetical phrases introduced by '{adjunct.split()[0]}' are quasi-prepositional modifiers. The verb agrees strictly with the initial singular subject '{subj}'.",
                f"Does the phrase '{adjunct}' alter the singular grammatical number of '{subj}'?"
            ))

        # 3. Indefinite pronouns
        indef_cases = [
            ("Each of the newly recruited police officers", "has", "have", "are having", "were"),
            ("Neither of the two disputing candidates", "was", "were", "are", "have been"),
            ("Everyone among the invited dignitaries", "is", "are", "were", "have been"),
            ("Either of the suggested alternatives", "is", "are", "were", "have been"),
            ("One of the most experienced pilots", "has", "have", "are having", "were"),
            ("Every one of the shortlisted applicants", "was", "were", "are", "have been"),
            ("Neither of the twins", "is", "are", "were", "have been"),
            ("Each and every member of the committee", "has", "have", "are having", "were")
        ]
        for subj, cor, d1, d2, d3 in indef_cases:
            q_text = f"{subj} _______ expressed profound satisfaction with the committee's decision."
            opts = {"A": cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Indefinite Pronoun Concord", q_text, opts, "A",
                f"Distributive and indefinite pronouns ('each', 'neither', 'everyone', 'either') are grammatically singular in standard English.",
                "Is the grammatical subject of the sentence singular or plural?"
            ))

        # 4. Plural nouns taking singular verbs (fields of study, diseases)
        plural_form_sing = [
            ("Mathematics", "is", "are", "were", "have been", "subject of academic study"),
            ("Economics", "is", "are", "were", "have been", "discipline of social science"),
            ("Physics", "requires", "require", "are requiring", "were requiring", "rigorous mathematical aptitude"),
            ("Linguistics", "deals", "deal", "are dealing", "were dealing", "with scientific analysis of language"),
            ("Measles", "is", "are", "were", "have been", "highly contagious viral disease"),
            ("The news from the battlefront", "is", "are", "were", "have been", "unusually encouraging"),
            ("Ten thousand naira", "is", "are", "were", "have been", "a sufficient transport stipend"),
            ("Twenty kilometres", "is", "are", "were", "have been", "a tedious distance to trek on foot")
        ]
        for noun, cor, d1, d2, d3, desc in plural_form_sing:
            q_text = f"{noun} _______ considered {desc}."
            opts = {"A": cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Nouns Plural in Form but Singular in Meaning", q_text, opts, "A",
                f"'{noun}' ends in '-s' but functions semantically as a singular uncount entity or single metric quantity, requiring a singular verb.",
                f"Is '{noun}' semantically treated as an indivisible singular concept?"
            ))

        # 5. Mandative Subjunctive
        subjunctive_verbs = ["insist", "demand", "recommend", "stipulate", "require", "suggest", "order", "decree"]
        for verb in subjunctive_verbs:
            q_text = f"The university senate {verb}s that every final-year undergraduate _______ a comprehensive drug clearance test."
            opts = {"A": "undergo", "B": "undergoes", "C": "underwent", "D": "must undergo"}
            items.append((
                "Mandative Subjunctive Mood", q_text, opts, "A",
                f"Verbs of formal command, requirement, or recommendation take the bare base infinitive (subjunctive) in the dependent 'that' clause.",
                "Why is the bare infinitive without '-s' mandated after verbs of demand or recommendation?"
            ))

        # 6. Conditionals (Third Conditional: If + had + V3 -> would have + V3)
        cond_cases = [
            ("he had studied more diligently", "he would have passed the examination with distinction", "he will have passed", "he would pass", "he had passed"),
            ("the ambulance had arrived earlier", "the patient would have survived the acute trauma", "the patient will survive", "the patient survived", "the patient would survive"),
            ("we had taken the express route", "we would have avoided the heavy traffic gridlock", "we will avoid", "we avoided", "we would avoid"),
            ("they had adhered to safety protocols", "the industrial accident would have been averted", "it will be averted", "it was averted", "it would avert")
        ]
        for if_cl, res_cl, d1, d2, d3 in cond_cases:
            q_text = f"If {if_cl}, _______."
            opts = {"A": res_cl, "B": d1, "C": d2, "D": d3}
            items.append((
                "Third Conditional Constructions", q_text, opts, "A",
                "Unfulfilled past hypothetical conditions (If + past perfect) require 'would have + past participle' in the main clause.",
                "Which modal auxiliary combination expresses an unrealized past condition?"
            ))

    elif topic == "Lexis & Structure":
        # Synonyms
        synonyms = [
            ("ephemeral", "transient / fleeting", "eternal", "massive", "ancient"),
            ("audacious", "bold / daring", "timid", "cowardly", "polite"),
            ("meticulous", "painstaking / thorough", "careless", "hasty", "sloppy"),
            ("indolent", "lazy / slothful", "energetic", "industrious", "diligent"),
            ("candid", "frank / outspoken", "deceptive", "evasive", "secretive"),
            ("pragmatic", "practical / realistic", "idealistic", "theoretical", "visionary"),
            ("ominous", "threatening / foreboding", "auspicious", "promising", "cheerful"),
            ("tenacious", "persistent / resolute", "yielding", "weak", "irresolute"),
            ("benevolent", "kind / philanthropic", "malevolent", "cruel", "stingy"),
            ("opaque", "impenetrable to light / cloudy", "transparent", "luminous", "brilliant"),
            ("austere", "severe / sternly simple", "luxurious", "indulgent", "lavish"),
            ("novice", "beginner / tyro", "expert", "veteran", "maestro"),
            ("lucid", "clear / easily understood", "obscure", "confusing", "turbid"),
            ("garrulous", "talkative / loquacious", "taciturn", "reticent", "silent"),
            ("affluent", "wealthy / prosperous", "destitute", "impoverished", "needy")
        ]
        for word, syn, ant1, ant2, ant3 in synonyms:
            q_text = f"Choose the option nearest in meaning to the capitalized word: 'The professor praised the student's {word.upper()} approach to academic research.'"
            opts = {"A": syn.split('/')[0].strip(), "B": ant1, "C": ant2, "D": ant3}
            items.append((
                "Lexical Synonyms", q_text, opts, "A",
                f"'{word}' means {syn}. Nearest in meaning is {syn.split('/')[0].strip()}.",
                f"Which word shares the closest semantic connotation with '{word}'?"
            ))
            q_text_ant = f"Choose the option most opposite in meaning to the capitalized word: 'The witness gave an unusually {word.upper()} statement to the court.'"
            opts_ant = {"A": ant1, "B": syn.split('/')[0].strip(), "C": syn.split('/')[-1].strip(), "D": "indifferent"}
            items.append((
                "Lexical Antonyms", q_text_ant, opts_ant, "A",
                f"The antonym of '{word}' ({syn}) is {ant1}.",
                f"Which word conveys the direct antonymous opposite of '{word}'?"
            ))

        # Idioms
        idioms = [
            ("burn the candle at both ends", "Exhaust oneself by working excessively hard day and night", "Save electricity", "Light candles during blackout", "Waste candles carelessly"),
            ("take it with a pinch of salt", "View a claim with skepticism and doubt its complete accuracy", "Add table salt to food", "Accept unconditionally", "Reject furiously"),
            ("bite the bullet", "Face a painful or difficult situation with courage and stoicism", "Eat dangerous metal", "Shoot a firearm", "Flee from confrontation"),
            ("barking up the wrong tree", "Pursuing a mistaken or completely erroneous line of inquiry", "Climbing tall trees", "Hunting wild animals", "Shouting at neighbors"),
            ("on the horns of a dilemma", "Trapped in a predicament with two equally unpleasant choices", "Being attacked by a bull", "Making a very easy decision", "Celebrating a victory"),
            ("turn over a new leaf", "Reform one's conduct and begin behaving in a much better way", "Read another page of a novel", "Rake dry autumn leaves", "Become an environmentalist"),
            ("spill the beans", "Divulge a confidential secret prematurely or indiscreetly", "Cook food carelessly", "Scatter seeds on farm", "Drop raw groceries"),
            ("face the music", "Accept the unpleasant consequences or criticism for one's actions", "Attend a musical concert", "Play an orchestra instrument", "Sing loudly"),
            ("cry over spilt milk", "Wasting futile time lamenting past losses that cannot be undone", "Cleaning liquid spills", "Milking dairy cattle", "Buying fresh groceries"),
            ("at the drop of a hat", "Willingly and immediately without the slightest hesitation", "Dropping headwear", "Losing one's clothes", "After long deliberation")
        ]
        for idm, meaning, d1, d2, d3 in idioms:
            q_text = f"What is the figurative idiomatic interpretation of the expression: '{idm}'?"
            opts = {"A": meaning, "B": d1, "C": d2, "D": d3}
            items.append((
                "Idiomatic Expressions & Figurative Usage", q_text, opts, "A",
                f"'{idm}' figuratively signifies: {meaning}.",
                "Avoid literal interpretations when analyzing idiomatic expressions."
            ))

        # Prepositional Collocations
        collocations = [
            ("accused", "of", "with", "for", "against", "stealing public funds"),
            ("congratulate", "on", "for", "with", "about", "his brilliant UTME score"),
            ("interested", "in", "with", "about", "at", "studying petroleum engineering"),
            ("prefer", "to", "than", "over", "instead", "tea"),
            ("comply", "with", "to", "by", "for", "statutory safety standards"),
            ("exempted", "from", "of", "against", "with", "paying the examination surcharge"),
            ("abstain", "from", "against", "of", "with", "consuming alcoholic drinks"),
            ("confided", "in", "to", "with", "on", "his closest companion"),
            ("eligible", "for", "to", "with", "about", "the undergraduate scholarship"),
            ("prone", "to", "with", "for", "against", "malarial infections in rainy season")
        ]
        for verb, prep, d1, d2, d3, context in collocations:
            q_text = f"The candidate was {verb} _______ {context}."
            opts = {"A": prep, "B": d1, "C": d2, "D": d3}
            items.append((
                "Prepositional Collocations", q_text, opts, "A",
                f"The adjective or verb '{verb}' idiomatically collocates strictly with the preposition '{prep}'.",
                f"Which preposition grammatically complements '{verb}'?"
            ))

    elif topic == "Oral Forms & Phonology":
        # 1. Silent letters
        silent_cases = [
            ("climb", "b", "m", "l", "c"),
            ("doubt", "b", "d", "u", "t"),
            ("debt", "b", "d", "e", "t"),
            ("subtle", "b", "s", "t", "l"),
            ("knight", "k", "n", "t", "i"),
            ("knuckle", "k", "n", "c", "l"),
            ("receipt", "p", "r", "e", "t"),
            ("psychology", "p", "s", "y", "l"),
            ("salmon", "l", "s", "a", "m"),
            ("listen", "t", "l", "s", "n"),
            ("castle", "t", "c", "s", "l"),
            ("sword", "w", "s", "o", "r"),
            ("sign", "g", "s", "i", "n"),
            ("foreign", "g", "f", "r", "n")
        ]
        for word, silent, d1, d2, d3 in silent_cases:
            q_text = f"Which consonant letter is phonetically silent in the pronunciation of the word '{word}'?"
            opts = {"A": silent, "B": d1, "C": d2, "D": d3}
            items.append((
                "Silent Consonant Letters", q_text, opts, "A",
                f"In the word '{word}', the letter '{silent}' is not articulated phonetically (it is silent).",
                f"Which letter is omitted from the phonetic transcription of '{word}'?"
            ))

        # 2. Vowel sounds (Same vowel sound)
        vowel_matches = [
            ("seat (/iː/)", "receive", "sit", "head", "threat"),
            ("ship (/ɪ/)", "busy", "sheep", "marine", "height"),
            ("bed (/e/)", "leopard", "meat", "break", "bead"),
            ("cat (/æ/)", "plait", "car", "cart", "father"),
            ("father (/ɑː/)", "clerk", "fat", "water", "gather"),
            ("pot (/ɒ/)", "cough", "port", "coat", "court"),
            ("caught (/ɔː/)", "law", "lot", "boat", "cot"),
            ("book (/ʊ/)", "could", "pool", "food", "blood"),
            ("moon (/uː/)", "canoe", "book", "look", "foot"),
            ("cup (/ʌ/)", "blood", "pull", "put", "bull"),
            ("bird (/ɜː/)", "journey", "beard", "peer", "bear")
        ]
        for cue, ans, d1, d2, d3 in vowel_matches:
            q_text = f"Which word contains the identical vowel sound to the one underlined in '{cue}'?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Vowel Sound Identification", q_text, opts, "A",
                f"'{cue}' and '{ans}' both share the identical phonemic vowel sound.",
                "Pronounce each word carefully and isolate the central vocalic nucleus."
            ))

        # 3. Consonants: /θ/ vs /ð/
        th_cases = [
            ("think (/θ/ voiceless dental fricative)", "bath", "then", "bathe", "clothe"),
            ("thought (/θ/ voiceless dental fricative)", "theatre", "this", "breathe", "feather"),
            ("this (/ð/ voiced dental fricative)", "breathe", "thumb", "theme", "cloth"),
            ("that (/ð/ voiced dental fricative)", "leather", "tooth", "thin", "think")
        ]
        for cue, ans, d1, d2, d3 in th_cases:
            q_text = f"Which word contains the identical dental consonant sound to the one in '{cue}'?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Dental Consonant Phonology (/θ/ vs /ð/)", q_text, opts, "A",
                f"Both '{cue}' and '{ans}' share the identical dental fricative phoneme.",
                "Determine whether vocal cords vibrate (voiced /ð/) or remain still (voiceless /θ/)."
            ))

        # 4. Stress placement
        stress_words = [
            ("phoTOgraphy (4 syllables)", "pho-TO-gra-phy (second syllable)", "PHO-to-gra-phy (first syllable)", "pho-to-GRA-phy (third syllable)", "pho-to-gra-PHY (fourth syllable)"),
            ("photoGRAPHic (4 syllables)", "pho-to-GRAPH-ic (third syllable)", "PHO-to-graph-ic (first syllable)", "pho-TO-graph-ic (second syllable)", "pho-to-graph-IC (fourth syllable)"),
            ("deMOcracy (4 syllables)", "de-MO-cra-cy (second syllable)", "DE-mo-cra-cy (first syllable)", "de-mo-CRA-cy (third syllable)", "de-mo-cra-CY (fourth syllable)"),
            ("demoCRATic (4 syllables)", "de-mo-CRAT-ic (third syllable)", "DE-mo-crat-ic (first syllable)", "de-MO-crat-ic (second syllable)", "de-mo-crat-IC (fourth syllable)"),
            ("eCOnomy (4 syllables)", "e-CO-no-my (second syllable)", "E-co-no-my (first syllable)", "e-co-NO-my (third syllable)", "e-co-no-MY (fourth syllable)"),
            ("ecoNOMic (4 syllables)", "e-co-NOM-ic (third syllable)", "E-co-nom-ic (first syllable)", "e-CO-nom-ic (second syllable)", "e-co-nom-IC (fourth syllable)")
        ]
        for word, ans, d1, d2, d3 in stress_words:
            q_text = f"On which syllable is the primary grammatical stress placed in the word '{word.split()[0]}'?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Polysyllabic Word Stress", q_text, opts, "A",
                f"Correct accentuation: {ans}.",
                "Notice stress shift caused by suffixes like -ic or -y."
            ))

    elif topic == "Comprehension & Prescribed Text":
        # Registers
        registers = [
            ("biopsy, suture, prognosis, cannula, outpatient, hematoma", "Medical & Clinical Healthcare", "Maritime Navigation", "Legal Jurisprudence", "Aviation"),
            ("affidavit, plaintiff, tort, bailiff, indictment, subpoena", "Legal & Judicial Jurisprudence", "Computer Programming", "Agriculture", "Theatrical Arts"),
            ("fuselage, altimeter, turbulence, avionics, aileron, runway", "Aviation & Aeronautical Engineering", "Banking & Finance", "Medical Science", "Mining"),
            ("collateral, debenture, insolvency, liquidity, dividend, ledger", "Banking, Finance & Commerce", "Military Warfare", "Linguistics", "Meteorology"),
            ("firmware, bandwidth, encryption, firewall, malware, cache", "Information & Communication Technology (ICT)", "Civil Law", "Culinary Arts", "Aviation"),
            ("hull, starboard, ballast, archipelago, anchor, capstan", "Maritime & Nautical Navigation", "Automobile Mechanics", "Accountancy", "Medicine"),
            ("tillage, silage, furrow, harrow, germination, mulch", "Agronomy & Agricultural Science", "Aviation", "Banking", "Law"),
            ("dramatis personae, catharsis, soliloquy, proscenium, prologue", "Drama & Theatrical Performance", "ICT", "Medicine", "Navigation")
        ]
        for term_list, reg_field, d1, d2, d3 in registers:
            q_text = f"To which specialized professional register or academic field do the vocabulary items '{term_list}' belong?"
            opts = {"A": reg_field, "B": d1, "C": d2, "D": d3}
            items.append((
                "Lexical Registers & Specialized Jargon", q_text, opts, "A",
                f"The lexical items are technical jargon characteristic of {reg_field}.",
                "Identify the common occupational or technical discipline unifying these terms."
            ))

        # Tone and mood
        tones = [
            ("The author mercilessly ridicules societal hypocrisy using biting sarcasm and caricature.", "Satirical and sardonic", "Objective and detached", "Laudatory and complimentary", "Indifferent"),
            ("The passage presents balanced statistical facts, empirical observations, and neutral logical deductions without emotional bias.", "Objective, analytical, and informative", "Emotional and sentimental", "Satirical", "Pessimistic"),
            ("The writer expresses profound grief, melancholy, and nostalgia for the vanished tranquil days of youth.", "Nostalgic, elegiac, and somber", "Humorous and jovial", "Aggressive", "Sarcastic"),
            ("The editorial bitterly denounces systemic bureaucratic corruption and calls for immediate civil revolt.", "Indignant, provocative, and revolutionary", "Placid and calm", "Humorous", "Apathetic")
        ]
        for desc, tone_ans, d1, d2, d3 in tones:
            q_text = f"Which tone or authorial attitude is displayed when {desc.lower()}?"
            opts = {"A": tone_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Comprehension: Authorial Tone & Attitude", q_text, opts, "A",
                f"The tone is accurately characterized as {tone_ans}.",
                "Infer the author's underlying emotional disposition from the vocabulary and stylistic tone."
            ))

    append_deep_english(items, topic)
    append_master_english(items, topic)
    append_final_push_english(items, topic)
    append_even_more_comprehension(items, topic)
    append_last_comprehension(items, topic)
    append_absolute_final_english(items, topic)
    return items

def append_deep_english(items, topic):
    if topic == "Concord & Grammar":
        # Inverted negative adverbs
        neg_adverbs = [
            ("Hardly", "had the bell rung when the students surged into the quadrangle", "the bell had rung", "has the bell rung", "did the bell rang"),
            ("Scarcely", "had he entered the banking hall when the alarm sounded", "he had entered", "did he entered", "has he entered"),
            ("No sooner", "had the referee blown the final whistle than the spectators invaded the pitch", "the referee had blown", "did the referee blew", "was the referee blown"),
            ("Seldom", "does one encounter such exceptional academic brilliance in a freshman", "one encounters", "one encounter", "has one encountered"),
            ("Rarely", "do politicians fulfill all their campaign promises faithfully", "politicians do fulfill", "politicians fulfills", "does politicians fulfill")
        ]
        for adv, cor_rest, d1, d2, d3 in neg_adverbs:
            q_text = f"{adv} _______."
            opts = {"A": cor_rest, "B": d1, "C": d2, "D": d3}
            items.append((
                "Negative Inversion Concord", q_text, opts, "A",
                f"Negative or limiting adverbs at the beginning of a clause ({adv}) trigger subject-auxiliary inversion: {adv} + auxiliary + subject.",
                f"Does placing '{adv}' at the start of a sentence require inverted word order?"
            ))

        # "A number of" vs "The number of"
        q_num_cases = [
            ("A number of brilliant candidates", "have", "has", "is having", "was having", "plural ('a number' = several/many)"),
            ("The number of registered UTME candidates", "has", "have", "are having", "were having", "singular ('the number' = a specific statistic)"),
            ("A majority of the board members", "were", "was", "is", "has been", "plural"),
            ("The majority in parliament", "was", "were", "are", "have been", "singular collective"),
            ("Many a diligent student", "has", "have", "are having", "were having", "singular ('many a' takes singular)")
        ]
        for subj_n, cor, d1, d2, d3, expl in q_num_cases:
            q_text = f"{subj_n} _______ passed the preliminary screening exercise."
            opts = {"A": cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Quantifier & Fractional Concord", q_text, opts, "A",
                f"Grammatical rule: {expl}.",
                "Determine whether the quantifier denotes an aggregate statistic or individual plural entities."
            ))

        # Question tags
        tag_cases = [
            ("The suspect hasn't confessed to the armed robbery", "has he?", "hasn't he?", "did he?", "didn't he?"),
            ("The candidates wrote the examination yesterday", "didn't they?", "did they?", "haven't they?", "weren't they?"),
            ("Let us quickly review our revision notes", "shall we?", "will we?", "can we?", "do we?"),
            ("Close the laboratory windows immediately", "will you?", "shall you?", "can't you?", "do you?"),
            ("Nobody attended the evening lecture", "did they?", "didn't they?", "did he?", "didn't he?"),
            ("You used to live in Kaduna", "didn't you?", "usedn't you?", "did you?", "haven't you?"),
            ("I am still your favorite instructor", "aren't I?", "amn't I?", "am I?", "isn't it?")
        ]
        for stem_s, tag_cor, d1, d2, d3 in tag_cases:
            q_text = f"Choose the correct question tag: '{stem_s}, _______?'"
            opts = {"A": tag_cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Tag Questions", q_text, opts, "A",
                f"Negative statement requires positive tag; positive statement requires negative tag. Indefinite pronouns like 'nobody' take 'they'.",
                "Reverse the polarity and match the auxiliary verb and pronoun."
            ))

    elif topic == "Lexis & Structure":
        # Additional Synonyms & Antonyms
        lex_pairs = [
            ("cacophony", "harsh discordance of sound", "euphony / melodious harmony", "quietness", "music"),
            ("gregarious", "sociable / fond of company", "solitary / reclusive", "timid", "hostile"),
            ("malleable", "pliable / easily shaped", "rigid / inflexible", "brittle", "hard"),
            ("lethargic", "sluggish / languid", "energetic / dynamic", "sleepy", "active"),
            ("ostentatious", "pretentious / showy", "modest / unassuming", "wealthy", "simple"),
            ("fastidious", "meticulously demanding / finicky", "easygoing / indifferent", "sloppy", "careful"),
            ("sporadic", "intermittent / occurring irregularly", "incessant / continuous", "isolated", "rare"),
            ("altruistic", "unselfishly generous", "selfish / egoistic", "rich", "kind"),
            ("capricious", "fickle / whimsical / erratic", "steadfast / reliable", "predictable", "stubborn"),
            ("ubiquitous", "omnipresent / everywhere", "rare / scarce", "visible", "distant"),
            ("taciturn", "habitually silent / reticent", "voluble / loquacious", "shy", "calm"),
            ("voracious", "insatiable / ravenous", "moderate / abstemious", "hungry", "wild"),
            ("zenith", "highest peak / acme", "nadir / lowest depth", "horizon", "summit"),
            ("alleviate", "mitigate / ease / relieve", "aggravate / exacerbate", "cure", "lessen"),
            ("disparage", "belittle / deprecate", "laud / extol / praise", "criticize", "ignore")
        ]
        for w, syn, ant, d2, d3 in lex_pairs:
            q_text = f"Select the word nearest in meaning to the capitalized word: 'The minister was criticized for his {w.upper()} demeanor.'"
            opts = {"A": syn.split('/')[0].strip(), "B": ant.split('/')[0].strip(), "C": d2, "D": d3}
            items.append((
                "Advanced Lexical Synonyms", q_text, opts, "A",
                f"'{w}' means {syn}. Nearest in meaning is {syn.split('/')[0].strip()}.",
                f"Identify the synonym for '{w}'."
            ))
            q_text_a = f"Select the word most opposite in meaning to the capitalized word: 'The critic described the performance as {w.upper()}'."
            opts_a = {"A": ant.split('/')[0].strip(), "B": syn.split('/')[0].strip(), "C": d2, "D": d3}
            items.append((
                "Advanced Lexical Antonyms", q_text_a, opts_a, "A",
                f"The antonym of '{w}' is {ant.split('/')[0].strip()}.",
                f"Identify the word directly opposite in meaning to '{w}'."
            ))

        # Phrasal verbs
        phrasals = [
            ("call off", "cancel an arranged event", "postpone to later date", "terminate by violence", "commence early"),
            ("put off", "postpone / delay to a future date", "extinguish a light", "cancel permanently", "insult someone"),
            ("look forward to", "anticipate with eagerness and pleasure", "look backward with regret", "dread with terror", "overlook a mistake"),
            ("put up with", "tolerate or endure an unpleasant situation", "erect a tent", "provide accommodation", "refuse angrily"),
            ("come across", "discover or find by chance without searching", "cross a wide street", "confront an enemy", "lose completely"),
            ("break down", "collapse mechanically or emotionally", "smash a door", "divide into small units", "cease speaking"),
            ("turn down", "reject or decline an offer/application", "lower the volume", "flip over a page", "destroy by fire")
        ]
        for pv, mean, d1, d2, d3 in phrasals:
            q_text = f"What is the meaning of the phrasal verb '{pv}' in standard English usage?"
            opts = {"A": mean, "B": d1, "C": d2, "D": d3}
            items.append((
                "Phrasal Verbs & Idiomatic Particle Usage", q_text, opts, "A",
                f"'{pv}' means {mean}.",
                f"Understand the non-literal idiomatic meaning of the particle verb '{pv}'."
            ))

    elif topic == "Oral Forms & Phonology":
        # Emphatic stress (capitalized word answers the question)
        stress_scenarios = [
            ("JOHN borrowed the red bicycle yesterday.", "Who borrowed the red bicycle yesterday?", "Did John buy the red bicycle yesterday?", "Did John borrow the blue bicycle yesterday?", "Did John borrow the red car yesterday?"),
            ("John BORROWED the red bicycle yesterday.", "Did John steal or buy the red bicycle yesterday?", "Who borrowed the red bicycle yesterday?", "Did John borrow the blue bicycle?", "When did John borrow the bicycle?"),
            ("John borrowed the RED bicycle yesterday.", "Did John borrow the green or blue bicycle yesterday?", "Who borrowed the bicycle?", "Did John sell the red bicycle?", "Where did John borrow the bicycle?"),
            ("John borrowed the red BICYCLE yesterday.", "Did John borrow the red motorcycle yesterday?", "Who borrowed the red bicycle?", "Did John borrow the blue bicycle?", "When did John borrow it?"),
            ("John borrowed the red bicycle YESTERDAY.", "Did John borrow the red bicycle last week?", "Who borrowed the red bicycle?", "Did John buy the red bicycle yesterday?", "Did John borrow a red car?")
        ]
        for sent, correct_q, d1, d2, d3 in stress_scenarios:
            q_text = f"In the sentence '{sent}', the capitalized word receives emphatic stress. Which question does this sentence appropriately answer?"
            opts = {"A": correct_q, "B": d1, "C": d2, "D": d3}
            items.append((
                "Emphatic Stress & Contrastive Meaning", q_text, opts, "A",
                "Emphatic stress highlights the specific piece of new or contrastive information that resolves the speaker's question.",
                "Identify which question is directly refuted or answered by the stressed word."
            ))

        # Rhyme patterns
        rhyme_cases = [
            ("seize", "freeze", "size", "cease", "says"),
            ("plough", "cow", "rough", "though", "tough"),
            ("through", "blew", "rough", "bough", "though"),
            ("daughter", "water", "laughter", "after", "slaughtered"),
            ("great", "bait", "greet", "threat", "seat"),
            ("quay", "key", "day", "say", "clay"),
            ("suite", "sweet", "suit", "shoot", "sweat")
        ]
        for cue_r, ans_r, d1, d2, d3 in rhyme_cases:
            q_text = f"Which word rhymes perfectly with '{cue_r}'?"
            opts = {"A": ans_r, "B": d1, "C": d2, "D": d3}
            items.append((
                "Rhyme Scheme & Phonemic Termination", q_text, opts, "A",
                f"'{cue_r}' and '{ans_r}' possess identical nucleus vowel and coda consonant sounds.",
                "Match the final sound pattern regardless of deceptive spelling differences."
            ))

    elif topic == "Comprehension & Prescribed Text":
        # Mini-passages with analytical questions
        passages_data = [
            ("Passage on Artificial Intelligence",
             "Artificial intelligence has permeated virtually every sphere of contemporary human existence, from automated algorithmic trading to precision medical diagnostics. However, ethicists warn that excessive reliance on autonomous cognitive architectures risks eroding fundamental human cognitive agency and critical thinking abilities.",
             [("What is the central thematic thesis of the passage?", "AI offers profound technological benefits but poses serious risks to human cognitive autonomy", "AI has completely failed in medical diagnostics", "Human beings should ban all computer algorithms", "Trading is the only sector transformed by AI"),
              ("The word 'eroding' as used in the passage nearest means:", "gradually diminishing and undermining", "violently destroying with explosives", "polishing to a shine", "speeding up dramatically"),
              ("The tone of the passage can best be described as:", "balanced, cautionary, and contemplative", "wildly euphoric and excited", "aggressively dismissive", "humorous and mocking")]),

            ("Passage on Climate Change in the Sahel",
             "The relentless southern encroachment of the Sahara desert across the Sahelian belt of West Africa has severely destabilized pastoral ecosystems. Transhumant Fulani pastoralists are pushed ever deeper into agricultural guinea savannas, precipitating severe farmer-herder conflicts over increasingly scarce freshwater aquifers and arable grazing corridors.",
             [("What is the primary ecological driver of farmer-herder conflicts according to the passage?", "Resource scarcity induced by environmental desertification", "Religious differences between ethnic communities", "Sudden industrialization of rural farmland", "Excessive rainfall and flooding in the Sahel"),
              ("The word 'precipitating' as used in the context means:", "triggering or bringing about prematurely", "raining heavily from clouds", "preventing peacefully", "cooling down disputes"),
              ("What solution is indirectly implied to alleviate the crisis?", "Restoration of degraded pasturelands and sustainable water management", "Complete eviction of all pastoralists", "Banning agriculture in the savannas", "Drying up the aquifers")]),

            ("Passage on Examination Malpractice",
             "The pernicious epidemic of examination malpractice in West Africa is not merely an academic misdemeanor; it is a structural cancer that corrodes the integrity of national human capital. When unearned credentials supersede verifiable competence, bridges collapse, misdiagnoses multiply in hospitals, and public institutions degenerate into incompetent bureaucracies.",
             [("According to the passage, what is the ultimate societal consequence of unearned academic credentials?", "Systemic institutional incompetence and catastrophic professional failure", "Rapid industrial economic growth", "Cheaper university tuition fees", "Higher employment rates for youths"),
              ("The author's tone in this excerpt is emphatically:", "grave, indignant, and warning", "candidly lighthearted and humorous", "ambivalent and unconcerned", "nostalgic and reminiscent"),
              ("The figure of speech in 'structural cancer that corrodes' is:", "metaphor", "simile", "personification", "hyperbole")]),

            ("Passage on Brain Drain (Japa Syndrome)",
             "The mass emigration of skilled medical professionals from developing countries to the Global North has reached unprecedented proportions. While remittances from the diaspora provide short-term foreign exchange buffers, the catastrophic hemorrhaging of surgical, nursing, and academic talent cripples primary healthcare delivery at the grassroots.",
             [("What paradoxical dichotomy does the author highlight regarding brain drain?", "Remittances provide temporary financial relief while the loss of skills cripples local healthcare", "Doctors earn less abroad than in their home countries", "Emigration completely solves local unemployment", "The Global North has no need for healthcare workers"),
              ("The term 'hemorrhaging' is used figuratively in the passage to convey:", "massive, rapid, and debilitating loss of essential human talent", "severe physical bleeding of patients", "excessive financial taxation by government", "violent military conflict"),
              ("Which title best encapsulates the substance of the passage?", "The Hidden Toll of Skilled Professional Migration", "The Glory of Foreign Remittances", "Healthcare in the Global North", "Why Doctors Refuse to Travel")])
        ]
        for title, p_text, q_list in passages_data:
            for p_q, cor_ans, d1, d2, d3 in q_list:
                q_full = f"Read the following excerpt:\n\"{p_text}\"\n\nQuestion: {p_q}"
                opts = {"A": cor_ans, "B": d1, "C": d2, "D": d3}
                items.append((
                    "Reading Comprehension & Critical Analysis", q_full, opts, "A",
                    f"Correct comprehension interpretation: {cor_ans}.",
                    "Analyze the text contextually to identify the main idea, vocabulary in context, or authorial tone."
                ))

def append_master_english(items, topic):
    if topic == "Oral Forms & Phonology":
        # More silent letters
        more_silent = [
            ("plumber", "b", "m", "l", "p"),
            ("tomb", "b", "t", "o", "m"),
            ("womb", "b", "w", "o", "m"),
            ("crumb", "b", "c", "r", "m"),
            ("island", "s", "i", "l", "n"),
            ("debris", "s", "d", "b", "r"),
            ("rendezvous", "z", "r", "n", "v"),
            ("depot", "t", "d", "e", "p"),
            ("mortgage", "t", "m", "r", "g"),
            ("hasten", "t", "h", "s", "n"),
            ("soften", "t", "s", "f", "n"),
            ("fasten", "t", "f", "s", "n"),
            ("indict", "c", "i", "n", "d"),
            ("chassis", "s", "c", "h", "a"),
            ("pneumonia", "p", "n", "e", "m"),
            ("psalm", "p", "s", "a", "l"),
            ("aisle", "s", "a", "i", "l"),
            ("gnat", "g", "n", "a", "t"),
            ("gnaw", "g", "n", "a", "w"),
            ("corps", "p", "c", "o", "r")
        ]
        for w_s, sil_l, d1, d2, d3 in more_silent:
            q_text = f"Which letter is phonetically unpronounced (silent) in the word '{w_s}'?"
            opts = {"A": sil_l, "B": d1, "C": d2, "D": d3}
            items.append((
                "Silent Consonants in English", q_text, opts, "A",
                f"In the word '{w_s}', the letter '{sil_l}' is phonetically silent.",
                f"Identify the unarticulated silent grapheme in '{w_s}'."
            ))

        # Consonant sounds contrast
        sound_contrasts = [
            ("church (/tʃ/ voiceless palato-alveolar affricate)", "nature", "machine", "chef", "chasm"),
            ("measure (/ʒ/ voiced palato-alveolar fricative)", "pleasure", "pressure", "mission", "nation"),
            ("mission (/ʃ/ voiceless palato-alveolar fricative)", "ocean", "measure", "vision", "decision"),
            ("judge (/dʒ/ voiced palato-alveolar affricate)", "soldier", "garage", "pleasure", "leisure"),
            ("cats (/s/ voiceless alveolar fricative ending)", "books", "dogs", "boys", "girls"),
            ("dogs (/z/ voiced alveolar fricative ending)", "cabs", "cats", "caps", "cliffs"),
            ("laugh (/f/ voiceless labiodental fricative)", "rough", "bough", "dough", "through"),
            ("chemistry (/k/ voiceless velar plosive)", "ache", "church", "charity", "chief"),
            ("chaos (/k/ voiceless velar plosive)", "choir", "champion", "chant", "chin"),
            ("genre (/ʒ/ voiced palato-alveolar fricative)", "beige", "giant", "general", "journey")
        ]
        for cue_snd, ans_snd, d1, d2, d3 in sound_contrasts:
            q_text = f"Which of the following words contains the identical consonant sound to the one in '{cue_snd}'?"
            opts = {"A": ans_snd, "B": d1, "C": d2, "D": d3}
            items.append((
                "Consonant Phoneme Contrast", q_text, opts, "A",
                f"Both '{cue_snd.split()[0]}' and '{ans_snd}' share the identical consonant phoneme.",
                "Pronounce the targeted sound carefully to verify place and manner of articulation."
            ))

        # Diphthongs
        diphthongs = [
            ("coin (/ɔɪ/)", "boy", "cone", "corn", "crow"),
            ("loud (/aʊ/)", "cow", "load", "lord", "loop"),
            ("cake (/eɪ/)", "break", "cat", "caught", "call"),
            ("bite (/aɪ/)", "height", "bit", "beat", "bet"),
            ("boat (/əʊ/)", "soul", "bought", "boot", "ball"),
            ("near (/ɪə/)", "deer", "dare", "door", "dark"),
            ("hair (/eə/)", "pear", "peer", "purr", "part")
        ]
        for cue_d, ans_d, d1, d2, d3 in diphthongs:
            q_text = f"Which word contains the identical diphthong sound to '{cue_d}'?"
            opts = {"A": ans_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Diphthong Vowel Glides", q_text, opts, "A",
                f"'{cue_d.split()[0]}' and '{ans_d}' both feature the same gliding diphthong sound.",
                "Listen to the two-target vocalic glide within the syllable nucleus."
            ))

    elif topic == "Comprehension & Prescribed Text":
        # Prescribed prose and life lessons
        prose_themes = [
            ("Salma's initial moral arrogance and subsequent academic tribulation in university", "The deceptive illusions of campus peer pressure and the high cost of examination malpractice", "The glory of unlimited hedonistic freedom", "The virtues of academic laziness", "Why students should avoid studying"),
            ("The role of Ummi (the narrator mother) in instilling ethical and cultural values", "The foundational indispensability of maternal moral guidance and open parent-child communication", "The redundancy of parental advice", "The importance of ignoring tradition", "The superiority of western culture"),
            ("The encounter with Habib and the dynamics of predatory transactional relationships", "The grave dangers of young undergraduates trading dignity for superficial material luxury", "The wisdom of seeking wealthy benefactors", "The inevitability of financial corruption", "The necessity of materialism"),
            ("The legal ordeal of Omar and the resolution of the car theft allegation", "The triumph of truth, lawful due process, and integrity over deceptive circumstantial evidence", "The superiority of jungle justice", "The uselessness of police verification", "The certainty of false imprisonment"),
            ("The phenomenon of cybercrime (Yahoo-Yahoo) and youth get-rich-quick syndrome", "The moral degradation of productive work ethic and the inevitable legal and psychological catastrophe of fraudulent greed", "The brilliance of innovative digital theft", "The nobility of defrauding foreigners", "A valid shortcut to national development"),
            ("The dilemma of secret cultism on tertiary education campuses", "Destructive violent syndicates that prey on youth vulnerability and truncate promising academic futures", "Legitimate student welfare unions", "Harmless fraternal brotherhoods", "Noble cultural dance troupes"),
            ("The thematic significance of female education in Northern Nigeria", "Empowering the girl-child through education is the most potent catalyst for breaking intergenerational poverty and advancing societal progress", "Female education is unnecessary", "Boys alone should attend university", "Educated women destabilize families"),
            ("The role of institutional transparency in university administration", "Fairness, merit-based grading, and uncompromising exam ethics sustain academic prestige and credibility", "Bribery ensures smooth administration", "Favoritism fosters ethnic solidarity", "Exam leakages should be tolerated")
        ]
        for event_t, theme_ans, d1, d2, d3 in prose_themes:
            q_text = f"In prescribed JAMB UTME prose literature, what central moral lesson or thematic insight is conveyed through {event_t.lower()}?"
            opts = {"A": theme_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Prescribed Text Thematic Analysis", q_text, opts, "A",
                f"{event_t}: {theme_ans}.",
                "Examine how narrative character development illustrates core ethical and societal themes."
            ))

        # Technical registers across fields
        more_registers = [
            ("crop rotation, harrowing, silviculture, pest infestation, organic fertilizer", "Agricultural Science & Agronomy", "Aviation", "Maritime Navigation", "Linguistics"),
            ("statutory declaration, jurat, injunction, tortfeasor, habeas corpus", "Judicial & Legal Jurisprudence", "Medicine", "Banking", "ICT"),
            ("overdraft, liquidity ratio, credit creation, collateral, fiduciary issue", "Monetary Banking & Macro-Finance", "Theatrical Arts", "Aeronautics", "Mining"),
            ("cockpit, cruising altitude, stall speed, landing gear, flight manifest", "Civil Aviation & Piloting", "Agricultural Science", "Civil Law", "Pedagogy"),
            ("intravenous infusion, sterile scalpel, laparotomy, anesthetic, defibrillator", "Surgery & Clinical Medicine", "Banking", "Navigation", "Accountancy"),
            ("broadsheet, editorial, scoop, byline, yellow journalism, syndicated columnist", "Journalism & Mass Media", "Agronomy", "Civil Aviation", "Military"),
            ("ballistic missile, reconnaissance, platoon, court-martial, tactical retreat", "Military Science & Defense", "Medicine", "Banking", "Pedagogy"),
            ("curriculum, pedagogy, formative assessment, syllabus, remedial instruction", "Education & Pedagogical Science", "Aviation", "Mining", "Maritime"),
            ("subsea pipeline, crude assay, offshore drilling rig, petrodollars, seismic survey", "Petroleum & Extraction Engineering", "Education", "Mass Media", "Law"),
            ("proscenium arch, soliloquy, cue, mime, dramatic irony, footlights", "Drama & Theatrical Performance", "Aviation", "Banking", "Agronomy")
        ]
        for words, field, d1, d2, d3 in more_registers:
            q_text = f"The set of specialized terms '{words}' belongs to the professional register of:"
            opts = {"A": field, "B": d1, "C": d2, "D": d3}
            items.append((
                "Specialized Occupational Registers", q_text, opts, "A",
                f"These technical terms are standard lexical items in {field}.",
                f"Identify the professional domain denoted by '{words.split(',')[0]}'."
            ))

        # Literary devices in comprehension
        lit_devices_comp = [
            ("'The government announced today that the Crown will address parliament tomorrow.'", "Metonymy (the Crown represents the reigning monarch or royal institution)", "Synecdoche", "Personification", "Hyperbole"),
            ("'All hands on deck to ensure we complete the mega bridge on schedule.'", "Synecdoche (hands represent the complete physical laborers)", "Metonymy", "Irony", "Euphemism"),
            ("'The wealthy industrialist was not the most generous philanthropist in town.'", "Litotes (understatement using double negative to express a strong affirmative)", "Hyperbole", "Oxymoron", "Apostrophe"),
            ("'The deafening silence in the abandoned hospital room spoke volumes.'", "Oxymoron (juxtaposition of contradictory words 'deafening silence')", "Metaphor", "Simile", "Synecdoche"),
            ("'He passed away peacefully in his sleep after a protracted illness.'", "Euphemism (mild or indirect expression substituted for the harsh word 'died')", "Hyperbole", "Paradox", "Irony")
        ]
        for sentence_ex, lit_ans, d1, d2, d3 in lit_devices_comp:
            q_text = f"Which figure of speech is employed in the underlined statement: {sentence_ex}?"
            opts = {"A": lit_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Figures of Speech in Textual Context", q_text, opts, "A",
                f"Analysis: {lit_ans}.",
                "Identify whether the literary device involves substitution, understatement, contradiction, or figurative association."
            ))

def append_final_push_english(items, topic):
    if topic == "Oral Forms & Phonology":
        homophones = [
            ("stationery (writing materials)", "stationary (not moving)", "station", "stationing", "stationer"),
            ("principal (head of a school / chief sum)", "principle (fundamental truth or moral rule)", "principality", "principled", "prince"),
            ("complement (something that completes or enhances)", "compliment (expression of praise or admiration)", "compliance", "complex", "complicity"),
            ("altar (place of sacrifice or worship)", "alter (to modify or change)", "alteration", "alternate", "altitude"),
            ("canvas (heavy coarse cloth for tents/paintings)", "canvass (to solicit votes or opinions)", "canopy", "canteen", "candid")
        ]
        for w1, hom, d1, d2, d3 in homophones:
            q_text = f"Which word is a perfect homophone (pronounced identically) of '{w1.split()[0]}'?"
            opts = {"A": hom.split()[0], "B": d1, "C": d2, "D": d3}
            items.append((
                "Homophones & Phonemic Equivalence", q_text, opts, "A",
                f"'{w1.split()[0]}' and '{hom.split()[0]}' are homophones: identical in phonetic pronunciation despite distinct spellings and meanings.",
                "Homophones share exact acoustic pronunciation but differ in orthography and semantics."
            ))

    elif topic == "Comprehension & Prescribed Text":
        more_passages = [
            ("Passage on Financial Literacy",
             "A distressing paradox of modern education is that students can solve differential calculus and memorize chemical equations without knowing how compound interest works or how inflation depreciates idle cash. True financial literacy is an existential survival skill, not an elective luxury.",
             [("What is the primary argument advanced by the author?", "Practical financial literacy is indispensable and should not be ignored by modern education", "Calculus and chemistry are completely useless", "Students should not attend secondary school", "Inflation is a myth created by banks"),
              ("The word 'depreciates' in the passage means:", "reduces the purchasing power or real value of", "increases dramatically", "saves securely", "invests in stock shares"),
              ("The author's tone can best be described as:", "pragmatic, critical, and persuasive", "fanciful and humorous", "indifferent", "cynical")]),

            ("Passage on Social Media and Reading Culture",
             "The relentless dopamine-driven notification culture of contemporary smartphones has fragmented the modern human attention span. The capacity for sustained, immersive reading of deep literature is being rapidly displaced by superficial skimming of algorithmic feeds.",
             [("According to the passage, what is the grave cultural consequence of smartphone notification addiction?", "The severe erosion of sustained attention and deep literary engagement", "Cheaper book publishing costs", "Better spelling among students", "Faster reading of long novels"),
              ("The word 'fragmented' as used in this context conveys:", "broken into disconnected, short-lived intervals", "multiplied into many copies", "sharpened to perfection", "translated into many languages"),
              ("What is the central contrast in the passage?", "Deep immersive reading versus superficial algorithmic skimming", "Android versus iPhone users", "Morning versus night study", "Science versus arts")]),

            ("Passage on Traditional Medicine",
             "For centuries before the advent of synthetic pharmacology, indigenous African herbalists utilized phytochemical bark and root decoctions to treat ailments ranging from malaria to microbial dysentery. While modern medicine often disparages these practices, scientific bioprospecting has confirmed that many traditional remedies contain potent therapeutic molecules.",
             [("What balanced perspective on traditional African medicine does the author maintain?", "Traditional herbal remedies often contain valid therapeutic chemical agents that warrant scientific validation", "Traditional medicine should completely replace modern hospitals", "Herbal remedies have zero medicinal value", "Synthetic drugs were invented in Africa"),
              ("The word 'disparages' in the passage nearest means:", "belittles, discredits, or looks down upon", "heavily invests in", "scientifically tests", "adopts enthusiastically"),
              ("The passage suggests that the ideal relationship between traditional and modern medicine is:", "collaborative bioprospecting and scientific integration", "complete mutual warfare", "abandoning all synthetic drugs", "criminalizing herbalism")]),

            ("Passage on Renewable Energy in Nigeria",
             "Nigeria's chronic electrical power deficit—hovering around 4,000 megawatts for a population exceeding 200 million—paralyzes industrial productivity and forces businesses to expend trillions of naira on diesel generators. Paradoxically, the country possesses immense untapped solar insolation in the North and vast hydropower corridors across its river basins.",
             [("What central irony or paradox does the author highlight?", "Nigeria suffers crippling electricity deficits despite possessing enormous untapped solar and hydro energy resources", "Diesel generators are cheaper than hydro power", "Nigeria's population is too small for modern grids", "Solar power does not work in Northern Nigeria"),
              ("The word 'deficit' as used in the passage denotes:", "a severe shortfall or deficiency below requirement", "an immense surplus", "a balanced equilibrium", "a temporary shutdown"),
              ("The primary economic effect of erratic power mentioned is:", "imposing massive financial costs on businesses running diesel generators", "eliminating public debt", "attracting foreign factories", "stopping river currents")]),

            ("Passage on Achebe's Literary Legacy",
             "When Chinua Achebe published 'Things Fall Apart' in 1958, he dismantled the patronizing colonial narrative that depicted Africa as a dark, cultureless void awaiting European illumination. Through rich Igbo proverbs, complex societal jurisprudence, and tragic characterization, he demonstrated that African societies possessed sophisticated civilizations long before the colonial encounter.",
             [("What revolutionary contribution did Achebe's seminal novel make to global literature?", "It restored authentic African cultural agency and dismantled racist colonial myths", "It proved that English should never be written in Africa", "It celebrated the total perfection of British colonial rule", "It was the first book ever published in Africa"),
              ("The word 'patronizing' in the excerpt nearest means:", "condescending, superior, and demeaning", "financially supportive", "deeply respectful", "scientifically rigorous"),
              ("Why did Achebe integrate Igbo proverbs into the English narrative?", "To capture the authentic philosophical depth and oral dignity of his indigenous culture", "Because he could not speak standard English", "To confuse European readers", "To hide secrets from the colonial police")])
        ]
        for title, p_text, q_list in more_passages:
            for p_q, cor_ans, d1, d2, d3 in q_list:
                q_full = f"Read the excerpt below:\n\"{p_text}\"\n\nQuestion: {p_q}"
                opts = {"A": cor_ans, "B": d1, "C": d2, "D": d3}
                items.append((
                    "Reading Comprehension & Critical Analysis", q_full, opts, "A",
                    f"Analysis: {cor_ans}.",
                    "Analyze the text contextually to evaluate the author's argument and vocabulary in context."
                ))

def append_even_more_comprehension(items, topic):
    if topic == "Comprehension & Prescribed Text":
        more_p = [
            ("Passage on Youth Unemployment and Agribusiness",
             "While millions of educated Nigerian graduates roam urban streets seeking scarce white-collar civil service jobs, vast tracts of fertile arable land lie fallow in rural communities. Modern agribusiness, transformed by drone surveying, mechanized cultivation, and digital supply chains, represents the most viable pathway to youth employment.",
             [("What unexploited economic opportunity does the passage highlight?", "Transitioning unemployed youth into modern technology-driven agribusiness", "Increasing government administrative secretarial jobs", "Banning youth from migrating to cities", "Importing all staple foods from abroad"),
              ("The word 'fallow' in this context means:", "uncultivated, unploughed, and left idle", "heavily flooded", "polluted with chemicals", "covered in concrete"),
              ("What modern technology is mentioned as revolutionizing agriculture?", "Drone surveying and digital supply chains", "Hand hoes only", "Wooden carts", "Steam engines")]),

            ("Passage on Cybersecurity and Digital Identity",
             "In an increasingly interconnected digital world, personal data is the new oil. Financial institutions and e-commerce platforms handle massive streams of customer identity records daily. However, weak password hygiene, credential stuffing, and phishing vectors routinely compromise national databases.",
             [("What metaphor does the author use to describe personal data?", "The new oil (a highly valuable and contested economic asset)", "A useless burden", "A free commodity", "A dangerous weapon"),
              ("What is identified as a primary vulnerability in digital security?", "Weak password hygiene, phishing, and credential stuffing", "Too much internet bandwidth", "High cost of computers", "Lack of social media"),
              ("The tone of the author is predominantly:", "informative, analytical, and alert", "frivolous and playful", "despairing", "poetic")]),

            ("Passage on The Scramble for Africa",
             "The 1884-1885 Berlin Conference partitioned the African continent among European imperial powers with arbitrary geometric borders drawn in Berlin parlors. These artificial frontiers bifurcated homogeneous ethnic groups and lumped historical adversaries together, leaving a legacy of post-colonial border disputes.",
             [("According to the passage, why are post-colonial African borders problematic?", "They are artificial geometric lines that divided homogeneous nations and joined rival groups", "They were drawn by African kings", "They follow natural mountain ranges perfectly", "They prevented European trade"),
              ("The word 'bifurcated' in the text means:", "divided or split into two branches or parts", "unified peacefully", "relocated to Europe", "photographed from above"),
              ("Where was the historic partition of Africa negotiated?", "In Berlin, Germany (1884-1885)", "In London, England", "In Paris, France", "In Lagos, Nigeria")]),

            ("Passage on Mental Health Stigma",
             "In many traditional African societies, clinical depression, bipolar disorder, and schizophrenia are frequently misattributed to spiritual witchcraft or demonic possession. This pervasive metaphysical superstition delays evidence-based psychiatric intervention and subjects vulnerable individuals to brutal exorcisms in prayer houses.",
             [("What tragic social consequence arises from superstitious views of mental illness?", "Vulnerable individuals are denied psychiatric care and subjected to harmful prayer camp abuse", "Mental illness is cured immediately", "Families celebrate patients with lavish gifts", "Traditional herbs eradicate schizophrenia"),
              ("The word 'pervasive' in this excerpt means:", "widespread, prevalent, and deeply entrenched", "extremely rare", "beneficial to health", "newly discovered"),
              ("What does the author advocate as the proper response to mental illness?", "Evidence-based psychiatric clinical intervention", "Stricter witchcraft laws", "Ignoring the symptoms", "Total social isolation")])
        ]
        for title, p_text, q_list in more_p:
            for p_q, cor_ans, d1, d2, d3 in q_list:
                q_full = f"Read the excerpt below:\n\"{p_text}\"\n\nQuestion: {p_q}"
                opts = {"A": cor_ans, "B": d1, "C": d2, "D": d3}
                items.append((
                    "Reading Comprehension & Critical Analysis", q_full, opts, "A",
                    f"Comprehension deduction: {cor_ans}.",
                    "Analyze the text contextually to evaluate the author's argument and vocabulary in context."
                ))

def append_last_comprehension(items, topic):
    if topic == "Comprehension & Prescribed Text":
        last_p = [
            ("Passage on Substance Abuse among Adolescents",
             "The alarming surge in adolescent consumption of cough syrups containing codeine, tramadol, and illicit methamphetamine in urban slums is destroying a generation. Addicted youths drop out of school, suffer irreversible cognitive neurological impairment, and frequently turn to violent street crime to finance their chemical dependency.",
             [("What is the primary danger highlighted regarding adolescent substance abuse?", "Severe neurological cognitive impairment, academic truncation, and descent into violent crime", "Increased sports performance", "Cheaper pharmaceutical manufacturing", "Better academic grades"),
              ("The word 'dependency' in the text denotes:", "an overwhelming physical and psychological addiction", "financial independence", "healthy social friendship", "medical recovery"),
              ("What holistic approach is needed to tackle the crisis?", "Stringent border control against illicit drug trafficking combined with community mental rehabilitation", "Legalizing all addictive narcotics", "Ignoring the youth", "Arresting only pharmaceutical chemists")]),

            ("Passage on Lagos Megacity Urbanization",
             "Lagos, projected to become the world's most populous megacity by the end of the century, confronts staggering infrastructural bottlenecks. Daily traffic gridlocks consume an estimated four million commuter hours, while informal settlements on the coastal lagoon lack municipal potable water and reticulated sewage disposal.",
             [("What acute challenge characterizes urbanization in Lagos according to the passage?", "Severe commuter traffic congestion and lack of basic municipal water and sanitation in slums", "Excess of empty highways", "Severe cold weather", "Total absence of economic trade"),
              ("The word 'bottlenecks' in this context signifies:", "severe points of traffic congestion and infrastructural obstruction", "glass bottles on beaches", "water storage containers", "open highway lanes"),
              ("The primary tone of the author is:", "realistic, urgent, and analytical", "whimsical and comical", "apathetic", "triumphant")]),

            ("Passage on the Power of Female Literacy",
             "Educating a girl child has an unparalleled multiplier effect on society. Literate mothers immunize their infants at significantly higher rates, space pregnancies intelligently, ensure their own daughters complete secondary school, and reinvest up to ninety percent of their entrepreneurial earnings directly into their households.",
             [("What is the 'multiplier effect' of female literacy described in the passage?", "Educated mothers dramatically improve child survival, family healthcare, and community reinvestment", "Educated women earn less than uneducated women", "It only benefits the girl herself", "It reduces economic productivity"),
              ("The word 'unparalleled' means:", "unmatched, exceptional, and without equal", "ordinary and common", "strictly parallel in geometry", "inferior in quality"),
              ("According to the passage, what percentage of earnings do literate mothers reinvest into their families?", "Up to ninety percent", "Only ten percent", "Fifty percent", "Zero percent")]),

            ("Passage on Decentralized Solar Mini-Grids",
             "For remote agrarian villages located dozens of kilometers away from the national electric transmission corridor, extending conventional high-voltage power lines is financially prohibitive. Solar photovoltaic mini-grids, backed by lithium-ion battery storage, offer an immediate, clean, and decentralized leapfrogging solution.",
             [("Why are solar mini-grids preferred for remote rural communities over the national grid?", "Extending high-voltage lines is financially prohibitive, while solar mini-grids offer instant clean local power", "National grid power is too cheap", "Villagers prefer total darkness", "Solar panels do not require sunlight"),
              ("The term 'leapfrogging' in technological development refers to:", "bypassing older, cumbersome technologies directly to modern superior innovations", "jumping physically over obstacles", "slow, gradual copying of old methods", "abandoning all technology"),
              ("What technology provides energy storage for the solar mini-grids?", "Lithium-ion battery systems", "Diesel generators only", "Open fire pits", "Wind turbines")])
        ]
        for title, p_text, q_list in last_p:
            for p_q, cor_ans, d1, d2, d3 in q_list:
                q_full = f"Read the excerpt below:\n\"{p_text}\"\n\nQuestion: {p_q}"
                opts = {"A": cor_ans, "B": d1, "C": d2, "D": d3}
                items.append((
                    "Reading Comprehension & Critical Analysis", q_full, opts, "A",
                    f"Textual deduction: {cor_ans}.",
                    "Analyze the text contextually to evaluate the author's argument and vocabulary in context."
                ))

def append_absolute_final_english(items, topic):
    if topic == "Comprehension & Prescribed Text":
        push_comp = [
            ("Passage on The Menace of Pipeline Vandalism",
             "Illicit bunkering and artisanal petroleum refining in the coastal creeks of the Niger Delta constitute a catastrophic ecological and economic hemorrhage. Toxic soot blankets Port Harcourt skies, while acid slicks eradicate marine life across thousands of hectares of ancestral mangrove.",
             [("What dual catastrophe does the passage ascribe to crude oil vandalism?", "Severe economic revenue sabotage and devastating environmental ecocide", "Cheap fuel for farmers", "Rapid economic growth", "Clean air for the city"),
              ("The word 'hemorrhage' in this context signifies:", "a massive, uncontrolled, and ruinous loss of resources", "a minor medical scratch", "a legal agreement", "an oil export boom"),
              ("What toxic consequence of artisanal refining directly affects Port Harcourt residents?", "Pervasive particulate black carbon soot polluting urban air", "Acid snow", "Severe cold weather", "Excessive ozone gas")]),

            ("Passage on Examination Ethics and Character",
             "A student who secures university admission through counterfeit examination scores has begun their professional journey on a foundation of quicksand. Character and intellectual competence cannot be forged; in the unforgiving crucible of the real world, genuine competence always distinguishes itself from fabricated credentials.",
             [("What is the central ethical moral of the passage?", "Genuine personal competence and integrity surpass any counterfeit or unearned advantage", "Cheating is acceptable if one is never caught", "University admission is all that matters in life", "Quicksand is a good construction material"),
              ("The phrase 'crucible of the real world' figuratively suggests:", "a harsh, testing environment that severely evaluates true character and ability", "a chemistry laboratory heating vessel", "a sports stadium", "a university lecture theatre"),
              ("What warning does the author issue to fraudulent students?", "Their fabricated advantages will inevitably collapse when subjected to real professional challenges", "They will become millionaires", "They will receive honorary doctorates", "They will never face problems")])
        ]
        for title, p_text, q_list in push_comp:
            for p_q, cor_ans, d1, d2, d3 in q_list:
                q_full = f"Read the excerpt below:\n\"{p_text}\"\n\nQuestion: {p_q}"
                opts = {"A": cor_ans, "B": d1, "C": d2, "D": d3}
                items.append((
                    "Reading Comprehension & Critical Analysis", q_full, opts, "A",
                    f"Textual deduction: {cor_ans}.",
                    "Analyze the text contextually to evaluate the author's argument and vocabulary in context."
                ))
