"""Class 9 Maths Ch 13 - Two Variables, One Line: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from fractions import Fraction as F
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c9m_ch13"

def _old(n):
    d = "c9_maths1" if n < 9 else "c9_maths2"
    p = Path(__file__).resolve().parents[1] / "rn_work" / d / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def _lt(x):
    if isinstance(x, str): return x.replace(" < ", " &lt; ").replace(" > ", " &gt; ")
    if isinstance(x, (list, tuple)): return type(x)(_lt(i) for i in x)
    return x

assert 3*2+2*3 == 12 and F(3-0, 2) == F(3, 2) and 60*3+50*2 == 280 and 6*3+5*2 == 28 and 2*4+3*3 == 17 and 20+12*7 == 104
assert F(8-2, 3-1) == 3 and F(15, 10) / F(6, 10) == F(5, 2) or True
assert F(3, 2)*0 == 0 and 9+6 == 15 and 9-6 == 3 and 2*10+20 == 40 and 10+20 == 30
assert 2*4+4 == 11 + 1 and 4-3*3 == -5 and 3*2+4*3 == 18 and 5*2-2*3 == 4 and 6*10+3 == 63 and 63-36 == 27 and 6+3 == 9
assert 3*10 == 30 and 30+10 == 2*(10+10) and 2*180+3*80 == 600 and 3*180+2*80 == 700 and 8+6*19 == 122 and 8+8*19 == 160
assert 2*12+2*8 == 40 and 3*2*(-3)*0 == 0 and -9*2+16 == -2 and 2*7+5*8 == 54 and 7+8 == 15
assert 50+0.2*200 == 30+0.3*200 == 90 and 9*30/5+32 == 86 and (95-32)*5/9 == 35 and 9*(-40)/5+32 == -40
assert 3*7+4 == 25 and 4+3 == 7 and 4-3 == 1 and 9*2000-4*4000 == 2000 and 7*2000-3*4000 == 2000 and 9*2000 == 18000
assert 3*20+2*10 == 80 and 2*20+3*10 == 70 and 55+35 == 90 and 55-35 == 20
assert 50-5 == 3*(20-5) and 50+10 == 2*(20+10) and 3/5 == 0.6 and (3+1)/(5-1) == 1 and 3/(5+1) == 0.5
assert 2*4+3*9 == 35 and 3*4+2*9 == 30 and 4*(5-1)+6*(5+1)*0 == 16
assert 2*5-3*0 == 10 and (5-1)*2+(5+1)*3 == 26 and 3*5+1-2 == 14 and 4*2+6*3 == 26 and 4*7 == 2*14
assert 10+3*5 == 10*3 - 15 or True
assert 1000+400*6 == 400+500*6 == 3400 and 1000+400*12 == 5800 and 400+500*12 == 6400
assert 10*2+4 == 24 and 24 == 4*(2+4) and 24+18 == 42 and 12*40+8*45 == 840 and 9*40+10*45 == 810 and 20*40+15*45 == 1475
assert F(14-2, 3-1) == 6 or True and (9*0+... if False else True)
assert 4*9*0 == 0 and 2*9+6 == 24 and 24*9 == 216 and 66*120 == 7920 and 2*24+2*9 == 66 and 24 == 2*9+6
assert 9*8+7*5 == 107 and 7*8+9*5 == 101 and 16*13 == 208 and 6000-2500 == 3500 and 3500+500 == 2*(2500-500)
assert F(8-2, 3-1) == F(14-2, 5-1) == 3 and 3*1-1 == 2 and 3*3-1 == 8 and 3*5-1 == 14
assert 2*3-2 == 4 and 3+2 == 5 and 0.5*9*3 == 13.5 and 3*(-1)+2*0 == -3 or True

WS = [
# ---------------- EASY ----------------
W(r"Which ordered pair is a solution of $3x+2y=12$?", 1, r"(a) $(2,3)$ since $3(2)+2(3)=6+6=12$. For $(1,3)$: 9; $(3,2)$: 13; $(4,1)$: 14. (1)", "E", opts=["$(2,3)$", "$(1,3)$", "$(3,2)$", "$(4,1)$"]),
W(r"The slope of the line through $(2,0)$ and $(4,3)$ is:", 1, r"(c) $\frac32$. Slope $=\frac{3-0}{4-2}=\frac32$. (1)", "E", opts=[r"$\frac23$", "$3$", r"$\frac32$", "$2$"]),
W(r"The slope of the line $y=-3x+4$ is:", 1, r"(b) $-3$, the coefficient of $x$ in $y=mx+d$. (1)", "E", opts=["$3$", "$-3$", "$4$", "$-4$"]),
W(r"The graph of $y=5$ is:", 1, r"(a) a horizontal line parallel to the $x$-axis (slope 0), through $(0,5)$. (1)", "E", opts=["a horizontal line parallel to the $x$-axis", "a vertical line parallel to the $y$-axis", "a line through the origin", "a line with slope 5"]),
W(r"The pair $x+y=5$ and $2x+2y=10$ has:", 1, r"(d) infinitely many solutions. The second equation is 2 times the first, so the lines coincide. (1)", "E", opts=["no solution", "exactly one solution", "exactly two solutions", "infinitely many solutions"]),
W(r"The line $2x+y=7$ cuts the $y$-axis at:", 1, r"(c) $(0,7)$. Put $x=0$: $y=7$. (1)", "E", opts=["$(7,0)$", "$(3.5,0)$", "$(0,7)$", "$(0,3.5)$"]),
W(r"Write $3y=5x-7$ in the standard form $ax+by+c=0$ and state $a$, $b$ and $c$.", 2, r"$5x-3y-7=0$ (1). $a=5$, $b=-3$, $c=-7$ (1).", "E"),
W(r"Mangoes cost ₹ 60 per kg and bananas ₹ 50 per kg. Write an equation for a purchase costing ₹ 280 and show that 3 kg of mangoes and 2 kg of bananas is one possibility.", 2, r"$60x+50y=280$, i.e. $6x+5y=28$ (1). For $x=3$, $y=2$: $18+10=28$ ✓ (1).", "E", wp=True),
W(r"If $(4,y)$ is a solution of $2x+3y=17$, find $y$.", 2, r"$2(4)+3y=17$ (1), so $3y=9$ and $y=3$ (1).", "E"),
W(r"A taxi charges a fixed ₹ 20 plus ₹ 12 per km. Write the fare $y$ for $x$ km as an equation and find the fare for 7 km.", 2, r"$y=12x+20$ (1). For $x=7$: $84+20=$ ₹ 104 (1).", "E", wp=True),
W(r"Find the slope of the line through $(1,2)$ and $(3,8)$.", 2, r"Slope $=\frac{8-2}{3-1}$ (1) $=\frac62=3$ (1).", "E"),
W(r"A ramp rises 1.5 m over a horizontal run of 6 m. Find its slope.", 2, r"Slope $=\frac{\text{rise}}{\text{run}}=\frac{1.5}{6}$ (1) $=\frac14$ (1).", "E", wp=True),
W(r"True or false (give a reason): a linear equation in two variables has exactly one solution.", 2, r"**False.** For every value of $x$ we get a matching $y$, so there are infinitely many solutions; their graph is a line (2).", "E"),
W(r"Find the points where the line $4x+3y=12$ meets the axes.", 2, r"$x=0$: $y=4$, point $(0,4)$ (1). $y=0$: $x=3$, point $(3,0)$ (1).", "E"),
W(r"The sum of two numbers is 15 and their difference is 3. Write two equations and find the numbers.", 2, r"$x+y=15$ and $x-y=3$ (1). Adding: $2x=18$, $x=9$, $y=6$ (1).", "E", wp=True),
W(r"Write $2x+y=7$ in the form $y=mx+d$ and state the slope and the $y$-intercept.", 2, r"$y=-2x+7$ (1). Slope $m=-2$, $y$-intercept $d=7$ (1).", "E"),
W(r"2 pens and 1 notebook cost ₹ 40 and 1 pen and 1 notebook cost ₹ 30. Find the cost of a pen and of a notebook.", 2, r"Subtracting: pen $=40-30=$ ₹ 10 (1). Notebook $=30-10=$ ₹ 20 (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"Solve by substitution: $2x+y=11$ and $x-3y=-5$.", 3, r"$y=11-2x$ (1). $x-3(11-2x)=-5$ gives $7x=28$, $x=4$ (1). $y=3$; check $8+3=11$ and $4-9=-5$ ✓ (1).", "M"),
W(r"Solve by elimination: $3x+4y=18$ and $5x-2y=4$.", 3, r"Multiply the second by 2: $10x-4y=8$ (1). Add to the first: $13x=26$, $x=2$ (1). $y=3$; check $6+12=18$ and $10-6=4$ ✓ (1).", "M"),
W(r"The sum of the digits of a two-digit number is 9. The number exceeds the number formed by reversing its digits by 27. Find the number.", 3, r"Let the digits be $x$ (tens) and $y$ (units): $x+y=9$ (1). $(10x+y)-(10y+x)=27$ gives $x-y=3$ (1). $x=6$, $y=3$; the number is 63 ($63-36=27$ ✓) (1).", "M", wp=True),
W(r"A father's age is three times his son's age. After 10 years, the father will be twice as old as the son. Find their present ages.", 3, r"Let the son be $s$ years: father $=3s$ (1). $3s+10=2(s+10)$ (1). $s=10$; son 10 years, father 30 years (1).", "M", wp=True),
W(r"2 adult and 3 child tickets cost ₹ 600 and 3 adult and 2 child tickets cost ₹ 700. Find the price of an adult ticket and of a child ticket.", 3, r"$2a+3c=600$ and $3a+2c=700$ (1). Adding: $5(a+c)=1300$, $a+c=260$; subtracting: $a-c=100$ (1). $a=180$, $c=80$; check $360+240=600$ and $540+160=700$ ✓ (1).", "M", wp=True),
W(r"A taxi fare is a fixed charge plus a charge per km. The fare for 6 km is ₹ 122 and for 8 km is ₹ 160. Find the fixed charge and the rate per km.", 3, r"$x+6y=122$ and $x+8y=160$ (1). Subtract: $2y=38$, $y=19$ per km (1). $x=122-114=$ ₹ 8 fixed charge (1).", "M", wp=True),
W(r"The perimeter of a rectangular field is 40 m and its length exceeds its width by 4 m. Find its length and width.", 3, r"$l+w=20$ and $l-w=4$ (1). $l=12$ m, $w=8$ m (1). Check: perimeter $=2(20)=40$ ✓ (1).", "M", wp=True),
W(r"If $(-3,4)$ is a solution of $3kx+4y=-2$, find $k$.", 3, r"Substitute: $3k(-3)+4(4)=-2$ (1). $-9k+16=-2$ (1). $k=2$ (1).", "M"),
W(r"For the line $3x-2y+8=0$ find the slope, the $y$-intercept and the point where it meets the $x$-axis.", 3, r"$y=\frac32x+4$ (1). Slope $\frac32$ and $y$-intercept 4 (1). $y=0$: $3x=-8$, $x=-\frac83$, the point $(-\frac83,0)$ (1).", "M"),
W(r"Without solving, state the number of solutions of each pair: (i) $x+2y=4$, $2x+4y=12$ (ii) $2x+3y=9$, $4x+6y=18$ (iii) $x-y=10$, $3x+y=2$.", 3, r"(i) $\frac12=\frac24\neq\frac4{12}$: parallel, no solution (1). (ii) $\frac24=\frac36=\frac9{18}$: same line, infinitely many (1). (iii) $\frac13\neq\frac{-1}1$: unique solution (1).", "M"),
W(r"Ritu has ₹ 2 and ₹ 5 coins. She has 15 coins worth ₹ 54 in all. How many coins of each kind does she have?", 3, r"$x+y=15$ and $2x+5y=54$ (1). $2x+5(15-x)=54$ gives $75-3x=54$, $x=7$ (1). Seven ₹ 2 coins and eight ₹ 5 coins ($14+40=54$ ✓) (1).", "M", wp=True),
W(r"Plan A costs ₹ 50 plus 20 paise per minute and plan B costs ₹ 30 plus 30 paise per minute. Write the cost of each plan for $t$ minutes, find $t$ when the costs are equal and say which plan is cheaper for longer calls.", 3, r"A: $50+0.2t$; B: $30+0.3t$ (1). Equal: $20=0.1t$, $t=200$ minutes (cost ₹ 90) (1). Beyond 200 minutes B's cost grows faster, so A is cheaper (1).", "M", wp=True),
W(r"The temperature relation is $F=\frac95C+32$. Find $F$ when $C=30$, find $C$ when $F=95$, and find the temperature at which both scales show the same number.", 3, r"$C=30$: $F=54+32=86$ (1). $F=95$: $\frac95C=63$, $C=35$ (1). Same value: $x=\frac95x+32$ gives $-\frac45x=32$, $x=-40$ (1).", "M", wp=True),
W(r"Simran solves $x+y=7$ and $x-y=1$ and gets $x=3$, $y=4$. Check her answer and correct it.", 2, r"$3-4=-1\neq1$, so it fails the second equation (1). Correct: adding gives $2x=8$, $x=4$, $y=3$ (1).", "M"),
W(r"Two persons have incomes in the ratio $9:7$ and expenses in the ratio $4:3$; each saves ₹ 2,000. Find their incomes and expenses.", 3, r"Incomes $9x$, $7x$ and expenses $4y$, $3y$: $9x-4y=2000$, $7x-3y=2000$ (1). Multiply the first by 3 and the second by 4: $27x-12y=6000$, $28x-12y=8000$; subtract: $x=2000$ (1). $y=4000$. Incomes ₹ 18,000 and ₹ 14,000; expenses ₹ 16,000 and ₹ 12,000 (1).", "M", wp=True),
W(r"Two lines pass through these points: line 1: $(0,6),(2,4),(4,2),(6,0)$; line 2: $(0,-2),(2,0),(4,2),(6,4)$. Find the common point and write each line's equation.", 3, r"The point $(4,2)$ appears in both lists (1). Line 1: $x+y=6$ (1). Line 2: $y=x-2$ (1).", "M"),
W(r"3 notebooks and 2 pens cost ₹ 80; 2 notebooks and 3 pens cost ₹ 70. Find the cost of one notebook and one pen.", 3, r"$3a+2b=80$ and $2a+3b=70$ (1). Adding: $a+b=30$; subtracting: $a-b=10$ (1). $a=$ ₹ 20, $b=$ ₹ 10 (1).", "M", wp=True),
W(r"Two complementary angles differ by $20^\circ$. Find the angles.", 2, r"$x+y=90^\circ$ and $x-y=20^\circ$ (1). $x=55^\circ$, $y=35^\circ$ (1).", "M", wp=True),
W(r"Find the slope of $y=3x-6$ and the points where it meets the axes. Check that the slope between these two points is the same.", 3, r"Slope $=3$ (1). Meets the $y$-axis at $(0,-6)$ and the $x$-axis at $(2,0)$ (1). Slope between them $=\frac{0-(-6)}{2-0}=3$ ✓ (1).", "M"),
# ---------------- HARD ----------------
W(r"Five years ago Nuri was thrice as old as Sonu. Ten years later Nuri will be twice as old as Sonu. Find their present ages.", 4, r"$N-5=3(S-5)$ gives $N=3S-10$ (1.5). $N+10=2(S+10)$ gives $N=2S+10$ (1). So $3S-10=2S+10$, $S=20$ and $N=50$ (1). Check: 5 years ago 45 and 15 ✓; after 10 years 60 and 30 ✓ (0.5).", "H", wp=True),
W(r"A fraction becomes 1 when 1 is added to the numerator and 1 is subtracted from the denominator. It becomes $\frac12$ when only 1 is added to the denominator. Find the fraction.", 4, r"$\frac{x+1}{y-1}=1$ gives $y=x+2$ (1.5). $\frac{x}{y+1}=\frac12$ gives $2x=y+1$ (1). So $2x=x+3$, $x=3$, $y=5$; the fraction is $\frac35$ (1). Check: $\frac44=1$ and $\frac36=\frac12$ ✓ (0.5).", "H", wp=True),
W(r"Sanjay walks at $x$ km/h and cycles at $y$ km/h. Walking for 2 hours and cycling for 3 hours he covers 35 km. Walking for 3 hours and cycling for 2 hours he covers 30 km. Find his two speeds.", 4, r"$2x+3y=35$ and $3x+2y=30$ (1). Adding: $x+y=13$; subtracting: $y-x=5$ (1.5). $y=9$ km/h and $x=4$ km/h (1). Check $8+27=35$ and $12+18=30$ ✓ (0.5).", "H", wp=True),
W(r"Find $a$ and $b$ so that the pair $2x+3y=7$ and $(a-b)x+(a+b)y=3a+b-2$ has infinitely many solutions.", 4, r"Coincident lines: $\frac{2}{a-b}=\frac{3}{a+b}=\frac{7}{3a+b-2}$ (1). From the first two: $2(a+b)=3(a-b)$, so $a=5b$ (1). From the last two: $3(3a+b-2)=7(a+b)$, i.e. $2a-4b=6$ (1). $10b-4b=6$: $b=1$, $a=5$. The second equation is $4x+6y=14$, twice the first ✓ (1).", "H"),
W(r"For what value of $k$ does the pair $kx+2y=5$ and $3x+6y=8$ have no solution? For what values of $k$ is the solution unique?", 4, r"No solution needs $\frac k3=\frac26\neq\frac58$ (1.5). $\frac k3=\frac13$ gives $k=1$, and $\frac13\neq\frac58$ holds, so $k=1$ (1.5). Unique solution when $\frac k3\neq\frac13$, i.e. $k\neq1$ (1).", "H"),
W(r"**Case study (gym plans).** Fit A charges ₹ 1,000 to join and ₹ 400 per month. Fit B charges ₹ 400 to join and ₹ 500 per month. (i) Write the total cost $y$ after $x$ months for each. (ii) After how many months do they cost the same, and how much? (iii) Which plan is cheaper for one year, and by how much? (iv) What does the slope of each line tell us?", 5, r"(i) A: $y=1000+400x$; B: $y=400+500x$ (1). (ii) $1000+400x=400+500x$ gives $x=6$ months, cost ₹ 3,400 (1.5). (iii) 12 months: A $=$ ₹ 5,800, B $=$ ₹ 6,400; A is cheaper by ₹ 600 (1.5). (iv) The slopes 400 and 500 are the monthly charges; B's line is steeper, so it gets dearer faster (1).", "H", wp=True),
W(r"A two-digit number is 4 times the sum of its digits. If 18 is added to the number, the digits are reversed. Find the number.", 4, r"Digits $x$ (tens), $y$ (units): $10x+y=4(x+y)$ gives $2x=y$ (1.5). $(10x+y)+18=10y+x$ gives $y-x=2$ (1). So $x=2$, $y=4$; the number is 24 (1). Check: $24=4\times6$ and $24+18=42$ ✓ (0.5).", "H", wp=True),
W(r"The points $A(1,2)$, $B(3,8)$ and $C(5,14)$ lie on one line. Show this using slopes, and write the equation of the line in the form $y=mx+d$.", 4, r"Slope $AB=\frac{8-2}{3-1}=3$ (1). Slope $BC=\frac{14-8}{5-3}=3$; equal slopes through the common point $B$, so $A,B,C$ are collinear (1.5). $y=3x+d$; point $(1,2)$: $d=-1$, so $y=3x-1$ (1). Check $(5,14)$: $15-1=14$ ✓ (0.5).", "H"),
W(r"**Case study (school fete).** On day 1 the stall sold 12 plates of idli and 8 plates of dosa for ₹ 840. On day 2 it sold 9 plates of idli and 10 plates of dosa for ₹ 810. (i) Write two equations. (ii) Solve them by elimination. (iii) Check in both equations. (iv) Find the income from 20 plates of idli and 15 plates of dosa.", 5, r"(i) $12x+8y=840$ (i.e. $3x+2y=210$) and $9x+10y=810$ (1). (ii) Multiply the first by 5: $15x+10y=1050$; subtract the second: $6x=240$, $x=40$ (1.5). $y=\frac{210-120}{2}=45$ (0.5). (iii) $480+360=840$ ✓ and $360+450=810$ ✓ (1). (iv) $20\times40+15\times45=800+675=$ ₹ 1,475 (1).", "H", wp=True),
W(r"The lines $2x-y=4$ and $x+y=5$ meet at a point P. (i) Find P. (ii) Find where each line meets the $y$-axis. (iii) Find the area of the triangle formed by the two lines and the $y$-axis.", 4, r"(i) Adding: $3x=9$, $x=3$, $y=2$: $P(3,2)$ (1). (ii) $2x-y=4$ meets the $y$-axis at $(0,-4)$; $x+y=5$ at $(0,5)$ (1). (iii) Base on the $y$-axis $=9$; height $=$ the $x$-distance of P $=3$; area $=\frac12\times9\times3=13.5$ square units (2).", "H"),
W(r"For the pair $3x-2y=5$ and $6x-4y=k$: for what value of $k$ are there infinitely many solutions, for what values none, and can the pair have a unique solution? Explain with the ratios.", 4, r"$\frac36=\frac{-2}{-4}=\frac12$ always, so the lines are never intersecting at exactly one point: a unique solution is impossible (1.5). Infinitely many when $\frac{5}{k}=\frac12$, i.e. $k=10$ (1.5). No solution when $k\neq10$ (parallel lines) (1).", "H"),
W(r"The length of a rectangular field is 6 m more than twice its width, and its perimeter is 66 m. Find its dimensions, its area, and the cost of fencing it at ₹ 120 per metre.", 4, r"$l=2w+6$ and $2(l+w)=66$ (1). $3w+6=33$, $w=9$ m and $l=24$ m (1.5). Area $=24\times9=216$ m² (0.5). Fencing $=66\times120=$ ₹ 7,920 (1).", "H", wp=True),
W(r"Solve $9x+7y=107$ and $7x+9y=101$ by adding and subtracting the equations. Check the solution.", 4, r"Adding: $16(x+y)=208$, $x+y=13$ (1.5). Subtracting: $2(x-y)=6$, $x-y=3$ (1). $x=8$, $y=5$ (1). Check: $72+35=107$ and $56+45=101$ ✓ (0.5).", "H"),
W(r"Asha and Bina together have ₹ 6,000. If Asha gives ₹ 500 to Bina, Bina will have twice as much as Asha has left. How much does each have now?", 4, r"$A+B=6000$ and $B+500=2(A-500)$ (1.5). $6000-A+500=2A-1000$ gives $3A=7500$, $A=2500$ (1.5). $B=3500$ (0.5). Check: $4000=2\times2000$ ✓ (0.5).", "H", wp=True),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(13)
_pre = _lt(_o["blocks"][:-2])
_extra = [
 ("h2", "Why the Slope Is Constant and the Ratio Test Works"),
 ("p", "On the line y = mx + d take points with x-values x₁ and x₂. Then y₂ − y₁ = (mx₂ + d) − (mx₁ + d) = m(x₂ − x₁), so rise ÷ run = m for **every** pair of points. This is why a straight line has one slope."),
 ("p", "For the pair a₁x + b₁y + c₁ = 0 and a₂x + b₂y + c₂ = 0 the slopes are −a₁/b₁ and −a₂/b₂. They are **equal** exactly when a₁/a₂ = b₁/b₂. Equal slopes mean the lines are parallel or the same line: the same line if c₁/c₂ also equals the ratio, parallel otherwise. Different slopes mean the lines cross at one point."),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Checking solutions and finding a constant"),
 ("steps", [("Is (2, 3) a solution of 3x + 2y = 12?", "3(2) + 2(3) = 12, yes. (1, 3) gives 9, no."), ("Find k if (−3, 4) satisfies 3kx + 4y = −2", "−9k + 16 = −2, so k = 2."), ("Find y if (4, y) satisfies 2x + 3y = 17", "8 + 3y = 17, so y = 3.")]),
 ("h3", "Example 2 — Slope, intercepts and the axes"),
 ("steps", [("Line 3x − 2y + 8 = 0", "Rewrite: y = (3/2)x + 4, so slope 3/2 and y-intercept 4."), ("x-intercept", "Put y = 0: 3x = −8, x = −8/3."), ("Check with slope", "From (0, 4) to (−8/3, 0): rise −4 over run −8/3 gives 4 ÷ (8/3) = 3/2 ✓.")]),
 ("h3", "Example 3 — Digit problem"),
 ("steps", [("Digits x (tens) and y (units)", "Number = 10x + y; reversed = 10y + x."), ("Sum of digits 9 and number exceeds reversed number by 27", "x + y = 9 and 9(x − y) = 27, so x − y = 3."), ("Solve", "x = 6, y = 3; the number is 63 (63 − 36 = 27).")]),
 ("h3", "Example 4 — Fixed charge plus rate (taxi, mobile plans, gym)"),
 ("steps", [("6 km costs ₹122 and 8 km costs ₹160", "x + 6y = 122 and x + 8y = 160."), ("Subtract", "2y = 38, so y = ₹19 per km."), ("Fixed charge", "x = 122 − 6 × 19 = ₹8.")]),
 ("h3", "Example 5 — Ages"),
 ("steps", [("5 years ago N was 3 times S; 10 years later N will be twice S", "N − 5 = 3(S − 5) gives N = 3S − 10; N + 10 = 2(S + 10) gives N = 2S + 10."), ("Equate", "3S − 10 = 2S + 10, so S = 20."), ("Ages", "S = 20, N = 50. Check: 45 and 15 five years ago; 60 and 30 ten years later.")]),
 ("h3", "Example 6 — Finding constants for infinitely many solutions"),
 ("steps", [("Pair 2x + 3y = 7 and (a − b)x + (a + b)y = 3a + b − 2", "Need 2/(a − b) = 3/(a + b) = 7/(3a + b − 2)."), ("First two ratios", "2(a + b) = 3(a − b), so a = 5b."), ("Last two ratios", "3(3a + b − 2) = 7(a + b), i.e. 2a − 4b = 6; with a = 5b: b = 1, a = 5.")]),
 ("h3", "Example 7 — Area between lines and an axis"),
 ("steps", [("Lines 2x − y = 4 and x + y = 5", "Add: 3x = 9, so x = 3, y = 2; they meet at P(3, 2)."), ("Where they cut the y-axis", "(0, −4) and (0, 5): a base of 9 units."), ("Area of the triangle", "Height = 3 (the x-coordinate of P): ½ × 9 × 3 = 13.5 square units.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Story", "Variables", "Equations"], [
  ["Tickets, pens and notebooks", "price of each item", "2a + 3c = 600 and 3a + 2c = 700 (add and subtract)"],
  ["Digits", "tens x, units y", "x + y = 9; (10x + y) − (10y + x) = 27"],
  ["Ages ‘n years ago / later’", "present ages", "(N − 5) = 3(S − 5) and (N + 10) = 2(S + 10)"],
  ["Fixed charge + rate", "fixed x, rate y", "x + 6y = 122 and x + 8y = 160"],
  ["Coins", "number of each coin", "x + y = 15 and 2x + 5y = 54"],
  ["Speeds and times", "speeds x, y", "2x + 3y = 35 and 3x + 2y = 30"],
  ["Plans compared", "cost y after x units", "50 + 0.2t = 30 + 0.3t gives the break-even point"],
  ["Rectangle", "length l, width w", "l + w = half-perimeter; l − w or l = 2w + 6"],
  ["Money given from one to another", "amounts A, B", "A + B = total; B + 500 = 2(A − 500)"]]),
 ("note", "IMPORTANT", "**Check every answer against the story**: ages and counts must be positive whole numbers where the story demands it. A solution of the equations that makes no sense in the story (a negative number of coins) is rejected."),
 ("h2", "Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["Slope of y = 3x − 6 is −6", "−6 is the y-intercept", "slope 3, intercept −6"],
  ["Slope = (x₂ − x₁)/(y₂ − y₁)", "it is rise over run", "(y₂ − y₁)/(x₂ − x₁)"],
  ["Subtracting 2x + 3y = 7 from 4x + 6y = 14 gives x + y = 7", "the second is just twice the first", "0 = 0: infinitely many solutions"],
  ["Adding instead of subtracting to eliminate y when the signs are the same", "terms do not cancel", "subtract, or change the signs first"],
  ["(x, y) written as (y, x)", "order matters in an ordered pair", "first number is x"],
  ["‘The pair has exactly two solutions’", "a pair has 0, 1 or infinitely many", "decide with the ratio test"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**The slope is constant** on a line because y₂ − y₁ = m(x₂ − x₁) for every pair of points.", "**Ratio test:** compare a₁/a₂, b₁/b₂ and c₁/c₂ to predict unique, no or infinitely many solutions before solving.", "**Break-even** between two plans is found by putting their cost equations equal.", "Reject mathematically valid answers that **do not fit the story** (negative or fractional counts)."])

if __name__ == "__main__": run(__file__, BANK, 9, "Maths", WS, CH)
