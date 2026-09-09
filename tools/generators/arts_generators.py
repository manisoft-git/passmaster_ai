import random

def generate_english_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Concord & Grammar":
            sub_type = i % 5
            if sub_type == 0:
                # Rule of proximity
                p1 = random.choice(["the headmaster", "the captain", "the commander", "the lecturer"])
                p2 = random.choice(["the students", "the soldiers", "the cadets", "the prefects"])
                q_text = f"Neither {p1} nor {p2} _______ willing to concede defeat in the inter-collegiate debate."
                opts = {"A": "were", "B": "was", "C": "is", "D": "has been"}
                items.append((
                    "Rule of Proximity", q_text, opts, "A",
                    f"In 'neither... nor' constructions, the verb agrees solely with the closest subject ('{p2}', plural).",
                    f"Which subject is physically closest to the verb: '{p1}' or '{p2}'?"
                ))
            elif sub_type == 1:
                # Intervening phrases
                p1 = random.choice(["The governor", "The general", "The president", "The principal"])
                adjunct = random.choice(["together with his aides", "as well as his commissioners", "accompanied by his entourage"])
                q_text = f"{p1}, {adjunct}, _______ scheduled to inspect the ongoing infrastructure projects today."
                opts = {"A": "is", "B": "are", "C": "were", "D": "have been"}
                items.append((
                    "Parenthetical Phrases", q_text, opts, "A",
                    f"Phrases introduced by '{adjunct.split()[0]}' are prepositional additions, not conjunctions. The subject '{p1}' is singular.",
                    f"Is '{p1}' the sole grammatical subject before the parenthetical commas?"
                ))
            elif sub_type == 2:
                # Subjunctive mood
                verb = random.choice(["demand", "recommend", "insist", "stipulate"])
                q_text = f"The university regulations {verb} that every fresh candidate _______ the physical verification exercise."
                opts = {"A": "undergo", "B": "undergoes", "C": "underwent", "D": "must undergo"}
                items.append((
                    "Mandative Subjunctive", q_text, opts, "A",
                    f"Verbs of demand/recommendation take the bare base infinitive (no '-s' or past tense) in the 'that' clause.",
                    "What form does a verb take in a subjunctive mandative clause following 'that'?"
                ))
            elif sub_type == 3:
                # Indefinite pronoun concord
                pronoun = random.choice(["Each of the suspects", "Everyone among the candidates", "Neither of the twins"])
                q_text = f"{pronoun} _______ denied any involvement in the security breach."
                opts = {"A": "has", "B": "have", "C": "are having", "D": "were"}
                items.append((
                    "Indefinite Pronouns", q_text, opts, "A",
                    f"Indefinite pronouns like 'each', 'everyone', and 'neither' take singular verbs in formal standard English.",
                    f"Is '{pronoun.split()[0]}' grammatically treated as singular or plural?"
                ))
            else:
                # Relative clause antecedent
                q_text = "She is one of those diligent medical scholars who _______ consistently published in peer-reviewed journals."
                opts = {"A": "have", "B": "has", "C": "is having", "D": "was"}
                items.append((
                    "Relative Pronoun Concord", q_text, opts, "A",
                    "In 'one of those [plural noun] who...', 'who' refers back to the plural antecedent 'scholars', requiring 'have'.",
                    "Does the relative pronoun 'who' refer to 'one' or to the plural noun 'scholars'?"
                ))

        elif topic == "Lexis & Structure":
            sub_type = i % 4
            if sub_type == 0:
                # Prepositional collocations
                collocations = [
                    ("preside", "over", "the senate committee meeting"),
                    ("take exception", "to", "the derogatory remarks"),
                    ("congratulate him", "on", "his academic promotion"),
                    ("comply", "with", "the new electoral guidelines"),
                    ("deprived", "of", "their fundamental civic rights")
                ]
                verb, prep, context = collocations[i % len(collocations)]
                q_text = f"The chairman was invited to {verb} _______ {context}."
                opts = {"A": prep, "B": "at" if prep != "at" else "in", "C": "with" if prep != "with" else "against", "D": "for"}
                items.append((
                    "Prepositional Collocations", q_text, opts, "A",
                    f"The fixed grammatical collocation in standard English is '{verb} {prep}'.",
                    f"What specific preposition is required by the verb phrase '{verb}'?"
                ))
            elif sub_type == 1:
                # Idioms
                q_text = "The manager told the new recruit to 'learn the ropes'. This idiomatic expression means to:"
                opts = {"A": "Learn how a specific job or task is organized and executed", "B": "Practice mountain climbing techniques", "C": "Tie ropes around cargo boxes", "D": "Punish subordinate workers"}
                items.append((
                    "Idiomatic Expressions", q_text, opts, "A",
                    "'Learn the ropes' is a nautical idiom meaning to acquire the basic skills and procedures necessary for a task.",
                    "What does the common idiom 'learn the ropes' mean in an office context?"
                ))
            elif sub_type == 2:
                # Antonyms in context
                q_text = "His EXORBITANT expenditure during the campaign led to severe financial insolvency. The antonym of 'exorbitant' is:"
                opts = {"A": "Moderate", "B": "Extravagant", "C": "Astronomical", "D": "Wasteful"}
                items.append((
                    "Antonyms in Context", q_text, opts, "A",
                    "'Exorbitant' means excessively high or unreasonable; its true antonym is 'moderate' or 'reasonable'.",
                    "What is the exact opposite of an excessively high or unreasonable cost?"
                ))
            else:
                # Phrasal verbs
                q_text = "Due to the relentless downpour, the tournament organizers decided to _______ the final match."
                opts = {"A": "call off (cancel)", "B": "call out", "C": "call for", "D": "call upon"}
                items.append((
                    "Phrasal Verbs", q_text, opts, "A",
                    "'Call off' means to cancel an event. 'Call out' means to summon, and 'call for' means to demand.",
                    "Which phrasal verb means to cancel a scheduled event?"
                ))

        elif topic == "Oral Forms & Phonology":
            sub_type = i % 4
            if sub_type == 0:
                # Silent letters
                words = [("subtle", "b"), ("debt", "b"), ("knight", "k"), ("pseudo", "p"), ("listen", "t")]
                w, l = words[i % len(words)]
                q_text = f"In which of the following words is the letter '{l}' completely silent in standard pronunciation?"
                opts = {"A": w.capitalize(), "B": "Robust", "C": "Public", "D": "Candid"}
                items.append((
                    "Silent Letters", q_text, opts, "A",
                    f"In standard Received Pronunciation, the letter '{l}' is unvoiced/silent in '{w}'.",
                    f"Is the '{l}' sound actually voiced when speaking the word '{w}'?"
                ))
            elif sub_type == 1:
                # Stress patterns
                q_text = "Which syllable bears the primary accentual stress in the word 'DEMOCRATIC'?"
                opts = {"A": "de-mo-CRA-tic (3rd syllable)", "B": "DE-mo-cra-tic (1st syllable)", "C": "de-MO-cra-tic (2nd syllable)", "D": "de-mo-cra-TIC (4th syllable)"}
                items.append((
                    "Syllabic Stress", q_text, opts, "A",
                    "Words ending with the suffix '-ic' place primary stress on the penultimate (second-to-last) syllable: de-mo-CRA-tic.",
                    "On which syllable do English words ending with the suffix '-ic' place primary stress?"
                ))
            elif sub_type == 2:
                # Vowel sound contrasts
                q_text = "Which of the following words contains the long vowel sound /iː/ as in 'LEAP'?"
                opts = {"A": "People", "B": "Pip", "C": "Build", "D": "Gym"}
                items.append((
                    "Vowel Contrasts", q_text, opts, "A",
                    "'People' (/ˈpiːpl/) contains the long monophthong /iː/, whereas 'pip' and 'build' have the short vowel /ɪ/.",
                    "Which word shares the long vowel sound of 'seat' or 'leap'?"
                ))
            else:
                # Consonant sound contrasts
                q_text = "Which of the following words contains the voiced dental fricative /ð/ as in 'THIS'?"
                opts = {"A": "Breathe", "B": "Breath", "C": "Bath", "D": "Thought"}
                items.append((
                    "Consonant Contrasts", q_text, opts, "A",
                    "The verb 'breathe' ends in the voiced fricative /ð/, while the noun 'breath' ends in the voiceless fricative /θ/.",
                    "Does 'breathe' have the voiced buzzing sound of 'them' or the soft sound of 'think'?"
                ))

        else: # Comprehension & Prescribed Text
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In 'The Life Changer' by Khadija Abubakar Jalli, what significant lesson does Ummi impart to her children through the story of the quiet village boy?"
                opts = {"A": "Humility, caution, and avoiding moral arrogance", "B": "That acquiring wealth is the ultimate purpose of life", "C": "That university degrees guarantee instant employment", "D": "That traditional medicine cures all illnesses"}
                items.append((
                    "The Life Changer Analysis", q_text, opts, "A",
                    "Ummi uses domestic narratives to instill moral integrity, cautionary discernment, and family values in her children.",
                    "What core moral theme does Ummi emphasize to her daughters regarding campus life?"
                ))
            elif sub_type == 1:
                q_text = "The figurative expression 'The fiery sun scorched the barren earth with wrathful vengeance' employs which literary device?"
                opts = {"A": "Personification and Hyperbole", "B": "Simile and Euphemism", "C": "Synecdoche and Irony", "D": "Onomatopoeia"}
                items.append((
                    "Literary Devices in Context", q_text, opts, "A",
                    "Attributing the human emotion of 'wrathful vengeance' to the inanimate sun is Personification, intensified by Hyperbolic exaggeration.",
                    "Is the sun capable of human vengeance, or is human intention being attributed to nature?"
                ))
            elif sub_type == 2:
                q_text = "When an author describes a character's speech as 'honey-coated venom', the device used is:"
                opts = {"A": "Oxymoron", "B": "Understatement", "C": "Apostrophe", "D": "Litotes"}
                items.append((
                    "Literary Tropes", q_text, opts, "A",
                    "Juxtaposing two mutually contradictory terms ('honey-coated' sweetness and deadly 'venom') side-by-side forms an Oxymoron.",
                    "What figure of speech places two sharply contradictory concepts right next to each other?"
                ))
            else:
                q_text = "When an author writes to expose societal corruption, greed, or political hypocrisy using wit, ridicule, and irony, the work is:"
                opts = {"A": "A Satire", "B": "An Elegy", "C": "A Romance", "D": "An Ode"}
                items.append((
                    "Literary Genres", q_text, opts, "A",
                    "Satire blends humor and sarcasm with moral critique to expose folly and inspire societal reform.",
                    "What literary mode uses irony and mockery to expose vice and hypocrisy?"
                ))

    return items

