import random
import math

def generate_math_pool(topic, count):
    items = []
    
    if topic == "Algebra":
        # Subtopics: Quadratic roots, Logarithms, Progressions (AP/GP), Polynomials, Matrices, Partial fractions
        for i in range(count):
            sub_type = i % 6
            if sub_type == 0:
                # Quadratic roots α, β
                a = random.choice([2, 3, 4, 5])
                b = random.choice([-10, -8, -6, 6, 8, 12])
                c = random.choice([1, 2, 3, 4, 5])
                # sum = -b/a, prod = c/a, 1/α + 1/β = (α+β)/αβ = -b/c
                ans_val = f"{-b}/{c}" if c != 1 else f"{-b}"
                dist1 = f"{b}/{c}"
                dist2 = f"{c}/{-b}"
                dist3 = f"{-b}/{a}"
                opts = {"A": ans_val, "B": dist1, "C": dist2, "D": dist3}
                q_text = f"If α and β are the roots of the quadratic equation {a}x² + ({b})x + {c} = 0, evaluate 1/α + 1/β."
                items.append((
                    "Quadratic Roots", q_text, opts, "A",
                    f"1/α + 1/β = (α + β) / αβ = (-b/a) / (c/a) = -b/c = -({b})/{c} = {ans_val}.",
                    "What is the algebraic sum of fractions 1/α + 1/β when expressed over a common denominator?"
                ))
            elif sub_type == 1:
                # Logarithms
                base = random.choice([2, 3, 5])
                p = random.choice([3, 4, 5])
                val = base ** p
                q_text = f"Evaluate the logarithmic expression log_{base}({val}) + log_{base}(1/{base})."
                ans_val = f"{p - 1}"
                opts = {"A": ans_val, "B": f"{p}", "C": f"{p + 1}", "D": f"{val - base}"}
                items.append((
                    "Logarithmic Laws", q_text, opts, "A",
                    f"log_{base}({val}) = {p}, and log_{base}({base}⁻¹) = -1. Therefore, {p} + (-1) = {p - 1}.",
                    f"What power of {base} produces {val}, and what is log_b(1/b)?"
                ))
            elif sub_type == 2:
                # AP / GP
                a = random.choice([2, 3, 5, 7])
                d = random.choice([3, 4, 5])
                n = random.choice([10, 12, 15, 20])
                nth_term = a + (n - 1) * d
                q_text = f"The first term of an Arithmetic Progression (AP) is {a} and the common difference is {d}. Find the {n}th term."
                opts = {"A": f"{nth_term}", "B": f"{nth_term - d}", "C": f"{nth_term + d}", "D": f"{a * d * n}"}
                items.append((
                    "Arithmetic Progressions", q_text, opts, "A",
                    f"In an AP, T_n = a + (n - 1)d = {a} + ({n} - 1)({d}) = {a} + ({n-1} × {d}) = {nth_term}.",
                    "What formula gives the n-th term of an arithmetic progression?"
                ))
            elif sub_type == 3:
                # Polynomial remainder
                k = random.choice([1, 2, 3])
                c1, c2, c3 = random.choice([2, 3]), random.choice([-4, -2, 5]), random.choice([-7, 6, 8])
                # P(k) = c1*k^2 + c2*k + c3
                rem = c1 * (k ** 2) + c2 * k + c3
                q_text = f"Find the remainder when P(x) = {c1}x² + ({c2})x + ({c3}) is divided by (x - {k})."
                opts = {"A": f"{rem}", "B": f"{-rem}", "C": f"{rem + c1}", "D": f"{c3}"}
                items.append((
                    "Remainder Theorem", q_text, opts, "A",
                    f"By the Remainder Theorem, the remainder upon division by (x - a) is P(a). Evaluating P({k}) = {c1}({k})² + ({c2})({k}) + ({c3}) = {rem}.",
                    f"According to the Remainder Theorem, what single value of x should you substitute into P(x)?"
                ))
            elif sub_type == 4:
                # 2x2 Matrix Determinant
                a, b, c, d = random.choice([2, 3, 4]), random.choice([1, 5]), random.choice([-2, 3]), random.choice([6, 7])
                det = a * d - b * c
                q_text = f"Calculate the determinant of the 2×2 matrix: [ [{a}, {b}], [{c}, {d}] ]."
                opts = {"A": f"{det}", "B": f"{a * d + b * c}", "C": f"{a + d - b - c}", "D": f"{b * c - a * d}"}
                items.append((
                    "Matrix Determinants", q_text, opts, "A",
                    f"Determinant |A| = (a × d) - (b × c) = ({a} × {d}) - ({b} × {c}) = {a*d} - ({b*c}) = {det}.",
                    "For a 2×2 matrix [ [a, b], [c, d] ], how do you combine the product of principal and secondary diagonals?"
                ))
            else:
                # Geometric progression sum to infinity
                a = random.choice([4, 6, 8, 12])
                r_num, r_den = 1, random.choice([2, 3, 4])
                # S_inf = a / (1 - r) = a / (1 - 1/r_den) = a * r_den / (r_den - 1)
                s_inf = (a * r_den) / (r_den - 1)
                ans_str = f"{int(s_inf)}" if s_inf.is_integer() else f"{int(a * r_den)}/{r_den - 1}"
                q_text = f"Find the sum to infinity of a Geometric Progression with first term a = {a} and common ratio r = {r_num}/{r_den}."
                opts = {"A": ans_str, "B": f"{a * r_den}", "C": f"{a / (r_den)}", "D": f"{int(s_inf) + 2}"}
                items.append((
                    "Sum to Infinity", q_text, opts, "A",
                    f"Sum to infinity S_∞ = a / (1 - r) = {a} / (1 - {r_num}/{r_den}) = {a} / ({(r_den - 1)}/{r_den}) = {ans_str}.",
                    "What is the condition on common ratio r for an infinite geometric series to converge?"
                ))
    
    elif topic == "Calculus":
        # Differentiation, Integration, Maxima/Minima, Rates of Change
        for i in range(count):
            sub_type = i % 5
            if sub_type == 0:
                # Polynomial derivative
                n = random.choice([3, 4, 5, 6])
                c = random.choice([2, 3, 4, 7])
                deriv_c = c * n
                deriv_p = n - 1
                q_text = f"Differentiate y = {c}x^{n} - 5x + 9 with respect to x."
                ans_val = f"{deriv_c}x^{deriv_p} - 5"
                opts = {"A": ans_val, "B": f"{deriv_c}x^{deriv_p}", "C": f"{c}x^{deriv_p} - 5", "D": f"{deriv_c}x^{n} - 5x"}
                items.append((
                    "Differentiation Power Rule", q_text, opts, "A",
                    f"By the power rule, d/dx(ax^n) = a·n x^(n-1). d/dx({c}x^{n} - 5x + 9) = {deriv_c}x^{deriv_p} - 5.",
                    "What happens to the constant term (9) when differentiating with respect to x?"
                ))
            elif sub_type == 1:
                # Trigonometric derivative
                k = random.choice([2, 3, 4, 5])
                q_text = f"Find the derivative of y = sin({k}x) with respect to x."
                opts = {"A": f"{k} cos({k}x)", "B": f"-{k} cos({k}x)", "C": f"cos({k}x)", "D": f"-cos({k}x)"}
                items.append((
                    "Trigonometric Derivatives", q_text, opts, "A",
                    f"By the Chain Rule: d/dx[sin(kx)] = k cos(kx).",
                    f"When differentiating sin({k}x), what is the derivative of the inner function {k}x?"
                ))
            elif sub_type == 2:
                # Definite integral
                k = random.choice([1, 2, 3])
                # integrate 3x^2 from 0 to k = [x^3] from 0 to k = k^3
                ans = k ** 3
                q_text = f"Evaluate the definite integral ∫ [0 to {k}] 3x² dx."
                opts = {"A": f"{ans}", "B": f"{ans * 2}", "C": f"{ans + 3}", "D": f"{ans - 1}"}
                items.append((
                    "Definite Integration", q_text, opts, "A",
                    f"∫ 3x² dx = x³. Evaluating from 0 to {k} yields ({k})³ - 0³ = {ans}.",
                    "What is the antiderivative of 3x² before applying the upper and lower limits?"
                ))
            elif sub_type == 3:
                # Turning points (stationary point of quadratic)
                # y = x^2 - 2bx + c => dy/dx = 2x - 2b = 0 => x = b
                b = random.choice([2, 3, 4, 5])
                c = random.choice([1, 7, 9])
                q_text = f"Find the x-coordinate of the minimum turning point of the curve y = x² - {2*b}x + {c}."
                opts = {"A": f"{b}", "B": f"{-b}", "C": f"{2*b}", "D": f"{c}"}
                items.append((
                    "Turning Points", q_text, opts, "A",
                    f"At a stationary point, dy/dx = 0. 2x - {2*b} = 0 => 2x = {2*b} => x = {b}. Since d²y/dx² = 2 > 0, this is a minimum.",
                    "What is the first derivative condition for any stationary or turning point?"
                ))
            else:
                # Rate of change (Area of circle)
                r = random.choice([3, 4, 5, 6])
                dr_dt = random.choice([2, 3])
                # dA/dt = 2πr (dr/dt)
                ans_rate = 2 * r * dr_dt
                q_text = f"The radius of a circular ripple in a pond expands at {dr_dt} m/s. Find the rate of increase of area when radius r = {r} m."
                opts = {"A": f"{ans_rate}π m²/s", "B": f"{ans_rate // 2}π m²/s", "C": f"{r ** 2 * dr_dt}π m²/s", "D": f"{ans_rate * 2}π m²/s"}
                items.append((
                    "Rates of Change", q_text, opts, "A",
                    f"A = πr². By the Chain Rule: dA/dt = 2πr (dr/dt) = 2π({r})({dr_dt}) = {ans_rate}π m²/s.",
                    "How do you apply the chain rule dA/dt = (dA/dr) × (dr/dt) to circular area?"
                ))

    elif topic == "Geometry & Trigonometry":
        # Circle theorems, coordinate geometry, trig rules, bearings
        for i in range(count):
            sub_type = i % 5
            if sub_type == 0:
                # Circle theorem: Angle at center
                theta = random.choice([35, 40, 45, 50, 65, 70])
                center_angle = 2 * theta
                q_text = f"In a circle with center O, chord AB subtends an angle of {theta}° at the circumference. What angle does AB subtend at the center O?"
                opts = {"A": f"{center_angle}°", "B": f"{theta}°", "C": f"{180 - theta}°", "D": f"{center_angle // 2}°"}
                items.append((
                    "Circle Theorems", q_text, opts, "A",
                    f"The angle subtended by an arc at the center is twice the angle subtended by it at any point on the remaining circumference: 2 × {theta}° = {center_angle}°.",
                    "Does the angle subtended at the center equal double the angle at the circumference?"
                ))
            elif sub_type == 1:
                # Coordinate distance
                dx = random.choice([3, 6, 8])
                dy = 4 if dx == 3 else (8 if dx == 6 else 6)
                dist = int(math.sqrt(dx**2 + dy**2))
                q_text = f"Calculate the Euclidean distance between points P(0, 0) and Q({dx}, {dy})."
                opts = {"A": f"{dist} units", "B": f"{dx + dy} units", "C": f"{dist + 2} units", "D": f"{abs(dx - dy)} units"}
                items.append((
                    "Coordinate Geometry", q_text, opts, "A",
                    f"Distance d = √[(x₂ - x₁)² + (y₂ - y₁)²] = √[{dx}² + {dy}²] = √[{dx**2 + dy**2}] = {dist} units.",
                    "What Pythagorean formula calculates distance between two Cartesian points?"
                ))
            elif sub_type == 2:
                # Cyclic quadrilateral
                opp = random.choice([75, 80, 85, 110, 115])
                supp = 180 - opp
                q_text = f"In a cyclic quadrilateral ABCD, angle A = {opp}°. What is the measure of the opposite angle C?"
                opts = {"A": f"{supp}°", "B": f"{opp}°", "C": f"{360 - opp}°", "D": f"{90}°"}
                items.append((
                    "Cyclic Quadrilaterals", q_text, opts, "A",
                    f"Opposite interior angles of a cyclic quadrilateral are supplementary (sum to 180°): Angle C = 180° - {opp}° = {supp}°.",
                    "What is the sum of opposite interior angles of any cyclic quadrilateral?"
                ))
            elif sub_type == 3:
                # Trigonometric identity
                q_text = "Simplify the trigonometric expression: (1 - cos² θ) / sin² θ."
                opts = {"A": "1", "B": "tan² θ", "C": "cos² θ", "D": "cot² θ"}
                items.append((
                    "Trigonometric Identities", q_text, opts, "A",
                    "From the fundamental identity sin² θ + cos² θ = 1, we have 1 - cos² θ = sin² θ. Thus sin² θ / sin² θ = 1.",
                    "What does the Pythagorean trigonometric identity sin²θ + cos²θ equal?"
                ))
            else:
                # Sine rule
                q_text = "In triangle ABC, side a = 10 cm, angle A = 30°, and angle B = 45°. Calculate side b (in cm, using sin 45° = 1/√2)."
                opts = {"A": "10√2 cm", "B": "5√2 cm", "C": "20 cm", "D": "10 cm"}
                items.append((
                    "The Sine Rule", q_text, opts, "A",
                    "Sine Rule: a / sin A = b / sin B => 10 / sin(30°) = b / sin(45°) => 10 / (1/2) = b / (1/√2) => 20 = b√2 => b = 20 / √2 = 10√2 cm.",
                    "How do you set up the ratio of sides to opposing sines using the Sine Rule?"
                ))

    elif topic == "Statistics & Probability":
        # Probability, Permutations, Combinations, Mean/Median/SD
        for i in range(count):
            sub_type = i % 5
            if sub_type == 0:
                # Independent probability (two dice / coins)
                p1_n, p1_d = random.choice([(1, 2), (1, 6), (2, 5)])
                p2_n, p2_d = random.choice([(1, 2), (1, 3), (3, 4)])
                ans_num = p1_n * p2_n
                ans_den = p1_d * p2_d
                gcd = math.gcd(ans_num, ans_den)
                ans_str = f"{ans_num // gcd}/{ans_den // gcd}"
                q_text = f"If event A has probability {p1_n}/{p1_d} and independent event B has probability {p2_n}/{p2_d}, find P(A and B)."
                opts = {"A": ans_str, "B": f"{(p1_n*p2_d + p2_n*p1_d)}/{ans_den}", "C": f"{p1_n + p2_n}/{p1_d + p2_d}", "D": "1/2"}
                items.append((
                    "Independent Events", q_text, opts, "A",
                    f"For independent events, P(A ∩ B) = P(A) × P(B) = ({p1_n}/{p1_d}) × ({p2_n}/{p2_d}) = {ans_str}.",
                    "Do you multiply or add probabilities when two events are completely independent?"
                ))
            elif sub_type == 1:
                # Combinations nCr
                n = random.choice([5, 6, 7])
                r = 2
                ans = math.comb(n, r)
                q_text = f"In how many ways can a committee of {r} members be chosen from a group of {n} candidates?"
                opts = {"A": f"{ans}", "B": f"{ans * 2}", "C": f"{n * r}", "D": f"{ans - 2}"}
                items.append((
                    "Combinations", q_text, opts, "A",
                    f"Since order does not matter, use combinations: nCr = {n}! / ({r}! × ({n}-{r})!) = {ans}.",
                    "Does the order of selection matter when choosing committee members?"
                ))
            elif sub_type == 2:
                # Permutations nPr
                n = random.choice([4, 5, 6])
                ans = math.perm(n, 2)
                q_text = f"In how many ways can 1st and 2nd prizes be awarded to {n} competing contestants?"
                opts = {"A": f"{ans}", "B": f"{ans // 2}", "C": f"{n ** 2}", "D": f"{ans + n}"}
                items.append((
                    "Permutations", q_text, opts, "A",
                    f"Order matters for ranked prizes: nPr = {n}! / ({n}-2)! = {n} × {n-1} = {ans}.",
                    "Why are ranked prizes calculated using permutations instead of combinations?"
                ))
            elif sub_type == 3:
                # Mean of numbers
                nums = [random.randint(10, 30) for _ in range(5)]
                mean_val = sum(nums) / len(nums)
                q_text = f"Find the arithmetic mean of the dataset: {', '.join(map(str, nums))}."
                opts = {"A": f"{mean_val:.1f}", "B": f"{mean_val + 2:.1f}", "C": f"{mean_val - 1.5:.1f}", "D": f"{nums[2]:.1f}"}
                items.append((
                    "Arithmetic Mean", q_text, opts, "A",
                    f"Mean x̄ = Σx / N = ({' + '.join(map(str, nums))}) / 5 = {sum(nums)} / 5 = {mean_val:.1f}.",
                    "How do you calculate the arithmetic mean of an ungrouped dataset?"
                ))
            else:
                # Standard deviation concept
                q_text = "If every value in a dataset is multiplied by a constant factor of 3, the standard deviation of the new dataset will:"
                opts = {"A": "Be multiplied by 3", "B": "Be multiplied by 9", "C": "Remain unchanged", "D": "Be increased by 3"}
                items.append((
                    "Standard Deviation Properties", q_text, opts, "A",
                    "Multiplying all data values by constant k scales the standard deviation by |k| (here 3). Note that variance would be scaled by k² = 9.",
                    "How does multiplying all observations by k affect standard deviation versus variance?"
                ))

    return items

