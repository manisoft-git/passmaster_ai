import random

def generate_government_questions(topic, count_needed=150):
    items = []

    if topic == "Elements of Government & Political Theory":
        # Basic political concepts
        concepts = [
            ("State", "A politically organized sovereign community occupying a clearly defined geographical territory with a legitimate government and population", "A cultural club", "A political party", "A labor union"),
            ("Sovereignty", "The supreme, absolute, and uncontrollable political authority of a state to make and enforce laws free from external control", "The popularity of a politician", "The wealth of a country", "Military conquest alone"),
            ("Power vs Authority (Max Weber)", "Power is the ability to enforce obedience through coercion or sanctions; Authority is the legitimate, legally accepted right to exercise power", "Power is always legal while authority is illegal", "They are identical in all respects", "Authority relies solely on gun violence"),
            ("Traditional Authority", "Legitimacy derived from long-standing ancestral customs, hereditary succession, and established sacred traditions (e.g. Obas, Emirs, Obis)", "Derived from democratic elections", "Derived from personal magnetic charisma", "Created by constitutional written statutes"),
            ("Charismatic Authority", "Legitimacy resting on extraordinary personal magnetism, exceptional heroism, or exemplary visionary qualities of an individual leader", "Hereditary royalty", "Bureaucratic office", "Military junta"),
            ("Legal-Rational / Bureaucratic Authority", "Legitimacy grounded in formally enacted constitutional rules, institutional laws, and offices rather than the person occupying the office", "Divine right of kings", "Supernatural powers", "Physical brute strength"),
            ("Legitimacy", "The popular moral and constitutional acceptance by the citizens of the government's right to govern and issue binding directives", "The total size of the army", "The amount of money printed", "Foreign military support"),
            ("Political Socialization", "The lifelong process by which individuals acquire political beliefs, civic attitudes, values, and behavioral norms through agents like family and schools", "Voting on election day only", "Bribing electoral officers", "Overthrowing a government")
        ]
        for c_title, c_desc, d1, d2, d3 in concepts:
            q_text = f"In political theory, which definition accurately explains '{c_title}'?"
            opts = {"A": c_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Core Political Theory Concepts", q_text, opts, "A",
                f"{c_title}: {c_desc}.",
                "Distinguish between state, sovereignty, power, authority, and legitimacy."
            ))

        # Forms of government
        gov_forms = [
            ("Parliamentary (Cabinet) system of government", "Fusion of executive and legislative powers, collective cabinet responsibility, and clear institutional separation between Head of State (monarch/president) and Head of Government (Prime Minister)", "Strict separation of powers with executive president", "Single military dictator", "Absence of parliament"),
            ("Presidential system of government", "Clear separation of powers, individual executive responsibility, fixed presidential tenure, and the President serves concurrently as both Head of State and Head of Government", "Prime minister elected from parliament", "Cabinet members must be sitting legislators", "No supreme court review"),
            ("Unitary system of government", "All constitutional governmental powers are concentrated in a single central national government; sub-national units exist merely as administrative delegates", "Autonomous sovereign states sharing power", "Power divided by constitution between tiers", "No central executive"),
            ("Federal system of government", "Constitutional division of sovereign governmental powers between a central national authority and autonomous federating units (states/regions)", "All power held by monarch", "Loose alliance with right to secede", "Single tier legislature only"),
            ("Confederal system (Confederation)", "A loose league of independent sovereign states delegating specific limited functions (defense, diplomacy) to a weak central council, retaining right of secession", "Strong centralized federal state", "Unitary dictatorship", "Strict presidential system")
        ]
        for f_name, f_desc, d1, d2, d3 in gov_forms:
            q_text = f"Which institutional feature distinguishes a {f_name.lower()}?"
            opts = {"A": f_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Systems and Forms of Government", q_text, opts, "A",
                f"{f_name}: {f_desc}.",
                "Examine executive-legislative relations and central versus regional power distributions."
            ))

        # Rule of Law and Separation of Powers
        doctrines = [
            ("A.V. Dicey's Doctrine of the Rule of Law", "Three cardinal pillars: absolute supremacy of regular law over arbitrary power, equality of all citizens before the law, and protection of fundamental human rights by the courts", "Dictatorship of the proletariat", "Divine right of kings", "Military supremacy over civilian laws"),
            ("Baron de Montesquieu's Doctrine of Separation of Powers", "Governmental powers should be distributed among three distinct, autonomous organs (Legislature, Executive, Judiciary) to prevent tyranny and preserve liberty", "Concentration of all power in one monarch", "Judiciary makes all laws", "Executive controls all courts directly"),
            ("System of Checks and Balances", "Each arm of government possesses constitutional powers to monitor, constrain, and check the potential excesses of the other two arms", "Complete isolation of organs", "Fusion of powers in parliament", "Military override of court orders")
        ]
        for d_name, d_desc, d1, d2, d3 in doctrines:
            q_text = f"What is the core philosophical tenet of {d_name}?"
            opts = {"A": d_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Constitutional Doctrines: Rule of Law & Separation of Powers", q_text, opts, "A",
                f"{d_name}: {d_desc}.",
                "Recall Dicey's three principles and Montesquieu's institutional checks."
            ))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        # Pre-colonial political systems
        precolonial = [
            ("Pre-colonial Hausa-Fulani Emirate System", "Highly centralized, theocratic autocratic system where the Emir wielded supreme executive and legislative authority, assisted by the Waziri (Prime Minister) and Alkali Sharia courts", "Decentralized acephalous democracy", "Constitutional monarchy with Oyomesi", "Age-grade direct assembly"),
            ("Pre-colonial Oyo Yoruba Kingdom", "Constitutional monarchy with institutional checks and balances; the Alaafin's executive powers were checked by the Oyomesi council of kingmakers led by the Bashorun and the Ogboni cult", "Absolute military theocracy", "Stateless segmentary lineage", "Feudal sultanate without council"),
            ("Pre-colonial Igbo Political Administration", "Acephalous (stateless), decentralized, segmentary political system characterized by direct participatory democracy involving the Ama-ala village assembly, Ofo titleholders, Ozo society, and age grades", "Centralized royal court with absolute king", "Theocratic caliphate", "Unitary military autocracy"),
            ("The ultimate constitutional sanction against a tyrannical Alaafin in Old Oyo", "The Bashorun presented the Alaafin with an empty calabash or parrot's eggs signifying rejection by the ancestors, compelling him to commit suicide", "Imprisonment in modern jail", "Removal of salary", "Exile to Europe")
        ]
        for pc_name, pc_desc, d1, d2, d3 in precolonial:
            q_text = f"Which governance framework characterized the {pc_name}?"
            opts = {"A": pc_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pre-Colonial Nigerian Political Systems", q_text, opts, "A",
                f"{pc_name}: {pc_desc}.",
                "Distinguish centralized Hausa-Fulani, checks-and-balances Yoruba, and acephalous Igbo systems."
            ))

        # British Indirect Rule
        indirect_rule = [
            ("Lord Lugard's system of Indirect Rule", "Governing colonized populations through their existing indigenous traditional rulers and native institutions under the supervision of British colonial residents", "Direct rule by British soldiers only", "Total destruction of indigenous culture", "Assimilation into British citizens"),
            ("Primary reason Indirect Rule succeeded exceptionally well in Northern Nigeria", "Presence of a highly centralized, hierarchical administrative structure under Emirs, an established tax system, and judicial Sharia courts", "Absence of any kings", "Widespread Christianity", "High British literacy among chiefs"),
            ("Primary cause of the complete failure of Indirect Rule in Eastern Nigeria", "The acephalous, decentralized segmentary nature of traditional Igbo society and the artificial imposition of appointed 'Warrant Chiefs'", "Resistance of the powerful Sultan", "Existing Islamic courts", "Rejection of British direct democracy"),
            ("1929 Aba Women's Riot in Eastern Nigeria", "Spontaneous revolt by Igbo women triggered by rumors of colonial taxation on women and widespread abuses by corrupt Warrant Chiefs", "Protest against school fees", "Demand for independence in 1929", "Religious conflict between churches")
        ]
        for ir_title, ir_desc, d1, d2, d3 in indirect_rule:
            q_text = f"What was the historical reality of {ir_title.lower()}?"
            opts = {"A": ir_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "British Colonial Administration & Indirect Rule", q_text, opts, "A",
                f"{ir_title}: {ir_desc}.",
                "Examine Lugard's administrative policy and varying regional receptions across Nigeria."
            ))

        # French Assimilation vs Association
        french_policy = [
            ("French Colonial Policy of Assimilation", "A cultural imperialist policy designed to transform indigenous Africans into Frenchmen through adoption of French language, culture, religion, and legal civil codes", "Ruling through native emirs", "Promoting indigenous African culture", "Immediate grant of national sovereignty"),
            ("The 'Four Communes' of Senegal where Assimilation was partially implemented", "Saint-Louis, Gorée, Dakar, and Rufisque (residents enjoyed full French citizenship and elected a deputy to the French National Assembly)", "Bamako, Conakry, Abidjan, Niamey", "Lagos, Calabar, Kano, Ibadan", "Accra, Kumasi, Cape Coast, Tamale"),
            ("Indigénat legal code under French colonial rule", "An arbitrary, repressive penal regime authorizing French colonial administrators to inflict summary arrest, fines, and forced labor (corvée) on subjects without trial", "A democratic constitution", "Free public education charter", "A bill of fundamental human rights")
        ]
        for fp_title, fp_desc, d1, d2, d3 in french_policy:
            q_text = f"Which historical fact characterizes the {fp_title.lower()}?"
            opts = {"A": fp_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "French Colonial Policy in West Africa", q_text, opts, "A",
                f"{fp_title}: {fp_desc}.",
                "Contrast British indirect rule with French assimilation, the Four Communes, and the Indigénat."
            ))

    elif topic == "Nigerian Constitutional Development":
        # Pre-independence constitutions
        constitutions = [
            ("Clifford Constitution of 1922", "First introduced the Elective Principle in Nigeria, creating 4 elected legislative seats (3 in Lagos, 1 in Calabar) which led to the formation of the NNDP by Herbert Macaulay", "Created the three regions", "Abolished the British monarchy", "Introduced presidential system"),
            ("Richards Constitution of 1946", "First introduced regionalism by dividing Nigeria into Northern, Western, and Eastern regions, bringing the North into the central legislative council for the first time", "Introduced the elective principle", "Granted independence to Nigeria", "Excised Lagos as federal capital"),
            ("Macpherson Constitution of 1951", "Introduced widespread consultation from village through provincial to regional levels, establishing a central Council of Ministers and quasi-ministerial system", "First introduced elective principle", "Abolished the regions", "Adopted executive presidency"),
            ("Lyttelton Constitution of 1954", "The formal birth of Nigerian Federalism: decentralized powers between central and regional governments, established premier offices, and excised Lagos as Federal Territory", "Introduced the Richards regionalism", "Abolished regional civil services", "Created the 12 states")
        ]
        for const_name, const_feat, d1, d2, d3 in constitutions:
            q_text = f"What landmark constitutional breakthrough was established by the {const_name}?"
            opts = {"A": const_feat, "B": d1, "C": d2, "D": d3}
            items.append((
                "Colonial Constitutional Evolution in Nigeria", q_text, opts, "A",
                f"{const_name}: {const_feat}.",
                "Trace constitutional milestones: Clifford (1922), Richards (1946), Macpherson (1951), Lyttelton (1954)."
            ))

        # Post-independence constitutions
        post_const = [
            ("Independence Constitution of 1960", "Retained the British monarch (Queen Elizabeth II) as titular Head of State represented by Governor-General Nnamdi Azikiwe, with parliamentary Prime Minister Sir Abubakar Tafawa Balewa", "Adopted an executive presidential system", "Severed all ties with Britain", "Abolished the Supreme Court"),
            ("Republican Constitution of 1963", "Completely severed monarchical ties with the British Crown; replaced the Queen with a ceremonial President (Nnamdi Azikiwe) and made Supreme Court apex appellate court", "Introduced executive presidency", "Created the 36 states", "Suspended the constitution"),
            ("1979 Constitution of the Second Republic", "Transitioned Nigeria from the British Westminster parliamentary system to an American-style Executive Presidential system with separation of powers and a bicameral National Assembly", "Adopted a prime ministerial model", "Re-instated British Governor-General", "Created unitary decrees"),
            ("1999 Constitution of the Fourth Republic", "Executive presidential framework establishing 36 states and FCT, bicameral National Assembly, separation of powers, and Exclusive, Concurrent, and Residual legislative lists", "Unicameral parliamentary system", "Confederal assembly", "Military council decree")
        ]
        for pc_name, pc_desc, d1, d2, d3 in post_const:
            q_text = f"Which structural provision defines the {pc_name}?"
            opts = {"A": pc_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Post-Independence Nigerian Constitutions", q_text, opts, "A",
                f"{pc_name}: {pc_desc}.",
                "Distinguish 1960 independence, 1963 republic, 1979 executive presidential, and 1999 frameworks."
            ))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        # State creation evolution
        state_evol = [
            ("1967 State Creation by General Yakubu Gowon", "Dissolved the 4 regions and created 12 states by decree on the eve of the Nigerian Civil War to break regional polarization and secure minority loyalty", "Created 19 states", "Created 36 states", "Abolished federalism"),
            ("1976 State Creation by General Murtala Mohammed", "Expanded the federal structure from 12 states to 19 states based on recommendations of the Justice Ayo Irikefe Panel", "Created 12 states", "Created 30 states", "Created 21 states"),
            ("1987 State Creation by General Ibrahim Babangida", "Created 2 new states (Akwa Ibom and Katsina), bringing the total to 21 states", "Created 36 states", "Created 12 states", "Created 19 states"),
            ("1991 State Creation by General Ibrahim Babangida", "Created 9 new states, expanding the federal structure to 30 states", "Created 19 states", "Created 36 states", "Created 12 states"),
            ("1996 State Creation by General Sani Abacha", "Created 6 new states (Bayelsa, Ebonyi, Ekiti, Gombe, Nasarawa, Zamfara), bringing the current federal structure to 36 states", "Created 21 states", "Created 30 states", "Created 19 states")
        ]
        for se_title, se_desc, d1, d2, d3 in state_evol:
            q_text = f"What historical milestone was achieved during the {se_title}?"
            opts = {"A": se_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Evolution of Nigerian Federalism & State Creation", q_text, opts, "A",
                f"{se_title}: {se_desc}.",
                "Chronicle Nigerian state creation from 12 states (1967) to 36 states (1996)."
            ))

        # Military rule features
        mil_rule = [
            ("Decree No. 34 (Unification Decree) of May 1966 issued by Major-General Aguiyi-Ironsi", "Abolished the federal structure, centralized civil services, and converted Nigeria into a unitary state, triggering immense northern unrest", "Created 12 states", "Returned power to civilians", "Restored the 1960 constitution"),
            ("Hallmarks of military governance in Nigeria", "Suspension and modification of the constitution, rule by decrees and edicts, concentration/fusion of executive and legislative powers, and absence of judicial review", "Strict adherence to separation of powers", "Bicameral parliaments", "Free multi-party elections"),
            ("General Olusegun Obasanjo's military handover in 1979", "Honored the transition timetable established by Murtala Mohammed, handing over power peacefully to democratically elected President Shehu Shagari", "Annulled the election results", "Extended military rule for 10 years", "Banned all political parties permanently"),
            ("General Abdulsalami Abubakar's 1998-1999 Transition Program", "Conducted swift, transparent democratic elections within 11 months, promulgating the 1999 Constitution and handing over power to Olusegun Obasanjo on May 29, 1999", "Refused to step down", "Created 50 new states", "Annulled the 1999 elections")
        ]
        for mr_title, mr_desc, d1, d2, d3 in mil_rule:
            q_text = f"Which major political event characterizes {mr_title}?"
            opts = {"A": mr_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Military Rule & Constitutional Transitions in Nigeria", q_text, opts, "A",
                f"{mr_title}: {mr_desc}.",
                "Examine military coups, decrees, and transitions back to civilian democracy."
            ))

        # Foreign policy
        foreign_policy = [
            ("Afrocentric foreign policy posture (Africa as the centerpiece)", "Nigeria's strategic commitment to prioritizing the political liberation, decolonization, security, and economic integration of the African continent", "Aligning exclusively with European powers", "Ignoring African crises", "Promoting American foreign interests"),
            ("Nigeria's leadership in the anti-apartheid struggle in Southern Africa", "Granted financial grants, passport facilities, scholarships to South African students, and nationalized British Petroleum assets to compel British compliance", "Supported the white minority apartheid regime", "Refused to join the UN committee on apartheid", "Banned all South African liberation movements"),
            ("Founding of ECOWAS (Economic Community of West African States) in Lagos (1975)", "Spearheaded by General Yakubu Gowon of Nigeria and President Gnassingbé Eyadéma of Togo to promote regional economic cooperation and free trade", "Created by European powers", "Formed to wage war in Asia", "A strictly military anti-communist alliance"),
            ("ECOMOG (ECOWAS Ceasefire Monitoring Group) military intervention", "Nigeria-led regional peacekeeping force that intervened decisively to restore peace during civil wars in Liberia and Sierra Leone", "NATO military exercise", "UN force in the Middle East", "Invasion of South Africa")
        ]
        for fp_t, fp_d, d1, d2, d3 in foreign_policy:
            q_text = f"In Nigerian diplomatic history, which principle explains {fp_t.lower()}?"
            opts = {"A": fp_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Nigerian Foreign Policy & International Relations", q_text, opts, "A",
                f"{fp_t}: {fp_d}.",
                "Analyze Nigeria's Afrocentric foreign policy, anti-apartheid leadership, and ECOMOG peacekeeping."
            ))

    append_deep_government(items, topic)
    append_exhaustive_government(items, topic)
    append_master_government(items, topic)
    append_ultimate_government(items, topic)
    append_grandmaster_government(items, topic)
    append_sovereign_government(items, topic)
    return items

