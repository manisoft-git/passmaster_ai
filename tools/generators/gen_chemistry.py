import random
import math

def generate_chemistry_questions(topic, count_needed=150):
    items = []

    if topic == "Physical & General Chemistry":
        # 1. Mole concept and mass calculations
        compounds = [
            ("CaCO₃", 100, [10, 20, 25, 50]),
            ("NaOH", 40, [4, 8, 12, 20]),
            ("H₂SO₄", 98, [4.9, 9.8, 19.6, 49.0]),
            ("NaCl", 58.5, [5.85, 11.7, 29.25]),
            ("HCl", 36.5, [3.65, 7.3, 18.25]),
            ("CO₂", 44, [4.4, 8.8, 22.0]),
            ("H₂O", 18, [3.6, 9.0, 36.0])
        ]
        for formula, mm, masses in compounds:
            for mass in masses:
                moles = mass / mm
                q_text = f"Calculate the number of moles in {mass} g of pure {formula}. (Molar mass = {mm} g/mol)"
                opts = {"A": f"{moles:.3f} mol", "B": f"{moles * 2:.3f} mol", "C": f"{mass * mm:.1f} mol", "D": f"{moles / 2:.3f} mol"}
                items.append((
                    "Mole Calculations", q_text, opts, "A",
                    f"Number of moles n = mass / molar mass = {mass} / {mm} = {moles:.3f} mol.",
                    "What is the standard formula relating mass, molar mass, and moles?"
                ))
        # 2. Gas volume at STP (22.4 dm³/mol)
        for mol in [0.25, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]:
            vol = mol * 22.4
            q_text = f"What volume is occupied by {mol} moles of an ideal gas at Standard Temperature and Pressure (STP)? (Molar gas volume = 22.4 dm³)"
            opts = {"A": f"{vol:.2f} dm³", "B": f"{vol / 2:.2f} dm³", "C": f"{vol * 22.4:.1f} dm³", "D": f"{vol * 2:.2f} dm³"}
            items.append((
                "Molar Gas Volume", q_text, opts, "A",
                f"At STP, Volume = moles × 22.4 dm³/mol = {mol} × 22.4 = {vol:.2f} dm³.",
                "Recall that 1 mole of any gas occupies 22.4 dm³ at standard temperature and pressure."
            ))
        # 3. pH and pOH calculations
        ph_values = [1, 2, 3, 4, 5, 8, 9, 10, 11, 12, 13]
        for ph in ph_values:
            poh = 14 - ph
            h_conc = f"1.0 × 10⁻{ph}"
            q_text = f"An aqueous solution has a hydrogen ion concentration [H⁺] of {h_conc} mol/dm³. What is the pH of this solution?"
            opts = {"A": f"{ph}", "B": f"{poh}", "C": f"{ph + 1}", "D": f"{14 + ph}"}
            items.append((
                "pH of Aqueous Solutions", q_text, opts, "A",
                f"pH = -log₁₀[H⁺] = -log₁₀(10⁻{ph}) = {ph}.",
                "How is pH mathematically defined in terms of hydrogen ion concentration?"
            ))
            q_text_poh = f"An aqueous solution has a pH of {ph}. Calculate its pOH at 25°C."
            opts_poh = {"A": f"{poh}", "B": f"{ph}", "C": f"{14 + ph}", "D": f"{7 - ph}"}
            items.append((
                "pOH and Ionic Product of Water", q_text_poh, opts_poh, "A",
                f"At 25°C, pH + pOH = 14. Therefore pOH = 14 - {ph} = {poh}.",
                "What is the sum of pH and pOH for an aqueous solution at standard 25°C?"
            ))
        # 4. Faraday's first law of electrolysis: Q = I * t
        for current in [2, 3, 4, 5]:
            for minutes in [10, 15, 20, 30, 60]:
                seconds = minutes * 60
                coulombs = current * seconds
                q_text = f"A current of {current} A is passed through an electrolytic cell for {minutes} minutes. Calculate the total quantity of electricity passed."
                opts = {"A": f"{coulombs} C", "B": f"{current * minutes} C", "C": f"{coulombs * 2} C", "D": f"{coulombs // 60} C"}
                items.append((
                    "Faraday's Laws of Electrolysis", q_text, opts, "A",
                    f"Quantity Q = I × t = {current} A × ({minutes} × 60 s) = {coulombs} C.",
                    "Always ensure time is converted from minutes into SI seconds before calculating coulombs."
                ))
        # 5. Oxidation numbers
        redox_species = [
            ("KMnO₄", "Mn", "+7", "+4", "+6", "+2", "K is +1, each O is -2. 1 + Mn + 4(-2) = 0 => Mn = +7."),
            ("K₂Cr₂O₇", "Cr", "+6", "+3", "+7", "+4", "2(+1) + 2(Cr) + 7(-2) = 0 => 2Cr = 12 => Cr = +6."),
            ("H₂SO₄", "S", "+6", "+4", "+2", "-2", "2(+1) + S + 4(-2) = 0 => S = +6."),
            ("HNO₃", "N", "+5", "+3", "+4", "-3", "1 + N + 3(-2) = 0 => N = +5."),
            ("ClO₃⁻", "Cl", "+5", "+7", "+3", "-1", "Cl + 3(-2) = -1 => Cl - 6 = -1 => Cl = +5."),
            ("Cr₂O₇²⁻", "Cr", "+6", "+7", "+3", "+4", "2Cr + 7(-2) = -2 => 2Cr = 12 => Cr = +6."),
            ("SO₄²⁻", "S", "+6", "+4", "+2", "-2", "S + 4(-2) = -2 => S - 8 = -2 => S = +6."),
            ("PO₄³⁻", "P", "+5", "+3", "+6", "+4", "P + 4(-2) = -3 => P - 8 = -3 => P = +5."),
            ("NH₄⁺", "N", "-3", "+3", "+5", "-1", "N + 4(+1) = +1 => N + 4 = 1 => N = -3."),
            ("Fe₂O₃", "Fe", "+3", "+2", "+4", "+6", "2(Fe) + 3(-2) = 0 => 2Fe = 6 => Fe = +3.")
        ]
        for compound, elem, ans, d1, d2, d3, exp in redox_species:
            q_text = f"What is the oxidation number of {elem} in the chemical species {compound}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append(("Oxidation States", q_text, opts, "A", exp, f"Set the algebraic sum of oxidation states equal to the net charge of {compound}."))

    elif topic == "Inorganic Chemistry":
        # 1. Flame test colors
        flame_tests = [
            ("Sodium (Na⁺)", "Golden yellow", "Lilac", "Brick-red", "Apple-green"),
            ("Potassium (K⁺)", "Lilac / Pale violet", "Golden yellow", "Crimson", "Blue-green"),
            ("Calcium (Ca²⁺)", "Brick-red", "Apple-green", "Lilac", "Golden yellow"),
            ("Barium (Ba²⁺)", "Apple-green", "Brick-red", "Crimson", "Lilac"),
            ("Copper (Cu²⁺)", "Blue-green", "Lilac", "Golden yellow", "Brick-red"),
            ("Strontium (Sr²⁺)", "Crimson / Bright red", "Apple-green", "Lilac", "Blue-green"),
            ("Lead (Pb²⁺)", "Pale grayish-blue", "Crimson", "Golden yellow", "Lilac")
        ]
        for ion, ans, d1, d2, d3 in flame_tests:
            q_text = f"In qualitative analysis, which characteristic flame color is observed when a platinum wire dipped in a {ion} salt is held in a non-luminous Bunsen flame?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Flame Tests", q_text, opts, "A",
                f"{ion} produces a distinctive {ans.lower()} flame due to electron excitation and emission.",
                f"What color flame is the diagnostic hallmark of {ion}?"
            ))
        # 2. Periodic Trends
        trends = [
            ("Atomic radius across Period 3 (Na to Ar)", "Decreases across the period", "Increases across the period", "Remains constant", "First increases then drops"),
            ("First ionization energy across Period 2 (Li to Ne)", "Generally increases across the period", "Steadily decreases", "Remains unchanged", "Drops to zero"),
            ("Electronegativity down Group 7 (Halogens: F to I)", "Decreases down the group", "Increases down the group", "Remains constant", "Flucutates unpredictably"),
            ("Reactivity of alkali metals (Group 1: Li to Cs)", "Increases down the group", "Decreases down the group", "Is identical for all", "Increases then decreases"),
            ("Electropositivity of alkaline earth metals (Group 2)", "Increases down the group", "Decreases down the group", "Shows no change", "Is highest in Beryllium")
        ]
        for prop, ans, d1, d2, d3 in trends:
            q_text = f"Which statement correctly describes the periodic trend for {prop}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Periodic Trends", q_text, opts, "A",
                f"As nuclear charge and shielding change across periods or down groups, {prop} {ans.lower()}.",
                "Consider effective nuclear charge and number of electron shielding shells."
            ))
        # 3. Anion identification tests
        anion_tests = [
            ("Chloride ion (Cl⁻)", "Forms a white precipitate with aqueous AgNO₃ that dissolves in dilute aqueous NH₃", "Forms a yellow precipitate insoluble in concentrated NH₃", "Produces brown fumes with dilute acid", "Turns moist blue litmus red"),
            ("Sulphate ion (SO₄²⁻)", "Produces a white precipitate with aqueous BaCl₂ that is insoluble in dilute hydrochloric acid", "Forms a red solution with KSCN", "Effervesces violently with cold water", "Turns acidified potassium dichromate green"),
            ("Carbonate ion (CO₃²⁻)", "Liberates a colorless, odorless gas with dilute HCl that turns calcium hydroxide solution (lime water) milky", "Forms a blue precipitate with sodium hydroxide", "Evolves pungent choking ammonia gas", "Turns lead acetate paper black"),
            ("Sulphide ion (S²⁻)", "Liberates H₂S gas with dilute mineral acid which turns moist lead(II) ethanoate paper shiny black", "Bleaches moist litmus paper completely", "Dissolves in ether with an explosion", "Forms a canary yellow precipitate with barium ions"),
            ("Nitrate ion (NO₃⁻)", "Forms a dark brown ring at the interface of concentrated H₂SO₄ and iron(II) sulphate solution", "Produces a purple precipitate with bromine", "Evolves oxygen gas that relights a glowing splint", "Forms an emerald green gelatinous precipitate")
        ]
        for ion, ans, d1, d2, d3 in anion_tests:
            q_text = f"What is the diagnostic laboratory test used to confirm the presence of {ion}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Qualitative Inorganic Analysis", q_text, opts, "A",
                f"The presence of {ion} is confirmed by: {ans}.",
                f"Which confirmatory precipitation or gas reaction identifies {ion}?"
            ))
        # 4. Metallurgy and metal extraction
        metal_extractions = [
            ("Iron from Haematite (Fe₂O₃)", "Carbon monoxide reduction in a blast furnace", "Electrolysis of molten ore", "Displacement by copper metal", "Decomposition by sunlight"),
            ("Aluminium from Bauxite (Al₂O₃·2H₂O)", "Electrolytic reduction of alumina dissolved in molten cryolite (Hall-Héroult process)", "Reduction with carbon at room temperature", "Roasting with sulfur dioxide", "Fractional distillation of its vapor"),
            ("Sodium from rock salt (NaCl)", "Electrolysis of molten NaCl in the Downs cell", "Electrolysis of aqueous NaCl using copper electrodes", "Reduction with limestone in a blast furnace", "Direct heating of sodium oxide"),
            ("Copper from chalcopyrite (CuFeS₂)", "Smelting in a reverberatory furnace followed by electrolytic refining", "Simple filtration and sun drying", "Electrolysis of sea water", "Direct reaction with nitrogen gas")
        ]
        for metal, ans, d1, d2, d3 in metal_extractions:
            q_text = f"Which industrial method is employed for the primary extraction of {metal}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Extraction of Metals", q_text, opts, "A",
                f"{metal} is commercially extracted by {ans.lower()}.",
                "Does the reactivity of the metal determine whether chemical reduction or electrolysis is required?"
            ))
        # 5. Water hardness
        hardness_items = [
            ("Temporary hardness of water", "Dissolved calcium and magnesium hydrogen carbonates [Ca(HCO₃)₂]", "Dissolved sodium chloride and potassium sulphate", "Suspended clay and insoluble sand", "Dissolved copper sulphate"),
            ("Permanent hardness of water", "Dissolved calcium and magnesium sulphates and chlorides [CaSO₄, MgCl₂]", "Suspended calcium carbonate", "Gaseous carbon dioxide", "Dissolved sodium carbonate"),
            ("Removal of temporary water hardness", "Simple boiling or adding calculated slaked lime [Ca(OH)₂]", "Adding dilute hydrochloric acid", "Adding sand and gravel", "Passing oxygen gas"),
            ("Removal of permanent water hardness", "Addition of washing soda (Na₂CO₃) or using ion-exchange resin (Zeolite)", "Simple boiling alone", "Passing chlorine gas", "Filtering through filter paper")
        ]
        for term, ans, d1, d2, d3 in hardness_items:
            q_text = f"What is responsible for, or causes the {term.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Water Hardness & Treatment", q_text, opts, "A",
                f"{term} is characterized by: {ans}.",
                "Differentiate between temporary hydrogencarbonate hardness and permanent sulphate hardness."
            ))

    elif topic == "Organic Chemistry":
        # 1. Homologous series and formulas
        series_data = [
            ("alkanes", "C_n H_{2n+2}", "C_n H_{2n}", "C_n H_{2n-2}", "C_n H_{2n+1}OH"),
            ("alkenes", "C_n H_{2n}", "C_n H_{2n+2}", "C_n H_{2n-2}", "C_n H_{2n-1}"),
            ("alkynes", "C_n H_{2n-2}", "C_n H_{2n}", "C_n H_{2n+2}", "C_n H_{2n-4}"),
            ("alkanols (aliphatic alcohols)", "C_n H_{2n+1}OH", "C_n H_{2n}O₂", "C_n H_{2n-1}OH", "C_n H_{2n+2}"),
            ("alkanoic acids (carboxylic acids)", "C_n H_{2n+1}COOH", "C_n H_{2n}O", "C_n H_{2n-1}COOH", "C_n H_{2n+2}O")
        ]
        for name, ans, d1, d2, d3 in series_data:
            q_text = f"What is the general molecular formula representing the homologous series of {name}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Homologous Series", q_text, opts, "A",
                f"The homologous series of {name} has general formula {ans}.",
                "Count the ratio of carbon to hydrogen atoms in this functional family."
            ))
        # 2. IUPAC Nomenclature
        iupac_samples = [
            ("CH₃-CH(CH₃)-CH₂-CH₃", "2-methylbutane", "3-methylbutane", "pentane", "dimethylpropane"),
            ("CH₃-CH₂-CH(OH)-CH₃", "butan-2-ol", "butan-1-ol", "2-hydroxybutane", "butyl alcohol"),
            ("CH₃-C(CH₃)₂-CH₃", "2,2-dimethylpropane", "2-methylbutane", "neopentane", "trimethylmethane"),
            ("CH₃-CH=CH-CH₃", "but-2-ene", "but-1-ene", "butene", "dimethylacetylene"),
            ("CH₃-CH₂-CHO", "propanal", "propanone", "propanoic acid", "propanol"),
            ("CH₃-CO-CH₃", "propanone", "propanal", "propanoic acid", "propan-2-ol"),
            ("CH₃-CH₂-COOH", "propanoic acid", "ethanoic acid", "propanoic ester", "propanal"),
            ("CH₃-COO-CH₂-CH₃", "ethyl ethanoate", "methyl propanoate", "propyl methanoate", "diethyl ketone"),
            ("CH≡C-CH₂-CH₃", "but-1-yne", "but-2-yne", "pentyne", "butane"),
            ("CH₃-CH(Cl)-CH₂-CH₃", "2-chlorobutane", "3-chlorobutane", "chlorobutane", "1-chlorobutane")
        ]
        for formula, ans, d1, d2, d3 in iupac_samples:
            q_text = f"What is the correct systematic IUPAC name of the compound with structural formula {formula}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "IUPAC Nomenclature", q_text, opts, "A",
                f"Longest continuous carbon chain and lowest substituent numbering gives {ans}.",
                "Find the longest carbon chain containing the principal functional group."
            ))
        # 3. Organic Chemical Tests
        tests_data = [
            ("unsaturation in alkenes and alkynes", "Decolourization of reddish-brown bromine water (Br₂/H₂O)", "Formation of a silver mirror with Tollens' reagent", "Effervescence of CO₂ with sodium hydrogencarbonate", "Evolution of ammonia gas"),
            ("aldehydes (distinguishing from ketones)", "Formation of a brick-red precipitate of Cu₂O with Fehling's solution", "Decolourization of bromine water without light", "Formation of a sweet smelling ester with alcohol", "Evolution of hydrogen gas with zinc"),
            ("terminal alkynes (containing -C≡C-H)", "Formation of a reddish-brown precipitate with ammoniacal copper(I) chloride", "Decolourization of alkaline litmus", "Evolution of sulfur dioxide", "Dissolving in concentrated nitric acid"),
            ("carboxylic acids (-COOH)", "Effervescence of carbon dioxide gas with aqueous NaHCO₃ turning lime water milky", "Silver mirror formation", "Decolourizing bromine water immediately", "Giving a purple color with neutral FeCl₃")
        ]
        for analyte, ans, d1, d2, d3 in tests_data:
            q_text = f"Which experimental observation confirms the presence of {analyte}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Qualitative Organic Tests", q_text, opts, "A",
                f"Diagnostic identification of {analyte}: {ans}.",
                f"Which specific reagent gives a distinctive color change or precipitate with {analyte}?"
            ))
        # 4. Polymers and Polymerization
        polymers = [
            ("Polythene", "Ethene (CH₂=CH₂)", "Ethyne", "Ethanol", "Ethanoic acid", "Addition polymerization"),
            ("Polyvinyl chloride (PVC)", "Chloroethene (vinyl chloride)", "1,2-dichloroethane", "Tetrachloroethene", "Chloromethane", "Addition polymerization"),
            ("Nylon-6,6", "Hexanedioic acid and hexane-1,6-diamine", "Ethene and benzene", "Glucose and fructose", "Amino acids", "Condensation polymerization with elimination of water"),
            ("Terylene (Dacron)", "Benzene-1,4-dicarboxylic acid and ethane-1,2-diol", "Phenol and methanal", "Ethene and styrene", "Glycerol and fatty acids", "Condensation polyester polymerization")
        ]
        for poly, monomer, d1, d2, d3, m_type in polymers:
            q_text = f"What is the monomer unit from which the synthetic polymer {poly} is manufactured?"
            opts = {"A": monomer, "B": d1, "C": d2, "D": d3}
            items.append((
                "Polymer Chemistry", q_text, opts, "A",
                f"{poly} is formed by {m_type.lower()} of {monomer}.",
                f"Identify the repeating monomer building block of {poly}."
            ))

    elif topic == "Environmental & Industrial Chemistry":
        # 1. Industrial manufacturing processes
        ind_processes = [
            ("Haber-Bosch Process", "Ammonia (NH₃)", "Iron (Fe) catalyst, ~450°C, 200 atm", "N₂ + 3H₂ ⇌ 2NH₃", "Nitric acid", "Sulfuric acid", "Fertilizer"),
            ("Contact Process", "Sulfuric acid (H₂SO₄)", "Vanadium(V) oxide (V₂O₅), ~450°C, 1-2 atm", "2SO₂ + O₂ ⇌ 2SO₃", "Ammonia", "Hydrochloric acid", "Detergent"),
            ("Solvay Process", "Sodium trioxocarbonate(IV) (Na₂CO₃)", "Brine, ammonia, and carbon dioxide from limestone", "2NaHCO₃ → Na₂CO₃ + H₂O + CO₂", "Caustic soda", "Bleaching powder", "Glass"),
            ("Ostwald Process", "Trioxonitrate(V) acid (HNO₃)", "Platinum-Rhodium gauze catalyst, ~850°C", "4NH₃ + 5O₂ → 4NO + 6H₂O", "Sulfuric acid", "Ammonia", "Explosives"),
            ("Downs Process", "Metallic Sodium and Chlorine gas", "Electrolysis of molten NaCl with CaCl₂ flux", "2NaCl → 2Na + Cl₂", "Caustic soda", "Bauxite", "Chemicals")
        ]
        for name, product, cond, rxn, d1, d2, d3 in ind_processes:
            q_text = f"The industrial {name} is globally utilized for the large-scale synthesis of which chemical product?"
            opts = {"A": product, "B": d1, "C": d2, "D": d3}
            items.append((
                "Industrial Chemical Synthesis", q_text, opts, "A",
                f"{name} produces {product}. Conditions: {cond}; Reaction: {rxn}.",
                f"Which major industrial compound is synthesized via {name}?"
            ))
            q_text_cat = f"Which catalyst and primary reaction condition are employed in the industrial {name}?"
            opts_cat = {"A": cond, "B": "Nickel at room temperature", "C": "Copper at 1000°C without pressure", "D": "Platinum in cold water"}
            items.append((
                "Industrial Catalysis", q_text_cat, opts_cat, "A",
                f"Operating parameters for {name}: {cond}.",
                f"Recall the specific catalyst and temperature used in {name}."
            ))
        # 2. Petroleum Fractions
        fractions = [
            ("Refinery gas (C₁ - C₄)", "Domestic heating and bottled cooking gas (LPG)", "Motor car fuel", "Jet engine fuel", "Road surfacing"),
            ("Petrol / Gasoline (C₄ - C₁₂)", "Fuel for internal combustion automobile spark-ignition engines", "Aircraft turbine fuel", "Lubricant for engines", "Tar for roofing"),
            ("Kerosene / Paraffin (C₁₁ - C₁₆)", "Aviation turbojet fuel and domestic lighting/stoves", "Car engine fuel", "Asphalt surfacing", "Candle wax"),
            ("Diesel / Gas oil (C₁₅ - C₁₉)", "Fuel for heavy trucks, buses, trains, and diesel generators", "Cooking gas", "Solvent for paints", "Lubricant"),
            ("Bitumen / Asphalt (> C₂₅)", "Road surfacing and roof waterproofing", "Car engine petrol", "Aviation kerosene", "Bottled gas")
        ]
        for frac, use, d1, d2, d3 in fractions:
            q_text = f"In the fractional distillation of crude crude petroleum, what is the primary economic use of the {frac} fraction?"
            opts = {"A": use, "B": d1, "C": d2, "D": d3}
            items.append((
                "Petroleum Refining & Fractions", q_text, opts, "A",
                f"The {frac} fraction is commercially utilized as {use.lower()}.",
                f"What is the boiling range and key application of {frac}?"
            ))
        # 3. Environmental Pollution & Greenhouse Effect
        pollutants = [
            ("Acid rain", "Sulfur dioxide (SO₂) and nitrogen dioxide (NO₂)", "Methane and neon", "Argon and helium", "Carbon monoxide only"),
            ("Global warming & Enhanced Greenhouse Effect", "Carbon dioxide (CO₂) and Methane (CH₄)", "Nitrogen and oxygen", "Ozone and helium", "Sulfur trioxide"),
            ("Stratospheric ozone layer depletion", "Chlorofluorocarbons (CFCs) releasing active chlorine radicals", "Carbon dioxide emissions", "Excessive water vapor", "Dust particles"),
            ("Carbon monoxide (CO) physiological toxicity", "Combines irreversibly with blood hemoglobin to form carboxyhemoglobin, preventing oxygen transport", "Destroys bone marrow", "Precipitates calcium in bones", "Causes immediate kidney failure"),
            ("Eutrophication of aquatic water bodies", "Excessive runoff of nitrogenous and phosphate artificial fertilizers promoting algal blooms and oxygen depletion", "Thermal heating from power plants", "Acid rain leaching mercury", "Spill of crude petroleum")
        ]
        for hazard, cause, d1, d2, d3 in pollutants:
            q_text = f"What is the direct chemical etiology or primary agent responsible for {hazard.lower()}?"
            opts = {"A": cause, "B": d1, "C": d2, "D": d3}
            items.append((
                "Environmental Chemistry & Pollution", q_text, opts, "A",
                f"{hazard} is primarily triggered by: {cause}.",
                f"Which pollutant is directly implicated in {hazard.lower()}?"
            ))

    append_extra_chemistry(items, topic)
    append_combinatorial_chemistry(items, topic)
    append_deep_chemistry(items, topic)
    append_even_more_chemistry(items, topic)
    append_final_env_chemistry(items, topic)
    return items

