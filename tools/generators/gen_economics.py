import random

def generate_economics_questions(topic, count_needed=150):
    items = []

    if topic == "Basic Economic Principles & Methodology":
        # 1. Opportunity cost & Scarcity
        scenarios = [
            ("A secondary school graduate chooses to attend university full-time for 4 years instead of accepting an immediate ₦150,000/month job", "The foregone cumulative salary of ₦7.2 million plus work experience", "The cost of textbooks", "The university tuition fees only", "The certificate earned"),
            ("A farmer with 2 hectares of arable land decides to cultivate cassava instead of maize", "The quantity of maize that could have been harvested and sold from that land", "The cost of cassava stems", "The farm laborers' wages", "The cost of land fertilizer"),
            ("The federal government allocates ₦500 billion to defense and security rather than healthcare infrastructure", "The modernized hospitals and medical equipment that could have been constructed", "The salary of soldiers", "The taxes collected", "The cost of military ammunition"),
            ("A consumer with ₦5,000 chooses to purchase a pair of shoes instead of a textbook", "The educational knowledge and utility of the forgone textbook", "The price of the shoes", "The time spent in the market", "The change received"),
            ("A firm uses its retained earnings of ₦50 million to construct a new factory rather than investing in 15% treasury bills", "The foregone annual interest income of ₦7.5 million from government securities", "The architect's design fees", "The price of factory cement", "The factory machinery")
        ]
        for sit, opp_cost, d1, d2, d3 in scenarios:
            q_text = f"In economic theory, what represents the true opportunity cost when {sit.lower()}?"
            opts = {"A": opp_cost, "B": d1, "C": d2, "D": d3}
            items.append((
                "Concept of Opportunity Cost", q_text, opts, "A",
                f"Opportunity cost is the next best alternative forgone: {opp_cost}.",
                "Identify the alternative benefit or revenue sacrificed to make the chosen decision."
            ))

        # 2. Production Possibility Curve (PPC)
        ppc_cases = [
            ("A production point situated strictly inside the boundary of the PPC", "Underutilization of economic resources and widespread unemployment/inefficiency", "Maximum productive efficiency", "Unattainable with existing technology", "Excessive economic growth"),
            ("Any point located directly along the frontier boundary of the PPC", "Full employment and optimal technical allocation of scarce productive resources", "Severe idle capacity", "Hyperinflation", "Technical impossibility"),
            ("A point situated entirely outside the boundary of the existing PPC", "Currently unattainable given existing productive resource endowments and technology", "Inefficient resource allocation", "Severe unemployment", "Depression"),
            ("An outward shift of the entire Production Possibility Curve to the right", "Long-term economic growth driven by technological innovation or increased factor endowments", "A severe national economic recession", "Rising structural unemployment", "Depletion of mineral reserves")
        ]
        for pt, meaning, d1, d2, d3 in ppc_cases:
            q_text = f"On a national Production Possibility Curve (PPC), what does {pt.lower()} signify?"
            opts = {"A": meaning, "B": d1, "C": d2, "D": d3}
            items.append((
                "Production Possibility Curve Analysis", q_text, opts, "A",
                f"{pt}: {meaning}.",
                "Recall the geometric interpretation of points relative to the production possibility frontier."
            ))

        # 3. Factors of production and rewards
        factors = [
            ("Land", "Rent", "Includes all natural resources, mineral wealth, water bodies, and soil; supply is completely inelastic (fixed)", "Wages", "Interest", "Profit"),
            ("Labour", "Wages / Salaries", "Human mental and physical productive effort; highly perishable and inseparable from the worker", "Rent", "Profit", "Dividend"),
            ("Capital", "Interest", "Man-made wealth and physical assets (tools, machinery, factories) used to produce further wealth", "Rent", "Wages", "Commission"),
            ("Entrepreneurship", "Profit", "The risk-bearing factor that organizes, coordinates, and combines land, labour, and capital", "Interest", "Wages", "Royalty")
        ]
        for fact_name, reward, desc, d1, d2, d3 in factors:
            q_text = f"What is the economic reward and primary defining characteristic of the factor of production '{fact_name}'?"
            opts = {"A": f"Reward: {reward}; {desc}", "B": f"Reward: {d1}; {desc}", "C": f"Reward: {d2}; consumable good", "D": f"Reward: {d3}; free gift of nature"}
            items.append((
                "Factors of Production & Factor Rewards", q_text, opts, "A",
                f"Factor {fact_name} earns {reward}. Feature: {desc}.",
                f"Identify the remuneration accrued to {fact_name}."
            ))

        # 4. Economic Systems
        systems = [
            ("Capitalism (Free Market Enterprise)", "Adam Smith's 'invisible hand': private ownership of assets, price mechanism, consumer sovereignty, and profit motive", "Karl Marx's central planning", "Total state ownership of all factories", "Feudal barter only"),
            ("Socialism (Command / Centrally Planned Economy)", "State ownership of productive means, allocation by Central Planning Authority, public welfare priority, and elimination of private profit", "Free price mechanism", "Consumer sovereignty", "Survival of the fittest"),
            ("Mixed Economy (e.g. Nigeria, United Kingdom)", "Coexistence of both private enterprise driven by profit and state public sector regulating vital utilities and infrastructure", "Absence of government laws", "Complete barter system", "100% state ownership")
        ]
        for sys_name, sys_feat, d1, d2, d3 in systems:
            q_text = f"Which institutional framework characterizes {sys_name}?"
            opts = {"A": sys_feat, "B": d1, "C": d2, "D": d3}
            items.append((
                "Comparative Economic Systems", q_text, opts, "A",
                f"{sys_name} is characterized by: {sys_feat}.",
                "Distinguish between market price mechanisms, state planning, and mixed models."
            ))

        # 5. Population calculations: Dependency Ratio
        # DR = (Pop < 15 + Pop > 65) / Pop (15-64) * 100
        for p_young, p_old, p_working in [
            (40, 10, 50),
            (45, 5, 50),
            (30, 10, 60),
            (35, 15, 50),
            (25, 15, 60)
        ]:
            dr = ((p_young + p_old) / p_working) * 100
            q_text = f"In an economy, children (under 15 years) constitute {p_young}% of the population, elderly citizens (above 65) make up {p_old}%, and the working-age population (15-64) comprises {p_working}%. Calculate the dependency ratio."
            opts = {"A": f"{dr:.1f}%", "B": f"{dr / 2:.1f}%", "C": f"{p_young + p_old}%", "D": f"{dr * 1.5:.1f}%"}
            items.append((
                "Demographic Dependency Ratio", q_text, opts, "A",
                f"Dependency Ratio = [(Children + Elderly) / Working-age] × 100% = [({p_young} + {p_old}) / {p_working}] × 100% = {dr:.1f}%.",
                "Divide total dependent population (youth + aged) by working-age population."
            ))

    elif topic == "Microeconomics & Price Mechanism":
        # 1. Equilibrium price and quantity: Qd = a - bP, Qs = c + dP
        for a, b, c, d in [
            (100, 4, 20, 4),
            (120, 5, 20, 5),
            (150, 6, 30, 6),
            (200, 8, 40, 8),
            (80, 2, 20, 4),
            (140, 4, 20, 8),
            (160, 5, 40, 7)
        ]:
            eq_p = (a - c) // (b + d)
            eq_q = a - b * eq_p
            q_text = f"The demand and supply functions for a staple commodity are given as Qd = {a} - {b}P and Qs = {c} + {d}P. Determine the equilibrium price (P) and quantity (Q)."
            opts = {"A": f"P = ₦{eq_p}, Q = {eq_q} units", "B": f"P = ₦{eq_p * 2}, Q = {eq_q} units", "C": f"P = ₦{eq_p}, Q = {eq_q + 10} units", "D": f"P = ₦{a // b}, Q = {c} units"}
            items.append((
                "Market Equilibrium Determination", q_text, opts, "A",
                f"At equilibrium Qd = Qs => {a} - {b}P = {c} + {d}P => {b+d}P = {a-c} => P = {eq_p}. Q = {a} - {b}({eq_p}) = {eq_q} units.",
                "Equate demand and supply equations and solve for P, then substitute P back to find Q."
            ))

        # 2. Price Elasticity of Demand (PED)
        for p1, p2, q1, q2 in [
            (100, 120, 500, 400),
            (50, 60, 200, 150),
            (200, 250, 1000, 700),
            (40, 50, 100, 60)
        ]:
            pct_dq = abs(q2 - q1) / q1
            pct_dp = abs(p2 - p1) / p1
            ped = pct_dq / pct_dp
            ped_type = "Price Elastic (PED > 1)" if ped > 1 else ("Price Inelastic (PED < 1)" if ped < 1 else "Unitary Elastic")
            q_text = f"When the price of a commodity increases from ₦{p1} to ₦{p2}, the quantity demanded falls from {q1} to {q2} units. Calculate the price elasticity of demand and classify its elasticity."
            opts = {"A": f"PED = {ped:.2f} ({ped_type})", "B": f"PED = {ped * 2:.2f}", "C": f"PED = {1/ped:.2f}", "D": f"PED = 0.50"}
            items.append((
                "Price Elasticity of Demand Calculation", q_text, opts, "A",
                f"%ΔQd = |{q2}-{q1}|/{q1} = {pct_dq:.2%}. %ΔP = |{p2}-{p1}|/{p1} = {pct_dp:.2%}. PED = {ped:.2f} ({ped_type}).",
                "Apply formula: PED = (% Change in Quantity Demanded) / (% Change in Price)."
            ))

        # 3. Cross elasticity and Income elasticity
        elasticity_types = [
            ("Cross elasticity of demand between two goods X and Y is positive (XED > 0)", "Substitute goods (an increase in price of Y increases demand for X, e.g. tea and coffee)", "Complementary goods", "Inferior goods", "Giffen goods"),
            ("Cross elasticity of demand between two goods A and B is negative (XED < 0)", "Complementary goods (an increase in price of car increases running cost and reduces demand for petrol)", "Substitute goods", "Normal goods", "Veblen goods"),
            ("Income elasticity of demand is negative (YED < 0)", "Inferior goods (as consumer income increases, demand for this good contracts, e.g. low-grade staple tubers)", "Luxury goods", "Normal goods", "Public goods"),
            ("Income elasticity of demand is positive and greater than 1 (YED > 1)", "Luxury / Superior goods (demand expands more than proportionately as real income rises)", "Inferior goods", "Giffen goods", "Necessities")
        ]
        for el_cond, el_ans, d1, d2, d3 in elasticity_types:
            q_text = f"If the {el_cond.lower()}, what economic relationship exists between the goods?"
            opts = {"A": el_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Cross & Income Elasticity of Demand", q_text, opts, "A",
                f"{el_cond}: {el_ans}.",
                "Check the sign (positive/negative) and magnitude of elasticity coefficient."
            ))

        # 4. Price controls
        price_controls = [
            ("Maximum price legislation (Price ceiling set legally below equilibrium)", "Protects consumers from exploitation, but leads to chronic shortages, queues, hoarding, and illicit black markets", "Causes agricultural surpluses", "Encourages producers to expand supply", "Eliminates all shortages"),
            ("Minimum price legislation (Price floor set legally above equilibrium)", "Protects producers/workers (minimum wage), but generates unsold structural surpluses and unemployment", "Causes severe shortages", "Eliminates unsold stock", "Lowers wage rates")
        ]
        for ctrl, effect, d1, d2, d3 in price_controls:
            q_text = f"What is the inevitable market consequence of imposing {ctrl.lower()}?"
            opts = {"A": effect, "B": d1, "C": d2, "D": d3}
            items.append((
                "Government Price Controls & Market Distortions", q_text, opts, "A",
                f"{ctrl}: {effect}.",
                "Analyze market disequilibrium when legal prices differ from clearing equilibrium price."
            ))

    elif topic == "Macroeconomics & National Income":
        # 1. National Income identity components
        for c, i, g, x, m in [
            (500, 150, 200, 100, 80),
            (600, 200, 250, 120, 150),
            (800, 300, 400, 150, 180),
            (1000, 350, 500, 200, 220)
        ]:
            gdp = c + i + g + (x - m)
            q_text = f"In an open macroeconomy, Consumer spending (C) = ₦{c}bn, Private investment (I) = ₦{i}bn, Government expenditure (G) = ₦{g}bn, Exports (X) = ₦{x}bn, and Imports (M) = ₦{m}bn. Calculate Gross Domestic Product (GDP)."
            opts = {"A": f"₦{gdp} billion", "B": f"₦{c+i+g} billion", "C": f"₦{gdp + m} billion", "D": f"₦{gdp - x} billion"}
            items.append((
                "GDP Expenditure Method", q_text, opts, "A",
                f"GDP = C + I + G + (X - M) = {c} + {i} + {g} + ({x} - {m}) = ₦{gdp} billion.",
                "Sum consumption, investment, government spending, and net exports (X - M)."
            ))

        # 2. National income definitions
        ni_defs = [
            ("Gross National Product (GNP)", "GNP = GDP + Net Factor Income from Abroad (NFIA: earnings of domestic nationals abroad minus earnings of foreigners domestically)", "GDP minus depreciation", "Total taxes collected", "GDP divided by population"),
            ("Net National Product (NNP at market prices)", "NNP = GNP minus Depreciation (Capital Consumption Allowance)", "GDP plus imports", "Total consumption expenditure", "GNP plus subsidies"),
            ("National Income at Factor Cost (NI)", "NNP at market prices minus Indirect Taxes plus Government Subsidies", "GNP at market price", "Personal Disposable Income", "Total bank deposits"),
            ("Per Capita Income", "Total National Income divided by Total Population of the country", "GDP multiplied by population", "Total revenue of commercial banks", "Total minimum wage")
        ]
        for term_n, def_n, d1, d2, d3 in ni_defs:
            q_text = f"How is {term_n} mathematically and conceptually derived in national income accounting?"
            opts = {"A": def_n, "B": d1, "C": d2, "D": d3}
            items.append((
                "National Income Aggregates", q_text, opts, "A",
                f"{term_n}: {def_n}.",
                "Trace national income accounting reconciliations from GDP to factor cost."
            ))

        # 3. Types of Unemployment
        unemployment_types = [
            ("Structural unemployment", "Arises from fundamental long-term shifts in the economy rendering workers' skills obsolete due to technological advancement or industrial decline", "Temporary job switching", "Seasonal harvest changes", "Shortfall in aggregate demand"),
            ("Frictional unemployment", "Transitional temporary unemployment experienced by individuals who are between jobs or freshly entering the labour market searching for suitable work", "Industrial obsolescence", "Severe economic depression", "Underemployment in farming"),
            ("Cyclical (Demand-deficient) unemployment", "Caused by a general macroeconomic downturn, business cycle recession, or contraction in aggregate effective demand", "Workers upgrading digital skills", "Weather changes", "Workers searching for higher pay"),
            ("Disguised unemployment (Underemployment)", "More workers are engaged in an activity than strictly necessary, such that the marginal physical productivity of extra labor is zero", "Complete absence of any job", "High technology job vacancy", "Frictional job search")
        ]
        for ut, u_desc, d1, d2, d3 in unemployment_types:
            q_text = f"Which economic definition accurately characterizes {ut.lower()}?"
            opts = {"A": u_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Theories of Unemployment", q_text, opts, "A",
                f"{ut}: {u_desc}.",
                "Distinguish between structural mismatch, frictional job search, and cyclical recessions."
            ))

    elif topic == "Money, Banking & Public Finance":
        # 1. Commercial Bank Credit Multiplier
        for rr in [0.05, 0.10, 0.20, 0.25]:
            mult = int(1 / rr)
            dep = 1000000
            tot_cred = dep * mult
            rr_pct = int(rr * 100)
            q_text = f"If the Central Bank sets the Cash Reserve Ratio (CRR) at {rr_pct}%, and a customer makes an initial cash deposit of ₦1,000,000 in a commercial bank, calculate the money multiplier and total potential credit generated."
            opts = {"A": f"Multiplier = {mult}; Total Credit = ₦{tot_cred:,}", "B": f"Multiplier = {mult // 2}; Total Credit = ₦{tot_cred // 2:,}", "C": f"Multiplier = {rr_pct}; Total Credit = ₦1,000,000", "D": f"Multiplier = 2; Total Credit = ₦2,000,000"}
            items.append((
                "Bank Credit Creation Multiplier", q_text, opts, "A",
                f"Credit Multiplier = 1 / CRR = 1 / {rr} = {mult}. Total potential money generated = ₦1,000,000 × {mult} = ₦{tot_cred:,}.",
                "Calculate multiplier as 1 / Reserve Ratio and multiply by initial deposit."
            ))

        # 2. Monetary Policy Instruments
        mon_tools = [
            ("Open Market Operations (OMO: Central Bank selling Treasury Bills to commercial banks)", "Contractionary: withdraws excess liquidity from the banking system, reducing loanable funds to combat inflation", "Expansionary: floods banks with cash", "Lowers interest rates", "Devalues currency immediately"),
            ("Raising the Monetary Policy Rate (MPR / Bank Rate)", "Contractionary: increases the cost of borrowing for commercial banks, driving up lending rates and cooling consumer borrowing", "Lowers borrowing cost", "Expands money supply", "Encourages massive business loans"),
            ("Increasing the Cash Reserve Ratio (CRR)", "Forces commercial banks to immobilize a higher percentage of their total deposits with the Central Bank, curbing credit creation capacity", "Increases bank lending profits", "Lowers bank reserves", "Floods the market with cash"),
            ("Lowering the Liquidity Ratio and Bank Rate", "Expansionary monetary policy: stimulates economic recovery during recession by boosting bank credit and reducing interest rates", "Combats runaway inflation", "Restricts bank lending", "Eliminates paper money")
        ]
        for tool_name, tool_impact, d1, d2, d3 in mon_tools:
            q_text = f"What is the macroeconomic objective and mechanism of {tool_name}?"
            opts = {"A": tool_impact, "B": d1, "C": d2, "D": d3}
            items.append((
                "Central Bank Monetary Policy Tools", q_text, opts, "A",
                f"{tool_name}: {tool_impact}.",
                "Identify whether the monetary tool expands or contracts banking liquidity."
            ))

        # 3. Canons of Taxation (Adam Smith)
        canons = [
            ("Canon of Equity (Equality)", "Taxation should be fair and assessed in proportion to taxpayers' ability to pay (wealthier pay more)", "Taxes must be collected at night", "Tax rates must be secret", "All citizens pay identical amounts regardless of income"),
            ("Canon of Certainty", "The time, manner, and exact amount of tax payable must be clear, transparent, and known in advance to both taxpayer and collector", "Tax collector can alter rates arbitrarily", "Tax must change every day", "Payment time is optional"),
            ("Canon of Convenience", "Taxes should be levied and collected at the time and in the manner most convenient for the taxpayer (e.g. PAYE deducted at monthly payday)", "Collected during famines", "Taxpayer treks to central bank", "Collected without notice"),
            ("Canon of Economy", "The administrative cost of collecting the tax must be minimal relative to the gross tax revenue realized for the government", "Spending 90% of tax revenue on collection agents", "Creating 100 new tax ministries", "Giving all taxes to collectors")
        ]
        for c_name, c_desc, d1, d2, d3 in canons:
            q_text = f"According to Adam Smith, what principle governs the {c_name}?"
            opts = {"A": c_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Canons of Taxation", q_text, opts, "A",
                f"{c_name}: {c_desc}.",
                "Recall Adam Smith's four fundamental maxims of sound taxation policy."
            ))

    append_deep_economics(items, topic)
    append_exhaustive_economics(items, topic)
    append_master_economics(items, topic)
    append_ultimate_economics(items, topic)
    append_numeric_boost_economics(items, topic)
    append_final_push_economics(items, topic)
    append_cap_money_banking(items, topic)
    return items