def append_deep_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        # Electoral systems
        electoral_sys = [
            ("First-Past-The-Post / Simple Majority System (Plurality)", "The candidate who secures the highest number of votes in a single-member constituency is declared winner, even without an absolute majority (>50%)", "Requires 100% consensus", "Every voter ranks all candidates", "Seats allocated proportional to national vote"),
            ("Proportional Representation (PR) System", "Total parliamentary seats are allocated to political parties in strict mathematical proportion to the percentage of total popular votes polled nationally", "Winner takes all in each district", "Candidate with one vote wins all seats", "No political parties exist"),
            ("Alternative Vote (Preferential Voting) System", "Voters rank candidates in order of preference (1, 2, 3); lowest candidates are eliminated and second preferences redistributed until one candidate secures an absolute majority (>50%)", "Simple plurality only", "Candidate chosen by lot", "Only one candidate allowed"),
            ("Second Ballot / Run-off Electoral System", "If no candidate secures an absolute majority (>50%) in the initial general election, a second run-off election is contested exclusively between the top two candidates", "Winner chosen by coin toss", "Election cancelled permanently", "The candidate with lowest votes wins")
        ]
        for es_name, es_desc, d1, d2, d3 in electoral_sys:
            q_text = f"Which mechanism defines the {es_name.lower()}?"
            opts = {"A": es_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Electoral Systems & Voting Formulas", q_text, opts, "A",
                f"{es_name}: {es_desc}.",
                "Distinguish plurality systems from proportional allocation and preferential rankings."
            ))

        # Pressure groups vs Political parties
        pressure_q = [
            ("Fundamental structural distinction between a Pressure Group and a Political Party", "A political party aspires directly to capture sovereign state power and form the government; a pressure group seeks solely to influence government policies without seeking formal office", "Political parties never participate in elections", "Pressure groups always field presidential candidates", "They are identical in purpose and operations"),
            ("Professional / Occupational Pressure Group (e.g. Nigerian Medical Association - NMA, Nigerian Bar Association - NBA, ASUU)", "Defends and promotes the economic welfare, working conditions, and occupational standards of its certified professional members", "Promotes religious charity for all", "Seeks to overthrow the government", "Operates commercial passenger buses"),
            ("Promotional / Cause Pressure Group (e.g. Amnesty International, Civil Liberties Organisation - CLO)", "Campaigns selflessly for altruistic public causes, civil human rights, or environmental protection, benefiting society broadly rather than members' private interests", "Fights only for doctors' salaries", "Seeks to win parliamentary elections", "Distributes commercial goods"),
            ("Anomic Pressure Group", "Spontaneous, unorganized crowds or mob demonstrations that erupt suddenly in response to acute social grievances, price hikes, or police brutality (e.g. #EndSARS protests)", "Formally registered trade union", "Elected senate committee", "Diplomatic embassy")
        ]
        for pq_title, pq_ans, d1, d2, d3 in pressure_q:
            q_text = f"In political sociology, what explains {pq_title.lower()}?"
            opts = {"A": pq_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pressure Groups & Civil Society Organizations", q_text, opts, "A",
                f"{pq_title}: {pq_ans}.",
                "Contrast seeking state office with lobbying and public policy advocacy."
            ))

        # Civil Service characteristics (Max Weber)
        civil_service = [
            ("Political Neutrality of the Civil Service", "Civil servants must serve whatever political party is democratically elected into power with total impartiality and refrain from partisan public politics", "Civil servants must campaign for the ruling party", "Civil servants resign when the president changes", "Civil servants must lead opposition protests"),
            ("Principle of Anonymity in the Civil Service", "Civil servants work quietly behind the scenes; the political Minister takes all public praise for successes and all constitutional blame for bureaucratic failures", "Civil servants never receive salaries", "Civil servants wear secret masks", "Civil servants operate without offices"),
            ("Principle of Permanence of Tenure", "Civil servants enjoy secure long-term career employment protected by the Civil Service Commission, surviving changes of government administrations", "Employment terminates every month", "Civil servants are hired by lottery", "Only soldiers can become civil servants")
        ]
        for cs_name, cs_desc, d1, d2, d3 in civil_service:
            q_text = f"Which civil service doctrine is defined by: '{cs_desc}'?"
            opts = {"A": cs_name, "B": d1, "C": d2, "D": d3}
            items.append((
                "Public Administration & Civil Service Principles", q_text, opts, "A",
                f"This describes the {cs_name}.",
                "Recall Weberian civil service tenets of neutrality, anonymity, and permanence."
            ))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        # Pre-colonial Hausa-Fulani Emirate Officials
        hausa_officials = [
            ("Waziri", "Prime Minister, chief legal and political advisor, and administrative coordinator of the Emirate", "Commander of the cavalry", "Head of the prison", "Treasurer"),
            ("Madawaki", "Commander-in-Chief of the Emirate cavalry and armed forces", "Chief judge", "Collector of river taxes", "Head of the market"),
            ("Galadima", "Governor / Administrator in charge of the security and day-to-day administration of the Emirate capital city", "Commander of foot soldiers", "Religious prayer leader", "Court jester"),
            ("Sarkin Fada", "Head of the Emir's palace administration, royal courtiers, and household staff", "Head of butchers", "Chief tax collector", "Head of prison warders"),
            ("Dogari", "Chief of the Emirate police force responsible for law enforcement and palace guards", "Naval admiral", "Foreign minister", "Head of blacksmiths"),
            ("Alkali", "Islamic magistrate / judge who presided over Sharia courts adjudicating civil and criminal cases according to Maliki Islamic jurisprudence", "Army general", "Horse caretaker", "Tax assessor")
        ]
        for off_name, off_role, d1, d2, d3 in hausa_officials:
            q_text = f"In the pre-colonial Hausa-Fulani political administration, what was the official portfolio of the '{off_name}'?"
            opts = {"A": off_role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pre-Colonial Hausa-Fulani Administrative Portfolios", q_text, opts, "A",
                f"The {off_name} served as {off_role.lower()}.",
                f"Identify the specialized administrative or judicial function of the {off_name}."
            ))

        # Pre-colonial Yoruba Officials & Oyo Empire
        yoruba_officials = [
            ("Bashorun", "Prime Minister and leader of the Oyomesi (council of seven kingmakers) possessing the constitutional authority to declare no-confidence in the Alaafin", "Commander of foot soldiers", "Palace gatekeeper", "Market supervisor"),
            ("Oyomesi", "Council of seven noble kingmakers representing the seven non-royal wards of Oyo, tasked with screening and selecting the new Alaafin and checking royal tyranny", "Secret cult of youth", "Royal bodyguards", "Foreign merchants"),
            ("Ogboni Society", "A powerful sacred secret cult of distinguished elders dedicated to the worship of the Earth goddess (Ile), mediating disputes between Alaafin and Oyomesi", "The trade union of farmers", "The king's personal soldiers", "An association of tax collectors"),
            ("Are-Ona-Kakanfo", "Supreme Field Marshal and supreme military commander of the Oyo imperial army; tradition mandated that he commit suicide if defeated in battle", "Chief tax collector", "Prime minister of the palace", "Spiritual high priest"),
            ("Iyalode", "Distinguished female chief representing women's commercial interests, market administration, and female civic affairs in the royal council", "Commander of the cavalry", "Supreme court judge", "Executioner")
        ]
        for y_title, y_role, d1, d2, d3 in yoruba_officials:
            q_text = f"In the constitutional structure of the pre-colonial Oyo Empire, what was the primary role of the '{y_title}'?"
            opts = {"A": y_role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pre-Colonial Yoruba Constitutional Framework", q_text, opts, "A",
                f"The {y_title} served as {y_role.lower()}.",
                f"Identify the constitutional check or military function of the {y_title}."
            ))

        # Early Nationalist leaders
        nationalists = [
            ("Herbert Macaulay (1864-1946)", "Widely revered as the 'Father of Nigerian Nationalism'; founded Nigeria's first political party, the Nigerian National Democratic Party (NNDP) in 1923, and established the Lagos Daily News", "First military head of state", "Premier of Northern Nigeria", "Author of the 1979 constitution"),
            ("Dr. Nnamdi Azikiwe (Zik of Africa)", "Pioneering nationalist who founded the West African Pilot newspaper in 1937, led the NCNC party, and became Nigeria's first indigenous Governor-General (1960) and President (1963)", "Leader of the Action Group", "Leader of the Northern People's Congress", "British colonial governor"),
            ("Chief Obafemi Awolowo", "Visionary statesman who founded the Egbe Omo Oduduwa and the Action Group (AG) party, pioneered Universal Primary Education (UPE) as Premier of the Western Region", "Leader of NEPU", "Military head of state in 1966", "President of the Senate in 1960"),
            ("Sir Ahmadu Bello (Sardauna of Sokoto)", "Foremost Northern political leader and Premier of the Northern Region; led the Northern People's Congress (NPC) and championed northern modernization within federal Nigeria", "Founder of the NNDP in Lagos", "Editor of the West African Pilot", "Commander of ECOMOG"),
            ("Mallam Aminu Kano", "Radical populist nationalist who broke from the NPC to form the Northern Elements Progressive Union (NEPU), championing the emancipation of the oppressed peasant talakawa class", "Founder of the Action Group", "Premier of Western Nigeria", "Supreme court chief justice")
        ]
        for nat_name, nat_legacy, d1, d2, d3 in nationalists:
            q_text = f"What was the monumental contribution of '{nat_name}' to Nigerian political development?"
            opts = {"A": nat_legacy, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pioneering Nigerian Nationalist Movements & Leaders", q_text, opts, "A",
                f"{nat_name}: {nat_legacy}.",
                "Recognize the political party, media organ, and regional leadership of early nationalists."
            ))

    elif topic == "Nigerian Constitutional Development":
        # Legislative lists
        leg_lists = [
            ("Exclusive Legislative List in Nigerian Constitutions", "Matters on which only the Federal National Assembly possesses constitutional jurisdiction to legislate (e.g. Defense, Foreign Affairs, Currency, Citizenship, Police, Customs)", "Matters shared equally with local councils", "Matters on which only state assemblies legislate", "Matters decided by customary chiefs"),
            ("Concurrent Legislative List", "Matters on which both the Federal National Assembly and State Houses of Assembly possess constitutional competence to legislate (e.g. Higher education, Agriculture, Industrial promotion, Health)", "Matters exclusively for the President", "Matters reserved exclusively for states", "Diplomatic treaties"),
            ("Doctrine of Covering the Field (Legislative Inconsistency)", "If a state law is inconsistent with a valid federal enactment on a concurrent subject, the federal law prevails and the state law becomes void to the extent of its inconsistency", "The state law always overrides federal law", "Both laws are canceled immediately", "The Supreme Court becomes the legislature"),
            ("Residual Legislative List", "All constitutional legislative subjects not specifically enumerated in either the Exclusive or Concurrent lists, which are reserved exclusively for State Houses of Assembly (e.g. Chieftaincy, local markets)", "Matters handled by the United Nations", "Matters reserved for the military", "Federal defense matters")
        ]
        for list_name, list_desc, d1, d2, d3 in leg_lists:
            q_text = f"Under Nigerian constitutional federalism, how is the '{list_name}' defined?"
            opts = {"A": list_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Division of Powers: Exclusive, Concurrent & Residual Lists", q_text, opts, "A",
                f"{list_name}: {list_desc}.",
                "Distinguish federal exclusivity from concurrent shared powers and state residual jurisdiction."
            ))

        # Judicial hierarchy in Nigeria
        judiciary_q = [
            ("Supreme Court of Nigeria", "The apex court of final appellate jurisdiction in Nigeria; its judicial decisions are binding precedents on all lower courts (stare decisis)", "The court that handles minor land disputes in villages", "A court presided over by the police", "A military tribunal only"),
            ("Court of Appeal", "The intermediate appellate court situated directly below the Supreme Court, hearing appeals from Federal and State High Courts, Election Tribunals, and National Industrial Court", "The lowest court in Nigeria", "Court that issues driving licenses", "Court presided over by traditional emirs"),
            ("National Industrial Court (NIC)", "Specialized superior court of record possessing exclusive original jurisdiction in civil causes related to labor, industrial relations, trade unions, and employment disputes", "Handles murder trials only", "Adjudicates land inheritance disputes", "Decides presidential elections"),
            ("Power of Judicial Review", "The constitutional authority of superior courts of record to declare acts of the Legislature or Executive unconstitutional, null, and void if they violate the constitution", "The right of judges to write new laws", "The power of the president to dismiss judges", "The right of police to overturn court verdicts")
        ]
        for jud_name, jud_desc, d1, d2, d3 in judiciary_q:
            q_text = f"What is the constitutional mandate of the '{jud_name}' in the Nigerian judicial hierarchy?"
            opts = {"A": jud_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Judicial Hierarchy & Powers in Nigeria", q_text, opts, "A",
                f"{jud_name}: {jud_desc}.",
                "Understand the appellate hierarchy from trial courts to the Supreme Court."
            ))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        # Military rulers and regimes
        military_regimes = [
            ("Major-General J.T.U. Aguiyi-Ironsi (January 1966 - July 1966)", "Assumed power following the January 15 coup led by Major Nzeogwu; promulgated Decree 34 (Unification Decree) abolishing federalism, leading to the July counter-coup", "Created 12 states in 1967", "Handed over power in 1979", "Annulled the June 12 election"),
            ("General Yakubu Gowon (July 1966 - July 1975)", "Created 12 states in May 1967, prosecuted the Nigerian Civil War (1967-1970) with the 'No Victor, No Vanquished' policy, launched the 3Rs (Reconciliation, Rehabilitation, Reconstruction), and co-founded ECOWAS", "Introduced the 1999 constitution", "Assassinated in 1976", "Promulgated Decree 34"),
            ("General Murtala Ramat Mohammed (July 1975 - February 1976)", "Dynamic reformist ruler who purged corrupt public servants, created 19 states, initiated the movement of the Federal Capital to Abuja, and established the 1979 transition program before his assassination", "Annulled the June 12 election", "Formed the first Nigerian political party", "Prosecuted the 1967 civil war"),
            ("Major-General Muhammadu Buhari (December 1983 - August 1985)", "Overthrew the Second Republic of Shehu Shagari; launched the War Against Indiscipline (WAI), executed currency change, and promulgated Decree No. 4 (Protection of Public Officers Against False Accusation)", "Handed over to civilians in 1979", "Created 36 states", "Co-founded ECOWAS in 1975"),
            ("General Ibrahim Badamasi Babangida (August 1985 - August 1993)", "Declared himself Military President; introduced the Structural Adjustment Programme (SAP), created 11 states (to 30 states), built the Third Mainland Bridge, but notoriously annulled the June 12, 1993 presidential election", "Created 12 states in 1967", "Promulgated the 1963 constitution", "Assassinated in a car"),
            ("General Sani Abacha (November 1993 - June 1998)", "Dismantled the Interim National Government of Ernest Shonekan; established the Provisional Ruling Council, created 6 states (to 36 states), formed the PTF, but faced intense international sanctions over the execution of the Ogoni 9", "Handed over power in 1979", "Abolished the military completely", "Moved capital to Calabar")
        ]
        for mr_name, mr_bio, d1, d2, d3 in military_regimes:
            q_text = f"Which historical accomplishments and controversies characterize the regime of '{mr_name}'?"
            opts = {"A": mr_bio, "B": d1, "C": d2, "D": d3}
            items.append((
                "Military Regimes in Nigerian Political History", q_text, opts, "A",
                f"{mr_name}: {mr_bio}.",
                "Match the Nigerian military ruler to his landmark decrees, policies, and tenure events."
            ))

        # International organizations: AU, UN, Commonwealth
        int_bodies = [
            ("African Union (AU, transitioned from OAU in Durban 2002)", "Pan-African continental body advancing political and economic integration, democracy, peace, and security through the Peace and Security Council and APRM", "European economic union", "Military alliance with the United States", "Barter trade club for oil nations"),
            ("United Nations Security Council", "Comprises 5 permanent veto-wielding members (USA, UK, France, Russia, China) and 10 non-permanent members elected for two-year terms, holding primary responsibility for international peace and security", "Has 50 permanent members", "Composed only of African states", "Has zero veto powers"),
            ("Commonwealth of Nations", "Voluntary association of 56 sovereign member nations, mostly former territories of the British Empire, promoting democracy, human rights, rule of law, and free trade", "A military defense pact led by NATO", "An organization of OPEC oil exporters", "A political union with single parliament in London"),
            ("International Court of Justice (ICJ, The Hague) 2002 Bakassi Ruling", "Adjudicated the territorial dispute between Nigeria and Cameroon, ceding sovereignty over the oil-rich Bakassi Peninsula to Cameroon based on the 1913 Anglo-German treaty", "Awarded Bakassi permanently to Nigeria", "Ordered military invasion of Cameroon", "Dismissed the case without judgment")
        ]
        for ib_name, ib_desc, d1, d2, d3 in int_bodies:
            q_text = f"What is the institutional profile and international role of the '{ib_name}'?"
            opts = {"A": ib_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "International Organizations: AU, UN & Commonwealth", q_text, opts, "A",
                f"{ib_name}: {ib_desc}.",
                "Distinguish mandates of the African Union, UN Security Council, Commonwealth, and ICJ."
            ))

