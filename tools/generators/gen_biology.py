import random

def generate_biology_questions(topic, count_needed=150):
    items = []

    if topic == "Cellular Biology & Life Processes":
        # Organelles and functions
        organelles = [
            ("Mitochondrion", "Aerobic cellular respiration and ATP synthesis", "Protein synthesis", "Packaging of secretory vesicles", "Lipid digestion"),
            ("Ribosome", "Protein synthesis by translating mRNA codons", "Photosynthesis", "Intracellular digestion", "Osmoregulation"),
            ("Rough Endoplasmic Reticulum", "Synthesis and intracellular transport of proteins via membrane-bound ribosomes", "Lipid metabolism", "DNA replication", "ATP hydrolysis"),
            ("Smooth Endoplasmic Reticulum", "Lipid and steroid synthesis, and detoxification of drugs/toxins in liver cells", "rRNA synthesis", "Cell wall deposition", "Water storage"),
            ("Golgi Apparatus (Dictyosome)", "Modification, sorting, packaging, and secretion of cellular glycoproteins", "Glycolysis", "Light absorption", "Spindle formation"),
            ("Lysosome", "Intracellular digestion of macromolecules and destruction of damaged organelles (autophagy)", "Protein synthesis", "Ribosome assembly", "Gas exchange"),
            ("Chloroplast", "Photosynthesis: light reactions in thylakoid membranes and Calvin cycle in the stroma", "Aerobic respiration", "Lipid breakdown", "Urea synthesis"),
            ("Nucleolus", "Transcription of ribosomal RNA (rRNA) and assembly of ribosomal subunits", "Cellular movement", "Fat storage", "Starch synthesis"),
            ("Centriole", "Organization of spindle fibers during cell division in animal cells", "Photosynthesis", "Enzyme secretion", "Pollen production"),
            ("Vacuole (enclosed by tonoplast)", "Maintenance of cell turgor pressure, osmotic balance, and storage of cell sap in plant cells", "Cellular respiration", "Lipid synthesis", "Antibody production")
        ]
        for org, role, d1, d2, d3 in organelles:
            q_text = f"Which vital cellular process is carried out specifically by the organelle {org}?"
            opts = {"A": role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Cell Organelles & Functions", q_text, opts, "A",
                f"{org} is responsible for {role.lower()}.",
                f"Identify the specialized physiological role of the {org}."
            ))
            q_text_rev = f"Which cell organelle is primarily responsible for {role.lower()}?"
            opts_rev = {"A": org, "B": d1.split()[0], "C": "Peroxisome", "D": "Centrosome"}
            items.append((
                "Organelle Identification", q_text_rev, opts_rev, "A",
                f"The organelle executing this function is the {org}.",
                "Match the cellular function to its specific ultrastructural organelle."
            ))

        # Osmosis & Cell Turgor
        osmosis_cases = [
            ("Plant cell placed in a strongly hypertonic (concentrated sucrose) solution", "Plasmolysis: water leaves vacuole by osmosis, cytoplasm shrinks away from the cell wall", "Turgidity: cell expands and bursts", "Hemolysis: cell lyses", "Crenation without cell wall separation"),
            ("Plant cell placed in a pure hypotonic (distilled water) environment", "Turgidity: water enters by osmosis until wall pressure balances osmotic potential, preventing lysis", "Plasmolysis", "Deplasmolysis with bursting", "Flaccidity"),
            ("Red blood cell (erythrocyte) placed in a strongly hypotonic solution (pure water)", "Hemolysis: water rapidly enters by endosmosis until the fragile plasma membrane bursts", "Crenation: cell shrivels", "Plasmolysis", "Turgidity maintained by cell wall"),
            ("Red blood cell placed in a strongly hypertonic (concentrated salt) solution", "Crenation: water exits by exosmosis, causing the erythrocyte to shrivel and notch", "Hemolysis", "Plasmolysis with wall detachment", "Swelling without bursting")
        ]
        for cond, ans, d1, d2, d3 in osmosis_cases:
            q_text = f"What physiological phenomenon occurs when a {cond}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Osmotic Phenomena in Living Cells", q_text, opts, "A",
                f"Outcome: {ans}.",
                "Determine the direction of net water movement across the selectively permeable membrane."
            ))

        # Mitosis & Meiosis stages
        stages = [
            ("Chromosomes condense, nuclear envelope breaks down, and spindle fibers begin to form", "Prophase", "Metaphase", "Anaphase", "Telophase"),
            ("Sister chromatids line up singly along the equatorial plane (metaphase plate) of the cell", "Metaphase of Mitosis", "Prophase I", "Anaphase II", "Telophase I"),
            ("Centromeres divide and sister chromatids are pulled apart to opposite poles by spindle fibers", "Anaphase of Mitosis", "Telophase", "Metaphase", "Interphase"),
            ("Nuclear envelopes reassemble around daughter nuclei and cytokinesis usually commences", "Telophase", "Anaphase", "Prophase", "Metaphase"),
            ("Homologous chromosomes synapse to form bivalents and crossing over (chiasmata) occurs", "Prophase I of Meiosis (Pachytene stage)", "Prophase II", "Metaphase I", "Anaphase I"),
            ("Homologous pairs of chromosomes separate and move toward opposite spindle poles while sister chromatids remain attached", "Anaphase I of Meiosis", "Anaphase of Mitosis", "Anaphase II", "Metaphase II")
        ]
        for desc, stg, d1, d2, d3 in stages:
            q_text = f"During eukaryotic cell division, which phase is characterized by: '{desc}'?"
            opts = {"A": stg, "B": d1, "C": d2, "D": d3}
            items.append((
                "Cell Division Stages", q_text, opts, "A",
                f"This event defines {stg}.",
                "Identify which stage of mitotic or meiotic nuclear division exhibits this diagnostic event."
            ))

        # Enzyme properties
        enzyme_facts = [
            ("Lock and key hypothesis of enzyme action", "Substrate molecular shape fits precisely into a rigid, complementary active site on the enzyme", "Enzyme shape changes randomly", "Enzyme is consumed permanently", "Coenzyme acts as substrate"),
            ("Denaturation of enzymes at temperatures above 60°C", "Thermal disruption of tertiary hydrogen bonds and hydrophobic interactions destroys active site geometry", "Freezing of cytoplasmic water", "Breakdown of covalent peptide bonds into amino acids", "Enzyme multiplies uncontrollably"),
            ("Competitive enzyme inhibition", "Inhibitor molecule resembles the substrate and competes directly for the active site, reversible by increasing substrate concentration", "Inhibitor binds allosteric site irreversibly", "Inhibitor destroys enzyme backbone", "Inhibitor doubles reaction velocity"),
            ("Non-competitive enzyme inhibition", "Inhibitor binds to an allosteric site away from the active site, altering the enzyme conformation regardless of substrate concentration", "Inhibitor competes directly for active site", "Increasing substrate overcomes inhibition", "Inhibitor acts as a coenzyme")
        ]
        for name, ans, d1, d2, d3 in enzyme_facts:
            q_text = f"Which statement scientifically explains the {name.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Enzymology & Kinetics", q_text, opts, "A",
                f"{name}: {ans}.",
                "Examine how temperature, pH, or molecular inhibitors affect active site conformation."
            ))

    elif topic == "Human Physiology & Systems":
        # Digestive enzymes
        digestive_enzymes = [
            ("Ptyalin (Salivary amylase)", "Salivary glands into mouth", "Neutral to slightly alkaline (pH 6.8 - 7.0)", "Starch into maltose", "Proteins into peptides"),
            ("Pepsin", "Gastric juice in stomach", "Strongly acidic (pH 1.5 - 2.0, due to HCl)", "Proteins into peptones and polypeptides", "Fats into fatty acids"),
            ("Trypsin", "Pancreatic juice into duodenum", "Alkaline (pH 7.5 - 8.5)", "Proteins and polypeptides into smaller peptides", "Starch into glucose"),
            ("Pancreatic Lipase (Steapsin)", "Pancreatic juice into duodenum", "Alkaline (pH 7.5 - 8.5)", "Emulsified lipids (fats) into fatty acids and glycerol", "Starch into maltose"),
            ("Rennin (Chymosin)", "Gastric juice in infants", "Acidic", "Coagulation / curdling of soluble milk caseinogen into insoluble casein", "Starch digestion"),
            ("Maltase", "Succus entericus (intestinal juice)", "Alkaline", "Maltose into two glucose molecules", "Sucrose into fructose"),
            ("Sucrase (Invertase)", "Succus entericus", "Alkaline", "Sucrose into glucose and fructose", "Lactose into galactose"),
            ("Lactase", "Succus entericus", "Alkaline", "Lactose into glucose and galactose", "Starch into maltose")
        ]
        for enz, site, ph_cond, action, dist in digestive_enzymes:
            q_text = f"What is the specific biochemical catalytic action of {enz} in human digestion?"
            opts = {"A": action, "B": dist, "C": "Synthesis of urea", "D": "Absorption of vitamin B12"}
            items.append((
                "Digestive Enzymes & Substrates", q_text, opts, "A",
                f"{enz} acts in {site.lower()} at {ph_cond.lower()} to catalyze: {action}.",
                f"What substrate does {enz} convert, and what end product is formed?"
            ))

        # Circulatory system
        circ_items = [
            ("Bicuspid (mitral) atrioventricular valve", "Prevents backflow of oxygenated blood from left ventricle into left atrium during ventricular systole", "Right atrium to right ventricle", "Aorta to pulmonary trunk", "Vena cava to right atrium"),
            ("Tricuspid atrioventricular valve", "Prevents backflow of deoxygenated blood from right ventricle into right atrium during ventricular systole", "Left ventricle to aorta", "Left atrium to pulmonary vein", "Coronary sinus to left ventricle"),
            ("Pulmonary artery", "Carries deoxygenated blood from the right ventricle to the lungs for oxygenation (exception to artery rule)", "Carries oxygenated blood to brain", "Transports digested food from ileum", "Drains blood from kidneys"),
            ("Pulmonary vein", "Carries oxygen-rich blood from the lungs into the left atrium (exception to vein rule)", "Carries deoxygenated blood to heart", "Transports bile to duodenum", "Connects liver to vena cava"),
            ("Hepatic portal vein", "Transports nutrient-rich deoxygenated blood directly from the digestive tract (ileum) to the liver for metabolic processing", "Transports bile to gall bladder", "Carries oxygenated blood to kidneys", "Returns blood from brain to heart")
        ]
        for struct, role, d1, d2, d3 in circ_items:
            q_text = f"What is the precise physiological function of the {struct} in human cardiovascular anatomy?"
            opts = {"A": role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Cardiovascular Anatomy & Flow", q_text, opts, "A",
                f"{struct}: {role}.",
                "Trace the path of blood flow and directional valve action through the four chambers."
            ))

        # Endocrine hormones
        hormones = [
            ("Insulin (secreted by beta cells of Islets of Langerhans in pancreas)", "Lowers blood glucose concentration by stimulating cellular uptake and glycogenesis in liver", "Raises blood sugar by glycogenolysis", "Stimulates milk secretion", "Regulates basal metabolic rate"),
            ("Glucagon (secreted by alpha cells of Islets of Langerhans)", "Elevates blood glucose concentration by promoting hepatic glycogenolysis and gluconeogenesis", "Decreases blood glucose", "Controls calcium deposition in bone", "Induces sleep cycles"),
            ("Thyroxine (secreted by thyroid gland)", "Regulates basal metabolic rate (BMR), cellular respiration rate, and physical/mental growth", "Stimulates uterine contraction", "Controls blood sodium levels", "Lowers blood sugar"),
            ("Antidiuretic Hormone (ADH / Vasopressin from posterior pituitary)", "Increases water reabsorption from kidney collecting ducts into blood, producing concentrated urine", "Causes rapid water loss", "Stimulates ovulation", "Promotes milk let-down"),
            ("Adrenaline / Epinephrine (secreted by adrenal medulla)", "Prepares body for 'fight or flight' emergency by increasing heart rate, dilating bronchioles, and raising blood sugar", "Induces deep relaxation", "Stimulates digestive peristalsis", "Lowers blood pressure"),
            ("Aldosterone (secreted by adrenal cortex)", "Promotes active reabsorption of sodium ions (Na⁺) and excretion of potassium (K⁺) in kidney tubules", "Stimulates bone growth", "Regulates iodine uptake", "Lowers blood sugar")
        ]
        for horn, func, d1, d2, d3 in hormones:
            q_text = f"What physiological effect is triggered by the hormone {horn}?"
            opts = {"A": func, "B": d1, "C": d2, "D": d3}
            items.append((
                "Endocrine Regulation & Hormones", q_text, opts, "A",
                f"{horn}: {func}.",
                f"Identify the target organ and homeostatic action of {horn.split('(')[0]}."
            ))

        # Nephron osmoregulation
        nephron_parts = [
            ("Bowman's capsule and Glomerulus (Malpighian body)", "Ultrafiltration of blood plasma under high hydrostatic pressure, excluding blood cells and large plasma proteins", "Selective active reabsorption of glucose", "Secretion of bile", "Countercurrent salt multiplication"),
            ("Proximal Convoluted Tubule (PCT)", "Obligatory selective reabsorption of 100% of filtered glucose, amino acids, and ~80% of water and sodium ions", "Ultrafiltration of large cells", "Final dilution of urine", "Production of aldosterone"),
            ("Loop of Henle (descending and ascending limbs)", "Creation of a hypertonic medullary osmotic gradient via countercurrent multiplier system", "Filtration of proteins", "Reabsorption of glucose only", "Storage of urine before micturition"),
            ("Collecting Duct under influence of ADH", "Facultative reabsorption of water, determining final concentration and volume of excreted urine", "Ultrafiltration", "Reabsorption of amino acids", "Production of urea from ammonia")
        ]
        for part, action, d1, d2, d3 in nephron_parts:
            q_text = f"What is the primary physiological event occurring in the {part}?"
            opts = {"A": action, "B": d1, "C": d2, "D": d3}
            items.append((
                "Renal Physiology & Nephron Mechanics", q_text, opts, "A",
                f"In the {part.split('(')[0].strip()}, {action.lower()}.",
                "Distinguish between ultrafiltration, selective reabsorption, and osmoregulation."
            ))

    elif topic == "Genetics & Evolution":
        # Blood group genetics crosses
        for mom_g, dad_g, child_g, ans_prob in [
            ("I^A i (Heterozygous Group A)", "I^B i (Heterozygous Group B)", "Group O (genotype ii)", "25% (1 in 4)"),
            ("I^A i (Heterozygous Group A)", "I^B i (Heterozygous Group B)", "Group AB (genotype I^A I^B)", "25% (1 in 4)"),
            ("I^A I^A (Homozygous Group A)", "I^B I^B (Homozygous Group B)", "Group AB (genotype I^A I^B)", "100%"),
            ("I^A I^B (Group AB)", "ii (Group O)", "Group O (genotype ii)", "0% (impossible)"),
            ("I^A I^B (Group AB)", "ii (Group O)", "Group A or Group B", "50% each (100% total)"),
            ("I^A i (Heterozygous Group A)", "ii (Group O)", "Group O (genotype ii)", "50% (1 in 2)"),
            ("I^B i (Heterozygous Group B)", "ii (Group O)", "Group B (genotype I^B i)", "50% (1 in 2)")
        ] :
            q_text = f"If a mother with genotype {mom_g} has a child with a father of genotype {dad_g}, what is the probability that their child will have {child_g}?"
            opts = {"A": ans_prob, "B": "75%", "C": "33.3%", "D": "12.5%"}
            items.append((
                "ABO Blood Group Inheritance", q_text, opts, "A",
                f"Punnett square cross of {mom_g} × {dad_g} yields probability of {ans_prob} for {child_g}.",
                "Construct a 2x2 Punnett square combining parental alleles."
            ))

        # Sickle cell crosses
        for dad_sc, mom_sc, child_target, prob_sc in [
            ("HbA HbS (carrier trait)", "HbA HbS (carrier trait)", "HbS HbS (sickle cell disease)", "25% (1 in 4)"),
            ("HbA HbS (carrier trait)", "HbA HbS (carrier trait)", "HbA HbS (carrier sickle cell trait)", "50% (1 in 2)"),
            ("HbA HbS (carrier trait)", "HbA HbS (carrier trait)", "HbA HbA (normal non-carrier)", "25% (1 in 4)"),
            ("HbA HbA (normal)", "HbS HbS (sickle cell disease)", "HbA HbS (carrier trait)", "100%"),
            ("HbA HbA (normal)", "HbS HbS (sickle cell disease)", "HbS HbS (sickle cell disease)", "0% (impossible)")
        ]:
            q_text = f"Two parents with hemoglobin genotypes {dad_sc} and {mom_sc} plan to have a child. What is the mathematical probability that an offspring will inherit {child_target}?"
            opts = {"A": prob_sc, "B": "75%", "C": "100%", "D": "33.3%"}
            items.append((
                "Sickle Cell Genetics", q_text, opts, "A",
                f"Cross of {dad_sc} × {mom_sc} produces offspring in 1 HbAA : 2 HbAS : 1 HbSS ratio. Probability of {child_target} is {prob_sc}.",
                "Recall Mendelian monohybrid codominant inheritance for sickle-cell alleles."
            ))

        # Sex linked conditions
        sex_crosses = [
            ("Carrier female (X^C X^c) and normal male (X^C Y)", "Male child being color-blind (X^c Y)", "50% of male children (25% of all children)", "100% of male children", "0%", "75% of male children"),
            ("Carrier female (X^H X^h) and normal male (X^H Y)", "Female child suffering from hemophilia (X^h X^h)", "0% (all daughters are either normal or carriers)", "50%", "25%", "100%"),
            ("Color-blind father (X^c Y) and homozygous normal mother (X^C X^C)", "Daughters being carriers of color blindness", "100% of daughters", "50% of daughters", "0%", "25% of daughters"),
            ("Color-blind father (X^c Y) and homozygous normal mother (X^C X^C)", "Sons inheriting color blindness from the father", "0% (sons receive Y chromosome from father, not X)", "50%", "100%", "25%")
        ]
        for parents, question_focus, ans, d1, d2, d3 in sex_crosses:
            q_text = f"In sex-linked human inheritance involving {parents}, what is the likelihood of a {question_focus}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Sex-Linked Inheritance", q_text, opts, "A",
                f"Inheritance analysis: {ans}.",
                "Remember that fathers pass their Y chromosome to sons and X chromosome to daughters."
            ))

        # Evidence of evolution
        evo_concepts = [
            ("Homologous structures (e.g. pentadactyl forelimb of human, bat wing, whale flipper, horse leg)", "Divergent evolution: common ancestral skeletal plan modified to serve diverse environmental functions", "Convergent evolution from different origins", "Vestigial organs with no origin", "Artificial selection by man"),
            ("Analogous structures (e.g. wing of butterfly and wing of bird)", "Convergent evolution: structurally dissimilar organs with different developmental origins adapted for the same aerodynamic function", "Divergent evolution from common ancestor", "Homologous evolution", "Atavism"),
            ("Vestigial organs in humans (e.g. vermiform appendix, coccyx, wisdom teeth, auricular ear muscles)", "Rudimentary remnants of once-functional structures in evolutionary ancestors", "Newly evolved adaptations", "Diseased pathological organs", "Analogous adaptations"),
            ("Lamarck's theory of evolution (Inheritance of Acquired Characters)", "Flawed premise that physical changes acquired by an organism during its lifetime are transmitted to offspring", "Natural selection of genetic mutations", "Survival of the fittest through struggle", "Genetic drift in isolated populations"),
            ("Darwinian Natural Selection", "Differential survival and reproductive success of individuals possessing advantageous inherited phenotypic variations", "Use and disuse of bodily organs", "Spontaneous generation of new species", "Transmission of somatic modifications")
        ]
        for topic_e, ans, d1, d2, d3 in evo_concepts:
            q_text = f"Which evolutionary principle is exemplified by {topic_e}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Evolutionary Theories & Anatomical Evidence", q_text, opts, "A",
                f"{topic_e}: {ans}.",
                "Differentiate between homologous (divergent) and analogous (convergent) evolution."
            ))

    elif topic == "Ecology & Environment":
        # Ecological instruments
        instruments = [
            ("Secchi disc", "Water turbidity and depth of light penetration in an aquatic habitat", "Atmospheric pressure", "Wind velocity", "Soil moisture"),
            ("Anemometer", "Wind speed and velocity in a terrestrial biome", "Relative humidity", "Rainfall volume", "Solar radiation"),
            ("Hygrometer (Wet and dry bulb psychrometer)", "Relative humidity of atmospheric air", "Soil acidity", "Wind direction", "Water salinity"),
            ("Quadrat (square sampling frame)", "Population density and frequency of plant species and sessile organisms", "Animal body temperature", "Depth of water", "Soil pH"),
            ("Sweep net", "Catching and sampling active flying and vegetation-dwelling insects", "Plankton density in deep sea", "Soil compaction", "Burrowing worms"),
            ("Rain gauge (pluviometer)", "Total depth of precipitation / rainfall in millimeters over a period", "Humidity percentage", "Wind velocity", "Atmospheric pressure"),
            ("Barometer", "Atmospheric air pressure", "Wind speed", "Water transparency", "Soil porosity")
        ]
        for inst, usage, d1, d2, d3 in instruments:
            q_text = f"Which ecological measurement is determined by using a {inst}?"
            opts = {"A": usage, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ecological Instruments & Sampling", q_text, opts, "A",
                f"A {inst} is calibrated to measure {usage.lower()}.",
                f"Identify the precise physical or biological parameter measured by a {inst}."
            ))

        # Ecological associations
        associations = [
            ("Lichens (mutualistic association of an alga and a fungus)", "Mutualism: alga synthesizes organic food by photosynthesis while fungus absorbs water, minerals, and provides anchorage", "Parasitism: fungus kills alga", "Commensalism: fungus feeds on dead alga", "Predation"),
            ("Rhizobium leguminosarum bacteria inhabiting root nodules of leguminous plants", "Mutualism: bacteria fix atmospheric nitrogen into nitrates for the host plant while receiving organic carbohydrates", "Commensalism", "Ectoparasitism", "Competition"),
            ("Epiphytic orchid growing on the high trunk bark of a tall forest tree", "Commensalism: orchid gains access to sunlight without absorbing nutrients from or harming the host tree", "Parasitism: kills tree", "Mutualism: feeds tree", "Symbiotic predation"),
            ("Remora fish attached to the ventral belly of a marine shark", "Commensalism: remora gains transport and feeding scraps without harming or helping the host shark", "Parasitism", "Mutualism", "Competition"),
            ("Plasmodium falciparum protozoan inside human red blood cells and liver tissue", "Parasitism: parasite derives nutrition and shelter at the physiological expense of the human host", "Mutualism", "Commensalism", "Saprophytism"),
            ("Dodder plant (Cuscuta) or Striga weed growing on sorghum roots", "Parasitism: haustoria penetrate host vascular bundles to siphon manufactured sugars and water", "Mutualism", "Commensalism", "Autotrophy")
        ]
        for title, ans, d1, d2, d3 in associations:
            q_text = f"What type of ecological symbiosis or association is demonstrated by {title}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ecological Associations & Symbiosis", q_text, opts, "A",
                f"{title}: {ans}.",
                "Determine whether both, one, or none of the interacting species benefits or suffers harm."
            ))

        # Nitrogen cycle steps
        n_steps = [
            ("Conversion of soil ammonia (NH₄⁺/NH₃) into nitrites (NO₂⁻)", "Nitrosomonas bacteria via chemoautotrophic oxidation", "Nitrobacter bacteria", "Rhizobium", "Pseudomonas denitrificans"),
            ("Conversion of soil nitrites (NO₂⁻) into plant-absorbable nitrates (NO₃⁻)", "Nitrobacter bacteria via chemoautotrophic oxidation", "Nitrosomonas", "Azotobacter", "Clostridium"),
            ("Conversion of soil nitrates (NO₃⁻) into atmospheric nitrogen gas (N₂) under anaerobic conditions", "Denitrifying bacteria (Pseudomonas denitrificans)", "Nitrifying bacteria", "Nitrogen-fixing bacteria", "Fungi"),
            ("Direct biological fixation of atmospheric nitrogen (N₂) in soil by free-living microbes", "Azotobacter (aerobic) and Clostridium (anaerobic) in soil", "Nitrosomonas", "Pseudomonas", "Yeast")
        ]
        for step_name, ans, d1, d2, d3 in n_steps:
            q_text = f"In the biological nitrogen cycle, which microorganism catalyzes the {step_name.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "The Nitrogen Cycle & Soil Bacteria", q_text, opts, "A",
                f"{step_name}: {ans}.",
                "Differentiate between Nitrosomonas, Nitrobacter, Rhizobium, and Pseudomonas."
            ))

        # Nigerian biomes
        biomes_nig = [
            ("Mangrove Swamp Forest (coastal fringe of Niger Delta)", "Halophytic red and white mangroves (Rhizophora) with prop roots and breathing pneumatophores in saline tidal mud", "Acacia thorn woodland", "Desert scrub with cacti", "Tall grassland without trees"),
            ("Tropical Rainforest (Southern Nigeria: Cross River, Edo, Ondo)", "Dense multi-layered canopy, tall emergent trees (Iroko, Mahogany) with buttress roots, epiphytes, rainfall >2000 mm", "Deciduous thorny scrub", "Scattered baobabs in short grass", "Arid sand dunes"),
            ("Guinea Savanna (Middle Belt of Nigeria: Kaduna, Plateau, Niger)", "Parkland of tall elephant grasses (Andropogon) interspersed with fire-resistant broad-leaved deciduous trees (Lophira)", "Mangrove prop roots", "Dense evergreen canopy with no grass", "Bare sand dunes"),
            ("Sudan Savanna (Northern Nigeria: Kano, Katsina, Sokoto)", "Short feather grasses with scattered drought-tolerant thorny acacia, baobab (Adansonia), and date palms", "Evergreen rainforest", "Stilt-rooted swamp", "Montane mist forest"),
            ("Sahel Savanna (Semi-arid northern border: Borno, Yobe)", "Sparse tussock grasses, thorny scrub, high evaporation, and rainfall under 400 mm per year", "Dense canopy forest", "Tidal mangrove swamp", "Deciduous forest")
        ]
        for b_name, b_desc, d1, d2, d3 in biomes_nig:
            q_text = f"Which distinct ecological and botanical features characterize the {b_name}?"
            opts = {"A": b_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Biomes & Vegetation Zones of Nigeria", q_text, opts, "A",
                f"{b_name} is characterized by: {b_desc}.",
                "Match the Nigerian ecological zone to its characteristic flora and climatic rainfall pattern."
            ))

    append_deep_biology(items, topic)
    append_exhaustive_biology(items, topic)
    append_master_biology(items, topic)
    append_ultimate_biology(items, topic)
    append_comprehensive_biology(items, topic)
    append_finish_biology(items, topic)
    append_absolute_cap_biology(items, topic)
    append_ecology_final_push(items, topic)
    return items