def append_deep_economics(items, topic):
    if topic == "Basic Economic Principles & Methodology":
        # Malthusian theory
        malthus_q = [
            ("Malthusian population growth proposition", "Population grows at a geometric progression (1, 2, 4, 8, 16) while food production expands at an arithmetic progression (1, 2, 3, 4, 5)", "Food grows geometrically while population is constant", "Both grow arithmetically", "Both grow geometrically"),
            ("Malthusian 'positive checks' to population growth", "Natural catastrophes that increase death rates: famine, pestilence, epidemic diseases, and destructive wars", "Late marriage and celibacy", "Artificial contraception", "Moral self-restraint"),
            ("Malthusian 'preventive checks' to population growth", "Voluntary human decisions that lower birth rates: delayed marriage, moral restraint, and celibacy", "Severe famines", "Bubonic plague", "Earthquakes and wars"),
            ("Criticism of Malthusian population doctrine", "Underestimated the immense capacity of technological revolution in agriculture (mechanization, fertilizers, high-yield seeds) and transport", "Ignored wars", "Assumed people eat food", "Overestimated human reproduction")
        ]
        for title, ans, d1, d2, d3 in malthus_q:
            q_text = f"Which statement accurately explains the {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Malthusian Population Doctrine", q_text, opts, "A",
                f"{title}: {ans}.",
                "Contrast geometric population expansion with arithmetic subsistence growth."
            ))

        # Demographic transition theory
        demo_stages = [
            ("Stage 1 of Demographic Transition", "High fluctuating birth rates and high death rates resulting in stationary, slow population growth (pre-industrial society)", "Low birth rate and high death rate", "Rapid population explosion", "Declining birth rate with zero death"),
            ("Stage 2 of Demographic Transition (Population Explosion)", "High birth rates remain persistent while death rates plummet rapidly due to improved sanitation and modern medicine", "Death rates exceed birth rates", "Birth rates drop to zero", "Both birth and death rates are minimal"),
            ("Stage 3 of Demographic Transition", "Birth rates decline significantly due to urbanization and family planning while death rates remain low, slowing growth", "Death rates rise sharply", "Birth rates double", "Population drops to zero"),
            ("Stage 4 of Demographic Transition", "Low birth rates and low death rates stabilizing population at a stationary or contracting replacement level (developed nations)", "High birth rate and high death rate", "Rapid population doubling every decade", "Famines decimate the population")
        ]
        for st_name, st_desc, d1, d2, d3 in demo_stages:
            q_text = f"What demographic characteristics define {st_name}?"
            opts = {"A": st_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Demographic Transition Model", q_text, opts, "A",
                f"{st_name}: {st_desc}.",
                "Identify birth and death rate trends across industrialization phases."
            ))

        # Statistical calculations: Pie Chart Angle
        # Sector degree = (Pct / 100) * 360
        for cat, pct in [
            ("Food expenditure", 40),
            ("Housing rent", 25),
            ("Education", 15),
            ("Healthcare", 10),
            ("Savings", 10),
            ("Transport", 20),
            ("Clothing", 30),
            ("Recreation", 5)
        ]:
            deg = (pct / 100) * 360
            q_text = f"In a household expenditure budget, {cat.lower()} accounts for {pct}% of total family expenditure. What angle would this sector occupy on a circular pie chart?"
            opts = {"A": f"{deg:.1f}°", "B": f"{pct}°", "C": f"{deg / 2:.1f}°", "D": f"{deg * 1.5:.1f}°"}
            items.append((
                "Economic Data Presentation: Pie Charts", q_text, opts, "A",
                f"Angle of sector = (Percentage / 100) × 360° = ({pct} / 100) × 360° = {deg:.1f}°.",
                "Multiply the fractional proportion by 360 degrees."
            ))

    elif topic == "Microeconomics & Price Mechanism":
        # Marginal utility and consumer equilibrium
        mu_data = [
            ("Law of Diminishing Marginal Utility", "As a consumer consumes successive additional units of a commodity, the extra satisfaction (marginal utility) derived from each additional unit declines", "Total utility always decreases", "Price increases as consumption rises", "Marginal utility is always constant"),
            ("Condition for consumer equilibrium when consuming two goods X and Y", "MUx / Px = MUy / Py (the ratio of marginal utility to price is equal across all commodities consumed)", "MUx = MUy regardless of price", "Px = Py always", "Total utility of X equals total utility of Y"),
            ("Consumer Surplus", "The economic difference between the maximum total price a consumer is willing to pay and the actual lower market price paid", "Total profit of the producer", "Taxes paid to government", "The price of the next best alternative")
        ]
        for mu_title, mu_ans, d1, d2, d3 in mu_data:
            q_text = f"In microeconomic consumer theory, what defines {mu_title.lower()}?"
            opts = {"A": mu_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Consumer Utility & Equilibrium", q_text, opts, "A",
                f"{mu_title}: {mu_ans}.",
                "Recall equimarginal utility principles and consumer surplus."
            ))

        # Cost calculations: TC, ATC, MC
        for q, tfc, tvc1, tvc2 in [
            (5, 200, 300, 380),
            (10, 500, 600, 750),
            (4, 150, 200, 260),
            (8, 400, 500, 620)
        ]:
            tc1 = tfc + tvc1
            tc2 = tfc + tvc2
            atc = tc1 / q
            mc = tc2 - tc1 # extra cost of 1 more unit
            q_text = f"A manufacturing firm has Total Fixed Costs (TFC) of ₦{tfc}. When output is {q} units, Total Variable Cost (TVC) is ₦{tvc1}. Calculate Average Total Cost (ATC)."
            opts = {"A": f"₦{atc:.2f}", "B": f"₦{tvc1 / q:.2f}", "C": f"₦{tfc / q:.2f}", "D": f"₦{tc1:.2f}"}
            items.append((
                "Short-Run Production Cost Analysis", q_text, opts, "A",
                f"Total Cost (TC) = TFC + TVC = {tfc} + {tvc1} = ₦{tc1}. ATC = TC / Q = {tc1} / {q} = ₦{atc:.2f}.",
                "Sum fixed and variable costs, then divide by total quantity."
            ))

        # Market Structures
        mkt_structs = [
            ("Perfect Competition", "Large number of buyers and sellers, homogeneous products, perfect market information, price-taking behavior (P = MR = AR), and free entry/exit", "Single producer setting prices", "Differentiated products with heavy advertising", "Kinked demand curve"),
            ("Pure Monopoly", "Single firm producing a unique product with no close substitutes, protected by insurmountable barriers to entry, acting as a price maker", "Price-taking behavior", "Homogeneous products by 1000 firms", "Horizontal demand curve"),
            ("Monopolistic Competition", "Many relatively small firms selling differentiated products (branding, packaging), engaging in non-price competition with free market entry", "Single seller", "Standardized homogeneous goods", "Collusive cartels"),
            ("Oligopoly & Sweezy's Kinked Demand Curve", "Few dominant firms characterized by mutual strategic interdependence; rivals match price decreases but ignore price increases, causing price rigidity", "Firms never compete", "Infinitely many small farmers", "Government fixes all prices")
        ]
        for m_name, m_char, d1, d2, d3 in mkt_structs:
            q_text = f"Which market structure is defined by: '{m_char}'?"
            opts = {"A": m_name, "B": d1, "C": d2, "D": d3}
            items.append((
                "Market Structures & Competitive Conduct", q_text, opts, "A",
                f"This describes {m_name}.",
                "Examine firm numbers, product homogeneity/differentiation, and barriers to entry."
            ))

    elif topic == "Macroeconomics & National Income":
        # Keynesian Multiplier: K = 1 / (1 - MPC) = 1 / MPS
        for mpc in [0.5, 0.6, 0.75, 0.8, 0.9]:
            mps = 1 - mpc
            k = int(1 / mps)
            d_inv = 50 # ₦50 billion
            d_y = d_inv * k
            q_text = f"In a Keynesian macroeconomic model, the Marginal Propensity to Consume (MPC) is {mpc}. If autonomous investment increases by ₦{d_inv} billion, calculate the investment multiplier (K) and total change in national income (ΔY)."
            opts = {"A": f"K = {k}; ΔY = ₦{d_y} billion", "B": f"K = {int(k/2)}; ΔY = ₦{d_y//2} billion", "C": f"K = {mpc}; ΔY = ₦{d_inv} billion", "D": f"K = 10; ΔY = ₦500 billion"}
            items.append((
                "Keynesian Investment Multiplier", q_text, opts, "A",
                f"MPS = 1 - MPC = 1 - {mpc} = {mps:.2f}. Multiplier K = 1 / MPS = 1 / {mps:.2f} = {k}. ΔY = K × ΔI = {k} × ₦{d_inv}bn = ₦{d_y} billion.",
                "Use K = 1 / (1 - MPC), then multiply by autonomous investment change."
            ))

        # Inflation causes & effects
        inf_concepts = [
            ("Demand-pull inflation etiology", "Aggregate monetary demand for goods and services outpaces the aggregate productive capacity of the economy ('too much money chasing too few goods')", "Rapid drop in minimum wage", "Massive rise in agricultural harvest", "Excess of supply over demand"),
            ("Cost-push inflation etiology", "Rising structural costs of production (higher wages, soaring energy tariffs, depreciated import costs) shifting aggregate supply curve to the left", "Increase in national savings", "Lower raw material prices", "Excessive consumer saving"),
            ("Winners during unexpected unanticipated inflation", "Debtors / Borrowers (repay debts with currency of reduced real purchasing power) and owners of real estate assets", "Creditors / Lenders", "Fixed-income salary earners and pensioners", "Holders of cash currency"),
            ("Losers during high unanticipated inflation", "Fixed-income wage earners, pensioners, and cash savers whose real purchasing power is severely eroded", "Debtors who borrowed at fixed interest", "Property speculators", "Commercial loan borrowers")
        ]
        for i_title, i_fact, d1, d2, d3 in inf_concepts:
            q_text = f"In macroeconomic analysis of inflation, what is true regarding {i_title.lower()}?"
            opts = {"A": i_fact, "B": d1, "C": d2, "D": d3}
            items.append((
                "Inflationary Dynamics & Distributional Effects", q_text, opts, "A",
                f"{i_title}: {i_fact}.",
                "Distinguish between demand-pull shifts, cost-push supply shocks, and wealth transfers."
            ))

    elif topic == "Money, Banking & Public Finance":
        # Tax structures: Progressive, Proportional, Regressive
        tax_types = [
            ("Progressive tax system (e.g. Personal Income Tax / PAYE)", "The tax rate increases as the taxpayer's taxable income increases, placing a relatively heavier burden on high-income earners to reduce income inequality", "Rate falls as income rises", "Every taxpayer pays identical percentage", "A tax on imported goods only"),
            ("Proportional (Flat) tax system", "The tax rate remains constant across all income brackets; every individual pays the exact same percentage of their income regardless of wealth", "Rate rises with income", "Rate falls with income", "A tax on luxury items"),
            ("Regressive tax system (e.g. Value Added Tax on basic foodstuffs)", "The effective tax rate represents a larger percentage of a low-income earner's income than of a high-income earner's income", "Places highest percentage on rich", "Exempts low-income earners", "Collects zero tax from poor")
        ]
        for t_name, t_def, d1, d2, d3 in tax_types:
            q_text = f"Which definition describes a {t_name.lower()}?"
            opts = {"A": t_def, "B": d1, "C": d2, "D": d3}
            items.append((
                "Tax Structures: Progressive, Proportional, Regressive", q_text, opts, "A",
                f"{t_name}: {t_def}.",
                "Observe the relationship between marginal tax rate and rising taxable income."
            ))

        # International trade: Comparative vs Absolute Advantage
        trade_theories = [
            ("David Ricardo's Theory of Comparative Advantage", "A nation should specialize in and export those commodities it can produce at a lower relative opportunity cost compared to other nations", "Produces goods with highest absolute cost", "Imports all goods regardless of cost", "Bans all foreign trade"),
            ("Adam Smith's Theory of Absolute Advantage", "A nation should specialize in producing goods that it can produce more efficiently (using fewer total input resources) than any other country", "Specializes in goods with higher opportunity cost", "Eliminates all export tariffs", "Trades only with neighbors"),
            ("Balance of Trade (BOT)", "The financial difference between the total value of visible merchandise exports and visible merchandise imports over a year", "Total visible and invisible exports plus foreign aid", "Government tax minus expenditure", "Total foreign exchange reserves"),
            ("Balance of Payments (BOP)", "A comprehensive systemic financial record of all economic transactions between the residents of a country and the rest of the world over a specified period", "Only trade in oil goods", "Total cash in commercial banks", "National budget deficit")
        ]
        for t_th, t_ans, d1, d2, d3 in trade_theories:
            q_text = f"In international economics, what principle defines {t_th.lower()}?"
            opts = {"A": t_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "International Trade Theories & Balance of Payments", q_text, opts, "A",
                f"{t_th}: {t_ans}.",
                "Distinguish comparative opportunity cost advantage from balance of trade and payments."
            ))

        # Near money & Functions of money
        money_q = [
            ("Primary functions of money", "Medium of exchange and Unit of account (measure of value)", "Store of value and standard of deferred payment", "Speculative asset only", "Generating commercial bank profits"),
            ("Secondary / Derivative functions of money", "Store of value and Standard of deferred payment", "Medium of exchange and unit of account", "Fulfilling reserve requirements", "Printing legal tender"),
            ("Near money (Quasi-money) financial assets", "Highly liquid interest-earning assets that can be converted into spendable cash rapidly with minimal risk of capital loss (e.g. Treasury bills, fixed deposit certificates)", "Physical paper notes in pocket", "Gold locked in jewelry", "Real estate land")
        ]
        for mq_title, mq_ans, d1, d2, d3 in money_q:
            q_text = f"Which categorization correctly identifies the {mq_title.lower()}?"
            opts = {"A": mq_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Monetary Economics & Financial Assets", q_text, opts, "A",
                f"{mq_title}: {mq_ans}.",
                "Distinguish between primary, secondary functions of money, and near-money liquidity."
            ))