def generate_physics_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Mechanics":
            sub_type = i % 5
            if sub_type == 0:
                # Equations of motion
                u = random.choice([0, 5, 10])
                a = random.choice([2, 3, 4])
                t = random.choice([3, 4, 5])
                v = u + a * t
                s = u * t + 0.5 * a * (t ** 2)
                q_text = f"A body accelerates uniformly from {u} m/s at {a} m/s² for {t} seconds. Calculate its final velocity."
                opts = {"A": f"{v} m/s", "B": f"{v + 4} m/s", "C": f"{u * t} m/s", "D": f"{v // 2} m/s"}
                items.append((
                    "Equations of Motion", q_text, opts, "A",
                    f"v = u + at = {u} + ({a} × {t}) = {v} m/s.",
                    "Which equation of motion connects initial velocity, acceleration, time, and final velocity?"
                ))
            elif sub_type == 1:
                # Momentum & Impulse
                m = random.choice([2, 4, 5])
                v1, v2 = random.choice([10, 15, 20]), random.choice([0, -5])
                impulse = abs(m * (v2 - v1))
                q_text = f"A ball of mass {m} kg moving at {v1} m/s hits a wall and stops (v = 0 m/s). What is the magnitude of impulse delivered to the ball?"
                opts = {"A": f"{impulse} N·s", "B": f"{impulse // 2} N·s", "C": f"{impulse * 2} N·s", "D": f"{m * 10} N·s"}
                items.append((
                    "Momentum & Impulse", q_text, opts, "A",
                    f"Impulse I = Δp = m(v₂ - v₁) = {m}(0 - {v1}) = {-impulse} N·s (magnitude is {impulse} N·s).",
                    "How is impulse related to change in linear momentum?"
                ))
            elif sub_type == 2:
                # Work and Kinetic Energy
                m = random.choice([2, 4, 10])
                v = random.choice([3, 4, 5, 6])
                ke = int(0.5 * m * (v ** 2))
                q_text = f"Calculate the kinetic energy of a body of mass {m} kg moving with a uniform speed of {v} m/s."
                opts = {"A": f"{ke} J", "B": f"{ke * 2} J", "C": f"{m * v} J", "D": f"{ke // 2} J"}
                items.append((
                    "Kinetic Energy", q_text, opts, "A",
                    f"KE = 1/2 mv² = 0.5 × {m} × ({v})² = 0.5 × {m} × {v**2} = {ke} J.",
                    "In the kinetic energy formula KE = 1/2 mv², is velocity squared or linear?"
                ))
            elif sub_type == 3:
                # Centripetal acceleration
                v = random.choice([10, 20])
                r = random.choice([20, 50, 100])
                ac = (v ** 2) / r
                q_text = f"A vehicle rounds a circular track of radius {r} m at a constant speed of {v} m/s. What is its centripetal acceleration?"
                opts = {"A": f"{ac:.1f} m/s²", "B": f"{ac * 2:.1f} m/s²", "C": f"{v / r:.2f} m/s²", "D": f"{ac / 2:.1f} m/s²"}
                items.append((
                    "Circular Motion", q_text, opts, "A",
                    f"Centripetal acceleration a_c = v² / r = ({v})² / {r} = {v**2} / {r} = {ac:.1f} m/s².",
                    "What formula connects tangential speed and radius to inward centripetal acceleration?"
                ))
            else:
                # Limiting friction
                m = random.choice([5, 10, 20])
                mu = random.choice([0.2, 0.3, 0.5])
                fl = mu * m * 10
                q_text = f"A box of mass {m} kg rests on a horizontal floor with static friction coefficient μ = {mu}. What force is required to initiate motion? (g = 10 m/s²)"
                opts = {"A": f"{fl:.1f} N", "B": f"{m * 10} N", "C": f"{fl / 2:.1f} N", "D": f"{mu * 10} N"}
                items.append((
                    "Friction", q_text, opts, "A",
                    f"Limiting friction F_L = μR = μ(mg) = {mu} × {m} × 10 = {fl:.1f} N.",
                    "What is the normal reaction force on a flat horizontal surface?"
                ))
        
        elif topic == "Thermal Physics & Waves":
            sub_type = i % 5
            if sub_type == 0:
                # Boyle's Law
                p1 = random.choice([1, 2, 3])
                v1 = random.choice([200, 300, 600])
                p2 = p1 * random.choice([2, 3])
                v2 = (p1 * v1) / p2
                q_text = f"A gas occupies {v1} cm³ at {p1} atm. If pressure is increased isothermally to {p2} atm, what is the new volume?"
                opts = {"A": f"{int(v2)} cm³", "B": f"{int(v2 * 2)} cm³", "C": f"{v1} cm³", "D": f"{int(v2 // 2)} cm³"}
                items.append((
                    "Boyle's Law", q_text, opts, "A",
                    f"P₁V₁ = P₂V₂ => {p1} × {v1} = {p2} × V₂ => V₂ = ({p1 * v1}) / {p2} = {int(v2)} cm³.",
                    "Does Boyle's Law state that pressure and volume are inversely proportional at constant temperature?"
                ))
            elif sub_type == 1:
                # Specific Heat Capacity
                m = random.choice([1, 2, 3])
                c_water = 4200
                dt = random.choice([5, 10, 20])
                q_heat = m * c_water * dt
                q_text = f"How much heat energy is required to raise the temperature of {m} kg of water by {dt}°C? (c = 4200 J/kg·K)"
                opts = {"A": f"{q_heat} J", "B": f"{q_heat // 2} J", "C": f"{q_heat * 2} J", "D": f"{c_water * dt} J"}
                items.append((
                    "Specific Heat Capacity", q_text, opts, "A",
                    f"Q = mcΔθ = {m} × 4200 × {dt} = {q_heat} J.",
                    "What formula gives thermal energy required for temperature rise without phase change?"
                ))
            elif sub_type == 2:
                # Wave Equation
                f_hz = random.choice([100, 200, 256, 440, 500])
                v_sound = 340
                lam = v_sound / f_hz
                q_text = f"A tuning fork vibrates at {f_hz} Hz in air where sound speed is 340 m/s. What is the wavelength of the emitted sound?"
                opts = {"A": f"{lam:.2f} m", "B": f"{lam * 2:.2f} m", "C": f"{f_hz * 340} m", "D": f"{lam / 2:.2f} m"}
                items.append((
                    "The Wave Equation", q_text, opts, "A",
                    f"v = fλ => λ = v / f = 340 / {f_hz} = {lam:.2f} m.",
                    "How are wave speed, frequency, and wavelength related in the fundamental wave equation?"
                ))
            elif sub_type == 3:
                # Snell's Law & Refractive Index
                n = random.choice([1.5, 1.33, 2.4])
                q_text = f"Light travels from vacuum (c = 3.0 × 10⁸ m/s) into a medium with refractive index n = {n}. What is the speed of light in this medium?"
                v_med = (3.0 * 10**8) / n
                opts = {"A": f"{v_med:.2e} m/s", "B": f"{(3.0 * 10**8 * n):.2e} m/s", "C": "3.00e+08 m/s", "D": f"{(v_med / 2):.2e} m/s"}
                items.append((
                    "Refractive Index", q_text, opts, "A",
                    f"Refractive index n = c / v => v = c / n = (3.0 × 10⁸) / {n} = {v_med:.2e} m/s.",
                    "Does light slow down when entering a denser optical medium with n > 1?"
                ))
            else:
                # Doppler effect concept
                q_text = "When an ambulance sounding a high-pitch siren moves rapidly towards a stationary pedestrian, the pitch heard by the pedestrian:"
                opts = {"A": "Increases due to compressed sound wavefronts", "B": "Decreases", "C": "Remains completely unchanged", "D": "Drops to zero"}
                items.append((
                    "Doppler Effect", q_text, opts, "A",
                    "Relative approach of the sound source compresses successive wave crests, increasing observed frequency (pitch).",
                    "What happens to apparent wave crest spacing when the sound source moves closer?"
                ))

        elif topic == "Electricity & Magnetism":
            sub_type = i % 4
            if sub_type == 0:
                # Parallel resistors
                r = random.choice([6, 10, 12, 20])
                r_parallel = r / 2
                q_text = f"Two identical resistors of resistance {r} Ω each are connected in parallel. What is their equivalent resistance?"
                opts = {"A": f"{r_parallel:.1f} Ω", "B": f"{r * 2} Ω", "C": f"{r} Ω", "D": f"{r_parallel / 2:.1f} Ω"}
                items.append((
                    "Resistor Networks", q_text, opts, "A",
                    f"For two identical resistors R in parallel, R_eq = R / 2 = {r} / 2 = {r_parallel:.1f} Ω.",
                    "When identical resistors are connected in parallel, how does total resistance relate to R/n?"
                ))
            elif sub_type == 1:
                # Ohm's Law & Internal resistance
                e = random.choice([6, 12, 24])
                r_int = random.choice([1, 2])
                r_ext = random.choice([4, 10])
                i_curr = e / (r_ext + r_int)
                q_text = f"A battery of emf {e} V and internal resistance {r_int} Ω is connected across an external resistor of {r_ext} Ω. Find the circuit current."
                opts = {"A": f"{i_curr:.2f} A", "B": f"{(e / r_ext):.2f} A", "C": f"{(e / r_int):.2f} A", "D": f"{i_curr * 2:.2f} A"}
                items.append((
                    "Internal Resistance", q_text, opts, "A",
                    f"Total resistance R_total = R + r = {r_ext} + {r_int} = {r_ext + r_int} Ω. Current I = E / (R + r) = {e} / {r_ext + r_int} = {i_curr:.2f} A.",
                    "Must internal resistance be added in series to the external load resistance?"
                ))
            elif sub_type == 2:
                # Transformers
                v_p = 240
                np = random.choice([1000, 1200])
                ns = random.choice([100, 200])
                vs = (v_p * ns) / np
                q_text = f"An ideal step-down transformer has {np} primary turns and {ns} secondary turns. If primary voltage is 240 V, what is secondary voltage?"
                opts = {"A": f"{vs:.1f} V", "B": f"{vs * 2:.1f} V", "C": f"{240 * np / ns:.1f} V", "D": "24 V"}
                items.append((
                    "Transformers", q_text, opts, "A",
                    f"V_s / V_p = N_s / N_p => V_s = 240 × ({ns} / {np}) = {vs:.1f} V.",
                    "What is the transformer turns ratio relating secondary voltage to primary voltage?"
                ))
            else:
                # Capacitor charge
                c_uf = random.choice([5, 10, 20])
                v = random.choice([6, 12])
                q_uc = c_uf * v
                q_text = f"What quantity of electric charge is stored on a {c_uf} μF capacitor connected across a {v} V battery?"
                opts = {"A": f"{q_uc} μC", "B": f"{q_uc // 2} μC", "C": f"{c_uf / v:.2f} μC", "D": f"{q_uc * 2} μC"}
                items.append((
                    "Capacitors", q_text, opts, "A",
                    f"Q = C × V = {c_uf} μF × {v} V = {q_uc} μC.",
                    "What fundamental equation links charge, capacitance, and potential difference?"
                ))

        else: # Modern & Atomic Physics
            sub_type = i % 4
            if sub_type == 0:
                # Half-life calculation
                t_half = random.choice([2, 4, 5, 8])
                periods = random.choice([2, 3])
                total_time = t_half * periods
                fraction = 1 / (2 ** periods)
                q_text = f"A radioactive isotope has a half-life of {t_half} days. What fraction of the original sample remains undecayed after {total_time} days?"
                opts = {"A": f"1/{2**periods}", "B": f"1/{2**(periods-1)}", "C": f"1/{2**(periods+1)}", "D": f"{periods}/{t_half}"}
                items.append((
                    "Radioactive Half-Life", q_text, opts, "A",
                    f"Number of half-life periods n = {total_time} / {t_half} = {periods}. Fraction remaining = (1/2)^{periods} = 1/{2**periods}.",
                    "How many times do you halve the radioactive sample over n half-life periods?"
                ))
            elif sub_type == 1:
                # Photon energy
                q_text = "According to Planck's quantum theory, the energy E carried by a single photon of frequency f is expressed as:"
                opts = {"A": "E = hf", "B": "E = h / f", "C": "E = 1/2 hf²", "D": "E = hc"}
                items.append((
                    "Photon Energy", q_text, opts, "A",
                    "Max Planck formulated that light is emitted in discrete quanta of energy proportional to frequency: E = hf.",
                    "What constant of proportionality links photon frequency to its quantum energy?"
                ))
            elif sub_type == 2:
                # Alpha decay
                q_text = "When an unstable uranium nucleus (²³⁸₉₂U) emits an alpha particle (⁴₂He), the daughter thorium nucleus has mass number and atomic number:"
                opts = {"A": "A = 234, Z = 90", "B": "A = 238, Z = 91", "C": "A = 234, Z = 92", "D": "A = 236, Z = 90"}
                items.append((
                    "Alpha Radioactive Decay", q_text, opts, "A",
                    "Alpha emission removes 2 protons and 2 neutrons: A decreases by 4 (238 - 4 = 234) and Z decreases by 2 (92 - 2 = 90).",
                    "How many protons and nucleons are carried away by an emitted alpha particle?"
                ))
            else:
                # De Broglie wavelength
                q_text = "The de Broglie wavelength λ of a subatomic particle moving with linear momentum p is given by:"
                opts = {"A": "λ = h / p", "B": "λ = p / h", "C": "λ = h × p", "D": "λ = hf"}
                items.append((
                    "De Broglie Wavelength", q_text, opts, "A",
                    "Louis de Broglie postulated wave-particle duality: wavelength λ = h / p = h / (mv).",
                    "How does de Broglie wavelength relate to Planck's constant and linear momentum?"
                ))

    return items