def append_deep_biology(items, topic):
    if topic == "Cellular Biology & Life Processes":
        # Photosynthesis light vs dark stages
        photo_q = [
            ("Light-dependent reaction of photosynthesis in thylakoid grana", "Photolysis of water yielding oxygen gas (O₂), ATP, and reduced NADPH", "Fixation of carbon dioxide into glucose", "Oxidation of glucose into pyruvate", "Production of lactic acid"),
            ("Light-independent reaction (Calvin cycle) in chloroplast stroma", "Fixation of CO₂ by RuBisCO enzyme and reduction using NADPH and ATP to form triose phosphates and glucose", "Photolysis of water", "Generation of ATP from sunlight", "Release of oxygen gas"),
            ("Chlorophyll light absorption spectrum", "Absorbs blue-violet and red wavelengths of light most effectively, reflecting green light", "Absorbs only green light", "Reflects red light", "Absorbs infrared radiation only"),
            ("Source of oxygen gas liberated during oxygenic photosynthesis", "Derived entirely from the photolytic splitting of water molecules (2H₂O → 4H⁺ + 4e⁻ + O₂)", "Derived from atmospheric carbon dioxide (CO₂)", "From glucose breakdown", "From ATP hydrolysis")
        ]
        for title, ans, d1, d2, d3 in photo_q:
            q_text = f"Which biochemical statement accurately describes the {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Photosynthetic Mechanisms", q_text, opts, "A",
                f"{title}: {ans}.",
                "Differentiate between thylakoid light-harvesting reactions and stroma carbon fixation."
            ))

        # Food test reactions
        food_tests = [
            ("Starch test", "Adding iodine solution: immediate color change from yellowish-brown to deep blue-black", "Brick-red precipitate with Benedict's", "Purple color with Biuret", "Translucent grease spot"),
            ("Reducing sugars (e.g. glucose, maltose)", "Boiling with Fehling's or Benedict's solution: color transition from blue through green/yellow to insoluble brick-red Cu₂O precipitate", "Blue-black with iodine", "Violet with Biuret", "White emulsion"),
            ("Proteins (Biuret test)", "Adding dilute sodium hydroxide followed by 1% copper(II) sulphate: appearance of a distinct violet / purple coloration", "Brick-red precipitate", "Blue-black color", "Effervescence of gas"),
            ("Proteins (Millon's test)", "Adding Millon's reagent and warming: white precipitate turning brick-red upon gentle heating", "Purple solution", "Yellow solution", "Grease spot on paper"),
            ("Lipids / Fats (Ethanol emulsion test)", "Dissolving sample in absolute ethanol and decanting into cold water: formation of a cloudy white emulsion", "Brick-red precipitate", "Blue-black color", "Violet color"),
            ("Lipids (Sudan III test)", "Stains fat globules with a distinct bright red color", "Turns purple", "Forms brick-red precipitate", "Bleaches solution clear")
        ]
        for nutrient, ans, d1, d2, d3 in food_tests:
            q_text = f"What is the characteristic laboratory procedure and positive observation for the {nutrient.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Biochemical Food Tests", q_text, opts, "A",
                f"{nutrient}: {ans}.",
                "Identify the diagnostic reagent and color change for this biological macromolecule."
            ))

        # Plant and animal tissues
        tissues = [
            ("Xylem tissue", "Dead, lignified vessel elements and tracheids conducting water and dissolved minerals uniderectionally upward from roots", "Living cells conducting sucrose downwards", "Photosynthetic tissue", "Storage parenchyma"),
            ("Phloem tissue", "Living sieve tube elements and companion cells conducting manufactured organic sucrose bi-directionally (translocation)", "Dead lignified water pipes", "Water absorption from soil", "Cuticular wax production"),
            ("Collenchyma tissue", "Living cells with uneven cellulose and pectin wall thickenings at corners providing flexible mechanical support in young stems", "Dead stone cells in pear fruit", "Rapid water conduction", "Gas exchange"),
            ("Sclerenchyma tissue", "Dead cells with uniformly thick, heavily lignified secondary cell walls providing rigid tensile strength (fibers and sclereids)", "Living storage cells", "Sugar transport", "Chloroplast-containing cells"),
            ("Ciliated columnar epithelium", "Hair-like motile cilia that sweep mucus, trapped dust particles, or ova along respiratory passages and oviducts", "Dead protective keratin layer", "Insulating adipose layer", "Bone formation")
        ]
        for tis, ans, d1, d2, d3 in tissues:
            q_text = f"Which structure and function correctly defines {tis}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Plant & Animal Histology", q_text, opts, "A",
                f"{tis}: {ans}.",
                "Relate tissue cellular structure and wall lignification to physiological function."
            ))

    elif topic == "Human Physiology & Systems":
        # Eye optics and defects
        eye_defects = [
            ("Myopia (Short-sightedness)", "Eyeball is too long or cornea/lens too convex; parallel rays focus in front of the retina; corrected with a concave (diverging) lens", "Parallel rays focus behind retina; corrected with convex lens", "Unequal curvature of cornea", "Loss of lens transparency"),
            ("Hypermetropia (Long-sightedness)", "Eyeball is too short or lens too flat; close rays focus behind the retina; corrected with a convex (converging) lens", "Focus in front of retina", "Corrected with concave lens", "Loss of night vision"),
            ("Astigmatism", "Irregular or non-uniform curvature of the cornea or lens causing distorted vision; corrected with cylindrical lenses", "Excessive eyeball length", "Biconcave lens correction", "Bile accumulation in retina"),
            ("Presbyopia", "Age-related progressive loss of crystalline lens elasticity and ciliary muscle tone, hindering near accommodation; corrected with bifocal lenses", "Infection of conjunctiva", "Clouding of vitreous humor", "Detachment of retina"),
            ("Cataract", "Progressive opacification and clouding of the crystalline eye lens, blocking light transmission; corrected by surgical lens replacement", "Corneal distortion", "Short eyeball", "Lack of rod photoreceptors")
        ]
        for defect, ans, d1, d2, d3 in eye_defects:
            q_text = f"What is the optical etiology, focal point error, and corrective lens for {defect}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Visual Optics & Sensory Defects", q_text, opts, "A",
                f"{defect}: {ans}.",
                "Determine where light rays converge relative to the retina and select the corrective lens."
            ))

        # Ear anatomy
        ear_parts = [
            ("Eustachian tube", "Equalizes atmospheric air pressure between the middle ear cavity and the nasopharynx", "Amplifies sound waves onto oval window", "Detects body rotation", "Maintains static balance"),
            ("Semicircular canals (three fluid-filled bony arches at right angles)", "Detect dynamic angular acceleration and rotational movement of the head", "Equalize middle ear air pressure", "Convey sound vibrations to brain", "Amplify air sound waves"),
            ("Cochlea (spiral fluid-filled canal with Organ of Corti)", "Contains sensory hair cells that transduce sound pressure fluid waves into nerve action potentials", "Detects head orientation to gravity", "Produces ear wax", "Equalizes pressure"),
            ("Ear ossicles (Malleus, Incus, Stapes)", "Transmit and mechanically amplify tympanic sound vibrations across the middle ear onto the membrane of the oval window", "Detect angular rotation", "Balance air pressure", "Secrete perilymph")
        ]
        for ear_p, role, d1, d2, d3 in ear_parts:
            q_text = f"What is the specific physiological responsibility of the {ear_p} in auditory or vestibular mechanics?"
            opts = {"A": role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Auditory & Vestibular Mechanics", q_text, opts, "A",
                f"{ear_p}: {role}.",
                "Distinguish between hearing structures and balance/equilibrium organs."
            ))

        # Thermoregulation
        thermo_cases = [
            ("Cutaneous physiological response to cold environmental temperature", "Vasoconstriction of superficial arterioles, shivering thermogenesis, and cessation of sweat secretion", "Vasodilation of arterioles and heavy sweating", "Increased panting and heat radiation", "Rapid cooling of core blood"),
            ("Cutaneous physiological response to hot environmental temperature", "Vasodilation of superficial arterioles to radiate heat and profuse sweat gland secretion for evaporative cooling", "Vasoconstriction and shivering", "Erection of hairs to trap air", "Suppression of skin blood flow")
        ]
        for cond_t, ans, d1, d2, d3 in thermo_cases:
            q_text = f"What is the body's coordinated {cond_t.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Homeostasis & Skin Thermoregulation", q_text, opts, "A",
                f"{cond_t}: {ans}.",
                "Trace autonomic control of dermal arteriole caliber and sweat gland activation."
            ))

        # Skeletal joints
        joints = [
            ("Ball and socket joint (shoulder and hip joints)", "Freely movable joint allowing multiaxial rotation and movement in all planes (360°)", "Allows movement in one plane only", "Allows rotational movement around a single central pivot", "Completely immovable joint"),
            ("Hinge joint (elbow and knee joints)", "Synovial joint permitting movement in a single angular plane like a door hinge (flexion and extension)", "Allows rotational movement in all directions", "Immovable fibrous joint", "Gliding movement across flat surfaces"),
            ("Pivot joint (joint between atlas and axis cervical vertebrae)", "Permits rotational movement of the head around a central odontoid peg axis ('no' movement)", "Multiaxial 360° rotation", "Flexion and extension only", "Suture joint with no movement"),
            ("Suture joint (cranial bones of skull)", "Immovable fibrous joint where interdigitating bone margins are locked firmly together by collagen fibers", "Freely movable synovial joint", "Hinge joint", "Ball and socket joint")
        ]
        for jt, ans, d1, d2, d3 in joints:
            q_text = f"How is the {jt} mechanically categorized and what range of articulation does it permit?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Skeletal System & Articulations", q_text, opts, "A",
                f"{jt}: {ans}.",
                "Identify the structural type of joint and degrees of freedom of motion."
            ))

    elif topic == "Genetics & Evolution":
        # Chargaff's rules calculations
        for a_pct in [18, 22, 26, 30, 32]:
            t_pct = a_pct
            c_pct = (100 - 2 * a_pct) // 2
            g_pct = c_pct
            q_text = f"A sample of double-stranded DNA is analyzed and found to contain {a_pct}% Adenine. According to Chargaff's rules, what percentage of Cytosine does this DNA contain?"
            opts = {"A": f"{c_pct}%", "B": f"{a_pct}%", "C": f"{a_pct * 2}%", "D": f"{50 - a_pct}%"}
            items.append((
                "Chargaff's Rules & DNA Base Pairing", q_text, opts, "A",
                f"In double-stranded DNA, %A = %T = {a_pct}%. Remaining bases (G + C) = 100% - {2*a_pct}% = {2*c_pct}%. Since %G = %C, Cytosine = {c_pct}%.",
                "Recall base-pairing rules: %A = %T, %G = %C, and all four sum to 100%."
            ))

        # Chromosomal aneuploidy
        aneuploidies = [
            ("Down's syndrome", "Trisomy of chromosome 21 (47, XX+21 or 47, XY+21) caused by meiotic nondisjunction", "Monosomy of X chromosome", "Extra X chromosome in males", "Deletion on chromosome 5"),
            ("Turner's syndrome", "Monosomy of sex chromosomes (45, XO female): sterile female with short stature and webbed neck", "Trisomy 21", "47, XXY male", "Triple X female"),
            ("Klinefelter's syndrome", "Aneuploidy resulting in an extra X chromosome in males (47, XXY): sterile male with hypogonadism and gynecomastia", "45, XO female", "Trisomy 18", "47, XYY male")
        ]
        for name, ans, d1, d2, d3 in aneuploidies:
            q_text = f"What is the genetic and karyotypic etiology of {name}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Chromosomal Mutations & Aneuploidy", q_text, opts, "A",
                f"{name}: {ans}.",
                "Identify total chromosome number and the specific autosome or sex-chromosome non-disjunction."
            ))

        # Natural selection modes
        nat_sel = [
            ("Stabilizing selection", "Favors intermediate average phenotypes while eliminating both extreme phenotypic variations (e.g. human infant birth weights around 3.5 kg)", "Shifts mean phenotype toward one extreme", "Favors both extreme phenotypes", "Eliminates all variations"),
            ("Directional selection", "Favors individuals with phenotypes at one extreme of the distribution curve, shifting allele frequencies in that direction (e.g. antibiotic resistance in bacteria, industrial melanism)", "Favors mean phenotype", "Splits population into two morphs", "Maintains ancestral phenotype"),
            ("Disruptive selection", "Favors individuals at both extremes of phenotypic variation over intermediate individuals, potentially leading to speciation", "Eliminates both extremes", "Favors middle phenotype", "Reduces genetic diversity")
        ]
        for m_name, ans, d1, d2, d3 in nat_sel:
            q_text = f"Which evolutionary trajectory characterizes {m_name.lower()} in a population?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Modes of Natural Selection", q_text, opts, "A",
                f"{m_name}: {ans}.",
                "Observe whether the bell curve narrows, shifts to one side, or bimodal splits."
            ))

    elif topic == "Ecology & Environment":
        # Lincoln-Petersen mark-recapture
        for m, c, r in [(50, 40, 10), (100, 60, 20), (80, 50, 10), (120, 80, 24), (200, 100, 25)]:
            pop_est = (m * c) // r
            q_text = f"In an ecological population study of grasshoppers, {m} individuals are captured, marked, and released. One week later, a second sample of {c} grasshoppers is captured, of which {r} are marked. Estimate the total population size."
            opts = {"A": f"{pop_est}", "B": f"{pop_est * 2}", "C": f"{m + c - r}", "D": f"{pop_est // 2}"}
            items.append((
                "Lincoln-Petersen Mark-Recapture Method", q_text, opts, "A",
                f"Estimated Population N = (M × C) / R = ({m} × {c}) / {r} = {pop_est}.",
                "Apply the Lincoln Index formula: Total Population = (Marked 1st × Total 2nd) / (Marked 2nd)."
            ))

        # Ecological succession
        succ_types = [
            ("Primary ecological succession", "Initiates on newly formed, completely sterile substrates devoid of soil and pre-existing organic life (e.g. cooled volcanic lava, sand dunes, bare rock)", "Occurs after forest fire where soil exists", "Occurs on abandoned farmland", "Occurs in garden pond"),
            ("Secondary ecological succession", "Occurs in an area where a pre-existing community has been cleared by a disturbance (fire, farming) but fertile soil and seed bank remain", "Starts on bare granite rock", "Starts on newly formed volcanic island", "Takes 10,000 years to reach pioneer stage"),
            ("Pioneer species in xerosere succession", "Hardy crustose lichens and pioneer mosses capable of weathering bare rock and establishing organic humus", "Hardwood emergent trees", "Ferns and shrubs", "Herbivorous mammals"),
            ("Climax ecological community", "Terminal, stable, self-perpetuating ecological community in equilibrium with regional macroclimate", "First community on bare rock", "Rapidly changing intermediate community", "Community with only one species")
        ]
        for name, ans, d1, d2, d3 in succ_types:
            q_text = f"Which description scientifically distinguishes {name.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ecological Succession & Pioneer Communities", q_text, opts, "A",
                f"{name}: {ans}.",
                "Determine whether pre-existing soil and seed banks are present or absent."
            ))

        # Soil properties
        soil_props = [
            ("Sandy soil characteristics", "Large coarse particles (>0.2 mm), high permeability, rapid water drainage, poor capillarity, and low nutrient-holding capacity", "Fine particles, poor aeration, waterlogged", "Highest humus content", "Impairs root respiration"),
            ("Clay soil characteristics", "Extremely fine particles (<0.002 mm), high water-holding capacity, poor aeration, slow drainage, prone to waterlogging and compaction", "Large air spaces and rapid drainage", "Cannot retain moisture", "Acidic sand grains"),
            ("Loamy soil for agriculture", "Balanced mixture of sand, clay, silt, and decaying organic humus providing optimum water retention, aeration, and mineral nutrients", "Pure sand with no humus", "Heavily waterlogged clay", "Bare bedrock")
        ]
        for stype, ans, d1, d2, d3 in soil_props:
            q_text = f"Which physical and agronomic features accurately describe {stype}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Edaphic Factors & Soil Ecology", q_text, opts, "A",
                f"{stype}: {ans}.",
                "Correlate soil particle size distribution with aeration and moisture retention."
            ))