def append_extra_chemistry(items, topic):
    if topic == "Physical & General Chemistry":
        # Graham's Law of Diffusion: R1 / R2 = sqrt(M2 / M1)
        gas_pairs = [
            ("Hydrogen (H₂, M=2)", "Oxygen (O₂, M=32)", "4", "16", "2", "8"),
            ("Methane (CH₄, M=16)", "Sulphur dioxide (SO₂, M=64)", "2", "4", "8", "0.5"),
            ("Helium (He, M=4)", "Oxygen (O₂, M=32)", "2.83", "8", "4", "1.41"),
            ("Carbon monoxide (CO, M=28)", "Carbon dioxide (CO₂, M=44)", "1.25", "1.57", "2.0", "0.8")
        ]
        for g1, g2, ans, d1, d2, d3 in gas_pairs:
            q_text = f"According to Graham's law of diffusion, how many times faster will {g1} diffuse compared to {g2} under identical conditions?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Graham's Law of Diffusion", q_text, opts, "A",
                f"Rate ratio = √(M₂ / M₁) = √(M({g2.split('(')[1].split(',')[0]}) / M({g1.split('(')[1].split(',')[0]})) = {ans}.",
                "Recall Graham's law: Rate of diffusion is inversely proportional to square root of molar mass or density."
            ))
        # Le Chatelier equilibrium shifts
        eq_scenarios = [
            ("N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol)", "Increasing total pressure", "Shifts right toward products (fewer gas moles)", "Shifts left", "No effect", "Stops the reaction"),
            ("N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92 kJ/mol)", "Increasing reaction temperature", "Shifts left toward reactants (endothermic reverse)", "Shifts right", "No effect", "Increases ammonia yield"),
            ("2SO₂(g) + O₂(g) ⇌ 2SO₃(g) (exothermic)", "Removing SO₃ as it forms", "Shifts right to replace removed product", "Shifts left", "Decreases reaction rate to zero", "Increases oxygen concentration"),
            ("N₂O₄(g, colorless) ⇌ 2NO₂(g, brown) (endothermic)", "Heating the gas mixture", "Shifts right, turning mixture darker brown", "Shifts left, turning colorless", "No color change", "Precipitates solid nitrogen"),
            ("H₂(g) + I₂(g) ⇌ 2HI(g)", "Increasing external pressure", "Has no effect on equilibrium position (equal gas moles on both sides)", "Shifts right", "Shifts left", "Destroys HI")
        ]
        for rxn, disturbance, ans, d1, d2, d3 in eq_scenarios:
            q_text = f"For the equilibrium system {rxn}, what is the effect of {disturbance.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Le Chatelier's Principle", q_text, opts, "A",
                f"According to Le Chatelier's principle, {disturbance.lower()} {ans.lower()}.",
                "Consider whether the forward reaction is exo/endothermic and count total moles of gas on each side."
            ))

    elif topic == "Inorganic Chemistry":
        # Electronic configurations
        configs = [
            ("Sodium (Na, Z=11)", "1s² 2s² 2p⁶ 3s¹", "1s² 2s² 2p⁵ 3s²", "1s² 2s² 2p⁶ 3p¹", "[Ne] 3p¹"),
            ("Chlorine (Cl, Z=17)", "1s² 2s² 2p⁶ 3s² 3p⁵", "1s² 2s² 2p⁶ 3s¹ 3p⁶", "[Ne] 3s² 3p⁶", "1s² 2s² 2p⁶ 3d⁷"),
            ("Calcium (Ca, Z=20)", "[Ar] 4s²", "[Ar] 3d²", "[Ne] 3s² 3p⁶ 4s¹", "[Ar] 4p²"),
            ("Chromium (Cr, Z=24)", "[Ar] 3d⁵ 4s¹ (anomalous half-filled stability)", "[Ar] 3d⁴ 4s²", "[Ar] 3d⁶", "[Ar] 4s² 4p⁴"),
            ("Copper (Cu, Z=29)", "[Ar] 3d¹⁰ 4s¹ (anomalous fully-filled d stability)", "[Ar] 3d⁹ 4s²", "[Ar] 3d⁸ 4s² 4p¹", "[Ar] 4s² 3d⁹"),
            ("Iron (Fe, Z=26)", "[Ar] 3d⁶ 4s²", "[Ar] 3d⁸", "[Ar] 3d⁷ 4s¹", "[Ar] 4s² 4p⁶"),
            ("Zinc (Zn, Z=30)", "[Ar] 3d¹⁰ 4s²", "[Ar] 3d⁸ 4s² 4p²", "[Ar] 3d¹²", "[Ar] 4s² 4d¹⁰"),
            ("Aluminium (Al, Z=13)", "1s² 2s² 2p⁶ 3s² 3p¹", "1s² 2s² 2p⁶ 3s³", "[Ne] 3p³", "1s² 2s² 2p⁵ 3s² 3p²"),
            ("Phosphorus (P, Z=15)", "1s² 2s² 2p⁶ 3s² 3p³", "[Ne] 3s¹ 3p⁴", "[Ne] 3p⁵", "1s² 2s² 2p⁶ 3d⁵"),
            ("Argon (Ar, Z=18)", "1s² 2s² 2p⁶ 3s² 3p⁶", "[Ne] 3s² 3p⁵ 4s¹", "[Ne] 3d⁸", "1s² 2s² 2p⁶ 3s¹ 3p⁷")
        ]
        for elem, ans, d1, d2, d3 in configs:
            q_text = f"What is the ground-state electronic configuration of {elem}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Electronic Configurations", q_text, opts, "A",
                f"Ground state configuration of {elem} follows Aufbau principle and Hund's rule: {ans}.",
                "Follow the Aufbau sequence: 1s, 2s, 2p, 3s, 3p, 4s, 3d."
            ))
        # Oxides classification
        oxides = [
            ("Aluminium oxide (Al₂O₃)", "Amphoteric oxide (reacts with both acids and strong bases)", "Acidic oxide", "Basic oxide", "Neutral oxide"),
            ("Zinc oxide (ZnO)", "Amphoteric oxide (reacts with both HCl and NaOH)", "Basic oxide only", "Acidic oxide only", "Peroxide"),
            ("Lead(II) oxide (PbO)", "Amphoteric oxide", "Neutral oxide", "Acidic oxide", "Superoxide"),
            ("Carbon monoxide (CO)", "Neutral oxide (does not form salts with acids or bases)", "Acidic oxide", "Basic oxide", "Amphoteric oxide"),
            ("Dinitrogen monoxide (N₂O)", "Neutral oxide", "Acidic oxide", "Basic oxide", "Amphoteric oxide"),
            ("Sulphur dioxide (SO₂)", "Acidic oxide (dissolves in water to form trioxosulphate(IV) acid)", "Basic oxide", "Amphoteric oxide", "Neutral oxide"),
            ("Calcium oxide (CaO, quicklime)", "Basic oxide (reacts with acids to form salt and water)", "Acidic oxide", "Amphoteric oxide", "Neutral oxide"),
            ("Sodium oxide (Na₂O)", "Strongly basic oxide", "Acidic oxide", "Amphoteric oxide", "Neutral oxide")
        ]
        for oxide, ans, d1, d2, d3 in oxides:
            q_text = f"How is {oxide} chemically classified based on its acid-base behavior?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Classification of Oxides", q_text, opts, "A",
                f"{oxide} is an {ans.lower()}.",
                "Does this oxide react with acids, bases, both, or neither?"
            ))
        # Drying agents
        drying = [
            ("Ammonia gas (NH₃)", "Quicklime (unslaked lime, CaO)", "Concentrated H₂SO₄", "Fused CaCl₂", "Phosphorus(V) oxide"),
            ("Chlorine gas (Cl₂)", "Concentrated H₂SO₄ or fused CaCl₂", "Quicklime (CaO)", "Aqueous sodium hydroxide", "Potassium hydroxide pellets"),
            ("Hydrogen chloride gas (HCl)", "Concentrated H₂SO₄", "Quicklime (CaO)", "Ammonia solution", "Fused sodium hydroxide"),
            ("Sulphur dioxide gas (SO₂)", "Concentrated H₂SO₄", "Calcium oxide pellets", "Ammoniacal copper chloride", "Sodium hydroxide")
        ]
        for gas, ans, d1, d2, d3 in drying:
            q_text = f"Which drying agent must be used to dry laboratory samples of {gas} without chemical reaction occurring?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Laboratory Gas Preparation & Drying", q_text, opts, "A",
                f"{gas} is dried using {ans} because it does not chemically react with the gas.",
                "Ensure the drying agent does not react acid-base with the gas."
            ))

    elif topic == "Organic Chemistry":
        # Combustion equations
        for c, h, name in [(1, 4, "Methane (CH₄)"), (2, 6, "Ethane (C₂H₆)"), (3, 8, "Propane (C₃H₈)"), (4, 10, "Butane (C₄H₁₀)")]:
            o2_moles = c + h / 4
            o2_str = f"{o2_moles}" if o2_moles.is_integer() else f"{int(o2_moles*2)}/2"
            q_text = f"In the balanced equation for complete combustion of 1 mole of {name}, how many moles of oxygen (O₂) are required?"
            opts = {"A": f"{o2_moles:.1f}", "B": f"{c:.1f}", "C": f"{h / 2:.1f}", "D": f"{c + h:.1f}"}
            items.append((
                "Combustion of Alkanes", q_text, opts, "A",
                f"General formula: C_x H_y + (x + y/4)O₂ → x CO₂ + y/2 H₂O. For {name}, moles of O₂ = {c} + {h}/4 = {o2_moles:.1f}.",
                "Balance carbon into CO₂ and hydrogen into H₂O, then count total oxygen atoms."
            ))
        # Functional group transformations
        transformations = [
            ("Primary alkanol (e.g. ethanol) with acidified K₂Cr₂O₇ under reflux", "Alkanoic acid (ethanoic acid)", "Alkanone (ketone)", "Ester", "Alkene"),
            ("Primary alkanol with acidified K₂Cr₂O₇ distilled immediately", "Alkanal (acetaldehyde / ethanal)", "Carboxylic acid", "Ester", "Alkane"),
            ("Secondary alkanol (e.g. propan-2-ol) with acidified KMnO₄", "Alkanone (propanone / acetone)", "Alkanal", "Alkanoic acid", "Alkene"),
            ("Tertiary alkanol (e.g. 2-methylpropan-2-ol) with strong oxidizing agents", "Resistant to oxidation under mild conditions (no alpha hydrogen)", "Alkanone", "Alkanal", "Carboxylic acid"),
            ("Ethanol heated with excess concentrated H₂SO₄ at 170°C", "Ethene (CH₂=CH₂) via elimination / dehydration", "Ethoxyethane (diethyl ether)", "Ethanoic acid", "Ethyl sulphate"),
            ("Ethanol heated with concentrated H₂SO₄ at 140°C in excess alcohol", "Ethoxyethane (diethyl ether) via intermolecular dehydration", "Ethene", "Ethanal", "Methane"),
            ("Reaction between ethanoic acid and ethanol in presence of concentrated H₂SO₄", "Ethyl ethanoate (ester) + water", "Ethene + water", "Diethyl ether", "Ethanal"),
            ("Alkaline hydrolysis of glyceryl tristearate (fat) with aqueous NaOH (Saponification)", "Sodium stearate (soap) and propane-1,2,3-triol (glycerol)", "Methanol and fatty acid", "Ethanol and soap", "Carbon dioxide and wax")
        ]
        for reactant, ans, d1, d2, d3 in transformations:
            q_text = f"What is the major organic product formed by {reactant}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Organic Reactions & Mechanisms", q_text, opts, "A",
                f"Reaction outcome: {ans}.",
                "Identify the classification of the starting material and reaction conditions."
            ))

    elif topic == "Environmental & Industrial Chemistry":
        # Water treatment stages
        water_stages = [
            ("Coagulation and flocculation of suspended clay particles", "Alum (potassium aluminium sulphate) or iron(III) sulphate", "Chlorine gas", "Sand filtration", "Activated carbon"),
            ("Disinfection and destruction of pathogenic bacteria in municipal water", "Chlorine gas (Cl₂) or sodium hypochlorite (NaOCl)", "Quicklime", "Copper sulphate", "Alum"),
            ("Adjustment of acidic pH in municipal water after treatment", "Slaked lime [Ca(OH)₂] or soda ash (Na₂CO₃)", "Hydrochloric acid", "Concentrated sulphuric acid", "Alum"),
            ("Removal of objectionable tastes, odors, and dissolved organic toxins", "Activated charcoal / carbon adsorption", "Simple boiling", "Chlorination", "Screening mesh")
        ]
        for goal, ans, d1, d2, d3 in water_stages:
            q_text = f"In modern municipal water purification plants, which chemical or unit operation is utilized for {goal.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Water Purification Technology", q_text, opts, "A",
                f"{goal} is achieved by using {ans.lower()}.",
                "Recall standard municipal water treatment sequences."
            ))
        # Heavy metals and toxicity
        toxic_metals = [
            ("Lead (Pb) poisoning from leaded petrol and old plumbing pipes", "Damage to central nervous system, cognitive impairment in children, anemia", "Minamata sensory ataxia", "Itai-itai brittle bone disease", "Thyroid goiter"),
            ("Mercury (Hg) industrial aquatic bioaccumulation (Minamata disease)", "Severe neurological damage, paresthesia, cerebellar ataxia, loss of motor control", "Lead line on gums", "Rickets", "Sickle cell crisis"),
            ("Cadmium (Cd) chronic environmental contamination (Itai-itai disease)", "Severe osteomalacia, painful bone fractures, and renal tubular dysfunction", "Dental fluorosis", "Goiter", "Asthma")
        ]
        for hazard, symptom, d1, d2, d3 in toxic_metals:
            q_text = f"What clinical syndrome or pathological effect is directly associated with {hazard}?"
            opts = {"A": symptom, "B": d1, "C": d2, "D": d3}
            items.append((
                "Heavy Metal Toxicology", q_text, opts, "A",
                f"{hazard} results in: {symptom}.",
                "Match the toxic heavy metal to its characteristic clinical disorder."
            ))
        # Cement and inorganic chemical industries
        cement_topics = [
            ("Gypsum (CaSO₄·2H₂O) added in Portland cement manufacture", "To retard and regulate the setting time of cement", "To accelerate the hardening speed", "To impart grey color", "To reduce production cost"),
            ("Limestone (CaCO₃) and shale/clay heated in a rotary cement kiln", "Produce cement clinker composed of calcium silicates and aluminates", "Form pure quicklime", "Synthesize baking soda", "Produce glass"),
            ("Major components of ordinary soda-lime glass", "Silica sand (SiO₂), soda ash (Na₂CO₃), and limestone (CaCO₃)", "Alumina and cryolite", "Gypsum and clay", "Pure carbon and iron")
        ]
        for topic_name, ans, d1, d2, d3 in cement_topics:
            q_text = f"Why is {topic_name}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Heavy Chemical & Building Materials Industry", q_text, opts, "A",
                f"{topic_name}: {ans}.",
                "Consider the inorganic chemical role of gypsum in cement hydration."
            ))