def generate_chemistry_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Physical & General Chemistry":
            sub_type = i % 4
            if sub_type == 0:
                # Mole concept
                mass = random.choice([12, 24, 48])
                moles = mass / 24 # for Mg
                q_text = f"How many moles of magnesium (Mg) atoms are present in {mass} g of magnesium? (Molar mass of Mg = 24 g/mol)"
                opts = {"A": f"{moles:.2f} mol", "B": f"{moles * 2:.2f} mol", "C": f"{mass * 24} mol", "D": f"{moles / 2:.2f} mol"}
                items.append((
                    "The Mole Concept", q_text, opts, "A",
                    f"Moles n = mass / molar mass = {mass} / 24 = {moles:.2f} mol.",
                    "What formula converts mass in grams to chemical amount in moles?"
                ))
            elif sub_type == 1:
                # Le Chatelier equilibrium
                q_text = "For the exothermic reversible reaction: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH < 0), what condition will shift equilibrium to the right to produce more ammonia?"
                opts = {"A": "Increasing pressure and lowering temperature", "B": "Decreasing pressure and raising temperature", "C": "Adding an inert gas at constant volume", "D": "Removing N₂ gas"}
                items.append((
                    "Le Chatelier's Principle", q_text, opts, "A",
                    "4 gas reactant moles produce 2 product moles, so higher pressure shifts right toward fewer gas moles. Since forward reaction is exothermic, lower temperature shifts forward.",
                    "Does increasing pressure favor the side of the equilibrium reaction with fewer moles of gas?"
                ))
            elif sub_type == 2:
                # pH calculation
                h_conc = random.choice([1e-2, 1e-3, 1e-4, 1e-5])
                ph_val = int(-math.log10(h_conc))
                q_text = f"What is the pH of an aqueous hydrochloric acid solution with hydrogen ion concentration [H⁺] = 1.0 × 10⁻{ph_val} mol/dm³?"
                opts = {"A": f"{ph_val}", "B": f"{14 - ph_val}", "C": f"{ph_val + 1}", "D": f"{ph_val - 1}"}
                items.append((
                    "pH of Solutions", q_text, opts, "A",
                    f"pH = -log₁₀[H⁺] = -log₁₀(1.0 × 10⁻{ph_val}) = {ph_val}.",
                    "What logarithmic formula defines pH from hydrogen ion concentration?"
                ))
            else:
                # Reaction kinetics
                q_text = "In chemical kinetics, adding a positive catalyst increases the rate of a chemical reaction because it:"
                opts = {"A": "Provides an alternative reaction pathway with lower activation energy", "B": "Increases the enthalpy change ΔH of the reaction", "C": "Increases the kinetic energy of reactant particles", "D": "Shifts the chemical equilibrium constant K_c"}
                items.append((
                    "Catalysis & Activation Energy", q_text, opts, "A",
                    "A catalyst lowers the activation energy barrier without altering reaction enthalpy (ΔH) or equilibrium position.",
                    "Does a catalyst alter the enthalpy of a reaction, or does it lower activation energy?"
                ))

        elif topic == "Inorganic Chemistry":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "Moving from left to right across Period 3 of the Periodic Table, the first ionization energy generally increases because:"
                opts = {"A": "Nuclear charge increases while electron screening shielding remains constant", "B": "Atomic radius increases significantly", "C": "The number of filled electron shells increases", "D": "Electronegativity drops to zero"}
                items.append((
                    "Periodic Trends", q_text, opts, "A",
                    "Across a period, proton number increases in the nucleus pulling the valence shell closer, while shielding remains identical.",
                    "What happens to nuclear pull across a period when electrons enter the same shell?"
                ))
            elif sub_type == 1:
                q_text = "In the industrial blast furnace extraction of iron from hematite (Fe₂O₃), limestone (CaCO₃) is added primarily to:"
                opts = {"A": "Decompose into CaO and remove sandy silica (SiO₂) impurities as molten slag (CaSiO₃)", "B": "Reduce iron(III) oxide directly to iron", "C": "Act as a fuel to heat the furnace", "D": "Oxidize molten iron"}
                items.append((
                    "Extraction of Iron", q_text, opts, "A",
                    "Thermal decomposition CaCO₃ -> CaO + CO₂. Basic CaO reacts with acidic silica impurity: CaO + SiO₂ -> CaSiO₃ (molten slag).",
                    "What substance in the blast furnace reacts with silica sand to form molten slag?"
                ))
            elif sub_type == 2:
                q_text = "When aqueous sodium hydroxide (NaOH) is added dropwise to an unknown salt solution, a reddish-brown precipitate is formed which is insoluble in excess NaOH. The cation present is:"
                opts = {"A": "Fe³⁺ (Iron(III))", "B": "Fe²⁺ (Iron(II))", "C": "Cu²⁺ (Copper(II))", "D": "Al³⁺ (Aluminum)"}
                items.append((
                    "Qualitative Salt Analysis", q_text, opts, "A",
                    "Fe³⁺ forms reddish-brown Fe(OH)₃ insoluble in excess alkali. Fe²⁺ gives dirty green, and Cu²⁺ gives pale blue.",
                    "Which transition metal cation forms a characteristic rust reddish-brown precipitate with NaOH?"
                ))
            else:
                q_text = "Which of the following halogens will spontaneously displace bromide ions (Br⁻) from aqueous sodium bromide solution?"
                opts = {"A": "Chlorine (Cl₂)", "B": "Iodine (I₂)", "C": "Astatine (At₂)", "D": "Sulfur (S)"}
                items.append((
                    "Halogen Reactivity", q_text, opts, "A",
                    "Reactivity of halogens decreases down Group 7. Chlorine is more electronegative than bromine and oxidizes 2Br⁻ to Br₂: Cl₂ + 2Br⁻ -> 2Cl⁻ + Br₂.",
                    "Can a halogen higher up in Group 7 displace a halide below it in aqueous solution?"
                ))

        elif topic == "Organic Chemistry":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "What is the systematic IUPAC name of the branched hydrocarbon: CH₃-CH(CH₃)-CH₂-CH₃?"
                opts = {"A": "2-Methylbutane", "B": "Isopentane", "C": "3-Methylbutane", "D": "2-Ethylpropane"}
                items.append((
                    "IUPAC Nomenclature", q_text, opts, "A",
                    "The longest continuous carbon chain has 4 carbons (butane), numbered from the left to give the methyl substituent the lowest locant (2-methylbutane).",
                    "How do you number the longest carbon chain to ensure the substituent gets the lowest number?"
                ))
            elif sub_type == 1:
                q_text = "Which of the following pairs of compounds are geometric (cis-trans) isomers of each other?"
                opts = {"A": "cis-But-2-ene and trans-But-2-ene", "B": "But-1-ene and But-2-ene", "C": "Propan-1-ol and Propan-2-ol", "D": "Ethanoic acid and Methyl methanoate"}
                items.append((
                    "Geometric Isomerism", q_text, opts, "A",
                    "Geometric isomerism occurs due to restricted rotation about C=C double bonds where each double-bonded carbon bears two different atoms/groups (H and CH₃).",
                    "What structural feature prevents free rotation and produces cis and trans isomers?"
                ))
            elif sub_type == 2:
                q_text = "Heating ethanol with excess concentrated sulfuric acid (H₂SO₄) at 170°C produces:"
                opts = {"A": "Ethene (C₂H₄) via dehydration", "B": "Ethoxyethane (ether)", "C": "Ethanoic acid", "D": "Ethyl hydrogen sulfate"}
                items.append((
                    "Dehydration of Alkanols", q_text, opts, "A",
                    "At 170°C with excess conc H₂SO₄, ethanol undergoes intramolecular dehydration to yield ethene: C₂H₅OH -> C₂H₄ + H₂O.",
                    "What elimination product forms when alcohol loses a water molecule at 170°C?"
                ))
            else:
                q_text = "Saponification of vegetable oils or animal fats with sodium hydroxide solution produces soap and:"
                opts = {"A": "Glycerol (Propane-1,2,3-triol)", "B": "Ethanol", "C": "Ethanoic acid", "D": "Glucose"}
                items.append((
                    "Saponification of Esters", q_text, opts, "A",
                    "Triglyceride fats are triesters of glycerol. Base hydrolysis yields sodium salts of fatty acids (soap) and glycerol.",
                    "What trihydric alcohol byproduct is produced when fats are boiled with caustic soda?"
                ))

        else: # Environmental & Industrial Chemistry
            sub_type = i % 4
            if sub_type == 0:
                # Faraday's law of electrolysis
                # 1 Faraday = 96500 C deposits 1 eq
                q_text = "How many Faradays of electricity are required to deposit 1 mole of copper metal from aqueous copper(II) sulfate (CuSO₄) solution?"
                opts = {"A": "2 Faradays", "B": "1 Faraday", "C": "4 Faradays", "D": "0.5 Faradays"}
                items.append((
                    "Faraday's Laws of Electrolysis", q_text, opts, "A",
                    "Cathode reaction: Cu²⁺ + 2e⁻ -> Cu(s). Depositing 1 mole of divalent Cu²⁺ requires 2 moles of electrons = 2 Faradays.",
                    "How many electrons must each Cu²⁺ copper ion gain at the cathode to become a neutral atom?"
                ))
            elif sub_type == 1:
                q_text = "Temporary hardness of water is caused by the presence of dissolved:"
                opts = {"A": "Calcium hydrogencarbonate (Ca(HCO₃)₂)", "B": "Calcium sulfate (CaSO₄)", "C": "Magnesium chloride (MgCl₂)", "D": "Sodium chloride (NaCl)"}
                items.append((
                    "Water Hardness", q_text, opts, "A",
                    "Temporary hardness is caused by hydrogencarbonates (Ca(HCO₃)₂ / Mg(HCO₃)₂) and can be eliminated simply by boiling.",
                    "Which dissolved salt decomposes upon boiling to deposit insoluble calcium carbonate scale?"
                ))
            elif sub_type == 2:
                q_text = "In the industrial Contact Process for the manufacture of sulfuric acid (H₂SO₄), the catalyst utilized in the oxidation of SO₂ to SO₃ is:"
                opts = {"A": "Vanadium(V) oxide (V₂O₅)", "B": "Finely divided iron (Fe)", "C": "Platinum-rhodium gauze", "D": "Nickel (Ni)"}
                items.append((
                    "The Contact Process", q_text, opts, "A",
                    "V₂O₅ catalyzes the reversible oxidation of sulfur dioxide to sulfur trioxide (2SO₂ + O₂ ⇌ 2SO₃) at ~450°C.",
                    "Which transition metal oxide catalyst is famously used in the Contact Process?"
                ))
            else:
                q_text = "Carbon monoxide (CO) is a deadly atmospheric poison primarily because:"
                opts = {"A": "It binds irreversibly to hemoglobin forming carboxyhemoglobin, preventing oxygen transport", "B": "It causes immediate destruction of the ozone layer", "C": "It forms concentrated sulfuric acid in the lungs", "D": "It dissolves alveoli membranes"}
                items.append((
                    "Air Pollution & Toxicology", q_text, opts, "A",
                    "CO has an affinity for hemoglobin over 200 times greater than oxygen, forming stable carboxyhemoglobin and causing suffocation.",
                    "Why does carbon monoxide prevent red blood cells from carrying oxygen to vital organs?"
                ))

    return items