def generate_economics_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Basic Economic Principles & Methodology":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In economic analysis, the fundamental problem of scarcity arises because:"
                opts = {"A": "Human wants are virtually insatiable while productive resources are finite", "B": "Governments print insufficient currency notes", "C": "Commercial banks hoard liquid cash", "D": "Export duties restrict international trade"}
                items.append((
                    "The Problem of Scarcity", q_text, opts, "A",
                    "Scarcity is universal because limited factors of production (land, labor, capital) cannot satisfy infinite human desires.",
                    "Why can no economic system completely eliminate the challenge of scarcity?"
                ))
            elif sub_type == 1:
                q_text = "The economic reward accrued to capital as a factor of production is:"
                opts = {"A": "Interest", "B": "Profit", "C": "Rent", "D": "Wages"}
                items.append((
                    "Factors of Production", q_text, opts, "A",
                    "Land earns Rent, Labor earns Wages, Capital earns Interest, and Enterprise earns Profit.",
                    "What is the specific economic return or factor payment paid for using capital?"
                ))
            elif sub_type == 2:
                q_text = "A point located INSIDE a nation's Production Possibility Curve (PPC) signifies:"
                opts = {"A": "Underutilization, unemployment, or inefficient allocation of resources", "B": "Maximum productive efficiency", "C": "An unattainable output combination", "D": "Rapid economic growth"}
                items.append((
                    "Production Possibility Curve", q_text, opts, "A",
                    "Points inside the frontier reflect wasted capacity or idle labor; points on the curve represent full employment efficiency.",
                    "What does an economy experience when operating below its potential production boundary?"
                ))
            else:
                q_text = "According to Adam Smith, the principal economic benefit of the division of labor in manufacturing is:"
                opts = {"A": "Increased worker dexterity and substantial savings in operational time", "B": "Elimination of all capital investment", "C": "Equal wages for all categories of labor", "D": "Higher boredom among workers"}
                items.append((
                    "Division of Labor", q_text, opts, "A",
                    "Specialization enhances speed, minimizes task-switching delays, and encourages mechanization.",
                    "Why does dividing complex jobs into repetitive specialized steps expand total factory output?"
                ))

        elif topic == "Microeconomics & Price Mechanism":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "If an increase in the price of petrol from ₦600 to ₦900 leads to zero change in the quantity demanded, demand is described as:"
                opts = {"A": "Perfectely inelastic (PED = 0)", "B": "Perfectely elastic (PED = ∞)", "C": "Unitary elastic (PED = 1)", "D": "Cross elastic"}
                items.append((
                    "Price Elasticity of Demand", q_text, opts, "A",
                    "When quantity demanded remains totally unresponsive to price alterations (%ΔQ = 0), demand is perfectly inelastic.",
                    "What is the elasticity value when buyers purchase the exact same amount regardless of price hikes?"
                ))
            elif sub_type == 1:
                q_text = "An effective statutory price ceiling (maximum legal price) enacted below the free market equilibrium price creates:"
                opts = {"A": "Persistent market shortages, queuing, and black markets", "B": "An unsold surplus of commodities", "C": "Higher profits for producers", "D": "A collapse in consumer demand"}
                items.append((
                    "Price Controls", q_text, opts, "A",
                    "Capping prices below equilibrium stimulates excess quantity demanded while discouraging supplier production, creating shortages.",
                    "What happens when the government forces sellers to charge less than market clearing price?"
                ))
            elif sub_type == 2:
                q_text = "In microeconomics, Marginal Cost (MC) is mathematically defined as:"
                opts = {"A": "The addition to total cost resulting from producing one extra unit of output (ΔTC / ΔQ)", "B": "Total fixed cost divided by quantity", "C": "Average cost multiplied by price", "D": "Total revenue minus variable cost"}
                items.append((
                    "Theory of Cost", q_text, opts, "A",
                    "Marginal Cost measures the incremental cost of producing one additional unit: MC = ΔTC / ΔQ = ΔVC / ΔQ.",
                    "What is the rate of change of total cost with respect to an incremental unit of output?"
                ))
            else:
                q_text = "Which market structure is characterized by a large number of buyers and sellers, identical homogeneous products, and zero barriers to entry?"
                opts = {"A": "Perfect Competition", "B": "Pure Monopoly", "C": "Oligopoly", "D": "Monopsony"}
                items.append((
                    "Market Structures", q_text, opts, "A",
                    "Perfect competition features price-taking firms selling identical goods with unrestricted free entry and exit.",
                    "In which market structure are individual firms complete price takers with zero market power?"
                ))

        elif topic == "Macroeconomics & National Income":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "If the Marginal Propensity to Consume (MPC) in an economy is 0.8, what is the value of the Keynesian investment multiplier?"
                opts = {"A": "5.0", "B": "1.25", "C": "4.0", "D": "0.2"}
                items.append((
                    "The Multiplier Concept", q_text, opts, "A",
                    "Multiplier k = 1 / (1 - MPC) = 1 / (1 - 0.8) = 1 / 0.2 = 5.0.",
                    "What formula calculates the investment multiplier from the marginal propensity to consume?"
                ))
            elif sub_type == 1:
                q_text = "Gross Domestic Product (GDP) differs fundamentally from Gross National Product (GNP) because GDP measures output produced:"
                opts = {"A": "Within the geographic domestic borders of a country, regardless of ownership nationality", "B": "By national citizens only, abroad and at home", "C": "Excluding all government services", "D": "Net of capital depreciation"}
                items.append((
                    "National Income Concepts", q_text, opts, "A",
                    "GDP is strictly geographical (domestic territory). GNP = GDP + Net Factor Income from Abroad.",
                    "Does GDP focus on the geographic location of production or the nationality of the producer?"
                ))
            elif sub_type == 2:
                q_text = "Cost-push inflation is triggered across an economy primarily by:"
                opts = {"A": "Substantial rises in wages, energy tariffs, and imported raw material prices", "B": "Excessive growth in the consumer money supply", "C": "A sudden surplus of agricultural food items", "D": "A cut in corporate income taxes"}
                items.append((
                    "Inflation Types", q_text, opts, "A",
                    "Cost-push inflation occurs when increased per-unit production costs shift the aggregate supply curve upward and to the left.",
                    "What kind of inflation occurs when rising production input costs force producers to raise prices?"
                ))
            else:
                q_text = "To curb an economic recession and high unemployment, the government should implement:"
                opts = {"A": "Expansionary fiscal policy: increase public spending and reduce direct taxes", "B": "Contractionary monetary policy: raise interest rates", "C": "A freeze on all bank lending", "D": "Increased tariffs on capital imports"}
                items.append((
                    "Fiscal Policy", q_text, opts, "A",
                    "Expansionary fiscal stimulus boosts aggregate demand (AD = C + I + G + X - M) by injecting government procurement and lowering personal taxes.",
                    "How can the state stimulate consumer purchasing power and business investment during a slump?"
                ))

        else: # Money, Banking & Public Finance
            sub_type = i % 4
            if sub_type == 0:
                q_text = "Which function of money solves the inefficiency of the 'double coincidence of wants' in barter trade?"
                opts = {"A": "Medium of exchange", "B": "Store of value", "C": "Standard for deferred payments", "D": "Unit of account"}
                items.append((
                    "Functions of Money", q_text, opts, "A",
                    "As a universally accepted medium of exchange, money facilitates trade without requiring matching reciprocal needs.",
                    "What core function allows money to act as an intermediary in commercial transactions?"
                ))
            elif sub_type == 1:
                q_text = "When the Central Bank of Nigeria (CBN) raises the Monetary Policy Rate (MPR), its immediate intended objective is to:"
                opts = {"A": "Increase borrowing costs, reduce commercial credit, and dampen inflation", "B": "Encourage commercial banks to lend more money", "C": "Lower mortgage interest rates", "D": "Print more physical paper notes"}
                items.append((
                    "Central Banking & Monetary Tools", q_text, opts, "A",
                    "Raising the benchmark policy rate increases the cost of funds across the financial system, reigning in excess liquidity.",
                    "Why does the central bank hike benchmark interest rates when inflation is surging?"
                ))
            elif sub_type == 2:
                q_text = "A tax system in which individuals with higher incomes pay a higher percentage rate of tax is classified as a:"
                opts = {"A": "Progressive tax", "B": "Regressive tax", "C": "Proportional flat tax", "D": "Specific customs tariff"}
                items.append((
                    "Taxation Principles", q_text, opts, "A",
                    "Progressive taxation (such as PAYE income tax) scales tax liability proportionally higher as income brackets rise.",
                    "What do economists call a tax structure where wealthier citizens contribute a higher percentage?"
                ))
            else:
                q_text = "Treasury bills issued periodically by the Central Bank on behalf of the Federal Government are:"
                opts = {"A": "Short-term debt securities with maturities of less than one year", "B": "Permanent equity shares in commercial banks", "C": "Currency notes issued for agricultural grants", "D": "Foreign exchange reserves"}
                items.append((
                    "Public Debt & Money Markets", q_text, opts, "A",
                    "Treasury bills are money market discount instruments (91, 182, 364 days) utilized for short-term fiscal borrowing.",
                    "Are treasury bills short-term money market instruments or long-term equity stocks?"
                ))

    return items