def append_exhaustive_biology(items, topic):
    if topic == "Cellular Biology & Life Processes":
        # Chromosome counts
        org_chroms = [
            ("Human (Homo sapiens)", 46, 23, 69),
            ("Fruit fly (Drosophila melanogaster)", 8, 4, 12),
            ("Garden pea (Pisum sativum)", 14, 7, 21),
            ("Maize (Zea mays)", 20, 10, 30),
            ("Domestic dog (Canis lupus)", 78, 39, 117),
            ("House mouse (Mus musculus)", 40, 20, 60),
            ("Tomato (Solanum lycopersicum)", 24, 12, 36)
        ]
        for org_name, diploid, haploid, triploid in org_chroms:
            q_text = f"If the diploid (2n) somatic chromosome count of {org_name} is {diploid}, how many chromosomes are present in its mature gametes (sperm/egg)?"
            opts = {"A": f"{haploid}", "B": f"{diploid}", "C": f"{diploid * 2}", "D": f"{haploid - 1}"}
            items.append((
                "Chromosomal Ploidy & Gametogenesis", q_text, opts, "A",
                f"Gametes are haploid (n = 2n / 2) = {diploid} / 2 = {haploid}.",
                "Meiotic reduction division halves the chromosome number from diploid (2n) to haploid (n)."
            ))
            q_text_tri = f"For the flowering plant {org_name} with diploid 2n = {diploid}, how many chromosomes are found in its triploid (3n) seed endosperm nucleus?"
            opts_tri = {"A": f"{triploid}", "B": f"{diploid}", "C": f"{haploid}", "D": f"{diploid * 2}"}
            items.append((
                "Endosperm Ploidy", q_text_tri, opts_tri, "A",
                f"Endosperm is triploid (3n) resulting from double fertilization: 3 × (haploid {haploid}) = {triploid}.",
                "Endosperm forms by fusion of one sperm nucleus (n) with two polar nuclei (2n)."
            ))

        # Vitamin deficiencies
        vitamins = [
            ("Vitamin A (Retinol)", "Night blindness (nyctalopia) and xerophthalmia (dry cornea)", "Scurvy", "Rickets", "Beriberi"),
            ("Vitamin B1 (Thiamine)", "Beriberi: muscular weakness, peripheral neuropathy, and cardiac failure", "Pellagra", "Pernicious anemia", "Goiter"),
            ("Vitamin B3 (Niacin / Nicotinic acid)", "Pellagra: characterized by the 3Ds (Dermatitis, Diarrhea, and Dementia)", "Scurvy", "Rickets", "Night blindness"),
            ("Vitamin C (Ascorbic acid)", "Scurvy: defective collagen synthesis leading to bleeding swollen gums, petechiae, and impaired wound healing", "Beriberi", "Night blindness", "Osteomalacia"),
            ("Vitamin D (Calciferol)", "Rickets in growing children (bow legs, pigeon chest) and osteomalacia in adults", "Scurvy", "Pellagra", "Hemophilia"),
            ("Vitamin K (Phylloquinone)", "Defective synthesis of prothrombin in liver resulting in prolonged bleeding and hemorrhagic disease", "Night blindness", "Goiter", "Beriberi"),
            ("Mineral Iron (Fe²⁺)", "Microcytic hypochromic anemia due to impaired hemoglobin synthesis", "Rickets", "Goiter", "Scurvy"),
            ("Mineral Iodine", "Endemic goiter (hyperplasia of thyroid gland) and cretinism in infants", "Anemia", "Beriberi", "Pellagra")
        ]
        for vit, def_disease, d1, d2, d3 in vitamins:
            q_text = f"A chronic nutritional deficiency of {vit} in the human diet directly causes which clinical disorder?"
            opts = {"A": def_disease, "B": d1, "C": d2, "D": d3}
            items.append((
                "Nutritional Deficiencies & Vitamins", q_text, opts, "A",
                f"Deficiency of {vit} causes: {def_disease}.",
                f"Identify the classic nutritional deficiency syndrome linked to {vit.split('(')[0]}."
            ))

    elif topic == "Human Physiology & Systems":
        # Blood group donor/recipient
        bg_compat = [
            ("Blood Group O (Rh-negative)", "Universal blood donor: red blood cells lack A, B, and Rh antigens, so they will not be agglutinated by recipient antibodies", "Universal recipient", "Can donate only to AB", "Cannot donate to anyone"),
            ("Blood Group AB (Rh-positive)", "Universal blood recipient: blood plasma lacks anti-A, anti-B, and anti-Rh antibodies", "Universal donor", "Can receive from AB only", "Can donate to Group O"),
            ("Blood Group A", "Possesses A antigens on red blood cells and anti-B antibodies in plasma", "Possesses B antigens", "Lacks all antigens", "Possesses anti-A antibodies"),
            ("Blood Group B", "Possesses B antigens on red blood cells and anti-A antibodies in plasma", "Possesses A antigens", "Universal donor", "Contains both anti-A and anti-B")
        ]
        for bg_type, fact_bg, d1, d2, d3 in bg_compat:
            q_text = f"What is the immunogenetic immunological characteristic of {bg_type}?"
            opts = {"A": fact_bg, "B": d1, "C": d2, "D": d3}
            items.append((
                "ABO Blood Group Compatibility", q_text, opts, "A",
                f"{bg_type}: {fact_bg}.",
                "Check the surface antigens on RBCs and the circulating antibodies in plasma."
            ))

        # Excretory structures across animal kingdom
        excretory_organs = [
            ("Flatworms (Planaria / Tapeworm)", "Flame cells (protonephridia) with tufts of beating cilia", "Malpighian tubules", "Nephridia", "Kidneys"),
            ("Earthworm (Annelida)", "Metanephridia with ciliated nephrostomes in each segment", "Flame cells", "Green glands", "Malpighian tubules"),
            ("Insects (Cockroach / Grasshopper)", "Malpighian tubules opening into the junction of midgut and hindgut", "Flame cells", "Kidneys", "Nephridia"),
            ("Crustaceans (Crayfish / Prawn)", "Antennal glands (green glands) situated at the base of antennae", "Malpighian tubules", "Flame cells", "Lungs"),
            ("Vertebrates (Mammals, Birds, Reptiles)", "Kidneys composed of millions of functional nephron filtration units", "Flame cells", "Green glands", "Malpighian tubules")
        ]
        for animal_grp, ex_struct, d1, d2, d3 in excretory_organs:
            q_text = f"Which specialized excretory and osmoregulatory organ is characteristic of {animal_grp}?"
            opts = {"A": ex_struct, "B": d1, "C": d2, "D": d3}
            items.append((
                "Comparative Excretory Systems", q_text, opts, "A",
                f"{animal_grp} excrete metabolic waste using {ex_struct.lower()}.",
                f"Identify the diagnostic excretory organ of {animal_grp.split('(')[0].strip()}."
            ))

        # Respiratory volumes
        resp_vols = [
            ("Tidal Volume (TV, ~500 mL)", "Volume of air inhaled or exhaled with each normal, resting breath", "Maximal air exhaled after maximal inhalation", "Air remaining in lungs after forced exhalation", "Air forced in after normal inhalation"),
            ("Residual Volume (RV, ~1200 mL)", "Volume of air remaining in the lungs even after a maximal forced expiration, preventing alveolar collapse", "Normal breath volume", "Maximal breath volume", "Air entering trachea only"),
            ("Vital Capacity (VC, ~4600 mL)", "Maximum volume of air that can be forcibly exhaled following a maximal deep inspiration (TV + IRV + ERV)", "Total lung capacity including residual air", "Air breathed per minute", "Tidal volume only")
        ]
        for v_name, v_def, d1, d2, d3 in resp_vols:
            q_text = f"In pulmonary spirometry, what does the parameter {v_name} represent?"
            opts = {"A": v_def, "B": d1, "C": d2, "D": d3}
            items.append((
                "Pulmonary Lung Volumes", q_text, opts, "A",
                f"{v_name}: {v_def}.",
                "Understand clinical lung volume parameters."
            ))

    elif topic == "Genetics & Evolution":
        # Hardy-Weinberg calculations
        # q^2 in [0.04, 0.09, 0.16, 0.25, 0.36] => q in [0.2, 0.3, 0.4, 0.5, 0.6]
        hw_data = [
            (0.04, 0.2, 0.8, 0.32, "4%", "20%", "80%", "32%"),
            (0.09, 0.3, 0.7, 0.42, "9%", "30%", "70%", "42%"),
            (0.16, 0.4, 0.6, 0.48, "16%", "40%", "60%", "48%"),
            (0.25, 0.5, 0.5, 0.50, "25%", "50%", "50%", "50%"),
            (0.36, 0.6, 0.4, 0.48, "36%", "60%", "40%", "48%")
        ]
        for q2, q, p, two_pq, q2_str, q_str, p_str, two_pq_str in hw_data:
            q_text = f"In a human population in Hardy-Weinberg equilibrium, an autosomal recessive condition affects {q2_str} of the individuals. What is the frequency of the heterozygous carrier genotype (2pq)?"
            opts = {"A": two_pq_str, "B": q2_str, "C": p_str, "D": q_str}
            items.append((
                "Hardy-Weinberg Equilibrium", q_text, opts, "A",
                f"q² = {q2} => q = √{q2} = {q}. Since p + q = 1, p = {p:.1f}. Heterozygous frequency 2pq = 2({p:.1f})({q:.1f}) = {two_pq:.2f} ({two_pq_str}).",
                "Take square root of recessive frequency to find q, then compute p = 1 - q and 2pq."
            ))
            q_text_dom = f"In a population where {q2_str} express a recessive trait, what is the frequency of the dominant allele (p)?"
            opts_dom = {"A": f"{p:.1f}", "B": f"{q:.1f}", "C": f"{two_pq:.2f}", "D": f"{p**2:.2f}"}
            items.append((
                "Hardy-Weinberg Allele Frequencies", q_text_dom, opts_dom, "A",
                f"q = √{q2} = {q}. Therefore dominant allele frequency p = 1 - q = 1 - {q} = {p:.1f}.",
                "Find q first, then use p = 1 - q."
            ))

        # Monohybrid offspring numbers
        for n_off in [40, 80, 100, 200, 400]:
            rec = n_off // 4
            dom = n_off - rec
            q_text = f"In a cross between two heterozygous tall pea plants (Tt × Tt), a total of {n_off} offspring are produced. Statistically, how many of these plants are expected to be dwarf (tt)?"
            opts = {"A": f"{rec}", "B": f"{dom}", "C": f"{n_off // 2}", "D": f"{rec // 2}"}
            items.append((
                "Mendelian Monohybrid Proportions", q_text, opts, "A",
                f"Phenotypic ratio is 3 tall : 1 dwarf. Probability of dwarf is 1/4 (25%). 1/4 × {n_off} = {rec} dwarf plants.",
                "Multiply the total offspring count by the expected Mendelian probability of 1/4."
            ))

    elif topic == "Ecology & Environment":
        # Energy trophic calculations
        for solar in [100000, 500000, 1000000]:
            prod = solar // 100 # 1% of solar captured by plants
            herb = prod // 10   # 10% rule
            carn = herb // 10
            q_text = f"If green photosynthetic plants in a grassland ecosystem absorb {solar:,} J of radiant solar energy, approximately how much energy is transferred to primary consumers (herbivores)? (Assume 1% capture efficiency and 10% trophic transfer)"
            opts = {"A": f"{herb:,} J", "B": f"{prod:,} J", "C": f"{carn:,} J", "D": f"{solar // 10:,} J"}
            items.append((
                "Trophic Level Energy Transfer (Lindeman's 10% Rule)", q_text, opts, "A",
                f"Producers capture 1%: {solar:,} × 0.01 = {prod:,} J. Herbivores receive 10%: {prod:,} × 0.10 = {herb:,} J.",
                "Apply the 10% ecological energy transfer rule at each trophic feeding step."
            ))

        # Animal adaptations
        adaptations = [
            ("Camel adaptations to desert (xerocole)", "Hump storing triglyceride fat which yields metabolic water upon oxidation, concentrated urine, and oval red blood cells that withstand dehydration", "Gills and scales", "Large leaf area for cooling", "Webbed feet for swimming"),
            ("Kangaroo rat (Dipodomys) desert survival", "Never drinks water; derives 100% of body water requirements from metabolic water produced during cellular respiration of dry seeds", "Drinks sea water", "Stores water in bladder for months", "Sweats continuously"),
            ("Birds adaptations for aerial flight", "Pneumatic hollow bones, absence of urinary bladder, keeled sternum for pectoral flight muscles, and air sacs for unidirectional lung ventilation", "Dense heavy solid bones", "Well-developed teeth", "Large urinary bladder"),
            ("Pelagic fish adaptations for rapid swimming", "Streamlined spindle-shaped body, swim bladder for hydrostatic buoyancy, lateral line sense organ, and mucous-coated scales", "Heavy bone armor", "Absence of fins", "Tracheae for air breathing")
        ]
        for animal, ans, d1, d2, d3 in adaptations:
            q_text = f"Which anatomical and physiological adaptations enable the {animal}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Animal Adaptations & Morphology", q_text, opts, "A",
                f"{animal}: {ans}.",
                "Connect behavioral and physiological features to survival in extreme biomes."
            ))