def generate_biology_pool(topic, count):
    items = []
    for i in range(count):
        if topic == "Cellular Biology & Life Processes":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "Which cellular organelle is responsible for synthesizing ATP energy through aerobic cellular respiration?"
                opts = {"A": "Mitochondrion", "B": "Ribosome", "C": "Golgi apparatus", "D": "Lysosome"}
                items.append((
                    "Cell Organelles", q_text, opts, "A",
                    "Mitochondria are the powerhouses of eukaryotic cells, executing the Krebs cycle and oxidative phosphorylation to produce ATP.",
                    "Which organelle contains cristae and generates ATP for metabolic processes?"
                ))
            elif sub_type == 1:
                q_text = "When fresh plant epidermal cells are placed in a concentrated (hypertonic) salt solution, the cells undergo:"
                opts = {"A": "Plasmolysis (shrinkage of the cytoplasm away from the cell wall)", "B": "Hemolysis", "C": "Turgidity", "D": "Active endocytosis"}
                items.append((
                    "Osmosis & Plasmolysis", q_text, opts, "A",
                    "In hypertonic media, water exits the plant cell sap vacuole by osmosis, causing protoplasm to pull away from the rigid cell wall.",
                    "What happens to a plant cell when water leaves its vacuole into a concentrated surrounding solution?"
                ))
            elif sub_type == 2:
                q_text = "Enzymes cease to function at temperatures above 60°C primarily because:"
                opts = {"A": "Their tertiary protein structure is denatured, destroying the active site geometry", "B": "Substrate molecules decompose into nitrogen", "C": "Water evaporates from the cytoplasm", "D": "Activation energy becomes zero"}
                items.append((
                    "Enzyme Kinetics", q_text, opts, "A",
                    "Excess thermal energy ruptures hydrogen and ionic bonds stabilizing the delicate active site, causing irreversible denaturation.",
                    "What happens to the catalytic active site of an enzyme protein when exposed to extreme heat?"
                ))
            else:
                q_text = "During aerobic cellular respiration, the breakdown of one molecule of glucose yields approximately how many net ATP molecules?"
                opts = {"A": "36 to 38 ATP", "B": "2 ATP", "C": "100 ATP", "D": "12 ATP"}
                items.append((
                    "Cellular Respiration", q_text, opts, "A",
                    "Glycolysis yields 2 ATP, and the Krebs cycle plus electron transport chain generates 34-36 ATP, totaling 36-38 ATP.",
                    "What is the total theoretical ATP yield when one glucose molecule is completely oxidized aerobically?"
                ))

        elif topic == "Human Physiology & Systems":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "Which blood vessel transports oxygenated blood from the lungs directly into the left atrium of the heart?"
                opts = {"A": "Pulmonary vein", "B": "Pulmonary artery", "C": "Aorta", "D": "Hepatic portal vein"}
                items.append((
                    "Circulatory System", q_text, opts, "A",
                    "The pulmonary vein is the exception among adult veins, carrying oxygen-rich blood from the pulmonary capillaries back to the left atrium.",
                    "Which specific vein in the human body carries freshly oxygenated blood from the lungs?"
                ))
            elif sub_type == 1:
                q_text = "In the human nephron, ultrafiltration of blood under high hydrostatic pressure takes place across the:"
                opts = {"A": "Glomerulus into Bowman's capsule", "B": "Loop of Henle", "C": "Distal convoluted tubule", "D": "Collecting duct"}
                items.append((
                    "Excretory System", q_text, opts, "A",
                    "High pressure in the glomerulus forces water, glucose, salts, and urea through podocytes into Bowman's capsule as glomerular filtrate.",
                    "Where does pressure filtration of plasma occur in the renal corpuscle?"
                ))
            elif sub_type == 2:
                q_text = "The hormone secreted by the islets of Langerhans in the pancreas that lowers blood glucose levels is:"
                opts = {"A": "Insulin", "B": "Glucagon", "C": "Thyroxine", "D": "Adrenaline"}
                items.append((
                    "Endocrine System", q_text, opts, "A",
                    "Beta cells secrete insulin to convert excess circulating glucose into glycogen stored in liver and skeletal muscles.",
                    "Which pancreatic hormone promotes cellular uptake and storage of glucose as glycogen?"
                ))
            else:
                q_text = "In the human digestive tract, emulsification of dietary fats into microscopic droplets is carried out by:"
                opts = {"A": "Bile salts synthesized in the liver", "B": "Pepsin in the stomach", "C": "Salivary amylase", "D": "Hydrochloric acid"}
                items.append((
                    "Digestive System", q_text, opts, "A",
                    "Bile salts contain no enzymes but mechanically emulsify large lipid globules to expand surface area for lipase action.",
                    "What liver secretion mechanically breaks down fats into smaller droplets in the duodenum?"
                ))

        elif topic == "Genetics & Evolution":
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In a Mendelian monohybrid cross between two heterozygous tall pea plants (Tt × Tt), the expected phenotypic ratio among offspring is:"
                opts = {"A": "3 Tall : 1 Short", "B": "1 Tall : 2 Medium : 1 Short", "C": "All Tall", "D": "9 Tall : 3 Short"}
                items.append((
                    "Mendelian Genetics", q_text, opts, "A",
                    "Genotypes: 1 TT : 2 Tt : 1 tt. Because T is completely dominant over t, 3 out of 4 offspring are phenotypically tall (3:1).",
                    "What phenotypic ratio is produced when dominant and recessive alleles segregate in a monohybrid cross?"
                ))
            elif sub_type == 1:
                q_text = "A man with blood group AB marries a woman with blood group O. What are the possible blood groups of their children?"
                opts = {"A": "Group A or Group B only", "B": "Group AB or Group O only", "C": "Group O only", "D": "Group A, B, AB, or O"}
                items.append((
                    "Codominance & Blood Groups", q_text, opts, "A",
                    "Father contributes I^A or I^B; mother contributes only i. Offspring genotypes are I^A i (Group A) or I^B i (Group B).",
                    "Can parents with genotypes I^A I^B and ii ever have a child with blood group O or AB?"
                ))
            elif sub_type == 2:
                q_text = "Sex-linked recessive traits such as hemophilia and red-green color blindness appear more frequently in human males because:"
                opts = {"A": "Males are hemizygous (XY) and have only one X chromosome with no homologous allele on the Y", "B": "Y chromosomes carry mutant suppressor genes", "C": "Females cannot carry the recessive allele", "D": "Testosterone activates the mutant gene"}
                items.append((
                    "Sex Linkage", q_text, opts, "A",
                    "Males receive a single X chromosome from their mother. A single recessive allele on X manifests immediately as the disorder.",
                    "Why does a single recessive X-linked allele always express itself phenotypically in a male?"
                ))
            else:
                q_text = "Structures in different organisms that share a common evolutionary origin and anatomical plan, despite performing different functions (such as the human arm and bat wing), are termed:"
                opts = {"A": "Homologous structures", "B": "Analogous structures", "C": "Vestigial organs", "D": "Convergent adaptations"}
                items.append((
                    "Evidence of Evolution", q_text, opts, "A",
                    "Homologous structures reflect divergent evolution from a common ancestral pentadactyl limb.",
                    "What is the evolutionary term for organs with similar developmental origins but different functions?"
                ))

        else: # Ecology & Environment
            sub_type = i % 4
            if sub_type == 0:
                q_text = "In an ecological food chain, why does available metabolic energy decrease drastically (by ~90%) at each successive trophic level?"
                opts = {"A": "Energy is dissipated as respiratory heat, locomotion, and non-consumed biomass", "B": "Carnivores consume energy faster than herbivores", "C": "Solar radiation decreases down the food chain", "D": "Decomposers destroy all chemical bonds"}
                items.append((
                    "Trophic Energy Transfer", q_text, opts, "A",
                    "According to Lindeman's 10% rule, ~90% of gross energy is lost to metabolic maintenance, cellular respiration, and heat.",
                    "Why can food chains rarely support more than 4 or 5 consecutive trophic levels?"
                ))
            elif sub_type == 1:
                q_text = "Which Nigerian vegetation zone is characterized by tall buttress-rooted emergent trees, multi-layered canopies, epiphytes, and annual rainfall exceeding 2000 mm?"
                opts = {"A": "Tropical Rainforest", "B": "Sahel Savanna", "C": "Sudan Savanna", "D": "Montane Grassland"}
                items.append((
                    "Biomes of Nigeria", q_text, opts, "A",
                    "The Southern Nigerian tropical rainforest zone features dense strata, continuous canopy layers, and year-round high precipitation.",
                    "Which vegetation belt in Southern Nigeria features emergent hardwoods like Iroko and Mahogany?"
                ))
            elif sub_type == 2:
                q_text = "In the biological nitrogen cycle, the conversion of ammonia (NH₃) into nitrites (NO₂⁻) in soil is carried out by:"
                opts = {"A": "Nitrosomonas bacteria", "B": "Nitrobacter bacteria", "C": "Pseudomonas denitrificans", "D": "Rhizobium leguminosarum"}
                items.append((
                    "The Nitrogen Cycle", q_text, opts, "A",
                    "Two-step nitrification: Nitrosomonas oxidizes NH₃ to NO₂⁻, and Nitrobacter subsequently oxidizes NO₂⁻ to NO₃⁻.",
                    "Which specific genus of nitrifying bacteria oxidizes soil ammonia into nitrites?"
                ))
            else:
                q_text = "Xerophytic plants such as cacti and acacia possess sunken stomata, succulent stems, and reduced needle-like leaves primarily to:"
                opts = {"A": "Minimize transpirational water loss in arid environments", "B": "Prevent predation by grazing herbivores", "C": "Absorb more carbon dioxide at night", "D": "Speed up photosynthetic rate"}
                items.append((
                    "Ecological Adaptations", q_text, opts, "A",
                    "Thick cuticles, reduced surface-area-to-volume ratios, and sunken stomata create humid microclimates that curb transpiration.",
                    "How do modified waxy needles and sunken stomata help desert plants conserve moisture?"
                ))

    return items
