"""Class 10 Maths Ch 8 - Introduction to Trigonometry: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import sqrt, isclose
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch08"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

s3 = sqrt(3)
assert 3**2 + 4**2 == 5**2 and 5**2 + 12**2 == 13**2 and 7**2 + 24**2 == 25**2 and 12**2 + 16**2 == 20**2
assert 10**2 + 24**2 == 26**2 and 8**2 + 15**2 == 17**2 and 5**2 + 12**2 == 13**2 and 20**2 + 21**2 == 29**2
assert isclose((43 - 24 * s3) / 11, (0.5 + 1 - 2 / s3) / (2 / s3 + 0.5 + 1))
assert isclose(1 / (2 + 2 - 1), 1 / 3) and isclose(2 * (1 / s3) / (1 + 1 / 3), s3 / 2)
assert 13 - 12 == 1 and 12**2 + 5**2 == 13**2 and 1.5**2 + 3.6**2 == 3.9**2 or isclose(1.5**2 + 3.6**2, 3.9**2)
assert isclose(3 / (s3 / 2), 2 * s3) and 9**2 + 12**2 == 15**2

WS = [
# ---------------- EASY ----------------
W(r"If $\sin A=\dfrac35$ and $A$ is acute, then $\cos A$ is:", 1, r"(b) $\dfrac45$. Perpendicular 3, hypotenuse 5, so base $=\sqrt{25-9}=4$ and $\cos A=\dfrac45$. (1)", "E", opts=[r"$\dfrac34$", r"$\dfrac45$", r"$\dfrac54$", r"$\dfrac53$"]),
W(r"The value of $\tan45^\circ+\sin30^\circ$ is:", 1, r"(c) $\dfrac32$. $1+\dfrac12=\dfrac32$. (1)", "E", opts=["1", r"$\dfrac12$", r"$\dfrac32$", "2"]),
W(r"The value of $\dfrac{\sin35^\circ}{\cos55^\circ}$ is:", 1, r"(b) 1. $\cos55^\circ=\cos(90^\circ-35^\circ)=\sin35^\circ$, so the ratio is 1. (1)", "E", opts=["0", "1", r"$\dfrac{35}{55}$", r"$\dfrac{7}{11}$"]),
W(r"Which of the following is NOT defined?", 1, r"(c) $\tan90^\circ$. $\tan90^\circ=\dfrac{\sin90^\circ}{\cos90^\circ}=\dfrac10$. (1)", "E", opts=[r"$\sin90^\circ$", r"$\cos0^\circ$", r"$\tan90^\circ$", r"$\cot90^\circ$"]),
W(r"The value of $\sec^2\theta-\tan^2\theta$ is:", 1, r"(b) 1. This is the identity $1+\tan^2\theta=\sec^2\theta$. (1)", "E", opts=["0", "1", "−1", r"$\sec\theta$"]),
W(r"If $\tan\theta=\dfrac1{\sqrt3}$ and $\theta$ is acute, then $\theta$ is:", 1, r"(a) $30^\circ$. $\tan30^\circ=\dfrac1{\sqrt3}$. (1)", "E", opts=[r"$30^\circ$", r"$45^\circ$", r"$60^\circ$", r"$90^\circ$"]),
W(r"Which of these can be the value of $\cos A$ for an acute angle $A$?", 1, r"(c) $\dfrac35$. The hypotenuse is the longest side, so $\cos A=\dfrac{\text{base}}{\text{hypotenuse}}$ cannot exceed 1; the other three values are greater than 1. (1)", "E", opts=[r"$\dfrac54$", "2", r"$\dfrac35$", r"$\dfrac75$"]),
W(r"In $\triangle ABC$, right-angled at $B$, $AB=3$ cm and $BC=4$ cm. Find $\sin A$, $\cos A$ and $\tan A$.", 2, r"$AC=\sqrt{9+16}=5$ cm (½). With respect to $A$: perpendicular $BC=4$, base $AB=3$. $\sin A=\dfrac45$, $\cos A=\dfrac35$, $\tan A=\dfrac43$. (½+½+½+½)", "E"),
W(r"A 13 m ladder leans against a wall with its foot 5 m from the wall. Find the sine and cosine of the angle the ladder makes with the ground.", 2, r"Height reached $=\sqrt{13^2-5^2}=12$ m (1). With the ground angle $\theta$: $\sin\theta=\dfrac{12}{13}$, $\cos\theta=\dfrac5{13}$ (1).", "E", wp=True),
W(r"Evaluate $\sin60^\circ\cos30^\circ+\sin30^\circ\cos60^\circ$.", 2, r"$\dfrac{\sqrt3}2\cdot\dfrac{\sqrt3}2+\dfrac12\cdot\dfrac12=\dfrac34+\dfrac14=1$. (1+1)", "E"),
W(r"A ramp rises 7 m over a horizontal distance of 24 m. Find its length and the ratio $\sin\theta$, where $\theta$ is the angle it makes with the horizontal.", 2, r"Length $=\sqrt{7^2+24^2}=25$ m (1). $\sin\theta=\dfrac7{25}$ (1).", "E", wp=True),
W(r"The slope of a roof makes an angle $A$ with the horizontal where $\tan A=\dfrac43$. Find $\sin A$ and $\cos A$.", 2, r"Perpendicular 4, base 3, hypotenuse $\sqrt{16+9}=5$ (1). $\sin A=\dfrac45$, $\cos A=\dfrac35$ (1).", "E", wp=True),
W(r"Evaluate $\dfrac{\tan26^\circ}{\cot64^\circ}$.", 2, r"$\cot64^\circ=\cot(90^\circ-26^\circ)=\tan26^\circ$ (1), so the value is $1$ (1).", "E"),
W(r"A kite string 20 m long is taut and the kite is 12 m above the flier's hand level. Find $\sin\theta$ and $\cos\theta$, where $\theta$ is the angle the string makes with the horizontal.", 2, r"Horizontal distance $=\sqrt{20^2-12^2}=16$ m (1). $\sin\theta=\dfrac{12}{20}=\dfrac35$, $\cos\theta=\dfrac{16}{20}=\dfrac45$ (1).", "E", wp=True),
W(r"True or false? Give a reason. $\sin A=\dfrac43$ is possible for some acute angle $A$.", 2, r"**False** (1). $\sin A=\dfrac{\text{perpendicular}}{\text{hypotenuse}}$ and the hypotenuse is the longest side, so $\sin A\le1$; $\dfrac43>1$ (1).", "E"),
W(r"Express $\cot75^\circ$ as a trigonometric ratio of an angle between $0^\circ$ and $45^\circ$.", 2, r"$\cot75^\circ=\cot(90^\circ-15^\circ)=\tan15^\circ$. (1+1)", "E"),
W(r"A 10 m ladder touches a wall at a height of 5 m. What angle does it make with the ground?", 2, r"$\sin\theta=\dfrac5{10}=\dfrac12$ (1), so $\theta=30^\circ$ (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"If $\sin A=\dfrac8{17}$, find $\cos A$ and $\tan A$.", 2, r"Base $=\sqrt{17^2-8^2}=15$ (1). $\cos A=\dfrac{15}{17}$, $\tan A=\dfrac8{15}$ (1).", "M"),
W(r"If $15\cot A=8$, find $\sin A$ and $\sec A$.", 2, r"$\cot A=\dfrac8{15}$: base 8, perpendicular 15, hypotenuse 17 (1). $\sin A=\dfrac{15}{17}$, $\sec A=\dfrac{17}8$ (1).", "M"),
W(r"If $\tan A=\dfrac5{12}$, find the value of $\dfrac{\cos A+\sin A}{\cos A-\sin A}$.", 2, r"Divide numerator and denominator by $\cos A$: $\dfrac{1+\tan A}{1-\tan A}$ (1) $=\dfrac{17/12}{7/12}=\dfrac{17}7$ (1).", "M"),
W(r"Evaluate $\dfrac{\tan45^\circ}{\operatorname{cosec}30^\circ+\sec60^\circ-\cot45^\circ}$.", 2, r"$\dfrac{1}{2+2-1}$ (1) $=\dfrac13$ (1).", "M"),
W(r"A 26 m ladder reaches a window 24 m above the ground. Find the distance of its foot from the wall and the values of $\cos\theta$ and $\tan\theta$, where $\theta$ is the angle with the ground.", 3, r"Foot distance $=\sqrt{26^2-24^2}=10$ m (1). $\cos\theta=\dfrac{10}{26}=\dfrac5{13}$ (1). $\tan\theta=\dfrac{24}{10}=\dfrac{12}5$ (1).", "M", wp=True),
W(r"If $\sin3A=\cos(A-26^\circ)$, where $3A$ is acute, find $A$.", 3, r"$\cos(A-26^\circ)=\sin(90^\circ-(A-26^\circ))=\sin(116^\circ-A)$ (1). So $3A=116^\circ-A$ (1), $A=29^\circ$ (1).", "M"),
W(r"Evaluate $\dfrac{\sin18^\circ}{\cos72^\circ}+\dfrac{\tan17^\circ}{\cot73^\circ}$.", 2, r"$\cos72^\circ=\sin18^\circ$ and $\cot73^\circ=\tan17^\circ$ (1). Value $=1+1=2$ (1).", "M"),
W(r"Verify that $\cos60^\circ=1-2\sin^230^\circ=2\cos^230^\circ-1$.", 3, r"$1-2\left(\dfrac12\right)^2=1-\dfrac12=\dfrac12$ (1). $2\left(\dfrac{\sqrt3}2\right)^2-1=\dfrac32-1=\dfrac12$ (1). Both equal $\cos60^\circ=\dfrac12$ (1).", "M"),
W(r"A triangular field $PQR$ is right-angled at $Q$ with $PQ=5$ m and $PR+QR=25$ m. Find $\sin P$, $\cos P$ and $\tan P$.", 3, r"Let $QR=x$, $PR=25-x$. $PR^2=PQ^2+QR^2\Rightarrow(25-x)^2=25+x^2\Rightarrow625-50x=25$, $x=12$ (1). So $QR=12$, $PR=13$ (1). $\sin P=\dfrac{12}{13}$, $\cos P=\dfrac5{13}$, $\tan P=\dfrac{12}5$ (1).", "M", wp=True),
W(r"Simplify $(1+\tan^2\theta)(1-\sin\theta)(1+\sin\theta)$.", 2, r"$(1-\sin^2\theta)\sec^2\theta=\cos^2\theta\cdot\dfrac1{\cos^2\theta}=1$. (1+1)", "M"),
W(r"Prove that $\dfrac{\sin\theta}{1+\cos\theta}+\dfrac{1+\cos\theta}{\sin\theta}=2\operatorname{cosec}\theta$.", 3, r"LHS $=\dfrac{\sin^2\theta+(1+\cos\theta)^2}{\sin\theta(1+\cos\theta)}$ (1) $=\dfrac{\sin^2\theta+1+2\cos\theta+\cos^2\theta}{\sin\theta(1+\cos\theta)}=\dfrac{2+2\cos\theta}{\sin\theta(1+\cos\theta)}$ (1) $=\dfrac2{\sin\theta}=2\operatorname{cosec}\theta$ (1).", "M"),
W(r"Prove that $\cos^4A-\sin^4A=2\cos^2A-1$.", 3, r"LHS $=(\cos^2A-\sin^2A)(\cos^2A+\sin^2A)$ (1) $=\cos^2A-\sin^2A$ (1) $=\cos^2A-(1-\cos^2A)=2\cos^2A-1$ (1).", "M"),
W(r"Aman writes: '$\sin60^\circ=2\sin30^\circ$'. Is he right? Find his mistake.", 2, r"No. $\sin60^\circ=\dfrac{\sqrt3}2\approx0.87$ but $2\sin30^\circ=1$ (1). A ratio is not multiplied through like an algebraic quantity: $\sin(2A)\ne2\sin A$ (1).", "M"),
W(r"A rectangular park has length 15 m and diagonal 17 m. If $\theta$ is the angle between the diagonal and the length, find $\sin\theta$, $\cos\theta$ and $\tan\theta$.", 3, r"Breadth $=\sqrt{17^2-15^2}=8$ m (1). $\sin\theta=\dfrac8{17}$, $\cos\theta=\dfrac{15}{17}$ (1), $\tan\theta=\dfrac8{15}$ (1).", "M", wp=True),
W(r"If $\sec\theta=\dfrac{13}{12}$, find all the other trigonometric ratios.", 3, r"Hypotenuse 13, base 12, perpendicular $=\sqrt{169-144}=5$ (1). $\sin\theta=\dfrac5{13}$, $\cos\theta=\dfrac{12}{13}$, $\tan\theta=\dfrac5{12}$ (1). $\cot\theta=\dfrac{12}5$, $\operatorname{cosec}\theta=\dfrac{13}5$ (1).", "M"),
W(r"If $\tan(A+B)=\sqrt3$ and $\tan(A-B)=\dfrac1{\sqrt3}$, with $0^\circ<A+B\le90^\circ$ and $A>B$, find $A$ and $B$.", 3, r"$A+B=60^\circ$ and $A-B=30^\circ$ (1). Adding: $2A=90^\circ$, $A=45^\circ$ (1). Then $B=15^\circ$ (1).", "M"),
W(r"A ramp for a wheelchair rises 1.5 m over a horizontal run of 3.6 m. Find the length of the ramp and the value of $\sin\theta$ for the angle $\theta$ of the ramp.", 3, r"Length $=\sqrt{1.5^2+3.6^2}=\sqrt{2.25+12.96}=\sqrt{15.21}=3.9$ m (2). $\sin\theta=\dfrac{1.5}{3.9}=\dfrac5{13}$ (1).", "M", wp=True),
W(r"Express $\sin67^\circ+\cos75^\circ$ in terms of trigonometric ratios of angles between $0^\circ$ and $45^\circ$.", 2, r"$\sin67^\circ=\cos(90^\circ-67^\circ)=\cos23^\circ$ (1) and $\cos75^\circ=\sin15^\circ$ (1). So the expression is $\cos23^\circ+\sin15^\circ$.", "M"),
W(r"Evaluate $\dfrac{2\tan30^\circ}{1+\tan^230^\circ}$ and name the ratio of a standard angle it equals.", 3, r"$\tan30^\circ=\dfrac1{\sqrt3}$. Numerator $=\dfrac2{\sqrt3}$, denominator $=1+\dfrac13=\dfrac43$ (1). Value $=\dfrac2{\sqrt3}\times\dfrac34=\dfrac{\sqrt3}2$ (1), which equals $\sin60^\circ$ (1).", "M"),
# ---------------- HARD ----------------
W(r"Evaluate $\dfrac{\sin30^\circ+\tan45^\circ-\operatorname{cosec}60^\circ}{\sec30^\circ+\cos60^\circ+\cot45^\circ}$.", 4, r"Numerator $=\dfrac12+1-\dfrac2{\sqrt3}=\dfrac{3\sqrt3-4}{2\sqrt3}$ (1). Denominator $=\dfrac2{\sqrt3}+\dfrac12+1=\dfrac{3\sqrt3+4}{2\sqrt3}$ (1). Ratio $=\dfrac{3\sqrt3-4}{3\sqrt3+4}$ (1). Multiply by $(3\sqrt3-4)$: $\dfrac{(3\sqrt3-4)^2}{27-16}=\dfrac{43-24\sqrt3}{11}$ (1).", "H"),
W(r"Prove that $\dfrac{1+\sec A}{\sec A}=\dfrac{\sin^2A}{1-\cos A}$.", 3, r"LHS $=\dfrac{1+\frac1{\cos A}}{\frac1{\cos A}}=\cos A+1$ (1). RHS $=\dfrac{1-\cos^2A}{1-\cos A}$ (1) $=\dfrac{(1-\cos A)(1+\cos A)}{1-\cos A}=1+\cos A$ (1). LHS = RHS.", "H"),
W(r"A triangular flower bed $ABC$ is right-angled at $B$ and $\tan A=\dfrac1{\sqrt3}$. Find the value of $\sin A\cos C+\cos A\sin C$.", 3, r"$\tan A=\dfrac1{\sqrt3}\Rightarrow A=30^\circ$ (1), so $C=60^\circ$ (1). $\sin30^\circ\cos60^\circ+\cos30^\circ\sin60^\circ=\dfrac14+\dfrac34=1$ (1).", "H", wp=True),
W(r"If $\sin\theta+\sin^2\theta=1$, show that $\cos^2\theta+\cos^4\theta=1$.", 3, r"$\sin\theta=1-\sin^2\theta=\cos^2\theta$ (1). Then $\cos^4\theta=\sin^2\theta$ (1). So $\cos^2\theta+\cos^4\theta=\sin\theta+\sin^2\theta=1$ (1).", "H"),
W(r"A 15 m ladder has its foot 9 m from the base of a wall. A safety rule says the ladder should make an angle of at least $60^\circ$ with the ground. Does it satisfy the rule? Reason using $\cos\theta$ (do not use a calculator).", 3, r"$\cos\theta=\dfrac9{15}=0.6$ (1). Since $\cos60^\circ=0.5$ and the cosine **decreases** as the angle increases, $\cos\theta=0.6>0.5$ means $\theta<60^\circ$ (1). So the ladder does **not** satisfy the rule (1).", "H", wp=True),
W(r"Two slides in a park are 3 m high. One makes an angle of $30^\circ$ with the ground and the other $60^\circ$. Find the length of each slide.", 3, r"Length $=\dfrac{3}{\sin\theta}$ (1). For $30^\circ$: $\dfrac3{1/2}=6$ m (1). For $60^\circ$: $\dfrac3{\sqrt3/2}=2\sqrt3\approx3.46$ m (1).", "H", wp=True),
W(r"If $\tan\theta+\sin\theta=m$ and $\tan\theta-\sin\theta=n$, show that $m^2-n^2=4\sqrt{mn}$.", 4, r"$m^2-n^2=(m+n)(m-n)=(2\tan\theta)(2\sin\theta)=4\tan\theta\sin\theta$ (2). $mn=\tan^2\theta-\sin^2\theta=\sin^2\theta\left(\dfrac1{\cos^2\theta}-1\right)=\sin^2\theta\tan^2\theta$ (1). So $\sqrt{mn}=\sin\theta\tan\theta$ and $m^2-n^2=4\sqrt{mn}$ (1).", "H"),
W(r"If $\sec\theta+\tan\theta=p$, show that $\sin\theta=\dfrac{p^2-1}{p^2+1}$.", 4, r"$(\sec\theta-\tan\theta)(\sec\theta+\tan\theta)=1$, so $\sec\theta-\tan\theta=\dfrac1p$ (1). Adding and subtracting: $\sec\theta=\dfrac12\left(p+\dfrac1p\right)=\dfrac{p^2+1}{2p}$ and $\tan\theta=\dfrac{p^2-1}{2p}$ (2). $\sin\theta=\dfrac{\tan\theta}{\sec\theta}=\dfrac{p^2-1}{p^2+1}$ (1).", "H"),
W(r"Prove that $\dfrac{\cos A}{1-\tan A}+\dfrac{\sin A}{1-\cot A}=\sin A+\cos A$.", 4, r"$\dfrac{\cos A}{1-\frac{\sin A}{\cos A}}=\dfrac{\cos^2A}{\cos A-\sin A}$ (1) and $\dfrac{\sin A}{1-\frac{\cos A}{\sin A}}=\dfrac{\sin^2A}{\sin A-\cos A}=-\dfrac{\sin^2A}{\cos A-\sin A}$ (1). Sum $=\dfrac{\cos^2A-\sin^2A}{\cos A-\sin A}$ (1) $=\cos A+\sin A$ (1).", "H"),
W(r"Prove that $\dfrac{\tan\theta+\sec\theta-1}{\tan\theta-\sec\theta+1}=\dfrac{1+\sin\theta}{\cos\theta}$.", 4, r"Replace the $1$ in the numerator by $\sec^2\theta-\tan^2\theta$: numerator $=(\tan\theta+\sec\theta)-(\sec\theta-\tan\theta)(\sec\theta+\tan\theta)=(\tan\theta+\sec\theta)(1-\sec\theta+\tan\theta)$ (2). Cancel the common factor $(\tan\theta-\sec\theta+1)$: ratio $=\tan\theta+\sec\theta$ (1) $=\dfrac{\sin\theta+1}{\cos\theta}$ (1).", "H"),
W(r"Prove that $(\sin A+\operatorname{cosec}A)^2+(\cos A+\sec A)^2=7+\tan^2A+\cot^2A$.", 4, r"Expand: $\sin^2A+2+\operatorname{cosec}^2A+\cos^2A+2+\sec^2A$ (1). $=(\sin^2A+\cos^2A)+4+\operatorname{cosec}^2A+\sec^2A$ (1) $=1+4+(1+\cot^2A)+(1+\tan^2A)$ (1) $=7+\tan^2A+\cot^2A$ (1).", "H"),
W(r"**Case study.** A surveyor models a triangular plot $PQR$ in Sikar, right-angled at $Q$, with $PQ=20$ m and $QR=21$ m. (i) Find $PR$. (ii) Find $\sin P$, $\cos P$ and $\tan P$. (iii) Show that $\sin R=\cos P$ and explain why this happens.", 5, r"(i) $PR=\sqrt{400+441}=29$ m (1). (ii) $\sin P=\dfrac{21}{29}$, $\cos P=\dfrac{20}{29}$, $\tan P=\dfrac{21}{20}$ (2). (iii) For angle $R$ the perpendicular is $PQ=20$, so $\sin R=\dfrac{20}{29}=\cos P$ (1). It happens because $P+R=90^\circ$, i.e. they are complementary and $\sin(90^\circ-P)=\cos P$ (1).", "H", wp=True),
W(r"If $\tan A=n\tan B$ and $\sin A=m\sin B$, prove that $\cos^2A=\dfrac{m^2-1}{n^2-1}$.", 5, r"From $\dfrac{\sin A}{\cos A}=n\dfrac{\sin B}{\cos B}$ and $\sin A=m\sin B$: $\dfrac m{\cos A}=\dfrac n{\cos B}$, so $\cos B=\dfrac{n\cos A}m$ (2). $\sin^2A=m^2\sin^2B=m^2(1-\cos^2B)=m^2-n^2\cos^2A$ (1). So $1-\cos^2A=m^2-n^2\cos^2A$ (1), giving $(n^2-1)\cos^2A=m^2-1$, i.e. $\cos^2A=\dfrac{m^2-1}{n^2-1}$ (1).", "H"),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(8)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "8.5 More Worked Examples"),
 ("h3", "Example 1 — Finding all ratios from one ratio"),
 ("steps", [("If sec θ = 13/12, find the other ratios", "sec θ = hypotenuse/base, so draw a right triangle with hypotenuse 13 and base 12."), ("Third side", "Perpendicular = √(13² − 12²) = √25 = 5."), ("Read the ratios", "sin θ = 5/13, cos θ = 12/13, tan θ = 5/12, cot θ = 12/5, cosec θ = 13/5.")]),
 ("h3", "Example 2 — Using the Pythagorean triple from a word problem"),
 ("steps", [("A 26 m ladder reaches a window 24 m high. Find cos θ and tan θ for the angle with the ground", "Ladder = hypotenuse = 26 m, wall = perpendicular = 24 m."), ("Foot distance", "Base = √(26² − 24²) = √100 = 10 m."), ("Ratios", "cos θ = base/hypotenuse = 10/26 = 5/13; tan θ = 24/10 = 12/5.")]),
 ("h3", "Example 3 — Complementary angle equation"),
 ("steps", [("If sin 3A = cos(A − 26°), find A", "Write the cosine as a sine: cos(A − 26°) = sin(90° − (A − 26°)) = sin(116° − A)."), ("Equate the angles", "3A = 116° − A, so 4A = 116° and **A = 29°**."), ("Check", "sin 87° = cos 3°, and cos(29° − 26°) = cos 3°. ✓")]),
 ("h3", "Example 4 — Evaluating a mixed expression"),
 ("steps", [("Evaluate tan 45° ÷ (cosec 30° + sec 60° − cot 45°)", "Substitute: tan 45° = 1, cosec 30° = 2, sec 60° = 2, cot 45° = 1."), ("Simplify", "1 ÷ (2 + 2 − 1) = **1/3**.")]),
 ("h3", "Example 5 — Proving an identity"),
 ("steps", [("Prove: cos⁴A − sin⁴A = 2cos²A − 1", "LHS is a difference of squares: (cos²A − sin²A)(cos²A + sin²A)."), ("Use the identity", "cos²A + sin²A = 1, so LHS = cos²A − sin²A."), ("Finish", "Replace sin²A by 1 − cos²A: LHS = cos²A − 1 + cos²A = 2cos²A − 1 = RHS. ✓")]),
 ("h3", "Example 6 — Eliminating a ratio"),
 ("steps", [("If sec θ + tan θ = p, show sin θ = (p² − 1)/(p² + 1)", "Since (sec θ − tan θ)(sec θ + tan θ) = 1, we get sec θ − tan θ = 1/p."), ("Add and subtract", "sec θ = (p + 1/p)/2 = (p² + 1)/2p and tan θ = (p − 1/p)/2 = (p² − 1)/2p."), ("Divide", "sin θ = tan θ ÷ sec θ = (p² − 1)/(p² + 1).")]),
 ("h2", "8.6 Real-Life Right Triangles: How to Translate"),
 ("p", "Many word problems in this chapter describe a ladder, ramp, slide, kite string, roof or diagonal of a plot. In each, find the right-angled triangle, then name the sides **from the point of view of the angle asked for**."),
 ("table", ["Situation", "Hypotenuse", "Perpendicular (opposite)", "Base (adjacent)"], [
  ["Ladder against a wall (angle with the ground)", "the ladder", "height on the wall", "distance of the foot from the wall"],
  ["Ramp or slide (angle with the horizontal)", "the sloping length", "vertical rise", "horizontal run"],
  ["Kite string (angle with the horizontal)", "the string", "height of the kite", "horizontal distance"],
  ["Diagonal of a rectangular plot", "the diagonal", "the side opposite the angle", "the side along the angle"],
  ["Roof truss or slope tan A = rise ÷ run", "the sloping rafter", "rise", "run"]]),
 ("note", "REMEMBER", "The same triangle gives **different ratios for the other acute angle**: the perpendicular for angle A is the base for angle C. That is why sin A = cos C when A + C = 90°."),
 ("p", "**Useful Pythagorean triples** let you avoid square roots: (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), and their multiples such as (6, 8, 10) or (9, 12, 15)."),
 ("h2", "8.7 Strategy for Proving Identities"),
 ("ol", ["Start with the **more complicated side** and try to reach the other side.", "Convert everything to **sin and cos** (tan = sin/cos, sec = 1/cos, and so on) when you are stuck.", "Look for patterns: a² − b² = (a − b)(a + b) and (a + b)² expansions, and the three identities, especially 1 − sin²A = cos²A and sec²A − tan²A = 1.", "If a fraction has 1 ± sin A in the denominator, **multiply and divide by the conjugate** (1 ∓ sin A).", "Never move terms across the equals sign in a proof; work on one side only and finish with ‘= RHS’."]),
 ("h2", "8.8 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["sin 2A = 2 sin A or sin(A + B) = sin A + sin B", "a ratio is a function of the angle, not a multiplier", "sin 60° ≠ 2 sin 30°; evaluate each ratio separately"],
  ["Writing sin² A as sin A²", "sin²A means (sin A)²", "square the ratio, not the angle"],
  ["Taking tan A = hypotenuse/base", "tan A = perpendicular/base", "hypotenuse appears in sin, cos, cosec, sec only"],
  ["sin A = 5/4 accepted as an answer", "sin and cos of an acute angle are at most 1", "check that perpendicular < hypotenuse"],
  ["tan 90° = 0 or cot 90° undefined", "tan 90° is undefined; cot 90° = 0", "learn the table; 0° and 90° swap roles"],
  ["Using sec²A = 1 + sin²A", "the identity is sec²A = 1 + tan²A", "learn the three identities with their ratios paired"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["In a word problem, **identify the right triangle and name the sides from the angle asked for**; the ladder, string or slide is the hypotenuse.", "Use **Pythagorean triples** (3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25) to get exact ratios quickly.", "To prove an identity, **start from the more complicated side**, convert to sin and cos, and use the three identities."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
