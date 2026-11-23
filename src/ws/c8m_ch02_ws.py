"""Class 8 Maths Ch 2 - Power Play: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch02"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

assert 0.1 * 2**10 == 102.4 and 2 * 3**4 == 162 and 2e9 * 86400 == 1.728e14 and 7**2025 % 10 == 7 and 5000 * 2**4 == 80000
assert 2**10 == 1024 and 3**4 == 81 and 4**3 == 64 and 2**(3**2) == 512 and (2**3)**2 == 64
assert 2**4 * 3 == 48 and 1.5e8 / 3.84e5 > 390

WS = [
# ---------------- EASY ----------------
W("$3^2\\times3^5$ is equal to:", 1, "(a) $3^7$. Same base, so add the exponents: $2+5=7$. (1)", "E", opts=["$3^7$", "$3^{10}$", "$9^7$", "$3^3$"]),
W("$(5^3)^2$ is equal to:", 1, "(b) $5^6$. Power of a power: multiply the exponents, $3\\times2=6$. (1)", "E", opts=["$5^5$", "$5^6$", "$5^9$", "$5^1$"]),
W("The value of $7^0+7^{-1}$ is:", 1, "(a) $\\frac{8}{7}$. $7^0=1$ and $7^{-1}=\\frac17$, so the sum is $\\frac87$. (1)", "E", opts=["$\\frac{8}{7}$", "$1$", "$\\frac{1}{7}$", "$\\frac{7}{8}$"]),
W("$10^{-3}$ is equal to:", 1, "(a) 0.001. $10^{-3}=\\frac1{10^3}=\\frac1{1000}$. (1)", "E", opts=["0.001", "0.0001", "$-1000$", "$-30$"]),
W("$4.5\\times10^5$ in usual form (Indian system) is:", 1, "(b) 4,50,000. Move the decimal point 5 places to the right. (1)", "E", opts=["45,000", "4,50,000", "45,00,000", "4,500"]),
W("The standard form of 0.00072 is:", 1, "(b) $7.2\\times10^{-4}$. The decimal point moves 4 places to the right, so the exponent is $-4$. (1)", "E",
  opts=["$7.2\\times10^{-3}$", "$7.2\\times10^{-4}$", "$72\\times10^{-5}$", "$0.72\\times10^{-3}$"]),
W("The value of $(-2)^5$ is:", 1, "(b) $-32$. An odd power of a negative number is negative: $2^5=32$. (1)", "E", opts=["$32$", "$-32$", "$-10$", "$10$"]),
W("Find the values of $2^5$ and $5^2$. Which is greater?", 2, "$2^5=32$ and $5^2=25$ (1). $2^5$ is greater (1).", "E"),
W("A bacterium splits into 2 every hour. Starting from 1 bacterium, how many are there after 6 hours?", 2, "Each hour the number doubles, so after 6 hours there are $2^6$ (1) $=$ **64** bacteria (1).", "E", wp=True),
W("Write 10,00,000 as a power of 10.", 1, "$10{,}00{,}000$ has six zeros, so it is $10^6$ (1).", "E"),
W("Simplify $6^5\\div6^3$.", 2, "Same base: subtract the exponents, $6^{5-3}=6^2$ (1) $=36$ (1).", "E"),
W("Write $\\dfrac{1}{81}$ as a power of 3 with a negative exponent.", 1, "$81=3^4$, so $\\frac1{81}=3^{-4}$ (1).", "E"),
W("The speed of light is $3\\times10^8$ m/s. Write this speed in usual form using Indian commas.", 1, "$3\\times10^8=30{,}00{,}00{,}000$ m/s (1).", "E", wp=True),
W("The thickness of a human hair is about 0.00007 m. Write it in standard form.", 2, "The decimal point moves 5 places to the right (1): $7\\times10^{-5}$ m (1).", "E", wp=True),
W("Which is greater, $3\\times10^4$ or $2\\times10^5$? Give a reason.", 1, "$2\\times10^5$ is greater because its power of 10 is larger ($2{,}00{,}000>30{,}000$) (1).", "E"),
W("Simplify $(2^3)^2\\times2^{-4}$.", 2, "$(2^3)^2=2^6$ (1); $2^6\\times2^{-4}=2^2=4$ (1).", "E"),
W("The population of a town is $2.5\\times10^5$. Write it in usual form.", 1, "$2.5\\times10^5=2{,}50{,}000$ (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("A chain message is sent as follows: in stage 1 one person sends it to 3 people; in each later stage every person who received it in the previous stage sends it to 3 new people. How many people receive it in stage 6?", 2, "Stage 1: 3; stage 2: $3^2$; stage $n$: $3^n$ (1). Stage 6: $3^6=$ **729** people (1).", "M", wp=True),
W("A sheet of paper is 0.1 mm thick. It is folded in half 10 times, so the thickness doubles at each fold. Find the thickness of the folded paper in mm and in cm.", 3, "Thickness $=0.1\\times2^{10}$ (1) $=0.1\\times1024=102.4$ mm (1) $=$ **10.24 cm** (1).", "M", wp=True),
W("Simplify $\\dfrac{2^5\\times3^4}{2^3\\times3^2}$.", 2, "$2^{5-3}\\times3^{4-2}=2^2\\times3^2$ (1) $=4\\times9=$ **36** (1).", "M"),
W("Simplify $\\left(\\dfrac23\\right)^{-3}$.", 2, "$\\left(\\frac23\\right)^{-3}=\\left(\\frac32\\right)^3$ (1) $=\\frac{27}{8}$ (1).", "M"),
W("Simplify $\\dfrac{(5^3)^2\\times5^{-4}}{5^2}$.", 3, "$(5^3)^2=5^6$ (1). Numerator $=5^{6-4}=5^2$ (1). $5^2\\div5^2=5^0=$ **1** (1).", "M"),
W("Write in standard form: (i) 62,00,00,000 (ii) 0.000345.", 2, "(i) 62,00,00,000 $=620{,}000{,}000=6.2\\times10^8$ (1). (ii) $0.000345=3.45\\times10^{-4}$ (1).", "M"),
W("The mass of the Earth is $5.97\\times10^{24}$ kg and that of the Moon is $7.35\\times10^{22}$ kg. Approximately how many times heavier is the Earth than the Moon?", 3, "Ratio $=\\dfrac{5.97\\times10^{24}}{7.35\\times10^{22}}$ (1) $=\\dfrac{5.97}{7.35}\\times10^{2}$ (1) $\\approx0.812\\times100\\approx$ **81 times** (1).", "M", wp=True),
W("Light travels $3\\times10^8$ m in one second. The Sun is $1.5\\times10^{11}$ m from the Earth. How long does sunlight take to reach the Earth? Give the answer in seconds and in minutes and seconds.", 3, "Time $=\\dfrac{1.5\\times10^{11}}{3\\times10^8}$ (1) $=0.5\\times10^3=500$ s (1) $=$ **8 min 20 s** (1).", "M", wp=True),
W("Find $x$: (i) $3^x\\times3^4=3^9$ (ii) $7^x\\div7^3=7^{-2}$.", 2, "(i) $x+4=9$, $x=5$ (1). (ii) $x-3=-2$, $x=1$ (1).", "M"),
W("Express 243 and $\\dfrac1{243}$ as powers of 3.", 2, "$243=3^5$ (1) and $\\frac1{243}=3^{-5}$ (1).", "M"),
W("Without a calculator compare (i) $2^{10}$ and $10^3$ (ii) $3^4$ and $4^3$.", 2, "(i) $2^{10}=1024>1000=10^3$ (1). (ii) $3^4=81>64=4^3$ (1).", "M"),
W("The population of India is about $1.4\\times10^9$ and that of a state is $7\\times10^7$. About how many such states would make up the population of India?", 2, "$\\dfrac{1.4\\times10^9}{7\\times10^7}=0.2\\times10^2$ (1) $=$ **20** (1).", "M", wp=True),
W("The diameter of an atom is about $1\\times10^{-10}$ m. How many atoms placed side by side in a line (each taking up one diameter) make a length of 1 mm $=10^{-3}$ m?", 3, "Number $=\\dfrac{10^{-3}}{10^{-10}}$ (1) $=10^{-3-(-10)}$ (1) $=10^7$, i.e. **1 crore** atoms (1).", "M", wp=True),
W("Sita writes $2^3+2^2=2^5$. Is she right? Check, and say what the mistake is.", 2, "$2^3+2^2=8+4=12$, but $2^5=32$, so she is wrong (1). The laws apply to **products** ($2^3\\times2^2=2^5$), not to sums (1).", "M"),
W("Simplify $\\dfrac{x^5\\times x^{-2}}{x^2}$ ($x\\ne0$).", 2, "$x^5\\times x^{-2}=x^3$ (1); $x^3\\div x^2=$ **$x$** (1).", "M"),
W("A sum of money doubles every 3 years. If ₹ 5,000 is invested, how much will it become after 12 years?", 3, "12 years has $12\\div3=4$ doublings (1). Amount $=5000\\times2^4$ (1) $=5000\\times16=$ **₹ 80,000** (1).", "M", wp=True),
W("Add $3\\times10^4+2\\times10^3$ and give the answer in standard form.", 2, "Make powers equal: $30\\times10^3+2\\times10^3=32\\times10^3$ (1) $=$ **$3.2\\times10^4$** (1).", "M"),
W("Evaluate $(-3)^4$, $(-3)^3$ and $-3^2$. Why are the first and third different?", 3, "$(-3)^4=81$ (1); $(-3)^3=-27$ (1); $-3^2=-9$ (the minus sign is not inside the power, only 3 is squared) (1).", "M"),
W("Write in usual form: (i) $4.7\\times10^{-3}$ (ii) $8\\times10^6$.", 2, "(i) $0.0047$ (1). (ii) $80{,}00{,}000$ (eighty lakh) (1).", "M"),
# ---------------- HARD ----------------
W("Rice grains are placed on a chessboard: 1 on the first square, 2 on the second, 4 on the third and so on (doubling each time). (i) How many grains are on the 10th square? (ii) How many grains are on the first 10 squares together?", 4, "(i) Square $n$ has $2^{n-1}$ grains: $2^9=$ **512** (2). (ii) $1+2+4+\\dots+512=2^{10}-1=$ **1,023** (2).", "H", wp=True),
W("A lab sample contains $3\\times10^5$ bacteria per millilitre. How many bacteria are in $2.5\\times10^2$ mL? Give the answer in standard form.", 3, "Total $=(3\\times10^5)\\times(2.5\\times10^2)$ (1) $=7.5\\times10^{7}$ (2).", "H", wp=True),
W("Simplify $\\left(\\dfrac23\\right)^{-2}\\times\\left(\\dfrac94\\right)^{-1}$.", 3, "$\\left(\\frac23\\right)^{-2}=\\frac94$ (1); $\\left(\\frac94\\right)^{-1}=\\frac49$ (1); product $=\\frac94\\times\\frac49=$ **1** (1).", "H"),
W("Simplify $\\dfrac{12^4\\times9^3\\times4}{6^3\\times8^2\\times27}$ by writing every base as a product of primes.", 4, "Numerator $=(2^2\\cdot3)^4\\cdot(3^2)^3\\cdot2^2=2^{10}\\cdot3^{10}$ (2). Denominator $=(2\\cdot3)^3\\cdot(2^3)^2\\cdot3^3=2^9\\cdot3^6$ (1). Value $=2^{1}\\times3^{4}=$ **162** (1).", "H"),
W("Find (i) $(4.2\\times10^5)\\div(2.1\\times10^2)$ and (ii) $(3\\times10^{-2})\\times(5\\times10^6)$, each in standard form.", 3, "(i) $(4.2\\div2.1)\\times10^{5-2}=2\\times10^3$ (1). (ii) $15\\times10^{4}$ (1) $=1.5\\times10^5$ in standard form (1).", "H"),
W("The mass of a hydrogen atom is $1.67\\times10^{-27}$ kg and that of an electron is $9.1\\times10^{-31}$ kg. Approximately how many times heavier is the hydrogen atom than the electron?", 3, "Ratio $=\\dfrac{1.67\\times10^{-27}}{9.1\\times10^{-31}}$ (1) $=\\dfrac{1.67}{9.1}\\times10^{4}$ (1) $\\approx0.1835\\times10^4\\approx$ **1,835 times** (1).", "H", wp=True),
W("Find $n$ if $2^{n+1}+2^n=48$.", 3, "$2^{n+1}=2\\times2^n$, so $2\\times2^n+2^n=3\\times2^n$ (1). $3\\times2^n=48\\Rightarrow2^n=16$ (1). $n=$ **4** (1).", "H"),
W("Find $x$ if $\\left(\\dfrac53\\right)^{x}\\times\\left(\\dfrac53\\right)^{-3}=\\left(\\dfrac35\\right)^{-4}$.", 3, "$\\left(\\frac35\\right)^{-4}=\\left(\\frac53\\right)^4$ (1). LHS $=\\left(\\frac53\\right)^{x-3}$ (1). $x-3=4\\Rightarrow x=$ **7** (1).", "H"),
W("A computer performs $2\\times10^9$ operations every second. How many operations does it perform in one day? (1 day $=8.64\\times10^4$ seconds.) Give the answer in standard form.", 4, "Operations $=(2\\times10^9)\\times(8.64\\times10^4)$ (1) $=17.28\\times10^{13}$ (2) $=$ **$1.728\\times10^{14}$** (1).", "H", wp=True),
W("Using the pattern $3^4=81,\\ 3^3=27,\\ 3^2=9,\\ 3^1=3$ (each time divide by 3), explain what $3^0$, $3^{-1}$ and $3^{-2}$ must be.", 3, "Continuing the pattern: $3^0=3\\div3=1$ (1); $3^{-1}=1\\div3=\\frac13$ (1); $3^{-2}=\\frac13\\div3=\\frac19$ (1).", "H"),
W("**Case study.** Average distances from the Sun: Mercury $5.8\\times10^7$ km, Earth $1.5\\times10^8$ km, Jupiter $7.8\\times10^8$ km, Neptune $4.5\\times10^9$ km. (i) Arrange the planets from nearest to farthest. (ii) How many times is Neptune farther than Earth? (iii) Find, in standard form, how much farther Jupiter is than Earth.", 4, "(i) Mercury, Earth, Jupiter, Neptune (compare powers of 10 first: 7, 8, 8, 9; then $1.5<7.8$) (1). (ii) $\\frac{4.5\\times10^9}{1.5\\times10^8}=3\\times10=$ **30 times** (1.5). (iii) $7.8\\times10^8-1.5\\times10^8=6.3\\times10^8$ km (1.5).", "H", wp=True),
W("Are $(2^3)^2$ and $2^{(3^2)}$ equal? Find both values and say which law applies to the first.", 3, "$(2^3)^2=2^6=64$ (1), using $(a^m)^n=a^{mn}$ (1). $2^{(3^2)}=2^9=512$, so they are **not** equal (1).", "H"),
W("Simplify $\\dfrac{25\\times5^2\\times t^8}{10^3\\times t^4}$ ($t\\ne0$).", 3, "Numerator $=5^2\\cdot5^2\\cdot t^8=5^4t^8$; denominator $=2^3\\cdot5^3\\cdot t^4$ (1). $\\dfrac{5^{4-3}\\,t^{8-4}}{2^3}$ (1) $=\\dfrac{5t^4}{8}$ (1).", "H"),
W("Powers of 7 follow a pattern: $7^1=7,\\ 7^2=49,\\ 7^3=343,\\ 7^4=2401$. Use the pattern of units digits to find the units digit of $7^{2025}$.", 3, "Units digits repeat every 4 powers: 7, 9, 3, 1 (1). $2025=4\\times506+1$ (1), so $7^{2025}$ ends in the same digit as $7^1$: **7** (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(2)
_pre = [b for b in _o["blocks"][:-2]]
_extra = [
 ("h2", "2.5 Growth by Powers: Doubling and Halving"),
 ("p", "Powers describe anything that keeps **multiplying by the same number**. A bacterium that splits into 2 every hour gives 2, 4, 8, … that is 2ⁿ after n hours. Paper 0.1 mm thick, folded 10 times, becomes 0.1 × 2¹⁰ = 102.4 mm, more than 10 cm. A rumour told to 3 new people in each stage reaches 3ⁿ people in stage n. Money that doubles every 3 years grows as ₹5,000 × 2⁴ = ₹80,000 in 12 years."),
 ("table", ["Situation", "Rule", "After 6 steps"], [["Doubling each step from 1", "2ⁿ", "2⁶ = 64"], ["Tripling each step from 1", "3ⁿ", "3⁶ = 729"], ["Halving each step from 1", "(½)ⁿ = 2⁻ⁿ", "(½)⁶ = 1/64"], ["Chessboard grains (1, 2, 4, …)", "square n has 2ⁿ⁻¹ grains", "6th square: 2⁵ = 32"]]),
 ("note", "NOTE", "Sum of the doubling sequence: 1 + 2 + 4 + … + 2ⁿ⁻¹ = **2ⁿ − 1**. On the 10 squares: 2¹⁰ − 1 = 1,023 grains."),
 ("h2", "2.6 Worked Examples"),
 ("h3", "Example 1 — Using the laws together"),
 ("steps", [("Simplify (5³)² × 5⁻⁴ ÷ 5²", "(5³)² = 5⁶."), ("Combine", "5⁶ × 5⁻⁴ = 5², then 5² ÷ 5² = 5⁰."), ("Answer", "**1**")]),
 ("h3", "Example 2 — Writing every base with primes"),
 ("steps", [("Simplify (12⁴ × 9³ × 4) ÷ (6³ × 8² × 27)", "12 = 2² × 3, 9 = 3², 4 = 2², 6 = 2 × 3, 8 = 2³, 27 = 3³."), ("Collect powers", "Numerator = 2⁸ · 3⁴ · 3⁶ · 2² = 2¹⁰ · 3¹⁰. Denominator = 2³ · 3³ · 2⁶ · 3³ = 2⁹ · 3⁶."), ("Divide", "2¹⁰⁻⁹ × 3¹⁰⁻⁶ = 2 × 81 = **162**.")]),
 ("h3", "Example 3 — Solving for an unknown exponent"),
 ("steps", [("Find n if 2ⁿ⁺¹ + 2ⁿ = 48", "2ⁿ⁺¹ = 2 × 2ⁿ."), ("Combine like terms", "2 × 2ⁿ + 2ⁿ = 3 × 2ⁿ = 48, so 2ⁿ = 16."), ("Answer", "16 = 2⁴, so **n = 4**.")]),
 ("h3", "Example 4 — Standard form of a large and a small number"),
 ("steps", [("Write 62,00,00,000", "Remove the Indian commas: 620,000,000."), ("Place one digit before the point", "Move the point 8 places left: 6.2."), ("Answer", "62,00,00,000 = **6.2 × 10⁸**; similarly 0.000345 = **3.45 × 10⁻⁴**.")]),
 ("h3", "Example 5 — Dividing in standard form (a word problem)"),
 ("steps", [("Time for sunlight to reach the Earth", "Distance 1.5 × 10¹¹ m, speed 3 × 10⁸ m/s."), ("Divide", "(1.5 ÷ 3) × 10¹¹⁻⁸ = 0.5 × 10³ = 500 s."), ("Convert", "500 s = 8 minutes 20 seconds.")]),
 ("h3", "Example 6 — Comparing two huge numbers"),
 ("steps", [("Earth ÷ Moon in mass", "(5.97 × 10²⁴) ÷ (7.35 × 10²²) = (5.97 ÷ 7.35) × 10²."), ("Divide the numbers", "5.97 ÷ 7.35 ≈ 0.81."), ("Answer", "0.81 × 100 ≈ **81 times** heavier.")]),
 ("h2", "2.7 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘doubles every …’, ‘splits into 2’", "multiply by 2ⁿ, n = number of doublings", "12 years, doubling every 3 years: 4 doublings"],
  ["‘how many times as large’", "divide the two standard-form numbers: divide the k-parts, subtract the exponents", "Earth ÷ Moon ≈ 81"],
  ["‘total in all samples’", "multiply the number per unit by the number of units", "3 × 10⁵ per mL × 2.5 × 10² mL = 7.5 × 10⁷"],
  ["‘how long / how far’ at constant speed", "time = distance ÷ speed", "1.5 × 10¹¹ ÷ 3 × 10⁸ = 500 s"],
  ["tiny lengths or masses", "negative exponent in standard form", "hair 0.00007 m = 7 × 10⁻⁵ m"]]),
 ("h2", "2.8 Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["2³ + 2² = 2⁵", "laws are for products and quotients, not sums", "8 + 4 = 12"],
  ["(2³)² = 2⁵", "powers of a power are multiplied", "2⁶ = 64"],
  ["(2³)² = 2⁹ (taking 2^(3²))", "(aᵐ)ⁿ means (aᵐ) squared, not a to the power mⁿ", "2⁶ = 64, while 2⁹ = 512"],
  ["3⁻² = −9", "a negative exponent means a reciprocal, not a negative number", "1/9"],
  ["−3² = 9", "the square applies only to 3", "−9; but (−3)² = 9"],
  ["2.5 × 10⁵ + 3 × 10⁴ = 5.5 × 10⁵", "exponents of 10 were different", "25 × 10⁴ + 3 × 10⁴ = 28 × 10⁴ = 2.8 × 10⁵"],
  ["a⁰ = 0", "anything (non-zero) to the power 0 is 1", "1"]]),
 ("note", "REMEMBER", "Before using a law, make sure the **bases are the same** (or write both bases with primes first). To check a long simplification, test it with small numbers."),
 ]
_blocks = _pre + _extra + _o["blocks"][-2:]
CH = dict(_o, blocks=_blocks, takeaways=_o["takeaways"] + ["**Doubling or tripling** problems use 2ⁿ or 3ⁿ; **word problems** with huge numbers are solved by dividing or multiplying in standard form."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
