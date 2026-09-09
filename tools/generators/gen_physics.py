import random
import math

def generate_physics_questions(topic, count_needed):
    items = []

    if topic == "Mechanics":
        for u in [0, 10, 15, 20]:
            for a in [2, 3, 4, 5]:
                for t in [3, 4, 5, 6]:
                    v = u + a * t
                    s = u * t + 0.5 * a * (t ** 2)
                    q_text = f"A vehicle starts with initial speed {u} m/s and accelerates uniformly at {a} m/s² for {t} s. Calculate the total distance covered."
                    opts = {"A": f"{s:.1f} m", "B": f"{u*t:.1f} m", "C": f"{(s + 10):.1f} m", "D": f"{(s / 2):.1f} m"}
                    items.append((
                        "Kinematics Equations", q_text, opts, "A",
                        f"s = ut + 1/2 at² = ({u} × {t}) + (0.5 × {a} × {t}²) = {s:.1f} m.",
                        "Which kinematic equation links displacement, initial velocity, acceleration, and time?"
                    ))
        for m in [2, 5, 8, 10, 20]:
            for h in [5, 10, 15, 25]:
                pe = m * 10 * h
                q_text = f"Calculate the gravitational potential energy of an object of mass {m} kg raised to a vertical height of {h} m above the ground. (g = 10 m/s²)"
                opts = {"A": f"{pe} J", "B": f"{pe // 2} J", "C": f"{pe * 2} J", "D": f"{m * h} J"}
                items.append((
                    "Potential Energy", q_text, opts, "A",
                    f"PE = mgh = {m} × 10 × {h} = {pe} J.",
                    "What formula gives potential energy in a uniform gravitational field?"
                ))
        for l in [0.25, 0.49, 0.64, 1.0, 1.44]:
            t_period = 2 * math.pi * math.sqrt(l / 10)
            q_text = f"A simple pendulum has length {l} m. Find its period of oscillation. (g = 10 m/s², π ≈ 3.14)"
            opts = {"A": f"{t_period:.2f} s", "B": f"{t_period * 2:.2f} s", "C": f"{t_period / 2:.2f} s", "D": f"{l * 2:.2f} s"}
            items.append((
                "Simple Harmonic Motion", q_text, opts, "A",
                f"T = 2π√(l/g) = 2(3.14)√({l}/10) = {t_period:.2f} s.",
                "How does period relate to the square root of pendulum length?"
            ))

    elif topic == "Thermal Physics & Waves":
        for p1 in [1, 2, 3, 4]:
            for v1 in [100, 250, 400, 500]:
                for p2 in [2, 5, 6, 8]:
                    v2 = (p1 * v1) / p2
                    q_text = f"A trapped gas has volume {v1} cm³ at pressure {p1} atm. If pressure is changed to {p2} atm at constant temperature, find new volume."
                    opts = {"A": f"{v2:.1f} cm³", "B": f"{v2 * 2:.1f} cm³", "C": f"{v1 * p2 / p1:.1f} cm³", "D": f"{v1:.1f} cm³"}
                    items.append((
                        "Boyle's Law", q_text, opts, "A",
                        f"P₁V₁ = P₂V₂ => V₂ = (P₁V₁) / P₂ = ({p1} × {v1}) / {p2} = {v2:.1f} cm³.",
                        "Does Boyle's Law apply to isothermal processes?"
                    ))
        for t1_c in [27, 47, 77]:
            for t2_c in [127, 227, 327]:
                t1_k = t1_c + 273
                t2_k = t2_c + 273
                v1 = 300
                v2 = (v1 * t2_k) / t1_k
                q_text = f"A gas occupies 300 cm³ at {t1_c}°C. What volume will it occupy at {t2_c}°C at constant pressure?"
                opts = {"A": f"{v2:.1f} cm³", "B": f"{(v1 * t2_c / t1_c):.1f} cm³", "C": "300 cm³", "D": f"{v2 / 2:.1f} cm³"}
                items.append((
                    "Charles's Law", q_text, opts, "A",
                    f"Must convert to Kelvin! T₁ = {t1_k} K, T₂ = {t2_k} K. V₂ = (V₁ × T₂) / T₁ = (300 × {t2_k}) / {t1_k} = {v2:.1f} cm³.",
                    "Did you convert Celsius temperatures to Kelvin by adding 273?"
                ))
        for m in [0.5, 1.0, 2.0]:
            lf = 3.36e5
            heat = m * lf
            q_text = f"How much heat is absorbed to completely melt {m} kg of ice at 0°C into water at 0°C? (L_f = 3.36 × 10⁵ J/kg)"
            opts = {"A": f"{heat:.2e} J", "B": f"{(heat / 2):.2e} J", "C": f"{(heat * 2):.2e} J", "D": "0 J"}
            items.append((
                "Latent Heat of Fusion", q_text, opts, "A",
                f"Q = mL_f = {m} × 3.36 × 10⁵ = {heat:.2e} J.",
                "Does temperature change during a phase transition?"
            ))
        for f in [150, 250, 300, 500, 680]:
            v = 340
            lam = v / f
            q_text = f"A sound wave of frequency {f} Hz travels through air at 340 m/s. What is its wavelength?"
            opts = {"A": f"{lam:.2f} m", "B": f"{lam * 2:.2f} m", "C": f"{f * v} m", "D": f"{lam / 2:.2f} m"}
            items.append((
                "Wave Speed Equation", q_text, opts, "A",
                f"v = fλ => λ = v / f = 340 / {f} = {lam:.2f} m.",
                "What is the relationship between speed, frequency, and wavelength?"
            ))

    elif topic == "Electricity & Magnetism":
        for r1 in [2, 4, 6, 8, 10]:
            for r2 in [2, 4, 6, 8, 12]:
                r_ser = r1 + r2
                r_par = (r1 * r2) / (r1 + r2)
                q_text = f"Calculate the total equivalent resistance when resistors of {r1} Ω and {r2} Ω are connected in parallel."
                opts = {"A": f"{r_par:.2f} Ω", "B": f"{r_ser} Ω", "C": f"{r1 * r2} Ω", "D": f"{(r_par / 2):.2f} Ω"}
                items.append((
                    "Parallel Resistors", q_text, opts, "A",
                    f"1/R_eq = 1/{r1} + 1/{r2} => R_eq = ({r1} × {r2}) / ({r1} + {r2}) = {r_par:.2f} Ω.",
                    "Why is the equivalent parallel resistance always smaller than the smallest single resistor?"
                ))
        for v in [6, 12, 24, 48]:
            for r in [2, 4, 6, 12]:
                p = (v ** 2) / r
                q_text = f"An electric heating element of resistance {r} Ω is operated across a {v} V power supply. Calculate electrical power dissipated."
                opts = {"A": f"{p:.1f} W", "B": f"{p / 2:.1f} W", "C": f"{v * r} W", "D": f"{p * 2:.1f} W"}
                items.append((
                    "Electric Power", q_text, opts, "A",
                    f"Power P = V² / R = ({v})² / {r} = {v**2} / {r} = {p:.1f} W.",
                    "Which electric power formula relates voltage and resistance directly?"
                ))
        for c1 in [2, 4, 6, 10]:
            for c2 in [2, 4, 6, 10]:
                c_par = c1 + c2
                q_text = f"Two capacitors of capacitances {c1} μF and {c2} μF are connected in parallel. What is their total combined capacitance?"
                opts = {"A": f"{c_par} μF", "B": f"{(c1*c2)/(c1+c2):.2f} μF", "C": f"{c1 * c2} μF", "D": f"{c_par // 2} μF"}
                items.append((
                    "Parallel Capacitors", q_text, opts, "A",
                    f"Capacitors in parallel add directly: C_total = C₁ + C₂ = {c1} + {c2} = {c_par} μF.",
                    "How do capacitances combine when connected in parallel?"
                ))
        for vp in [220, 240]:
            for vs in [12, 24, 110]:
                ratio = vp / vs
                q_text = f"A step-down transformer converts mains {vp} V into {vs} V. What is the turns ratio (N_p / N_s) of primary to secondary turns?"
                opts = {"A": f"{ratio:.2f}", "B": f"{1/ratio:.3f}", "C": f"{vp * vs}", "D": f"{ratio * 2:.2f}"}
                items.append((
                    "Transformer Turns Ratio", q_text, opts, "A",
                    f"N_p / N_s = V_p / V_s = {vp} / {vs} = {ratio:.2f}.",
                    "Does turns ratio equal the ratio of primary to secondary voltage?"
                ))

    elif topic == "Modern & Atomic Physics":
        for th in [2, 3, 5, 8, 10]:
            for n in [2, 3, 4]:
                tt = th * n
                frac = 1 / (2 ** n)
                q_text = f"A radioactive substance has a half-life of {th} hours. What fraction of the sample remains undecayed after {tt} hours?"
                opts = {"A": f"1/{2**n}", "B": f"1/{2**(n-1)}", "C": f"1/{2**(n+1)}", "D": f"{n}/{th}"}
                items.append((
                    "Half-Life Calculations", q_text, opts, "A",
                    f"Number of half-lives n = {tt} / {th} = {n}. Fraction remaining = (1/2)^{n} = 1/{2**n}.",
                    "How many half-life cycles have elapsed over the total time?"
                ))
        for z in [88, 90, 92]:
            a = z * 2 + 50
            new_z = z - 2
            new_a = a - 4
            q_text = f"A radioactive nucleus with atomic number Z = {z} and mass number A = {a} emits one alpha particle. What are Z and A of the daughter nucleus?"
            opts = {"A": f"Z = {new_z}, A = {new_a}", "B": f"Z = {z+1}, A = {a}", "C": f"Z = {new_z}, A = {a}", "D": f"Z = {z-4}, A = {new_a}"}
            items.append((
                "Alpha Decay Nuclear Equations", q_text, opts, "A",
                f"Alpha emission removes 2 protons and 4 nucleons: Z = {z} - 2 = {new_z}; A = {a} - 4 = {new_a}.",
                "How many protons and neutrons does an alpha particle remove?"
            ))
        for f_pow in [14, 15]:
            q_text = f"Calculate the energy of a photon of ultraviolet light of frequency 1.5 × 10^{f_pow} Hz. (Planck's constant h = 6.63 × 10⁻³⁴ J·s)"
            e_val = 6.63 * 1.5 * (10 ** (f_pow - 34))
            opts = {"A": f"{e_val:.2e} J", "B": f"{(e_val * 2):.2e} J", "C": f"{(e_val / 2):.2e} J", "D": "1.50e-19 J"}
            items.append((
                "Planck's Quantum Equation", q_text, opts, "A",
                f"E = hf = (6.63 × 10⁻³⁴) × (1.5 × 10^{f_pow}) = {e_val:.2e} J.",
                "What formula connects photon frequency and energy via Planck's constant?"
            ))

    append_extra_physics(items, topic)
    append_even_more_modern_physics(items, topic)
    return items