def append_exhaustive_economics(items, topic):
    if topic == "Basic Economic Principles & Methodology":
        # Mean, Median, Mode of wage distribution
        for base in [20, 30, 40, 50, 60, 70, 80, 90, 100]:
            dataset = [base, base + 10, base + 20, base + 20, base + 30]
            mean_val = sum(dataset) / len(dataset)
            med_val = dataset[2]
            mode_val = base + 20
            q_text_mean = f"Calculate the arithmetic mean daily wage for five agricultural laborers whose daily earnings are: ₦{dataset[0]}, ₦{dataset[1]}, ₦{dataset[2]}, ₦{dataset[3]}, ₦{dataset[4]}."
            opts_mean = {"A": f"₦{mean_val:.2f}", "B": f"₦{med_val:.2f}", "C": f"₦{mean_val + 5:.2f}", "D": f"₦{mean_val - 10:.2f}"}
            items.append((
                "Measures of Central Tendency in Economics", q_text_mean, opts_mean, "A",
                f"Mean = Sum / N = ({' + '.join(map(str, dataset))}) / 5 = ₦{mean_val:.2f}.",
                "Sum all observations and divide by total number of items."
            ))
            q_text_med = f"Determine the median and modal wage from the dataset: {', '.join(map(str, dataset))}."
            opts_med = {"A": f"Median = ₦{med_val}, Mode = ₦{mode_val}", "B": f"Median = ₦{mean_val:.0f}, Mode = ₦{med_val}", "C": f"Median = ₦{base}, Mode = ₦{base+30}", "D": f"Median = ₦{mode_val}, Mode = ₦{base}"}
            items.append((
                "Median and Mode Analysis", q_text_med, opts_med, "A",
                f"Median is the middle (3rd) value = ₦{med_val}; Mode is the most frequent value = ₦{mode_val}.",
                "Locate the central position for median and highest frequency for mode."
            ))

        # Population density: Pop / Area
        for pop_m, area_sqkm in [(10, 50000), (15, 75000), (20, 100000), (30, 120000), (5, 25000)]:
            pop_actual = pop_m * 1000000
            density = pop_actual // area_sqkm
            q_text = f"A state has an estimated population of {pop_m} million people residing within a total land area of {area_sqkm:,} km². Calculate its population density."
            opts = {"A": f"{density} persons/km²", "B": f"{density * 2} persons/km²", "C": f"{density // 2} persons/km²", "D": f"{pop_m * 10} persons/km²"}
            items.append((
                "Population Density Calculation", q_text, opts, "A",
                f"Population Density = Total Population / Total Land Area = {pop_actual:,} / {area_sqkm:,} = {density} persons/km².",
                "Divide total population count by geographical land area."
            ))

    elif topic == "Microeconomics & Price Mechanism":
        # Price shifts and simultaneous movements
        market_shifts = [
            ("An outward increase in demand while supply remains perfectly constant", "Equilibrium price rises and equilibrium quantity increases", "Price falls and quantity increases", "Price rises and quantity falls", "Both price and quantity decrease"),
            ("An inward decrease in demand while supply remains constant", "Equilibrium price falls and equilibrium quantity decreases", "Price rises and quantity falls", "Price falls and quantity rises", "Quantity remains unchanged"),
            ("An outward increase in supply (technological breakthrough) while demand is constant", "Equilibrium price falls and equilibrium quantity increases", "Price rises and quantity increases", "Both price and quantity fall", "Price remains fixed"),
            ("An inward decrease in supply (severe agricultural drought) while demand is constant", "Equilibrium price rises and equilibrium quantity decreases", "Price falls and quantity falls", "Price rises and quantity rises", "Quantity increases"),
            ("Simultaneous equal rightward increases in both demand and supply", "Equilibrium quantity increases while equilibrium price remains unchanged", "Price doubles", "Quantity drops to zero", "Price drops to zero")
        ]
        for shift_case, outcome, d1, d2, d3 in market_shifts:
            q_text = f"In competitive market equilibrium analysis, what is the net market result of {shift_case.lower()}?"
            opts = {"A": outcome, "B": d1, "C": d2, "D": d3}
            items.append((
                "Shifts in Demand & Supply Curves", q_text, opts, "A",
                f"{shift_case}: {outcome}.",
                "Draw intersecting demand and supply curves to visualize new equilibrium coordinates."
            ))

        # Cross Elasticity calculations
        for p1, p2, q1, q2 in [(100, 150, 200, 260), (200, 250, 400, 480), (50, 75, 100, 130), (80, 120, 300, 390)]:
            pct_dp = (p2 - p1) / p1
            pct_dq = (q2 - q1) / q1
            xed = pct_dq / pct_dp
            q_text = f"When the price of Good X rises from ₦{p1} to ₦{p2}, the sales of Good Y rise from {q1} to {q2} units. Calculate the Cross Elasticity of Demand (XED) and identify the relationship between X and Y."
            opts = {"A": f"XED = +{xed:.2f} (Substitutes)", "B": f"XED = -{xed:.2f} (Complements)", "C": f"XED = 0 (Unrelated)", "D": f"XED = 1.00"}
            items.append((
                "Cross Elasticity of Demand Calculation", q_text, opts, "A",
                f"%ΔPx = {pct_dp:.2%}; %ΔQy = {pct_dq:.2%}. XED = +{xed:.2f}. Positive sign confirms goods X and Y are substitutes.",
                "Positive XED indicates substitutes; negative XED indicates complementary goods."
            ))

        # Profit maximization rule
        q_text_prof = "What is the universal profit-maximizing condition for any business firm regardless of market structure?"
        opts_prof = {"A": "Marginal Revenue equals Marginal Cost (MR = MC), with MC cutting MR from below", "B": "Total Revenue equals Total Cost", "C": "Average Revenue equals Average Cost", "D": "Price equals zero"}
        items.append((
            "Firm Profit Maximization Rule", q_text_prof, opts_prof, "A",
            "Firms maximize economic profit by expanding output up to the point where MR = MC.",
            "Equate marginal revenue to marginal cost."
        ))

    elif topic == "Macroeconomics & National Income":
        # Inflation rate calculations from CPI
        for cpi1, cpi2 in [(100, 115), (120, 138), (150, 180), (200, 250), (160, 200), (250, 300)]:
            inf_rate = ((cpi2 - cpi1) / cpi1) * 100
            q_text = f"The Consumer Price Index (CPI) of an economy stood at {cpi1} in year 1 and rose to {cpi2} in year 2. Calculate the annual rate of inflation."
            opts = {"A": f"{inf_rate:.1f}%", "B": f"{cpi2 - cpi1}%", "C": f"{inf_rate / 2:.1f}%", "D": f"{inf_rate * 1.5:.1f}%"}
            items.append((
                "Consumer Price Index & Inflation Measurement", q_text, opts, "A",
                f"Inflation Rate = [(CPI₂ - CPI₁) / CPI₁] × 100% = [({cpi2} - {cpi1}) / {cpi1}] × 100% = {inf_rate:.1f}%.",
                "Subtract base CPI from current CPI, divide by base CPI, and multiply by 100."
            ))

        # Per capita income calculations
        for y_bill, pop_mill in [(50, 10), (100, 20), (120, 15), (80, 25), (200, 50), (300, 100)]:
            y_actual = y_bill * 1000000000
            pop_actual = pop_mill * 1000000
            per_capita = y_actual // pop_actual
            q_text = f"A developing country records a total National Income of ₦{y_bill} billion with a total population of {pop_mill} million citizens. What is the per capita income?"
            opts = {"A": f"₦{per_capita:,}", "B": f"₦{per_capita * 2:,}", "C": f"₦{per_capita // 2:,}", "D": f"₦{y_bill * 100:,}"}
            items.append((
                "Per Capita Income Calculation", q_text, opts, "A",
                f"Per Capita Income = Total National Income / Population = ₦{y_actual:,} / {pop_actual:,} = ₦{per_capita:,}.",
                "Divide total national income by total population count."
            ))

    elif topic == "Money, Banking & Public Finance":
        # Balance of trade calculations
        for x_val, m_val in [(500, 400), (600, 750), (800, 650), (450, 550), (1000, 800)]:
            bot = x_val - m_val
            bot_status = f"Surplus of ₦{bot} billion" if bot > 0 else f"Deficit of ₦{abs(bot)} billion"
            q_text = f"In an economic trading year, a country recorded total visible merchandise exports of ₦{x_val} billion and total visible merchandise imports of ₦{m_val} billion. Calculate the Balance of Trade (BOT)."
            opts = {"A": bot_status, "B": f"Balanced at ₦{x_val} billion", "C": f"Surplus of ₦{x_val + m_val} billion", "D": f"Deficit of ₦{x_val // 2} billion"}
            items.append((
                "Balance of Trade Accounting", q_text, opts, "A",
                f"BOT = Visible Exports - Visible Imports = ₦{x_val}bn - ₦{m_val}bn = ₦{bot}bn ({bot_status}).",
                "Subtract visible imports from visible exports."
            ))

        # Capital vs Money Market
        markets = [
            ("Money Market", "Financial market for borrowing and lending short-term funds (maturity under 1 year); key instruments include Treasury bills, Commercial papers, and Certificates of deposit", "Long-term shares and debentures", "Physical trade in crude oil", "Foreign exchange only"),
            ("Capital Market (e.g. Nigerian Exchange Group / SEC)", "Financial market mobilizing long-term investment capital (maturity exceeding 1 year) via ordinary shares, debentures, and government bonds", "Overnight interbank loans", "Treasury bills under 90 days", "Central bank cash reserves"),
            ("Ordinary Shares (Equities)", "Represent variable-dividend equity ownership in a corporation carrying voting rights at Annual General Meetings", "Fixed-interest debt obligation", "Short-term money market instrument", "Guaranteed capital refund in liquidation"),
            ("Debentures", "Long-term fixed-interest loan certificates issued by a company acknowledging debt, carrying no voting rights but senior claim on liquidation", "Equity ownership with voting rights", "Short-term promissory notes", "Government tax receipts")
        ]
        for mkt_name, mkt_desc, d1, d2, d3 in markets:
            q_text = f"What is the institutional structure and defining instrument of the {mkt_name}?"
            opts = {"A": mkt_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Financial Markets: Money vs Capital Market", q_text, opts, "A",
                f"{mkt_name}: {mkt_desc}.",
                "Distinguish between short-term money market liquidity and long-term capital formation."
            ))

