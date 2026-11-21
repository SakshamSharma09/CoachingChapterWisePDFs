"""Class 8 Maths Ch 1 - A Square and a Cube: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch01"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# quick sanity checks on the numbers used below
assert 1521 == 39**2 and 2304 == 48**2 and 4096 == 64**2 and 15**3 == 3375 and 12**3 == 1728
assert 6084 == 78**2 and 14**2 + 48**2 == 50**2 and 12**2 + 35**2 == 37**2 and 21+23+25+27+29 == 125
assert 84**2 == 7056 and 24**3 == 13824 and 3**3 + 4**3 + 5**3 == 6**3 and 9**3 + 15**3 == 4104 == 2**3 + 16**3
assert 7744 == 88**2 and 59**2 == 3481 and 5832 == 18**3

WS = [
# ---------------- EASY ----------------
W("Which of these numbers can **not** be a perfect square?", 1, "(c) 3,872. A perfect square never ends in 2, 3, 7 or 8, and 3,872 ends in 2. (1)", "E",
  opts=["1,521", "2,304", "3,872", "4,096"]),
W("The sum of the first 12 odd natural numbers, found without adding, is:", 1, "(c) 144. The sum of the first $n$ odd numbers is $n^2$, so $12^2=144$. (1)", "E",
  opts=["24", "121", "144", "156"]),
W("How many natural numbers lie between $24^2$ and $25^2$?", 1, "(c) 48. Between $n^2$ and $(n+1)^2$ there are $2n$ numbers: $2\\times24=48$. (1)", "E",
  opts=["24", "25", "48", "49"]),
W("The cube root of 3,375 is:", 1, "(b) 15. $15\\times15\\times15=3375$ (ends in 5, so the root ends in 5; $10^3=1000<3375<20^3$). (1)", "E",
  opts=["13", "15", "25", "55"]),
W("Which of the following is a Pythagorean triplet?", 1, "(a) $(5,12,13)$ because $25+144=169=13^2$. In the others $36+64\\ne144$, $49+576\\ne676$ and $81+144\\ne256$. (1)", "E",
  opts=["(5, 12, 13)", "(6, 8, 12)", "(7, 24, 26)", "(9, 12, 16)"]),
W("The smallest number that can be written as the sum of two cubes in two different ways is:", 1, "(b) 1,729 $=1^3+12^3=9^3+10^3$ (the Hardy–Ramanujan number). (1)", "E",
  opts=["1,331", "1,729", "2,197", "4,104"]),
W("The units digit of $38^3$ is:", 1, "(a) 2. The units digit of the cube depends on the units digit of the number: $8^3=512$ ends in 2. (1)", "E",
  opts=["2", "4", "6", "8"]),
W("A square courtyard is covered with 529 identical square tiles. How many tiles are laid in each row?", 2, "Tiles in each row = $\\sqrt{529}$. $529=23\\times23$ (1). So there are **23 tiles** in each row (1).", "E", wp=True),
W("A square garden has area 225 m². Find the cost of fencing it at ₹ 40 per metre.", 2, "Side $=\\sqrt{225}=15$ m, perimeter $=4\\times15=60$ m (1). Cost $=60\\times40=$ **₹ 2,400** (1).", "E", wp=True),
W("Without adding, find $1+3+5+7+\\dots$ up to 15 terms.", 1, "The sum of the first 15 odd numbers $=15^2=$ **225** (1).", "E"),
W("Find the cube root of 1,728 by prime factorisation.", 2, "$1728=2^6\\times3^3=(2\\times2\\times3)^3$ (1). So $\\sqrt[3]{1728}=2^2\\times3=$ **12** (1).", "E"),
W("True or false (give a reason): the square of an odd number is always odd.", 1, "**True.** An odd number has no factor 2, so its square has none either (e.g. $7^2=49$) (1).", "E"),
W("Write $7^2$ as the sum of consecutive odd numbers starting from 1.", 2, "$7^2=1+3+5+7+9+11+13$ (seven odd numbers) (1) $=49$ (1).", "E"),
W("A cubical water tank has an edge of 4 m. Find its volume and the number of litres it holds (1 m³ = 1,000 L).", 2, "Volume $=4^3=64$ m³ (1). Capacity $=64\\times1000=$ **64,000 L** (1).", "E", wp=True),
W("Use the pattern for numbers ending in 5 to find $35^2$ and $95^2$.", 2, "$35^2=(3\\times4)\\,|\\,25=1225$ (1). $95^2=(9\\times10)\\,|\\,25=9025$ (1).", "E"),
W("Without calculating, say which of 1,237; 4,225; 7,788; 9,000 can be perfect squares. Give a reason for each rejection.", 2, "Only **4,225** can be (it is $65^2$) (1). 1,237 and 7,788 end in 7 and 8 (a square never does); 9,000 has an odd number (3) of zeros (1).", "E"),
W("A sweet box is a cube of volume 343 cm³. Find the length of its edge and the area of one face.", 2, "Edge $=\\sqrt[3]{343}=7$ cm (1). Area of one face $=7^2=$ **49 cm²** (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("Find the smallest number by which 1,512 must be multiplied to get a perfect cube. What is the cube root of the product?", 2, "$1512=2^3\\times3^3\\times7$; the prime 7 appears once (1). Multiply by $7\\times7=$ **49** to get $2^3\\times3^3\\times7^3=74088=42^3$, so the cube root is **42** (1).", "M"),
W("Find the smallest number by which 2,925 must be divided so that the quotient is a perfect square. Find the square root of the quotient.", 2, "$2925=3^2\\times5^2\\times13$; 13 is unpaired (1). Divide by **13**: quotient $225=15^2$, root **15** (1).", "M"),
W("For a school function 2,000 students are to stand in a square formation (as many rows as students in a row). How many more students are needed to complete the square? How many in each row then?", 2, "$44^2=1936<2000<45^2=2025$ (1). More students needed $=2025-2000=$ **25**; **45** in each row (1).", "M", wp=True),
W("A square park has an area of 6,084 m². Rohan jogs 3 times round its boundary. How far does he jog?", 3, "Side $=\\sqrt{6084}=78$ m ($6084=2^2\\times3^2\\times13^2$) (1). Perimeter $=4\\times78=312$ m (1). Distance $=3\\times312=$ **936 m** (1).", "M", wp=True),
W("Find a Pythagorean triplet whose smallest member is 14.", 2, "Use $(2m,\\,m^2-1,\\,m^2+1)$ with $2m=14$, $m=7$ (1): $(14,\\,48,\\,50)$. Check: $196+2304=2500=50^2$ (1).", "M"),
W("Find a Pythagorean triplet whose largest member is 37.", 2, "$m^2+1=37\\Rightarrow m=6$ (1). Triplet $(2m,m^2-1,m^2+1)=(12,35,37)$; $144+1225=1369=37^2$ ✓ (1).", "M"),
W("A 25 m ladder reaches a window 24 m above the ground. Using a Pythagorean triplet, find how far the foot of the ladder is from the wall.", 2, "Ladder is the hypotenuse; $(7,24,25)$ is a triplet since $49+576=625$ (1). Distance **7 m** (1).", "M", wp=True),
W("Write $5^3$ as the sum of five consecutive odd numbers and verify.", 2, "$5^3=21+23+25+27+29$ (1). Check: $21+23+25+27+29=125$ ✓ (1).", "M"),
W("Find $\\sqrt{7056}$ by prime factorisation.", 2, "$7056=2^4\\times3^2\\times7^2$ (1). Take one prime from each pair: $2^2\\times3\\times7=$ **84** (1).", "M"),
W("Find $\\sqrt[3]{13824}$ by prime factorisation.", 2, "$13824=2^9\\times3^3$ (1). Groups of three: $2^3\\times3=$ **24** (1).", "M"),
W("A cube-shaped godown has volume 3,375 m³. Find its height, the area of its floor and the total area of its four walls.", 3, "Edge $=\\sqrt[3]{3375}=15$ m (1). Floor $=15^2=225$ m² (1). Four walls $=4\\times225=$ **900 m²** (1).", "M", wp=True),
W("A square plot of area 1,764 m² is divided into 4 equal square plots by two fences that cross at the centre and run from side to side. Find the total length of fencing used inside.", 3, "Side $=\\sqrt{1764}=42$ m ($1764=2^2\\times3^2\\times7^2$) (1). Each dividing fence is 42 m long (1). Two fences: $2\\times42=$ **84 m** (1).", "M", wp=True),
W("Find the smallest square number that is divisible by each of 4, 6 and 10.", 3, "LCM$(4,6,10)=60=2^2\\times3\\times5$ (1). 3 and 5 are unpaired; multiply by $3\\times5=15$ (1). Smallest square $=60\\times15=$ **900** $=30^2$ (1).", "M"),
W("How many non-square numbers lie between $40^2$ and $41^2$? Explain why.", 2, "There are $2\\times40=$ **80** numbers (1) because $41^2-40^2=2\\times40+1=81$, which leaves 80 numbers strictly between; none is a perfect square as squares of consecutive numbers are 81 apart (1).", "M"),
W("Mohan writes $\\sqrt{144+25}=12+5=17$. Find his mistake and give the correct value.", 2, "$\\sqrt{a+b}\\ne\\sqrt a+\\sqrt b$ (1). Correct: $\\sqrt{169}=$ **13** (1).", "M"),
W("True or false (give a reason): the cube of an even number is odd.", 2, "**False** (1). An even number has a factor 2, so its cube has $2^3$; e.g. $4^3=64$ is even (1).", "M"),
W("Find the smallest number by which 1,125 must be divided so that the quotient is a perfect cube. Find the cube root of the quotient.", 2, "$1125=3^2\\times5^3$; the prime 3 occurs only twice (1). Divide by $9$: quotient $125=5^3$, cube root **5** (1).", "M"),
W("Anita has a chessboard-like pattern of $24\\times24$ small squares. She adds one row and one column to make it $25\\times25$. How many small squares are added? Which rule does this show?", 2, "$25^2-24^2=625-576=$ **49** (1). Rule: $(n+1)^2-n^2=2n+1=2\\times24+1=49$ (1).", "M", wp=True),
W("Find the smallest 4-digit perfect square and the greatest 4-digit perfect cube.", 3, "$31^2=961$ (3-digit), $32^2=$ **1,024** is the smallest 4-digit square (1). $21^3=9261$ and $22^3=10648$ (5-digit) (1), so the greatest 4-digit cube is **9,261** (1).", "M"),
# ---------------- HARD ----------------
W("Show that 4,104 can be written as a sum of two cubes in two different ways (a number like 1,729).", 3, "$2^3+16^3=8+4096=4104$ (1). $9^3+15^3=729+3375=4104$ (1). Both give 4,104, so it is the sum of two cubes in two ways (1).", "H"),
W("A park is a rectangle 40 m long and 9 m wide. Savita walks from one corner to the opposite corner along the diagonal instead of along two sides. Using a Pythagorean triplet, find how much distance she saves.", 3, "$(9,40,41)$ is a triplet since $81+1600=1681=41^2$ (1). Diagonal $=41$ m (1). Along two sides $=49$ m, so she saves $49-41=$ **8 m** (1).", "H", wp=True),
W("Find the smallest perfect cube that is divisible by both 20 and 50.", 3, "LCM$=100=2^2\\times5^2$ (1). To make a cube each prime needs a power of 3: multiply by $2\\times5=10$ (1). Smallest cube $=1000=10^3$ (1).", "H"),
W("A cube of side 12 cm is painted green on all faces and then cut into 1 cm cubes. How many small cubes are there in all, and how many have **no** face painted?", 4, "Total $=12^3=$ **1,728** (2). Unpainted cubes form an inner $10\\times10\\times10$ cube (one layer removed from each side): $10^3=$ **1,000** (2).", "H", wp=True),
W("The $n$th triangular number is $T_n=\\dfrac{n(n+1)}{2}$. Prove that the sum of two consecutive triangular numbers is a perfect square, and check it for $T_9+T_{10}$.", 4, "$T_n+T_{n+1}=\\dfrac{n(n+1)}{2}+\\dfrac{(n+1)(n+2)}{2}=\\dfrac{(n+1)(2n+2)}{2}=(n+1)^2$ (3). $T_9+T_{10}=45+55=100=10^2$ ✓ (1).", "H"),
W("Check that $1^3+2^3+3^3+4^3=10^2$. Use the pattern to write down $1^3+2^3+\\dots+10^3$ without adding.", 4, "$1+8+27+64=100=10^2$, and $10=1+2+3+4$ (2). Pattern: the sum of the first $n$ cubes is $(1+2+\\dots+n)^2$. For $n=10$: $1+2+\\dots+10=55$, so the sum is $55^2=$ **3,025** (2).", "H"),
W("Three metal cubes of edges 3 cm, 4 cm and 5 cm are melted and recast into one cube. Find the edge of the new cube. (No metal is lost.)", 3, "Total volume $=27+64+125=216$ cm³ (1). Edge $=\\sqrt[3]{216}$ (1) $=$ **6 cm** (1).", "H", wp=True),
W("A 4-digit number of the form $aabb$ is a perfect square. Since $aabb=11(100a+b)$, the number $100a+b$ must also be a multiple of 11. Use this to find the number.", 4, "Since $100\\equiv1\\pmod{11}$, $100a+b$ is a multiple of 11 only when $a+b$ is a multiple of 11, so $a+b=11$ (1). Candidates: 2299, 3388, 4477, 5566, 6655, 7744, 8833, 9922 (1). Squares never end in 2, 3, 7 or 8, so 3388, 4477, 8833 and 9922 are out; 5566 ends in 66 but 5566 is not a square (74²=5476, 75²=5625); 6655 ends in 55 (a square ending in 5 ends in 25), so it is out (1). Left: 2299 (between $47^2=2209$ and $48^2=2304$, not a square) and $7744=88^2$ (1). Answer **7744**.", "H"),
W("A cubical box has volume 512 cm³. Its outer surface (all six faces) is to be painted at ₹ 0.50 per cm². Find the cost of painting.", 3, "Edge $=\\sqrt[3]{512}=8$ cm (1). Surface area $=6\\times8^2=384$ cm² (1). Cost $=384\\times0.50=$ **₹ 192** (1).", "H", wp=True),
W("Gita writes $1728=2^6\\times3^3$ and says $\\sqrt[3]{1728}=2\\times3=6$ because ‘one prime is taken from each group’. Find the error and give the correct cube root.", 3, "Cube root takes one prime from **each group of three equal primes**, not each prime (1). $2^6$ has two groups of $2\\times2\\times2$ so it gives $2^2=4$ (1). Correct root $=2^2\\times3=$ **12** (1).", "H"),
W("**Case study.** Hardy told Ramanujan that his taxi number 1729 was ‘dull’. (i) Express 1,729 as a sum of two cubes in two ways. (ii) Is 1,729 itself a perfect cube? Between which two consecutive cubes does it lie? (iii) By how much does it exceed the nearest cube below it?", 4, "(i) $1729=1^3+12^3=9^3+10^3$ (1). (ii) $12^3=1728$ and $13^3=2197$; so 1,729 is **not** a cube and lies between $12^3$ and $13^3$ (2). (iii) $1729-1728=$ **1** (1).", "H", wp=True),
W("A cube of side 20 cm is melted and recast into small cubes of side 5 cm. How many small cubes are formed? Why is the answer not simply $20\\div5=4$?", 3, "Volume of big cube $=8000$ cm³, of a small one $=125$ cm³ (1). Number $=8000\\div125=$ **64** (1). Volume grows as the **cube** of the edge: $(20/5)^3=4^3=64$, not 4 (1).", "H", wp=True),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(1)
_blocks = _o["blocks"][:-1] + [
 ("h2", "1.5 Worked Examples"),
 ("h3", "Example 1 — Square root by prime factorisation"),
 ("steps", [("Find √7056", "Divide by primes: 7056 = 2 × 2 × 2 × 2 × 3 × 3 × 7 × 7."), ("Pair the primes", "(2 × 2)(2 × 2)(3 × 3)(7 × 7): every prime is in a pair, so 7056 is a perfect square."), ("Take one from each pair", "√7056 = 2 × 2 × 3 × 7 = **84**.")]),
 ("h3", "Example 2 — Smallest multiplier to make a perfect cube"),
 ("steps", [("Factorise", "1512 = 2³ × 3³ × 7. The primes 2 and 3 already form groups of three; 7 occurs only once."), ("Complete the group", "Two more 7s are needed: multiply by 7 × 7 = **49**."), ("Check", "1512 × 49 = 74,088 = (2 × 3 × 7)³ = 42³.")]),
 ("h3", "Example 3 — Smallest number to divide by (square)"),
 ("steps", [("Factorise", "2925 = 3 × 3 × 5 × 5 × 13."), ("Find the unpaired prime", "13 has no partner."), ("Divide", "2925 ÷ 13 = 225 = 15². The smallest divisor is **13**.")]),
 ("h3", "Example 4 — Perfect square formed from several numbers"),
 ("steps", [("Smallest square divisible by 4, 6 and 10", "LCM = 60 = 2² × 3 × 5."), ("Pair the unpaired primes", "3 and 5 are single: multiply by 3 × 5 = 15."), ("Answer", "60 × 15 = **900** = 30².")]),
 ("h3", "Example 5 — Pythagorean triplet from a given member"),
 ("steps", [("Smallest member 14 (even)", "Use (2m, m² − 1, m² + 1) with 2m = 14, so m = 7."), ("Find the others", "m² − 1 = 48, m² + 1 = 50."), ("Verify", "14² + 48² = 196 + 2304 = 2500 = 50². Triplet **(14, 48, 50)**.")]),
 ("h3", "Example 6 — Counting with cubes"),
 ("steps", [("Painted cube of side 12 cm cut into 1 cm cubes", "Total small cubes = 12³ = 1,728."), ("Remove the outer layer", "The unpainted cubes form a cube of side 12 − 2 = 10."), ("Unpainted cubes", "10³ = **1,000**; painted cubes = 728.")]),
 ("h2", "1.6 Word Problems: How to Translate"),
 ("table", ["Words in the problem", "Mathematics", "Example"], [
  ["‘as many rows as students in a row’, ‘square formation’", "number = n²; find √", "529 tiles in a square: √529 = 23 per row"],
  ["area of a square field given", "side = √area; perimeter = 4 × side", "area 225 m²: side 15 m, fence 60 m"],
  ["volume of a cubical box/tank given", "edge = ∛volume; one face = edge²; total surface = 6 × edge²", "343 cm³: edge 7 cm, face 49 cm²"],
  ["‘how many more to make a square’", "next perfect square − number", "2000 → 45² = 2025: 25 more"],
  ["ladder / diagonal of a rectangular park", "right triangle: use a Pythagorean triplet", "(9, 40, 41): diagonal of a 9 m × 40 m park is 41 m"],
  ["a cube melted into smaller cubes", "divide volumes (edge ratio cubed)", "edge 20 cm into 5 cm cubes: (20 ÷ 5)³ = 64"]]),
 ("note", "REMEMBER", "Length uses the **square root**, volume uses the **cube root**. Doubling the edge of a cube **multiplies the volume by 8** and the face area by 4, not by 2."),
 ("h2", "1.7 Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["√(144 + 25) = 12 + 5", "root of a sum is not the sum of the roots", "√169 = 13"],
  ["∛1728: 2⁶ × 3³ gives 2 × 3", "one prime is taken from each **group of three**", "2² × 3 = 12"],
  ["3,000 is a square because it ends in 0", "number of end zeros of a square must be even", "3,000 is not a square"],
  ["The square of 15 is 30", "squaring is n × n, not n × 2", "15² = 225"],
  ["The cube of an even number is odd", "2³ factor stays in the product", "4³ = 64 is even"]]),
 _o["blocks"][-1]]
_blocks = [b for b in _blocks if not (b[0] == "h2" and b[1].startswith("Quick Revision"))]
_blocks.insert(len(_blocks) - 1, ("h2", "Quick Revision: Likely Exam Questions"))
CH = dict(_o, blocks=_blocks, takeaways=_o["takeaways"] + ["For word problems: **length needs a square root, volume needs a cube root**; a cube melted into smaller cubes is solved by dividing volumes."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
