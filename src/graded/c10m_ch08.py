"""Class 10 Maths Ch 8 - Introduction to Trigonometry (graded banks)."""
from mg import *

SLUG, NAME, CHNO = "Introduction_to_Trigonometry", "Introduction to Trigonometry", 8

TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (6, 8, 10), (9, 12, 15), (12, 16, 20), (12, 35, 37)]
def fr(p, q): return t(F(p, q))
def RATIOS(a, b, c):
    """right-angled at B, AB=a (base), BC=b (perp), AC=c: ratios for angle A"""
    return Q(f"In $\\triangle ABC$, right-angled at $B$, $AB={a}$ cm and $BC={b}$ cm. Find $\\sin A$, $\\cos A$ and $\\tan A$.", f"$AC=\\sqrt{{{a}^2+{b}^2}}={c}$ cm (1); $\\sin A=\\frac{{BC}}{{AC}}={fr(b,c)}$ (1); $\\cos A=\\frac{{AB}}{{AC}}={fr(a,c)}$ (1); $\\tan A=\\frac{{BC}}{{AB}}={fr(b,a)}$ (1).", "1+1+1+1") if False else \
        Q(f"In $\\triangle ABC$, right-angled at $B$, $AB={a}$ cm and $BC={b}$ cm. Find $\\sin A$, $\\cos A$ and $\\tan A$.", f"$AC=\\sqrt{{{a}^2+{b}^2}}={c}$ cm (1); $\\sin A=\\frac{{BC}}{{AC}}={fr(b,c)}$, $\\cos A=\\frac{{AB}}{{AC}}={fr(a,c)}$ (1); $\\tan A=\\frac{{BC}}{{AB}}={fr(b,a)}$ (1).", "1+1+1")
def GIVEN(p, q, c):
    return Q(f"If $\\tan\\theta=\\dfrac{{{p}}}{{{q}}}$, find $\\sin\\theta$, $\\cos\\theta$ and $\\sec\\theta$.", f"Hypotenuse $=\\sqrt{{{p}^2+{q}^2}}={c}$ (1); $\\sin\\theta={fr(p,c)}$, $\\cos\\theta={fr(q,c)}$ (1); $\\sec\\theta={fr(c,q)}$ (1).", "1+1+1")
def GSIN(p, c, q):
    return Q(f"If $\\sin A=\\dfrac{{{p}}}{{{c}}}$, find $\\cos A$ and $\\tan A$.", f"Base $=\\sqrt{{{c}^2-{p}^2}}={q}$ (1); $\\cos A={fr(q,c)}$ (1); $\\tan A={fr(p,q)}$ (1).", "1+1+1")
def EVAL(p, q, c, a, b, d, e):
    # (a sin + b cos)/(d sin - e cos) with tan = p/q  -> (a p + b q)/(d p - e q)
    val = F(a * p + b * q, d * p - e * q)
    return Q(f"If $\\tan A=\\dfrac{{{p}}}{{{q}}}$, evaluate $\\dfrac{{{a}\\sin A{sg(b)}\\cos A}}{{{d}\\sin A{sg(-e)}\\cos A}}$.", f"Divide numerator and denominator by $\\cos A$ (1): $\\dfrac{{{a}\\tan A{sg(b)}}}{{{d}\\tan A{sg(-e)}}}$ (1); $=\\dfrac{{{a}({fr(p,q)}){sg(b)}}}{{{d}({fr(p,q)}){sg(-e)}}}={t(val)}$ (2); verified with $\\sin A={fr(p,c)}$, $\\cos A={fr(q,c)}$ (1).", "1+1+2+1")
S = {"sin": {0: F(0), 30: F(1, 2), 90: F(1)}, "cos": {0: F(1), 60: F(1, 2), 90: F(0)}, "tan": {0: F(0), 45: F(1)}}
S2 = {"sin": {0: F(0), 30: F(1, 4), 45: F(1, 2), 60: F(3, 4), 90: F(1)}, "cos": {0: F(1), 30: F(3, 4), 45: F(1, 2), 60: F(1, 4), 90: F(0)}, "tan": {0: F(0), 30: F(1, 3), 45: F(1), 60: F(3)}}
def SQV(terms):
    """terms: list of (coef, fn, deg) for squares"""
    val = sum(F(c) * S2[fn][d] for c, fn, d in terms)
    txt = "".join(("+" if c > 0 and i else ("-" if c < 0 else "")) + (str(abs(c)) if abs(c) != 1 else "") + f"\\{fn}^2{d}^\\circ" for i, (c, fn, d) in enumerate(terms))
    return txt, val
def EXPR(terms):
    txt, v = SQV(terms)
    return Q(f"Evaluate: ${txt}$.", "Use $" + ",\\ ".join(f"\\{fn}^2{d}^\\circ={t(S2[fn][d])}" for c, fn, d in terms) + f"$ (2); value $={t(v)}$ (1).", "2+1")