def append_master_economics(items, topic):
    if topic == "Basic Economic Principles & Methodology":
        # Economies of scale
        scale_items = [
            ("Technical economies of scale", "Cost savings achieved by using larger, specialized, highly efficient machinery capable of indivisible large-scale output", "Borrowing loans at lower interest rates", "Bulk purchasing discounts", "Hiring specialist managers"),
            ("Financial economies of scale", "Large corporate firms obtaining commercial loans at preferential lower interest rates with wider collateral security", "Technical machinery efficiencies", "Free advertising on television", "Bulk raw material transport"),
            ("Managerial economies of scale", "Employing specialized functional managers (marketing, finance, operations) to boost corporate efficiency", "Cheaper electricity tariffs", "Using bigger trucks", "Selling in village markets"),
            ("Internal diseconomies of scale", "Cost increases per unit output caused by managerial bureaucracy, communication bottlenecks, and worker alienation in an oversized firm", "Government tax holidays", "Technical innovation", "Bulk discount on materials"),
            ("External economies of scale", "Cost reductions accrued to all firms in an industry due to industrial localization, specialized training schools, and shared research", "One company buying new computers", "A firm cutting salaries", "Internal promotion of staff")
        ]
        for s_title, s_ans, d1, d2, d3 in scale_items:
            q_text = f"Which economic concept is defined as: '{s_title}'?"
            opts = {"A": s_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Economies & Diseconomies of Scale", q_text, opts, "A",
                f"{s_title}: {s_ans}.",
                "Distinguish between internal firm-specific scale effects and external industry-wide localization benefits."
            ))

        # Division of labor
        div_labor = [
            ("Primary economic advantage of division of labour and specialization", "Increases worker dexterity and productivity through repetition, saving transitional time between tasks and fostering mechanization", "Increases worker boredom", "Eliminates all factory machines", "Guarantees identical wages for all"),
            ("Primary economic disadvantage of extreme division of labour for the individual worker", "Monotony and psychological alienation resulting from performing a single repetitive task endlessly", "Higher technical skill", "Lower output per hour", "Decreased risk of industrial accidents"),
            ("Limitation on the extent of division of labour (Adam Smith)", "The extent of the market (the volume of consumer effective demand for the product)", "The number of hours in a day", "The amount of paper money in banks", "The geographical distance from the sea")
        ]
        for dl_title, dl_ans, d1, d2, d3 in div_labor:
            q_text = f"In classical economic production theory, what represents the {dl_title.lower()}?"
            opts = {"A": dl_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Division of Labour & Specialization", q_text, opts, "A",
                f"{dl_title}: {dl_ans}.",
                "Recall Adam Smith's analysis of pin-making specialization and market limits."
            ))

    elif topic == "Microeconomics & Price Mechanism":
        # Types of Demand
        demand_types = [
            ("Derived demand", "Demand for a factor of production or intermediate input resulting directly from the demand for the final consumer good (e.g. demand for labor in bricklaying)", "Demand for luxury cars", "Demand for goods consumed together", "Demand for alternative brands"),
            ("Joint / Complementary demand", "Demand for two or more commodities that are consumed together to satisfy a single desire (e.g. petrol and motor cars)", "Demand for substitutes like tea and coffee", "Demand for labor", "Demand for raw timber"),
            ("Competitive demand", "Demand for commodities that are close substitutes for one another, where an increase in demand for one reduces demand for the other (e.g. butter and margarine)", "Demand for bread and butter", "Demand for steel in cars", "Demand for water"),
            ("Composite demand", "Demand for a single commodity that serves multiple diverse economic uses (e.g. crude oil used for petrol, diesel, kerosene, and plastics)", "Demand for an exclusive luxury good", "Demand for a good with one single use", "Demand for complementary products")
        ]
        for dt_name, dt_desc, d1, d2, d3 in demand_types:
            q_text = f"Which classification describes {dt_name.lower()}?"
            opts = {"A": dt_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Classifications of Economic Demand", q_text, opts, "A",
                f"{dt_name}: {dt_desc}.",
                "Identify whether goods are consumed together, substitute for one another, serve multiple uses, or derive from final output."
            ))

        # Types of Supply
        supply_types = [
            ("Joint supply", "Two or more distinct commodities produced together from a single shared production process or raw material (e.g. beef and leather hides from cattle)", "Supply of substitutes", "Supply of goods by a monopoly", "Supply fixed by law"),
            ("Competitive supply", "Two or more commodities that compete for the same scarce production factors, such that producing more of one reduces output of the other (e.g. maize vs soybeans on same farm)", "Supply of cattle yielding beef and milk", "Supply of electricity", "Subsidized goods"),
            ("Composite supply", "Total aggregate supply of a commodity or satisfaction provided by several competing sources (e.g. energy supplied by solar, hydro, gas, and coal)", "Supply of a single patented good", "Supply of agricultural hides", "Supply by a pure monopoly")
        ]
        for st_name, st_desc, d1, d2, d3 in supply_types:
            q_text = f"What is meant by {st_name.lower()} in microeconomic supply analysis?"
            opts = {"A": st_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Classifications of Economic Supply", q_text, opts, "A",
                f"{st_name}: {st_desc}.",
                "Distinguish between joint byproducts, factor-competing crops, and multiple energy sources."
            ))

        # Law of Variable Proportions
        var_stages = [
            ("Stage I of Law of Diminishing Returns (Increasing Returns)", "Marginal product of the variable factor increases and exceeds average product, driven by better utilization of fixed factors", "Marginal product is negative", "Average product drops to zero", "Total product falls continuously"),
            ("Stage II of Law of Diminishing Returns (Diminishing Returns)", "Marginal product is positive but declining, and average product is falling; this is the rational stage of production where a profit-maximizing firm operates", "Total product is negative", "Firm fires all workers", "Marginal product is infinite"),
            ("Stage III of Law of Diminishing Returns (Negative Returns)", "Marginal product becomes strictly negative, meaning additional variable labor actually reduces total physical output due to overcrowding and friction", "Total output reaches infinity", "Firms achieve maximum profit", "Marginal product equals price")
        ]
        for stg, s_exp, d1, d2, d3 in var_stages:
            q_text = f"In the short-run theory of production, what characterizes {stg}?"
            opts = {"A": s_exp, "B": d1, "C": d2, "D": d3}
            items.append((
                "Law of Variable Proportions & Production Stages", q_text, opts, "A",
                f"{stg}: {s_exp}.",
                "Identify trends in Total Product (TP), Marginal Product (MP), and Average Product (AP)."
            ))

    elif topic == "Macroeconomics & National Income":
        # Equilibrium National Income: Y = a + bY + I + G
        # Y(1 - b) = a + I + G => Y = (a + I + G) / (1 - b)
        for a_c, b_mpc, inv, gov in [
            (100, 0.8, 50, 50),
            (200, 0.75, 100, 100),
            (150, 0.8, 80, 70),
            (80, 0.6, 40, 40),
            (120, 0.5, 60, 60)
        ]:
            top = a_c + inv + gov
            denom = 1 - b_mpc
            y_eq = int(top / denom)
            q_text = f"In a closed macroeconomic model, Consumption function C = ₦{a_c}m + {b_mpc}Y, Planned Investment I = ₦{inv}m, and Government spending G = ₦{gov}m. Calculate equilibrium national income (Y)."
            opts = {"A": f"₦{y_eq} million", "B": f"₦{top} million", "C": f"₦{y_eq // 2} million", "D": f"₦{y_eq * 2} million"}
            items.append((
                "Macroeconomic Equilibrium Determination", q_text, opts, "A",
                f"Y = C + I + G = ({a_c} + {b_mpc}Y) + {inv} + {gov} => Y - {b_mpc}Y = {top} => {denom:.2f}Y = {top} => Y = ₦{y_eq} million.",
                "Substitute C, I, G into aggregate expenditure Y = C + I + G and solve for Y."
            ))

        # Economic Growth vs Development
        growth_dev = [
            ("Economic Growth", "A quantitative, measurable sustained increase in a nation's real Gross Domestic Product (GDP) or output over a given period", "Qualitative improvements in literacy and life expectancy", "Elimination of poverty", "Equitable income distribution"),
            ("Economic Development", "A multidimensional qualitative transformation entailing economic growth accompanied by improved standard of living, lower poverty, better healthcare, and higher Human Development Index (HDI)", "Mere quantitative rise in GDP figures", "Printing more currency", "Importing luxury vehicles"),
            ("Human Development Index (HDI)", "A composite statistical index combining Life Expectancy at birth, Education (expected and mean years of schooling), and Gross National Income (GNI) per capita", "Only military spending and crude oil reserves", "Total land area", "Number of banks in the country")
        ]
        for gd_title, gd_ans, d1, d2, d3 in growth_dev:
            q_text = f"Which definition correctly distinguishes {gd_title.lower()}?"
            opts = {"A": gd_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Economic Growth vs Economic Development & HDI", q_text, opts, "A",
                f"{gd_title}: {gd_ans}.",
                "Distinguish between quantitative output growth and comprehensive socioeconomic development."
            ))

    elif topic == "Money, Banking & Public Finance":
        # Exchange rate mechanisms
        forex_systems = [
            ("Floating / Flexible Exchange Rate system", "Exchange rate determined purely by market forces of supply and demand for foreign exchange without central bank pegging or intervention", "Exchange rate fixed permanently by statute", "Exchange rate fixed by United Nations", "Barter trade only"),
            ("Currency Devaluation under fixed exchange rate", "Deliberate official downward adjustment by government of the value of domestic currency relative to foreign anchor currencies", "Natural market fall in value", "Deliberate upward adjustment of currency", "Elimination of foreign currency"),
            ("Currency Depreciation under floating exchange rate", "A market-driven decline in the purchasing value of domestic currency against foreign currencies caused by excess domestic demand or trade deficits", "Official government decree", "A rise in domestic currency value", "A budget surplus"),
            ("Marshall-Lerner Condition for successful devaluation", "Currency devaluation improves the national balance of trade only if the sum of price elasticities of demand for exports and imports exceeds 1 (|PEDx| + |PEDm| > 1)", "Exports must equal zero", "Imports must be inelastic", "All tariffs must be doubled")
        ]
        for fx_title, fx_ans, d1, d2, d3 in forex_systems:
            q_text = f"In foreign exchange and international finance, what defines {fx_title.lower()}?"
            opts = {"A": fx_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Exchange Rate Systems & Currency Devaluation", q_text, opts, "A",
                f"{fx_title}: {fx_ans}.",
                "Distinguish market-driven floating depreciation from official administrative devaluation."
            ))

        # Tariffs and Trade Restrictions
        tariffs = [
            ("Specific tariff", "A fixed monetary tax levy assessed per physical unit of imported commodity (e.g. ₦500 per imported tire)", "A percentage tax on product invoice value", "Total physical ban on imports", "Limit on foreign currency"),
            ("Ad valorem tariff", "A customs duty calculated as a fixed percentage proportion of the monetary assessed value of imported goods (e.g. 20% on imported electronics)", "A flat monetary fee per bag", "A license to import", "An export subsidy"),
            ("Import Quota", "A direct quantitative physical ceiling on the maximum volume of a specific good permitted into the country over a given timeframe", "A tax on export revenue", "A subsidy on shipping", "A devaluation of the currency"),
            ("Embargo", "A complete official government ban on the importation or exportation of specified goods or all trade with a targeted nation", "A 10% tariff", "A temporary discount", "A commercial free-trade agreement")
        ]
        for tr_name, tr_desc, d1, d2, d3 in tariffs:
            q_text = f"Which trade policy instrument is defined as an '{tr_name}'?"
            opts = {"A": tr_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Commercial Trade Protectionism & Tariffs", q_text, opts, "A",
                f"{tr_name}: {tr_desc}.",
                "Differentiate between specific, ad valorem duties, physical quotas, and complete trade bans."
            ))