def append_combinatorial_chemistry(items, topic):
    if topic == "Inorganic Chemistry":
        # Transition metal ion colors
        tm_colors = [
            ("Iron(II) [Fe²⁺]", "Pale green", "Yellow-brown", "Deep blue", "Pink"),
            ("Iron(III) [Fe³⁺]", "Yellowish-brown / reddish-brown", "Pale green", "Colorless", "Deep violet"),
            ("Copper(II) [Cu²⁺]", "Blue", "Green", "Colorless", "Yellow"),
            ("Chromium(III) [Cr³⁺]", "Green", "Pale pink", "Golden yellow", "Colorless"),
            ("Manganese(II) [Mn²⁺]", "Faint pink / almost colorless", "Deep blue", "Orange", "Dark brown"),
            ("Cobalt(II) [Co²⁺]", "Pink in aqueous solution", "Pale green", "Yellow", "Colorless"),
            ("Nickel(II) [Ni²⁺]", "Bright apple-green", "Blue", "Red", "Colorless"),
            ("Zinc(II) [Zn²⁺]", "Colorless (d¹⁰ fully filled subshell)", "Green", "Blue", "Pink")
        ]
        for ion_name, col, d1, d2, d3 in tm_colors:
            q_text = f"What is the characteristic color of hydrated {ion_name} ions in aqueous solution?"
            opts = {"A": col, "B": d1, "C": d2, "D": d3}
            items.append((
                "Transition Metal Chemistry", q_text, opts, "A",
                f"{ion_name} exhibits a {col.lower()} color due to d-d electron transitions.",
                "Relate d-orbital electron configuration to light absorption in aqueous complex ions."
            ))
        # Complex ions
        complexes = [
            ("Tetraamminecopper(II) ion, [Cu(NH₃)₄]²⁺", "Deep royal blue", "Pale green", "Colorless", "Yellow"),
            ("Diamminesilver(I) ion, [Ag(NH₃)₂]⁺ (Tollens' complex)", "Colorless linear complex", "Deep blue", "Bright red", "Pale yellow"),
            ("Hexacyanoferrate(II) ion, [Fe(CN)₆]⁴⁻", "Pale yellow octahedral complex", "Deep green", "Violet", "Colorless"),
            ("Hexacyanoferrate(III) ion, [Fe(CN)₆]³⁻", "Ruby red / orange-red octahedral complex", "Pale blue", "Colorless", "Green"),
            ("Tetrahydroxozincate(II) ion, [Zn(OH)₄]²⁻", "Colorless soluble amphoteric complex", "Deep blue precipitate", "Green solution", "Brown suspension")
        ]
        for comp_name, col, d1, d2, d3 in complexes:
            q_text = f"What is the optical appearance of the coordination complex {comp_name}?"
            opts = {"A": col, "B": d1, "C": d2, "D": d3}
            items.append((
                "Coordination Compounds", q_text, opts, "A",
                f"{comp_name} appears as a {col.lower()}.",
                "Identify the characteristic color and geometry of this transition metal complex."
            ))
        # Solubility rules
        sol_cases = [
            ("Lead(II) chloride (PbCl₂)", "Insoluble in cold water, but readily dissolves in boiling water", "Completely soluble at all temperatures", "Insoluble in boiling water", "Decomposes explosively in water"),
            ("Barium sulphate (BaSO₄)", "Completely insoluble in water and concentrated acids", "Highly soluble in cold water", "Slightly soluble in ethanol only", "Forms a clear blue solution"),
            ("Silver chloride (AgCl)", "Insoluble white precipitate, dissolves in dilute aqueous ammonia", "Freely soluble in cold water", "Soluble in benzene", "Soluble only in molten sulfur"),
            ("Calcium sulphate (CaSO₄)", "Sparingly soluble in water", "Completely insoluble in hot water", "Highly deliquescent", "Gas at room temperature"),
            ("All nitrate salts (e.g. NaNO₃, KNO₃, Cu(NO₃)₂)", "Completely soluble in water without exception", "Insoluble in water", "Soluble only in alcohol", "Soluble only when heated")
        ]
        for salt_name, ans, d1, d2, d3 in sol_cases:
            q_text = f"What is the water solubility characteristic of {salt_name}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Solubility Rules", q_text, opts, "A",
                f"{salt_name}: {ans}.",
                "Recall general solubility guidelines for common inorganic salts."
            ))
        # Periodic group characteristics
        pg_data = [
            ("Group 1 (Alkali Metals)", "1 valence electron, forms M⁺ cations, highly electropositive, stored under paraffin oil", "2 valence electrons", "Forms M²⁻ anions", "Transition elements"),
            ("Group 2 (Alkaline Earth Metals)", "2 valence electrons, forms M²⁺ cations, less reactive than Group 1", "1 valence electron", "Forms covalent hydrides only", "Inert gases"),
            ("Group 17 (Halogens)", "7 valence electrons, forms X⁻ halide anions, powerful oxidizing agents", "1 valence electron", "Forms basic oxides", "Liquid metals"),
            ("Group 18 (Noble / Inert Gases)", "Complete octet (ns²np⁶), chemically unreactive monoatomic gases", "Forms diatomic ions", "Strong reducing agents", "Forms acidic halides readily")
        ]
        for grp, ans, d1, d2, d3 in pg_data:
            q_text = f"Which set of properties accurately characterizes the elements of {grp}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Periodic Group Characteristics", q_text, opts, "A",
                f"Elements in {grp} possess {ans.lower()}.",
                "Count outer valence electrons and determine redox nature."
            ))

    elif topic == "Organic Chemistry":
        # Functional group recognition
        fg_pairs = [
            ("-OH (hydroxyl group)", "Alkanol (Alcohol)", "Alkanoic acid", "Alkanal", "Ester"),
            ("-CHO (formyl / carbonyl at terminal carbon)", "Alkanal (Aldehyde)", "Alkanone", "Alkanol", "Amine"),
            ("-CO- (carbonyl bonded to two carbon atoms)", "Alkanone (Ketone)", "Alkanal", "Carboxylic acid", "Ether"),
            ("-COOH (carboxyl group)", "Alkanoic acid (Carboxylic acid)", "Ester", "Alkanone", "Amide"),
            ("-COO- (alkoxycarbonyl group)", "Alkanoate (Ester)", "Ether", "Carboxylic acid", "Anhydride"),
            ("-O- (alkoxy bridge between two alkyl groups)", "Ether (Alkoxyalkane)", "Ester", "Ketone", "Alcohol"),
            ("-NH₂ (amino group)", "Aliphatic Amine", "Amide", "Nitrile", "Nitroalkane"),
            ("-CONH₂ (carboxamide group)", "Amide", "Amine", "Amino acid", "Imine"),
            ("-C≡C- (carbon-carbon triple bond)", "Alkyne", "Alkene", "Alkane", "Arene"),
            ("-C=C- (carbon-carbon double bond)", "Alkene", "Alkyne", "Alkane", "Cycloalkane")
        ]
        for sym, fam, d1, d2, d3 in fg_pairs:
            q_text = f"The characteristic functional group {sym} defines which organic homologous class?"
            opts = {"A": fam, "B": d1, "C": d2, "D": d3}
            items.append((
                "Functional Group Identification", q_text, opts, "A",
                f"{sym} is the diagnostic functional group of {fam.lower()}.",
                "Identify the structural functional group linkage."
            ))
        # Haloalkanes IUPAC
        halo_examples = [
            ("CH₃-CH₂-CH₂-Br", "1-bromopropane", "2-bromopropane", "bromobutane", "propyl bromide"),
            ("CH₃-CH(Br)-CH₃", "2-bromopropane", "1-bromopropane", "bromopropane", "isopropyl butane"),
            ("CH₃-CH₂-CH(Cl)-CH₃", "2-chlorobutane", "1-chlorobutane", "3-chlorobutane", "chlorobutane"),
            ("CH₃-C(CH₃)(Cl)-CH₃", "2-chloro-2-methylpropane", "1-chloro-2-methylpropane", "2-chlorobutane", "chloro-tert-butane"),
            ("CH₃-CH₂-CH₂-CH₂-I", "1-iodobutane", "2-iodobutane", "butyl iodide", "1-iodopentane"),
            ("CH₃-CH(I)-CH₂-CH₃", "2-iodobutane", "3-iodobutane", "1-iodobutane", "iodobutane"),
            ("CH₃-CH₂-CH₂-OH", "propan-1-ol", "propan-2-ol", "propanal", "propyl alcohol"),
            ("CH₃-CH(OH)-CH₃", "propan-2-ol", "propan-1-ol", "propanone", "isopropanol")
        ]
        for struct, ans, d1, d2, d3 in halo_examples:
            q_text = f"Assign the correct IUPAC nomenclature to the halogenated or hydroxylated alkane {struct}."
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Substituted Hydrocarbon Nomenclature", q_text, opts, "A",
                f"Number the chain from the end nearest the substituent to obtain {ans}.",
                "Give the principal substituent the lowest possible locant number."
            ))
        # Benzene reactions
        arene_rxns = [
            ("Nitration of benzene (C₆H₆ + HNO₃)", "Concentrated H₂SO₄ catalyst at 55°C to form nitrobenzene", "Iron catalyst at 200°C", "Sunlight without acid", "Aqueous sodium hydroxide"),
            ("Bromination of benzene (C₆H₆ + Br₂)", "Iron(III) bromide (FeBr₃) halogen carrier catalyst to form bromobenzene", "UV light at 0°C", "Nickel catalyst at 400°C", "Alkaline solution"),
            ("Friedel-Crafts alkylation of benzene (C₆H₆ + CH₃Cl)", "Anhydrous aluminium chloride (AlCl₃) catalyst to form methylbenzene (toluene)", "Platinum at 100°C", "Concentrated HCl", "Zinc amalgam")
        ]
        for rxn_name, ans, d1, d2, d3 in arene_rxns:
            q_text = f"Which reagents and catalyst are required for the electrophilic aromatic {rxn_name.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Aromatic Chemistry & Electrophilic Substitution", q_text, opts, "A",
                f"{rxn_name} requires: {ans}.",
                "Recall the Lewis acid catalyst required for electrophilic aromatic substitution."
            ))

    elif topic == "Environmental & Industrial Chemistry":
        # Specific pollutants and effects
        env_details = [
            ("Chlorofluorocarbons (CFCs) in the stratosphere", "Release free chlorine radicals under UV irradiation that catalyze ozone decomposition (Cl• + O₃ → ClO• + O₂)", "Dissolve in clouds to form acid rain", "Absorb infrared radiation to turn sky red", "React with nitrogen to form ammonia"),
            ("Oxides of nitrogen (NO and NO₂) in urban atmospheres", "Catalyze the photochemical synthesis of secondary ground-level ozone and PAN in photochemical smog", "Neutralize acid rain", "Purify drinking water", "Deplete oxygen in rivers directly"),
            ("Carbon dioxide accumulation in oceans (ocean acidification)", "Forms carbonic acid (H₂CO₃), lowering seawater pH and dissolving calcium carbonate shells of marine organisms", "Turns seawater purple", "Increases ocean salinity by 50%", "Eliminates all aquatic algae"),
            ("Biochemical Oxygen Demand (BOD) metric", "Measures the amount of dissolved oxygen consumed by aerobic microorganisms to decompose organic matter in a water sample", "Measures water temperature", "Indicates acidity of drinking water", "Quantifies suspended sand"),
            ("Thermal pollution in aquatic environments", "Elevated water temperature decreases the solubility of dissolved oxygen, suffocating fish and aquatic fauna", "Increases ice formation", "Lowers chemical reaction rates", "Eliminates all bacteria")
        ]
        for title, ans, d1, d2, d3 in env_details:
            q_text = f"What is the precise environmental consequence or chemical mechanism of {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Atmospheric & Aquatic Pollution Chemistry", q_text, opts, "A",
                f"{title}: {ans}.",
                "Analyze the biological and chemical impact of this pollutant."
            ))
        # Renewable vs non-renewable
        energy_q = [
            ("Renewable energy resource", "Biogas from anaerobic digestion of organic matter", "Crude petroleum", "Anthracite coal", "Natural gas (LPG)"),
            ("Non-renewable fossil fuel", "Bituminous coal formed from prehistoric vegetative compression", "Solar photovoltaic power", "Geothermal steam", "Wind energy"),
            ("Advantage of green hydrogen as fuel", "Burns cleanly in oxygen yielding only pure water vapor with zero greenhouse gas emissions", "Easier to store than coal", "Cheaper than firewood", "Does not require oxygen to combust")
        ]
        for prompt_e, ans, d1, d2, d3 in energy_q:
            q_text = f"Which of the following is classified as an authentic {prompt_e.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Energy Resources & Green Chemistry", q_text, opts, "A",
                f"{prompt_e}: {ans}.",
                "Distinguish between replenishable renewable sources and finite fossil fuels."
            ))