def EXPRM(terms):
    txt, v = SQV(terms)
    return MN(f"The value of ${txt}$ is:", v, why="Substitute the standard values")
def COMPL(a, b):
    return Q(f"Evaluate: $\\dfrac{{\\sin {a}^\\circ}}{{\\cos {90-a}^\\circ}}+\\dfrac{{\\tan {b}^\\circ}}{{\\cot {90-b}^\\circ}}$.", f"$\\cos{90-a}^\\circ=\\sin{a}^\\circ$ and $\\cot{90-b}^\\circ=\\tan{b}^\\circ$ (2); value $=1+1=2$ (1).", "2+1")
def ANG(fn, al, m, c):
    val = {("sin", 30): "\\frac12", ("sin", 60): "\\frac{\\sqrt3}{2}", ("cos", 30): "\\frac{\\sqrt3}{2}", ("cos", 60): "\\frac12", ("tan", 30): "\\frac{1}{\\sqrt3}", ("tan", 45): "1", ("tan", 60): "\\sqrt3", ("sin", 45): "\\frac{1}{\\sqrt2}", ("cos", 45): "\\frac{1}{\\sqrt2}"}[(fn, al)]
    x = F(al - c, m)
    arg = (f"{m}x" if m != 1 else "x") + (f"{sg(c)}^\\circ" if c else "^\\circ")
    return Q(f"If $\\{fn}({arg})={val}$, find the value of $x$ (an acute angle).", f"${val}=\\{fn}{al}^\\circ$ (1); ${m}x{sg(c)}={al}$ (1); $x={t(x)}^\\circ$ (1).", "1+1+1")