def append_ultimate_economics(items, topic):
    if topic == "Basic Economic Principles & Methodology":
        # Business organizations
        biz_orgs = [
            ("Sole proprietorship (One-man business)", "Easiest to establish, total decision-making autonomy, but suffers from unlimited personal liability and lack of capital continuity", "Requires 50 shareholders", "Issues shares on the stock exchange", "Operated by a board of directors"),
            ("Partnership business structure", "Formed by 2 to 20 partners (up to 50 for banking); partners share unlimited liability unless registered as a limited partnership", "Always managed by the federal government", "Can issue public debentures", "Requires minimum of 100 people"),
            ("Private Limited Liability Company (Ltd)", "Restricted share transfer, maximum of 50 shareholders, cannot invite the public to subscribe to shares, limited liability for owners", "Free trading of shares on stock exchange", "Minimum of 500 members", "No legal registration required"),
            ("Public Limited Liability Company (Plc)", "Minimum of 7 shareholders with no statutory upper limit, authorized to raise public equity capital via the stock exchange, limited liability", "Maximum of 20 partners", "Unlimited personal liability for debts", "Total secrecy of financial accounts"),
            ("Cooperative Society", "Voluntary democratic association organized by members (one man, one vote) to eliminate middleman exploitation and share dividends based on patronage", "Owned exclusively by foreign investors", "Controlled by a private monopoly", "Run solely for military profit")
        ]
        for b_name, b_feat, d1, d2, d3 in biz_orgs:
            q_text = f"Which legal, structural, and financial characteristics define a {b_name}?"
            opts = {"A": b_feat, "B": d1, "C": d2, "D": d3}
            items.append((
                "Forms of Business Organizations", q_text, opts, "A",
                f"{b_name}: {b_feat}.",
                "Examine membership limits, liability, capital mobilization, and share transferability."
            ))

        # Comparative advantage numerical trade-offs
        for c1_yams, c1_cloth, c2_yams, c2_cloth in [
            (100, 50, 40, 40),
            (120, 60, 60, 60),
            (80, 40, 50, 50),
            (150, 50, 100, 100),
            (200, 100, 50, 50)
        ]:
            # Country 1: 1 cloth = (c1_yams / c1_cloth) yams
            opp1 = c1_yams / c1_cloth
            opp2 = c2_yams / c2_cloth
            q_text = f"Country A can produce {c1_yams} units of yams or {c1_cloth} units of cloth. Country B can produce {c2_yams} units of yams or {c2_cloth} units of cloth. What is the opportunity cost of producing 1 unit of cloth in Country A?"
            opts = {"A": f"{opp1:.1f} units of yams", "B": f"{opp2:.1f} units of yams", "C": f"{1/opp1:.2f} units of yams", "D": f"{c1_yams} units of yams"}
            items.append((
                "Comparative Advantage Opportunity Cost Ratio", q_text, opts, "A",
                f"Opportunity cost of 1 cloth in Country A = {c1_yams} / {c1_cloth} = {opp1:.1f} units of yams.",
                "Divide forgone output of good X by gained output of good Y."
            ))

        # Land tenure and Land Use Act
        land_q = [
            ("Nigerian Land Use Act of 1978", "Vested all urban land in state governors and rural land in local government councils to hold in trust for the public", "Sold all land to foreign banks", "Abolished private land sales permanently", "Gave all land to traditional chiefs"),
            ("Communal land tenure system in traditional societies", "Land belongs to the entire community, clan, or village; individuals only enjoy usufructuary rights without power of outright sale", "Land is owned by corporate banks", "Land cannot be farmed", "Land is bought through the stock market")
        ]
        for l_title, l_fact, d1, d2, d3 in land_q:
            q_text = f"What is the statutory or legal provision of the {l_title}?"
            opts = {"A": l_fact, "B": d1, "C": d2, "D": d3}
            items.append((
                "Land Tenure Systems & Economic Legislation", q_text, opts, "A",
                f"{l_title}: {l_fact}.",
                "Recall key provisions of statutory land reforms in Nigeria."
            ))

    elif topic == "Microeconomics & Price Mechanism":
        # Price elasticity of supply calculations
        for p1, p2, q1, q2 in [
            (50, 75, 100, 150),
            (100, 120, 400, 520),
            (80, 100, 200, 240),
            (200, 300, 500, 800),
            (40, 60, 200, 260)
        ]:
            pct_dp = (p2 - p1) / p1
            pct_dq = (q2 - q1) / q1
            pes = pct_dq / pct_dp
            pes_type = "Elastic (PES > 1)" if pes > 1 else ("Inelastic (PES < 1)" if pes < 1 else "Unitary")
            q_text = f"When the market price of a manufactured commodity rises from ₦{p1} to ₦{p2}, the quantity supplied expands from {q1} to {q2} units. Calculate the Price Elasticity of Supply (PES)."
            opts = {"A": f"PES = {pes:.2f} ({pes_type})", "B": f"PES = {pes / 2:.2f}", "C": f"PES = {pes * 2:.2f}", "D": f"PES = 1.00"}
            items.append((
                "Price Elasticity of Supply Calculation", q_text, opts, "A",
                f"%ΔQs = ({q2}-{q1})/{q1} = {pct_dq:.2%}; %ΔP = ({p2}-{p1})/{p1} = {pct_dp:.2%}. PES = {pes:.2f} ({pes_type}).",
                "Apply formula: PES = (%Δ Quantity Supplied) / (%Δ Price)."
            ))

        # Revenue effects of elasticity
        rev_effects = [
            ("A monopolist faces price-elastic demand (PED > 1)", "Lowering the price expands quantity demanded proportionately more, increasing Total Revenue (TR)", "Raising price increases TR", "TR is unaffected", "TR drops to zero"),
            ("A firm operates along the price-inelastic portion of its demand curve (PED < 1)", "Raising the price contracts demand by a smaller percentage, resulting in an increase in Total Revenue (TR)", "Lowering price increases TR", "TR remains identical", "Firms make no revenue"),
            ("Demand exhibits unitary elasticity (PED = 1)", "Any percentage change in price is exactly offset by an equal percentage change in quantity demanded, leaving Total Revenue unchanged", "TR is zero", "TR doubles", "TR drops by 50%"),
            ("Marginal Revenue (MR) at the output where Total Revenue (TR) reaches its maximum", "Marginal Revenue is exactly equal to zero (MR = 0) and PED = 1", "MR is positive infinity", "MR equals Average Cost", "MR equals Price")
        ]
        for r_cond, r_res, d1, d2, d3 in rev_effects:
            q_text = f"In microeconomic revenue analysis, what occurs when {r_cond.lower()}?"
            opts = {"A": r_res, "B": d1, "C": d2, "D": d3}
            items.append((
                "Elasticity & Total Revenue Relationships", q_text, opts, "A",
                f"{r_cond}: {r_res}.",
                "Understand the mathematical link between PED and changes in Total Revenue."
            ))

        # Indifference curve properties
        indiff_props = [
            ("Properties of standard Indifference Curves", "Downwards sloping, convex to the origin due to diminishing marginal rate of substitution (MRS), and cannot intersect one another", "Concave to origin and intersect", "Horizontal straight lines", "Upward sloping curves"),
            ("Consumer equilibrium tangency point on an indifference map", "The point where the budget constraint line is tangent to the highest attainable indifference curve (MRSxy = Px / Py)", "Intersection of two indifference curves", "Point where budget line crosses the origin", "Where total spending is zero")
        ]
        for ip_title, ip_desc, d1, d2, d3 in indiff_props:
            q_text = f"In ordinal utility theory, what describes the {ip_title.lower()}?"
            opts = {"A": ip_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Indifference Curve Analysis & Budget Constraints", q_text, opts, "A",
                f"{ip_title}: {ip_desc}.",
                "Examine the geometry of indifference curves and tangency with budget lines."
            ))

    elif topic == "Macroeconomics & National Income":
        # Multiplier and MPC loops
        for b_val in [0.5, 0.6, 0.7, 0.75, 0.8, 0.85, 0.9]:
            k_val = 1 / (1 - b_val)
            q_text = f"Calculate the Keynesian income multiplier when the Marginal Propensity to Consume (MPC) is {b_val}."
            opts = {"A": f"K = {k_val:.2f}", "B": f"K = {1/b_val:.2f}", "C": f"K = {b_val * 10:.1f}", "D": f"K = 1.00"}
            items.append((
                "Investment Multiplier Formulations", q_text, opts, "A",
                f"K = 1 / (1 - MPC) = 1 / (1 - {b_val}) = 1 / {1-b_val:.2f} = {k_val:.2f}.",
                "Use K = 1 / (1 - MPC)."
            ))

        # Economic integration stages
        integ_stages = [
            ("Free Trade Area (FTA)", "Member states eliminate all tariffs and quotas on trade between themselves but maintain independent national external tariffs against non-members", "Adopts a single currency", "Adopts common external tariffs", "Eliminates all national governments"),
            ("Customs Union", "Members eliminate internal tariffs and adopt a common external tariff (CET) against all non-member countries (e.g. ECOWAS CET)", "Independent external tariffs", "Complete political union", "Shared army"),
            ("Common Market", "A customs union that additionally permits completely free mobility of factors of production (labor and capital) among member states", "Restricts labor movement", "Bans capital investment", "Maintains high internal tariffs"),
            ("Economic and Monetary Union (e.g. European Union Eurozone)", "Full common market combined with harmonization of macroeconomic fiscal policies and adoption of a single common currency managed by a central bank", "Independent currency printing", "Trade barriers between members", "Bilateral barter only")
        ]
        for stg_name, stg_desc, d1, d2, d3 in integ_stages:
            q_text = f"Which stage of international economic integration is defined as a '{stg_name}'?"
            opts = {"A": stg_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Stages of Regional Economic Integration", q_text, opts, "A",
                f"{stg_name}: {stg_desc}.",
                "Observe the progression from Free Trade Area to Customs Union, Common Market, and Monetary Union."
            ))

        # Terms of Trade
        tot_concepts = [
            ("Terms of Trade formula", "Index of Export Prices divided by Index of Import Prices multiplied by 100: (Px / Pm) × 100", "Exports minus Imports", "GDP divided by imports", "Exchange rate multiplied by tariffs"),
            ("Favourable Terms of Trade (TOT > 100)", "Export prices have risen faster than import prices, meaning a country can purchase more imports with a given volume of exports", "Import prices exceed export prices", "Imports are completely free", "Exports drop to zero"),
            ("Unfavourable / Deteriorating Terms of Trade (TOT < 100)", "Import prices rise faster than export prices, forcing the nation to export more physical goods to purchase the same volume of imports", "Export prices soar", "Trade balance is zero", "Domestic currency doubles in value")
        ]
        for tot_t, tot_d, d1, d2, d3 in tot_concepts:
            q_text = f"In international trade economics, how is {tot_t.lower()} defined?"
            opts = {"A": tot_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Terms of Trade Analysis", q_text, opts, "A",
                f"{tot_t}: {tot_d}.",
                "Apply price index ratios of exports versus imports."
            ))

    elif topic == "Money, Banking & Public Finance":
        # International financial organizations
        orgs = [
            ("International Monetary Fund (IMF)", "Provides short-to-medium term foreign exchange financing to member countries facing acute balance of payments crises, enforcing macroeconomic structural adjustments", "Finances construction of long-term dams only", "Regulates world sports", "Prints legal tender notes for all nations"),
            ("World Bank (International Bank for Reconstruction and Development - IBRD)", "Provides long-term concessional loans, technical assistance, and grants for capital infrastructure projects (highways, power grids, healthcare) in developing countries", "Provides 30-day emergency currency loans", "Acts as a commercial bank for citizens", "Controls international oil prices"),
            ("African Development Bank (AfDB)", "Regional development bank dedicated to financing transformative public and private sector socioeconomic development projects across African member states", "Regulates European banks", "Collects customs duties in Africa", "Issues a pan-African currency"),
            ("Organization of the Petroleum Exporting Countries (OPEC)", "Coordinates and unifies petroleum production policies among member nations, utilizing national output quotas to stabilize international crude oil markets", "Fixes gold prices globally", "Controls agricultural exports", "Operates oil tankers directly"),
            ("World Trade Organization (WTO)", "Administers global multilateral trade agreements, provides a forum for trade negotiations, and settles trade disputes between sovereign nations", "Provides long-term bank loans", "Fixes foreign exchange rates", "Sets domestic sales tax rates")
        ]
        for org_n, org_r, d1, d2, d3 in orgs:
            q_text = f"What is the primary mandate and institutional responsibility of the {org_n}?"
            opts = {"A": org_r, "B": d1, "C": d2, "D": d3}
            items.append((
                "International Economic & Financial Organizations", q_text, opts, "A",
                f"{org_n}: {org_r}.",
                "Distinguish between IMF monetary stabilization, World Bank project development, and WTO trade governance."
            ))

        # Public Debt & Sinking Fund
        debt_mgmt = [
            ("Sinking Fund in public debt management", "A dedicated fund established by government into which periodic financial contributions are deposited to accumulate money for retiring a national debt maturity", "Printing currency during inflation", "Selling national assets abroad", "Borrowing from commercial banks at compound interest"),
            ("Debt-to-GDP ratio", "Total accumulated public debt expressed as a percentage of the nation's annual Gross Domestic Product, measuring fiscal debt sustainability", "Annual budget deficit", "Taxes collected divided by inflation", "Total bank reserves"),
            ("Paris Club and London Club debt", "Paris Club represents sovereign bilateral government creditors; London Club represents private commercial bank syndicates", "Both are central banks", "Paris Club represents oil companies", "London Club is the World Bank")
        ]
        for dm_t, dm_d, d1, d2, d3 in debt_mgmt:
            q_text = f"What is meant by {dm_t.lower()} in sovereign public finance?"
            opts = {"A": dm_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Public Debt Management & Fiscal Sustainability", q_text, opts, "A",
                f"{dm_t}: {dm_d}.",
                "Analyze national debt amortization mechanisms and creditor institutions."
            ))