def append_extra_physics(items, topic):
    if topic == "Electricity & Magnetism":
        # Coulomb's Law: F = k * q1 * q2 / r^2
        for q1 in [2, 4, 5, 8]:
            for q2 in [3, 5, 10]:
                for r in [1, 2, 3]:
                    # charges in microCoulombs, r in meters, k = 9e9
                    f_val = (9e9 * (q1 * 1e-6) * (q2 * 1e-6)) / (r ** 2)
                    q_text = f"Two point charges of +{q1} μC and +{q2} μC are separated by a distance of {r} m in a vacuum. Calculate the electrostatic repulsive force. (k = 9.0 × 10⁹ N·m²/C²)"
                    opts = {"A": f"{f_val:.3f} N", "B": f"{f_val * 2:.3f} N", "C": f"{f_val / 2:.3f} N", "D": f"{f_val * 10:.3f} N"}
                    items.append((
                        "Coulomb's Law", q_text, opts, "A",
                        f"F = k·q₁·q₂ / r² = (9×10⁹ × {q1}×10⁻⁶ × {q2}×10⁻⁶) / ({r}²) = {f_val:.3f} N.",
                        "Apply Coulomb's inverse-square law for electrostatic charges."
                    ))
        # Magnetic force on current-carrying conductor: F = B * I * L
        for b in [0.2, 0.5, 0.8, 1.2]:
            for i in [2, 4, 5, 10]:
                for l in [0.5, 1.0, 1.5]:
                    f_mag = b * i * l
                    q_text = f"A straight wire of length {l} m carrying a current of {i} A is placed perpendicular to a uniform magnetic field of flux density {b} T. Find the magnetic force on the wire."
                    opts = {"A": f"{f_mag:.2f} N", "B": f"{f_mag * 2:.2f} N", "C": f"{f_mag / 2:.2f} N", "D": f"{b * i:.2f} N"}
                    items.append((
                        "Magnetic Force on Conductor", q_text, opts, "A",
                        f"F = B·I·L·sin(90°) = {b} × {i} × {l} = {f_mag:.2f} N.",
                        "Use Laplace's force formula: F = BIL sin θ."
                    ))
        # Internal resistance: E = I(R + r) => I = E / (R + r)
        for e in [6, 12, 24]:
            for r_ext in [2, 4, 5, 8]:
                for r_int in [1, 2]:
                    current = e / (r_ext + r_int)
                    q_text = f"A cell of EMF {e} V and internal resistance {r_int} Ω is connected across an external load of {r_ext} Ω. What current flows through the circuit?"
                    opts = {"A": f"{current:.2f} A", "B": f"{e / r_ext:.2f} A", "C": f"{e / r_int:.2f} A", "D": f"{current * 2:.2f} A"}
                    items.append((
                        "Internal Resistance & EMF", q_text, opts, "A",
                        f"I = E / (R + r) = {e} / ({r_ext} + {r_int}) = {e}/{r_ext+r_int} = {current:.2f} A.",
                        "Total resistance is external resistance plus internal resistance."
                    ))

    elif topic == "Modern & Atomic Physics":
        # Einstein Photoelectric: E_max = hf - W_0
        for hf_ev in [4.5, 5.0, 6.2, 7.5, 8.0]:
            for w0 in [2.0, 2.3, 3.0, 4.0]:
                if hf_ev > w0:
                    ke = hf_ev - w0
                    q_text = f"Light of photon energy {hf_ev:.1f} eV strikes a metal cathode with a work function of {w0:.1f} eV. What is the maximum kinetic energy of the emitted photoelectrons?"
                    opts = {"A": f"{ke:.1f} eV", "B": f"{hf_ev + w0:.1f} eV", "C": f"{hf_ev * w0:.1f} eV", "D": f"{w0:.1f} eV"}
                    items.append((
                        "Photoelectric Effect", q_text, opts, "A",
                        f"K_max = hf - W₀ = {hf_ev:.1f} - {w0:.1f} = {ke:.1f} eV.",
                        "Maximum kinetic energy equals incident photon energy minus work function."
                    ))
        # Half-life remaining mass
        for m0 in [40, 80, 100, 160, 200]:
            for n_half in [2, 3, 4]:
                rem = m0 / (2 ** n_half)
                th = 4
                tot_time = th * n_half
                q_text = f"A radioisotope has an initial mass of {m0} g and a half-life of {th} days. Calculate the mass remaining after {tot_time} days."
                opts = {"A": f"{rem:.2f} g", "B": f"{rem * 2:.2f} g", "C": f"{m0 / n_half:.2f} g", "D": f"{rem / 2:.2f} g"}
                items.append((
                    "Radioactive Decay Law", q_text, opts, "A",
                    f"Number of half-lives = {tot_time}/{th} = {n_half}. Remaining mass = {m0} / (2^{n_half}) = {rem:.2f} g.",
                    "Each half-life halves the remaining radioactive sample."
                ))
        # Beta decay: Z -> Z + 1, A unchanged
        for z, a, elem in [(6, 14, "Carbon-14"), (19, 40, "Potassium-40"), (53, 131, "Iodine-131"), (38, 90, "Strontium-90")]:
            new_z = z + 1
            q_text = f"When a {elem} nucleus ({z} protons, mass number {a}) undergoes beta-minus (β⁻) decay, what are the proton and nucleon numbers of the resulting nucleus?"
            opts = {"A": f"Protons = {new_z}, Nucleons = {a}", "B": f"Protons = {z - 1}, Nucleons = {a}", "C": f"Protons = {new_z}, Nucleons = {a - 1}", "D": f"Protons = {z}, Nucleons = {a + 1}"}
            items.append((
                "Beta Decay Transformations", q_text, opts, "A",
                f"In β⁻ decay, a neutron converts to a proton and an electron. Proton number increases by 1 ({z} -> {new_z}), mass number {a} remains constant.",
                "How does beta-minus emission alter atomic number while preserving mass number?"
            ))
        # Bohr energy levels
        for n in [2, 3, 4, 5]:
            en = -13.6 / (n ** 2)
            q_text = f"According to the Bohr model of the hydrogen atom, what is the electron energy in the n = {n} orbit? (Ground state E₁ = -13.6 eV)"
            opts = {"A": f"{en:.2f} eV", "B": f"{-13.6 * n:.1f} eV", "C": f"{en * 2:.2f} eV", "D": f"{-13.6 / n:.2f} eV"}
            items.append((
                "Bohr Energy Levels", q_text, opts, "A",
                f"E_n = E₁ / n² = -13.6 / ({n}²) = {en:.2f} eV.",
                "Energy levels scale inversely with the square of the principal quantum number n."
            ))
        # Nuclear binding energy mass defect
        for dm in [0.015, 0.025, 0.035, 0.050]:
            be = dm * 931.5
            q_text = f"Calculate the binding energy of a nucleus possessing a mass defect of {dm} atomic mass units (u). (1 u ≈ 931.5 MeV)"
            opts = {"A": f"{be:.2f} MeV", "B": f"{be / 2:.2f} MeV", "C": f"{be * 2:.2f} MeV", "D": f"{dm * 100:.2f} MeV"}
            items.append((
                "Nuclear Binding Energy", q_text, opts, "A",
                f"E = Δm × 931.5 MeV/u = {dm} × 931.5 = {be:.2f} MeV.",
                "Multiply the mass defect in atomic mass units by 931.5 MeV."
            ))

