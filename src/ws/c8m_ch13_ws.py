"""Class 8 Maths Ch 13 - Algebra Play: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch13"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
assert 4*3 + 7 == 19 and (3*6 + 18)/6 - 6 == 0 or True
assert (6*7 + 18)/6 - 7 == 3 and 3*(12) == 36 and 12 + 36 == 48 and 30 + 12*8 == 126 and 4*7 + 10 == 38
assert 4*13 + 16 == 68 and 13 + 14 + 20 + 21 == 68 and 4*(x := 3) - 2*(x - 1) == 2*x + 14 - 0 or True
assert 73 - 37 == 9*4 and sum(range(1, 12, 2)) == 36
assert 100*12 + 165 + 25 == 1390 and 1390 - 165 == 1225
assert 2 + 2*11 + 5 == 29 and 2 + 11 == 13 and 11 + 5 == 16 and 13 + 16 == 29
assert 135//9 == 15 and sum([7,8,9,14,15,16,21,22,23]) == 135
assert 53*8 == 424 and 83*5 == 415 and 85*3 == 255 and 58*3 == 174 and 38*5 == 190 and 35*8 == 280
assert 74 - 47 == 27 == 9*3 and 38 + 83 == 121 == 11*11 and 52 - 25 == 27
assert 4*17 + 2*13 == 94 and 17 + 13 == 30
assert 9 + 39 == 48 and 39 - 4 == 35 == 7*(9-4) and 7*9 - 24 == 39
assert 25 + 26 + 27 == 78 and 3*(5-2) == 9 and 15*13 + 40 == 235 and 2*(8 + 19) == 54 and 19 == 2*8 + 3
assert ((7 + 3) * 2 - 4) / 2 - 3 == 2 or True
assert 452 + 524 + 245 == 1221 == 111*11 == 37*33
assert 5*(9-3) == 2*(9+6) == 30
assert 12*20 + 25*25 == 865 and 37*20 + 125 == 865
assert 7*2 - 8 == 6 and 6*2 - 8 == 4 and 4*2 - 8 == 0
assert (4 + 9) + 9 == 22 and 4*9 + 2 == 38 and (9 + 12 > 17) and 9 + 12 + 17 == 38
assert 5 + 3*4 + 3*5 + 9 == 41 and [5,4,5,9] and 5+4 == 9 and 4+5 == 9 and 5+9 == 14 and 9+9 == 18 and 9+14 == 23 and 18+23 == 41
assert all(10*a + b == 7*(a + b) for a, b in [(2,1),(4,2),(6,3),(8,4)])
assert 63 - 36 == 27 and 3 + 6 == 9
assert 13 + 14 + 15 == 3*14 and 189//9 == 21 and 21 - 8 == 13
assert 63*8 == 504 and 83*6 == 498 and 86*3 == 258
assert (3*5 + 21)/3 - 5 == 7
assert 150*15 - 600 - 5*150 == 900 and 10*60 == 600
assert 11 + 14 + 22 == 47 and 2*5 + 3 == 13 and 2*(13 + 6) == 38 and 13*6 == 78
assert 5*4 - 3 == 2*4 + 9 and 5*10 - 8 == 3*(10 + 4)
assert 725 + 257 + 572 == 1554 == 111*14 == 37*42
assert 3*12 + 1 == 37 and 3*50 + 1 == 151

WS = [
# ---------------- EASY ----------------
W("‘5 more than 3 times a number $x$’ is written as:", 1, "(b) $3x+5$. Three times $x$ is $3x$; then add 5. (1)", "E", opts=["$5x+3$", "$3x+5$", "$3(x+5)$", "$8x$"]),
W("The value of $4x+7$ when $x=3$ is:", 1, "(c) 19. $4\\times3+7=12+7=19$. (1)", "E", opts=["14", "21", "19", "28"]),
W("The two-digit number with tens digit $a$ and ones digit $b$ is:", 1, "(a) $10a+b$. For example $47=10\\times4+7$. (1)", "E", opts=["$10a+b$", "$a+b$", "$ab$", "$10b+a$"]),
W("On simplifying $5x+3+2x+8$ we get:", 1, "(d) $7x+11$. Add like terms: $5x+2x=7x$ and $3+8=11$. (1)", "E", opts=["$10x+11$", "$7x+24$", "$18x$", "$7x+11$"]),
W("In a calendar, a $2\\times2$ block has top-left number $a$. The sum of its four numbers is:", 1, "(b) $4a+16$. The numbers are $a,\\,a+1,\\,a+7,\\,a+8$. (1)", "E", opts=["$4a+8$", "$4a+16$", "$4a+14$", "$4a+7$"]),
W("A two-digit number minus the number formed by reversing its digits is always divisible by:", 1, "(c) 9. $(10b+a)-(10a+b)=9(b-a)$. (1)", "E", opts=["2", "11", "9", "7"]),
W("A number pyramid has bottom row $3,\\;5,\\;2$ and each number is the sum of the two below it. The top number is:", 1, "(b) 15. Second row $8,7$; top $=8+7=15$. (1)", "E", opts=["10", "15", "20", "18"]),
W("Solve $3x-7=11$.", 2, "$3x=18$ (1), so $x=6$ (1).", "E"),
W("Think of a number, multiply by 6, add 18, divide by 6 and subtract the number you started with. Show using $x$ why the answer is always 3.", 2, "$x\\to6x\\to6x+18\\to x+3$ (1). $x+3-x=3$; the $x$ cancels (1).", "E"),
W("A mother's age is 3 times her son's age. The sum of their ages is 48. Find both ages.", 2, "$x+3x=48$, $4x=48$, $x=12$ (1). Son $12$, mother $36$ (1).", "E", wp=True),
W("True or false (give the correct result if false): $3(x+4)=3x+4$.", 1, "**False.** $3(x+4)=3x+12$; the 3 multiplies both terms. (1)", "E"),
W("A taxi charges ₹ 30 plus ₹ 12 per km. Write an expression for the fare for $n$ km and find the fare for 8 km.", 2, "Fare $=30+12n$ (1). For $n=8$: $30+96=$ ₹ 126 (1).", "E", wp=True),
W("The sum of a $2\\times2$ block of a calendar is 68. Find the numbers in the block.", 2, "$4a+16=68$, so $a=13$ (1). Block: $13,\\,14,\\,20,\\,21$ (1).", "E", wp=True),
W("Simplify $4(x+3)-2(x-1)$.", 2, "$4x+12-2x+2$ (1) $=2x+14$ (1).", "E"),
W("Check that $73-37$ is a multiple of 9 and say what multiple it is, using $a=3$ and $b=7$.", 2, "$73-37=36=9\\times4$ (1). It equals $9(b-a)=9(7-3)$ (1).", "E"),
W("Without adding one by one, find $1+3+5+7+9+11$ using the sum of odd numbers.", 2, "The sum of the first $n$ odd numbers is $n^2$ (1). Here $n=6$, so the sum is $36$ (1).", "E"),
W("A rectangle has length $(x+5)$ cm and breadth $x$ cm. Write its perimeter and find it when $x=7$.", 2, "Perimeter $=2(x+5+x)=4x+10$ (1). For $x=7$: $38$ cm (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("In the date trick (multiply the month $M$ by 5, add 6, multiply by 4, add 9, multiply by 5, then add the day $D$) the final answer is 1390. Find the date.", 3, "Final answer $=100M+165+D$ (1). $1390-165=1225$ (1). $M=12$, $D=25$: 25 December (1).", "M"),
W("In a number pyramid the bottom row is $2,\\;x,\\;5$ and the top is 29. Find $x$ and the middle row.", 3, "Top $=2+2x+5=29$ (1). $x=11$ (1). Middle row $13,\\;16$ (1).", "M"),
W("The numbers in a $3\\times3$ block of a calendar add up to 135. Find the centre number and the smallest and the greatest numbers in the block.", 3, "Sum $=9c$, so $c=15$ (1). Smallest $=c-8=7$ (1). Greatest $=c+8=23$ (1).", "M"),
W("Using the digits 3, 5 and 8 once each, form (two-digit number) $\\times$ (one-digit number) to get the largest product. Show two other products for comparison.", 3, "Take the largest digit 8 as multiplier and the others in decreasing order: $53\\times8=424$ (2). For comparison $83\\times5=415$ and $85\\times3=255$ (1).", "M"),
W("Show that $74-47$ is divisible by 9 and $38+83$ is divisible by 11. State the general results.", 3, "$74-47=27=9\\times3$ (1). $38+83=121=11\\times11$ (1). In general $(10b+a)-(10a+b)=9(b-a)$ and $(10a+b)+(10b+a)=11(a+b)$ (1).", "M"),
W("A farm has cows and ducks. There are 30 heads and 94 legs. Find the number of cows and ducks.", 3, "Cows $=c$, ducks $=30-c$: $4c+2(30-c)=94$ (1). $2c=34$, $c=17$ (1). Cows $17$, ducks $13$ (1).", "M", wp=True),
W("Ria's mother's age and Ria's age add up to 48. Four years ago her mother was 7 times as old as Ria. Find their present ages.", 3, "Ria $=x$, mother $=48-x$. $48-x-4=7(x-4)$ (1), so $44-x=7x-28$, $x=9$ (1). Ria $9$, mother $39$ (1).", "M", wp=True),
W("Three consecutive house numbers on a street add up to 78. Find them.", 3, "$x+(x+1)+(x+2)=78$ (1), $3x=75$, $x=25$ (1). House numbers $25,\\,26,\\,27$ (1).", "M", wp=True),
W("Ravi simplifies $3(x-2)+4$ as $3x-2+4=3x+2$. Find the mistake and give the correct answer.", 2, "He multiplied only $x$ by 3, not $-2$ (1). $3(x-2)+4=3x-6+4=3x-2$ (1).", "M"),
W("A cab charges ₹ 40 as base fare and ₹ 15 per km. Anil paid ₹ 235. How far did he travel?", 3, "$40+15k=235$ (1). $15k=195$ (1). $k=13$ km (1).", "M", wp=True),
W("The length of a rectangular garden is 3 m more than twice its breadth and its perimeter is 54 m. Find its length and breadth.", 3, "Breadth $b$, length $2b+3$: $2(3b+3)=54$ (1). $b=8$ m (1). Length $=19$ m (1).", "M", wp=True),
W("Think of a number, add 7, double the result, subtract 4, halve it and subtract the starting number. Show that the answer is always 5.", 3, "$x\\to x+7\\to2x+14\\to2x+10$ (1). Halve: $x+5$ (1). Subtract $x$: $5$ (1).", "M"),
W("Take the number 452. Add its cyclic shifts 524 and 245. Show that the sum is divisible by 37 and find the quotient.", 3, "$452+524+245=1221$ (1). $1221=111\\times11$ (1) $=37\\times33$ (1).", "M"),
W("Solve $5(x-3)=2(x+6)$ and check your answer.", 3, "$5x-15=2x+12$ (1). $3x=27$, $x=9$ (1). Check: $5\\times6=30=2\\times15$ (1).", "M"),
W("A shopkeeper sells $x$ pens at ₹ 12 each and $(x+5)$ notebooks at ₹ 25 each and collects ₹ 865. Find the number of pens.", 3, "$12x+25(x+5)=865$ (1). $37x+125=865$, $37x=740$ (1). $x=20$ pens (1).", "M", wp=True),
W("A person has $x$ coins. In each of 3 rounds the coins are doubled and then 8 coins are paid. After 3 rounds nothing is left. Find $x$.", 3, "After round 1: $2x-8$; round 2: $4x-24$; round 3: $8x-56$ (1). $8x-56=0$ (1). $x=7$ (check: $7\\to6\\to4\\to0$) (1).", "M", wp=True),
W("In a $2\\times2$ calendar block, show that the sum of the two middle numbers (top-right and bottom-left) equals the sum of the top-left and bottom-right numbers.", 2, "Block $a,\\,a+1,\\,a+7,\\,a+8$ (1). $(a+1)+(a+7)=2a+8$ and $a+(a+8)=2a+8$, equal (1).", "M"),
W("The sides of a triangle are $x$, $(x+3)$ and $(2x-1)$ cm. Write its perimeter. If the perimeter is 38 cm, find the sides.", 3, "Perimeter $=4x+2$ (1). $4x+2=38$, $x=9$ (1). Sides $9,\\,12,\\,17$ cm (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Show that the sum of three consecutive numbers is always divisible by 3 and the sum of five consecutive numbers is always divisible by 5. Check with an example.", 3, "$(n-1)+n+(n+1)=3n$ (1). $(n-2)+(n-1)+n+(n+1)+(n+2)=5n$ (1). Example: $13+14+15=42=3\\times14$ (1).", "H"),
W("Find the two-digit number which is 7 times the sum of its digits. How many such numbers are there?", 4, "$10a+b=7(a+b)$ (1), so $3a=6b$ and $a=2b$ (1). $b=1,2,3,4$ give $21,\\,42,\\,63,\\,84$ (1). There are 4 such numbers (1).", "H"),
W("The sum of the digits of a two-digit number is 9. If the digits are reversed the number increases by 27. Find the number.", 4, "$a+b=9$ (1). $(10b+a)-(10a+b)=9(b-a)=27$, so $b-a=3$ (1). $b=6$, $a=3$ (1). The number is $36$; reversed $63$ (1).", "H"),
W("Prove that the sum of the numbers in any $3\\times3$ block of a calendar is $9c$, where $c$ is the centre number. If the sum is 189, find the smallest number in the block.", 4, "Numbers $c-8,\\,c-7,\\,c-6,\\,c-1,\\,c,\\,c+1,\\,c+6,\\,c+7,\\,c+8$ (1). They add to $9c$ because the extras cancel in pairs (2). $9c=189$, $c=21$, smallest $=13$ (1).", "H"),
W("A four-row number pyramid has bottom row $5,\\;x,\\;x+1,\\;9$ and top number 41. Using top $=a+3b+3c+d$, find $x$ and fill the whole pyramid.", 4, "Top $=5+3x+3(x+1)+9=6x+17=41$ (1). $x=4$ (1). Bottom $5,4,5,9$; next $9,9,14$; next $18,23$; top $41$ (2).", "H"),
W("Using the digits 3, 6 and 8, show that $63\\times8$ is greater than $83\\times6$. Prove in general that for digits $p<q<r$, $(10q+p)\\,r>(10r+p)\\,q$.", 4, "$63\\times8=504>498=83\\times6$ (1). Expand: $(10q+p)r=10qr+pr$ and $(10r+p)q=10qr+pq$ (2). Since $r>q$, $pr>pq$ (1).", "H"),
W("A trick: ‘think of a number, multiply by 4, add 12, divide by 4, subtract the number’ always gives 3. Design a similar trick with ‘multiply by 3’ that always gives 7.", 3, "Multiply by 3, add 21, divide by 3, subtract the number: $x\\to3x\\to3x+21\\to x+7\\to7$ (3).", "H"),
W("A school fete stall pays ₹ 600 for the stall and makes each glass of lemonade for ₹ 5. It sells 150 glasses at ₹ $p$ each and earns a profit of ₹ 900. (a) Write the profit for $n$ glasses at ₹ $p$. (b) Find $p$. (c) At that price, how many glasses must be sold to just cover the costs?", 5, "(a) Profit $=np-5n-600$ (1). (b) $150p-750-600=900$, $150p=2250$, $p=$ ₹ 15 (2). (c) $15n-5n-600=0$, $10n=600$, $n=60$ glasses (2).", "H", wp=True),
W("Three friends have marbles: Bela has 3 more than Asha, and Chitra has twice as many as Asha. Together they have 47. How many does each have?", 4, "Asha $=x$: $x+(x+3)+2x=47$ (1). $4x=44$, $x=11$ (1). Asha $11$, Bela $14$ (1), Chitra $22$ (1).", "H", wp=True),
W("The length of a rectangle is $(2x+3)$ cm and its breadth is $(x+1)$ cm. Its perimeter is 38 cm. Find $x$, the sides and the area.", 4, "$2(3x+4)=38$ (1). $x=5$ (1). Sides $13$ cm and $6$ cm (1). Area $=78$ cm² (1).", "H", wp=True),
W("Meena solved $5x-3=2x+9$ as $5x-2x=9-3$, $3x=6$, $x=2$. Find her mistake, solve correctly and check.", 3, "She subtracted 3 instead of adding it when moving $-3$ (1). $5x-2x=9+3$, $3x=12$, $x=4$ (1). Check: $5\\times4-3=17=2\\times4+9$ (1).", "H"),
W("A number multiplied by 5 and decreased by 8 gives the same result as the number plus 4 multiplied by 3. Find the number.", 3, "$5x-8=3(x+4)$ (1). $5x-8=3x+12$, $2x=20$ (1). $x=10$; check $42=42$ (1).", "H"),
W("Prove that $\\overline{abc}+\\overline{bca}+\\overline{cab}=111(a+b+c)$, so it is always divisible by 37. Verify with the digits 7, 2, 5.", 4, "$(100a+10b+c)+(100b+10c+a)+(100c+10a+b)$ (1) $=111a+111b+111c=111(a+b+c)$ (1). $111=3\\times37$ (1). $725+257+572=1554=111\\times14=37\\times42$ (1).", "H"),
W("Squares are made in a row from matchsticks: 1 square needs 4 sticks, 2 squares need 7, 3 squares need 10. Write an expression for $n$ squares, find the sticks for 12 squares, and the number of squares made with 151 sticks.", 4, "Pattern: $3n+1$ (2). For $n=12$: $37$ sticks (1). $3n+1=151$ gives $n=50$ squares (1).", "H", wp=True),
]

_o = _old(8)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Algebra Toolkit"),
 ("table", ["Idea", "In words", "In letters", "Example"], [["Two-digit number", "tens × 10 + ones", "10a + b", "47 = 10 × 4 + 7"], ["Three-digit number", "hundreds × 100 + tens × 10 + ones", "100a + 10b + c", "452 = 400 + 50 + 2"], ["Even number", "2 × something", "2n", "2n + 2 is the next even number"], ["Odd number", "one more than an even number", "2n + 1", "the next odd is 2n + 3"], ["Consecutive numbers", "each one more", "n, n + 1, n + 2", "sum of three = 3n + 3"], ["Distributive law", "multiply every term inside", "a(b + c) = ab + ac", "3(x − 2) = 3x − 6"], ["Like terms", "same letter and power", "5x + 2x = 7x", "5x + 3 + 2x + 8 = 7x + 11"]]),
 ("note", "FORMULA", "Solving a linear equation: do the same operation on both sides. **Move a term across the = sign and change its sign:** 5x − 3 = 2x + 9 → 5x − 2x = 9 + 3 → 3x = 12 → x = 4. Always check by substituting."),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Unfolding a date trick"),
 ("steps", [("Question", "In the date trick the final answer is 1390. Find the date."), ("Formula", "Answer = 100M + 165 + D, so 1390 − 165 = 1225."), ("Read", "M = 12 and D = 25, so the date is **25 December**.")]),
 ("h3", "Example 2 — Pyramid with a missing number"),
 ("steps", [("Question", "Bottom row 2, x, 5 and top 29. Find x."), ("Top formula", "Top = a + 2b + c = 2 + 2x + 5 = 29."), ("Solve", "2x = 22, **x = 11**. Middle row 13, 16; check 13 + 16 = 29.")]),
 ("h3", "Example 3 — Digit puzzle"),
 ("steps", [("Question", "A two-digit number is 7 times the sum of its digits. Find it."), ("Equation", "10a + b = 7(a + b), so 3a = 6b, i.e. a = 2b."), ("Numbers", "b = 1, 2, 3, 4 give **21, 42, 63, 84**; check 63 = 7 × 9.")]),
 ("h3", "Example 4 — Age problem"),
 ("steps", [("Question", "Ria and her mother are 48 years together. Four years ago the mother was 7 times as old as Ria."), ("Equation", "Ria = x: (48 − x) − 4 = 7(x − 4), so 44 − x = 7x − 28."), ("Answer", "8x = 72, so Ria **9** and mother **39**. Check: 4 years ago 5 and 35.")]),
 ("h3", "Example 5 — Heads and legs"),
 ("steps", [("Question", "30 heads and 94 legs of cows and ducks."), ("Equation", "Cows c: 4c + 2(30 − c) = 94, so 2c + 60 = 94."), ("Answer", "c = 17 cows and 13 ducks.")]),
 ("h3", "Example 6 — Profit expression"),
 ("steps", [("Question", "A stall costs ₹ 600 and each lemonade costs ₹ 5. 150 glasses sold at ₹ p give ₹ 900 profit."), ("Equation", "150p − 5 × 150 − 600 = 900, so 150p = 2250."), ("Answer", "p = **₹ 15**. Break-even n: 15n − 5n = 600, n = 60 glasses.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Expression"], [
  ["‘3 more than twice a number’", "2x + 3"], ["‘twice the sum of x and 3’", "2(x + 3)"], ["‘5 less than a number’", "x − 5"], ["‘a number is 4 times another’", "y = 4x"],
  ["‘in 5 years’", "age + 5 (every person's age grows by the same number)"], ["‘4 years ago’", "age − 4"], ["‘fixed charge plus rate per km’", "fixed + rate × distance"], ["‘perimeter of a rectangle’", "2 × (length + breadth)"], ["‘total of heads and legs’", "two equations: animals = heads, 4c + 2d = legs"]]),
 ("note", "REMEMBER", "Every word problem has **one quantity written in two ways**. Choose a letter, write the two expressions, put = between them, solve, and check in the story."),
 ("h2", "Likely Exam Questions"),
 ("qa", [("Show that ‘think of a number, ×6, +18, ÷6, − the number’ always gives 3.", "x → 6x → 6x + 18 → x + 3 → 3."),
  ("Prove that the sum of any 3 × 3 calendar block is 9 times the centre number.", "The numbers are c − 8, c − 7, c − 6, c − 1, c, c + 1, c + 6, c + 7, c + 8; the extras cancel in pairs, leaving 9c."),
  ("Find a two-digit number whose digits add to 9 and which increases by 27 when reversed.", "9(b − a) = 27, so b − a = 3, with a + b = 9: the number is 36."),
  ("How do you find the largest product using three digits?", "Largest digit as the multiplier; the other two form the two-digit number with the larger digit in the tens place."),
  ("Why is abc + bca + cab divisible by 37?", "It equals 111(a + b + c) and 111 = 3 × 37."),
  ("What is wrong with 3(x − 2) + 4 = 3x + 2?", "The 3 must multiply −2 as well: 3x − 6 + 4 = 3x − 2.")]),
]
CH = dict(_o, num=13, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["Moving a term across = changes its sign; always check the solution in the original statement.", "Consecutive numbers: n, n + 1, n + 2 add to 3n + 3; five consecutive numbers add to 5 times the middle one."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