def append_master_biology(items, topic):
    if topic == "Cellular Biology & Life Processes":
        # Cell comparison & taxonomy
        cell_comps = [
            ("Prokaryotic cells (e.g. bacteria) vs Eukaryotic cells", "Prokaryotes have 70S ribosomes, lack a true membrane-bound nucleus, and have naked circular DNA without histones", "Prokaryotes possess mitochondria", "Prokaryotes have 80S ribosomes", "Eukaryotes lack a nucleus"),
            ("Plant cell vs Animal cell ultrastructure", "Plant cells possess a rigid cellulose cell wall, large central sap vacuole, and plastids/chloroplasts", "Plant cells possess centrioles during mitosis", "Animal cells contain chloroplasts", "Animal cells have cellulose walls"),
            ("Fungal cell structural composition", "Cell walls composed of chitin and storage of excess carbohydrate as glycogen (not starch)", "Cellulose cell walls and starch storage", "Autotrophic photosynthesis", "Lack of cell membrane"),
            ("Viral biological characteristics", "Acellular infectious entities containing either DNA or RNA enclosed in a protein capsid, replicating only inside living host cells", "Independent binary fission", "Possess functional ribosomes and mitochondria", "Classified as prokaryotes"),
            ("Biomolecules: Disaccharides breakdown", "Maltose = Glucose + Glucose; Sucrose = Glucose + Fructose; Lactose = Glucose + Galactose", "Sucrose = Glucose + Glucose", "Maltose = Fructose + Galactose", "Lactose = Fructose + Fructose"),
            ("Polysaccharide functions", "Starch and glycogen are insoluble energy storage polymers in plants and animals; cellulose and chitin are structural", "Starch is structural in animals", "Cellulose is soluble fuel", "Glycogen is found in plant seeds")
        ]
        for title, ans, d1, d2, d3 in cell_comps:
            q_text = f"Which statement correctly describes the {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Cell Classification & Comparative Cytology", q_text, opts, "A",
                f"{title}: {ans}.",
                "Examine organelle presence, ribosomal S-value, and biochemical storage molecules."
            ))

    elif topic == "Human Physiology & Systems":
        # Autonomic nervous system
        autonomic_actions = [
            ("Sympathetic nervous system stimulation (Adrenergic)", "Dilates pupils, increases heart rate, dilates bronchioles, and inhibits gastrointestinal peristalsis", "Constricts pupils and slows heart rate", "Stimulates digestion and saliva", "Contracts bladder wall"),
            ("Parasympathetic nervous system stimulation (Cholinergic)", "Constricts pupils, decreases heart rate, constricts bronchioles, and stimulates digestive peristalsis/saliva", "Accelerates heart rate for emergency", "Dilates pupils for night vision", "Inhibits digestive enzymes"),
            ("Synaptic transmission mechanism", "Action potential triggers Ca²⁺ influx at axon terminal, stimulating exocytosis of acetylcholine into the synaptic cleft", "Direct electrical jump across gap", "Flow of red blood cells across cleft", "Mechanical contraction of myelin"),
            ("Arteries vs Veins architectural differences", "Arteries have thicker tunica media with abundant elastic fibers to resist high systolic pressure, and lack valves; veins have wide lumens and pocket valves", "Veins have higher hydrostatic pressure", "Arteries carry pocket valves throughout", "Veins have thicker muscular walls"),
            ("Myocardial infarction (Heart attack)", "Occlusion of coronary arteries by atherosclerosis or thrombus, depriving cardiac muscle tissue of oxygen and causing ischemia", "Inflammation of pericardial sac", "Failure of bicuspid valve", "Rupture of pulmonary vein"),
            ("Renal failure and hemodialysis", "Artificial kidney dialysis machine removes accumulated urea, excess salts, and toxic wastes across a semipermeable membrane down concentration gradients", "Pumps blood directly to lungs", "Replaces red blood cells", "Injects ADH hormone")
        ]
        for title, ans, d1, d2, d3 in autonomic_actions:
            q_text = f"What is the physiological mechanism or clinical feature of {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Neuro-Cardiovascular Physiology & Clinical Pathology", q_text, opts, "A",
                f"{title}: {ans}.",
                "Distinguish sympathetic vs parasympathetic outflow and cardiovascular biomechanics."
            ))

    elif topic == "Genetics & Evolution":
        # Genetic code & Variation
        gen_codes = [
            ("Degeneracy (redundancy) of the genetic code", "Multiple distinct mRNA nucleotide triplet codons can specify the identical amino acid (e.g. 6 codons for leucine)", "Each codon codes for multiple amino acids", "The code varies between species", "Codons overlap during translation"),
            ("Continuous variation in human populations (e.g. height, skin color, body mass)", "Controlled by multiple additive polygenes (polygenic inheritance) interacting with environmental factors, yielding a bell-shaped normal distribution", "Controlled by a single Mendelian gene pair", "Shows distinct non-overlapping categories", "Is unaffected by environmental nutrition"),
            ("Discontinuous variation in humans (e.g. ABO blood group, tongue rolling, albinism)", "Controlled by one or few major genes with negligible environmental influence, displaying discrete non-overlapping phenotypic classes", "Follows a continuous normal distribution curve", "Influenced predominantly by diet", "Controlled by polygenes on all autosomes"),
            ("Allopatric speciation mechanism", "Physical geographic barrier (river, mountain range, desert) splits a population, preventing gene flow and allowing divergent natural selection to create reproductive isolation", "Speciation without physical separation", "Instant mutation in one generation", "Artificial selective breeding by humans"),
            ("Pre-zygotic reproductive isolating mechanisms", "Ecological, temporal, behavioral (mating calls), or mechanical incompatibilities that prevent successful copulation or fertilization", "Hybrid inviability in embryonic stage", "Hybrid sterility like the sterile mule", "Chromosomal breakdown in F2 generation")
        ]
        for title, ans, d1, d2, d3 in gen_codes:
            q_text = f"Which biological concept is exemplified by {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Molecular Genetics & Speciation Mechanisms", q_text, opts, "A",
                f"{title}: {ans}.",
                "Analyze the distinction between continuous/discontinuous traits and speciation barriers."
            ))

        # Hemophilia cross calculations
        hemo_cases = [
            ("Carrier mother (X^H X^h) and normal father (X^H Y)", "Son inheriting hemophilia", "50% of sons (1 in 2)", "100% of sons", "0%", "25% of sons"),
            ("Carrier mother (X^H X^h) and normal father (X^H Y)", "Daughter suffering from hemophilia", "0% (all daughters are either homozygous normal or carriers)", "50%", "25%", "100%"),
            ("Hemophiliac mother (X^h X^h) and normal father (X^H Y)", "Son suffering from hemophilia", "100% of sons (all sons receive mutant X from mother)", "50%", "0%", "25%"),
            ("Normal homozygous mother (X^H X^H) and hemophiliac father (X^h Y)", "Daughter being an asymptomatic genetic carrier", "100% of daughters (all daughters receive X^h from father)", "50%", "0%", "25%")
        ]
        for par, focus, ans, d1, d2, d3 in hemo_cases:
            q_text = f"In human sex-linked hemophilia inheritance involving a {par}, what is the mathematical probability of a {focus}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Sex-Linked Hemophilia Probabilities", q_text, opts, "A",
                f"Cross analysis: {ans}.",
                "Sons receive their single X chromosome exclusively from their mother."
            ))

    elif topic == "Ecology & Environment":
        # Environmental issues in Nigeria
        eco_nig = [
            ("Oil spillage in the Niger Delta aquatic ecosystem", "Forms an impermeable surface film blocking atmospheric oxygen diffusion and sunlight penetration, destroying mangroves and artisanal fish spawning grounds", "Increases soil alkalinity", "Causes rapid eutrophication of lakes", "Leads to severe desertification"),
            ("Desertification in Northern Nigerian frontline states (Sokoto, Katsina, Yobe, Borno)", "Southward expansion of Sahara desert driven by prolonged droughts, overgrazing, and massive deforestation for domestic fuelwood; countered by the Great Green Wall", "Flooding from Atlantic Ocean", "Heavy acid rain leaching soil", "Thermal heating from industries"),
            ("Severe gully erosion in Southeastern Nigeria (Anambra, Abia, Imo)", "High-intensity tropical rainfall acting on friable, poorly consolidated sandy soils aggravated by improper road drainage and devegetation", "Wind deposition of sand", "Tidal ocean surges", "Gas flaring thermal pollution"),
            ("Coastal ocean surge erosion along Lagos coastal coastline (Victoria Island / Kuramo)", "Atlantic ocean wave energy eroding low-lying unconsolidated sandy beaches, exacerbated by sea level rise and removal of natural coastal buffers", "Gully erosion from rainfall", "Desertification", "Acid mine drainage")
        ]
        for issue, ans, d1, d2, d3 in eco_nig:
            q_text = f"What is the environmental etiology and ecological impact of {issue}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Environmental Ecological Challenges in Nigeria", q_text, opts, "A",
                f"{issue}: {ans}.",
                "Identify the regional environmental problem and its specific ecological consequence."
            ))

        # Population growth curves
        pop_curves = [
            ("Sigmoid (S-shaped / logistic) population growth curve", "Comprises lag phase, exponential (log) acceleration phase, deceleration phase, and steady stationary carrying capacity (K) equilibrium", "Unlimited exponential growth without plateau", "Continuous linear decline to extinction", "Cyclic spikes with no stationary phase"),
            ("Carrying capacity (K) of an ecosystem", "Maximum population size of a species that a specific habitat can sustainably support indefinitely without environmental degradation", "Minimum population needed for breeding", "Total number of species in a community", "Rate of natural increase"),
            ("Density-dependent environmental limiting factors", "Biotic factors whose regulatory intensity increases as population density rises (e.g. infectious epidemics, food competition, predation, territoriality)", "Flash floods and tsunamis", "Volcanic eruptions", "Forest wildfires"),
            ("Density-independent environmental limiting factors", "Abiotic climatic catastrophes that decimate population numbers regardless of population density (e.g. drought, severe frost, hurricanes)", "Contagious diseases", "Competition for nesting sites", "Parasitic worm infections")
        ]
        for p_term, p_def, d1, d2, d3 in pop_curves:
            q_text = f"In population ecology, how is {p_term} defined?"
            opts = {"A": p_def, "B": d1, "C": d2, "D": d3}
            items.append((
                "Population Dynamics & Carrying Capacity", q_text, opts, "A",
                f"{p_term}: {p_def}.",
                "Distinguish between density-dependent biotic regulators and density-independent abiotic disasters."
            ))