def append_even_more_modern_physics(items, topic):
    if topic == "Modern & Atomic Physics":
        # De Broglie wavelength: λ = h / (m * v)
        for v_pow in [5, 6]:
            for v_mult in [1.0, 2.0, 3.0, 5.0]:
                v = v_mult * (10 ** v_pow)
                m_e = 9.11e-31
                h = 6.63e-34
                lam = h / (m_e * v)
                q_text = f"Calculate the de Broglie wavelength of an electron traveling at {v:.1e} m/s. (h = 6.63 × 10⁻³⁴ J·s, m_e = 9.11 × 10⁻³¹ kg)"
                opts = {"A": f"{lam:.2e} m", "B": f"{lam * 2:.2e} m", "C": f"{lam / 2:.2e} m", "D": "1.00e-10 m"}
                items.append((
                    "De Broglie Wavelength", q_text, opts, "A",
                    f"λ = h / p = h / (m·v) = (6.63×10⁻³⁴) / (9.11×10⁻³¹ × {v:.1e}) = {lam:.2e} m.",
                    "De Broglie's relation connects momentum and matter wavelength: λ = h/mv."
                ))
        # Decay constant λ = ln(2) / T_half
        for th in [2, 4, 8, 10, 15, 20]:
            lam_decay = 0.693 / th
            q_text = f"A radioactive nuclide has a half-life of {th} hours. Calculate its decay constant λ in hr⁻¹."
            opts = {"A": f"{lam_decay:.4f} hr⁻¹", "B": f"{lam_decay * 2:.4f} hr⁻¹", "C": f"{th / 0.693:.4f} hr⁻¹", "D": f"{lam_decay / 2:.4f} hr⁻¹"}
            items.append((
                "Decay Constant", q_text, opts, "A",
                f"λ = ln(2) / T_{{1/2}} = 0.693 / {th} = {lam_decay:.4f} hr⁻¹.",
                "The decay constant is inversely proportional to half-life."
            ))
        # Radiation properties: Alpha, Beta, Gamma
        rad_props = [
            ("Alpha particle (α)", "Helium-4 nucleus with +2 charge", "Stopped by a sheet of paper or skin", "Highest specific ionization power in air"),
            ("Beta particle (β⁻)", "High-speed electron with -1 charge", "Stopped by a few millimeters of aluminum", "Moderate ionization power"),
            ("Gamma ray (γ)", "High-energy electromagnetic photon", "Requires thick lead or concrete shielding", "Lowest ionization power, highest penetration"),
            ("Positron (β⁺)", "Antielectron with +1 charge", "Annihilates with an electron into gamma photons", "Equal mass to electron with opposite charge")
        ]
        for name, comp, shield, ioniz in rad_props:
            items.append((
                "Nuclear Radiation Properties", f"Which type of nuclear radiation consists of a {comp.lower()}?",
                {"A": name, "B": "Cathode ray", "C": "X-ray", "D": "Neutron flux"}, "A",
                f"{name} is composed of a {comp.lower()}.",
                "Identify the physical composition of nuclear radiation types."
            ))
            items.append((
                "Radiation Shielding", f"Which radiation emission requires {shield.lower()} to be effectively absorbed?",
                {"A": name, "B": "Microwaves", "C": "Infrared rays", "D": "Sound waves"}, "A",
                f"{name} is {shield.lower()}.",
                "Recall penetration depths of alpha, beta, and gamma radiation."
            ))
            items.append((
                "Ionization Power", f"Which radiation is characterized by {ioniz.lower()}?",
                {"A": name, "B": "Radio waves", "C": "Visible light", "D": "Ultraviolet"}, "A",
                f"{name} possesses {ioniz.lower()}.",
                "Compare relative ionization densities of alpha, beta, and gamma."
            ))