PROOFS = {
 "a": ("\\dfrac{\\sin\\theta}{1+\\cos\\theta}+\\dfrac{1+\\cos\\theta}{\\sin\\theta}=2\\csc\\theta", "LHS $=\\dfrac{\\sin^2\\theta+(1+\\cos\\theta)^2}{\\sin\\theta(1+\\cos\\theta)}$ (1); $=\\dfrac{\\sin^2\\theta+1+2\\cos\\theta+\\cos^2\\theta}{\\sin\\theta(1+\\cos\\theta)}=\\dfrac{2+2\\cos\\theta}{\\sin\\theta(1+\\cos\\theta)}$ (2); $=\\dfrac{2}{\\sin\\theta}=2\\csc\\theta$ = RHS (2)."),
 "b": ("(\\csc\\theta-\\cot\\theta)^2=\\dfrac{1-\\cos\\theta}{1+\\cos\\theta}", "LHS $=\\left(\\dfrac{1-\\cos\\theta}{\\sin\\theta}\\right)^2$ (2); $=\\dfrac{(1-\\cos\\theta)^2}{1-\\cos^2\\theta}$ (1); $=\\dfrac{(1-\\cos\\theta)^2}{(1-\\cos\\theta)(1+\\cos\\theta)}=\\dfrac{1-\\cos\\theta}{1+\\cos\\theta}$ (2)."),
 "c": ("\\dfrac{\\tan\\theta}{1-\\cot\\theta}+\\dfrac{\\cot\\theta}{1-\\tan\\theta}=1+\\sec\\theta\\csc\\theta", "Write in $\\sin,\\cos$: LHS $=\\dfrac{\\sin^2\\theta}{\\cos\\theta(\\sin\\theta-\\cos\\theta)}+\\dfrac{\\cos^2\\theta}{\\sin\\theta(\\cos\\theta-\\sin\\theta)}$ (2); $=\\dfrac{\\sin^3\\theta-\\cos^3\\theta}{\\sin\\theta\\cos\\theta(\\sin\\theta-\\cos\\theta)}$ (1); $=\\dfrac{\\sin^2\\theta+\\sin\\theta\\cos\\theta+\\cos^2\\theta}{\\sin\\theta\\cos\\theta}=1+\\sec\\theta\\csc\\theta$ (2)."),
 "d": ("(\\sin\\theta+\\csc\\theta)^2+(\\cos\\theta+\\sec\\theta)^2=7+\\tan^2\\theta+\\cot^2\\theta", "Expand: $\\sin^2\\theta+2+\\csc^2\\theta+\\cos^2\\theta+2+\\sec^2\\theta$ (2); $=5+\\csc^2\\theta+\\sec^2\\theta$ (1); $=5+(1+\\cot^2\\theta)+(1+\\tan^2\\theta)=7+\\tan^2\\theta+\\cot^2\\theta$ (2)."),
 "e": ("(1+\\cot A-\\csc A)(1+\\tan A+\\sec A)=2", "In $\\sin,\\cos$: $\\left(\\dfrac{\\sin A+\\cos A-1}{\\sin A}\\right)\\left(\\dfrac{\\cos A+\\sin A+1}{\\cos A}\\right)$ (2); numerator $=(\\sin A+\\cos A)^2-1=2\\sin A\\cos A$ (2); so value $=2$ (1)."),
 "f": ("\\sec A(1-\\sin A)(\\sec A+\\tan A)=1", "$\\dfrac{1}{\\cos A}(1-\\sin A)\\cdot\\dfrac{1+\\sin A}{\\cos A}$ (2); $=\\dfrac{1-\\sin^2A}{\\cos^2A}$ (2); $=1$ (1)."),
 "g": ("(\\sec A-\\tan A)^2=\\dfrac{1-\\sin A}{1+\\sin A}", "LHS $=\\left(\\dfrac{1-\\sin A}{\\cos A}\\right)^2$ (2); $=\\dfrac{(1-\\sin A)^2}{1-\\sin^2A}$ (1); $=\\dfrac{1-\\sin A}{1+\\sin A}$ (2)."),
 "h": ("\\dfrac{\\cos A}{1+\\sin A}+\\dfrac{1+\\sin A}{\\cos A}=2\\sec A", "LHS $=\\dfrac{\\cos^2A+(1+\\sin A)^2}{\\cos A(1+\\sin A)}$ (2); $=\\dfrac{2+2\\sin A}{\\cos A(1+\\sin A)}$ (2); $=\\dfrac{2}{\\cos A}=2\\sec A$ (1)."),
 "i": ("\\dfrac{1+\\tan^2A}{1+\\cot^2A}=\\left(\\dfrac{1-\\tan A}{1-\\cot A}\\right)^2", "LHS $=\\dfrac{\\sec^2A}{\\csc^2A}=\\tan^2A$ (2); RHS: $1-\\cot A=\\dfrac{\\tan A-1}{\\tan A}$ so $\\dfrac{1-\\tan A}{1-\\cot A}=-\\tan A$ (2); square $=\\tan^2A$ (1)."),
 "j": ("\\sin^4\\theta-\\cos^4\\theta=2\\sin^2\\theta-1", "LHS $=(\\sin^2\\theta-\\cos^2\\theta)(\\sin^2\\theta+\\cos^2\\theta)$ (2); $=\\sin^2\\theta-\\cos^2\\theta$ (1); $=\\sin^2\\theta-(1-\\sin^2\\theta)=2\\sin^2\\theta-1$ (2)."),
 "k": ("\\dfrac{1+\\sec A}{\\sec A}=\\dfrac{\\sin^2A}{1-\\cos A}", "LHS $=\\dfrac{1+\\frac{1}{\\cos A}}{\\frac{1}{\\cos A}}=\\cos A+1$ (2); RHS $=\\dfrac{1-\\cos^2A}{1-\\cos A}$ (2); $=1+\\cos A$ (1)."),
 "l": ("\\sqrt{\\dfrac{1+\\sin\\theta}{1-\\sin\\theta}}=\\sec\\theta+\\tan\\theta", "LHS $=\\sqrt{\\dfrac{(1+\\sin\\theta)^2}{1-\\sin^2\\theta}}$ (2); $=\\dfrac{1+\\sin\\theta}{\\cos\\theta}$ (2); $=\\sec\\theta+\\tan\\theta$ (1)."),
 "m": ("(\\csc\\theta-\\sin\\theta)(\\sec\\theta-\\cos\\theta)(\\tan\\theta+\\cot\\theta)=1", "$\\csc\\theta-\\sin\\theta=\\dfrac{\\cos^2\\theta}{\\sin\\theta}$, $\\sec\\theta-\\cos\\theta=\\dfrac{\\sin^2\\theta}{\\cos\\theta}$ (2); $\\tan\\theta+\\cot\\theta=\\dfrac{1}{\\sin\\theta\\cos\\theta}$ (1); product $=\\sin\\theta\\cos\\theta\\cdot\\dfrac{1}{\\sin\\theta\\cos\\theta}=1$ (2)."),
 "n": ("\\dfrac{\\sin\\theta-2\\sin^3\\theta}{2\\cos^3\\theta-\\cos\\theta}=\\tan\\theta", "LHS $=\\dfrac{\\sin\\theta(1-2\\sin^2\\theta)}{\\cos\\theta(2\\cos^2\\theta-1)}$ (2); $1-2\\sin^2\\theta=2\\cos^2\\theta-1$ (2); so LHS $=\\tan\\theta$ (1)."),
 "o": ("\\tan^2A-\\sin^2A=\\tan^2A\\sin^2A", "LHS $=\\dfrac{\\sin^2A}{\\cos^2A}-\\sin^2A=\\sin^2A\\left(\\dfrac{1-\\cos^2A}{\\cos^2A}\\right)$ (3); $=\\sin^2A\\cdot\\dfrac{\\sin^2A}{\\cos^2A}=\\tan^2A\\sin^2A$ (2)."),
 "p": ("\\dfrac{\\sec\\theta+\\tan\\theta-1}{\\tan\\theta-\\sec\\theta+1}=\\dfrac{1+\\sin\\theta}{\\cos\\theta}", "Use $1=\\sec^2\\theta-\\tan^2\\theta$ in the numerator: $(\\sec\\theta+\\tan\\theta)-(\\sec\\theta-\\tan\\theta)(\\sec\\theta+\\tan\\theta)$ (2); $=(\\sec\\theta+\\tan\\theta)(1-\\sec\\theta+\\tan\\theta)$ (2); cancel with denominator: $\\sec\\theta+\\tan\\theta=\\dfrac{1+\\sin\\theta}{\\cos\\theta}$ (1)."),
 "q": ("\\dfrac{\\cos\\theta-\\sin\\theta+1}{\\cos\\theta+\\sin\\theta-1}=\\csc\\theta+\\cot\\theta", "Divide numerator and denominator by $\\sin\\theta$: $\\dfrac{\\cot\\theta-1+\\csc\\theta}{\\cot\\theta+1-\\csc\\theta}$ (2); use $1=\\csc^2\\theta-\\cot^2\\theta$ (1); numerator $=(\\csc\\theta+\\cot\\theta)(1-\\csc\\theta+\\cot\\theta)$ (1); cancel: $\\csc\\theta+\\cot\\theta$ (1)."),
 "r": ("\\cos^4A-\\sin^4A=2\\cos^2A-1", "LHS $=(\\cos^2A-\\sin^2A)(\\cos^2A+\\sin^2A)$ (2); $=\\cos^2A-\\sin^2A$ (1); $=\\cos^2A-(1-\\cos^2A)=2\\cos^2A-1$ (2)."),
}
def PR(k, marks="2+3"):
    st, pf = PROOFS[k]
    return Q(f"Prove that: ${st}$.", pf, "5")