def append_deep_chemistry(items, topic):
    if topic == "Inorganic Chemistry":
        # Valency and formula prediction
        elem_groups = [
            ("an alkali metal X (valency 1)", "oxide", "X₂O", "XO", "XO₂", "X₂O₃"),
            ("an alkaline earth metal Y (valency 2)", "chloride", "YCl₂", "YCl", "YCl₃", "Y₂Cl"),
            ("a trivalent element Z (valency 3)", "oxide", "Z₂O₃", "ZO₃", "Z₃O₂", "ZO"),
            ("a trivalent element M (valency 3)", "sulphate", "M₂(SO₄)₃", "MSO₄", "M(SO₄)₂", "M₃SO₄"),
            ("a tetravalent element Q (valency 4)", "oxide", "QO₂", "Q₂O", "QO₄", "Q₂O₃"),
            ("a divalent metal A (valency 2)", "trioxonitrate(V)", "A(NO₃)₂", "ANO₃", "A₂(NO₃)₃", "A₃NO₃"),
            ("a monovalent metal K (valency 1)", "trioxophosphate(V)", "K₃PO₄", "KPO₄", "K₂(PO₄)₃", "K(PO₄)₂"),
            ("a divalent metal B (valency 2)", "phosphate", "B₃(PO₄)₂", "BPO₄", "B₂(PO₄)₃", "B(PO₄)₂")
        ]
        for desc, comp_type, ans, d1, d2, d3 in elem_groups:
            q_text = f"What is the empirical chemical formula of the {comp_type} formed by {desc}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Chemical Formula Prediction", q_text, opts, "A",
                f"Balancing valencies between {desc} and {comp_type} gives {ans}.",
                "Criss-cross the combining valencies to balance ionic charges."
            ))
        # Gas preparation reactions
        gas_preps = [
            ("Oxygen (O₂)", "Catalytic thermal decomposition of KClO₃ using MnO₂ catalyst", "Reaction of copper with dilute acid", "Heating limestone with sand", "Passing steam over red-hot coke"),
            ("Chlorine (Cl₂)", "Action of concentrated HCl on manganese(IV) oxide (MnO₂) with gentle heating", "Heating ammonium chloride", "Dissolving sulfur in water", "Electrolysis of pure water"),
            ("Carbon dioxide (CO₂)", "Action of dilute hydrochloric acid on calcium carbonate marble chips", "Heating iron in air", "Decomposition of sodium chloride", "Reaction of copper with water"),
            ("Hydrogen (H₂)", "Action of dilute hydrochloric or sulphuric acid on granulated zinc metal", "Heating copper oxide", "Burning sulfur in air", "Action of water on mercury"),
            ("Ammonia (NH₃)", "Heating a mixture of ammonium chloride (NH₄Cl) and calcium hydroxide (slaked lime)", "Direct action of nitric acid on iron", "Decomposition of urea in cold water", "Electrolysis of brine"),
            ("Hydrogen sulphide (H₂S)", "Action of dilute hydrochloric acid on iron(II) sulphide (FeS)", "Oxidation of sulfur with nitric acid", "Heating copper sulphate", "Action of lime on salt"),
            ("Sulphur dioxide (SO₂)", "Action of dilute hydrochloric acid on sodium trioxosulphate(IV) (Na₂SO₃)", "Heating charcoal in steam", "Decomposition of water", "Oxidation of ammonia")
        ]
        for g_name, ans, d1, d2, d3 in gas_preps:
            q_text = f"Which standard laboratory method is used to prepare pure dry samples of {g_name}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Laboratory Preparation of Gases", q_text, opts, "A",
                f"{g_name} is prepared by: {ans}.",
                "Recall the reagents and conditions used for laboratory gas synthesis."
            ))

    elif topic == "Organic Chemistry":
        # Molar mass formula determinations
        # Alkanes: M = 14n + 2
        for n, m_val in [(1, 16), (2, 30), (3, 44), (4, 58), (5, 72), (6, 86), (7, 100)]:
            f_str = f"C{n}H{2*n + 2}"
            q_text = f"An open-chain alkane has a relative molecular mass of {m_val}. Determine its molecular formula. (C = 12, H = 1)"
            opts = {"A": f_str, "B": f"C{n}H{2*n}", "C": f"C{n}H{2*n - 2}", "D": f"C{n+1}H{2*n+4}"}
            items.append((
                "Alkane Molar Mass", q_text, opts, "A",
                f"General formula C_n H_{{2n+2}}: 12n + 2n + 2 = {m_val} => 14n = {m_val - 2} => n = {n}. Formula is {f_str}.",
                "Set 14n + 2 equal to the given molecular mass."
            ))
        # Alkenes: M = 14n
        for n, m_val in [(2, 28), (3, 42), (4, 56), (5, 70), (6, 84)]:
            f_str = f"C{n}H{2*n}"
            q_text = f"An aliphatic alkene has a molar mass of {m_val} g/mol. What is its molecular formula? (C = 12, H = 1)"
            opts = {"A": f_str, "B": f"C{n}H{2*n + 2}", "C": f"C{n}H{2*n - 2}", "D": f"C{n+1}H{2*n+2}"}
            items.append((
                "Alkene Molar Mass", q_text, opts, "A",
                f"General formula C_n H_{{2n}}: 14n = {m_val} => n = {n}. Formula is {f_str}.",
                "Divide alkene molecular mass by 14 to find carbon count n."
            ))
        # Alkanols: M = 14n + 18
        for n, m_val in [(1, 32), (2, 46), (3, 60), (4, 74), (5, 88)]:
            f_str = f"C{n}H{2*n + 1}OH"
            q_text = f"A monohydric alkanol has a molecular mass of {m_val} g/mol. What is its molecular formula? (C = 12, H = 1, O = 16)"
            opts = {"A": f_str, "B": f"C{n}H{2*n}O", "C": f"C{n}H{2*n+2}O₂", "D": f"C{n+1}H{2*n+3}OH"}
            items.append((
                "Alkanol Molecular Formula", q_text, opts, "A",
                f"Formula C_n H_{{2n+1}}OH has mass 14n + 18 = {m_val} => 14n = {m_val - 18} => n = {n}. Formula is {f_str}.",
                "Subtract 18 (mass of H2O equivalent) and divide by 14."
            ))
        # Percentage carbon
        for name, c_atoms, h_atoms, mm in [
            ("methane (CH₄)", 1, 4, 16),
            ("ethane (C₂H₆)", 2, 6, 30),
            ("propane (C₃H₈)", 3, 8, 44),
            ("ethene (C₂H₄)", 2, 4, 28),
            ("ethyne (C₂H₂)", 2, 2, 26),
            ("benzene (C₆H₆)", 6, 6, 78)
        ]:
            pct_c = (c_atoms * 12 / mm) * 100
            q_text = f"Calculate the percentage by mass of carbon in {name}. (C = 12, H = 1)"
            opts = {"A": f"{pct_c:.1f}%", "B": f"{100 - pct_c:.1f}%", "C": f"{pct_c / 2:.1f}%", "D": f"{pct_c * 0.8:.1f}%"}
            items.append((
                "Percentage Composition of Hydrocarbons", q_text, opts, "A",
                f"% Carbon = (Total mass of C / Molar mass) × 100% = ({c_atoms*12} / {mm}) × 100% = {pct_c:.1f}%.",
                "Divide total carbon mass by molar mass of compound."
            ))

    elif topic == "Environmental & Industrial Chemistry":
        # Ores and Minerals
        ores = [
            ("Bauxite", "Aluminium (Al)", "Al₂O₃·2H₂O", "Iron", "Copper", "Tin"),
            ("Haematite", "Iron (Fe)", "Fe₂O₃", "Aluminium", "Lead", "Zinc"),
            ("Magnetite", "Iron (Fe)", "Fe₃O₄", "Copper", "Silver", "Gold"),
            ("Chalcopyrite (copper pyrites)", "Copper (Cu)", "CuFeS₂", "Tin", "Iron only", "Lead"),
            ("Cassiterite (tinstone)", "Tin (Sn)", "SnO₂", "Titanium", "Lead", "Zinc"),
            ("Galena", "Lead (Pb)", "PbS", "Iron", "Aluminium", "Mercury"),
            ("Sphalerite (zinc blende)", "Zinc (Zn)", "ZnS", "Lead", "Copper", "Tin"),
            ("Calamine", "Zinc (Zn)", "ZnCO₃", "Calcium", "Magnesium", "Copper"),
            ("Dolomite", "Calcium and Magnesium (Ca & Mg)", "CaCO₃·MgCO₃", "Sodium", "Iron", "Aluminium"),
            ("Rock salt (halite)", "Sodium (Na)", "NaCl", "Potassium", "Lithium", "Calcium")
        ]
        for ore_name, metal, formula, d1, d2, d3 in ores:
            q_text = f"From which mineral ore is {metal} primarily extracted industrially? ({formula})"
            opts = {"A": ore_name, "B": d1, "C": d2, "D": d3}
            items.append((
                "Mineral Ores of Metals", q_text, opts, "A",
                f"{metal} is extracted from {ore_name} ({formula}).",
                f"Identify the primary commercial mineral ore of {metal}."
            ))
            q_text_chem = f"What is the chemical composition / formula of the mineral ore {ore_name}?"
            opts_chem = {"A": formula, "B": "NaCl", "C": "CaSO₄·2H₂O", "D": "SiO₂"}
            items.append((
                "Chemical Formulas of Ores", q_text_chem, opts_chem, "A",
                f"The chemical formula of {ore_name} is {formula}.",
                f"Recall the exact chemical formula of {ore_name}."
            ))
        # Fertilizer percentages
        fertilizers = [
            ("Urea [CO(NH₂)₂]", 28, 60, "46.7%"),
            ("Ammonium nitrate (NH₄NO₃)", 28, 80, "35.0%"),
            ("Ammonium sulphate [(NH₄)₂SO₄]", 28, 132, "21.2%"),
            ("Sodium nitrate (NaNO₃)", 14, 85, "16.5%")
        ]
        for fert_name, n_mass, mm, pct_str in fertilizers:
            q_text = f"Calculate the percentage by mass of active nitrogen in the commercial fertilizer {fert_name}. (N = 14, Molar mass = {mm} g/mol)"
            opts = {"A": pct_str, "B": f"{float(pct_str[:-1])/2:.1f}%", "C": f"{float(pct_str[:-1])*1.5:.1f}%", "D": "50.0%"}
            items.append((
                "Fertilizer Chemistry & Nitrogen Content", q_text, opts, "A",
                f"% N = (Total mass of N / Molar mass) × 100% = ({n_mass} / {mm}) × 100% = {pct_str}.",
                "Multiply the number of nitrogen atoms by 14 and divide by total molar mass."
            ))