def generate_government_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Elements of Government & Political Theory":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "The supreme, absolute, and uncontrollable power of a sovereign state to make and enforce laws without external dictation is:"
                opts = {"A": "Sovereignty", "B": "Legitimacy", "C": "Delegated legislation", "D": "Separation of powers"}
                items.append((
                    "Sovereignty", q_text, opts, "A",
                    "Jean Bodin defined sovereignty as the supreme legal authority of a state over its subjects, free from external control.",
                    "What political concept embodies the ultimate, supreme legal authority of an independent state?"
                ))
            elif sub_type == 1:
                q_text = "In constitutional law, the doctrine of the Rule of Law formulated by A.V. Dicey implies:"
                opts = {"A": "Supremacy of regular law, equality before the law, and protection of fundamental human rights", "B": "Absolute immunity for government officials", "C": "Supremacy of military decrees over judges", "D": "That parliament cannot be dissolved"}
                items.append((
                    "The Rule of Law", q_text, opts, "A",
                    "Dicey's triad guarantees that no citizen is above the law, arbitrary executive power is barred, and rights are defended by courts.",
                    "What are the three core pillars of A.V. Dicey's doctrine on the Rule of Law?"
                ))
            elif sub_type == 2:
                q_text = "In a parliamentary system of government (such as Britain or Nigeria's First Republic), the Executive is:"
                opts = {"A": "Drawn directly from and politically responsible to the Legislature", "B": "Completely separate and independent from parliament", "C": "Elected directly by nationwide popular vote", "D": "Headed by a military supreme commander"}
                items.append((
                    "Forms of Government", q_text, opts, "A",
                    "In the Westminster parliamentary model, cabinet ministers must be sitting members of parliament (fusion of powers).",
                    "In a Westminster cabinet system, are ministers chosen from inside the legislature?"
                ))
            else:
                q_text = "The legal principle where citizenship is acquired based on the territorial place of birth is termed:"
                opts = {"A": "Jus soli (Right of the soil)", "B": "Jus sanguinis (Right of blood)", "C": "Naturalization", "D": "Honorary conferment"}
                items.append((
                    "Citizenship", q_text, opts, "A",
                    "Jus soli assigns citizenship by birthplace; Jus sanguinis assigns it by biological parental lineage.",
                    "What Latin legal maxim describes citizenship acquired automatically by birth on a nation's soil?"
                ))

        elif topic == "Colonial Administration in Nigeria & West Africa":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "The British colonial administrative policy of Indirect Rule relied on indigenous traditional rulers primarily because:"
                opts = {"A": "The British lacked sufficient European personnel, financial funds, and language comprehension", "B": "The British wished to grant immediate self-rule to Africans", "C": "Traditional monarchs had British university law degrees", "D": "The League of Nations banned direct taxation"}
                items.append((
                    "Indirect Rule", q_text, opts, "A",
                    "Lord Lugard instituted Indirect Rule as a cheap administrative compromise due to severe manpower and budgetary shortages.",
                    "Why did Lord Lugard choose to govern Nigeria through existing traditional rulers?"
                ))
            elif sub_type == 1:
                q_text = "The imposition of British Warrant Chiefs in Eastern Nigeria provoked intense resistance and the 1929 Aba Women's Riots because:"
                opts = {"A": "Traditional Igbo society was decentralized and acephalous, lacking hereditary executive monarchs", "B": "The Warrant Chiefs were all foreign French citizens", "C": "Women demanded the return of the Royal Niger Company", "D": "The chiefs refused to collect agricultural taxes"}
                items.append((
                    "Warrant Chiefs System", q_text, opts, "A",
                    "Arbitrarily creating autocratic Warrant Chiefs violated the democratic, consensus-driven traditions of Igbo village governance.",
                    "Why was creating artificial chiefs fundamentally incompatible with traditional Igbo democracy?"
                ))
            elif sub_type == 2:
                q_text = "Under the French colonial policy of Assimilation, Africans in the Four Communes of Senegal were granted:"
                opts = {"A": "Full French citizenship, legal equality, and representation in the French National Assembly", "B": "Indentured servitude in Caribbean plantations", "C": "Immediate national sovereignty", "D": "Zero civic rights under the Indigénat code"}
                items.append((
                    "French Policy of Assimilation", q_text, opts, "A",
                    "Residents of Dakar, Gorée, Saint-Louis, and Rufisque were classified as French citizens ('citoyens') rather than colonial subjects ('sujets').",
                    "What special civic status did France bestow upon Africans living in the Four Communes?"
                ))
            else:
                q_text = "The first organized nationwide political party established in Nigeria in 1923 by Herbert Macaulay was:"
                opts = {"A": "The Nigerian National Democratic Party (NNDP)", "B": "The Action Group (AG)", "C": "The Northern People's Congress (NPC)", "D": "The National Council of Nigeria and the Cameroons (NCNC)"}
                items.append((
                    "Early Nationalist Movements", q_text, opts, "A",
                    "Macaulay founded the NNDP in 1923 to contest the newly introduced elective seats in the Lagos Legislative Council.",
                    "Which political party was founded by Herbert Macaulay following the 1922 Clifford Constitution?"
                ))

        elif topic == "Nigerian Constitutional Development":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "The landmark innovation introduced into Nigerian political governance by the Clifford Constitution of 1922 was the:"
                opts = {"A": "Elective Principle, allowing four elected Africans into the Legislative Council", "B": "Creation of regional houses of assembly", "C": "Introduction of an executive federal president", "D": "Abolition of all British colonial rule"}
                items.append((
                    "Clifford Constitution (1922)", q_text, opts, "A",
                    "Clifford introduced elections for 3 representatives from Lagos and 1 from Calabar, stimulating political party formation.",
                    "What constitutional milestone allowed Nigerians to cast democratic ballots for the first time in 1922?"
                ))
            elif sub_type == 1:
                q_text = "The Lyttelton Constitution of 1954 is historically revered in Nigerian constitutional evolution because it formally established:"
                opts = {"A": "A truly federal framework with exclusive, concurrent, and residual legislative lists", "B": "A unitary dictatorship under the Governor-General", "C": "Universal adult suffrage for Northern women", "D": "A republican supreme court"}
                items.append((
                    "Lyttelton Constitution (1954)", q_text, opts, "A",
                    "Lyttelton institutionalized regional autonomy, regional premiers, and divided federal-regional legislative powers.",
                    "Which colonial constitution created genuine federalism and autonomous regional governments in Nigeria?"
                ))
            elif sub_type == 2:
                q_text = "The historic significance of the 1963 Republican Constitution of Nigeria was:"
                opts = {"A": "Severing legal ties with the British Monarchy and making the Nigerian Supreme Court the apex court of appeal", "B": "Adopting the American executive presidential model", "C": "Introducing the elective principle", "D": "Granting political independence from Britain"}
                items.append((
                    "1963 Republican Constitution", q_text, opts, "A",
                    "Queen Elizabeth II was replaced by an elected President (Dr. Nnamdi Azikiwe), and appeals to the British Privy Council were terminated.",
                    "What did the 1963 Constitution do to the judicial role of the British Privy Council in Nigeria?"
                ))
            else:
                q_text = "The 1979 Constitution marked a revolutionary departure in Nigerian history by discarding the Westminster parliamentary model in favor of:"
                opts = {"A": "An American-style Executive Presidential system", "B": "A socialist command state", "C": "A diarchy military council", "D": "A confederation of independent states"}
                items.append((
                    "1979 Second Republic Constitution", q_text, opts, "A",
                    "The 1979 Constitution created an executive president with a nationwide mandate and strict institutional separation of powers.",
                    "Which foreign system of governance did Nigeria adopt upon transitioning to the Second Republic in 1979?"
                ))

        else: # Federalism, Military Rule & Foreign Policy
            sub_type = i % 4
            if sub_type == 0:
                q_text = "The 'derivation principle' in Nigerian fiscal federalism dictates that:"
                opts = {"A": "A specific percentage of federally collected revenue must be returned directly to the state where the natural resource was extracted", "B": "All revenues are shared equally regardless of location", "C": "States receive funds solely based on population census", "D": "The federal president retains all mineral royalties"}
                items.append((
                    "Fiscal Federalism & Derivation", q_text, opts, "A",
                    "Derivation compensates oil and mineral producing communities for resource depletion and ecological degradation.",
                    "What principle guarantees mineral-producing states a direct percentage share of natural resource revenues?"
                ))
            elif sub_type == 1:
                q_text = "Nigerian military regimes systematically inserted 'ouster clauses' into their decrees in order to:"
                opts = {"A": "Strip regular courts of jurisdiction to question or invalidate military decrees", "B": "Expel foreign commercial ambassadors", "C": "Dismiss civilian civil servants without trial", "D": "Abolish the Central Bank"}
                items.append((
                    "Military Rule & Ouster Clauses", q_text, opts, "A",
                    "Ouster clauses shielded military legislation from judicial review, subjugating the constitution to military decree supremacy.",
                    "Why did military juntas bar regular courts from entertaining lawsuits challenging their decrees?"
                ))
            elif sub_type == 2:
                q_text = "Nigeria's foreign policy commitment to 'Afrocentricism' means that:"
                opts = {"A": "The defense of African interests, liberation, and continental development forms the cornerstone of external relations", "B": "Nigeria trades exclusively with West African states", "C": "Foreign diplomats must be of African descent", "D": "Nigeria refuses to join international organizations"}
                items.append((
                    "Afrocentric Foreign Policy", q_text, opts, "A",
                    "Articulated by Prime Minister Balewa, Afrocentricism drove Nigeria's leadership in anti-apartheid liberation and ECOWAS peacekeeping.",
                    "What geographical continent occupies the center of Nigeria's foreign policy considerations?"
                ))
            else:
                q_text = "The Economic Community of West African States (ECOWAS) was founded in Lagos on May 28, 1975, through the joint diplomatic initiative of:"
                opts = {"A": "General Yakubu Gowon of Nigeria and President Gnassingbé Eyadéma of Togo", "B": "General Murtala Mohammed and Dr. Kwame Nkrumah", "C": "General Olusegun Obasanjo and President Léopold Senghor", "D": "Sir Abubakar Tafawa Balewa and Félix Houphouët-Boigny"}
                items.append((
                    "ECOWAS Founding", q_text, opts, "A",
                    "Gowon and Eyadéma spearheaded the Treaty of Lagos uniting Anglophone and Francophone West Africa into an economic bloc.",
                    "Which Nigerian head of state co-founded ECOWAS alongside Togo's president in 1975?"
                ))

    return items