def append_numeric_boost_economics(items, topic):
    if topic == "Microeconomics & Price Mechanism":
        # Extra equilibrium calculations
        for a, b, c, d in [
            (300, 10, 50, 15),
            (250, 5, 50, 5),
            (180, 4, 60, 2),
            (400, 12, 100, 8),
            (500, 20, 100, 20),
            (220, 6, 40, 3),
            (350, 10, 50, 5),
            (160, 3, 40, 1),
            (280, 8, 40, 4),
            (450, 15, 90, 9)
        ]:
            eq_p = (a - c) // (b + d)
            eq_q = a - b * eq_p
            q_text = f"Given market demand function Qd = {a} - {b}P and market supply function Qs = {c} + {d}P, calculate the market clearing price (P) and quantity (Q)."
            opts = {"A": f"P = ₦{eq_p}, Q = {eq_q} units", "B": f"P = ₦{eq_p * 2}, Q = {eq_q} units", "C": f"P = ₦{eq_p}, Q = {eq_q + 15} units", "D": f"P = ₦{a // b}, Q = {c} units"}
            items.append((
                "Market Equilibrium Mathematical Analysis", q_text, opts, "A",
                f"Equating Qd = Qs: {a} - {b}P = {c} + {d}P => {b+d}P = {a-c} => P = {eq_p}. Q = {a} - {b}({eq_p}) = {eq_q} units.",
                "Set Qd equal to Qs and solve for P, then compute equilibrium Q."
            ))

        # Extra PED calculations
        for p1, p2, q1, q2 in [
            (50, 60, 500, 450),
            (100, 150, 1000, 600),
            (80, 100, 400, 320),
            (200, 220, 500, 400),
            (30, 45, 600, 360),
            (120, 150, 800, 640),
            (60, 90, 300, 210),
            (40, 50, 200, 180),
            (150, 180, 600, 510),
            (250, 300, 1000, 850)
        ]:
            pct_dp = (p2 - p1) / p1
            pct_dq = (q1 - q2) / q1
            ped = pct_dq / pct_dp
            ped_type = "Elastic" if ped > 1 else ("Inelastic" if ped < 1 else "Unitary")
            q_text = f"A price increase from ₦{p1} to ₦{p2} causes quantity demanded to drop from {q1} to {q2} units. Compute the Price Elasticity of Demand (PED)."
            opts = {"A": f"PED = {ped:.2f} ({ped_type})", "B": f"PED = {ped * 2:.2f}", "C": f"PED = {ped / 2:.2f}", "D": f"PED = {pct_dp:.2f}"}
            items.append((
                "PED Quantitative Computation", q_text, opts, "A",
                f"%ΔQd = {pct_dq:.2%}; %ΔP = {pct_dp:.2%}. PED = {pct_dq:.2f}/{pct_dp:.2f} = {ped:.2f} ({ped_type}).",
                "Divide percentage change in quantity demanded by percentage change in price."
            ))

        # Extra Cost calculations
        for q, tfc, tvc in [
            (2, 100, 60),
            (3, 150, 120),
            (4, 200, 180),
            (5, 250, 250),
            (6, 300, 330),
            (8, 400, 480),
            (10, 500, 700),
            (12, 600, 900),
            (15, 750, 1200),
            (20, 1000, 1800)
        ]:
            tc = tfc + tvc
            afc = tfc / q
            avc = tvc / q
            atc = tc / q
            q_text = f"A firm produces {q} units of output with Total Fixed Cost (TFC) = ₦{tfc} and Total Variable Cost (TVC) = ₦{tvc}. What is the Average Fixed Cost (AFC) and Average Total Cost (ATC)?"
            opts = {"A": f"AFC = ₦{afc:.2f}, ATC = ₦{atc:.2f}", "B": f"AFC = ₦{atc:.2f}, ATC = ₦{afc:.2f}", "C": f"AFC = ₦{tfc}, ATC = ₦{tc}", "D": f"AFC = ₦{avc:.2f}, ATC = ₦{atc:.2f}"}
            items.append((
                "Production Costs: AFC and ATC Computation", q_text, opts, "A",
                f"AFC = TFC / Q = {tfc} / {q} = ₦{afc:.2f}. Total Cost TC = {tfc} + {tvc} = ₦{tc}. ATC = TC / Q = {tc} / {q} = ₦{atc:.2f}.",
                "Divide TFC by output Q for AFC, and divide TC by output Q for ATC."
            ))

    elif topic == "Macroeconomics & National Income":
        # Additional GDP calculations
        for c, i, g, x, m in [
            (450, 120, 180, 90, 70),
            (700, 250, 300, 140, 160),
            (900, 320, 450, 180, 210),
            (1100, 400, 600, 250, 280),
            (550, 160, 220, 110, 90),
            (650, 180, 260, 130, 140),
            (850, 280, 380, 160, 170),
            (1200, 450, 650, 300, 320),
            (750, 220, 310, 150, 130),
            (950, 340, 480, 200, 240)
        ]:
            gdp = c + i + g + (x - m)
            q_text = f"Determine the Gross Domestic Product (GDP) using the expenditure approach: C = ₦{c}bn, I = ₦{i}bn, G = ₦{g}bn, Exports = ₦{x}bn, Imports = ₦{m}bn."
            opts = {"A": f"₦{gdp} billion", "B": f"₦{c+i+g} billion", "C": f"₦{gdp + 50} billion", "D": f"₦{gdp - 50} billion"}
            items.append((
                "National Income GDP Computation", q_text, opts, "A",
                f"GDP = C + I + G + (X - M) = {c} + {i} + {g} + ({x} - {m}) = ₦{gdp} billion.",
                "Sum consumption, investment, government expenditure, and net exports."
            ))

        # Real GDP from Nominal and Deflator
        for nom, defl in [
            (220, 110),
            (360, 120),
            (450, 150),
            (520, 130),
            (600, 150),
            (800, 160),
            (1000, 200),
            (1250, 250),
            (720, 180),
            (900, 150)
        ]:
            real = int((nom / defl) * 100)
            q_text = f"If a country's Nominal GDP is ₦{nom} billion and its GDP Deflator index is {defl}, calculate the Real GDP."
            opts = {"A": f"₦{real} billion", "B": f"₦{nom} billion", "C": f"₦{real // 2} billion", "D": f"₦{real * 2} billion"}
            items.append((
                "Real vs Nominal GDP Adjustment", q_text, opts, "A",
                f"Real GDP = (Nominal GDP / GDP Deflator) × 100 = (₦{nom}bn / {defl}) × 100 = ₦{real} billion.",
                "Deflate nominal GDP by the price deflator index."
            ))

        # Inflation calculations
        for c1, c2 in [
            (110, 132),
            (140, 168),
            (180, 225),
            (210, 273),
            (240, 300),
            (150, 195),
            (175, 210),
            (200, 260),
            (225, 270),
            (300, 390)
        ]:
            inf = ((c2 - c1) / c1) * 100
            q_text = f"Calculate the rate of inflation if the Consumer Price Index rises from {c1} to {c2}."
            opts = {"A": f"{inf:.1f}%", "B": f"{c2 - c1}%", "C": f"{inf / 2:.1f}%", "D": f"{inf * 1.2:.1f}%"}
            items.append((
                "CPI Inflation Rate Formulations", q_text, opts, "A",
                f"Inflation Rate = [(CPI₂ - CPI₁) / CPI₁] × 100% = [({c2} - {c1}) / {c1}] × 100% = {inf:.1f}%.",
                "Compute the percentage change between initial and final price indices."
            ))

    elif topic == "Money, Banking & Public Finance":
        # Additional Bank Credit Multiplier loops
        for rr_pct, dep_val in [
            (4, 500000),
            (5, 2000000),
            (8, 1000000),
            (10, 5000000),
            (12.5, 2000000),
            (15, 3000000),
            (20, 4000000),
            (25, 5000000),
            (50, 1000000),
            (2, 1000000)
        ]:
            rr_dec = rr_pct / 100
            mult = 1 / rr_dec
            tot_c = int(dep_val * mult)
            mult_str = f"{int(mult)}" if mult.is_integer() else f"{mult:.1f}"
            q_text = f"If the Cash Reserve Ratio (CRR) is {rr_pct}%, and an initial deposit of ₦{dep_val:,} is made, calculate the deposit multiplier and total money created."
            opts = {"A": f"Multiplier = {mult_str}; Total Deposit = ₦{tot_c:,}", "B": f"Multiplier = {rr_pct}; Total Deposit = ₦{dep_val * 2:,}", "C": f"Multiplier = 2; Total Deposit = ₦{tot_c // 2:,}", "D": f"Multiplier = 1; Total Deposit = ₦{dep_val:,}"}
            items.append((
                "Credit Creation & Reserve Ratios", q_text, opts, "A",
                f"Multiplier = 1 / CRR = 1 / {rr_dec} = {mult_str}. Total Credit = ₦{dep_val:,} × {mult_str} = ₦{tot_c:,}.",
                "Divide 1 by reserve ratio, then multiply by initial deposit."
            ))

        # Balance of trade calculations
        for exp_v, imp_v in [
            (350, 280),
            (420, 500),
            (580, 460),
            (720, 850),
            (950, 750),
            (640, 600),
            (820, 910),
            (1100, 950),
            (480, 530),
            (1300, 1100)
        ]:
            bot = exp_v - imp_v
            stat = f"Surplus of ₦{bot}bn" if bot > 0 else f"Deficit of ₦{abs(bot)}bn"
            q_text = f"In a given fiscal year, merchandise exports equal ₦{exp_v} billion and merchandise imports equal ₦{imp_v} billion. What is the Balance of Trade?"
            opts = {"A": stat, "B": f"Balanced at ₦{exp_v}bn", "C": f"Surplus of ₦{exp_v + imp_v}bn", "D": f"Deficit of ₦{exp_v // 2}bn"}
            items.append((
                "Merchandise Balance of Trade Calculation", q_text, opts, "A",
                f"BOT = Exports - Imports = ₦{exp_v}bn - ₦{imp_v}bn = ₦{bot}bn ({stat}).",
                "Deduct imports from exports to determine surplus or deficit status."
            ))