SH = {  # 3-mark identities
 1: ("(1-\\cos^2\\theta)\\csc^2\\theta=1", "$(1-\\cos^2\\theta)=\\sin^2\\theta$ (1); $\\sin^2\\theta\\cdot\\csc^2\\theta$ (1) $=1$ (1)."),
 2: ("\\tan\\theta+\\cot\\theta=\\sec\\theta\\csc\\theta", "LHS $=\\dfrac{\\sin^2\\theta+\\cos^2\\theta}{\\sin\\theta\\cos\\theta}$ (2); $=\\dfrac{1}{\\sin\\theta\\cos\\theta}=\\sec\\theta\\csc\\theta$ (1)."),
 3: ("(\\sin\\theta+\\cos\\theta)^2+(\\sin\\theta-\\cos\\theta)^2=2", "Expand: $2\\sin^2\\theta+2\\cos^2\\theta$ (2); $=2$ (1)."),
 4: ("\\sec^2\\theta+\\csc^2\\theta=\\sec^2\\theta\\csc^2\\theta", "LHS $=\\dfrac{1}{\\cos^2\\theta}+\\dfrac{1}{\\sin^2\\theta}=\\dfrac{\\sin^2\\theta+\\cos^2\\theta}{\\sin^2\\theta\\cos^2\\theta}$ (2); $=\\sec^2\\theta\\csc^2\\theta$ (1)."),
 5: ("\\dfrac{1-\\tan^2A}{1+\\tan^2A}=\\cos^2A-\\sin^2A", "$1+\\tan^2A=\\sec^2A$ (1); LHS $=(1-\\tan^2A)\\cos^2A$ (1); $=\\cos^2A-\\sin^2A$ (1)."),
 6: ("(1+\\tan^2A)\\sin^2A=\\tan^2A", "$(1+\\tan^2A)=\\sec^2A$ (1); $\\sec^2A\\sin^2A=\\dfrac{\\sin^2A}{\\cos^2A}$ (1) $=\\tan^2A$ (1)."),
 7: ("\\sqrt{1-\\sin^2A}\\cdot\\sec A=1", "$\\sqrt{\\cos^2A}=\\cos A$ (1); $\\cos A\\cdot\\sec A$ (1) $=1$ (1)."),
 8: ("\\dfrac{\\sin A}{\\csc A}+\\dfrac{\\cos A}{\\sec A}=1", "$\\dfrac{\\sin A}{\\csc A}=\\sin^2A$, $\\dfrac{\\cos A}{\\sec A}=\\cos^2A$ (2); sum $=1$ (1)."),
 9: ("\\cos^2A(1+\\tan^2A)=1", "$1+\\tan^2A=\\sec^2A$ (1); $\\cos^2A\\sec^2A$ (1) $=1$ (1)."),
 10: ("\\sin^2A\\cot^2A+\\cos^2A\\tan^2A=1", "$\\sin^2A\\cdot\\dfrac{\\cos^2A}{\\sin^2A}=\\cos^2A$ (1); $\\cos^2A\\tan^2A=\\sin^2A$ (1); sum $=1$ (1)."),
 11: ("(\\csc A-\\cot A)(\\csc A+\\cot A)=1", "Use $(a-b)(a+b)=a^2-b^2$ (1); $\\csc^2A-\\cot^2A$ (1) $=1$ (1)."),
 12: ("\\dfrac{1}{1+\\tan^2A}+\\dfrac{1}{1+\\cot^2A}=1", "$\\dfrac{1}{\\sec^2A}+\\dfrac{1}{\\csc^2A}$ (1); $=\\cos^2A+\\sin^2A$ (1) $=1$ (1)."),
}
def SHQ(k): return Q(f"Prove that: ${SH[k][0]}$.", SH[k][1], "1+1+1" if k not in (2, 3, 4, 8) else "2+1")
def STRI(a, b, c, k):
    return Q(f"In $\\triangle PQR$, right-angled at $Q$, $PQ={a*k}$ cm and $QR={b*k}$ cm. Find $\\sin P$, $\\cos P$, $\\tan P$ and check that $\\sin^2P+\\cos^2P=1$.", f"$PR={c*k}$ cm (1); $\\sin P={fr(b,c)}$, $\\cos P={fr(a,c)}$, $\\tan P={fr(b,a)}$ (2); $\\left({fr(b,c)}\\right)^2+\\left({fr(a,c)}\\right)^2={t(F(b*b+a*a,c*c))}=1$ (2).", "1+2+2")