def append_exhaustive_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        # Political ideologies
        ideologies = [
            ("Socialism", "Advocates collective state ownership and democratic administration of the means of production, distribution, and exchange to ensure egalitarian social equity", "Private ownership of all factories", "Rule by hereditary kings", "Rule by the military"),
            ("Communism (Karl Marx and Friedrich Engels)", "A theoretical classless, stateless, and moneyless society based on common ownership where resources are distributed 'from each according to ability, to each according to need'", "Monopoly capitalism", "Absolute theocracy", "Feudal landlordism"),
            ("Fascism (Benito Mussolini in Italy)", "An extreme right-wing authoritarian, ultra-nationalist political ideology characterized by dictatorial power, forcible suppression of opposition, and state subordination of individual liberties", "Direct democracy", "Pacifist communalism", "Laissez-faire capitalism"),
            ("Feudalism", "A medieval socio-political system based on land tenure where monarchs granted fiefs of land to noble lords in exchange for military service, while serfs worked the land", "Universal adult suffrage", "Modern industrial democracy", "Rule by urban factory workers"),
            ("Theocracy", "A form of government in which sovereign political authority is held by religious clerics or divinely guided leaders claiming to rule according to divine law (e.g. Vatican City, Iran)", "Secular democracy", "Atheist military junta", "Feudal oligarchy")
        ]
        for id_name, id_desc, d1, d2, d3 in ideologies:
            q_text = f"Which political ideology is defined as: '{id_desc}'?"
            opts = {"A": id_name, "B": d1, "C": d2, "D": d3}
            items.append((
                "Comparative Political Ideologies", q_text, opts, "A",
                f"This definition describes {id_name}.",
                "Examine ownership of production factors, state power concentration, and societal goals."
            ))

        # Citizenship modes
        citizenship = [
            ("Citizenship by Birth (Jus soli and Jus sanguinis)", "Acquired automatically at birth by being born on national territory (jus soli) or born to citizen parents anywhere (jus sanguinis)", "Purchased with money", "Given by military decree", "Conferred after passing an exam"),
            ("Citizenship by Naturalization", "Conferred upon an alien foreigner who has fulfilled statutory constitutional conditions (continuous residency, good character, oath of allegiance)", "Acquired automatically at birth", "Reserved for ambassadors", "Purchased on stock market"),
            ("Citizenship by Registration", "Conferred upon a foreign woman legally married to a citizen of the country or upon a foreign-born person whose grandparents were citizens", "Acquired through military service", "Conferred by university degree", "Awarded by court jury"),
            ("Deprivation / Revocation of Citizenship", "A naturalized citizen can be constitutionally stripped of citizenship for acts of treason, trading with enemy states during war, or imprisonment for felony within 5-7 years", "Cannot ever be revoked", "Revoked for being late to work", "Revoked for changing religion")
        ]
        for cz_title, cz_desc, d1, d2, d3 in citizenship:
            q_text = f"Under constitutional jurisprudence, what governs {cz_title.lower()}?"
            opts = {"A": cz_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Modes of Acquisition & Deprivation of Citizenship", q_text, opts, "A",
                f"{cz_title}: {cz_desc}.",
                "Distinguish between citizenship by birth, registration, and statutory naturalization."
            ))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        # Amalgamation of 1914
        amal = [
            ("1914 Amalgamation of Northern and Southern Nigeria by Lord Lugard", "United the Northern and Southern protectorates primarily to use the prosperous Southern customs revenue surplus to offset the Northern railroad budget deficit", "Granted political independence to Nigeria", "Created the three regions", "Abolished indirect rule"),
            ("Governor-General of Nigeria immediately following the 1914 Amalgamation", "Sir Frederick Lugard (later Lord Lugard)", "Sir Donald Cameron", "Sir Arthur Richards", "Sir John Macpherson"),
            ("Clifford Constitution 1922 Franchise Requirements", "Restricted suffrage to adult male British subjects or protected persons earning a minimum taxable annual income of £100 with 12 months continuous residency", "Universal adult suffrage for all women and men", "Only university graduates", "Only traditional chiefs")
        ]
        for am_t, am_d, d1, d2, d3 in amal:
            q_text = f"What historical fact describes the {am_t.lower()}?"
            opts = {"A": am_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "1914 Amalgamation & Early Colonial Administration", q_text, opts, "A",
                f"{am_t}: {am_d}.",
                "Recall economic rationale of 1914 amalgamation and Clifford franchise restrictions."
            ))

        # Early political parties
        early_parties = [
            ("Nigerian National Democratic Party (NNDP, founded 1923)", "Founded by Herbert Macaulay following the Clifford Constitution; dominated elective seats in the Lagos Town Council and Legislative Council throughout the 1920s", "Founded by Obafemi Awolowo", "A northern Islamic party", "Formed to fight in World War II"),
            ("Nigerian Youth Movement (NYM, founded 1934)", "Founded by Ernest Ikoli, Samuel Akinsanya, and Dr. J.C. Vaughan (joined by Azikiwe and Awolowo); broke the NNDP's electoral monopoly in Lagos in 1938", "A military council", "A colonial British party", "A trade union of dockworkers"),
            ("National Council of Nigeria and the Cameroons (NCNC, founded 1944)", "First genuine nationwide political party founded by Herbert Macaulay (President) and Nnamdi Azikiwe (Secretary); spearheaded anti-Richards constitution protests", "Founded exclusively for northern emirs", "Founded in London by British MPs", "A religious missionary movement"),
            ("Action Group (AG, founded 1951)", "Emerged from the Yoruba cultural organization Egbe Omo Oduduwa under the leadership of Chief Obafemi Awolowo; formed the first regional government of Western Nigeria", "Founded by Herbert Macaulay in 1923", "Founded in Kano by Aminu Kano", "Formed to oppose Nigerian federalism"),
            ("Northern People's Congress (NPC, founded 1951)", "Evolved from the cultural group Jam'iyyar Mutanen Arewa under the leadership of Dr. R.A. Dikko, Sir Ahmadu Bello, and Sir Abubakar Tafawa Balewa, dominating Northern politics", "A southern radical party", "A labor union of railway workers", "Led by Nnamdi Azikiwe")
        ]
        for p_name, p_hist, d1, d2, d3 in early_parties:
            q_text = f"Which historical milestone is linked to the {p_name}?"
            opts = {"A": p_hist, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pioneering Political Parties in Colonial Nigeria", q_text, opts, "A",
                f"{p_name}: {p_hist}.",
                "Identify party founders, regional strongholds, and historical origins."
            ))

    elif topic == "Nigerian Constitutional Development":
        # Exclusive list subjects
        exclusive_items = [
            ("Currency, coinage, and legal tender", "Exclusive Legislative List (Federal National Assembly only)", "Concurrent Legislative List", "Residual List (States only)", "Local Government Council only"),
            ("National defense, armed forces, and military operations", "Exclusive Legislative List", "Concurrent Legislative List", "Residual List", "Customary Courts"),
            ("Foreign affairs, international diplomacy, and extradition treaties", "Exclusive Legislative List", "Concurrent Legislative List", "Residual List", "State High Courts"),
            ("Aviation, safety of aircraft, and international airports", "Exclusive Legislative List", "Concurrent Legislative List", "Residual List", "Local Governments"),
            ("Citizenship, naturalization, and alien immigration", "Exclusive Legislative List", "Concurrent Legislative List", "Residual List", "Regional Chiefs"),
            ("Customs and excise tariffs on imported and exported goods", "Exclusive Legislative List", "Concurrent Legislative List", "Residual List", "Town Council")
        ]
        for subj_m, leg_ans, d1, d2, d3 in exclusive_items:
            q_text = f"Under the 1999 Nigerian Constitution, on which legislative list is '{subj_m}' placed?"
            opts = {"A": leg_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Exclusive Legislative Powers of the Federal Government", q_text, opts, "A",
                f"'{subj_m}' is placed on the {leg_ans}.",
                "Remember that defense, diplomacy, currency, customs, and aviation belong solely to the federal tier."
            ))

        # Concurrent list subjects
        concurrent_items = [
            ("Establishment of universities, polytechnics, and tertiary educational institutions", "Concurrent Legislative List (both Federal and State governments can establish)", "Exclusive List only", "Residual List only", "Chieftaincy council"),
            ("Promotion of agricultural development and agricultural research institutes", "Concurrent Legislative List", "Exclusive List only", "Residual List only", "Customary court"),
            ("Industrial and commercial development facilities", "Concurrent Legislative List", "Exclusive List only", "Residual List only", "Traditional rulers"),
            ("Public health, hospitals, and clinics", "Concurrent Legislative List", "Exclusive List only", "Residual List only", "Ministry of Defense only")
        ]
        for c_subj, c_ans, d1, d2, d3 in concurrent_items:
            q_text = f"On which legislative list is '{c_subj}' constitutionally categorized in Nigeria?"
            opts = {"A": c_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Concurrent Legislative Powers in Nigerian Federalism", q_text, opts, "A",
                f"'{c_subj}' belongs to the {c_ans}.",
                "Both federal and state governments have competence in tertiary education, health, and agriculture."
            ))

        # Chapter IV Fundamental Human Rights
        human_rights = [
            ("Section 33 of the 1999 Constitution", "Right to Life (no one shall be intentionally deprived of life save in execution of a court sentence for a criminal offence)", "Right to freedom of speech", "Right to acquire property", "Right to strike"),
            ("Section 34 of the 1999 Constitution", "Right to Dignity of the Human Person (freedom from torture, cruel/inhuman treatment, and slavery/forced labor)", "Right to vote in elections", "Right to free passport", "Right to bail"),
            ("Section 35 of the 1999 Constitution", "Right to Personal Liberty (freedom from arbitrary arrest, unlawful detention, and entitlement to be brought to court within 24-48 hours)", "Right to own land", "Right to marry", "Right to free medical care"),
            ("Section 36 of the 1999 Constitution", "Right to Fair Hearing (determination of civil rights or criminal charges by an independent, impartial court within a reasonable time)", "Right to free housing", "Right to free water", "Right to create a bank")
        ]
        for sec_t, sec_d, d1, d2, d3 in human_rights:
            q_text = f"What fundamental human right is guaranteed under {sec_t}?"
            opts = {"A": sec_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Constitutional Fundamental Human Rights (Chapter IV)", q_text, opts, "A",
                f"{sec_t}: {sec_d}.",
                "Recall key sections of Chapter IV: Sec 33 (Life), Sec 34 (Dignity), Sec 35 (Liberty), Sec 36 (Fair Hearing)."
            ))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        # Revenue allocation principles
        rev_principles = [
            ("Principle of Derivation in revenue allocation", "A percentage proportion of federally collected mineral or commodity revenues is allocated directly back to the specific states/regions from which the resources were extracted", "Equal sharing to all 36 states", "Sharing according to total school enrollment", "Giving all money to the federal capital"),
            ("Principle of Equality of States", "A component of the federal revenue allocation formula distributed in mathematically equal shares to all 36 states regardless of population or size", "Allocated by landmass only", "Allocated by oil barrels produced", "Distributed by bank size"),
            ("Principle of Population in revenue sharing", "Allocating a significant portion of the federation account in direct proportion to the certified demographic census population of each state", "Allocated to the state with smallest population", "Allocated equally to all", "Shared only among emirs"),
            ("Revenue Mobilization Allocation and Fiscal Commission (RMAFC)", "Permanent constitutional body established to monitor federal revenue accruals and prescribe equitable revenue allocation formulas for the three tiers of government", "A private commercial bank", "An international oil trading company", "A military tribunal")
        ]
        for rp_name, rp_desc, d1, d2, d3 in rev_principles:
            q_text = f"In Nigerian fiscal federalism, how is the '{rp_name}' defined?"
            opts = {"A": rp_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Fiscal Federalism & Revenue Allocation Principles", q_text, opts, "A",
                f"{rp_name}: {rp_desc}.",
                "Distinguish between derivation, equality of states, population, and the mandate of RMAFC."
            ))

        # Coup events
        coup_events = [
            ("The January 15, 1966 Military Coup ('Operation Damisa')", "Nigeria's first military coup led by Major Chukwuma Kaduna Nzeogwu and four other majors; assassinated Prime Minister Tafawa Balewa, Premier Ahmadu Bello, and Premier Ladoke Akintola", "Overthrew General Gowon", "Handed over to civilians", "Created 36 states"),
            ("The July 29, 1966 Counter-Coup", "Northern officers assassinated Major-General Aguiyi-Ironsi and Western military governor Lt. Col. Adekunle Fajuyi in Ibadan, installing Lt. Col. Yakubu Gowon as Head of State", "Abolished the military", "Promulgated the 1979 constitution", "Created the NNDP"),
            ("The February 13, 1976 Abortive Coup", "Attempted coup led by Lt. Col. Buka Suka Dimka that ambushed and assassinated Head of State General Murtala Ramat Mohammed in Lagos; General Olusegun Obasanjo assumed power", "Overthrew Shehu Shagari", "Annulled the June 12 election", "Started the Nigerian civil war"),
            ("The June 12, 1993 Presidential Election", "Widely recognized as the freest and fairest election in Nigerian history, won by Chief Moshood Kashimawo Olawale (M.K.O.) Abiola of the SDP, but annulled by General Ibrahim Babangida", "Won by Shehu Shagari", "Won by Olusegun Obasanjo", "Held under the Clifford constitution")
        ]
        for c_t, c_d, d1, d2, d3 in coup_events:
            q_text = f"What occurred during the historical event '{c_t}'?"
            opts = {"A": c_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Landmark Military Coups & Political Crises in Nigeria", q_text, opts, "A",
                f"{c_t}: {c_d}.",
                "Chronicle major military coups, assassinations, and the June 12 annulment."
            ))