def append_final_push_economics(items, topic):
    if topic == "Basic Economic Principles & Methodology":
        # Location of industries
        ind_loc = [
            ("Raw material-oriented industry (e.g. cement factory near limestone quarries)", "Located in close proximity to bulky, perishable, or weight-losing raw materials to minimize transport costs", "Located near luxury shopping malls", "Located near airports only", "Located in foreign countries"),
            ("Market-oriented industry (e.g. bakeries, daily newspapers, soft drink bottling)", "Located near consumer markets because finished goods are perishable, fragile, or gain weight/bulk during production", "Located in remote uninhabited forests", "Located near deep coal mines", "Located on mountain peaks"),
            ("Footloose industry (e.g. semiconductor microchip assembly, software development)", "Industries whose production costs and outputs are unaffected by raw material or market location; can locate anywhere with internet and electricity", "Must locate at seaports", "Must locate inside iron mines", "Must locate near farms"),
            ("Industrial localization / Clustering (e.g. computer village in Ikeja, auto-parts in Nnewi)", "Concentration of competing and complementary firms in the same geographic area to benefit from shared infrastructure and skilled labor", "Scattering factories across 100 islands", "Banning all competitors", "Government nationalizing all private firms")
        ]
        for l_type, l_desc, d1, d2, d3 in ind_loc:
            q_text = f"Which economic factor determines the location of a '{l_type}'?"
            opts = {"A": l_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Location & Localization of Industries", q_text, opts, "A",
                f"{l_type}: {l_desc}.",
                "Analyze weight-losing raw materials versus weight-gaining finished goods."
            ))

        # Additional opportunity cost calculations
        for yams, cassava in [(200, 100), (300, 150), (400, 200), (500, 250), (160, 80), (240, 120)]:
            opp = yams / cassava
            q_text = f"A farm with given inputs can harvest either {yams} heaps of yams or {cassava} heaps of cassava. What is the opportunity cost of harvesting 1 heap of cassava?"
            opts = {"A": f"{opp:.1f} heaps of yams", "B": f"{1/opp:.2f} heaps of yams", "C": f"{yams} heaps of yams", "D": f"{cassava} heaps of yams"}
            items.append((
                "Opportunity Cost of Agricultural Production", q_text, opts, "A",
                f"Opportunity cost = {yams} / {cassava} = {opp:.1f} heaps of yams.",
                "Divide forgone output of yams by gained output of cassava."
            ))

    elif topic == "Macroeconomics & National Income":
        # Additional per capita income calculations
        for gdp_b, pop_m in [(150, 30), (240, 40), (350, 70), (480, 80), (500, 100)]:
            pc = (gdp_b * 1000) // pop_m
            q_text = f"If a nation's GDP is $ {gdp_b} billion and its total population is {pop_m} million citizens, calculate the per capita GDP in US dollars."
            opts = {"A": f"${pc:,}", "B": f"${pc * 2:,}", "C": f"${pc // 2:,}", "D": f"${gdp_b * 100:,}"}
            items.append((
                "Per Capita GDP Calculations", q_text, opts, "A",
                f"Per Capita GDP = ($ {gdp_b}bn × 1000) / {pop_m}m = ${pc:,}.",
                "Divide total output by total population."
            ))

    elif topic == "Money, Banking & Public Finance":
        # Additional Credit Multiplier calculations
        for crr_p, dep in [
            (2.5, 1000000),
            (6.25, 2000000),
            (16, 4000000),
            (33.33, 3000000),
            (30, 6000000)
        ]:
            mult = 100 / crr_p
            tot = int(dep * mult)
            q_text = f"Calculate the potential total credit created from an initial commercial bank deposit of ₦{dep:,} when the Central Bank imposes a {crr_p:.1f}% Cash Reserve Ratio."
            opts = {"A": f"₦{tot:,} (Multiplier = {mult:.1f})", "B": f"₦{dep * 2:,}", "C": f"₦{tot // 2:,}", "D": f"₦{dep:,}"}
            items.append((
                "Commercial Bank Credit Creation Scaling", q_text, opts, "A",
                f"Credit Multiplier = 100 / {crr_p:.1f} = {mult:.1f}. Total Credit = ₦{dep:,} × {mult:.1f} = ₦{tot:,}.",
                "Apply 1 / CRR multiplier to initial deposit."
            ))

        # Direct vs Indirect tax features
        tax_features = [
            ("Direct taxes (e.g. PAYE personal income tax, company tax)", "Levied directly on the income or wealth of the taxpayer and cannot be shifted or transferred to another person", "Can be shifted onto consumers via price hikes", "Tax on imported fuel only", "Optional donations to government"),
            ("Indirect taxes (e.g. VAT, excise duties, customs tariffs)", "Levied on expenditure on goods and services, and can be shifted by producers onto final consumers via higher retail prices", "Levied directly on inheritance wealth", "Cannot be shifted to anyone", "Collected only from government workers"),
            ("Incidence of indirect tax with perfectly inelastic demand (e.g. essential life-saving medicine)", "The entire economic tax burden is shifted 100% onto the final consumer", "Borne 100% by producer", "Shared 50-50", "No tax is paid"),
            ("Incidence of indirect tax with perfectly elastic demand", "The entire economic tax burden is borne 100% by the producer / seller", "Borne 100% by consumer", "Paid by central bank", "Subsidized by government")
        ]
        for tf_name, tf_desc, d1, d2, d3 in tax_features:
            q_text = f"In public finance, what principle governs {tf_name.lower()}?"
            opts = {"A": tf_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Tax Incidence & Direct vs Indirect Taxes", q_text, opts, "A",
                f"{tf_name}: {tf_desc}.",
                "Analyze ability to shift tax burden depending on price elasticity."
            ))

        # Additional public debt instruments
        debt_inst = [
            ("Treasury Bills (T-Bills)", "Short-term sovereign promissory debt instruments issued by the Central Bank on behalf of government with maturities of 91, 182, or 364 days", "Long-term 25-year infrastructure bonds", "Shares in private companies", "Commercial bank foreign loans"),
            ("Treasury Certificates", "Medium-term government borrowing securities with maturities ranging between one and two years", "90-day promissory notes", "Private company equities", "International currency reserves"),
            ("Development Stocks (FGN Bonds)", "Long-term debt securities issued by the federal government with maturities of 5 to 30 years to finance long-term capital projects", "Overnight interbank cash", "Import tariffs", "Bank checking accounts"),
            ("Ways and Means Advances", "Direct short-term credit advances provided by the Central Bank to finance temporary federal government revenue shortfalls", "Private mortgage loans", "IMF structural adjustment loans", "World Bank educational grants")
        ]
        for di_name, di_desc, d1, d2, d3 in debt_inst:
            q_text = f"How is the sovereign debt instrument '{di_name}' defined?"
            opts = {"A": di_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Government Debt Instruments & Fiscal Deficit Financing", q_text, opts, "A",
                f"{di_name}: {di_desc}.",
                "Differentiate between short-term T-bills, medium-term certificates, long-term bonds, and central bank overdrafts."
            ))

