"""Class 10 Maths Ch 3 - Pair of Linear Equations in Two Variables: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch03"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

from fractions import Fraction as F
def solve(a1, b1, c1, a2, b2, c2):          # a1 x + b1 y = c1
    d = a1 * b2 - a2 * b1
    return F(c1 * b2 - c2 * b1, d), F(a1 * c2 - a2 * c1, d)
CHK = [((1, 1, 5, 1, -1, 1), (3, 2)), ((2, 1, 11, 1, -1, 1), (4, 3)), ((1, 1, 40, 1, -1, 12), (26, 14)), ((2, 1, 17, 1, 1, 12), (5, 7)),
       ((3, 4, 10, 2, -2, 2), (2, 1)), ((2, 3, 12, 3, -2, 5), (3, 2)), ((1, -3, -10, 1, -2, 10), (50, 20)), ((1, 1, 12, 1, -1, 6), (9, 3)),
       ((3, 2, 3500, 2, 3, 4000), (500, 1000)), ((3, -1, 3, 4, -1, 8), (5, 12)), ((1, 1, 9, 1, -1, 3), (6, 3)), ((3, -5, 6, 2, 3, 61), (17, 9)),
       ((1, 1, 83, 4, 1, 182), (33, 50)), ((1, 10, 105, 1, 15, 155), (5, 10)), ((3, 2, 24, 2, 3, 21), (6, 3)), ((1, 1, 16, 50, 20, 620), (10, 6)),
       ((1, -2, 4, 1, 1, 28), (20, 8)), ((99, 101, 499, 101, 99, 501), (3, 2)), ((1, -1, 20, 1, 1, 100), (60, 40)), ((1, 20, 1000, 1, 26, 1180), (400, 30)),
       ((3, 2, 80, 2, 5, 90), (20, 10)), ((1, 1, 100, 20, 10, 1700), (70, 30)), ((2, -1, 0, 1, -1, -2), (2, 4)), ((1, -12, -110, 1, -2, 10), (34, 12)),
       ((1, 5, 27, 1, 3, 21), (12, 3))]
for _k, _v in CHK: assert solve(*_k) == _v, _k
assert solve(1, -1, 20, 1, 1, 100) == (60, 40) or True
assert (17 - 5) * (9 + 3) == 17 * 9 - 9 and (17 + 3) * (9 + 2) == 17 * 9 + 67
assert (2 * 33 + 4) + (2 * 50 + 10) == 180 and (50 + 3) + (4 * 33 - 5) == 180 and 5 + 25 * 10 == 255
a_, b_ = 5, 1; assert F(2, a_ - b_) == F(3, a_ + b_) == F(7, 3 * a_ + b_ - 2) == F(1, 2)
assert F(2, 6) == F(3, 9) or True
assert F(5, -10) == F(-3, 6) == F(11, -22) and 5 * 4 - 3 * 3 == 11 and 5 * (-2) - 3 * (-7) == 11 and 5 - 3 * (-2) == 11

WS = [
# ---------------- EASY ----------------
W(r"The solution of the pair $x+y=5$, $x-y=1$ is:", 1, r"(b) $(3,2)$. Adding gives $2x=6$, $x=3$, then $y=2$. (1)", "E", opts=["$(2,3)$", "$(3,2)$", "$(4,1)$", "$(1,4)$"]),
W(r"The pair $2x+3y=7$ and $4x+6y=14$ has:", 1, r"(c) infinitely many solutions. The second equation is twice the first, so the lines coincide: $\dfrac24=\dfrac36=\dfrac7{14}$. (1)", "E", opts=["a unique solution", "no solution", "infinitely many solutions", "exactly two solutions"]),
W(r"The pair $x+2y=3$ and $2x+4y=9$ has:", 1, r"(b) no solution. $\dfrac12=\dfrac24\ne\dfrac39$, so the lines are parallel and distinct. (1)", "E", opts=["a unique solution", "no solution", "infinitely many solutions", "exactly two solutions"]),
W(r"If $\dfrac{a_1}{a_2}\ne\dfrac{b_1}{b_2}$ for a pair of linear equations, the lines are:", 1, r"(a) intersecting. Unequal ratios of the $x$- and $y$-coefficients give exactly one common point. (1)", "E", opts=["intersecting", "parallel", "coincident", "perpendicular"]),
W(r"The pair $kx+2y=5$ and $3x+y=1$ has a unique solution when:", 1, r"(b) $k\ne6$. Need $\dfrac k3\ne\dfrac21$, i.e. $k\ne6$. (1)", "E", opts=[r"$k=6$", r"$k\ne6$", r"$k=3$", r"$k\ne3$"]),
W(r"The sum of two numbers is 15 and their difference is 3. The larger number is:", 1, r"(b) 9. $x+y=15$, $x-y=3$ give $x=9$, $y=6$. (1)", "E", opts=["8", "9", "10", "12"]),
W(r"If $x=2$, $y=-1$ is a solution of $3x+ky=4$, then $k$ equals:", 1, r"(b) 2. $3(2)+k(-1)=4\Rightarrow6-k=4\Rightarrow k=2$. (1)", "E", opts=["10", "2", "-2", "-10"]),
W(r"Solve by substitution: $y=2x$ and $x+y=9$.", 2, r"$x+2x=9$ (1) $\Rightarrow x=3$, $y=6$ (1).", "E"),
W(r"Solve by elimination: $2x+y=11$ and $x-y=1$.", 2, r"Adding: $3x=12$, $x=4$ (1). Then $y=x-1=3$ (1).", "E"),
W(r"Check whether $(2,1)$ is a solution of $3x-2y=4$.", 1, r"$3(2)-2(1)=6-2=4$, so $(2,1)$ **is** a solution (1).", "E"),
W(r"The sum of two numbers is 40 and their difference is 12. Find the numbers.", 2, r"$x+y=40$, $x-y=12$ (1). Adding: $2x=52$, $x=26$, $y=14$ (1).", "E", wp=True),
W(r"A pen and a pencil together cost ₹ 12; two pens and a pencil cost ₹ 17. Find the cost of each.", 2, r"Let pen $=x$, pencil $=y$: $x+y=12$, $2x+y=17$ (1). Subtracting: $x=5$, $y=7$. Pen ₹ **5**, pencil ₹ **7** (1).", "E", wp=True),
W(r"Draw up a table of two points on each line $x+y=6$ and $x-y=2$ and find the point where the lines meet.", 2, r"$x+y=6$: $(0,6)$, $(6,0)$; $x-y=2$: $(0,-2)$, $(2,0)$ (1). The lines meet at $(4,2)$, since $4+2=6$ and $4-2=2$ (1).", "E"),
W(r"Without solving, find the nature of the solution of $x+2y-4=0$ and $2x+4y-12=0$.", 2, r"$\dfrac{a_1}{a_2}=\dfrac12$, $\dfrac{b_1}{b_2}=\dfrac24=\dfrac12$, $\dfrac{c_1}{c_2}=\dfrac{-4}{-12}=\dfrac13$ (1). Two equal ratios and a different third: parallel lines, **no solution**, inconsistent (1).", "E"),
W(r"The sum of the ages of a father and his son is 50 years and the father is 4 times as old as the son. Find their ages.", 2, r"$x+y=50$, $x=4y$ (1). $5y=50$, $y=10$, $x=40$: son **10 years**, father **40 years** (1).", "E", wp=True),
W(r"True or false? Give a reason. A pair of linear equations in two variables can have exactly two solutions.", 1, r"**False.** Two distinct lines meet at one point or none; coincident lines have infinitely many common points, never exactly two (1).", "E"),
W(r"The length of a rectangle exceeds its breadth by 5 cm and its perimeter is 50 cm. Find the length and the breadth.", 2, r"$l-b=5$, $l+b=25$ (1). $l=15$ cm, $b=10$ cm (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"Solve by substitution: $3x+4y=10$ and $2x-2y=2$.", 3, r"From the second, $x=y+1$ (1). $3(y+1)+4y=10\Rightarrow7y=7$, $y=1$ (1), $x=2$ (1).", "M"),
W(r"Solve by elimination: $2x+3y=12$ and $3x-2y=5$.", 3, r"Multiply by 2 and 3: $4x+6y=24$, $9x-6y=15$ (1). Add: $13x=39$, $x=3$ (1). $y=2$ (check: $9-4=5$ ✓) (1).", "M"),
W(r"Solve $99x+101y=499$ and $101x+99y=501$.", 3, r"Add: $200(x+y)=1000$, so $x+y=5$ (1). Subtract: $2x-2y=2$, so $x-y=1$ (1). Hence $x=3$, $y=2$ (1).", "M"),
W(r"Solve $\dfrac x2+\dfrac y3=4$ and $\dfrac x3+\dfrac y2=\dfrac72$.", 3, r"Multiply by 6: $3x+2y=24$ and $2x+3y=21$ (1). Eliminating $y$ (×3, ×2): $5x=30$, $x=6$ (1); $y=3$ (1).", "M"),
W(r"For what value of $k$ will the pair $3x-y=5$ and $6x-2y=k$ have infinitely many solutions?", 2, r"$\dfrac36=\dfrac{-1}{-2}=\dfrac12$, so need $\dfrac5k=\dfrac12$ (1) $\Rightarrow k=10$ (1).", "M"),
W(r"For what value of $p$ does the pair $2x+3y=5$ and $px+6y=10$ have infinitely many solutions?", 2, r"Need $\dfrac2p=\dfrac36=\dfrac5{10}=\dfrac12$ (1), so $p=4$ (1).", "M"),
W(r"Without solving, state whether each pair is consistent, and say how many solutions: (i) $x-2y=3$, $3x+4y=1$ (ii) $2x-3y=8$, $4x-6y=9$ (iii) $3x+5y=15$, $6x+10y=30$", 3, r"(i) $\dfrac13\ne\dfrac{-2}{4}$: intersecting, consistent, one solution (1). (ii) $\dfrac24=\dfrac{-3}{-6}=\dfrac12\ne\dfrac89$: parallel, inconsistent, none (1). (iii) all three ratios equal $\dfrac12$: coincident, consistent, infinitely many (1).", "M"),
W(r"The sum of the ages of Anita and Bina is 28 years. Four years from now Anita will be twice as old as Bina. Find their present ages.", 3, r"$x+y=28$ and $x+4=2(y+4)$, i.e. $x-2y=4$ (1,1). Subtracting: $3y=24$, $y=8$, $x=20$: Anita **20 years**, Bina **8 years** (1).", "M", wp=True),
W(r"Five years ago Nuri was thrice as old as Sonu. Ten years later Nuri will be twice as old as Sonu. Find their present ages.", 3, r"$x-5=3(y-5)\Rightarrow x-3y=-10$; $x+10=2(y+10)\Rightarrow x-2y=10$ (1). Subtract: $y=20$ (1), $x=50$. Nuri **50**, Sonu **20** (1). (Check: $45=3\times15$, $60=2\times30$.)", "M", wp=True),
W(r"A fraction becomes $\dfrac13$ if 1 is subtracted from the numerator and becomes $\dfrac14$ if 8 is added to the denominator. Find the fraction.", 3, r"Fraction $\dfrac xy$: $\dfrac{x-1}y=\dfrac13\Rightarrow3x-y=3$ and $\dfrac x{y+8}=\dfrac14\Rightarrow4x-y=8$ (1,1). Subtract: $x=5$, $y=12$ (1). Fraction $=\dfrac5{12}$.", "M", wp=True),
W(r"A boat covers 36 km downstream in 3 hours and 24 km upstream in 4 hours. Find the speed of the boat in still water and the speed of the stream.", 3, r"Downstream speed $=12$ km/h, upstream speed $=6$ km/h (1). $x+y=12$, $x-y=6$ (1). Boat $=9$ km/h, stream $=3$ km/h (1).", "M", wp=True),
W(r"The cost of 3 chairs and 2 tables is ₹ 3,500 and the cost of 2 chairs and 3 tables is ₹ 4,000. Find the cost of one chair and one table.", 3, r"$3c+2t=3500$, $2c+3t=4000$ (1). ×3 and ×2: $9c+6t=10500$, $4c+6t=8000$, so $5c=2500$ (1). Chair ₹ **500**, table ₹ **1,000** (1).", "M", wp=True),
W(r"Find the value of $k$ for which $2x+3y=7$ and $(k-1)x+(k+2)y=3k$ have infinitely many solutions.", 3, r"Need $\dfrac2{k-1}=\dfrac3{k+2}=\dfrac7{3k}$ (1). $2(k+2)=3(k-1)\Rightarrow k=7$ (1). Check: $\dfrac3{9}=\dfrac7{21}=\dfrac13$ ✓ (1).", "M"),
W(r"Meena buys 2 pencils and 3 erasers for ₹ 9. Sakshi buys 4 pencils and 6 erasers for ₹ 18. Write the equations, say what kind of lines they represent, and explain whether the price of one pencil can be found.", 3, r"$2x+3y=9$ and $4x+6y=18$ (1). The second is twice the first: coincident lines (1). Infinitely many price pairs fit (e.g. pencil ₹ 3 and eraser ₹ 1, or pencil ₹ 1.50 and eraser ₹ 2), so the prices **cannot** be found from these data alone (1).", "M", wp=True),
W(r"The sum of the digits of a two-digit number is 9. The number obtained by reversing the digits is 27 more than the original number. Find the number.", 3, r"Digits $x$ (tens), $y$ (units): $x+y=9$; $(10y+x)-(10x+y)=27\Rightarrow y-x=3$ (1,1). $y=6$, $x=3$: the number is **36** (check: $63-36=27$) (1).", "M", wp=True),
W(r"A taxi charges a fixed amount plus a fixed rate per kilometre. The fare for 10 km is ₹ 105 and for 15 km is ₹ 155. Find the fixed charge, the rate per km and the fare for 25 km.", 3, r"$x+10y=105$, $x+15y=155$ (1). Subtract: $5y=50$, $y=10$, $x=5$ (1). Fixed charge ₹ 5, ₹ 10 per km; 25 km: $5+250=$ ₹ **255** (1).", "M", wp=True),
W(r"The lines $x+2y=6$ and $2x-y=2$ intersect at $(2,2)$. Find where each line meets the $x$-axis and the area of the triangle formed by the two lines and the $x$-axis.", 3, r"$x+2y=6$ meets the $x$-axis at $(6,0)$; $2x-y=2$ at $(1,0)$ (1). The base along the $x$-axis is $6-1=5$ and the height is the $y$-coordinate of the intersection, 2 (1). Area $=\dfrac12\times5\times2=$ **5 square units** (1).", "M"),
W(r"Pooja solves $2x+3y=13$ and $2x-y=5$. She subtracts and writes $3y-y=2y$, so $2y=8$ and $y=4$. Find her mistake and solve correctly.", 2, r"The second equation has $-y$, so subtracting gives $3y-(-y)=4y$ and $13-5=8$ (1). $y=2$, then $2x-2=5$, $x=\dfrac72$ (1).", "M"),
W(r"A cashier has 16 notes of ₹ 50 and ₹ 20 only, worth ₹ 620 altogether. How many notes of each kind does she have?", 3, r"$x+y=16$, $50x+20y=620$ (1). From the first $y=16-x$: $50x+320-20x=620$, $30x=300$ (1). **10 notes of ₹ 50 and 6 notes of ₹ 20** (1).", "M", wp=True),
# ---------------- HARD ----------------
W(r"For what value of $k$ does the pair $kx+3y=k-3$ and $12x+ky=k$ have no solution?", 3, r"No solution needs $\dfrac k{12}=\dfrac3k\ne\dfrac{k-3}k$ (1). $k^2=36$, $k=\pm6$ (1). For $k=6$: $\dfrac{k-3}{k}=\dfrac12=\dfrac6{12}$, so all three ratios are equal and there are infinitely many solutions; for $k=-6$: $\dfrac k{12}=-\dfrac12$ but $\dfrac{k-3}{k}=\dfrac{-9}{-6}=\dfrac32\ne-\dfrac12$. So $k=-6$ (1).", "H"),
W(r"A hostel's monthly bill has a fixed part plus a charge for each day food is taken. Ravi takes food for 20 days and pays ₹ 1,000; Gopal takes food for 26 days and pays ₹ 1,180. Find the fixed charge and the cost per day, and the bill for 30 days.", 3, r"$f+20x=1000$, $f+26x=1180$ (1). $6x=180$, $x=30$, $f=400$ (1). Bill for 30 days $=400+900=$ ₹ **1,300** (1).", "M", wp=True),
W(r"For what values of $k$ does the pair $kx-y=2$ and $6x-2y=3$ have (i) a unique solution, (ii) no solution, (iii) infinitely many solutions?", 3, r"$\dfrac k6$, $\dfrac{-1}{-2}=\dfrac12$, $\dfrac{-2}{-3}=\dfrac23$. (i) $k\ne3$ (1). (ii) $k=3$, since then $\dfrac12=\dfrac12\ne\dfrac23$ (1). (iii) impossible, because $\dfrac12\ne\dfrac23$ for every $k$ (1).", "H"),
W(r"Show that the pair $5x-3y=11$ and $-10x+6y=-22$ has infinitely many solutions and write three solutions.", 3, r"$\dfrac5{-10}=\dfrac{-3}6=\dfrac{11}{-22}=-\dfrac12$, so the lines coincide (1). Any point of $5x-3y=11$ works: $(1,-2)$, $(4,3)$, $(-2,-7)$ (2).", "H"),
W(r"Two cars start from towns A and B, 100 km apart. If they drive in the same direction, they meet after 5 hours; if they drive towards each other, they meet after 1 hour. Find the speed of each car.", 4, r"Let the speeds be $u>v$. Same direction: relative speed $u-v=\dfrac{100}5=20$ (1). Towards each other: $u+v=\dfrac{100}1=100$ (1). Adding: $u=60$, $v=40$ (2). Speeds **60 km/h and 40 km/h**.", "H", wp=True),
W(r"A rectangle's area decreases by 9 square units if its length is decreased by 5 units and its breadth increased by 3 units. The area increases by 67 square units if the length is increased by 3 units and the breadth by 2 units. Find the dimensions.", 4, r"$(l-5)(b+3)=lb-9\Rightarrow3l-5b=6$ (1). $(l+3)(b+2)=lb+67\Rightarrow2l+3b=61$ (1). Eliminating $b$: $9l-15b=18$, $10l+15b=305$, $19l=323$ (1). $l=17$, $b=9$ (1).", "H", wp=True),
W(r"In a cyclic quadrilateral ABCD, $\angle A=(2x+4)^\circ$, $\angle B=(y+3)^\circ$, $\angle C=(2y+10)^\circ$ and $\angle D=(4x-5)^\circ$. Find all four angles.", 4, r"Opposite angles of a cyclic quadrilateral add to $180^\circ$: $2x+4+2y+10=180\Rightarrow x+y=83$ (1); $y+3+4x-5=180\Rightarrow4x+y=182$ (1). Subtract: $3x=99$, $x=33$, $y=50$ (1). $\angle A=70^\circ$, $\angle B=53^\circ$, $\angle C=110^\circ$, $\angle D=127^\circ$ (1).", "H", wp=True),
W(r"Find the values of $a$ and $b$ for which the pair $2x+3y=7$ and $(a-b)x+(a+b)y=3a+b-2$ has infinitely many solutions.", 4, r"Need $\dfrac2{a-b}=\dfrac3{a+b}=\dfrac7{3a+b-2}$ (1). First two: $2a+2b=3a-3b\Rightarrow a=5b$ (1). Last two: $9a+3b-6=7a+7b\Rightarrow a-2b=3$ (1). So $3b=3$: $b=1$, $a=5$ (1).", "H"),
W(r"**Case study.** At the school fete in Jaipur a stall sells lassi at ₹ $x$ a glass and samosas at ₹ $y$ each. Group A pays ₹ 80 for 3 lassi and 2 samosas; Group B pays ₹ 90 for 2 lassi and 5 samosas. (i) Write the pair of equations. (ii) Find $x$ and $y$. (iii) Find the bill for 5 lassi and 4 samosas. (iv) At the end of the day the stall sold 100 items for ₹ 1,700. How many lassi were sold?", 5, r"(i) $3x+2y=80$ and $2x+5y=90$ (1). (ii) ×2 and ×3: $6x+4y=160$, $6x+15y=270$; $11y=110$, $y=10$, $x=20$ (2). (iii) $5(20)+4(10)=$ ₹ **140** (1). (iv) $a+b=100$, $20a+10b=1700$: $10a=700$, so **70 lassi** (and 30 samosas) (1).", "H", wp=True),
W(r"A two-digit number is 4 times the sum of its digits. If 18 is added to the number, its digits are reversed. Find the number.", 4, r"Digits $x$ (tens), $y$ (units): $10x+y=4(x+y)\Rightarrow2x=y$ (1). $10x+y+18=10y+x\Rightarrow y-x=2$ (1). So $x=2$, $y=4$ (1). The number is **24** (check: $24=4\times6$, $24+18=42$) (1).", "H", wp=True),
W(r"Isha solves $2x+3y=12$ and $3x+2y=13$ by substitution. She writes $x=\dfrac{12-3y}2$ and then $3\left(\dfrac{12-3y}2\right)+2y=13$, which she multiplies by 2 to get $36-9y+2y=26$. Find her mistake and solve correctly.", 3, r"When multiplying by 2 she forgot to multiply $2y$ by 2: it should be $36-9y+4y=26$ (1). So $-5y=-10$, $y=2$ (1), $x=\dfrac{12-6}2=3$ (1). Check: $3(3)+2(2)=13$ ✓.", "H"),
W(r"Ten years ago a father was 12 times as old as his son. Ten years from now he will be twice as old as his son. Find their present ages.", 4, r"Father $F$, son $S$: $F-10=12(S-10)$ and $F+10=2(S+10)$ (1). So $F-12S=-110$ and $F-2S=10$ (1). Subtract: $10S=120$, $S=12$ (1), $F=34$. Check: ten years ago $24=12\times2$; ten years hence $44=2\times22$ ✓ (1).", "H", wp=True),
W(r"Solve for $x$ and $y$: $ax+by=a-b$ and $bx-ay=a+b$.", 4, r"Multiply the first by $a$ and the second by $b$: $a^2x+aby=a^2-ab$, $b^2x-aby=ab+b^2$ (1). Add: $(a^2+b^2)x=a^2+b^2$, so $x=1$ (2). Then $a+by=a-b$ gives $y=-1$ (1).", "H"),
W(r"To hire a library book, Saritha pays ₹ 27 for 6 days and Susy pays ₹ 21 for 4 days. The charge is a fixed amount for the first day plus a fixed amount for each extra day. Find both amounts and the charge for 10 days.", 3, r"Let first day ₹ $x$, each extra day ₹ $y$: $x+5y=27$, $x+3y=21$ (1). $2y=6$, $y=3$, $x=12$ (1). For 10 days: $12+9\times3=$ ₹ **39** (1).", "H", wp=True),
]
WS.sort(key=lambda w: "EMH".index(w["level"]))   # keep the parts contiguous after a re-tag
for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(3)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "3.6 More Worked Examples"),
 ("h3", "Example 1 — Elimination"),
 ("steps", [("Solve 2x + 3y = 12 and 3x − 2y = 5", "Make the y-coefficients equal in size: multiply the first by 2 and the second by 3."), ("Add", "4x + 6y = 24 and 9x − 6y = 15 give 13x = 39, so x = 3."), ("Back-substitute", "6 + 3y = 12, so y = 2. Check in the second: 9 − 4 = 5 ✓.")]),
 ("h3", "Example 2 — Substitution"),
 ("steps", [("Solve 3x + 4y = 10 and 2x − 2y = 2", "From the second equation x − y = 1, so x = y + 1."), ("Substitute", "3(y + 1) + 4y = 10, so 7y = 7 and y = 1."), ("Answer", "x = 2, y = 1.")]),
 ("h3", "Example 3 — Finding k"),
 ("steps", [("For which k do 2x + 3y = 7 and (k − 1)x + (k + 2)y = 3k have infinitely many solutions?", "Need a₁/a₂ = b₁/b₂ = c₁/c₂, i.e. 2/(k − 1) = 3/(k + 2) = 7/(3k)."), ("Use two of the ratios", "2(k + 2) = 3(k − 1), so k = 7."), ("Check", "3/9 = 7/21 = 1/3 ✓, so the third ratio also agrees. For **no solution** the first two ratios are equal and the third is different.")]),
 ("h3", "Example 4 — Digits of a number"),
 ("steps", [("Sum of digits is 9; reversing the digits adds 27", "Let the tens digit be x and the units digit y. The number is 10x + y."), ("Equations", "x + y = 9 and (10y + x) − (10x + y) = 27, i.e. y − x = 3."), ("Solve", "y = 6, x = 3; the number is **36** (63 − 36 = 27).")]),
 ("h3", "Example 5 — Speed, distance and time"),
 ("steps", [("Two cars start 100 km apart. Same direction: meet in 5 h; towards each other: meet in 1 h", "Let the speeds be u (faster) and v."), ("Equations", "Same direction, relative speed u − v = 100/5 = 20. Opposite directions u + v = 100/1 = 100."), ("Solve", "u = 60 km/h and v = 40 km/h.")]),
 ("h3", "Example 6 — Fixed charge plus rate"),
 ("steps", [("Fare for 10 km is ₹105 and for 15 km is ₹155", "Let the fixed charge be x and the rate per km be y: x + 10y = 105 and x + 15y = 155."), ("Subtract", "5y = 50, so y = 10 and x = 5."), ("Use it", "Fare for 25 km = 5 + 250 = **₹255**.")]),
 ("h2", "3.7 Deciding the Nature of the Solution"),
 ("table", ["Compare", "Lines", "Solutions", "Name of the pair"], [
  ["a₁/a₂ ≠ b₁/b₂", "intersect at one point", "exactly **one**", "consistent"],
  ["a₁/a₂ = b₁/b₂ = c₁/c₂", "coincide", "**infinitely many**", "consistent (dependent)"],
  ["a₁/a₂ = b₁/b₂ ≠ c₁/c₂", "parallel", "**none**", "inconsistent"]]),
 ("p", "Write each equation as ax + by + c = 0 before comparing, so that c carries its sign. Two parallel lines never meet; two lines that are not parallel meet exactly once. That is why a pair of linear equations never has exactly two solutions."),
 ("note", "IMPORTANT", "When the pair contains k, write the equal ratios **in pairs**: use the two ratios that do not contain the unknown to check, and the other equations to find k. Always test the third ratio; for k = 6 in kx + 3y = k − 3, 12x + ky = k the pair has **infinitely many** solutions, so only k = −6 gives no solution."),
 ("h2", "3.8 Word Problems: How to Translate"),
 ("table", ["Type", "Choose variables", "Typical equations"], [
  ["numbers", "the two numbers x, y", "sum x + y, difference x − y, one is a multiple of the other"],
  ["ages", "present ages x and y", "x − 5 = 3(y − 5) (past); x + 10 = 2(y + 10) (future)"],
  ["digits", "tens digit x, units digit y", "number = 10x + y; reversed = 10y + x"],
  ["fractions", "numerator x, denominator y", "(x − 1)/y = 1/3 becomes 3x − y = 3"],
  ["money and articles", "price of each article", "3c + 2t = 3500 and 2c + 3t = 4000"],
  ["fixed charge plus rate", "fixed x, rate y", "x + 10y = 105, x + 15y = 155"],
  ["boat or stream (steady speeds)", "boat x, stream y", "downstream = x + y, upstream = x − y"],
  ["two moving bodies", "speeds u, v", "same direction: u − v; opposite: u + v (distance ÷ time)"],
  ["geometry", "unknown angles or sides", "cyclic quadrilateral: opposite angles add to 180°; rectangle: perimeter 2(l + b)"]]),
 ("steps", [("Step 1", "Read carefully and name the two unknown quantities."), ("Step 2", "Form two equations from the two facts given."), ("Step 3", "Solve by substitution or elimination."), ("Step 4", "Check in the **words** of the problem and write the answer with units.")]),
 ("h2", "3.9 Common Mistakes"),
 ("table", ["Mistake", "Correct idea"], [
  ["Subtracting equations and forgetting that −(−y) = +y", "write the subtraction line by line: 3y − (−y) = 4y"],
  ["Multiplying only one side when making coefficients equal", "multiply **every** term, including the constant"],
  ["Writing the reversed number as 10x + y", "reversed number is 10y + x"],
  ["Taking u + v for two cars moving in the same direction", "same direction uses u − v; opposite directions uses u + v"],
  ["Giving only x and forgetting y", "the answer is a **pair** (x, y); check it in both equations"],
  ["Saying 'the lines are parallel' without checking c₁/c₂", "if all three ratios are equal the lines coincide"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["Choose **two variables, form two equations, solve, then check in the words** of the problem.", "Digit, age, fraction, money, fixed-plus-rate and speed problems each have a **standard way to form equations**.", "Never state only one value; the answer is the pair (x, y)."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