def append_master_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        # Unicameral vs Bicameral legislature
        leg_types = [
            ("Advantage of a Bicameral Legislature", "Prevents hasty, ill-considered legislation by subjecting bills to second-chamber scrutiny, and ensures equal representation for federating states in a federation", "Extremely cheap to maintain", "Passes laws within 10 minutes", "Abolishes all executive vetoes"),
            ("Advantage of a Unicameral Legislature", "Cheaper and more economical to run, avoiding legislative gridlocks, duplication of personnel, and unnecessary bureaucratic delays", "Guarantees state equality in a federation", "Provides two chambers of debate", "Allows two presidents"),
            ("Bicameral legislative deadlocks", "A constitutional stalemate where both houses disagree on bill amendments; resolved through a Joint Conference Harmonization Committee or joint sitting", "The military dissolves parliament", "The Chief Justice votes", "The bill is burned")
        ]
        for lt_t, lt_d, d1, d2, d3 in leg_types:
            q_text = f"In legislative institutional design, what describes the {lt_t.lower()}?"
            opts = {"A": lt_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Legislative Structure: Unicameral vs Bicameralism", q_text, opts, "A",
                f"{lt_t}: {lt_d}.",
                "Contrast single-chamber efficiency with dual-chamber scrutiny and federal representation."
            ))

        # Types of elections
        elections = [
            ("General Election", "A nationwide election held at regular statutory intervals in which all or most members of the national political legislature and executive are chosen", "Election to fill a dead senator's seat", "Internal voting in a club", "Military appointment"),
            ("Bye-Election", "An election held to fill a single vacant legislative or local council seat caused by the death, resignation, or disqualification of an incumbent member", "Nationwide presidential poll", "Election across all 36 states", "Voting for a new pope"),
            ("Primary Election", "An internal election conducted by registered members of a political party to choose their party's official candidate for a general election", "Inter-party national voting", "General presidential election", "Referendum on the constitution"),
            ("Referendum", "A direct popular vote in which the entire electorate is invited to vote 'Yes' or 'No' on a specific public policy, statute, or constitutional amendment", "Voting for a political party", "Choosing a local councilor", "Appointing a judge"),
            ("Plebiscite", "A direct vote of the qualified electorate on an important sovereign political question, such as national boundary redrawing or self-determination (e.g. 1961 Northern Cameroons plebiscite)", "Annual budget vote", "Election of parliament speaker", "Internal party dispute")
        ]
        for el_name, el_desc, d1, d2, d3 in elections:
            q_text = f"Which electoral process is defined as a '{el_name}'?"
            opts = {"A": el_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Types of Elections & Plebiscites", q_text, opts, "A",
                f"{el_name}: {el_desc}.",
                "Distinguish general, bye, primary elections, referendums, and plebiscites."
            ))

        # Checks and balances mechanisms
        checks = [
            ("Executive Veto Override by the Legislature", "Under Section 58 of the 1999 Constitution, the National Assembly can override a presidential veto by passing the bill again with a two-thirds majority in both chambers", "By a simple majority in Senate", "By petitioning the Chief Justice", "By military intervention"),
            ("Legislative Confirmation of Executive Appointments", "The constitutional requirement that the President's nominations for Federal Ministers, Ambassadors, and Supreme Court Justices must be screened and confirmed by the Senate", "Confirmed by the police", "Approved by civil service", "Decided by traditional rulers"),
            ("Impeachment of the President under the 1999 Constitution (Section 143)", "Notice of gross misconduct signed by at least one-third of all members of the National Assembly, investigated by an independent 7-man panel, and adopted by a two-thirds majority of each chamber", "Simple majority of the House of Reps", "A court judgment by a magistrate", "A military decree")
        ]
        for ch_name, ch_desc, d1, d2, d3 in checks:
            q_text = f"Under Nigerian constitutional law, what procedural mechanism governs the {ch_name.lower()}?"
            opts = {"A": ch_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Checks and Balances Mechanisms in Governance", q_text, opts, "A",
                f"{ch_name}: {ch_desc}.",
                "Recall two-thirds legislative majority requirements and independent panel investigations."
            ))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        # Pre-colonial kingdoms: Benin, Borno, Nupe
        other_kingdoms = [
            ("Pre-colonial Benin Kingdom administration", "Monarchical autocracy ruled by the Oba of Benin assisted by the Uzama (council of seven hereditary kingmakers) and town chiefs (Eghaevbo n'Ore led by the Iyase)", "Rule by an Islamic Emir and Waziri", "Stateless acephalous age grades", "British district commissioners"),
            ("Pre-colonial Kanem-Borno Empire administration", "Ruled by the Mai (hereditary king), assisted by an imperial state council of 12 nobles including the Kaigama (commander of army) and Magira (queen mother)", "Oyomesi council of 7", "Warrant chiefs", "Ama-ala village democracy"),
            ("Pre-colonial Tiv political organization", "A strictly egalitarian segmentary lineage system lacking centralized kingship; family heads (Orya) settled local disputes until the British created the Tor Tiv office in 1946", "Centralized Sultanate", "Absolute monarchy with standing army", "Caliphate with Sharia judges"),
            ("Pre-colonial Itsekiri Kingdom political structure", "Centralized maritime kingdom ruled by the Olu of Warri, assisted by an advisory royal council of Ologbotsere (Prime Minister) and Iyatsere (Warlord)", "Decentralized age grade democracy", "Emirate with Alkali courts", "Unitary state with governor")
        ]
        for k_name, k_desc, d1, d2, d3 in other_kingdoms:
            q_text = f"Which governance framework accurately describes the {k_name}?"
            opts = {"A": k_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Comparative Pre-Colonial Nigerian Systems", q_text, opts, "A",
                f"{k_name}: {k_desc}.",
                "Identify royal councils, kingmakers, and lineage structures in Benin, Borno, Tiv, and Itsekiri."
            ))

        # Colonial conferences leading to independence
        conferences = [
            ("1950 Ibadan General Constitutional Conference", "Landmark national conference bringing northern and southern delegates together; Northern delegates demanded and secured 50% representation in the central legislature", "Granted independence immediately", "Abolished the three regions", "Adopted a unitary system"),
            ("1953 London Constitutional Conference (chaired by Oliver Lyttelton)", "Convened following the constitutional breakdown caused by the 1953 self-government motion; agreed that Nigeria should formally become a federal state with regional autonomy", "Created 12 states", "Adopted an executive president", "Severed all ties with Britain"),
            ("1957 London Constitutional Conference", "Granted internal self-government to the Eastern and Western regions, created the office of Federal Prime Minister (conferred on Balewa), and established the Minorities Commission", "Granted self-government to the North", "Abolished the regional civil service", "Promulgated the 1999 constitution"),
            ("1958 London Constitutional Conference", "Agreed to grant internal self-government to Northern Nigeria in 1959, incorporated Fundamental Human Rights into the constitution, and fixed Nigeria's independence for October 1, 1960", "Abolished the elective principle", "Created 19 states", "Adopted the American constitution")
        ]
        for conf_n, conf_d, d1, d2, d3 in conferences:
            q_text = f"What historic constitutional agreement was reached at the {conf_n}?"
            opts = {"A": conf_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pre-Independence Constitutional Conferences", q_text, opts, "A",
                f"{conf_n}: {conf_d}.",
                "Track agreements from 1950 Ibadan to 1953/1954 federalism and 1957/1958 independence dates."
            ))

        # Colonial administrative hierarchy
        col_hierarchy = [
            ("Secretary of State for the Colonies (based in London)", "British cabinet minister with overall political and executive responsibility for all colonies across the British Empire", "Colonial resident in Kano", "District officer in Owerri", "Village warrant chief"),
            ("Governor / Governor-General of Nigeria", "The supreme British representative on Nigerian soil, appointed by the British Crown and exercising immense executive and legislative veto powers", "Leader of the Nigerian Bar", "Elected Prime Minister", "Chief justice of the colony"),
            ("Colonial Resident (Provincial level)", "British administrative officer in charge of a province (e.g. Kano, Sokoto, Calabar), supervising traditional rulers and advising native authorities", "District messenger", "Village school head", "Supreme court judge"),
            ("District Officer (DO, Division level)", "Field administrative officer directly supervising Native Courts, collecting direct taxes, and implementing colonial policy at the grassroots district level", "Cabinet minister in London", "High commissioner", "Crown prosecutor")
        ]
        for h_title, h_desc, d1, d2, d3 in col_hierarchy:
            q_text = f"In the British colonial administrative bureaucracy in Nigeria, what was the function of the '{h_title}'?"
            opts = {"A": h_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "British Colonial Administrative Hierarchy", q_text, opts, "A",
                f"{h_title}: {h_desc}.",
                "Trace administrative authority from London Secretary of State to Governor, Resident, and District Officer."
            ))

    elif topic == "Nigerian Constitutional Development":
        # Constitutional amendment procedure
        amend_q = [
            ("Procedure for amending the 1999 Nigerian Constitution (Section 9)", "Proposal must be supported by a two-thirds majority of all members in both the Senate and House of Representatives, and approved by resolutions of at least two-thirds of all State Houses of Assembly (24 states)", "Simple majority of the Senate only", "Signature of the President alone", "A military council decree"),
            ("Procedure for altering Section 9 or creating new states under the 1999 Constitution", "Requires an extraordinary four-fifths (80%) majority of all members in both the Senate and House of Representatives, plus approval by two-thirds of State Assemblies", "Simple majority of 50%", "Decision of the Chief Justice", "A proclamation by state governors"),
            ("Code of Conduct Bureau and Tribunal", "Statutory constitutional body mandated to enforce public morality, asset declaration, and integrity among public officers, preventing conflicts of interest", "A police special squad", "A military secret court", "An agency that prints textbooks")
        ]
        for aq_title, aq_desc, d1, d2, d3 in amend_q:
            q_text = f"Under Nigerian constitutional provisions, how is {aq_title.lower()} executed?"
            opts = {"A": aq_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Constitutional Amendment & Integrity Institutions", q_text, opts, "A",
                f"{aq_title}: {aq_desc}.",
                "Understand super-majority thresholds (2/3 and 4/5) and the role of Code of Conduct institutions."
            ))

        # Federal Character Commission
        fcc_items = [
            ("Federal Character Principle (Section 14(3) of the 1999 Constitution)", "Directs that public appointments, bureaucratic positions, and armed forces command must reflect the diverse linguistic, ethnic, and regional character of Nigeria to prevent domination by one group", "Gives all jobs to the richest citizens", "Requires all ministers to speak English only", "Abolishes states"),
            ("Federal Character Commission (FCC)", "Autonomous constitutional body established to enforce compliance with proportional ethnic and regional equity in public appointments across federal ministries and agencies", "An electoral polling agency", "A criminal investigation bureau", "A tax collection service"),
            ("National Judicial Council (NJC)", "Independent constitutional body responsible for recommending the appointment and discipline of judicial officers (judges) to the President and Governors, safeguarding judicial independence", "The ministry of justice", "A military tribunal", "An association of private lawyers")
        ]
        for fcc_t, fcc_d, d1, d2, d3 in fcc_items:
            q_text = f"What is the constitutional purpose of the '{fcc_t}'?"
            opts = {"A": fcc_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Federal Character & Judicial Governance Bodies", q_text, opts, "A",
                f"{fcc_t}: {fcc_d}.",
                "Analyze national integration mechanisms and judicial independence under the NJC."
            ))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        # Revenue allocation commissions
        rev_commissions = [
            ("Phillipson Commission of 1946", "First formal revenue allocation commission in Nigeria; recommended Derivation and Even Progress as principles for sharing colonial revenues between the three regions", "Recommended 100% population sharing", "Abolished the derivation principle", "Created the Value Added Tax"),
            ("Chick Commission of 1953", "Recommended maximum 100% adherence to the Principle of Derivation for regional revenue allocation, greatly enriching the agricultural export-rich Western and Northern regions", "Abolished derivation completely", "Allocated all money to the central federal government", "Introduced equal sharing for all states"),
            ("Raisman Commission of 1958", "Created the landmark Distributable Pool Account (DPA); reduced derivation to 50% and allocated the remaining 50% to the DPA to be shared based on regional population and balanced development", "Created the Central Bank", "Gave all money to oil companies", "Recommended 100% derivation"),
            ("Okigbo Presidential Commission on Revenue Allocation (1980)", "Recommended vertical allocation formula: 53% to Federal Government, 30% to State Governments, 10% to Local Governments, and 7% to Special Funds", "Recommended 100% to states", "Abolished local government funding", "Gave all oil revenues to Abuja only")
        ]
        for rc_name, rc_desc, d1, d2, d3 in rev_commissions:
            q_text = f"What revenue allocation formula or principle was recommended by the '{rc_name}'?"
            opts = {"A": rc_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Historical Revenue Allocation Commissions in Nigeria", q_text, opts, "A",
                f"{rc_name}: {rc_desc}.",
                "Trace evolution from Phillipson (1946) to Chick (1953), Raisman (1958), and Okigbo (1980)."
            ))

        # Minorities Willink Commission
        willink = [
            ("Henry Willink Commission of 1958 (Commission to Enquire into the Fears of Minorities)", "Established following ethnic minority agitations; refused to create new separate regions for minorities, recommending instead a chapter on Fundamental Human Rights and the Niger Delta Development Board", "Created 12 new states immediately", "Abolished the three major regions", "Expelled minorities from Nigeria"),
            ("Major minority state demands investigated by the 1958 Willink Commission", "Calabar-Ogoja-Rivers (COR) state from Eastern Region, Mid-West state from Western Region, and Middle Belt state from Northern Region", "Demand to merge Nigeria with Ghana", "Demand to return to British rule", "Demand for a military government")
        ]
        for w_t, w_d, d1, d2, d3 in willink:
            q_text = f"What historical finding is associated with the '{w_t}'?"
            opts = {"A": w_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ethnic Minorities Agitation & The Willink Commission", q_text, opts, "A",
                f"{w_t}: {w_d}.",
                "Understand why the Willink Commission recommended a Bill of Rights rather than state creation."
            ))

        # Peacekeeping missions
        peacekeeping = [
            ("Nigeria's UN Peacekeeping mission in Congo (ONUC, 1960-1964)", "Nigeria's historic first UN peacekeeping mission, commanded with distinction by Major-General J.T.U. Aguiyi-Ironsi during the Congo crisis", "A colonial British war", "An invasion of South Africa", "A border dispute with Chad"),
            ("ECOMOG operations in Liberia (1990-1997)", "Nigeria committed massive troops, funds, and air support under Generals Arnold Quainoo, Joshua Dogonyaro, and Tunji Olurin to halt the Liberian Civil War and protect civilians", "A NATO peacekeeping mission", "A European Union military intervention", "A French foreign legion operation"),
            ("ECOMOG operations in Sierra Leone (1997-1998)", "Nigeria-led regional troops reversed the military coup of Johnny Paul Koroma and restored the democratically elected government of President Ahmad Tejan Kabbah", "An invasion of Ghana", "A UN operation in Asia", "A joint border exercise with Niger"),
            ("Nigeria's historic role in the founding of the Organization of African Unity (OAU, 1963)", "Sir Abubakar Tafawa Balewa championed the moderate Monrovia Group principles, reconciling with the radical Casablanca Group to establish the OAU in Addis Ababa", "Nigeria refused to attend the conference", "Nigeria demanded immediate continental government", "Nigeria advocated military alignment with the USSR")
        ]
        for pk_name, pk_desc, d1, d2, d3 in peacekeeping:
            q_text = f"In Nigerian diplomatic and military history, what was the significance of the '{pk_name}'?"
            opts = {"A": pk_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Nigerian Military Peacekeeping & Diplomatic Leadership", q_text, opts, "A",
                f"{pk_name}: {pk_desc}.",
                "Identify Nigeria's prominent contributions to UN peacekeeping and West African ECOMOG operations."
            ))