# ---------------- EASY ----------------
eA = [[MS(f"In a right triangle with perpendicular {b}, base {a} and hypotenuse {c}, $\\sin\\theta=$", fr(b, c), [fr(a, c), fr(b, a), fr(c, b)], "$\\sin\\theta=\\frac{\\text{perpendicular}}{\\text{hypotenuse}}$") for a, b, c in TR[:5]],
      [MS(f"In a right triangle with perpendicular {b}, base {a} and hypotenuse {c}, $\\tan\\theta=$", fr(b, a), [fr(a, b), fr(b, c), fr(a, c)], "$\\tan\\theta=\\frac{\\text{perpendicular}}{\\text{base}}$") for a, b, c in TR[:5]],
      [MS(f"The value of ${fn}{d}^\\circ$ is:", t(S[fn][d]), [x for x in ["0", "1", "\\frac12", "2"] if x != t(S[fn][d])], "Standard value") for fn, d in [("sin", 30), ("cos", 60), ("tan", 45), ("sin", 90), ("cos", 0), ("tan", 0)]],
      [MS(f"$\\sin^2\\theta+\\cos^2\\theta=$" if False else f"The value of $\\sin^2{a}^\\circ+\\cos^2{a}^\\circ$ is:", "1", ["0", "2", f"{a}"], "Identity") for a in [20, 35, 50, 65, 72]],
      [MS(f"$\\sin{a}^\\circ=\\cos$ of:", f"{90-a}^\\circ", [f"{a}^\\circ", f"{a+10}^\\circ", f"{180-a}^\\circ"], "$\\sin\\theta=\\cos(90^\\circ-\\theta)$") for a in [25, 40, 55, 15, 70]],
      [MS("$\\sec\\theta$ is the reciprocal of:", "$\\cos\\theta$", ["$\\sin\\theta$", "$\\tan\\theta$", "$\\cot\\theta$"], "$\\sec\\theta=1/\\cos\\theta$") for _ in range(1)] + [MS(f"If $\\sin A=\\frac{{{p}}}{{{c}}}$, then $\\csc A=$", fr(c, p), [fr(p, c), fr(c - 1, p), fr(p, c + 1)], "Reciprocal") for p, c in [(3, 5), (5, 13), (8, 17), (7, 25)]]]
eB = ([Q(f"In a right triangle the perpendicular is {b} and the hypotenuse is {c}. Find $\\sin\\theta$.", f"$\\sin\\theta=\\frac{{{b}}}{{{c}}}$ (1) $={fr(b,c)}$ (1).", "1+1") for a, b, c in TR[:4]]
      + [Q(f"Find the value of ${fn}{d}^\\circ+{fn2}{d2}^\\circ$.", f"${t(S[fn][d])}+{t(S[fn2][d2])}$ (1) $={t(S[fn][d]+S[fn2][d2])}$ (1).", "1+1") for fn, d, fn2, d2 in [("sin", 30, "cos", 60), ("tan", 45, "sin", 90), ("cos", 0, "sin", 30), ("cos", 60, "tan", 45)]]
      + [Q(f"Evaluate: $\\sin^2{a}^\\circ+\\cos^2{a}^\\circ$.", "Using $\\sin^2\\theta+\\cos^2\\theta=1$ (1); value $=1$ (1).", "1+1") for a in [25, 38, 47, 62]])
