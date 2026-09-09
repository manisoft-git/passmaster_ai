import math
import random

def generate_math_questions(topic, count_needed=150):
    items = []

    if topic == "Algebra":
        # 1. Quadratic equations and roots α, β
        for a in [1, 2, 3]:
            for b in [-8, -7, -6, -5, 5, 6, 7, 8]:
                for c in [1, 2, 3, 4, 6]:
                    ans_recip = f"{-b}/{c}" if c != 1 else f"{-b}"
                    q_text = f"If α and β are the distinct roots of the quadratic equation {a}x² + ({b})x + {c} = 0, find the value of (1/α + 1/β)."
                    opts = {"A": ans_recip, "B": f"{b}/{c}", "C": f"{-b}/{a}", "D": f"{c}/{-b}"}
                    items.append((
                        "Quadratic Roots", q_text, opts, "A",
                        f"1/α + 1/β = (α + β)/αβ = (-b/a) / (c/a) = -b/c = -({b})/{c} = {ans_recip}.",
                        "Express 1/α + 1/β over a common denominator: (α + β)/(αβ)."
                    ))
        # 2. Sum of roots and product of roots to form equation
        for s in [-5, -3, 2, 4, 7]:
            for p in [-6, -2, 3, 5, 8]:
                sign_s = f"- {s}x" if s >= 0 else f"+ {abs(s)}x"
                sign_p = f"+ {p}" if p >= 0 else f"- {abs(p)}"
                eq = f"x² {sign_s} {sign_p} = 0"
                q_text = f"Find the quadratic equation whose sum of roots is {s} and product of roots is {p}."
                opts = {"A": eq, "B": f"x² + {s}x + {p} = 0", "C": f"x² - {p}x + {s} = 0", "D": f"x² + {p}x - {s} = 0"}
                items.append((
                    "Formation of Quadratics", q_text, opts, "A",
                    f"A quadratic equation with root sum S and product P is x² - Sx + P = 0. Here S = {s}, P = {p} => {eq}.",
                    "Recall the standard form: x² - (sum of roots)x + (product of roots) = 0."
                ))
        # 3. Arithmetic Progressions (AP)
        for a in [2, 3, 5, 7, 10]:
            for d in [3, 4, 5, 6]:
                for n in [8, 11, 15, 20]:
                    nth = a + (n - 1) * d
                    q_text = f"The first term of an AP is {a} and the common difference is {d}. Determine the {n}th term."
                    opts = {"A": f"{nth}", "B": f"{nth - d}", "C": f"{nth + d}", "D": f"{a * d * n}"}
                    items.append((
                        "Arithmetic Progressions", q_text, opts, "A",
                        f"T_n = a + (n - 1)d = {a} + ({n} - 1)({d}) = {nth}.",
                        "Use the n-th term formula: T_n = a + (n - 1)d."
                    ))
        # 4. Geometric Progressions (GP)
        for a in [2, 3, 4, 5]:
            for r in [2, 3]:
                for n in [4, 5, 6]:
                    nth_gp = a * (r ** (n - 1))
                    q_text = f"In a Geometric Progression (GP), the first term is {a} and the common ratio is {r}. Calculate the {n}th term."
                    opts = {"A": f"{nth_gp}", "B": f"{nth_gp * r}", "C": f"{a + (n-1)*r}", "D": f"{nth_gp // r}"}
                    items.append((
                        "Geometric Progressions", q_text, opts, "A",
                        f"T_n = a·r^(n - 1) = {a} × {r}^{n-1} = {nth_gp}.",
                        "Recall T_n = a·r^(n-1) for a geometric progression."
                    ))
        # 5. Sum to infinity of GP
        for a in [6, 9, 12, 18, 24]:
            for r_denom in [2, 3, 4]:
                r = 1 / r_denom
                s_inf = a / (1 - r)
                s_str = f"{int(s_inf)}" if s_inf.is_integer() else f"{s_inf:.1f}"
                q_text = f"Find the sum to infinity of a GP with first term {a} and common ratio 1/{r_denom}."
                opts = {"A": s_str, "B": f"{a * r_denom}", "C": f"{a + r_denom}", "D": f"{a / r_denom:.1f}"}
                items.append((
                    "Sum to Infinity", q_text, opts, "A",
                    f"S_∞ = a / (1 - r) = {a} / (1 - 1/{r_denom}) = {a} / ({(r_denom-1)}/{r_denom}) = {s_str}.",
                    "Use S_∞ = a / (1 - r) when |r| < 1."
                ))
        # 6. Logarithms
        for base in [2, 3, 5, 10]:
            for p in [2, 3, 4]:
                val = base ** p
                q_text = f"Solve for x: log_{base}(x) = {p}."
                opts = {"A": f"{val}", "B": f"{base * p}", "C": f"{base + p}", "D": f"{p ** base}"}
                items.append((
                    "Logarithmic Equations", q_text, opts, "A",
                    f"By definition of logarithms, log_b(x) = y means x = b^y = {base}^{p} = {val}.",
                    "Convert logarithmic equation log_b(x) = y into its exponential form x = b^y."
                ))
        # 7. Matrices: 2x2 Determinant
        for a, b, c, d in [(2, 3, 1, 4), (5, 2, 3, 1), (4, -2, 1, 3), (3, 5, 2, 4), (6, 1, 2, 3), (1, 4, 2, 9), (7, 3, 2, 1)]:
            det = a * d - b * c
            q_text = f"Evaluate the determinant of the 2×2 matrix: |[{a}, {b}], [{c}, {d}]|."
            opts = {"A": f"{det}", "B": f"{a*d + b*c}", "C": f"{a+d - (b+c)}", "D": f"{det + 2}"}
            items.append((
                "Matrix Determinants", q_text, opts, "A",
                f"det(A) = ad - bc = ({a} × {d}) - ({b} × {c}) = {a*d} - {b*c} = {det}.",
                "Multiply diagonal elements (ad) and subtract off-diagonal elements (bc)."
            ))
        # 8. Polynomial Remainder Theorem
        for k in [1, 2, 3]:
            for p1, p2, p3 in [(2, -3, 4), (1, 4, -5), (3, -2, 1), (1, -5, 6)]:
                rem = p1 * (k**2) + p2 * k + p3
                q_text = f"Find the remainder when f(x) = {p1}x² + ({p2})x + ({p3}) is divided by (x - {k})."
                opts = {"A": f"{rem}", "B": f"{rem + 3}", "C": f"{-rem}", "D": f"{rem - 2}"}
                items.append((
                    "Remainder Theorem", q_text, opts, "A",
                    f"By the Remainder Theorem, R = f({k}) = {p1}({k}²) + ({p2})({k}) + {p3} = {rem}.",
                    "Evaluate f(k) where divisor is (x - k)."
                ))
        # 9. Variations
        for k_val in [2, 3, 4, 5]:
            for x1, x2 in [(3, 6), (2, 8), (4, 12), (5, 15)]:
                y1 = k_val * x1
                y2 = k_val * x2
                q_text = f"If y varies directly as x, and y = {y1} when x = {x1}, find y when x = {x2}."
                opts = {"A": f"{y2}", "B": f"{y1 * x2}", "C": f"{x2 // x1}", "D": f"{y2 + 4}"}
                items.append((
                    "Direct Variation", q_text, opts, "A",
                    f"y = kx => k = y/x = {y1}/{x1} = {k_val}. When x = {x2}, y = {k_val} × {x2} = {y2}.",
                    "First solve for constant of proportionality k = y/x."
                ))

    elif topic == "Calculus":
        # 1. Polynomial differentiation
        for c in range(2, 12):
            for p in range(2, 6):
                deriv_c = c * p
                deriv_p = p - 1
                q_text = f"Find dy/dx for y = {c}x^{p} - {c*2}x + 9."
                ans = f"{deriv_c}x^{deriv_p} - {c*2}"
                opts = {"A": ans, "B": f"{deriv_c}x^{p} - {c*2}", "C": f"{c}x^{deriv_p}", "D": f"{deriv_c}x^{deriv_p}"}
                items.append((
                    "Polynomial Differentiation", q_text, opts, "A",
                    f"d/dx(ax^n) = n·ax^(n-1). d/dx({c}x^{p} - {c*2}x + 9) = {deriv_c}x^{deriv_p} - {c*2}.",
                    "Apply power rule to each term independently."
                ))
        # 2. Definite integrals
        for a in [2, 4, 6]:
            for k in [1, 3, 5]:
                for lim in [1, 2, 3]:
                    ans_int = (a // 2) * (lim ** 2) + k * lim
                    q_text = f"Evaluate the definite integral: ∫ [0 to {lim}] ({a}x + {k}) dx."
                    opts = {"A": f"{ans_int}", "B": f"{ans_int + 2}", "C": f"{ans_int * 2}", "D": f"{a + k}"}
                    items.append((
                        "Definite Integration", q_text, opts, "A",
                        f"∫ ({a}x + {k}) dx = {a//2}x² + {k}x. Between 0 and {lim}: {a//2}({lim}²) + {k}({lim}) = {ans_int}.",
                        "Integrate term by term, then evaluate F(upper) - F(lower)."
                    ))
        # 3. Turning points / extrema
        for m in [1, 2, 3, 4, 5, 6]:
            q_text = f"Find the x-coordinate of the minimum point of the curve y = x² - {2*m}x + {m**2 + 5}."
            opts = {"A": f"{m}", "B": f"{-m}", "C": f"{2*m}", "D": f"{m*2 + 1}"}
            items.append((
                "Stationary Points", q_text, opts, "A",
                f"dy/dx = 2x - {2*m} = 0 => 2x = {2*m} => x = {m}. Since d²y/dx² = 2 > 0, it is a local minimum.",
                "Set first derivative to 0 to locate the stationary point."
            ))
        # 4. Tangents and gradients
        for k in [2, 3, 4, 5]:
            for x0 in [1, 2]:
                grad = 3 * k * (x0 ** 2)
                q_text = f"Find the gradient of the curve y = {k}x³ at the point x = {x0}."
                opts = {"A": f"{grad}", "B": f"{k * (x0**3)}", "C": f"{grad + 2}", "D": f"{k * 3}"}
                items.append((
                    "Tangents & Gradients", q_text, opts, "A",
                    f"dy/dx = 3({k})x² = {3*k}x². At x = {x0}, m = {3*k}({x0}²) = {grad}.",
                    "Evaluate dy/dx at the specific value of x."
                ))
        # 5. Trigonometric differentiation
        trig_rules = [
            ("sin(2x)", "2cos(2x)", "cos(2x)", "-2cos(2x)", "2sin(2x)"),
            ("cos(3x)", "-3sin(3x)", "3sin(3x)", "-sin(3x)", "3cos(3x)"),
            ("sin(4x)", "4cos(4x)", "-4cos(4x)", "cos(4x)", "4sin(4x)"),
            ("cos(5x)", "-5sin(5x)", "5cos(5x)", "-sin(5x)", "5sin(5x)"),
            ("tan(x)", "sec²(x)", "-sec²(x)", "cosec²(x)", "cos²(x)"),
            ("e^(2x)", "2e^(2x)", "e^(2x)", "2xe^(2x)", "e^(x)"),
            ("ln(3x)", "1/x", "3/x", "1/(3x)", "ln(3)"),
            ("e^(4x)", "4e^(4x)", "e^(4x)", "4xe^(4x)", "16e^(4x)"),
            ("sin(5x)", "5cos(5x)", "-5cos(5x)", "cos(5x)", "5sin(5x)"),
            ("cos(2x)", "-2sin(2x)", "2sin(2x)", "-sin(2x)", "-2cos(2x)")
        ]
        for expr, ans, d1, d2, d3 in trig_rules:
            q_text = f"Find the derivative with respect to x of y = {expr}."
            opts = {"A": ans, "B": d1, "C": d2, "D": d3}
            items.append((
                "Trigonometric & Exponential Calculus", q_text, opts, "A",
                f"Applying chain rule to {expr} yields {ans}.",
                "Remember chain rule: multiply derivative of the inner function."
            ))

    elif topic == "Geometry & Trigonometry":
        # 1. Circle Theorems: Subtended angles
        for ang in range(20, 85, 5):
            opts = {"A": f"{ang*2}°", "B": f"{ang}°", "C": f"{180 - ang}°", "D": f"{ang//2}°"}
            items.append((
                "Circle Theorems", f"An arc subtends an angle of {ang}° at the circumference of a circle. What angle does it subtend at the center?", opts, "A",
                f"Angle at center is twice the angle at circumference: 2 × {ang}° = {ang*2}°.",
                "Is the angle at the center double the angle at the circumference?"
            ))
        # 2. Cyclic Quadrilaterals
        for ang in range(60, 130, 5):
            supp = 180 - ang
            opts = {"A": f"{supp}°", "B": f"{ang}°", "C": f"{360 - ang}°", "D": "90°"}
            items.append((
                "Cyclic Quadrilateral", f"In a cyclic quadrilateral ABCD, angle B = {ang}°. What is the measure of opposite angle D?", opts, "A",
                f"Opposite angles of a cyclic quadrilateral sum to 180°: 180° - {ang}° = {supp}°.",
                "Remember opposite angles in a cyclic quadrilateral are supplementary."
            ))
        # 3. Coordinate distance
        for x1, y1, dx, dy in [(1, 2, 3, 4), (0, 0, 6, 8), (2, 3, 5, 12), (3, 1, 8, 15), (-1, -2, 3, 4), (2, -1, 6, 8)]:
            x2, y2 = x1 + dx, y1 + dy
            dist = int(math.hypot(dx, dy))
            q_text = f"Calculate the distance between points P({x1}, {y1}) and Q({x2}, {y2})."
            opts = {"A": f"{dist} units", "B": f"{dx + dy} units", "C": f"{dist + 2} units", "D": f"{dist - 1} units"}
            items.append((
                "Coordinate Distance", q_text, opts, "A",
                f"d = √[(x₂-x₁)² + (y₂-y₁)²] = √[{dx}² + {dy}²] = {dist}.",
                "Use distance formula: d = √[(Δx)² + (Δy)²]."
            ))
        # 4. Midpoint of line segment
        for x1, y1, x2, y2 in [(2, 4, 6, 8), (1, 3, 5, 7), (-2, 4, 4, 8), (3, -1, 7, 5), (0, 6, 4, 10), (8, 2, 2, 6)]:
            mx, my = (x1 + x2) // 2, (y1 + y2) // 2
            q_text = f"Find the coordinates of the midpoint of the line segment connecting A({x1}, {y1}) and B({x2}, {y2})."
            opts = {"A": f"({mx}, {my})", "B": f"({mx+1}, {my})", "C": f"({x2-x1}, {y2-y1})", "D": f"({my}, {mx})"}
            items.append((
                "Midpoint Formula", q_text, opts, "A",
                f"Midpoint = ((x₁+x₂)/2, (y₁+y₂)/2) = (({x1}+{x2})/2, ({y1}+{y2})/2) = ({mx}, {my}).",
                "Average the x-coordinates and y-coordinates independently."
            ))
        # 5. Perpendicular gradients
        for m in [2, 3, 4, 5, -2, -3, -4]:
            perp = f"-1/{m}" if m > 0 else f"1/{abs(m)}"
            q_text = f"A straight line L₁ has gradient m = {m}. Find the gradient of line L₂ perpendicular to L₁."
            opts = {"A": perp, "B": f"{m}", "C": f"{-m}", "D": f"1/{m}"}
            items.append((
                "Perpendicular Lines", q_text, opts, "A",
                f"For perpendicular lines, m₁ × m₂ = -1 => m₂ = -1/m₁ = {perp}.",
                "Negative reciprocal of slope m is -1/m."
            ))
        # 6. Trigonometric ratios and identities
        for angle, s_val, c_val, t_val in [
            (30, "1/2", "√3/2", "1/√3"),
            (45, "1/√2", "1/√2", "1"),
            (60, "√3/2", "1/2", "√3")
        ]:
            items.append((
                "Special Angles", f"What is the exact value of sin({angle}°)?",
                {"A": s_val, "B": c_val, "C": t_val, "D": "2"}, "A",
                f"From standard 30-60-90 or 45-45-90 triangles, sin({angle}°) = {s_val}.",
                f"Recall exact ratios for special angle {angle}°."
            ))
            items.append((
                "Special Angles", f"What is the exact value of cos({angle}°)?",
                {"A": c_val, "B": s_val, "C": t_val, "D": "0"}, "A",
                f"From standard triangles, cos({angle}°) = {c_val}.",
                f"Recall exact cosine for {angle}°."
            ))
        # 7. Bearings
        for b in [35, 60, 110, 145, 215, 250, 310, 340]:
            back = (b + 180) % 360
            b_str = f"{b:03d}°"
            back_str = f"{back:03d}°"
            q_text = f"The three-figure bearing of point Y from point X is {b_str}. What is the back bearing of X from Y?"
            opts = {"A": back_str, "B": f"{(b + 90)%360:03d}°", "C": f"{b_str}", "D": f"{(b + 270)%360:03d}°"}
            items.append((
                "Bearings & Vectors", q_text, opts, "A",
                f"Back bearing = forward bearing ± 180° = {b}° + 180° = {back_str}.",
                "Add 180° if bearing < 180°, subtract 180° if bearing > 180°."
            ))

    elif topic == "Statistics & Probability":
        # 1. Probability with replacement and without replacement
        for w in [3, 4, 5, 6]:
            for r in [2, 3, 4]:
                tot = w + r
                num = w * (w - 1)
                den = tot * (tot - 1)
                g = math.gcd(num, den)
                ans = f"{num//g}/{den//g}"
                q_text = f"A box contains {w} white balls and {r} red balls. If two balls are drawn at random without replacement, find the probability that both are white."
                opts = {"A": ans, "B": f"{(w/tot)**2:.2f}", "C": f"{w}/{tot}", "D": f"{r}/{tot}"}
                items.append((
                    "Probability Without Replacement", q_text, opts, "A",
                    f"P(W₁) = {w}/{tot}, P(W₂|W₁) = {w-1}/{tot-1}. P(Both) = ({w}/{tot}) × ({w-1}/{tot-1}) = {ans}.",
                    "Remember that without replacement, denominator reduces by 1."
                ))
        # 2. Combinations
        for n in [5, 6, 7, 8, 9, 10]:
            for r in [2, 3]:
                c_ans = math.comb(n, r)
                q_text = f"In how many ways can a committee of {r} members be chosen from a group of {n} people?"
                opts = {"A": f"{c_ans}", "B": f"{math.perm(n, r)}", "C": f"{c_ans * 2}", "D": f"{n * r}"}
                items.append((
                    "Combinations", q_text, opts, "A",
                    f"nCr = n! / (r!(n-r)!) = {n}C{r} = {c_ans}.",
                    "Order does not matter in committee selection: use combinations nCr."
                ))
        # 3. Permutations
        for n in [4, 5, 6, 7]:
            for r in [2, 3]:
                p_ans = math.perm(n, r)
                q_text = f"In how many ways can {r} distinct prizes (1st, 2nd...) be awarded to {n} competing students?"
                opts = {"A": f"{p_ans}", "B": f"{math.comb(n, r)}", "C": f"{n ** r}", "D": f"{p_ans // 2}"}
                items.append((
                    "Permutations", q_text, opts, "A",
                    f"nP{r} = n! / (n-r)! = {n}! / ({n-r})! = {p_ans}.",
                    "Since prizes are ranked, order matters: use permutations nPr."
                ))
        # 4. Mean and Median of grouped/ungrouped sets
        for start in range(1, 15):
            nums = [start, start + 2, start + 4, start + 6, start + 8]
            mean = sum(nums) / len(nums)
            q_text = f"Calculate the arithmetic mean of the numbers: {', '.join(map(str, nums))}."
            opts = {"A": f"{mean:.1f}", "B": f"{mean + 2:.1f}", "C": f"{mean - 1:.1f}", "D": f"{nums[-1]:.1f}"}
            items.append((
                "Arithmetic Mean", q_text, opts, "A",
                f"Mean = Σx / N = ({' + '.join(map(str, nums))}) / 5 = {sum(nums)} / 5 = {mean:.1f}.",
                "Sum all numbers and divide by count N = 5."
            ))
        # 5. Variance and Standard Deviation
        for d in [1, 2, 3, 4]:
            nums = [10 - d, 10, 10 + d]
            var = ((-d)**2 + 0 + d**2) / 3
            sd = math.sqrt(var)
            q_text = f"Find the variance of the dataset {{{10-d}, 10, {10+d}}}."
            opts = {"A": f"{var:.2f}", "B": f"{sd:.2f}", "C": f"{var * 2:.2f}", "D": f"{d}"}
            items.append((
                "Measures of Dispersion", q_text, opts, "A",
                f"Mean = 10. Deviations are {-d}, 0, {d}. Variance = [({-d})² + 0² + {d}²] / 3 = {2*(d**2)}/3 = {var:.2f}.",
                "Variance is the average of squared deviations from the mean."
            ))

    append_extra_math(items, topic)
    return items

def append_extra_math(items, topic):
    if topic == "Calculus":
        # Second derivatives
        for a in [2, 3, 4, 5, 6]:
            for p in [3, 4, 5]:
                # y = a x^p => y' = a*p x^(p-1) => y'' = a*p*(p-1) x^(p-2)
                c2 = a * p * (p - 1)
                p2 = p - 2
                q_text = f"Find the second derivative d²y/dx² of y = {a}x^{p} - 7x² + 4."
                ans = f"{c2}x^{p2} - 14" if p2 > 0 else f"{c2} - 14"
                opts = {"A": ans, "B": f"{a*p}x^{p-1} - 14x", "C": f"{c2}x^{p-1}", "D": f"{a}x^{p-2}"}
                items.append((
                    "Higher Order Derivatives", q_text, opts, "A",
                    f"First derivative dy/dx = {a*p}x^{p-1} - 14x. Differentiating again gives d²y/dx² = {c2}x^{p2} - 14.",
                    "Differentiate twice consecutively using the power rule."
                ))
        # More definite integrals
        for a in [1, 2, 3]:
            for b in [1, 2, 3]:
                for lim in [1, 2, 3, 4]:
                    val = a * (lim**3) // 3 + b * lim
                    q_text = f"Compute the definite integral: ∫ [0 to {lim}] ({a}x² + {b}) dx."
                    opts = {"A": f"{val}", "B": f"{val + 2}", "C": f"{val * 2}", "D": f"{val - 1}"}
                    items.append((
                        "Definite Integration of Polynomials", q_text, opts, "A",
                        f"Antiderivative is ({a}/3)x³ + {b}x. Evaluated from 0 to {lim} gives {val}.",
                        "Apply fundamental theorem of calculus: F(b) - F(a)."
                    ))
    elif topic == "Geometry & Trigonometry":
        # Interior and exterior angles of polygons
        for n in [5, 6, 7, 8, 9, 10, 12, 15]:
            int_ang = ((n - 2) * 180) / n
            ext_ang = 360 / n
            items.append((
                "Polygon Angles", f"Calculate the interior angle of a regular polygon with {n} sides.",
                {"A": f"{int_ang:.1f}°", "B": f"{ext_ang:.1f}°", "C": f"{180 - ext_ang/2:.1f}°", "D": f"{n * 10}°"}, "A",
                f"Interior angle = (n - 2) × 180° / n = ({n} - 2) × 180° / {n} = {int_ang:.1f}°.",
                "Use formula ((n - 2) × 180) / n."
            ))
            items.append((
                "Polygon Angles", f"What is the size of each exterior angle of a regular polygon with {n} sides?",
                {"A": f"{ext_ang:.1f}°", "B": f"{int_ang:.1f}°", "C": f"{ext_ang * 2:.1f}°", "D": f"{360 - ext_ang:.1f}°"}, "A",
                f"Exterior angle of regular polygon = 360° / n = 360° / {n} = {ext_ang:.1f}°.",
                "Exterior angles of any convex polygon sum to 360°."
            ))
        # Cosine rule
        for b in [3, 4, 5, 6]:
            for c in [4, 5, 6, 7]:
                # A = 60°, cos 60° = 0.5. a² = b² + c² - 2bc(0.5) = b² + c² - bc
                a_sq = b**2 + c**2 - b * c
                q_text = f"In triangle ABC, side b = {b} cm, side c = {c} cm, and angle A = 60°. Calculate a²."
                opts = {"A": f"{a_sq}", "B": f"{b**2 + c**2}", "C": f"{a_sq + b*c}", "D": f"{b*c*2}"}
                items.append((
                    "Cosine Rule", q_text, opts, "A",
                    f"a² = b² + c² - 2bc·cos(60°) = {b**2} + {c**2} - 2({b})({c})(0.5) = {b**2 + c**2} - {b*c} = {a_sq}.",
                    "Recall cosine rule: a² = b² + c² - 2bc cos(A)."
                ))
    elif topic == "Statistics & Probability":
        # Sum of two dice
        dice_sums = {
            2: ("1/36", "2/36", "1/18", "1/12"),
            3: ("2/36", "1/36", "3/36", "1/12"),
            4: ("3/36", "4/36", "2/36", "1/6"),
            5: ("4/36", "5/36", "3/36", "1/6"),
            6: ("5/36", "6/36", "4/36", "1/4"),
            7: ("6/36", "5/36", "1/12", "1/4"),
            8: ("5/36", "4/36", "6/36", "1/6"),
            9: ("4/36", "3/36", "5/36", "1/9"),
            10: ("3/36", "2/36", "4/36", "1/12"),
            11: ("2/36", "1/36", "3/36", "1/18"),
            12: ("1/36", "2/36", "1/12", "1/6")
        }
        for s, (p_cor, d1, d2, d3) in dice_sums.items():
            q_text = f"Two fair six-sided dice are thrown simultaneously. What is the probability of obtaining a total score of {s}?"
            opts = {"A": p_cor, "B": d1, "C": d2, "D": d3}
            items.append((
                "Dice Probability", q_text, opts, "A",
                f"There are 36 equally likely outcomes in a double dice throw. Favorable outcomes for sum {s} give probability {p_cor}.",
                "Count the pairs (x, y) such that x + y = target score."
            ))
        # Coin tosses
        for n_tosses in [3, 4, 5]:
            total_outcomes = 2 ** n_tosses
            for h in range(1, n_tosses):
                fav = math.comb(n_tosses, h)
                g = math.gcd(fav, total_outcomes)
                ans = f"{fav//g}/{total_outcomes//g}"
                q_text = f"A fair coin is tossed {n_tosses} times. What is the probability of obtaining exactly {h} heads?"
                opts = {"A": ans, "B": f"{h}/{total_outcomes}", "C": f"1/{total_outcomes}", "D": f"1/{h}"}
                items.append((
                    "Binomial Coin Toss", q_text, opts, "A",
                    f"P(X = {h}) = ({n_tosses}C{h}) / 2^{n_tosses} = {fav} / {total_outcomes} = {ans}.",
                    "Use binomial probability formula nCr × (1/2)^n."
                ))