def append_ultimate_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        philosophers = [
            ("Thomas Hobbes (Leviathan, 1651)", "Argued that life in the pre-political state of nature was solitary, poor, nasty, brutish, and short, necessitating an absolute sovereign to maintain order", "Advocated direct democracy", "Supported overthrow of all kings", "Argued that state is unnecessary"),
            ("John Locke (Two Treatises of Government, 1689)", "Father of classical liberalism; argued that government exists solely to protect natural inalienable rights to Life, Liberty, and Property, with right of revolution if breached", "Supported absolute royal tyranny", "Argued against private property", "Opposed written constitutions"),
            ("Jean-Jacques Rousseau (The Social Contract, 1762)", "Proclaimed that Man is born free, and everywhere he is in chains; sovereignty resides irrevocably in the collective General Will of the people", "Advocated military dictatorship", "Supported British colonial rule", "Argued that kings are gods"),
            ("Niccolo Machiavelli (The Prince, 1532)", "Realist political philosopher asserting that political rulers must prioritize state survival and power retention above moral scruples (the ends justify the means)", "Advocated Christian pacifism", "Argued that citizens should rule directly", "Supported communist equality"),
            ("Karl Marx and Friedrich Engels (Communist Manifesto, 1848)", "Posited that human history is the history of class struggles between the exploiting bourgeoisie and exploited proletariat, culminating in a proletarian revolution", "Defended free-market capitalism", "Supported feudal monarchies", "Opposed labor unions")
        ]
        for phil_name, phil_idea, d1, d2, d3 in philosophers:
            q_text = f"Which monumental political thesis was articulated by {phil_name}?"
            opts = {"A": phil_idea, "B": d1, "C": d2, "D": d3}
            items.append(("Classical Political Philosophers & Theories", q_text, opts, "A", f"{phil_name}: {phil_idea}.", "Match the political philosopher to their seminal text and philosophical doctrine."))

        aristocracy_forms = [
            ("Aristocracy", "Government rule by the best-born hereditary nobility or privileged upper social class", "Rule by the worst criminals", "Rule by the richest billionaires only", "Direct rule by factory workers"),
            ("Plutocracy", "A system of government dominated, controlled, or ruled exclusively by the wealthiest economic class", "Rule by hereditary royal princes", "Rule by religious priests", "Rule by military generals"),
            ("Ochlocracy (Mobocracy)", "Government by the mob, characterized by mass disorder, demagoguery, and violent popular passion", "Constitutional democracy", "Rule by supreme court judges", "Feudal tenure"),
            ("Gerontocracy", "A political system where leadership and decision-making authority are vested exclusively in the oldest elder members of society", "Rule by the youth", "Rule by women only", "Rule by foreign ambassadors"),
            ("Meritocracy", "A system where political advancement, offices, and appointments are awarded strictly based on demonstrated intellectual ability, skill, and competence", "Rule by hereditary birth", "Rule by bribery", "Rule by lottery")
        ]
        for ar_name, ar_desc, d1, d2, d3 in aristocracy_forms:
            q_text = f"Which form of government is defined as: {ar_desc}?"
            opts = {"A": ar_name, "B": d1, "C": d2, "D": d3}
            items.append(("Forms of Governance & Rule Typology", q_text, opts, "A", f"This definition describes {ar_name}.", "Examine who holds sovereign power in each governmental classification."))

        lg_reforms = [
            ("1976 Local Government Reforms in Nigeria", "Introduced a uniform single-tier multi-purpose local government system nationwide, recognized local councils as the third tier of government, and established statutory federal funding allocations", "Abolished local governments completely", "Subordinated councils to traditional emirs only", "Made council positions military commands"),
            ("Exclusive / Mandatory Functions of Local Governments (Fourth Schedule, 1999 Constitution)", "Collection of rates/radio/television licenses, establishment and maintenance of cemeteries/burial grounds, licensing of bicycles/carts, and naming of streets", "Maintenance of national armed forces", "Printing of naira banknotes", "Conducting foreign diplomacy"),
            ("Concurrent functions of Local Governments in Nigeria", "Participating in the provision and maintenance of primary, adult, and vocational education, and development of agriculture and health services", "Control of federal trunk roads", "Regulation of commercial aviation", "Customs and excise collection")
        ]
        for lg_t, lg_d, d1, d2, d3 in lg_reforms:
            q_text = f"Under Nigerian local government administration, what characterizes the {lg_t.lower()}?"
            opts = {"A": lg_d, "B": d1, "C": d2, "D": d3}
            items.append(("Local Government Administration & 1976 Reforms", q_text, opts, "A", f"{lg_t}: {lg_d}.", "Recall Fourth Schedule exclusive council duties versus concurrent social responsibilities."))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        governors = [
            ("Sir Hugh Clifford (1919-1925)", "Replaced Lugard; introduced the 1922 Clifford Constitution establishing the elective principle for 4 legislative seats (3 Lagos, 1 Calabar)", "Created the 12 states in 1967", "Amalgamated Nigeria in 1914", "Promulgated the 1979 constitution"),
            ("Sir Arthur Richards (1943-1948)", "Promulgated the 1946 Richards Constitution introducing regionalism by creating Northern, Western, and Eastern regions and regional assemblies", "Introduced the elective principle in 1922", "Handed over independence in 1960", "Amalgamated Nigeria"),
            ("Sir John Macpherson (1948-1955)", "Initiated the 1951 Macpherson Constitution featuring unprecedented grassroots consultation from village to national levels and establishing a Council of Ministers", "Introduced the Richards regionalism", "Abolished the regional councils", "Executed the 1914 amalgamation"),
            ("Sir James Robertson (1955-1960)", "The final British colonial Governor-General who oversaw the 1957/1958 constitutional conferences and presided over Nigeria formal independence on October 1, 1960", "First colonial governor in 1914", "Introduced the elective principle", "Promulgated Decree 34")
        ]
        for gov_n, gov_d, d1, d2, d3 in governors:
            q_text = f"What was the monumental colonial policy achievement of Governor {gov_n} in Nigeria?"
            opts = {"A": gov_d, "B": d1, "C": d2, "D": d3}
            items.append(("British Colonial Governors in Nigerian History", q_text, opts, "A", f"{gov_n}: {gov_d}.", "Associate British colonial governors with their respective landmark constitutional promulgations."))

        newspapers = [
            ("West African Pilot (founded in Lagos, 1937)", "Founded by Dr. Nnamdi Azikiwe with the historic motto Show the light and the people will find the way; served as the spearhead of militant anti-colonial nationalism", "A colonial government gazette", "A northern Islamic newspaper", "Founded by Lord Lugard"),
            ("Lagos Daily News (founded 1925)", "Founded and edited by Herbert Macaulay and Dr. J.C. Caulcrick, serving as the official media organ of the Nigerian National Democratic Party (NNDP)", "Founded by British governors", "A religious missionary magazine", "Published in London only"),
            ("Nigerian Tribune (founded in Ibadan, 1949)", "Founded by Chief Obafemi Awolowo to articulate progressive nationalist views, promote regional self-governance, and support the Action Group party", "Founded by Herbert Macaulay in 1923", "A French colonial newspaper", "An official publication of the Nigerian military")
        ]
        for np_name, np_desc, d1, d2, d3 in newspapers:
            q_text = f"In Nigerian nationalist history, what was the role and founder of the {np_name}?"
            opts = {"A": np_desc, "B": d1, "C": d2, "D": d3}
            items.append(("Nationalist Print Media & Anti-Colonial Press", q_text, opts, "A", f"{np_name}: {np_desc}.", "Recognize the role of the indigenous press in mobilizing anti-colonial resistance."))

    elif topic == "Nigerian Constitutional Development":
        const_1979 = [
            ("Constitution Drafting Committee (CDC) of 1975 (The 49 Wise Men)", "Headed by Chief Rotimi Williams (SAN) to draft a new constitution for Nigeria; Chief Obafemi Awolowo famously declined to serve on the committee", "Headed by General Obasanjo", "Composed of 100 military officers", "Headed by Nnamdi Azikiwe"),
            ("Constituent Assembly of 1977-1978", "Presided over by Justice Udo Udoma; deliberated, amended, and ratified the draft constitution produced by the CDC, leading to the 1979 presidential constitution", "A military tribunal", "An electoral polling team", "A trade union conference"),
            ("Federal Electoral Commission (FEDECO, 1978-1983)", "Electoral management body chaired by Chief Michael Ani that registered 5 political parties (NPN, UPN, NPP, PRP, GNPP) and conducted the 1979 general elections", "INEC", "NECON", "Electoral Commission of Nigeria (ECN)"),
            ("The Five Registered Political Parties in the 1979 Second Republic", "National Party of Nigeria (NPN), Unity Party of Nigeria (UPN), Nigerian People Party (NPP), People Redemption Party (PRP), and Great Nigeria People Party (GNPP)", "SDP and NRC only", "APC and PDP only", "NNDP, NYM, and AG only")
        ]
        for c79_t, c79_d, d1, d2, d3 in const_1979:
            q_text = f"In the transition to the Nigerian Second Republic, what characterizes {c79_t}?"
            opts = {"A": c79_d, "B": d1, "C": d2, "D": d3}
            items.append(("1979 Second Republic Transition & Institutions", q_text, opts, "A", f"{c79_t}: {c79_d}.", "Identify key institutions: 49 Wise Men CDC, Udo Udoma Constituent Assembly, FEDECO, and the 5 political parties."))

        bill_stages = [
            ("First Reading of a Bill", "Formal introduction of the bill to the legislative chamber; the clerk reads the short title aloud and copies are distributed to legislators without debate", "Detailed line-by-line debate", "Presidential signature", "Public hearing across the country"),
            ("Second Reading of a Bill", "The sponsor of the bill explains its underlying principles, purpose, and philosophy, followed by extensive debate on the general merits of the bill", "Signing into law by the President", "Reading only the title without debate", "Immediate rejection by clerk"),
            ("Committee Stage of a Bill", "The bill is referred to a specialized standing or ad-hoc legislative committee for meticulous clause-by-clause scrutiny, public hearings, and expert testimony", "Immediate presidential veto", "Broadcast on national radio", "Voting by the general public"),
            ("Joint Conference Harmonization Committee", "Convened when the Senate and House of Representatives pass conflicting amendments on the same bill to reconcile differences before final passage", "A meeting with the Chief Justice", "A conference with military generals", "A dissolution of parliament")
        ]
        for bs_name, bs_desc, d1, d2, d3 in bill_stages:
            q_text = f"In parliamentary procedure, what occurs during the {bs_name} in the National Assembly?"
            opts = {"A": bs_desc, "B": d1, "C": d2, "D": d3}
            items.append(("Legislative Bill Passage Stages", q_text, opts, "A", f"{bs_name}: {bs_desc}.", "Trace a bill through First Reading, Second Reading debate, Committee scrutiny, and Joint Harmonization."))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        opec_details = [
            ("Nigeria accession to the Organization of the Petroleum Exporting Countries (OPEC)", "Joined OPEC in July 1971 as its 11th member country under the leadership of General Yakubu Gowon", "Joined in 1960 at independence", "Joined in 1999 under Obasanjo", "Joined in 1985 under Babangida"),
            ("Dr. Rilwanu Lukman historic role in OPEC", "Eminent Nigerian petroleum engineer who served with international distinction as OPEC Conference President for a record eight consecutive terms and later OPEC Secretary-General", "First military general of Nigeria", "Chief Justice of the Federation", "President of the United Nations General Assembly"),
            ("Primary economic objective of OPEC quotas on member nations", "Regulate aggregate global crude petroleum supply to prevent price collapses and secure stable, equitable export revenues for member countries", "Ban all oil drilling permanently", "Sell oil for free to Europe", "Nationalize all foreign banks")
        ]
        for op_t, op_d, d1, d2, d3 in opec_details:
            q_text = f"In Nigerian international energy diplomacy, what fact describes {op_t.lower()}?"
            opts = {"A": op_d, "B": d1, "C": d2, "D": d3}
            items.append(("OPEC & Nigerian Energy Diplomacy", q_text, opts, "A", f"{op_t}: {op_d}.", "Recall Nigeria OPEC entry in 1971 and Dr. Rilwanu Lukman diplomatic leadership."))

        ecowas_q = [
            ("Treaty of Lagos (May 28, 1975)", "Founding multilateral treaty signed by 15 West African heads of state in Lagos establishing the Economic Community of West African States (ECOWAS)", "Created the African Union", "Established the United Nations", "Signed to end the Nigerian civil war"),
            ("Headquarters of the ECOWAS Commission and ECOWAS Court of Justice", "Abuja, Federal Capital Territory of Nigeria", "Accra, Ghana", "Lome, Togo", "Dakar, Senegal"),
            ("ECOWAS Trade Liberalization Scheme (ETLS)", "Operational mechanism aimed at progressively dismantling customs tariffs, quotas, and non-tariff barriers on goods originating within West Africa", "A military training program", "A common passport for European tourists", "A single tax on foreign aircraft")
        ]
        for ec_t, ec_d, d1, d2, d3 in ecowas_q:
            q_text = f"In West African regional integration history, what characterizes {ec_t.lower()}?"
            opts = {"A": ec_d, "B": d1, "C": d2, "D": d3}
            items.append(("ECOWAS Regional Integration & Treaties", q_text, opts, "A", f"{ec_t}: {ec_d}.", "Recognize the 1975 Treaty of Lagos, Abuja headquarters, and ETLS trade liberalization."))