def append_even_more_chemistry(items, topic):
    if topic == "Inorganic Chemistry":
        # Group 2 carbonate thermal decomposition
        carb_data = [
            ("CaCO₃ (calcium carbonate)", "CaO (calcium oxide) and CO₂", "Ca metal and O₂", "Ca(OH)₂ and CO", "CaC₂ and O₂"),
            ("MgCO₃ (magnesium carbonate)", "MgO (magnesium oxide) and CO₂", "Mg and CO", "Mg(OH)₂", "Mg₃N₂"),
            ("ZnCO₃ (zinc carbonate)", "ZnO (zinc oxide, yellow when hot, white when cold) and CO₂", "Zn metal and CO", "Zn(OH)₂", "ZnO₂"),
            ("PbCO₃ (lead(II) carbonate)", "PbO (lead(II) oxide, reddish-brown when hot, yellow when cold) and CO₂", "Pb and O₂", "PbO₂ and CO", "Pb₃O₄"),
            ("CuCO₃ (copper(II) carbonate, green)", "CuO (copper(II) oxide, black powder) and CO₂", "Cu metal and O₂", "Cu₂O and CO", "CuSO₄")
        ]
        for c_name, prod, d1, d2, d3 in carb_data:
            q_text = f"What are the thermal decomposition products when solid {c_name} is strongly heated in a test tube?"
            opts = {"A": prod, "B": d1, "C": d2, "D": d3}
            items.append((
                "Thermal Decomposition of Carbonates", q_text, opts, "A",
                f"Heating {c_name} decomposes it into metal oxide and carbon dioxide: {prod}.",
                "Heavy metal and transition metal carbonates decompose upon heating to metal oxide + CO₂."
            ))
        # Nitrogen oxides
        nox = [
            ("Dinitrogen monoxide (N₂O, laughing gas)", "Sweet-smelling neutral gas that relights a glowing splint but less vigorously than O₂", "Pungent suffocating gas", "Brown toxic gas", "Acidic gas turning litmus blue"),
            ("Nitrogen monoxide (NO, nitric oxide)", "Colorless neutral gas that turns reddish-brown immediately on exposure to air/O₂", "Green poisonous gas", "Sweet-smelling liquid", "Alkaline gas"),
            ("Nitrogen dioxide (NO₂)", "Dense reddish-brown acidic toxic gas with a sharp, biting odor", "Colorless odorless gas", "Pale blue gas", "Inert unreactive gas")
        ]
        for name, prop, d1, d2, d3 in nox:
            q_text = f"Which description correctly identifies the physical and chemical properties of {name}?"
            opts = {"A": prop, "B": d1, "C": d2, "D": d3}
            items.append((
                "Oxides of Nitrogen", q_text, opts, "A",
                f"{name}: {prop}.",
                "Recall the colors and redox behaviors of different nitrogen oxides."
            ))

    elif topic == "Organic Chemistry":
        # Additional functional families and reactions
        extra_org = [
            ("Addition of hydrogen gas to vegetable oils in the presence of finely divided nickel catalyst at 180°C", "Margarine (hardened saturated fat)", "Biodiesel", "Soap and glycerol", "Crude petroleum"),
            ("Reaction of an alkyne (e.g. ethyne) with ammoniacal silver trioxonitrate(V)", "White/yellowish precipitate of silver dicarbide (silver acetylide)", "Silver mirror on glass", "Effervescence of hydrogen", "Deep blue complex"),
            ("Enzymatic fermentation of glucose (C₆H₁₂O₆) by zymase in yeast", "Ethanol (C₂H₅OH) and carbon dioxide (CO₂)", "Methanol and water", "Ethanoic acid and oxygen", "Methane and hydrogen"),
            ("Conversion of ethanol to ethanoic acid by atmospheric Acetobacter aceti", "Vinegar production via aerobic oxidation", "Esterification", "Saponification", "Cracking"),
            ("Distinguishing primary, secondary, and tertiary alcohols using Lucas reagent (anhydrous ZnCl₂ in conc HCl)", "Tertiary forms turbidity immediately, secondary in 5 minutes, primary remains clear at room temperature", "Primary forms red color, tertiary forms blue", "Only primary gives precipitates", "No difference in reaction times"),
            ("Reaction of carboxylic acids with phosphorus pentachloride (PCl₅)", "Acyl chloride (acid chloride), POCl₃, and steamy fumes of HCl", "Alkane and phosphoric acid", "Ester and chlorine gas", "Alcohol and phosphorus trichloride"),
            ("Reduction of nitrobenzene (C₆H₅NO₂) using tin (Sn) and concentrated hydrochloric acid", "Phenylamine (aniline / aminobenzene)", "Benzene", "Phenol", "Chlorobenzene"),
            ("Bromination of phenol in aqueous solution", "2,4,6-tribromophenol as a white precipitate with antiseptic odor", "Bromobenzene", "4-bromophenol only", "1,2-dibromocyclohexane")
        ]
        for title, ans, d1, d2, d3 in extra_org:
            q_text = f"What is the major observation or synthetic product resulting from {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Applied Organic Synthesis", q_text, opts, "A",
                f"Reaction result: {ans}.",
                "Analyze the organic reaction conditions and characteristic functional transformation."
            ))

    elif topic == "Environmental & Industrial Chemistry":
        # Cracking and petrochemical processes
        petro = [
            ("Thermal cracking of heavy petroleum gas oil fractions", "High temperature (700-800°C) and pressure to yield lower alkenes (ethene, propene)", "Room temperature with water", "Addition of lime to form solid bitumen", "Cooling to 0°C"),
            ("Catalytic cracking of long-chain alkanes", "Moderate temperature (~500°C) with zeolite / silica-alumina catalyst to yield high-octane branched petrol", "Using sunlight in open tanks", "Reaction with concentrated sulfuric acid", "Passing chlorine gas"),
            ("Catalytic reforming in petroleum refineries", "Conversion of straight-chain aliphatic alkanes into branched-chain and aromatic hydrocarbons to boost octane rating", "Elimination of carbon atoms", "Addition of lead additives", "Dehydration of alcohols"),
            ("Octane rating of 2,2,4-trimethylpentane (isooctane)", "Assigned standard rating of 100 (excellent antiknock properties)", "Assigned 0", "Assigned 50", "Assigned 200"),
            ("Octane rating of straight-chain n-heptane", "Assigned standard baseline rating of 0 (severe engine knocking)", "Assigned 100", "Assigned 75", "Assigned 50")
        ]
        for desc, ans, d1, d2, d3 in petro:
            q_text = f"In industrial petroleum refining, what defines or describes {desc.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Petrochemical Cracking & Reforming", q_text, opts, "A",
                f"{desc}: {ans}.",
                "Understand the industrial rationale behind catalytic cracking and reforming."
            ))
        # Atmospheric layers & ozone
        atmos = [
            ("Troposphere", "Lowest layer of atmosphere (0-12 km), contains 75% of atmospheric mass and all weather phenomena", "Highest layer", "Contains the ozone protective layer", "Has temperature of 1000°C"),
            ("Stratosphere", "Atmospheric layer (12-50 km) housing the protective ozone (O₃) shield that absorbs lethal solar UV-C and UV-B radiation", "Ground-level air layer", "Contains all clouds and rain", "Layer where auroras occur"),
            ("Photochemical smog formulation", "Sunlight acting on nitrogen oxides (NOx) and volatile organic compounds (VOCs) to generate peroxyacetyl nitrate (PAN) and tropospheric ozone", "Acid rain reacting with marble", "Dust storms from Sahara", "Burning of firewood indoors"),
            ("Greenhouse warming mechanism", "Infrared radiation emitted by warm Earth's surface is absorbed and re-radiated by greenhouse gases back towards the surface", "Solar ultraviolet rays trapped by clouds", "Nuclear heat from earth core", "Ozone layer reflection of light")
        ]
        for lyr, ans, d1, d2, d3 in atmos:
            q_text = f"Which definition correctly explains the atmospheric role of the {lyr}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Atmospheric Chemistry", q_text, opts, "A",
                f"{lyr}: {ans}.",
                "Differentiate between troposphere, stratosphere, and greenhouse radiation mechanisms."
            ))
        # Chemical industries in Nigeria
        ind_nig = [
            ("Primary raw material for Nigerian nitrogenous fertilizer plants (e.g. Indorama, Dangote Fertilizer in Eleme/Lekki)", "Abundant domestic natural gas (methane, CH₄) as hydrogen source", "Imported coal", "Limestone from Ewekoro", "Crude palm oil"),
            ("Primary raw material for Nigerian cement complexes (e.g. Obajana, Ibese, Ewekoro)", "Extensive domestic limestone (CaCO₃) and shale/clay deposits", "Imported quartz sand", "Petroleum pitch", "Cryolite ore"),
            ("Major environmental hazard of gas flaring in the Niger Delta region of Nigeria", "Emission of greenhouse gases (CO₂, CH₄), unburnt hydrocarbons, and acid rain (SO₂, NO₂), damaging agricultural soil and roofing sheets", "Depletion of fresh water lakes", "Ozone accumulation in groundwater", "Radioactive fallout"),
            ("Industrial importance of bitumen deposits found in Ondo/Ogun belt of Nigeria", "Raw material for heavy asphalt road paving, roofing waterproofing, and potential synthetic heavy crude oil", "Production of white sugar", "Raw material for table salt", "Synthesis of nylon fabric")
        ]
        for name, fact, d1, d2, d3 in ind_nig:
            q_text = f"What is the key industrial and environmental characteristic of {name.lower()}?"
            opts = {"A": fact, "B": d1, "C": d2, "D": d3}
            items.append((
                "Chemical Industries in Nigeria", q_text, opts, "A",
                f"{name}: {fact}.",
                "Relate local Nigerian natural mineral deposits and industrial chemical processing."
            ))