def append_cap_money_banking(items, topic):
    if topic == "Money, Banking & Public Finance":
        extra_mb = [
            ("Central Bank function as 'Lender of Last Resort'", "Provides emergency short-term liquidity advances to solvent commercial banks experiencing temporary deposit runs or cash panics", "Lends money to all citizens", "Finances private companies directly", "Bails out foreign governments"),
            ("Distinction between Statutory Allocation and Internally Generated Revenue (IGR)", "Statutory allocation is federally shared revenue derived from crude oil and customs; IGR is revenue collected locally by state/local governments via taxes/levies", "IGR comes from foreign loans", "Statutory allocation is paid only to private banks", "Both are foreign grants"),
            ("Sovereign Wealth Fund (e.g. Nigeria Sovereign Investment Authority - NSIA)", "State-owned investment fund investing surplus commodity revenues across stabilization, future generations, and infrastructure funds", "A commercial bank branch", "A fund for military pensions only", "A private hedge fund"),
            ("Impact of high budget deficit financed by 'Ways and Means' printing of money", "Injects unbacked monetary liquidity into circulation, triggering runaway demand-pull inflation and depreciating currency exchange rate", "Lowers inflation to zero", "Strengthens national currency", "Eliminates all public debt"),
            ("Fiduciary issue of currency", "Paper currency notes issued by the Central Bank that are backed entirely by government trust and securities rather than physical gold reserves", "Currency backed 100% by gold", "Foreign coins", "Digital crypto tokens only"),
            ("Merchant banks vs Commercial banks", "Merchant banks specialize in wholesale banking, loan syndication, underwriting of securities, and corporate finance, accepting large wholesale deposits only", "Merchant banks offer small retail savings accounts", "Commercial banks cannot take deposits", "Merchant banks issue physical legal tender currency"),
            ("Mortgage institutions (e.g. Federal Mortgage Bank of Nigeria - FMBN)", "Specialized financial institutions providing long-term loans for residential housing construction and home ownership (National Housing Fund)", "Provide short-term travel loans", "Finance deep-sea fishing only", "Sell foreign currency at airports"),
            ("Development finance institutions (e.g. Bank of Industry - BOI, Bank of Agriculture - BOA)", "Provide low-interest long-term credit, concessionary facilities, and technical advisory to stimulate strategic industrial and agricultural sectors", "Operate consumer lottery games", "Print legal tender currency", "Offer high-interest pawn loans")
        ]
        for mb_t, mb_d, d1, d2, d3 in extra_mb:
            q_text = f"In monetary economics and financial institutions, what describes the {mb_t.lower()}?"
            opts = {"A": mb_d, "B": d1, "C": d2, "D": d3}
            items.append((
                "Specialized Financial Institutions & Fiscal Mechanics", q_text, opts, "A",
                f"{mb_t}: {mb_d}.",
                "Understand the specific institutional mandate of development banks, sovereign funds, and central bank lender of last resort facilities."
            ))