def append_grandmaster_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        grand_political = [
            ("A.V. Dicey's Three Postulates of the Rule of Law (1885)", "Absolute supremacy of regular law over arbitrary discretionary power, equality before the ordinary courts of the land, and protection of fundamental individual rights by judicial decisions", "Military decrees supersede constitution", "Citizens have no right to sue government", "Kings can change laws at will"),
            ("Delegated (Subordinate) Legislation", "Laws, statutory instruments, bye-laws, rules, and orders enacted by non-parliamentary executive authorities or local councils under statutory power conferred by parliament", "Decrees made by foreign ambassadors", "Judgments written by jury members", "Treaties made without legislative approval"),
            ("Judicial Control of Delegated Legislation: Doctrine of Ultra Vires", "Courts declare subordinate rules null, void, and of no effect if the rule-making executive body exceeded the statutory boundaries set by the enabling Act", "President dissolving the supreme court", "Judges drafting municipal council bye-laws", "Legislature arresting civil servants"),
            ("Civil Service Principle of Political Neutrality and Impartiality", "Civil servants must serve whatever political party is in power with equal dedication, professional integrity, and loyalty without partisan bias", "Civil servants running for elective governor", "Civil servants leading political party rallies", "Civil servants striking during elections"),
            ("Civil Service Principle of Anonymity", "Civil servants work behind the scenes and cannot be publicly praised or blamed; the political Minister takes full constitutional responsibility before parliament", "Civil servants must remain nameless to their families", "Civil servants never sign official files", "Civil servants cannot speak in offices"),
            ("Pressure Groups vs Political Parties", "Pressure groups seek to influence government policies, legislation, and public opinion without contesting elections or aspiring to capture state power", "Pressure groups contest presidential elections", "Political parties never seek power", "They are legally identical in all aspects"),
            ("Montesquieu's Separation of Powers (The Spirit of the Laws, 1748)", "To preserve political liberty and prevent tyrannical autocracy, the three distinct governmental powers (law-making, law-enforcement, law-interpretation) must be held by separate branches", "All three powers should be unified in the monarch", "Judges should write and enforce all laws", "Armed forces should govern all branches"),
            ("Checks and Balances mechanism in presidential governance", "Constitutional powers granted to each governmental branch to check, supervise, restrain, and balance potential abuses by other branches (e.g. presidential veto, Senate confirmation, judicial review)", "The central bank balancing currency reserves", "The police checking vehicles on highways", "The civil service auditing private bank accounts"),
            ("Modes of Acquiring Citizenship: Jus Sanguinis vs Jus Soli", "Jus Sanguinis awards citizenship based on bloodline/descent of parents; Jus Soli awards citizenship based on the territory/soil of birth", "Jus Sanguinis is citizenship by purchase; Jus Soli is by marriage", "Both mean citizenship by military service", "Jus Soli applies only to royal princes"),
            ("Citizenship by Naturalization requirements in Nigeria (Section 27, 1999 Constitution)", "Requires continuous residence in Nigeria for 15 years, good character, assimilation into local customs, acceptable means of livelihood, and oath of allegiance", "Requires living in Nigeria for only 30 days", "Automatic for all foreign tourists", "Requires owning 5 factories in Lagos"),
            ("Fundamental Human Rights Generations (Karel Vasak framework)", "First-generation: Civil and political liberties (life, speech, vote); Second-generation: Socio-economic and cultural rights (education, health, shelter); Third-generation: Solidarity rights (peace, clean environment)", "First: Military rights; Second: Police rights; Third: Merchant rights", "All rights are exclusively economic", "First-generation applies only to kings"),
            ("Habeas Corpus Prerogative Writ", "A judicial order commanding a detaining authority (police, prison) to bring an incarcerated suspect before court to justify lawful detention, preventing arbitrary executive imprisonment", "An order seizing private land for roads", "An order dissolving parliament", "An order compelling payment of taxes"),
            ("Writ of Mandamus", "A judicial order issued by a superior court commanding a public official, agency, or lower tribunal to perform a specific statutory duty required by law", "An order banning a political party", "An order releasing military weapons", "An order declaring war on a neighbor"),
            ("Writ of Certiorari", "A judicial order issued by a superior court quashing and setting aside an erroneous decision made by an inferior tribunal that exceeded its legal jurisdiction", "An order executing a criminal convict", "An order appointing a cabinet minister", "An order transferring money to the treasury"),
            ("Writ of Prohibition", "A judicial order issued by a superior court restraining and forbidding an inferior court or administrative tribunal from hearing a matter beyond its statutory jurisdiction", "An order banning alcohol sales", "An order stopping strikes in schools", "An order arresting journalists"),
            ("Ombudsman / Public Complaints Commission role in Nigeria (established 1975)", "Investigates citizens' complaints regarding administrative injustice, bureaucratic tyranny, unfair dismissals, and high-handedness by public officers free of charge", "Arrests armed robbery suspects", "Conducts general presidential elections", "Collects federal income taxes"),
            ("Concept of Judicial Independence safeguards", "Security of tenure for judges (retiring age), salaries charged directly to Consolidated Revenue Fund, immunity from civil suits for official acts, and appointment via National Judicial Council", "Judges elected every 2 years by public vote", "Judges reporting directly to police inspectors", "President firing judges at personal whim"),
            ("Dominant Party System vs One-Party State", "In a dominant party system, multiple parties are legally permitted and compete, but one party consistently wins power (e.g. South Africa's ANC); in a one-party state, opposition parties are constitutionally outlawed", "They are identical in law and practice", "In dominant systems, voting is illegal", "One-party states have more elections"),
            ("Two-Party System dynamics (Duverger's Law)", "Electoral systems featuring single-member simple-plurality districts naturally tend toward a stable two-party competition (e.g. USA Republicans and Democrats)", "Guarantees at least 10 parties in power", "Outlaws all independent candidates", "Requires mandatory military rulers"),
            ("Proportional Representation (Party-List System)", "Legislative seats are allocated to political parties in direct mathematical proportion to the percentage of total popular votes won nationwide", "The candidate with single highest vote takes all", "Only royal nobility can cast ballots", "Voters select only military generals")
        ]
        for gp_t, gp_d, d1, d2, d3 in grand_political:
            q_text = f"In constitutional jurisprudence and political theory, what accurately defines {gp_t.lower()}?"
            opts = {"A": gp_d, "B": d1, "C": d2, "D": d3}
            items.append(("Constitutional Theory & Jurisprudence", q_text, opts, "A", f"{gp_t}: {gp_d}.", "Analyze rule of law, delegated legislation, civil service neutrality, and prerogative writs."))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        grand_colonial = [
            ("Royal Niger Company (1886-1899) and Sir George Goldie", "Administered and commercially monopolized territories along the Niger-Benue waterways under British royal charter until charter revocation on Dec 31, 1899", "Established the 1979 constitution", "Built the first Nigerian university in 1886", "Fought against British colonialism"),
            ("Proclamation of January 1, 1900 in Nigeria", "The British Crown formally took direct colonial control from the Royal Niger Company, creating the Protectorate of Northern Nigeria and Southern Nigeria", "Independence was granted to Nigeria", "Lagos was handed over to Germany", "The First Republic was established"),
            ("Aba Women's War of 1929 (Ogu Umunwanye)", "Historic anti-colonial resistance led by Igbo women protesting rumors of direct taxation of women, Warrant Chief abuses, and the destruction of Native Courts", "A military coup against Lord Lugard", "A religious holy war in Calabar", "A trade union strike on railways"),
            ("Warrant Chiefs in Eastern Nigeria under British Indirect Rule", "Artificially created British colonial local rulers appointed in decentralized Igbo communities lacking centralized kings, provoking widespread corruption and popular rebellion", "Hereditary kings descended from ancient gods", "Elected democratic district senators", "British military generals born in London"),
            ("Satiru Rebellion of 1906 in Sokoto Caliphate", "A militant anti-colonial Mahdist peasant rebellion that annihilated a British military detachment before being brutally crushed by Lugard's troops", "A peaceful tea party in Kano", "A constitutional convention in Kaduna", "A boundary dispute between Nigeria and Chad"),
            ("Egba Uprising of 1918 (Adubi War) in Abeokuta", "Armed rebellion by Egba people protesting direct taxation, unpaid forced labor (corvee), and the subversion of Egba autonomous government by British indirect rule", "A conflict between Christian churches", "A naval battle with French gunboats", "An election riot in Lagos"),
            ("French Colonial Policy of Assimilation in Senegal's Four Communes", "Sought to transform educated Africans into French citizens (evolués) enjoying full civic rights in Dakar, Gorée, Saint-Louis, and Rufisque", "Aimed to preserve African languages", "Encouraged armed revolution against France", "Banned all French cultural education"),
            ("Blaise Diagne historic milestone (1914)", "The first indigenous Black African elected to the French Chamber of Deputies in Paris, representing the Four Communes of Senegal", "First president of independent Senegal", "First African general in the British army", "Founder of the African Union"),
            ("Code de l'Indigénat (Indigenat Regime) in French West Africa", "An oppressive colonial legal code empowering French administrators to summarily impose fines, imprisonment without trial, and forced labor on unassimilated native subjects", "A human rights charter protecting Africans", "A free education law in Dakar", "A treaty ending colonial rule in 1920"),
            ("French Policy of Association (Loi-Cadre and beyond)", "Replaced the impractical assimilation policy, recognizing indigenous cultural institutions while maintaining French political hegemony and economic exploitation", "Complete grant of immediate independence", "Unification of Africa into one republic", "Transfer of colonies to Great Britain"),
            ("Portuguese Policy of Assimilado in Mozambique and Angola", "Elitist colonial policy conferring legal status on Africans who could speak Portuguese, adopt Christianity, and abandon African customs, leaving the vast majority as unenfranchised indígenas", "Encouraged traditional African chiefdoms", "Granted free independence in 1910", "Abolished all taxes on native farmers"),
            ("National Congress of British West Africa (NCBWA, 1920)", "Founded by J.E. Casely Hayford in Accra, uniting educated elites from Nigeria, Gold Coast, Sierra Leone, and Gambia to demand legislative franchises and higher education", "A military army fighting colonial rule", "A labor union of cocoa farmers", "A traditional council of emirs and obas"),
            ("Sole Native Authority system and democratic agitation", "Lugardian indirect rule structure vesting absolute legislative and executive powers in a single traditional ruler, fiercely contested by educated Nigerian youths", "A system of universal adult suffrage", "A socialist commune of farmers", "A British parliamentary cabinet"),
            ("Herbert Macaulay's Eleko Affair in Lagos (1920s)", "Macaulay championed the cause of Eshugbayi Eleko (Oba of Lagos) against British colonial deposition, taking the litigation successfully to the Privy Council in London", "An armed rebellion in Ibadan", "A dispute over railway construction", "A strike by dockworkers in Port Harcourt"),
            ("West African Students' Union (WASU, founded London 1925)", "Founded by Chief Ladipo Solanke and Dr. Bankole-Bright, serving as a vital political incubator for radical West African nationalist agitation in Great Britain", "A sports club for cricket players", "A colonial police recruitment office", "A trading company selling cocoa")
        ]
        for gc_t, gc_d, d1, d2, d3 in grand_colonial:
            q_text = f"In West African colonial history and anti-colonial resistance, what characterizes {gc_t.lower()}?"
            opts = {"A": gc_d, "B": d1, "C": d2, "D": d3}
            items.append(("Colonial Resistance & Administrative History", q_text, opts, "A", f"{gc_t}: {gc_d}.", "Examine Aba Women's War, French Assimilation/Indigenat, and nationalist pioneers."))

    elif topic == "Nigerian Constitutional Development":
        grand_const = [
            ("1922 Clifford Constitution Elective Principle details", "Provided for 4 elected legislative council seats (3 representing Lagos, 1 representing Calabar) restricted to adult males with an annual income qualification of £100", "Provided for 100 elected seats nationwide", "Granted universal adult suffrage to all women", "Abolished the legislative council completely"),
            ("Nigerian National Democratic Party (NNDP, founded 1923)", "Nigeria's first formal political party, founded by Herbert Macaulay, which swept the Lagos legislative council elections in 1923, 1928, and 1933", "Founded by Obafemi Awolowo in Ibadan", "A military junta formed by soldiers", "A trade union of railway workers"),
            ("Nigerian Youth Movement (NYM, founded 1934)", "Pioneering nationalist movement founded by Ernest Ikoli, Samuel Akinsanya, and Dr. J.C. Vaughan, advocating true national unity beyond Lagos municipal politics", "A youth sports club in Kaduna", "A religious organization in Enugu", "A colonial government propaganda team"),
            ("1946 Richards Constitution Regional Assemblies", "Created Regional Councils/Houses of Assembly in Northern, Western, and Eastern regions, laying the foundational roots of regionalism in Nigeria", "Abolished regional divisions completely", "Created 36 states with military governors", "Merged Nigeria with Ghana and Sierra Leone"),
            ("1951 Macpherson Constitution Council of Ministers", "Established a central Council of Ministers comprising the Governor and 12 Nigerian ministers (4 appointed from each of the three regions)", "Composed exclusively of British civil servants", "Had no executive authority at all", "Was chaired by Herbert Macaulay"),
            ("1953 Anthony Enahoro Self-Government Motion", "Action Group backbencher Chief Anthony Enahoro moved the historic motion that the House of Representatives accept as primary objective self-government in 1956", "Moved to declare war on Cameroon", "Moved to abolish the regional assemblies", "Moved to adopt French as official language"),
            ("1953 Kano Riots and aftermath", "Violent political and inter-ethnic clashes erupted in Kano following Northern humiliation in Lagos over the self-government motion, prompting the Northern Eight-Point Demand", "A dispute over cattle grazing routes", "A protest against railway ticket fares", "A riot over salt shortages in wartime"),
            ("1954 Lyttelton Constitution: True Federalism institutionalized", "Formally institutionalized a true federal structure with Exclusive Legislative List for Center, Concurrent List for both Center and Regions, and Residual powers for Regions", "Made Nigeria a centralized unitary state", "Abolished the office of regional Premier", "United all regions under a single governor"),
            ("1954 Lyttelton Constitution: Neutral Federal Capital Territory", "Carved out Lagos from the Western Region to become a neutral, independent Federal Capital Territory under central federal administration", "Named Kaduna as the capital of Nigeria", "Made Calabar the sole national capital", "Transferred the federal capital to Enugu"),
            ("1957 London Constitutional Conference achievements", "Granted internal self-government to the Western and Eastern Regions, and created the office of Federal Prime Minister (Abubakar Tafawa Balewa appointed)", "Declared full independence from Britain", "Created 12 states in Nigeria", "Drafted the 1999 constitution"),
            ("1958 Willink Commission of Inquiry findings", "Investigated fears of ethnic minorities in the three regions; recommended a Bill of Fundamental Rights in the constitution and special development boards (NDDB) rather than creating new minority states", "Recommended immediate creation of 30 states", "Recommended expelling all minority tribes", "Recommended a military unitary dictatorship"),
            ("1960 Independence Constitution structure", "Nigeria became an independent sovereign state within the Commonwealth, retainining Queen Elizabeth II as ceremonial Head of State represented by Governor-General Nnamdi Azikiwe", "Abolished all regional legislatures", "Created an executive presidential system", "Instituted a one-party socialist state"),
            ("1960 Independence Constitution: Judicial Appeals", "Maintained the Judicial Committee of the Privy Council in London as the highest appellate court of the Nigerian judiciary", "Made the Supreme Court in Lagos the final court", "Transferred all appeals to the United Nations", "Abolished the court of appeal"),
            ("1963 Republican Constitution changes", "Severed ceremonial ties with the British Monarchy; Dr. Nnamdi Azikiwe became ceremonial President; Supreme Court of Nigeria became the apex final appellate court", "Re-established British royal rule", "Introduced military rule across the country", "Eliminated the prime minister position"),
            ("Creation of the Mid-Western Region in August 1963", "Carved out of the Western Region following a constitutional plebiscite, becoming the fourth region of the Nigerian federation with Benin City as capital", "Created out of the Northern Region", "Formed by merging Lagos and Calabar", "Created by a military decree without vote")
        ]
        for gco_t, gco_d, d1, d2, d3 in grand_const:
            q_text = f"In Nigerian constitutional evolution, what is the historic significance of {gco_t.lower()}?"
            opts = {"A": gco_d, "B": d1, "C": d2, "D": d3}
            items.append(("Nigerian Constitutional Evolution & Milestones", q_text, opts, "A", f"{gco_t}: {gco_d}.", "Master constitutional development: 1922 Clifford, 1946 Richards, 1951 Macpherson, 1954 Lyttelton, and 1963 Republic."))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        grand_fed = [
            ("Major Chukwuma Kaduna Nzeogwu and the January 15, 1966 Coup", "Led Nigeria's first military coup d'etat, assassinating Prime Minister Tafawa Balewa, Sir Ahmadu Bello, Ladoke Akintola, and Chief Festus Okotie-Eboh", "Handed over power to an elected senate", "Promulgated the 1979 constitution", "Created the 36 states in Nigeria"),
            ("Major-General J.T.U. Aguiyi-Ironsi's Unification Decree No. 34 (May 1966)", "Abolished the Nigerian federal structure, unified the regional civil services, and declared Nigeria a unitary republic, sparking violent northern backlash", "Created 12 autonomous states", "Instituted the 1979 presidential system", "Introduced universal basic education"),
            ("July 29, 1966 Counter-Coup in Nigeria", "Northern military officers staged a bloody counter-coup assassinating General Ironsi and Adekunle Fajuyi, installing Lt-Col. Yakubu Gowon as Head of State", "Restored civilian rule immediately", "Formed the Second Republic", "Ended all military intervention in politics"),
            ("The Aburi Accord of January 1967 (Ghana meeting)", "Meeting between Gowon and Ojukwu agreeing in principle on a loose confederation and regional military autonomy to prevent civil war, but conflicting interpretations collapsed the accord", "A treaty ending the Nigerian civil war", "A trade pact with Great Britain", "An agreement creating the African Union"),
            ("General Yakubu Gowon's May 27, 1967 State Creation Decree", "Divided Nigeria into 12 states (6 in North, 6 in South), structurally dismantling the regional hegemony and neutralizing Eastern secessionist plans", "Created 36 states at once", "Abolished all states into 1 unitary territory", "Created only 2 regions"),
            ("General Yakubu Gowon's 'No Victor, No Vanquished' declaration (January 1970)", "Concluded the 30-month Nigerian Civil War with magnanimity, launching the 3Rs national reconstruction, rehabilitation, and reconciliation policy", "Ordered the execution of all Biafran leaders", "Imposed permanent military curfew in the East", "Banned all trade with former eastern region"),
            ("General Murtala Ramat Mohammed's Reforms (July 1975 – Feb 1976)", "Purged corrupt civil servants, created 7 additional states (totaling 19 states), initiated relocation of the federal capital to Abuja, and set an irreversible democratic transition timetable", "Cancelled all plans for civilian transition", "Dissolved the armed forces", "Declared Nigeria an Islamic sultanate"),
            ("The Dimka Abortive Coup (February 13, 1976)", "Lt-Col. B.S. Dimka ambushed and assassinated Head of State Murtala Mohammed in Lagos traffic, but the coup collapsed, leading to Obasanjo assuming command", "Successfully restored civilian democracy", "Installed Shehu Shagari as president", "Disbanded the Nigerian police force"),
            ("General Olusegun Obasanjo's 1979 Historic Handover of Power", "Faithfully implemented Murtala's transition timetable, becoming the first Nigerian military ruler to peacefully hand over power to a democratically elected civilian President (Shehu Shagari)", "Refused to step down from power", "Crowned himself emperor of Nigeria", "Handed power over to the British Crown"),
            ("Major-General Muhammadu Buhari Coup (December 31, 1983)", "Overthrew the Second Republic citing endemic corruption and economic mismanagement, launching the War Against Indiscipline (WAI) and Decree No. 4", "Introduced the 1999 constitution", "Held the June 12 presidential election", "Created 36 states in Nigeria"),
            ("General Ibrahim Babangida's Structural Adjustment Programme (SAP, 1986)", "Economic policy package involving currency devaluation, trade liberalization, subsidy cuts, and privatization mandated by the IMF/World Bank, provoking widespread anti-SAP riots", "A military training program for soldiers", "A free university education scheme", "A policy banning all foreign trade"),
            ("Annulment of the June 12, 1993 Presidential Election", "General Babangida annulled Nigeria's freest and fairest election won by Chief M.K.O. Abiola of the SDP, plunging the country into prolonged political crisis", "Confirmed Abiola as president immediately", "Held a run-off election between SDP and NRC", "Ended all military governance in 1993"),
            ("General Sani Abacha's Regime (1993-1998) and Commonwealth Suspension", "Authoritarian military regime governed by the Provisional Ruling Council (PRC); executed Ken Saro-Wiwa and the Ogoni 9 in 1995, triggering worldwide international sanctions and Commonwealth suspension", "Celebrated for greatest democratic freedom", "Joined the European Union", "Handed power immediately to Abiola"),
            ("General Abdulsalami Abubakar's Rapid Transition (1998-1999)", "Oversaw an eleven-month transition to democracy following Abacha's sudden death, conducting elections that produced President Olusegun Obasanjo and the 1999 Constitution", "Extended military rule for 10 more years", "Dissolved all Nigerian courts", "Banned all political parties permanently"),
            ("The Bakassi Peninsula Dispute Resolution (ICJ Judgement 2002 & Green Tree Agreement 2006)", "The International Court of Justice awarded sovereignty of oil-rich Bakassi to Cameroon, peacefully implemented through diplomatic handover by President Obasanjo in accordance with international law", "Nigeria invaded Cameroon with 100,000 troops", "Nigeria purchased Cameroon for $10 billion", "The dispute was referred to OPEC for arbitration")
        ]
        for gfd_t, gfd_d, d1, d2, d3 in grand_fed:
            q_text = f"In Nigerian political history, military governance, and foreign diplomacy, what characterizes {gfd_t.lower()}?"
            opts = {"A": gfd_d, "B": d1, "C": d2, "D": d3}
            items.append(("Military Governance & Diplomatic Milestones", q_text, opts, "A", f"{gfd_t}: {gfd_d}.", "Analyze military coups (1966, 1975, 1983), June 12, transition to Fourth Republic, and Bakassi diplomacy."))