def generate_literature_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Literary Appreciation & Devices":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "The poetic line 'The child is father of the man' (Wordsworth) is an example of which figure of speech?"
                opts = {"A": "Paradox", "B": "Oxymoron", "C": "Hyperbole", "D": "Euphemism"}
                items.append((
                    "Figures of Contradiction", q_text, opts, "A",
                    "A paradox appears self-contradictory on the surface, but reveals a profound philosophical truth upon reflection.",
                    "Is a full sentence that seems contradictory on the surface but contains deep truth a paradox or an oxymoron?"
                ))
            elif sub_type == 1:
                q_text = "In literature, when an outcome turns out to be the exact reverse of what the characters and readers logically expected, it is termed:"
                opts = {"A": "Situational Irony", "B": "Dramatic Irony", "C": "Verbal Irony", "D": "Sarcasm"}
                items.append((
                    "Types of Irony", q_text, opts, "A",
                    "Situational irony involves a sharp discrepancy between expected results and actual physical events.",
                    "What type of irony occurs when real-world circumstances turn out opposite to reasonable expectations?"
                ))
            elif sub_type == 2:
                q_text = "The literary substitution of a physical symbol or attribute for the institution itself (such as using 'The Crown' for the King) is:"
                opts = {"A": "Metonymy", "B": "Synecdoche", "C": "Simile", "D": "Apostrophe"}
                items.append((
                    "Figures of Association", q_text, opts, "A",
                    "Metonymy substitutes an associated concept or attribute for the entity (The Crown => the monarchy). Synecdoche uses a physical part of the whole.",
                    "Is substituting an associated symbol for an authority figure an example of metonymy or synecdoche?"
                ))
            else:
                q_text = "The literary device of placing two contradictory words directly side-by-side (such as 'cruel kindness' or 'sweet sorrow') is:"
                opts = {"A": "Oxymoron", "B": "Paradox", "C": "Metaphor", "D": "Litotes"}
                items.append((
                    "Oxymoron", q_text, opts, "A",
                    "An oxymoron pairs two contradictory words directly adjacent to one another.",
                    "What figure of speech juxtaposes two opposing words right next to each other?"
                ))

        elif topic == "Drama & Theatrical Techniques":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In classical Aristotelian tragedy, the emotional cleansing or purging of pity and fear experienced by the audience is called:"
                opts = {"A": "Catharsis", "B": "Hamartia", "C": "Hubris", "D": "Nemesis"}
                items.append((
                    "Classical Tragedy Conventions", q_text, opts, "A",
                    "Catharsis is the emotional purgation achieved by viewing the tragic downfall of a noble protagonist.",
                    "What ancient Greek dramatic term describes the emotional release of pity and terror in an audience?"
                ))
            elif sub_type == 1:
                q_text = "A dramatic device where a character speaks directly to the audience, while other characters onstage pretend not to hear, is:"
                opts = {"A": "An Aside", "B": "A Soliloquy", "C": "A Monologue", "D": "A Chorus"}
                items.append((
                    "Dramatic Devices", q_text, opts, "A",
                    "An aside is a brief confidential comment addressed to the audience while other characters are frozen or oblivious.",
                    "What theatrical convention allows a character to make a secret remark to the audience while others are onstage?"
                ))
            elif sub_type == 2:
                q_text = "In Wole Soyinka's 'The Lion and the Jewel', the primary reason Sidi rejects Lakunle's marriage proposal is that:"
                opts = {"A": "He refuses to pay her traditional bride price, insulting her village pride", "B": "He is an undercover British police officer", "C": "He cannot speak English", "D": "Her father forbade the union"}
                items.append((
                    "The Lion and the Jewel Analysis", q_text, opts, "A",
                    "Lakunle condemns the bride price as 'savage custom', but Sidi insists that without it, the village will consider her damaged goods.",
                    "Why does Sidi view Lakunle's refusal to pay the bride price as an attack on her personal dignity?"
                ))
            else:
                q_text = "In Femi Osofisan's 'Women of Owu', the central dramatic critique focuses on:"
                opts = {"A": "The catastrophic human toll of imperial warfare inflicted upon innocent women and children", "B": "The introduction of railways into ancient Yoruba city-states", "C": "The discovery of petroleum in the Niger Delta", "D": "Religious rivalry between Christian missionaries"}
                items.append((
                    "Women of Owu Analysis", q_text, opts, "A",
                    "Osofisan adapts Euripides' 'Trojan Women' to condemn patriarchal warmongering and celebrate the resilience of traumatized women.",
                    "Whose tragic suffering does Femi Osofisan highlight following the total destruction of Owu?"
                ))

        elif topic == "Poetry & Versification":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "A Shakespearean (English) sonnet is structurally organized into:"
                opts = {"A": "Three quatrains and a rhyming couplet (abab cdcd efef gg)", "B": "An octave and a sestet (abba abba cde cde)", "C": "Two stanzas of seven lines each", "D": "Four rhyming triplets"}
                items.append((
                    "Sonnet Forms", q_text, opts, "A",
                    "Shakespearean sonnets consist of 14 iambic pentameter lines arranged in 3 quatrains and concluding with a couplet.",
                    "What is the stanzaic breakdown and rhyme scheme of an English/Shakespearean sonnet?"
                ))
            elif sub_type == 1:
                q_text = "A serious, reflective lyrical poem composed specifically to mourn the death of an individual or lament human mortality is:"
                opts = {"A": "An Elegy", "B": "An Ode", "C": "An Epic", "D": "A Ballad"}
                items.append((
                    "Poetic Genres", q_text, opts, "A",
                    "An elegy is a formal lyric expressing grief and meditative mourning for the dead.",
                    "What poetic form is written specifically as a solemn lament for someone who has died?"
                ))
            elif sub_type == 2:
                q_text = "When a poetic sentence runs over from one verse line into the next without terminal punctuation, the technique is:"
                opts = {"A": "Enjambment (Run-on line)", "B": "End-stopping", "C": "Caesura", "D": "Alliteration"}
                items.append((
                    "Poetic Mechanics", q_text, opts, "A",
                    "Enjambment carries syntactic momentum across line breaks to mimic continuous flow or conversational thought.",
                    "What French term describes a line of verse that spills over into the next line without punctuation?"
                ))
            else:
                q_text = "A metrical line of poetry consisting of five feet, where each foot has an unstressed syllable followed by a stressed syllable, is:"
                opts = {"A": "Iambic Pentameter", "B": "Trochaic Tetrameter", "C": "Dactylic Hexameter", "D": "Anapestic Trimeter"}
                items.append((
                    "Poetic Meter", q_text, opts, "A",
                    "Iambic pentameter consists of five iambs (da-DUM da-DUM da-DUM da-DUM da-DUM), totaling 10 syllables.",
                    "What metrical rhythm contains five pairs of unstressed and stressed syllables?"
                ))

        else: # Prose & Fictional Techniques
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In Chinua Achebe's 'Things Fall Apart', Okonkwo's tragic downfall is catalyzed primarily by his:"
                opts = {"A": "Paralyzing fear of being perceived as weak and failure-prone like his father Unoka", "B": "Refusal to plant yams during the rainy season", "C": "Desire to convert to Christianity", "D": "Exile to the British penal colony"}
                items.append((
                    "Things Fall Apart Analysis", q_text, opts, "A",
                    "Achebe explicitly states: 'Okonkwo was ruled by one passion—to hate everything that his father Unoka had loved.' This internal insecurity drove his excessive violence.",
                    "What deep-seated psychological trauma drove Okonkwo's aggressive obsession with hyper-masculinity?"
                ))
            elif sub_type == 1:
                q_text = "In Buchi Emecheta's 'The Joys of Motherhood', the tragic irony of Nnu Ego's life culminates in:"
                opts = {"A": "Dying alone and destitute by a roadside, neglected by the sons for whom she sacrificed her youth", "B": "Becoming a wealthy cocoa merchant in Ibadan", "C": "Receiving a chieftaincy title in Ibuza", "D": "Founding a national women's university"}
                items.append((
                    "The Joys of Motherhood Analysis", q_text, opts, "A",
                    "Emecheta sharply subverts patriarchal expectations: Nnu Ego's complete self-abnegation for motherhood brings poverty and abandonment, not joy.",
                    "How does Nnu Ego's lonely death expose the hollow promises of traditional patriarchal mother-worship?"
                ))
            elif sub_type == 2:
                q_text = "When a story is narrated by a voice that knows all characters' internal thoughts, motives, historical secrets, and future outcomes, the point of view is:"
                opts = {"A": "Third-Person Omniscient", "B": "First-Person Participant", "C": "Third-Person Limited", "D": "Second-Person Objective"}
                items.append((
                    "Narrative Point of View", q_text, opts, "A",
                    "An omniscient narrator possesses god-like, all-knowing insight into the consciousness of every character.",
                    "What narrative perspective possesses unrestricted access to the inner psychology of all characters?"
                ))
            else:
                q_text = "A literary narrative device in which an author provides subtle clues or warnings about significant plot developments to occur later is:"
                opts = {"A": "Foreshadowing", "B": "Flashback (Analepsis)", "C": "In media res", "D": "Deus ex machina"}
                items.append((
                    "Fictional Techniques", q_text, opts, "A",
                    "Foreshadowing plants advance hints that prepare the reader psychologically for future dramatic revelations.",
                    "What plot technique drops early literary hints about impending tragic or dramatic events?"
                ))

    return items