def append_ultimate_biology(items, topic):
    if topic == "Cellular Biology & Life Processes":
        # Specialized cell adaptations
        spec_cells = [
            ("Root hair cell of flowering plants", "Slender elongated epidermal extension providing immense surface-area-to-volume ratio and dense sap vacuole to maximize water absorption by osmosis", "Packed with chloroplasts for photosynthesis", "Lignified dead walls for structural support", "Ciliated motile flagellum"),
            ("Mature human erythrocyte (red blood cell)", "Biconcave disc shape increasing surface area for oxygen diffusion, lacking a nucleus and mitochondria to maximize hemoglobin payload", "Contains massive nucleus for reproduction", "Equipped with pseudopodia for phagocytosis", "Heavily flagellated for locomotion"),
            ("Human spermatozoon (sperm cell)", "Head with haploid nucleus and acrosome containing digestive hyaluronidase enzymes, midpiece rich in mitochondria for ATP, and flagellar tail", "Biconcave disc shape", "Surrounded by cellulose wall", "Multi-nucleated syncytium"),
            ("Guard cells of dicot foliar stomata", "Kidney-shaped cells with thick, inelastic inner walls and thin, elastic outer walls; turgor pressure causes them to bow outward, opening the pore", "Dead sclerenchyma fibers", "Lack chloroplasts completely", "Uniformly thin walls that burst when turgid"),
            ("Palisade mesophyll cell of leaf", "Densely packed vertical columnar cells directly beneath upper epidermis containing highest density of chloroplasts for light harvesting", "Dead water-conducting cells", "Spherical cells with large air gaps", "Lack cell walls"),
            ("Spongy mesophyll cell of leaf", "Irregularly shaped loosely arranged cells with extensive intercellular air spaces facilitating gaseous exchange of CO₂ and O₂", "Tightly packed columns with no air spaces", "Devoid of chloroplasts", "Lignified mechanical fibers"),
            ("Myelinated motor neuron", "Large dendritic soma and elongated axon enveloped in insulating lipid myelin sheath punctuated by Nodes of Ranvier for rapid saltatory nerve conduction", "Transports oxygen in blood", "Secretes digestive enzymes", "Undergoes rapid mitosis every hour"),
            ("Ciliated epithelial lining of trachea", "Motile hair-like cilia beating in coordinated rhythmic metachronal waves to sweep mucus and entrapped airborne debris up toward pharynx", "Absorbs digested amino acids", "Stores triglyceride fat", "Forms protective keratin stratum")
        ]
        for cname, cadapt, d1, d2, d3 in spec_cells:
            q_text = f"Which specialized structural adaptation characterizes the {cname}?"
            opts = {"A": cadapt, "B": d1, "C": d2, "D": d3}
            items.append((
                "Specialized Cellular Adaptations", q_text, opts, "A",
                f"{cname}: {cadapt}.",
                "Relate unique cellular morphology directly to specialized physiological function."
            ))
            q_text_rev = f"Which cell type is described as possessing: {cadapt.lower()}?"
            opts_rev = {"A": cname, "B": "Amoeba proteus", "C": "Yeast cell", "D": "Chlamydomonas"}
            items.append((
                "Cell Morphology Identification", q_text_rev, opts_rev, "A",
                f"The cell type possessing these features is the {cname}.",
                "Identify the specialized cell based on its ultrastructural description."
            ))

    elif topic == "Human Physiology & Systems":
        # Brain regions and functions
        brain_parts = [
            ("Cerebrum (Cerebral Cortex)", "Executive functions, conscious thought, intelligence, memory, sensory perception, and voluntary motor control", "Coordination of muscular balance and posture", "Autonomic control of cardiac and breathing rhythm", "Thermoregulation and water balance"),
            ("Cerebellum", "Unconscious coordination of voluntary muscle movements, maintenance of posture, body equilibrium, and fine motor precision", "Conscious thought and reasoning", "Peristalsis control", "Endocrine hormone production"),
            ("Medulla Oblongata", "Autonomic regulatory reflex center controlling heart rate, respiratory rhythm, blood pressure, peristalsis, coughing, and swallowing", "Visual learning and memory", "Voluntary speech articulation", "Balance and posture"),
            ("Hypothalamus", "Primary homeostatic control center regulating core body temperature, water balance (osmoregulation), appetite, and pituitary secretions", "Motor muscle coordination", "Speech interpretation", "Reflex eye blinking"),
            ("Thalamus", "Main relay sensory station routing incoming sensory information (except smell) to appropriate regions of cerebral cortex", "Cardiovascular control", "Production of melatonin", "Hearing balance")
        ]
        for b_part, b_func, d1, d2, d3 in brain_parts:
            q_text = f"Which major neurological function is governed by the {b_part} of the human central nervous system?"
            opts = {"A": b_func, "B": d1, "C": d2, "D": d3}
            items.append((
                "Central Nervous System & Brain Anatomy", q_text, opts, "A",
                f"{b_part}: {b_func}.",
                f"Identify the specialized neurological responsibility of the {b_part.split('(')[0].strip()}."
            ))

        # Dental formulas and herbivore vs carnivore
        dentition = [
            ("Adult human permanent dentition", "2(I 2/2, C 1/1, PM 2/2, M 3/3) = 32 teeth (heterodont dentition: cutting, tearing, grinding)", "2(I 3/3, C 1/1, PM 4/4, M 2/2) = 40", "Homodont peg-like teeth", "Only incisors and molars"),
            ("Herbivore dentition (e.g. Cow / Sheep)", "Absence of upper incisors/canines (replaced by a tough horny pad) and presence of a toothless diastema gap", "Prominent pointed canine tusks", "Sharp scissor-like carnassial teeth", "Homodont conical teeth"),
            ("Carnivore dentition (e.g. Dog / Lion)", "Enlarged pointed canines for piercing prey and specialized carnassial teeth (upper PM4/lower M1) for shearing flesh and bone", "Horny pad on upper jaw", "Diastema gap between incisors and premolars", "Absence of molars"),
            ("Function of the diastema in herbivores", "Toothless space between incisors and premolars allowing the tongue to manipulate, sort, and retain grass cud during chewing", "Cracking heavy bones", "Injecting venom", "Piercing tough hides")
        ]
        for dent_title, dent_fact, d1, d2, d3 in dentition:
            q_text = f"Which anatomical feature defines {dent_title.lower()}?"
            opts = {"A": dent_fact, "B": d1, "C": d2, "D": d3}
            items.append((
                "Mammalian Dentition & Dietary Adaptations", q_text, opts, "A",
                f"{dent_title}: {dent_fact}.",
                "Correlate tooth morphology and dental formula with herbivorous or carnivorous diets."
            ))

    elif topic == "Genetics & Evolution":
        # Dihybrid cross probabilities
        dihybrid_q = [
            ("Round Yellow (RrYy × RrYy) dihybrid cross: phenotypic proportion of Round Yellow offspring", "9/16 (56.25%)", "3/16 (18.75%)", "1/16 (6.25%)", "1/4 (25%)"),
            ("Round Yellow (RrYy × RrYy) dihybrid cross: phenotypic proportion of Round Green offspring", "3/16 (18.75%)", "9/16 (56.25%)", "1/16 (6.25%)", "3/4 (75%)"),
            ("Round Yellow (RrYy × RrYy) dihybrid cross: phenotypic proportion of Wrinkled Yellow offspring", "3/16 (18.75%)", "9/16 (56.25%)", "1/16 (6.25%)", "1/2 (50%)"),
            ("Round Yellow (RrYy × RrYy) dihybrid cross: phenotypic proportion of Wrinkled Green (double recessive rryy)", "1/16 (6.25%)", "3/16 (18.75%)", "9/16 (56.25%)", "1/4 (25%)"),
            ("Test cross of a dihybrid individual (AaBb × aabb): expected phenotypic ratio", "1:1:1:1 (equal proportions of all four phenotypic classes)", "9:3:3:1", "3:1", "1:2:1"),
            ("Monohybrid test cross of a heterozygous tall plant (Tt × tt): expected phenotypic ratio", "1 Tall : 1 Dwarf (50% tall, 50% dwarf)", "3 Tall : 1 Dwarf", "All Tall", "1:2:1")
        ]
        for title, ans, d1, d2, d3 in dihybrid_q:
            q_text = f"In classical Mendelian genetics, what is the expected outcome for a {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Mendelian Dihybrid & Test Cross Ratios", q_text, opts, "A",
                f"{title}: {ans}.",
                "Recall standard 9:3:3:1 dihybrid and 1:1 test cross phenotypic frequencies."
            ))

    elif topic == "Ecology & Environment":
        # Hydrophyte adaptations
        hydro_adapt = [
            ("Water lily (Nymphaea) aquatic adaptations", "Broad floating leaves with stomata confined exclusively to the upper epidermis and extensive aerenchyma air tissue for buoyancy", "Sunken stomata on lower surface only", "Thick waxy water-impermeable cuticle on upper surface", "Deep taproot system"),
            ("Water hyacinth (Eichhornia crassipes) floating mechanism", "Swollen, bulbous petiole filled with spongy aerenchyma tissue containing copious trapped air", "Heavy lignified woody stems", "Absence of root hairs", "Spiny succulent leaves"),
            ("Submerged aquatic plants (e.g. Ceratophyllum, Elodea)", "Finely divided ribbon-like leaves offering minimal resistance to currents and lacking cuticles/stomata; absorb gases directly across epidermal cells", "Thick waxy cuticles", "High density of stomata", "Thick bark"),
            ("Halophyte mangrove pneumatophores", "Negatively geotropic erect breathing roots rising above tidal water with lenticels for atmospheric oxygen uptake in anoxic saline mud", "Roots that absorb fresh water only", "Leaves that catch insects", "Thorns that deter herbivores")
        ]
        for plant_t, ans, d1, d2, d3 in hydro_adapt:
            q_text = f"Which specialized botanical adaptation enables {plant_t.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Aquatic & Halophytic Plant Adaptations", q_text, opts, "A",
                f"{plant_t}: {ans}.",
                "Analyze structural modifications for buoyancy, aeration in water, and salt tolerance."
            ))