def append_sovereign_government(items, topic):
    if topic == "Elements of Government & Political Theory":
        sov_poly = [
            ("Judicial Review doctrine (Marbury v. Madison, 1803)", "The constitutional power of independent courts to review, interpret, and invalidate executive actions and legislative laws conflicting with the constitution", "The power of judges to command armed forces", "The power of legislature to try convicts", "The right of police to arrest suspects"),
            ("Characteristics of a Good Constitution", "Clarity, comprehensiveness, accessibility to citizens, adaptability/flexibility to changing times, and protection of fundamental rights", "Being written in secret by a dictator", "Being impossible to amend under any condition", "Having no judicial provisions"),
            ("Unitary Constitution characteristics", "A supreme central government possessing undivided sovereignty; regional bodies derive authority purely as administrative delegates (e.g. UK, France)", "A loose league of independent nations", "Strict constitutional separation of states", "Equal regional flags and armies"),
            ("Rigid vs Flexible Constitution", "A rigid constitution requires cumbersome, special, and stringent amendment procedures (e.g. 2/3 legislative majorities, state ratifications); a flexible constitution can be altered via ordinary legislative acts", "Rigid is written on stone; flexible is written on paper", "Rigid applies only to men; flexible to all", "Rigid constitutions have no courts"),
            ("Functions of the Legislature", "Enacting legislation, scrutinizing executive budget appropriations, confirming high executive appointments, investigating public agencies, and ratifying treaties", "Commanding naval ships in war", "Arresting street criminals directly", "Interpreting legal contracts in disputes"),
            ("Functions of the Executive", "Implementing enacted laws, maintaining internal security and law enforcement, formulating national policies, managing foreign relations, and appointing public officials", "Interpreting statutory constitutional ambiguities", "Writing novel statutes without parliament", "Sentencing felons to prison terms"),
            ("Functions of the Judiciary", "Adjudicating legal disputes between citizens and between citizens and state, interpreting constitutional provisions, issuing prerogative writs, and safeguarding the rule of law", "Drafting annual federal tax budgets", "Leading military troops into battle", "Conducting census counts"),
            ("Merit Principle in Bureaucracy (Max Weber)", "Recruitment, appointment, compensation, and promotion in public service based strictly on proven educational competence, competitive examinations, and technical qualifications", "Appointing only family members and cousins", "Selling civil service offices for cash bribes", "Awarding posts exclusively to ruling party members"),
            ("Civil Society Organizations (CSOs)", "Non-governmental, voluntary civic associations (NGOs, human rights groups, trade unions, faith-based bodies) that operate in the public realm to check state power and champion citizen interests", "Branches of the military junta", "Government ministries collecting tariffs", "Foreign intelligence agencies operating covertly"),
            ("Franchise / Suffrage Qualifications in Modern Democracies", "Universal adult suffrage based on reaching legal age of maturity (e.g. 18 years in Nigeria), mental sanity, and citizenship, without discrimination on property, gender, or race", "Restricted strictly to wealthy property owners", "Permitted only to individuals with university degrees", "Restricted exclusively to male taxpayers")
        ]
        for sp_t, sp_d, d1, d2, d3 in sov_poly:
            q_text = f"In political institutions and constitutional governance, what defines {sp_t.lower()}?"
            opts = {"A": sp_d, "B": d1, "C": d2, "D": d3}
            items.append(("Institutions & Governance Theory", q_text, opts, "A", f"{sp_t}: {sp_d}.", "Understand judicial review, constitutional classification, bureaucratic merit, and franchise."))

    elif topic == "Colonial Administration in Nigeria & West Africa":
        sov_col = [
            ("Treaty of Cession of Lagos (August 6, 1861)", "King Docemo (Dosunmu) of Lagos formally ceded possession and sovereignty of the port and island of Lagos to the British Crown under threat of naval bombardment", "Ceded Lagos to the French Empire", "Formed the Independent Republic of Lagos", "Established the University of Lagos"),
            ("Consul John Beecroft's Naval Bombardment of Lagos (1851)", "British naval intervention (the Reduction of Lagos) expelling King Kosoko for slave trading and installing puppet monarch Akitoye to advance British commercial interests", "A battle against French warships", "An attack by Dahomey warriors", "A Portuguese pirate raid"),
            ("King Jaja of Opobo's Resistance and Exile (1887)", "Defied British commercial monopoly in palm oil trade; was deceitfully lured onto HMS Goshawk by Vice-Consul Harry Johnston, deported to Accra, and exiled to St. Vincent in the West Indies", "Defeated the entire British navy", "Sold his kingdom to Germany", "Became the first colonial governor"),
            ("Nana Olomu of Itsekiri's Resistance (1894 Ebrohimi War)", "Wealthy palm oil merchant and Governor of Benin River who resisted British free trade encroachments; his heavily fortified stronghold of Ebrohimi was bombarded and he was exiled to Ghana", "Assassinated the Queen of England", "Surrendered his weapons without resistance", "Signed a military treaty with France"),
            ("Oba Ovonramwen Nogbaisi and the Fall of Benin (1897)", "Resisted British commercial hegemony; following the Phillips massacre, British forces launched a punitive expedition, looting thousands of priceless Benin bronzes and deporting Ovonramwen to Calabar", "Conquered the British colony of Lagos", "Sold Benin City to Dutch merchants", "Converted to Anglicanism"),
            ("Lord Lugard's Dual Mandate in British Tropical Africa (1922 publication)", "Articulated the moral and economic justification of British imperialism: developing Africa's natural resources for the industrial benefit of mankind while civilizing the native population", "A military handbook on desert warfare", "A legal treatise abolishing all colonies", "A medical textbook on malaria treatment"),
            ("The 1914 Amalgamation of Northern and Southern Nigeria", "Lord Frederick Lugard unified the Protectorate of Northern Nigeria and Colony and Protectorate of Southern Nigeria for British fiscal and administrative convenience, creating modern Nigeria", "Nigeria gained political independence", "The first general election was held", "The civil war broke out"),
            ("The Clifford Legislative Council of 1922 Composition", "Composed of 46 members (27 official British members and 19 unofficial members, of which 4 were elected by indigenous citizens: 3 Lagos, 1 Calabar)", "Had 360 elected Nigerian members", "Composed entirely of traditional emirs", "Had zero British colonial officials"),
            ("The Railway Strike of 1945 led by Michael Imoudu", "A 44-day nationwide general strike of over 40,000 workers demanding a cost-of-living allowance (COLA) amidst wartime inflation, crippling the colonial economy and energizing the nationalist movement", "A riot over railway locomotive repairs", "A protest against French colonial expansion", "A strike by British colonial judges"),
            ("The Burutu Dockers' Strike of 1947", "United Africa Company (UAC) marine workers in Burutu struck for 25 days demanding higher wages, demonstrating the growing militancy of organized labor against colonial corporate exploitation", "A dispute over canoe fishing licenses", "A conflict between rival chiefdoms", "A naval battle on the Atlantic Ocean"),
            ("The Iva Valley Coal Miners' Massacre in Enugu (November 18, 1949)", "British colonial police shot dead 21 striking African coal miners and wounded 51 at the Iva Valley mine, galvanizing national outrage and unifying rival nationalist factions into the National Emergency Committee", "A mine cave-in disaster caused by gas", "A clash between rival political parties", "An ethnic riot in Enugu township"),
            ("West African Court of Appeal (WACA, 1928-1954)", "Regional appellate court serving British West African territories (Nigeria, Gold Coast, Sierra Leone, Gambia) as an intermediary appellate step before the Privy Council in London", "The judicial court of the African Union", "A military tribunal trying deserters", "A municipal traffic court in Lagos"),
            ("Native Authority Police and Native Courts in Northern Nigeria", "Operated under the supervision of traditional Emirs applying Islamic Sharia and Maliki jurisprudence alongside Native Authority ordinances under indirect rule supervision", "Were manned entirely by British constables", "Operated purely under French civil code", "Were completely abolished by Lugard in 1900"),
            ("The West African Youth League (WAYL, 1935)", "Founded by I.T.A. Wallace-Johnson in the Gold Coast and Sierra Leone, promoting radical socialist and pan-African anti-imperialist mass mobilization", "A sports club for cricket students", "A colonial cadet training unit", "An association of European merchants"),
            ("Loi-Cadre (Enabling Act of 1956 in French West Africa)", "Decentralized French colonial rule in AOF and AEF, granting substantial internal self-governance and individual territorial assemblies to each French West African colony", "Abolished all schools in French colonies", "Declared immediate war on Great Britain", "Merged all French colonies into one state"),
            ("Sekou Toure and the 1958 Guinean Constitutional Referendum", "Guinea overwhelmingly voted 'Non' to Charles de Gaulle's French Community ('We prefer poverty in liberty to riches in slavery'), becoming the first French West African colony to achieve immediate independence", "Voted to remain an overseas French department", "Joined the British Commonwealth of Nations", "Merged with Senegal immediately"),
            ("Kwame Nkrumah's Positive Action Campaign (1950 in Gold Coast)", "A nationwide campaign of non-violent civil disobedience, strikes, and boycotts organized by the Convention People's Party (CPP) demanding immediate self-government", "An armed guerilla assault on Accra castles", "A commercial boycott of cocoa planting", "A petition to the League of Nations"),
            ("Convention People's Party (CPP) vs UGCC in Gold Coast", "Nkrumah broke away from the conservative United Gold Coast Convention (UGCC) in 1949 to form the radical populist CPP with the motto 'Self-Government NOW'", "UGCC was a military rebel movement", "CPP opposed independence from Britain", "Both were French political parties"),
            ("J.E. Casely Hayford's Ethiopianism and African Identity", "Ghanaian jurist and intellectual who articulated early cultural nationalism, advocating that Black Africans should take pride in their authentic heritage rather than aping Europeans", "Advocated full assimilation into British culture", "Opposed the establishment of universities in Africa", "Supported the Atlantic slave trade"),
            ("The Crown Colony Government System in British West Africa", "Direct administration by a British Governor assisted by an Executive Council of European officials and a nominated Legislative Council without representative democracy", "Self-governing sovereign democracy", "A system of military junta decrees", "A communist soviet council system")
        ]
        for sc_t, sc_d, d1, d2, d3 in sov_col:
            q_text = f"In West African colonial history and nationalist agitation, what describes {sc_t.lower()}?"
            opts = {"A": sc_d, "B": d1, "C": d2, "D": d3}
            items.append(("Nationalist Agitation & Colonial Incidents", q_text, opts, "A", f"{sc_t}: {sc_d}.", "Analyze Iva Valley massacre, 1945 general strike, King Jaja/Nana Olomu resistance, and Sekou Toure."))

    elif topic == "Nigerian Constitutional Development":
        sov_cst = [
            ("1950 Ibadan All-Nigeria Constitutional Conference", "Convened to aggregate regional consensus on the Macpherson constitution, resolving contentious debates on regional representation (North secured 50% representation) and revenue allocation", "Drafted the 1963 Republican Constitution", "Declared Nigerian independence in 1950", "Abolished the regional houses of assembly"),
            ("The 1953 London and 1954 Lagos Constitutional Conferences", "Resolved the constitutional deadlock caused by the 1953 self-government crisis, agreeing to discard the unitary elements of Macpherson and establish a genuine federal system (Lyttelton Constitution)", "Merged Nigeria with Gold Coast", "Agreed to hand over power to a military general", "Banned all regional political parties"),
            ("Regional Premiers established under 1954 Lyttelton Constitution", "Created the official political post of Regional Premier: Chief Obafemi Awolowo (Western Region), Dr. Nnamdi Azikiwe (Eastern Region), and Sir Ahmadu Bello (Northern Region)", "Created an executive President for Nigeria", "Abolished regional chief ministers", "Made British officers premiers"),
            ("The Northern Elements Progressive Union (NEPU, founded 1950)", "Radical democratic mass party founded in Kano by Malam Aminu Kano to champion the rights of the oppressed talakawa (masses) against feudal Native Authority aristocracy", "A conservative royalist party of Emirs", "A military secret society in Kaduna", "A southern Christian missionary party"),
            ("The United Middle Belt Congress (UMBC, founded 1955)", "Led by Joseph Tarka to mobilize Middle Belt Christian and non-Hausa-Fulani ethnic minorities, fiercely demanding creation of a separate Middle Belt Region out of the North", "A party advocating the merger of North with Niger", "A commercial association of railway merchants", "An arm of the Action Group in Lagos"),
            ("Action Group (AG, founded 1951)", "Political party founded by Chief Obafemi Awolowo evolving from the Egbe Omo Oduduwa, adopting democratic socialism with the motto 'Life More Abundant' and introducing Universal Primary Education (UPE)", "Founded by Herbert Macaulay in 1923", "A radical trade union of coal miners", "A conservative Muslim party of Sokoto"),
            ("National Council of Nigeria and the Cameroons (NCNC, founded 1944)", "Founded by Herbert Macaulay (President) and Dr. Nnamdi Azikiwe (Secretary-General) as a broad-based nationalist coalition of trade unions, literary clubs, and tribal unions", "A regional party restricted strictly to Enugu", "A colonial civil servants welfare union", "A political wing of the British armed forces"),
            ("Northern People's Congress (NPC, founded 1949)", "Evolved from the cultural Jam'iyyar Mutanen Arewa under Sir Ahmadu Bello (Sardauna of Sokoto) and Sir Abubakar Tafawa Balewa with the motto 'One North, One People, Irrespective of Religion, Rank or Tribe'", "A revolutionary communist party", "A southern business corporation", "An armed peasant militia"),
            ("The 1959 Federal Parliamentary Elections", "Conducted to elect members of the House of Representatives that formed the independence government; produced an NPC-NCNC coalition with Balewa as Prime Minister and Azikiwe as Senate President", "Produced an absolute majority for Action Group", "Led to the immediate cancellation of independence", "Was won by the military high command"),
            ("The Census Crisis of 1962/1963 in Nigeria", "Bitter political controversy over alleged fraudulent inflation of regional population figures, which determined federal revenue allocation and parliamentary seat distributions", "A dispute over school examination grades", "A controversy over railway fares", "A conflict regarding currency exchange rates"),
            ("The Western Region Crisis of 1962 and State of Emergency", "Violent political split between Chief Obafemi Awolowo and Chief S.L. Akintola culminating in fighting in the Western House of Assembly, prompting Prime Minister Balewa to declare a state of emergency under Dr. M.A. Majekodunmi", "An armed invasion by French troops", "A flood disaster destroying Ibadan", "A religious dispute in church councils"),
            ("The Federal Election Crisis of 1964 (UPGA vs NNA)", "Stark electoral confrontation between the United Progressive Grand Alliance (UPGA: NCNC + AG) and Nigerian National Alliance (NNA: NPC + NNDP), plagued by massive boycotts and near constitutional collapse", "A peaceful consensus election with zero boycotts", "An election contested by 100 independent candidates", "A municipal local council referendum"),
            ("The Western Election Crisis of October 1965 ('Operation Wetie')", "Massive electoral fraud in the Western Region parliamentary elections triggered widespread violent rioting, arson ('wetting' political opponents with petrol), and lawlessness, precipitating the January 1966 coup", "A festival celebrating rainfall in Ibadan", "A peaceful transition to a new governor", "A boycott of cocoa exportation"),
            ("The 1979 Constitution: Introduction of Executive Presidentialism", "Replaced the British Westminster parliamentary model with the American-style executive presidential system, creating an independently elected President as both Head of State and Chief Executive", "Restored the British monarchy over Nigeria", "Created a military collegiate council", "Made the Chief Justice the head of government"),
            ("The 1979 Constitution: Federal Character Principle (Section 14(3))", "Mandated that the composition of the federal government, appointments, and distribution of public resources must reflect national geographical spread to prevent ethnic dominance", "Mandated that only one tribe can hold federal jobs", "Abolished all state governments in Nigeria", "Required all citizens to speak three languages"),
            ("The 1979 Presidential Election 'Two-Thirds of 19 States' Supreme Court Case (Awolowo v. Shagari)", "Supreme Court ruled that two-thirds of 19 states was mathematically 12 two-thirds (12 states plus two-thirds of the vote in Kano State), upholding Alhaji Shehu Shagari's election as President", "Ordered an immediate re-run election in all 19 states", "Declared Awolowo as the elected president", "Abolished the Supreme Court of Nigeria"),
            ("The 1989 Third Republic Constitution Innovations", "Drafted under General Babangida, proposing a two-party system (SDP and NRC), open ballot voting (Option A4), and bicameral legislature, though largely aborted by the June 12 annulment", "Created 50 political parties at once", "Abolished all democratic institutions", "Declared Nigeria an absolute monarchy"),
            ("The 1999 Constitution (Promulgated by Decree No. 24 of 1999)", "The governing supreme legal grundnorm of the Fourth Republic, re-establishing executive presidentialism, 36-state federal structure, bicameral National Assembly, and independent judiciary", "Established a one-party military state", "Re-introduced the British Queen as head of state", "Abolished the federal character principle"),
            ("1999 Constitution National Assembly Composition", "Bicameral legislature comprising the Senate with 109 senators (3 from each of the 36 states plus 1 from FCT) and House of Representatives with 360 single-member constituency members", "Unicameral parliament of 1,000 members", "Composed entirely of traditional rulers", "Has only 50 senators and no representatives"),
            ("Doctrine of Covering the Field in Nigerian Constitutional Law", "When the National Assembly enacts a valid federal law on a concurrent matter, any state law on that identical subject is rendered inoperative and suspended to the extent of its inconsistency", "State laws always override federal statutes", "Local government bye-laws supersede the constitution", "Military decrees are subordinate to customary law"),
            ("Exclusive Legislative List under Second Schedule of 1999 Constitution", "Comprises 68 enumerated subjects (defence, foreign affairs, currency, aviation, customs, police) reserved exclusively for the federal National Assembly", "Subjects reserved strictly for state governors", "Matters handled only by local government sweepers", "A list of religious festivals"),
            ("Concurrent Legislative List under 1999 Constitution", "Comprises 30 subjects (higher education, electric power, industrial development, collection of certain taxes) on which both the National Assembly and State Houses of Assembly may legislate", "Subjects only the President can execute", "Matters reserved for traditional chiefs", "List of military weapons"),
            ("Chapter II of the 1999 Constitution: Fundamental Objectives and Directive Principles", "Sets forth the political, economic, educational, and foreign policy goals of the Nigerian state, declared non-justiciable (unenforceable in court) by Section 6(6)(c)", "Fully justiciable criminal code", "A list of commercial taxes", "An international human rights treaty"),
            ("National Judicial Council (NJC) Established under Section 153 of 1999 Constitution", "Independent constitutional statutory body responsible for screening, recommending, disciplining, and insulating judicial officers from executive interference", "An association of private criminal lawyers", "A military court martial tribunal", "A legislative committee approving bills"),
            ("Code of Conduct Bureau and Tribunal (Fifth Schedule, 1999 Constitution)", "Statutory anti-corruption body mandated to receive and verify asset declarations of public officers and prosecute breaches of official ethics", "An agency managing federal highways", "An agency issuing driving licenses", "A commission organizing national census"),
            ("Section 8 of 1999 Constitution: Procedure for Creation of New States", "Requires a request supported by 2/3 of members representing the area in Senate, Reps, and State Assembly, approved by 2/3 in a referendum, and ratified by 2/3 of all State Assemblies", "Requires only the personal signature of the President", "Requires an announcement by the army chief", "Requires a simple majority vote in one council"),
            ("Section 143 of 1999 Constitution: Presidential Impeachment Procedure", "Involves notice signed by 1/3 of National Assembly, 2/3 resolution to investigate, 7-person independent panel appointed by CJN, and final 2/3 vote in each chamber to remove", "Immediate arrest by the police inspector general", "A public street demonstration in Abuja", "A declaration of war by the senate"),
            ("Qualifications for Office of the President of Nigeria (Section 131, 1999 Constitution)", "Must be a citizen of Nigeria by birth, have attained the age of 35 years, be educated up to at least School Certificate level, and be a member of a registered political party", "Must be a retired military general over 70", "Must possess a PhD degree in political science", "Must be born in the federal capital territory"),
            ("Section 308 of 1999 Constitution: Executive Immunity Clause", "Confers absolute civil and criminal litigation immunity on the incumbent President, Vice President, State Governors, and Deputy Governors while in office", "Confers immunity on all police officers", "Protects all bank directors from audit", "Applies to all legislative members in parliament"),
            ("The Corrupt Practices and Other Related Offences Act (ICPC Act, 2000)", "Statutory anti-graft law establishing the ICPC to investigate and prosecute corrupt practices and bribery among public officials in the Fourth Republic", "An act dissolving labor unions", "A military decree banning public protests", "A treaty regulating foreign imports")
        ]
        for scs_t, scs_d, d1, d2, d3 in sov_cst:
            q_text = f"In Nigerian constitutional and political history, what is the core significance of {scs_t.lower()}?"
            opts = {"A": scs_d, "B": d1, "C": d2, "D": d3}
            items.append(("Constitutional Milestones & Electoral Crises", q_text, opts, "A", f"{scs_t}: {scs_d}.", "Analyze 1950 Ibadan conference, 1962 Action Group split, Operation Wetie, and Awolowo v. Shagari."))

    elif topic == "Federalism, Military Rule & Foreign Policy":
        sov_fmp = [
            ("Characteristics of Military Rule in Nigeria", "Suspension of key constitutional sections, governance by dictatorial decrees with 'ouster clauses' barring judicial review, centralization of power, and prohibition of political parties", "Strict adherence to separation of powers", "Holding weekly parliamentary debates", "Electing military officers by public votes"),
            ("Supreme Military Council (SMC) / Armed Forces Ruling Council (AFRC)", "The apex decision-making and legislative body under military regimes, composed of senior military officers, service chiefs, and the military Head of State", "A committee of civilian supreme court judges", "An elected house of assembly in Lagos", "A delegation of traditional emirs"),
            ("Military Ouster Clauses in Decrees (e.g. Decree No. 2 of 1984)", "Statutory provisions in military decrees expressly stripping courts of jurisdiction to entertain any legal challenge against acts done under the decree (ouster of judicial review)", "Clauses forcing judges to join the military", "Clauses protecting free speech of journalists", "Clauses requiring approval of parliament"),
            ("Lakanmi v. Attorney-General (Western State) 1970 landmark case", "Supreme Court held that the 1966 handover to the military was not a revolution but an interim constitutional arrangement, invalidating an asset confiscation decree; General Gowon replied with Decree No. 28 asserting military decree supremacy over the constitution", "Decided the ownership of oil fields in Delta", "Established the 1979 constitution", "Ruled on the winner of 1964 election"),
            ("Revenue Allocation Principles in Nigerian Federalism", "Derivation (percentage retained by source state), Equality of States, Population, Land Mass/Terrain, and Internal Revenue Generation Effort (IGR)", "Only derivation is ever used in Nigeria", "Revenues are distributed alphabetically by state", "Revenues are given exclusively to Abuja"),
            ("The Derivation Principle controversy in Niger Delta", "Mandates that a constitutional percentage (currently 13% minimum under Section 162) of natural resource revenue be returned directly to the littoral oil-producing states", "All oil revenue goes to foreign embassies", "No revenue is allocated to littoral states", "Only gold-producing states receive funds"),
            ("The Technical Committee on Revenue Allocation (Aboyade Commission, 1977)", "Proposed technical fiscal criteria (absorptive capacity, fiscal efficiency, minimum national standards) for revenue allocation, later rejected by the 1979 Constituent Assembly for being overly complex", "Recommended abolishing all oil revenues", "Recommended giving all revenue to local governments", "Drafted the 1960 constitution"),
            ("Okigbo Presidential Commission on Revenue Allocation (1980)", "Recommended vertical allocation formula: Federal 53%, States 30%, Local Governments 10%, Special Funds 7%, forming the structural basis for Second Republic revenue sharing", "Recommended 100% derivation to states", "Abolished the Federation Account", "Transferred all taxing power to councils"),
            ("ECOMOG Peacekeeping Interventions in West Africa (1990 Liberia, 1997 Sierra Leone)", "Under Nigerian leadership and major troop/financial contributions, the ECOWAS Ceasefire Monitoring Group intervened militarily to restore constitutional order and stop civil war atrocities", "Invaded neighboring countries for land annexation", "A military intervention by NATO in Africa", "An economic boycott of European imports"),
            ("Nigeria's Role in the Anti-Apartheid Struggle and Frontline States", "Despite geographical distance, Nigeria was officially designated a 'Frontline State', nationalizing Barclays Bank and BP assets in 1979 to compel British action and financing the Southern Africa Relief Fund (SARF)", "Supported the apartheid South African regime", "Refused to admit Black South African students", "Banned all anti-apartheid campaigns"),
            ("Nigeria's Afrocentric Foreign Policy doctrine", "The diplomatic cornerstone asserting that Africa is the center-piece of Nigerian foreign policy, dedicating diplomatic, financial, and military resources to African liberation, security, and integration", "Focusing exclusively on European trade", "Joining the North Atlantic Treaty Organization", "Aligning strictly with the Soviet Union in Cold War"),
            ("Technical Aid Corps (TAC) Scheme established in 1987", "Initiated by Foreign Minister Bolaji Akinyemi, deploying Nigerian volunteer doctors, engineers, and teachers to assist needy developing countries in Africa, Caribbean, and Pacific", "A scheme recruiting foreign mercenary soldiers", "A scheme deporting illegal immigrants", "A military air defense program"),
            ("The Concert of Medium Powers (Lagos Forum, 1987)", "Diplomatic initiative launched by Bolaji Akinyemi bringing together influential regional powers (Nigeria, Brazil, India, Egypt, Sweden) to mediate Cold War superpower tensions", "A military pact against Israel", "A sports tournament for medium countries", "A trade embargo against American goods"),
            ("Non-Aligned Movement (NAM) core tenets in Nigerian diplomacy", "Commitment to national sovereignty, opposition to foreign military alliances with either Western or Eastern Cold War blocs, and solidarity with Global South nations", "Mandatory membership in Warsaw Pact", "Subservience to American military commands", "Refusal to join the United Nations"),
            ("African Union (AU) Transformation from OAU in 2002 (Durban Summit)", "Transitioned the Organization of African Unity from anti-colonial liberation toward deep economic integration, democratic peer review (NEPAD/APRM), and collective security", "Abolished all independent African states", "Merged Africa into the United States of America", "Created an African military empire under one king"),
            ("Gulf War Oil Windfall Controversy (Pius Okigbo Panel Report, 1994)", "Investigated the utilization of $12.4 billion in dedicated oil revenues earned during the 1990/1991 Gulf War oil price surge, criticizing non-transparent extra-budgetary disbursements", "Investigated the assassination of Murtala", "Audited the First Republic cocoa revenues", "Evaluated the construction of the Third Mainland Bridge"),
            ("National Democratic Coalition (NADECO, formed 1994)", "Broad coalition of Nigerian pro-democracy activists, elder statesmen, and human rights organizations that spearheaded domestic and international resistance against the Abacha military dictatorship following the June 12 annulment", "A military wing of the Nigerian army", "A political party sponsored by General Abacha", "A commercial union of oil companies"),
            ("Commonwealth Ministerial Action Group (CMAG) Sanctions on Nigeria (1995-1999)", "Suspended Nigeria from the Commonwealth of Nations and imposed visa and military cooperation sanctions following the execution of Ken Saro-Wiwa and the Ogoni 9", "Awarded Nigeria the Commonwealth peace prize", "Expelled Nigeria from the United Nations", "Froze all commercial shipping in Lagos port"),
            ("General Sani Abacha's 1996 State Creation Exercise", "Created 6 additional states on October 1, 1996 (Bayelsa, Ebonyi, Ekiti, Gombe, Nasarawa, and Zamfara), bringing the federation to its present 36-state structure", "Created 12 states from 4 regions", "Created 19 states from 12", "Merged all states into 6 zones"),
            ("General Ibrahim Babangida's 1987 State Creation Exercise", "Created 2 additional states (Akwa Ibom and Katsina) bringing the total number of Nigerian states to 21", "Created 36 states", "Abolished the federal capital", "Merged Lagos with Ogun"),
            ("General Ibrahim Babangida's 1991 State Creation Exercise", "Created 9 new states on August 27, 1991 (Abia, Delta, Enugu, Jigawa, Kebbi, Kogi, Osun, Taraba, and Yobe), raising the total to 30 states", "Abolished all local governments", "Reduced states back to 12", "Created the Mid-Western Region"),
            ("The 1978 Land Use Act (Decree No. 6 of 1978)", "Promulgated by the Obasanjo military regime, vesting all land in each state in the State Governor to hold in trust for the public, later entrenched in the 1979 and 1999 constitutions", "Abolished all private property", "Sold all land to foreign oil corporations", "Transferred all farm land to the military"),
            ("Nigeria's First United Nations Peacekeeping Mission (ONUC, 1960)", "Deployed Nigerian troops to the Republic of Congo shortly after independence under Major-General J.T.U. Aguiyi-Ironsi, earning international military acclaim", "Invaded Congo to conquer territory", "A joint mission with South Africa", "A naval blockading campaign"),
            ("The Lake Chad Basin Commission (LCBC, established 1964)", "Regional security and environmental organization comprising Nigeria, Chad, Cameroon, and Niger to manage shared Lake Chad water resources and coordinate the Multinational Joint Task Force (MNJTF)", "A fishing company owned by France", "A private oil exploration syndicate", "A diamond mining monopoly"),
            ("The Gulf of Guinea Commission (GGC, established 2001)", "Inter-governmental treaty organization comprising Nigeria, Angola, Congo, Gabon, and Sao Tome to coordinate maritime security, prevent oil bunkering, and foster regional peaceful development", "A military alliance with NATO", "A private shipping container company", "An organization fighting climate change in Europe"),
            ("Nigeria-Sao Tome and Principe Joint Development Zone (JDZ, 2001)", "Historic bilateral treaty establishing joint offshore exploration and exploitation of petroleum and mineral resources in overlapping maritime borders without boundary conflict", "A declaration of naval war", "A treaty selling Nigerian oil rigs", "A border dispute submitted to the ICJ")
        ]
        for sf_t, sf_d, d1, d2, d3 in sov_fmp:
            q_text = f"In Nigerian federalism, military jurisprudence, and international diplomacy, what characterizes {sf_t.lower()}?"
            opts = {"A": sf_d, "B": d1, "C": d2, "D": d3}
            items.append(("Federalism & Strategic Diplomacy", q_text, opts, "A", f"{sf_t}: {sf_d}.", "Analyze military decrees/ouster clauses, Lakanmi case, 13% derivation, ECOMOG, TAC, and NADECO."))