eC = ([RATIOS(a, b, c) for a, b, c in TR[:6]] + [GSIN(p, c, q) for q, p, c in TR[:6]] + [EXPR(terms) for terms in [[(1, "sin", 30), (1, "cos", 60)], [(1, "tan", 45), (1, "sin", 90)], [(1, "cos", 0), (1, "sin", 0)], [(2, "sin", 30), (1, "cos", 90)], [(1, "tan", 45), (-1, "sin", 30)], [(3, "sin", 90), (-1, "cos", 0)]]])
eD = ([GIVEN(p, q, c) for q, p, c in TR[:6]] + [STRI(a, b, c, k) for (a, b, c), k in zip(TR[:6], [2, 3, 2, 1, 3, 2])])

# ---------------- NCERT ----------------
nA = [[MS(f"If $\\tan A=\\frac{{{p}}}{{{q}}}$, then $\\sin A=$", fr(p, c), [fr(q, c), fr(c, p), fr(p, q)], "Hypotenuse is " + str(c)) for q, p, c in TR[:5]],
      [MS(f"If $\\cos A=\\frac{{{q}}}{{{c}}}$, then $\\tan A=$", fr(p, q), [fr(q, p), fr(p, c), fr(c, q)], "Find the perpendicular") for q, p, c in TR[1:6]],
      [EXPRM(tms) for tms in [[(1, "sin", 30), (1, "cos", 30)], [(1, "tan", 60), (-1, "sec", 0)] if False else [(1, "tan", 60), (-1, "tan", 30)], [(1, "sin", 45), (1, "cos", 45)], [(2, "tan", 45), (1, "cos", 60)], [(1, "sin", 60), (1, "cos", 60)]]],
      [MS(f"$\\tan{a}^\\circ\\cdot\\tan{90-a}^\\circ=$", "1", ["0", "2", f"{a}"], "$\\tan(90^\\circ-\\theta)=\\cot\\theta$") for a in [20, 35, 50, 65, 28]],
      [MS(f"The value of $\\sin{a}^\\circ/\\cos{90-a}^\\circ$ is:", "1", ["0", "2", f"{a}"], "$\\cos(90^\\circ-\\theta)=\\sin\\theta$") for a in [15, 22, 37, 48, 63]],
      [MS(f"$(1+\\tan^2\\theta)\\cos^2\\theta=$" if False else f"$({k}\\sin\\theta)^2+({k}\\cos\\theta)^2=$", str(k * k), [str(k), str(2 * k), "1"], "$k^2(\\sin^2+\\cos^2)$") for k in [2, 3, 4, 5, 6]],
      [MS(f"$\\sec^2\\theta-\\tan^2\\theta=$" if False else f"If $\\sec\\theta={fr(c,q)}$ then $\\cos\\theta=$", fr(q, c), [fr(c, q), fr(p, c), fr(p, q)], "Reciprocal") for q, p, c in TR[:3]]]
nB = ([Q(f"If $\\tan A=\\frac{{{p}}}{{{q}}}$, find $\\sec A$.", f"Hypotenuse $={c}$ (1); $\\sec A=\\frac{{{c}}}{{{q}}}$ (1).", "1+1") for q, p, c in TR[:4]] + [COMPL(a, b) for a, b in [(25, 40), (18, 35), (32, 50), (14, 61)]]
      + [Q(f"Evaluate: $\\dfrac{{\\tan{a}^\\circ}}{{\\cot{90-a}^\\circ}}$.", f"$\\cot{90-a}^\\circ=\\tan{a}^\\circ$ (1); value $=1$ (1).", "1+1") for a in [21, 33, 47, 58]])
nC = ([GIVEN(p, q, c) for q, p, c in TR[1:7]] + [RATIOS(a, b, c) for a, b, c in TR[3:9]] + [SHQ(k) for k in [1, 2, 3, 4, 5, 6]])
nD = ([PR(k) for k in "abcdef"] + [EVAL(p, q, c, a, b, d, e) for (q, p, c), (a, b, d, e) in zip(TR[:6], [(4, 3, 4, -3), (5, 2, 3, -2), (2, 3, 5, -1), (3, 1, 2, -1), (5, 4, 5, -2), (7, 2, 4, -1)])])