def append_comprehensive_biology(items, topic):
    if topic == "Human Physiology & Systems":
        # Blood clotting cascade
        clotting_q = [
            ("Initial trigger of blood clotting cascade upon vessel injury", "Platelets adhere to collagen fibers and release thromboplastin (thrombokinase)", "Fibrin dissolves immediately", "Red blood cells burst", "White cells secrete heparin"),
            ("Conversion of prothrombin into active thrombin enzyme", "Catalyzed by thromboplastin in the essential presence of ionic calcium (Ca²⁺) and Vitamin K", "Catalyzed by pepsin", "Occurs spontaneously in air", "Requires iron and Vitamin C"),
            ("Final step in blood clot formation", "Active thrombin converts soluble blood plasma fibrinogen into an insoluble network of fibrous fibrin threads that trap erythrocytes", "Fibrin converts into albumin", "Platelets dissolve", "Prothrombin precipitates"),
            ("Anticoagulant substance in normal circulating blood", "Heparin (produced by basophils and liver cells) prevents intravascular clotting in undamaged blood vessels", "Thromboplastin", "Calcium ions", "Fibrinogen")
        ]
        for c_step, c_ans, d1, d2, d3 in clotting_q:
            q_text = f"In human hemostasis, which mechanism describes the {c_step.lower()}?"
            opts = {"A": c_ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Hemostasis & Blood Clotting Cascade", q_text, opts, "A",
                f"{c_step}: {c_ans}.",
                "Follow the sequence: Thromboplastin + Ca²⁺ -> Prothrombin to Thrombin -> Fibrinogen to Fibrin."
            ))

        # Types of immunity
        immunity_types = [
            ("Natural active immunity", "Production of specific antibodies and memory lymphocytes following natural recovery from an infectious illness (e.g. chickenpox)", "Antibodies received across placenta", "Injection of pre-formed antivenom serum", "Vaccine with dead pathogen"),
            ("Artificial active immunity", "Administration of vaccines containing attenuated pathogens, dead microbes, or toxoids to stimulate antibody and memory cell synthesis without disease", "Natural infection and recovery", "Maternal antibodies in colostrum", "Immediate snake antivenom injection"),
            ("Natural passive immunity", "Transfer of maternal IgG antibodies across the placenta and secretory IgA via colostrum breast milk providing immediate, temporary infant protection", "Vaccination with toxoid", "Production of memory B cells", "Infection by wild virus"),
            ("Artificial passive immunity", "Intramuscular injection of pre-formed exogenous antibodies (antiserum, antitoxin, or antivenom) for immediate emergency neutralization without memory", "Inoculation with live attenuated polio vaccine", "Lifelong immunity from measles", "Maternal milk transmission")
        ]
        for im_type, im_desc, d1, d2, d3 in immunity_types:
            q_text = f"Which epidemiological scenario exemplifies {im_type.lower()}?"
            opts = {"A": im_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Immunology & Modes of Immunity", q_text, opts, "A",
                f"{im_type}: {im_desc}.",
                "Distinguish between active (own antibodies + memory) and passive (borrowed antibodies, no memory)."
            ))

        # Liver functions
        liver_actions = [
            ("Deamination of excess amino acids in the liver", "Removal of the amino group (-NH₂) from excess amino acids, converting it into urea via the ornithine cycle for renal excretion", "Synthesis of insulin", "Storage of bile in gall bladder", "Absorption of glucose from stomach"),
            ("Detoxification function of hepatic cells", "Biochemical conversion of toxic substances (alcohol, drugs, metabolic ammonia) into harmless excretable compounds", "Production of pepsin", "Reabsorption of sodium in kidneys", "Gas exchange in alveoli"),
            ("Destruction of senescent erythrocytes in the liver", "Kupffer reticuloendothelial cells phagocytose worn-out RBCs, recycling iron and converting heme into bile pigments (bilirubin and biliverdin)", "Production of new platelets", "Excretion of urea", "Neutralization of chyme"),
            ("Carbohydrate homeostatic buffering by the liver", "Converts excess postprandial glucose into glycogen (glycogenesis under insulin) and hydrolyzes glycogen to glucose (glycogenolysis under glucagon)", "Digests cellulose", "Absorbs starch directly", "Excretes glucose in normal urine")
        ]
        for l_act, l_desc, d1, d2, d3 in liver_actions:
            q_text = f"How does the mammalian liver execute {l_act.lower()}?"
            opts = {"A": l_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Hepatic Physiology & Metabolism", q_text, opts, "A",
                f"{l_act}: {l_desc}.",
                "Understand the central metabolic roles of hepatocytes and Kupffer cells."
            ))

    elif topic == "Genetics & Evolution":
        # Molecular DNA vs RNA
        dna_rna = [
            ("Nitrogenous pyrimidine base present in DNA but absent in RNA", "Thymine (T) [replaced by Uracil (U) in RNA]", "Cytosine", "Adenine", "Guanine"),
            ("Pentose sugar component of ribonucleic acid (RNA)", "Ribose sugar possessing a hydroxyl (-OH) group on the 2' carbon", "Deoxyribose sugar lacking oxygen on 2' carbon", "Glucose", "Fructose"),
            ("Bond linking complementary nitrogenous base pairs across DNA double helix", "Hydrogen bonds (2 between Adenine and Thymine, 3 between Guanine and Cytosine)", "Covalent peptide bonds", "Ionic phosphodiester bonds", "Glycosidic linkages"),
            ("Enzyme responsible for synthesizing complementary mRNA from a DNA template during transcription", "RNA polymerase", "DNA ligase", "DNA helicase", "Peptidyl transferase"),
            ("Molecular function of transfer RNA (tRNA) in cellular translation", "Carries a specific amino acid to the ribosome and pairs its anticodon with the matching mRNA codon", "Transcribes DNA into code", "Forms the structural backbone of chromosome", "Synthesizes ATP")
        ]
        for q_title, ans, d1, d2, d3 in dna_rna:
            q_text = f"Which statement correctly identifies the {q_title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Molecular Nucleic Acids: DNA vs RNA", q_text, opts, "A",
                f"{q_title}: {ans}.",
                "Analyze nucleotide composition, base-pairing rules, and transcriptional enzymes."
            ))

        # Types of mutations
        mutation_types = [
            ("Missense point mutation (e.g. Sickle-cell anemia)", "A single base substitution that alters a codon so that it specifies a different amino acid (GAG coding for glutamate becomes GTG coding for valine)", "Insertion that shifts reading frame", "Deletion of an entire chromosome", "Silent mutation producing same protein"),
            ("Nonsense point mutation", "A single base substitution that prematurely converts an amino acid-specifying codon into a stop termination codon (UAA, UAG, UGA), truncating the protein", "Insertion of 3 bases", "Substitution specifying same amino acid", "Duplication of chromosome"),
            ("Frameshift mutation", "Insertion or deletion of a number of nucleotides that is not a multiple of three, altering the reading frame of all subsequent codons downstream", "Single base substitution with no frame shift", "Inversion of inverted repeats", "Polyploidy"),
            ("Archaeopteryx fossil evolutionary significance", "Missing transitional link exhibiting reptilian features (teeth, clawed digits, long bony tail) and avian features (feathers, furcula/wishbone, wings)", "Ancient mammal with scales", "Primitive amphibian", "Direct ancestor of modern sharks")
        ]
        for m_title, m_desc, d1, d2, d3 in mutation_types:
            q_text = f"Which genetic or evolutionary concept defines {m_title.lower()}?"
            opts = {"A": m_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Mutational Mechanisms & Transitional Fossils", q_text, opts, "A",
                f"{m_title}: {m_desc}.",
                "Distinguish between missense, nonsense, frameshift mutations and transitional evolutionary fossils."
            ))

    elif topic == "Ecology & Environment":
        # Biological water pollution bioindicators
        bioindicators = [
            ("Tubifex sludge worms and bloodworms (Chironomus larvae)", "Presence indicates heavy organic sewage pollution, severe bacterial decomposition, and critically low dissolved oxygen levels", "Pristine unpolluted alpine streams", "High salinity estuaries", "Absence of organic matter"),
            ("Stonefly and Mayfly nymphs (Plecoptera and Ephemeroptera)", "Strict bioindicators of clean, pristine, cold, and highly oxygenated freshwater streams", "Grossly polluted toxic sewage lagoons", "Anoxic swamp mud", "High industrial detergent pollution"),
            ("Measurement of soil organic humus percentage by ignition loss", "Oven-dry soil is heated strongly in a crucible to burn off organic carbon: Loss in mass / Oven-dry mass × 100%", "Measuring soil volume with water", "Shaking soil with universal indicator", "Passing dry air through soil")
        ]
        for ind_name, ind_role, d1, d2, d3 in bioindicators:
            q_text = f"In environmental ecological monitoring, what does the {ind_name.lower()} signify?"
            opts = {"A": ind_role, "B": d1, "C": d2, "D": d3}
            items.append((
                "Bioindicators & Soil Ecological Methodology", q_text, opts, "A",
                f"{ind_name}: {ind_role}.",
                "Relate macroinvertebrate tolerance levels to biochemical oxygen demand and organic pollution."
            ))

        # Global biomes
        world_biomes = [
            ("Tundra biome", "Circumpolar northern biome characterized by treeless landscapes, permafrost (permanently frozen subsoil), dwarf shrubs, and lichen ground cover", "Dense evergreen multi-canopy hardwood trees", "Hot arid sands with succulent cacti", "Vast grasslands with acacia trees"),
            ("Taiga (Boreal Coniferous Forest) biome", "Subarctic biome dominated by evergreen needle-leaved gymnosperms (spruce, fir, pine) adapted to long, harsh, freezing winters", "Deciduous broad-leaved oaks", "Tropical mangrove swamps", "Treeless Arctic permafrost"),
            ("Temperate Deciduous Forest biome", "Characterized by four distinct seasons and broad-leaved hardwood trees (oak, beech, maple) that shed all their leaves before winter dormancy", "Evergreen thorny scrub", "Permafrost tundra", "Arid succulent desert")
        ]
        for b_name, b_desc, d1, d2, d3 in world_biomes:
            q_text = f"Which climatic and vegetational profile describes the global {b_name}?"
            opts = {"A": b_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Global Terrestrial Biomes", q_text, opts, "A",
                f"{b_name}: {b_desc}.",
                "Match global biomes to their seasonal climate and dominant vegetation."
            ))