def append_final_env_chemistry(items, topic):
    if topic == "Environmental & Industrial Chemistry":
        extra_env = [
            ("Thermal decomposition of limestone in Lime Kiln", "Endothermic reaction (CaCO₃ → CaO + CO₂ at ~1000°C)", "Exothermic combustion", "Catalytic hydrogenation", "Polymerization"),
            ("Function of limestone in iron blast furnace", "Thermal decomposition into CaO which reacts with silica sand (SiO₂) impurities to form molten calcium silicate slag (CaSiO₃)", "Provides fuel", "Reduces iron oxide directly", "Acts as cooling agent"),
            ("Slag removal in blast furnace", "Molten slag is less dense than molten pig iron and floats on top, tapped off separately", "Slag sinks to bottom", "Slag is evaporated as gas", "Slag solidifies instantly"),
            ("Cast iron vs Wrought iron carbon content", "Cast iron (pig iron) contains ~3-4% carbon (hard, brittle); wrought iron contains <0.15% carbon (purest commercial malleable iron)", "Cast iron has 0% carbon", "Wrought iron is 10% carbon", "Both have identical carbon percentage"),
            ("Alloy composition of Brass", "Copper (Cu, ~65-70%) and Zinc (Zn, ~30-35%)", "Copper and Tin", "Lead and Tin", "Aluminium and Magnesium"),
            ("Alloy composition of Bronze", "Copper (Cu, ~88-90%) and Tin (Sn, ~10-12%)", "Copper and Zinc", "Iron and Carbon", "Aluminium and Copper"),
            ("Alloy composition of Duralumin", "Aluminium (Al, 95%), Copper (Cu, 4%), Magnesium (Mg), and Manganese (Mn) for aircraft construction", "Copper and Zinc", "Iron and Lead", "Tin and Lead"),
            ("Alloy composition of Solder", "Lead (Pb, ~50%) and Tin (Sn, ~50%) having low melting point for electrical joints", "Copper and Zinc", "Iron and Nickel", "Gold and Silver"),
            ("Alloy composition of Stainless Steel", "Iron (Fe), Chromium (Cr, ~18%), and Nickel (Ni, ~8%) resisting corrosion", "Iron and Lead", "Zinc and Copper", "Aluminium and Tin"),
            ("Soapless detergents (synthetic alkylbenzene sulphonates) advantage over natural soaps", "Do not form insoluble scum (curd) in hard water containing Ca²⁺ and Mg²⁺ ions", "Are 100% edible", "Do not produce lather", "Are made from beef fat"),
            ("Environmental drawback of non-biodegradable branched alkylbenzene sulphonates", "Resist bacterial decomposition, causing persistent foam on rivers and suffocating aquatic life", "Cause radioactive leaks", "Form heavy acid rain", "Absorb carbon dioxide"),
            ("Greenhouse effect of Nitrous oxide (N₂O)", "Atmospheric residence time of over 100 years with 300-fold higher warming potential than CO₂", "Cools down global climate", "Neutralizes methane", "Absorbs cosmic rays only"),
            ("Biodegradable vs non-biodegradable plastics", "Biodegradable plastics are decomposed by natural microbial action into CO₂ and water; non-biodegradable persist for centuries", "Both decompose in one day", "Non-biodegradable are made from starch", "Biodegradable cannot hold liquids"),
            ("Catalytic converter in motor vehicles", "Converts harmful exhaust gases (CO, NOx, unburnt hydrocarbons) into less harmful CO₂, N₂, and H₂O using platinum/rhodium catalysts", "Increases vehicle fuel consumption by 50%", "Removes lead from engine oil", "Turns exhaust into pure oxygen"),
            ("Carbon cycle atmospheric balance", "Photosynthesis removes atmospheric CO₂ while cellular respiration, decomposition, and fossil combustion release CO₂", "Only combustion controls CO₂", "Plants do not respire", "Oceans do not absorb CO₂")
        ]
        for name, ans, d1, d2, d3 in extra_env:
            q_text = f"What is the chemical principle or industrial importance of {name.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Industrial Chemical Principles & Materials", q_text, opts, "A",
                f"{name}: {ans}.",
                "Analyze the metallurgical, alloying, or environmental chemical mechanism."
            ))
