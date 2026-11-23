"""Class 9 Maths Ch 3 - The World of Numbers: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run
from fractions import Fraction as F

BANK = "c9m_ch03"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c9_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# ---- verification ----
assert F(3, 8) == F(375, 1000) and 7 - (-3) == 10 and -3 + 11 - 5 == 3 and -350 + 500 - 400 == -250
assert F(3, 4) / F(1, 8) == 6 and F(2375, 1000) == F(19, 8) and F(2, 5) + F(3, 10) == F(7, 10) and F(2, 5) - F(3, 10) == F(1, 10)
assert F(4, 9) == F(4, 9) and 8 ** 0.5 * 2 ** 0.5 == 4 or abs((2 * 8) ** 0.5 - 4) < 1e-9
assert (-5) * (-4) == 20 and (-6) * 7 == -42 and 0 - (-9) == 9 and (-12) // (-3) == 4
assert F(5, 8) - F(1, 4) == F(3, 8) and 3 / 8 == 0.375
assert F(36, 99) == F(4, 11) and F(21, 90) == F(7, 30)
assert F(7, 80) == F(875, 10000) and 80 == 2 ** 4 * 5 and F(13, 125) == F(104, 1000)
assert F(525, 100) / F(75, 100) == 7
assert abs(50 ** 0.5 - 7.07) < 0.005 and 22 / 7 * 14 == 44
assert 100 % 6 == 4 and "142857"[3] == "8"
assert (-2 - 5 + 0 - 7 - 3) == -17 and F(-17, 5) == F(-34, 10)
assert F(12, 5) / F(3, 10) == 8
assert F(-2, 3) * (F(3, 4) + F(1, 2)) == F(-5, 6) and F(-2, 3) * F(3, 4) + F(-2, 3) * F(1, 2) == F(-5, 6)
assert 1.4 ** 2 != 2 and abs(1.41 ** 2 - 1.9881) < 1e-9 and abs(1.414 ** 2 - 1.999396) < 1e-9
assert F(126, 99) == F(14, 11) and 50 % 6 == 2 and "714285"[1] == "1" and sum(map(int, "714285")) == 27
assert round(1.414 * 40, 2) == 56.56 and round(56.56 * 50, 2) == 2828.0 and (5 - 4) == 1
assert F(7, 8) == F(875, 1000) and F(7, 25) == F(28, 100) and F(7, 40) == F(175, 1000)
assert 3 * 400 - 5 * 250 == -50 and -50 - (-50) == 0
assert 3 * 76923 == 230769 and 4 * 76923 == 307692 and F(1, 13) * 10**6 // 1 == 76923
assert F(3927, 1250) == F(31416, 10000) and round(30 * 1.414, 2) == 42.42 and abs(30 * 2 ** 0.5 - 42.4264) < 1e-3
assert F(3, 7) < F(2, 4) < F(4, 7) and F(2, 5) < F(41, 100) < F(1, 2)

WS = [
# ---------------- EASY ----------------
W("The number $-3$ belongs to which of these sets?", 1, "(c) Integers. It is not a natural or whole number because it is negative, although it is also a rational number. (1)", "E", opts=["Natural numbers", "Whole numbers", "Integers", "Irrational numbers"]),
W("The decimal expansion of $\\frac38$ is:", 1, "(b) $0.375$. $3\\div8=0.375$, which terminates after $3$ places. (1)", "E", opts=["$0.38$", "$0.375$", "$0.125$", "$0.0375$"]),
W("Which of these numbers is irrational?", 1, "(c) $\\sqrt7$. $7$ is not a perfect square, while $\\sqrt{16}=4$, $0.25=\\frac14$ and $\\frac{22}{7}$ are rational. (1)", "E", opts=["$\\sqrt{16}$", "$0.25$", "$\\sqrt7$", "$\\frac{22}{7}$"]),
W("The decimal $0.333\\dots$ written as a fraction is:", 1, "(a) $\\frac13$. Let $x=0.333\\dots$; $10x-x=3$, so $x=\\frac13$. (1)", "E", opts=["$\\frac13$", "$\\frac{33}{100}$", "$\\frac{3}{10}$", "$\\frac{1}{30}$"]),
W("Using Brahmagupta's rule for 'a fortune minus a debt', $7-(-3)$ equals:", 1, "(b) $10$. Taking away a debt increases the fortune: $7+3=10$. (1)", "E", opts=["$4$", "$10$", "$-4$", "$-10$"]),
W("Between $0$ and $1$ there are:", 1, "(d) infinitely many rational numbers. The average of two rationals is always a rational between them, so the process never ends. (1)", "E", opts=["no rational number", "exactly ten rational numbers", "exactly one rational number", "infinitely many rational numbers"]),
W("The block of digits that repeats in the decimal expansion of $\\frac17$ has length:", 1, "(c) $6$. $\\frac17=0.\\overline{142857}$. (1)", "E", opts=["$1$", "$3$", "$6$", "$7$"]),
W("On a winter night in Mount Abu the temperature is $-3^\\circ$C. By noon it rises by $11^\\circ$C and by evening it falls by $5^\\circ$C. Find the temperature in the evening.", 2, "$-3+11=8$ (1). $8-5=3^\\circ$C (1).", "E", wp=True),
W("A shopkeeper owes ₹ $350$ to a supplier (take this as $-350$). He receives ₹ $500$ from customers and then pays ₹ $400$ for rent. Find his final balance and say whether he is in debt or fortune.", 2, "$-350+500-400=-250$ (1). He is in debt of ₹ $250$ (1).", "E", wp=True),
W("A $\\frac34$ m long ribbon is cut into pieces each $\\frac18$ m long. How many pieces are obtained?", 2, "Pieces $=\\frac34\\div\\frac18=\\frac34\\times8$ (1) $=6$ pieces (1).", "E", wp=True),
W("A recipe needs $2.375$ kg of flour. Write $2.375$ in the form $\\frac pq$ in the simplest form.", 2, "$2.375=\\frac{2375}{1000}$ (1) $=\\frac{19}{8}$ (1).", "E", wp=True),
W("A bus stop is $\\frac34$ km from the school gate along a straight road. Into how many equal parts would you divide the first kilometre of the number line, and which mark gives the bus stop?", 2, "Divide the unit length into $4$ equal parts (1) and take the $3$rd mark from $0$ (1).", "E", wp=True),
W("Name the smallest set among $\\mathbb N$, $\\mathbb W$, $\\mathbb Z$, $\\mathbb Q$ that contains each number: $0$, $-7$, $\\frac53$, $12$.", 2, "$0\\in\\mathbb W$; $-7\\in\\mathbb Z$; $\\frac53\\in\\mathbb Q$; $12\\in\\mathbb N$. (Half mark each)", "E"),
W("True or false (give an example): the set of natural numbers is closed under subtraction.", 1, "**False.** For example $3-5=-2$, which is not a natural number. (1)", "E"),
W("Without dividing, say whether the decimals of $\\frac7{20}$, $\\frac5{12}$ and $\\frac9{40}$ terminate.", 2, "$20=2^2\\times5$ and $40=2^3\\times5$ have only the factors $2,5$, so $\\frac7{20}$ and $\\frac9{40}$ terminate (1). $12=2^2\\times3$ has the factor $3$, so $\\frac5{12}$ does not terminate (1).", "E"),
W("Write $0.444\\dots$ in the form $\\frac pq$.", 2, "Let $x=0.444\\dots$; $10x=4.444\\dots$ (1). $9x=4$, so $x=\\frac49$ (1).", "E"),
W("Ravi walks $\\frac25$ km to school and Sheela walks $\\frac3{10}$ km. Who walks farther, by how much, and what is their total walk in decimals?", 2, "$\\frac25=\\frac4{10}>\\frac3{10}$, so Ravi walks farther by $\\frac1{10}=0.1$ km (1). Total $=\\frac7{10}=0.7$ km (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("Evaluate using Brahmagupta's rules for fortunes and debts: (i) $(-5)\\times(-4)$ (ii) $(-6)\\times7$ (iii) $0-(-9)$ (iv) $(-12)\\div(-3)$.", 3, "(i) debt $\\times$ debt $=$ fortune: $20$ (ii) debt $\\times$ fortune $=$ debt: $-42$ (iii) $0-(-9)=9$ (iv) $4$. (Marks: $1,1,\\frac12,\\frac12$)", "M"),
W("A water tank is $\\frac58$ full. Water equal to $\\frac14$ of the tank is used. What fraction of the tank is left? Write it as a decimal and as a percentage.", 3, "Left $=\\frac58-\\frac14=\\frac58-\\frac28=\\frac38$ (1). Decimal $=0.375$ (1). Percentage $=37.5\\%$ (1).", "M", wp=True),
W("Find three rational numbers between $\\frac25$ and $\\frac35$.", 2, "Write $\\frac25=0.4$ and $\\frac35=0.6$ (1). Three rationals between them: $0.45$, $0.5$, $0.55$ i.e. $\\frac9{20},\\frac12,\\frac{11}{20}$ (1).", "M"),
W("Express $0.363636\\dots$ in the form $\\frac pq$.", 2, "$x=0.3636\\dots$; $100x=36.3636\\dots$ (1). $99x=36$, $x=\\frac{36}{99}=\\frac4{11}$ (1).", "M"),
W("Express $0.2333\\dots$ in the form $\\frac pq$.", 3, "$x=0.2333\\dots$; $10x=2.333\\dots$ and $100x=23.333\\dots$ (1). Subtract: $90x=21$ (1). $x=\\frac{21}{90}=\\frac7{30}$ (1).", "M"),
W("Without long division, decide which of $\\frac7{80}$, $\\frac{11}{30}$ and $\\frac{13}{125}$ have terminating decimals and write the terminating ones.", 3, "$80=2^4\\times5$, so $\\frac7{80}=0.0875$ terminates (1). $30=2\\times3\\times5$ has the factor $3$, so $\\frac{11}{30}$ does not terminate (1). $125=5^3$, so $\\frac{13}{125}=0.104$ terminates (1).", "M"),
W("A tailor has $5.25$ m of cloth and cuts pieces $0.75$ m long. Write both lengths as fractions and find the number of pieces.", 2, "$5.25=\\frac{21}4$ and $0.75=\\frac34$ (1). Pieces $=\\frac{21}{4}\\div\\frac34=7$ (1).", "M", wp=True),
W("Asha claims that the product or sum of two irrational numbers is always irrational. Disprove her claim with one example for each.", 3, "Product: $\\sqrt3\\times\\sqrt3=3$, which is rational (1). Sum: $(3+\\sqrt2)+(3-\\sqrt2)=6$, which is rational (1). Both $\\sqrt3$ and $3\\pm\\sqrt2$ are irrational, so the claim is false (1).", "M"),
W("Classify each number as rational or irrational with a reason: $\\sqrt{49}$, $\\sqrt{20}$, $0.1010010001\\dots$, $\\frac{22}7$, $3.14159$, $\\pi$.", 3, "$\\sqrt{49}=7$: rational. $\\sqrt{20}=2\\sqrt5$: irrational. $0.1010010001\\dots$ non-terminating, non-repeating: irrational. $\\frac{22}7$: rational. $3.14159$ terminates: rational. $\\pi$: irrational. (Half mark each)", "M"),
W("A square floor has an area of $50$ m². Is the side length rational? Find the side to two decimal places and say why the exact value cannot be written as a decimal. What would the side be if the area were $49$ m²?", 3, "Side $=\\sqrt{50}=5\\sqrt2$, which is irrational (1). $\\approx7.07$ m, because its decimal never ends or repeats (1). For $49$ m² the side is $7$ m, a rational number (1).", "M", wp=True),
W("The diameter of a circular pond is $14$ m. Find its circumference using $\\pi\\approx\\frac{22}7$. Is the answer exact? Explain, mentioning Āryabhaṭa's word for such values.", 3, "$C=\\pi d\\approx\\frac{22}7\\times14=44$ m (1). It is not exact because $\\pi$ is irrational and $\\frac{22}7=3.142857\\dots$ is only an approximation (1). Āryabhaṭa called such a value *āsanna* (approximate) (1).", "M", wp=True),
W("Given that $\\sqrt3$ is irrational, prove that $2+\\sqrt3$ is irrational.", 3, "Suppose $2+\\sqrt3=r$, a rational number (1). Then $\\sqrt3=r-2$, which is rational (difference of rationals) (1). This contradicts $\\sqrt3$ being irrational, so $2+\\sqrt3$ is irrational (1).", "M"),
W("Explain how to locate $\\sqrt2$ and then $\\sqrt3$ on the number line using right triangles.", 3, "Draw a unit square on $[0,1]$; its diagonal is $\\sqrt{1^2+1^2}=\\sqrt2$; swing it with a compass from $0$ onto the line to mark $\\sqrt2$ (1). At that point raise a perpendicular of length $1$ (1). The hypotenuse of the triangle with legs $\\sqrt2$ and $1$ is $\\sqrt3$; swing it onto the line (1).", "M"),
W("Rohan knows that $\\frac17=0.\\overline{142857}$. Without dividing, write $\\frac27$ and $\\frac37$ using the same digits, and find the $100$th digit after the decimal point in $\\frac17$.", 3, "$\\frac27=0.\\overline{285714}$ and $\\frac37=0.\\overline{428571}$ (the same digits rotated) (1). The block has $6$ digits (1). $100=6\\times16+4$, so the $100$th digit is the $4$th digit of the block, which is $8$ (1).", "M", wp=True),
W("Is the set $\\{0,1\\}$ closed under addition? Under multiplication? Give reasons.", 2, "Not closed under addition: $1+1=2\\notin\\{0,1\\}$ (1). Closed under multiplication: $0\\times0=0$, $0\\times1=0$, $1\\times1=1$ (1).", "M"),
W("The lowest night temperatures (in °C) of a hill station on five days were $-2,-5,0,-7,-3$. Find the mean temperature as a rational number in the form $\\frac pq$ and as a decimal, and name the coldest day by number.", 3, "Sum $=-2-5+0-7-3=-17$ (1). Mean $=\\frac{-17}5=-3.4^\\circ$C (1). Coldest is day $4$ ($-7^\\circ$C) (1).", "M", wp=True),
W("Meera has a ribbon $2.4$ m long and cuts it into pieces each $\\frac3{10}$ m long. How many pieces does she get? Show the working with fractions.", 2, "$2.4=\\frac{12}5$ (1). $\\frac{12}5\\div\\frac3{10}=\\frac{12}5\\times\\frac{10}3=8$ pieces (1).", "M", wp=True),
W("Verify the distributive law $a(b+c)=ab+ac$ for $a=-\\frac23$, $b=\\frac34$, $c=\\frac12$.", 3, "$b+c=\\frac54$, so $a(b+c)=-\\frac23\\times\\frac54=-\\frac56$ (1). $ab=-\\frac12$ and $ac=-\\frac13$ (1). $ab+ac=-\\frac56$, so both sides are equal (1).", "M"),
W("A student measures the diagonal of a unit square as $1.4$ and says it is exactly $\\frac{14}{10}$. Show by squaring that this is not exact, and find which of $1.41$ and $1.414$ is the better approximation of $\\sqrt2$.", 3, "$1.4^2=1.96\\ne2$, so $1.4$ is not exact (1). $1.41^2=1.9881$ and $1.414^2=1.999396$ (1). $1.414$ is closer to $2$, so it is the better approximation; no fraction squares to exactly $2$ since $\\sqrt2$ is irrational (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Prove that $\\sqrt3$ is irrational.", 4, "Assume $\\sqrt3=\\frac pq$ with $p,q$ integers and no common factor, $q\\ne0$ (1). Squaring: $3q^2=p^2$, so $3$ divides $p^2$ and therefore $3$ divides $p$; write $p=3k$ (1). Then $3q^2=9k^2$, $q^2=3k^2$, so $3$ divides $q$ (1). Then $3$ is a common factor of $p$ and $q$, contradicting the assumption; so $\\sqrt3$ is irrational (1).", "H"),
W("Given that $\\sqrt5$ is irrational, show that $3+2\\sqrt5$ is irrational.", 3, "Suppose $3+2\\sqrt5=r$ is rational (1). Then $\\sqrt5=\\frac{r-3}2$, which is rational (1). This contradicts the irrationality of $\\sqrt5$, so $3+2\\sqrt5$ is irrational (1).", "H"),
W("Express $1.272727\\dots$ in the form $\\frac pq$ in lowest terms and verify your answer by division.", 4, "$x=1.2727\\dots$; $100x=127.2727\\dots$ (1). $99x=126$ (1). $x=\\frac{126}{99}=\\frac{14}{11}$ (1). Check: $14\\div11=1.2727\\dots$ (1).", "H"),
W("Find the $50$th digit after the decimal point in $\\frac57=0.\\overline{714285}$ and the sum of the digits in one full block. How many complete blocks are in the first $50$ digits?", 3, "Block length $6$; $50=6\\times8+2$, so $8$ complete blocks (1). The $50$th digit is the $2$nd digit of the block, which is $1$ (1). Digit sum $=7+1+4+2+8+5=27$ (1).", "H"),
W("(i) Find an irrational number between $\\frac25$ and $\\frac12$. (ii) Find a rational number between $\\sqrt2$ and $\\sqrt3$. Give reasons.", 4, "(i) $\\frac25=0.4$ and $\\frac12=0.5$; $0.41010010001\\dots$ is non-terminating, non-repeating (irrational) and lies between them (2). (ii) $\\sqrt2\\approx1.414$ and $\\sqrt3\\approx1.732$; $1.5=\\frac32$ lies between and is rational (2).", "H"),
W("A square garden has an area of $200$ m². Find the length of its side in surd form and, using $\\sqrt2=1.414$, the length of fencing needed and its cost at ₹ $50$ per metre.", 4, "Side $=\\sqrt{200}=10\\sqrt2$ m (1). Perimeter $=40\\sqrt2=40\\times1.414=56.56$ m (2). Cost $=56.56\\times50=$ ₹ $2828$ (1).", "H", wp=True),
W("State whether each is rational or irrational: (i) $(2+\\sqrt3)+(2-\\sqrt3)$ (ii) $(\\sqrt5+2)(\\sqrt5-2)$ (iii) $3\\sqrt2\\times2\\sqrt2$ (iv) $\\frac{\\sqrt2}{\\sqrt8}$ (v) $(\\sqrt3+1)^2$.", 4, "(i) $4$: rational. (ii) $5-4=1$: rational. (iii) $6\\times2=12$: rational. (iv) $\\sqrt{\\frac28}=\\frac12$: rational. (v) $3+2\\sqrt3+1=4+2\\sqrt3$: irrational. (Marks: $1,1,1,\\frac12,\\frac12$)", "H"),
W("For which of the denominators $n=8,12,15,25,40,45$ does $\\frac7n$ have a terminating decimal? Write the decimals for those that do and give the number of decimal places.", 4, "Terminating only if $n$ has no prime factors other than $2$ and $5$: $n=8,25,40$ (2). $\\frac78=0.875$ ($3$ places), $\\frac7{25}=0.28$ ($2$ places), $\\frac7{40}=0.175$ ($3$ places) (2). Others have a factor $3$.", "H"),
W("A merchant has $3$ fortunes of ₹ $400$ each and $5$ debts of ₹ $250$ each. (i) Using signed numbers find his net worth. (ii) A friend cancels (takes away) a debt of ₹ $50$ from him; what is his worth now? Use Brahmagupta's rules.", 4, "(i) $3\\times400+5\\times(-250)=1200-1250=-50$, a debt of ₹ $50$ (2). (ii) $-50-(-50)=0$: taking away a debt of $50$ from a debt of $50$ leaves zero (2).", "H", wp=True),
W("Show that $0.999\\dots=1$ and explain why this means that $0.999\\dots$ is a rational number.", 3, "Let $x=0.999\\dots$; $10x=9.999\\dots$ (1). Subtract: $9x=9$, so $x=1$ (1). It equals $1=\\frac11$, which is of the form $\\frac pq$, so it is rational (1).", "H"),
W("The decimal expansion of $\\frac1{13}$ is $0.\\overline{076923}$. Use the cyclic pattern to write $\\frac3{13}$ and $\\frac4{13}$ without division, and verify one of them by multiplying the block by the numerator.", 4, "Multiplying the block by $3$: $3\\times76923=230769$, so $\\frac3{13}=0.\\overline{230769}$ (2). $4\\times76923=307692$, so $\\frac4{13}=0.\\overline{307692}$ (2). Both are rotations of $076923$.", "H"),
W("In the square-root spiral, the first right triangle has legs $1$ and $1$; each new triangle has legs equal to the previous hypotenuse and $1$. (i) Write the hypotenuses of the first four triangles. (ii) Find the area of the fourth triangle. (iii) Write the hypotenuse of the $n$th triangle.", 4, "(i) $\\sqrt2,\\sqrt3,\\sqrt4=2,\\sqrt5$ (1). (ii) Fourth triangle has legs $\\sqrt4=2$ and $1$, area $=\\frac12\\times2\\times1=1$ (2). (iii) $\\sqrt{n+1}$ (1).", "H", wp=True),
W("Ritu measures the diagonal of a square tile of side $30$ cm as $42.4$ cm. Sana calculates it using $\\sqrt2=1.414$. (i) Write the exact diagonal. (ii) Find Sana's value. (iii) Explain, using the nature of $\\sqrt2$, why a ruler can never give the exact diagonal as a finite decimal.", 4, "(i) Diagonal $=30\\sqrt2$ cm (1). (ii) $30\\times1.414=42.42$ cm (1). (iii) $\\sqrt2$ is irrational: its decimal expansion neither terminates nor repeats, so any measured or calculated decimal is only an approximation ($30\\sqrt2\\approx42.4264$) (2).", "H", wp=True),
]

for _w in WS:   # answer-key/question renderer does not interpret **bold**
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(3)
_pre, _tail = _o["blocks"][:-2], _o["blocks"][-2:]
_extra = [
 ("h2", "3.5 Zero and Brahmagupta's Rules"),
 ("p", "In the Bakhśhālī manuscript, dated to the early centuries CE, a bold dot (bindu) stands for zero. It was Brahmagupta (Brāhmasphuṭasiddhānta, 628 CE) who treated zero and negative quantities as numbers with rules, using *fortunes* (positive) and *debts* (negative)."),
 ("table", ["Brahmagupta's rule", "In modern signs", "Example"], [
  ["sum of two fortunes is a fortune", "(+a) + (+b) = +(a + b)", "5 + 3 = 8"],
  ["sum of two debts is a debt", "(−a) + (−b) = −(a + b)", "−4 + (−6) = −10"],
  ["sum of a fortune and a debt is their difference, with the sign of the larger", "(+a) + (−b)", "7 + (−10) = −3"],
  ["a debt subtracted from zero is a fortune", "0 − (−a) = +a", "0 − (−9) = 9"],
  ["taking away a debt increases the fortune", "a − (−b) = a + b", "7 − (−3) = 10"],
  ["product of two debts is a fortune", "(−a) × (−b) = +ab", "(−5) × (−4) = 20"],
  ["product of a debt and a fortune is a debt", "(−a) × (+b) = −ab", "(−6) × 7 = −42"],
  ["a number minus itself is zero", "a − a = 0", "−50 − (−50) = 0"]]),
 ("note", "REMEMBER", "Division by zero is **not defined**: if 5 ÷ 0 = x then 0 × x = 5, which no number satisfies. Dividing 0 by a non-zero number gives 0."),
 ("h2", "3.6 Worked Examples"),
 ("steps", [("Example 1 — Fortunes and debts", "A shopkeeper owes ₹ 350 (−350), receives ₹ 500 and pays ₹ 400 rent. Balance = −350 + 500 − 400 = **−250**, a debt of ₹ 250. A merchant with 3 fortunes of ₹ 400 and 5 debts of ₹ 250 has 1200 − 1250 = **−50**.")]),
 ("steps", [("Example 2 — Repeating decimal with a non-repeating start", "x = 0.2333…: 10x = 2.333…, 100x = 23.333…. Subtract: 90x = 21, so **x = 7/30**. Rule: multiply by 10 to move the non-repeating digits, by 100 (10ⁿ for a block of n digits) to move one block, then subtract. For 1.2727…: 100x − x = 126, so x = 126/99 = **14/11**.")]),
 ("steps", [("Example 3 — Does the decimal terminate?", "Reduce to lowest terms first, then factorise the denominator. 7/80: 80 = 2⁴ × 5, so it terminates, and 7/80 = **0.0875** (4 places). 11/30: 30 contains 3, so the decimal repeats. 13/125: 125 = 5³, so **0.104** (3 places).")]),
 ("steps", [("Example 4 — A word problem with fractions", "A 2.4 m ribbon is cut into pieces of 3/10 m. Convert: 2.4 = 12/5. Pieces = 12/5 ÷ 3/10 = 12/5 × 10/3 = **8**. A tank 5/8 full loses 1/4: 5/8 − 2/8 = 3/8 = 0.375 = 37.5 %.")]),
 ("steps", [("Example 5 — Proof by contradiction (√3)", "Assume √3 = p/q in lowest terms. Then 3q² = p², so 3 | p; put p = 3k. Then q² = 3k², so 3 | q. Both are divisible by 3: contradiction. So **√3 is irrational**. The same argument works for any prime in place of 3, but not for 4 (√4 = 2 is rational).")]),
 ("steps", [("Example 6 — Rational + irrational", "Prove 2 + √3 is irrational. If 2 + √3 = r (rational) then √3 = r − 2 is rational, a contradiction. In the same way **3 + 2√5** is irrational, because √5 = (r − 3)/2 would be rational.")]),
 ("h2", "3.7 Cyclic Numbers and Long Division"),
 ("p", "When a fraction p/q is divided out, only q possible remainders can occur, so the remainders must repeat within q steps and the decimal repeats. For 1/7 the block has length 6: 0.142857 142857… and multiples of 1/7 use the **same digits rotated**: 2/7 = 0.285714…, 3/7 = 0.428571…, 5/7 = 0.714285…. Similarly 1/13 = 0.076923… and 3 × 76923 = 230769, so 3/13 = 0.230769…. To find the kth digit, divide k by the block length: the remainder tells which digit of the block to take (for 1/7 the 100th digit: 100 = 6 × 16 + 4, the 4th digit is **8**)."),
 ("h2", "3.8 More on Irrational Numbers and π"),
 ("ul", ["**Square-root spiral:** start with a right triangle with legs 1 and 1 (hypotenuse √2). Each new triangle has legs equal to the last hypotenuse and 1, so the hypotenuses are √2, √3, 2, √5, … and the nth is **√(n + 1)**.", "**Surds in word problems:** a square floor of area 50 m² has side 5√2 ≈ 7.07 m; a square garden of area 200 m² has side 10√2 and perimeter 40√2 ≈ 56.56 m (taking √2 = 1.414). A measurement can only be a rational approximation of an irrational length.", "**π:** the ratio of the circumference of a circle to its diameter is irrational. Āryabhaṭa (499 CE) gave 3927/1250 = 3.1416 and called it āsanna, an approximation; 22/7 = 3.142857… is another approximation. Madhava later gave an infinite series for π.", "0.999… = 1 (let x = 0.999…, then 9x = 9), so it is a rational number; recurring nines do not give a new number."]),
 ("table", ["Expression", "Result", "Type"], [
  ["(2 + √3) + (2 − √3)", "4", "rational"],
  ["(√5 + 2)(√5 − 2)", "5 − 4 = 1", "rational"],
  ["3√2 × 2√2", "12", "rational"],
  ["√2 / √8", "1/2", "rational"],
  ["(√3 + 1)²", "4 + 2√3", "irrational"],
  ["2 + √3", "—", "irrational (rational + irrational)"]]),
 ("note", "REMEMBER", "**Common mistakes.** (1) Calling 3.14159 or 22/7 irrational: both are rational (π is irrational). (2) Saying √16 or √49 is irrational. (3) Forgetting to reduce a fraction to lowest terms before testing whether its decimal terminates (e.g. 21/60 = 7/20 terminates). (4) Saying the sum or product of two irrational numbers is always irrational. (5) Subtracting wrongly when a debt is taken away: 7 − (−3) = 10, not 4. (6) Writing the digit position of a repeating block without using the remainder after division by the block length."),
]
CH = dict(_o, blocks=_pre + _extra + _tail, takeaways=_o["takeaways"] + ["**Brahmagupta's rules:** debt × debt = fortune, debt × fortune = debt, and taking away a debt increases the fortune; division by zero is undefined.", "To convert 0.2333… or 1.2727…, multiply by 10ⁿ for the **block** and also to clear the non-repeating start, then subtract.", "The kth digit of a repeating block: divide k by the block length and use the **remainder** as the position.", "A rational + an irrational is irrational (proof by contradiction), but two irrationals can give a rational: (2 + √3) + (2 − √3) = 4.", "Lengths such as √2 or π can only be measured **approximately**; Āryabhaṭa called such a value āsanna."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