def append_finish_biology(items, topic):
    if topic == "Human Physiology & Systems":
        # Pituitary hormones
        pit_hormones = [
            ("Growth Hormone (Somatotropin)", "Stimulates cell division, skeletal bone elongation, and protein synthesis; hypersecretion in youth causes gigantism, hyposecretion causes dwarfism", "Regulates calcium in bones", "Controls water reabsorption", "Stimulates milk secretion only"),
            ("Thyroid-Stimulating Hormone (TSH)", "Stimulates the follicular cells of the thyroid gland to synthesize and release thyroxine (T₄ and T₃)", "Lowers blood glucose", "Stimulates adrenal medulla", "Triggers ovulation directly"),
            ("Adrenocorticotropic Hormone (ACTH)", "Stimulates the adrenal cortex to synthesize and secrete glucocorticoid hormones like cortisol", "Stimulates adrenaline from medulla", "Causes milk let-down", "Controls urine concentration"),
            ("Follicle-Stimulating Hormone (FSH)", "Stimulates the maturation of Graafian ovarian follicles in females and spermatogenesis in male seminiferous tubules", "Stimulates uterine contractions", "Causes milk production", "Controls metabolic rate"),
            ("Luteinizing Hormone (LH / ICSH)", "Triggers ovulation, converts ruptured follicle into corpus luteum in females, and stimulates Leydig cells to secrete testosterone in males", "Stimulates bone elongation", "Controls thyroid size", "Dilates bronchioles")
        ]
        for h_name, h_act, d1, d2, d3 in pit_hormones:
            q_text = f"What is the specific target organ and physiological function of {h_name}?"
            opts = {"A": h_act, "B": d1, "C": d2, "D": d3}
            items.append((
                "Anterior Pituitary Endocrinology", q_text, opts, "A",
                f"{h_name}: {h_act}.",
                "Match the pituitary tropic hormone to its target endocrine gland and function."
            ))

        # White blood cell types
        wbc_types = [
            ("Neutrophils (Polymorphonuclear leucocytes)", "Most abundant phagocytic white blood cells that engulf and destroy invasive bacterial pathogens via lysosomes", "Produce histamine in allergies", "Differentiate into platelets", "Carry oxygen to brain"),
            ("Lymphocytes (B cells and T cells)", "Provide adaptive antigen-specific immunity: B cells differentiate into antibody-secreting plasma cells, T cells provide cell-mediated immunity", "Carry out phagocytosis of bacteria", "Synthesize hemoglobin", "Initiate blood clotting"),
            ("Basophils", "Granulocytes that synthesize and secrete histamine and heparin during allergic inflammatory responses", "Phagocytose large parasites", "Produce antibodies", "Destroy red blood cells"),
            ("Monocytes (differentiating into Macrophages)", "Large agranular phagocytes that engulf cellular debris, foreign microorganisms, and act as antigen-presenting cells", "Release hemoglobin", "Form blood clots", "Secrete thyroxine")
        ]
        for w_name, w_act, d1, d2, d3 in wbc_types:
            q_text = f"Which biological role is carried out specifically by the leucocyte {w_name}?"
            opts = {"A": w_act, "B": d1, "C": d2, "D": d3}
            items.append((
                "Leucocyte Immunology & Differentiation", q_text, opts, "A",
                f"{w_name}: {w_act}.",
                "Distinguish between innate phagocytes (neutrophils, macrophages) and adaptive lymphocytes."
            ))

        # Musculoskeletal connections
        skeletal_tissues = [
            ("Ligament connective tissue", "Dense fibrous regular connective tissue connecting bone to bone across synovial joints, stabilizing joint architecture", "Connects skeletal muscle to bone", "Cushions bone ends", "Secretes synovial fluid"),
            ("Tendon connective tissue", "Inelastic collagenous cord attaching skeletal muscle to periosteum of bone to transmit contractile force", "Connects bone to bone", "Produces red blood cells", "Stores calcium phosphate"),
            ("Synovial fluid", "Viscous egg-white-like lubricating fluid secreted by synovial membrane to reduce friction and nourish articular cartilage", "Hardens joint permanently", "Acts as ligament", "Destroys bone cells"),
            ("Hyaline articular cartilage", "Smooth, resilient bluish-white cartilage covering articulating bone epiphyses, absorbing shock and minimizing joint friction", "Dense bone marrow", "Tendon sheath", "Skeletal muscle fiber")
        ]
        for st_name, st_act, d1, d2, d3 in skeletal_tissues:
            q_text = f"What is the anatomical function of the {st_name}?"
            opts = {"A": st_act, "B": d1, "C": d2, "D": d3}
            items.append((
                "Musculoskeletal Connective Tissues", q_text, opts, "A",
                f"{st_name}: {st_act}.",
                "Remember: Ligaments tie bone to bone; Tendons tie muscle to bone."
            ))

    elif topic == "Genetics & Evolution":
        # DNA replication enzymes
        rep_enzymes = [
            ("DNA Helicase", "Unwinds and separates the two complementary parental DNA strands by breaking hydrogen bonds at the replication fork", "Synthesizes RNA primers", "Joins Okazaki fragments", "Proofreads synthesized DNA"),
            ("DNA Polymerase III", "Synthesizes the complementary leading and lagging DNA strands by adding deoxynucleotides in the 5' to 3' direction and proofreading", "Unwinds the double helix", "Forms peptide bonds", "Transcribes mRNA"),
            ("DNA Ligase", "Catalyzes the formation of covalent phosphodiester bonds to join Okazaki fragments on the lagging strand into a continuous DNA chain", "Breaks hydrogen bonds", "Synthesizes RNA primers", "Degrades cellular RNA"),
            ("DNA Topoisomerase (Gyrase)", "Relieves torsional supercoiling stress ahead of the replicating fork by transiently cutting and swiveling DNA strands", "Adds nucleotides to 3' end", "Separates chromatids", "Forms ribosomal subunits")
        ]
        for e_name, e_act, d1, d2, d3 in rep_enzymes:
            q_text = f"During semiconservative DNA replication, what is the role of {e_name}?"
            opts = {"A": e_act, "B": d1, "C": d2, "D": d3}
            items.append((
                "Enzymology of DNA Replication", q_text, opts, "A",
                f"{e_name}: {e_act}.",
                "Identify the specific biochemical step catalyzed by this replication enzyme."
            ))

        # Mendel's laws
        mendel_laws = [
            ("Mendel's First Law (Law of Segregation)", "The two alleles of a gene separate during meiosis during gamete formation so that each gamete carries only one allele for each gene locus", "Alleles of different genes assort together", "Recessive alleles are destroyed in F1", "Dominant traits are always more frequent"),
            ("Mendel's Second Law (Law of Independent Assortment)", "Alleles of two or more different unlinked genes assort independently of one another during metaphase I gamete formation", "Alleles on same chromosome never cross over", "Genes always blend together", "Recessive traits never appear in F2"),
            ("Chromosomal centromere", "Constricted specialized DNA region of a chromosome where sister chromatids are joined and where kinetochore spindle fibers attach", "Terminal ends of chromosomes", "Genes coding for rRNA", "Band on nuclear membrane"),
            ("Chromosomal telomeres", "Repetitive non-coding nucleotide caps at the ends of eukaryotic chromosomes that protect them from degradation and genomic instability", "Center of the chromosome", "Spindle attachment point", "Region of crossing over")
        ]
        for l_name, l_desc, d1, d2, d3 in mendel_laws:
            q_text = f"Which genetic definition accurately describes {l_name}?"
            opts = {"A": l_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Mendelian Principles & Chromosomal Anatomy", q_text, opts, "A",
                f"{l_name}: {l_desc}.",
                "Distinguish between segregation (single gene) and independent assortment (multiple unlinked genes)."
            ))

    elif topic == "Ecology & Environment":
        # National parks in Nigeria
        parks = [
            ("Yankari National Park (Bauchi State)", "Guinea Savanna wildlife reserve famous for Wikki warm springs, African bush elephants, baboons, and western hartebeest", "Mangrove swamp bird sanctuary", "Tropical rainforest gorilla reserve", "Desert sand dune park"),
            ("Cross River National Park (Cross River State)", "High tropical rainforest biosphere reserve preserving endangered Cross River gorillas, drills, and high biodiversity", "Sahel savanna reserve", "Open desert reserve", "Arid acacia scrub"),
            ("Okomu National Park (Edo State)", "Rainforest reserve dedicated to protecting the endangered endemic white-throated guenon monkey and forest elephants", "Sahel thorn reserve", "Desert reserve", "Montane tundra"),
            ("Kainji Lake National Park (Niger/Kwara States)", "Savanna reserve integrating the Borgu and Zugurma sectors with Kainji hydroelectric reservoir", "Mangrove swamp reserve", "Rainforest gorilla sanctuary", "High alpine tundra")
        ]
        for p_name, p_desc, d1, d2, d3 in parks:
            q_text = f"Which ecological biome and conservation focus defines {p_name}?"
            opts = {"A": p_desc, "B": d1, "C": d2, "D": d3}
            items.append((
                "Conservation & Nigerian National Parks", q_text, opts, "A",
                f"{p_name}: {p_desc}.",
                "Associate Nigerian national parks with their geographic location, biome, and protected species."
            ))

        # Ecological terms
        eco_terms = [
            ("Ecological niche of an organism", "The precise functional role, trophic position, and resource utilization pattern of a species within its biotic community", "The geographical address where it lives", "The total number of individuals", "The geological age of the habitat"),
            ("Ecotone", "A narrow transitional tension zone between two distinct adjoining ecological biomes or communities (e.g. mangrove to rainforest)", "Center of a desert", "Top layer of ocean water", "Deep underground cave"),
            ("Biomass", "Total dry mass of living biological organic matter present per unit area or volume of an ecosystem at a given time", "Weight of soil rocks", "Total rainfall volume", "Number of dead organisms"),
            ("Biosphere", "The global sum of all ecosystems on Earth encompassing the thin layer of air, land, and water supporting living organisms", "Only the earth's atmosphere", "Only marine oceans", "Core of the earth")
        ]
        for et_name, et_def, d1, d2, d3 in eco_terms:
            q_text = f"In environmental ecology, how is an {et_name.lower()} defined?"
            opts = {"A": et_def, "B": d1, "C": d2, "D": d3}
            items.append((
                "Fundamental Ecological Concepts", q_text, opts, "A",
                f"{et_name}: {et_def}.",
                "Understand essential definitions in ecosystem ecology."
            ))