# ---------------- MEDIUM ----------------
mA = [[EXPRM(tms) for tms in [[(1, "sin", 30), (1, "sin", 45)], [(2, "sin", 60), (-1, "tan", 30)], [(1, "cos", 45), (1, "tan", 45)], [(3, "tan", 30), (1, "cos", 60)], [(4, "sin", 30), (-2, "cos", 45)]]],
      [MS(f"If $\\sin\\theta=\\frac{{{p}}}{{{c}}}$, then $\\sec\\theta+\\tan\\theta=$", fr(c + p, q), [fr(c + p, p), fr(c - p, q), fr(c, q)], "$\\frac{c}{q}+\\frac{p}{q}$") for q, p, c in TR[:5]],
      [MS(f"If $\\cos\\theta=\\frac{{{q}}}{{{c}}}$, then $\\csc\\theta-\\cot\\theta=$", fr(c - q, p), [fr(c + q, p), fr(c - p, q), fr(c, p)], "$\\frac{c}{p}-\\frac{q}{p}$") for q, p, c in TR[:5]],
      [MS(f"$\\dfrac{{\\sin{a}^\\circ}}{{\\cos{90-a}^\\circ}}+\\dfrac{{\\cos{b}^\\circ}}{{\\sin{90-b}^\\circ}}=$", "2", ["0", "1", "4"], "Each ratio is 1") for a, b in [(20, 30), (35, 40), (48, 55), (12, 66), (27, 58)]],
      [MS(f"If $\\tan\\theta={fr(p,q)}$, then $\\dfrac{{\\sin\\theta+\\cos\\theta}}{{\\cos\\theta}}=$", fr(p + q, q), [fr(p, q), fr(q, p + q), fr(p - q, q)], "Divide by $\\cos\\theta$") for q, p, c in TR[:5]],
      [MS(f"If $\\sin\\theta=\\cos\\theta$, then $\\tan\\theta=$" if False else f"If $\\sin{a}^\\circ=\\cos{b}^\\circ$ (acute angles), then $a+b=$", "$90^\\circ$", ["$45^\\circ$", "$180^\\circ$", "$60^\\circ$"], "Complementary") for a, b in [(20, 70), (35, 55), (48, 42), (12, 78), (27, 63)]]]
mB = ([EVAL(p, q, c, a, b, d, e) if False else Q(f"If $\\tan A=\\frac{{{p}}}{{{q}}}$, find $\\dfrac{{\\sin A+\\cos A}}{{\\sin A-\\cos A}}$.", f"Divide by $\\cos A$: $\\dfrac{{\\tan A+1}}{{\\tan A-1}}$ (1) $={t(F(p+q,p-q))}$ (1).", "1+1") for q, p, c in [(3, 4, 5), (5, 12, 13), (4, 5, 0) if False else (7, 24, 25), (12, 5, 13)] if p != q]
      + [ANG(*p) for p in [("sin", 30, 2, 0), ("tan", 60, 3, 0), ("cos", 60, 1, 30) if False else ("cos", 60, 2, 10), ("tan", 45, 5, 0)]]
      + [EXPR(tms) for tms in [[(1, "sin", 45), (1, "cos", 45)], [(2, "tan", 60), (-1, "sin", 30)], [(1, "sec", 0)] if False else [(1, "cos", 30), (1, "sin", 60)], [(3, "sin", 60), (-2, "cos", 30)]]])
mC = ([ANG(*p) for p in [("sin", 30, 2, 10) if False else ("sin", 30, 3, 0), ("tan", 60, 2, 0), ("cos", 30, 3, 0), ("tan", 30, 1, 0) if False else ("tan", 30, 2, 0), ("sin", 60, 3, 0), ("cos", 45, 5, 0)]]
      + [GIVEN(p, q, c) for q, p, c in TR[2:8]] + [SHQ(k) for k in [7, 8, 9, 10, 11, 12]])
mD = ([PR(k) for k in "ghijkl"] + [EVAL(p, q, c, a, b, d, e) for (q, p, c), (a, b, d, e) in zip(TR[2:8], [(3, 2, 4, -1), (2, 5, 3, -2), (5, 3, 1, -1), (4, 7, 2, -1), (6, 1, 3, -1), (1, 8, 2, -1)])])