def append_absolute_cap_biology(items, topic):
    if topic == "Genetics & Evolution":
        extra_gen = [
            ("Avian sex determination system (ZW / ZZ)", "Females are the heterogametic sex (ZW) while males are homogametic (ZZ)", "Males are heterogametic XY", "Sex determined by nest temperature", "No sex chromosomes exist"),
            ("Color blindness: Color-blind mother (X^c X^c) and normal vision father (X^C Y)", "100% of sons are color-blind (X^c Y) and 100% of daughters are carriers (X^C X^c)", "All children are normal", "Daughters are color-blind", "50% of sons are normal"),
            ("Albinism cross: Two heterozygous normally pigmented parents (Aa × Aa)", "25% chance (1 in 4) of producing an albino child (aa)", "50% chance", "75% chance", "0% chance"),
            ("Albinism cross: Heterozygous carrier parent (Aa) and albino parent (aa)", "50% chance (1 in 2) of producing an albino child (aa)", "25% chance", "100% chance", "75% chance"),
            ("Universal initiation start codon in eukaryotic mRNA translation", "AUG (specifies the amino acid Methionine)", "UAA", "UGA", "UAG"),
            ("Stop termination codons in mRNA translation", "UAA, UAG, and UGA (do not code for any amino acid; trigger release factor binding)", "AUG, GUG, and CUG", "AAA, UUU, and GGG", "CCA, CCG, and CCU"),
            ("Epistasis in genetics", "A genetic phenomenon where the expression of one gene locus masks or alters the phenotypic expression of a different gene locus", "Alleles blend together", "Only dominant alleles are expressed", "Genes link on same chromosome"),
            ("Pleiotropy in human medical genetics", "A single gene mutation produces multiple seemingly unrelated phenotypic effects (e.g. HbS causing anemia, bone pain, and splenomegaly)", "Multiple genes control one trait", "One gene controls one enzyme", "Recessive trait skips generations"),
            ("Polygenic inheritance of human melanin pigmentation", "At least three separate gene pairs act additively, producing a continuous spectrum of skin tones from very fair to very dark", "Controlled by a single codominant gene", "Controlled by sex-linked alleles", "Discontinuous trait with 2 categories"),
            ("Discontinuous variation of human tongue rolling ability", "Controlled by a single dominant allele: individuals either roll their tongue or cannot, with no intermediate states", "Continuous bell-curve distribution", "Caused by nutrition", "Polygenic trait")
        ]
        for title, ans, d1, d2, d3 in extra_gen:
            q_text = f"Which genetic principle or probability describes {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Advanced Mendelian & Molecular Genetics", q_text, opts, "A",
                f"{title}: {ans}.",
                "Apply Mendelian rules or genetic code specifications."
            ))

    elif topic == "Ecology & Environment":
        extra_eco = [
            ("Tropical rainforest canopy stratification layers", "Five vertical strata: Emergent layer (>40 m), Continuous canopy (20-40 m), Understorey (5-20 m), Shrub layer, and Forest floor", "Only one uniform tree layer", "Two layers: moss and grass", "Three layers of cacti"),
            ("Emergent layer in tropical rainforest", "Scattered towering hardwood trees (Iroko, Obeche, Mahogany) extending 40-60 meters above the general forest canopy to access direct sunlight", "Shrubs at ground level", "Floating aquatic plants", "Epiphytes on rocks"),
            ("Forest floor in dense tropical rainforest", "Deep shade with less than 2% light penetration, rapid decomposition of leaf litter, and absence of grasses", "Blinding sunlight and dry sand", "Permanent frost", "Abundant tall grasses"),
            ("Mycorrhizal fungal-root mutualism", "Fungal hyphae greatly expand root surface area to absorb phosphorus and water for the plant while receiving photosynthesized carbohydrates", "Fungus kills root cells", "Fungus lives on dead bark", "Plant parasitizes fungus"),
            ("Protozoan-termite mutualistic symbiosis", "Cellulase-producing protozoa (Trichonympha) in termite hindgut digest cellulose in chewed wood into absorbable sugars for both organisms", "Protozoa kill the termite", "Termite feeds on protozoa", "No mutual benefit"),
            ("Escherichia coli in human large intestine (colon)", "Bacterial synthesis of essential Vitamin K and certain B vitamins for the human host while utilizing dietary residue", "Bacterium causes severe malaria", "Bacterium digests proteins in stomach", "Destroys gut lining"),
            ("Inverted pyramid of numbers in woodland ecosystems", "A single massive producer (e.g. giant mango or oak tree) supporting tens of thousands of herbivorous insects and hyperparasites", "Energy increases up the pyramid", "More lions than antelopes", "Aquatic phytoplankton inverted"),
            ("Inverted pyramid of biomass in marine pelagic ecosystems", "Standing crop biomass of phytoplankton at any single instant is smaller than that of zooplankton due to rapid turnover and high productivity of algae", "Energy is created by consumers", "Fish weigh less than bacteria", "Trees weigh less than caterpillars"),
            ("Ecological role of saprophytic decomposers (bacteria and fungi)", "Break down complex organic matter of dead organisms and feces, releasing inorganic nutrients (carbon, nitrogen, phosphorus) back into soil and air", "Direct primary production via sunlight", "Predation on live herbivores", "Consume living plants"),
            ("Eutrophication stages in a freshwater lake", "Fertilizer runoff -> algal bloom -> light blocked -> submersed plants die -> bacterial decomposition consumes oxygen -> fish asphyxiate", "Lake dries up instantly", "Oxygen increases to toxic levels", "Algae freeze the water"),
            ("Water cycle: Transpiration from terrestrial vegetation", "Evaporation of water vapor from aerial plant parts (mainly foliar stomata) contributing up to 10% of total atmospheric water vapor", "Absorption of rain by roots", "Condensation on soil", "Deep underground percolation"),
            ("Soil capillarity across soil types", "Highest in clay soil (finest micropores pull water highest against gravity) and lowest in coarse sandy soil", "Highest in sand", "Equal in all soils", "Zero in clay"),
            ("Soil percolation rate comparison", "Coarse sandy soils exhibit the highest percolation rates (rapid water drainage) while dense clay exhibits slowest percolation", "Clay has highest percolation", "Loam cannot drain water", "Sand holds water longest"),
            ("Biological control of crop pests (e.g. Ladybird beetles controlling aphids)", "Utilizing natural predatory or parasitic organisms to regulate pest population density below economic injury level without chemical pesticides", "Spraying toxic DDT", "Flooding fields with saltwater", "Burning the entire crop"),
            ("Conservation of natural resources: Wildlife game reserves", "Preserving biodiversity, preventing extinction of endangered species, maintaining gene pools, and supporting eco-tourism", "Commercial logging of old trees", "Converting forest to cattle ranches", "Urban industrial zoning")
        ]
        for title, ans, d1, d2, d3 in extra_eco:
            q_text = f"What is the ecological principle, adaptation, or mechanism of {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ecosystem Dynamics & Natural Resources", q_text, opts, "A",
                f"{title}: {ans}.",
                "Analyze trophic ecology, soil physics, or conservation management."
            ))

def append_ecology_final_push(items, topic):
    if topic == "Ecology & Environment":
        eco_push = [
            ("Nitrogen-fixing free-living aerobic bacterium in agricultural soil", "Azotobacter chroococcum", "Pseudomonas denitrificans", "Nitrobacter", "Nitrosomonas"),
            ("Nitrogen-fixing free-living anaerobic bacterium in waterlogged soil", "Clostridium pasteurianum", "Rhizobium", "Escherichia coli", "Streptococcus"),
            ("Symbiotic nitrogen fixation in non-leguminous plants (e.g. Alder tree)", "Frankia actinomycete living in actinorhizal root nodules", "Nitrosomonas", "Yeast", "Lactobacillus"),
            ("Commensalism between barnacles and baleen whales", "Barnacles obtain transport and access to plankton-rich feeding currents without affecting whale health", "Barnacles feed on whale blubber", "Whale feeds on barnacles", "Mutual killing"),
            ("Parasitic angiosperm: Witchweed (Striga hermonthica)", "Obligate root parasitic weed severely stunting cereal crops (maize, sorghum, millet) in Nigerian savannas", "Beneficial legume", "Floating hydrophyte", "Desert succulent cactus"),
            ("Parasitic angiosperm: Mistletoe (Loranthus)", "Hemiparasite penetrating host tree xylem branches via haustoria to extract water and mineral nutrients", "Complete saprophyte", "Nitrogen fixer", "Insectivorous plant"),
            ("Insectivorous plant: Sundew (Drosera) or Pitcher plant (Nepenthes)", "Traps and digests insects enzymatically to obtain nitrogen compounds in nitrogen-deficient bogs", "Cannot photosynthesize", "Feeds on soil clay", "Parasitizes tree trunks"),
            ("Biological significance of the Ozone Layer (O₃) in the stratosphere", "Absorbs destructive solar ultraviolet UV-B and UV-C radiation, preventing skin carcinomas and cataractogenesis", "Traps heat to warm earth", "Provides oxygen for flight", "Destroys carbon dioxide"),
            ("Biomagnification / Bioaccumulation of persistent pesticides (e.g. DDT)", "Progressive increase in chemical pesticide concentration in fatty tissues of organisms at higher trophic levels", "Dilution of pesticide up the food chain", "Destruction of pesticide by sun", "Rapid excretion in urine"),
            ("Primary cause of deforestation in Sub-Saharan Africa", "Uncontrolled clearing for subsistence shifting agriculture and harvesting of fuelwood and charcoal", "Urban industrial skyscrapers", "Volcanic lava flows", "Acid rain destruction")
        ]
        for title, ans, d1, d2, d3 in eco_push:
            q_text = f"Which statement scientifically explains {title.lower()}?"
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Ecological Biotic Interactions & Biosphere Conservation", q_text, opts, "A",
                f"{title}: {ans}.",
                "Examine ecological interactions, parasitism, or environmental bioaccumulation."
            ))