# ---------------- HARD ----------------
hA = [[MS(f"If $\\sin\\theta+\\cos\\theta=\\sqrt2$ ... " if False else f"If $\\sin\\theta={fr(p,c)}$ then $\\sin^2\\theta+\\cos^2\\theta+\\tan^2\\theta=$", t(F(1) + F(p, q) ** 2), [t(F(p, q) ** 2), t(F(p, c) ** 2), t(F(q, c) ** 2)], "$1+\\tan^2\\theta$") for q, p, c in TR[:5]],
      [MS(f"If $\\tan\\theta={fr(p,q)}$, then $\\dfrac{{1-\\tan^2\\theta}}{{1+\\tan^2\\theta}}=$", t(F(q * q - p * p, q * q + p * p)), [t(F(p * p - q * q, q * q + p * p)), t(F(2 * p * q, q * q + p * p)), t(F(q, p))], "$\\cos^2\\theta-\\sin^2\\theta$") for q, p, c in TR[:5]],
      [MS(f"If $\\sin\\theta={fr(p,c)}$, then $\\dfrac{{2\\sin\\theta\\cos\\theta}}{{1}}$ equals:" if False else f"If $\\sin\\theta={fr(p,c)}$, the value of $2\\sin\\theta\\cos\\theta$ is:", t(F(2 * p * q, c * c)), [t(F(p * q, c * c)), t(F(2 * p, c)), t(F(2 * q, c))], "$2\\cdot\\frac pc\\cdot\\frac qc$") for q, p, c in TR[:5]],
      [MS(f"If $\\sec\\theta+\\tan\\theta={fr(c+p,q)}$, then $\\sec\\theta-\\tan\\theta=$", fr(q, c + p), [fr(c + p, q), fr(c - p, q), fr(q, c - p)], "$(\\sec+\\tan)(\\sec-\\tan)=1$") for q, p, c in TR[:5]],
      [MS(f"$\\dfrac{{\\sin^2{a}^\\circ+\\sin^2{90-a}^\\circ}}{{\\cos^2{b}^\\circ+\\cos^2{90-b}^\\circ}}=$", "1", ["0", "2", "$\\frac12$"], "Each pair sums to 1") for a, b in [(25, 35), (40, 12), (58, 20), (33, 71), (17, 44)]],
      [MS(f"If $x\\sin^2{a}^\\circ... $" if False else f"The value of $\\tan{a}^\\circ\\tan{b}^\\circ\\tan{90-b}^\\circ\\tan{90-a}^\\circ$ is:", "1", ["0", "2", "$\\tan 45^\\circ+1$"], "Pair as $\\tan\\theta\\tan(90^\\circ-\\theta)=1$") for a, b in [(10, 20), (15, 35), (25, 42), (33, 57), (18, 61)]]]
hB = ([Q(f"If $\\sin\\theta={fr(p,c)}$, find $\\dfrac{{1-\\tan^2\\theta}}{{1+\\tan^2\\theta}}$." if False else f"If $\\sin\\theta={fr(p,c)}$, find the value of $\\cos^2\\theta-\\sin^2\\theta$.", f"$\\cos^2\\theta=1-\\left({fr(p,c)}\\right)^2={t(F(q*q,c*c))}$ (1); value $={t(F(q*q-p*p,c*c))}$ (1).", "1+1") for q, p, c in TR[:4]]
      + [Q(f"If $\\cot\\theta={fr(q,p)}$, find $\\sin\\theta$ and $\\sec\\theta$.", f"Hypotenuse $={c}$ (1); $\\sin\\theta={fr(p,c)}$, $\\sec\\theta={fr(c,q)}$ (1).", "1+1") for q, p, c in TR[4:8]]
      + [Q(f"If $x=a\\sec\\theta$ and $y=b\\tan\\theta$ with $a={a}$, $b={b}$, express $\\dfrac{{x^2}}{{{a*a}}}-\\dfrac{{y^2}}{{{b*b}}}$.", f"$\\dfrac{{x^2}}{{{a*a}}}=\\sec^2\\theta$, $\\dfrac{{y^2}}{{{b*b}}}=\\tan^2\\theta$ (1); difference $=1$ (1).", "1+1") for a, b in [(2, 3), (3, 5), (4, 7), (5, 2)]])
hC = ([SHQ(k) for k in [2, 4, 5, 6, 8, 10]]
      + [Q(f"If $\\sin\\theta+\\cos\\theta=\\sqrt{{{m}}}$ then find $\\sin\\theta\\cos\\theta$." if False else f"If $\\sin\\theta+\\cos\\theta={t(F(a,b))}$, find $\\sin\\theta\\cos\\theta$.", f"Square both sides: $1+2\\sin\\theta\\cos\\theta={t(F(a*a,b*b))}$ (2); $\\sin\\theta\\cos\\theta={t(F(a*a-b*b,2*b*b))}$ (1).", "2+1") for a, b in [(7, 5), (13, 10), (17, 13), (5, 4), (9, 7), (11, 8)]]
      + [Q(f"If $\\tan\\theta+\\cot\\theta={a}$, find $\\tan^2\\theta+\\cot^2\\theta$.", f"Square: $\\tan^2\\theta+2+\\cot^2\\theta={a*a}$ (2); value $={a*a-2}$ (1).", "2+1") for a in [3, 4, 5, 6, 7, 8]])
hD = ([PR(k) for k in "mnopqr"] + [EVAL(p, q, c, a, b, d, e) for (q, p, c), (a, b, d, e) in zip(TR[3:9], [(5, 4, 7, -3), (3, 7, 2, -1), (4, 9, 6, -2), (2, 3, 8, -1), (7, 5, 3, -2), (6, 8, 1, -1)])])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
