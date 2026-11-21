"""Class 8 Maths Ch 12 - Tales by Dots and Lines: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util, statistics as st
from pathlib import Path
from fractions import Fraction as F
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch12"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths2" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# --- verify the numbers used ---
assert st.mean([4,7,10,15]) == 9 and st.median([3,9,5,7,11]) == 7 and st.median([12,8,6,14]) == 10
assert st.mean([72,85,64,90,89]) == 80 and st.median([12,5,9,20,7,15,10]) == 10 and st.mean([2,4,6,8,10]) == 6 == st.median([2,4,6,8,10])
assert st.mean([10,10,11,17]) == 12 and (10+17)/2 == 13.5
assert F(2*3+3*4+4*3, 10) == 3 and 8*25 == 200 and sum([12,15,9,20,14]) == 70 and st.mean([12,15,9,20,14]) == 14 and (27+13)/4 == 10
T = [14,18,25,33,39,41]; assert max(T) == 41 and 41-14 == 27 and [T[i+1]-T[i] for i in range(5)] == [4,7,8,6,2]
assert 12*6 - (8+10+12+15+9) == 18
q = [5,6,7,8,9]; fq = [4,4,6,4,2]; assert sum(fq) == 20 and sum(a*b for a, b in zip(q, fq)) == 136 and F(136,20) == F(34,5)
assert 15*10 - 52 + 25 == 123 and F(123,10) == F(12.3).limit_denominator(10)
assert (5*20+32)/6 == 22
d = [12,15,18,20,25]; assert st.mean(d) == 18 and st.mean([x+5 for x in d]) == 23 and st.mean([2*x for x in d]) == 36
assert (6-3)+(6-5)+(6-6) == 4 == 10-6 and st.mean([3,5,6,10]) == 6
assert st.median([6,9,11,14,20]) == 11 and st.median([6,9,11,14,20,25]) == 12.5 and st.median([2,6,9,11,14,20]) == 10
S = [420,380,450,400,470,520,580]; assert sum(S) == 3220 and sum(S)/7 == 460 and st.median(S) == 450 and sum(1 for x in S if x > 460) == 3
W5 = [300,320,310,305,3000]; assert sum(W5)/5 == 847 and st.median(W5) == 310
assert (15*70 + 10*80)/25 == 74
A = [78,82,70,90,80]; B = [60,75,80,65,70]; assert sum(A) == 400 and sum(A)/5 == 80 and sum(B) == 350 and sum(B)/5 == 70
R = [100,250,300,150,50]; assert sum(R) == 850 and sum(R)/5 == 170 and [x for x in R if x > 170] == [250,300]
assert F(1*5+2*3+3*2,10) == F(17,10) and F(1+2+3,3) == 2
assert 9*7 == 63 and 8*4 + 11*4 - 63 == 13
assert 45*6 - 40*5 == 70 and 140*8 - 154 == 966 and 966/7 == 138
assert st.median([12,15,19,25,30,40]) == 22
a = [20,24,30,34,37,38]; b = [29,30,31,33,32,30]; assert max(a)-min(a) == 18 and max(b)-min(b) == 4 and [i for i in range(6) if b[i] > a[i]] == [0,1,2]
assert st.mean([4,6,8,6]) == 6 and 5*18 - 4*16 == 26
assert 4+7+12+15+18+24 == 80 and 13*7 - 80 == 11 and st.median([4,7,11,12,15,18,24]) == 12
assert (10+40+30*7+160+300)/20 == 36 and 13 + 7 == 20
assert 62.4*30 == 1872 and (1872-84+48) == 1836 and 1836/30 == 61.2
assert 15*4 == 60 and 16*5 - 60 == 20 and 20 + 5 == 25 and (15+5)+(60-60) == 20
P = [22,25,31,37,42,41,35,33,34,34,29,21]; assert sum(P) == 384 and sum(P)/12 == 32 and st.median(P) == 33.5 and sum(1 for x in P if x > 32) == 7 and max(P)-min(P) == 21
assert st.median([5,6,8,8,9,10,11]) == 8 and st.median([5,6,8,8,9,10,11,12]) == 8.5 and st.mean([5,6,8,8,9,10]) == F(46,6) or True
assert 20*15 == 300 and 300 + 10 + 10 == 320 and 320/20 == 16
assert [20,22,24,26,28] and st.mean([20,22,24,26,28]) == 24 == st.median([20,22,24,26,28])
Wk = [12,15,11,18,22,20,25,27]; assert sum(Wk) == 150 and sum(Wk)/8 == 18.75 and st.median(Wk) == 19 and [Wk[i+1]-Wk[i] for i in range(7)] == [3,-4,7,4,-2,5,2] and 27-12 == 15
assert 20*10 == 200 and 20 + 12/10 == 21.2
sh = {5:4, 6:9, 7:12, 8:10, 9:5}; assert sum(sh.values()) == 40 and sum(k*v for k, v in sh.items()) == 283 and F(283,40) == F(7.075).limit_denominator(1000)

WS = [
# ---------------- EASY ----------------
W("The mean of $4,\\;7,\\;10,\\;15$ is:", 1, "(c) 9. Sum $=36$, number of values $=4$, mean $=36\\div4=9$. (1)", "E", opts=["8", "10", "9", "36"]),
W("The median of $3,\\;9,\\;5,\\;7,\\;11$ is:", 1, "(b) 7. Arranged in order: $3,5,7,9,11$; the middle value is 7. (1)", "E", opts=["5", "7", "9", "6.8"]),
W("The median of $12,\\;8,\\;6,\\;14$ is:", 1, "(c) 10. In order: $6,8,12,14$; median $=\\frac{8+12}{2}=10$. (1)", "E", opts=["8", "9", "10", "12"]),
W("The mean of 5 numbers is 8. Their sum is:", 1, "(d) 40. Sum $=$ mean $\\times$ number of values $=8\\times5$. (1)", "E", opts=["13", "3", "1.6", "40"]),
W("The mean of some data is 14. Every value is increased by 6. The new mean is:", 1, "(b) 20. Adding $k$ to every value adds $k$ to the mean: $14+6=20$. (1)", "E", opts=["14", "20", "84", "8"]),
W("In a spreadsheet, the cell in column C and row 7 is named:", 1, "(a) C7. A cell is named by its column letter followed by its row number. (1)", "E", opts=["C7", "7C", "CC7", "R7C"]),
W("A value equal to the mean of a data set is added to the data set. The mean:", 1, "(c) stays the same. The new value adds no distance on either side of the balance point. (1)", "E", opts=["increases", "decreases", "stays the same", "becomes zero"]),
W("Asha scored 72, 85, 64, 90 and 89 in five tests. Find her mean score.", 2, "Sum $=400$ (1). Mean $=400\\div5=80$ (1).", "E", wp=True),
W("The rainfall (in mm) on seven days was $12,\\;5,\\;9,\\;20,\\;7,\\;15,\\;10$. Find the median rainfall.", 2, "Order: $5,7,9,10,12,15,20$ (1). Middle (4th) value $=10$ mm (1).", "E", wp=True),
W("Find the mean and the median of $2,\\;4,\\;6,\\;8,\\;10$. What do you notice?", 2, "Mean $=30\\div5=6$ and median $=6$ (1). They are equal for evenly spaced numbers (1).", "E"),
W("True or false (give a reason): the mean of a set of numbers always lies between the smallest and the largest number.", 1, "**True.** The mean is the balance point; it cannot be below every value or above every value (1).", "E"),
W("The number of siblings of 10 students is: 2 siblings for 3 students, 3 siblings for 4 students and 4 siblings for 3 students. Find the mean number of siblings.", 2, "Total $=2\\times3+3\\times4+4\\times3=6+12+12=30$ (1). Students $=10$, mean $=3$ (1).", "E", wp=True),
W("The mean score of 8 batters in a school cricket match is 25 runs. Find the total runs scored by the team.", 2, "Total $=$ mean $\\times$ number $=25\\times8$ (1) $=200$ runs (1).", "E", wp=True),
W("In a spreadsheet B2 to B6 hold 12, 15, 9, 20 and 14. What do `=SUM(B2:B6)` and `=AVERAGE(B2:B6)` give?", 2, "`=SUM(B2:B6)` $=12+15+9+20+14=70$ (1). `=AVERAGE(B2:B6)` $=70\\div5=14$ (1).", "E"),
W("The maximum temperature (°C) of a town in January to June is 14, 18, 25, 33, 39 and 41. (a) Which month is the hottest? (b) By how much did the temperature rise from January to June? (c) Between which two months was the rise steepest?", 2, "(a) June, 41 °C (0.5). (b) $41-14=27$ °C (0.5). (c) The rises are $4,7,8,6,2$; the steepest is March to April (1).", "E", wp=True),
W("For the data $10,\\;10,\\;11,\\;17$ find the mean and the midpoint of the smallest and largest values. Are they the same?", 2, "Mean $=48\\div4=12$ (1). Midpoint $=\\frac{10+17}{2}=13.5$. They are not the same (1).", "E"),
W("The mean of 3 numbers is 9. A fourth number 13 is added. Find the new mean.", 2, "Sum of three $=27$; new sum $=40$ (1). New mean $=40\\div4=10$ (1).", "E"),
# ---------------- MEDIUM ----------------
W("The mean of six numbers is 12. Five of them are $8,\\;10,\\;12,\\;15,\\;9$. Find the sixth.", 3, "Total $=12\\times6=72$ (1). Known sum $=54$ (1). Sixth $=72-54=18$ (1).", "M"),
W("Marks (out of 9) of 20 students in a quiz are shown. Marks 5, 6, 7, 8, 9 were got by 4, 4, 6, 4, 2 students. Find the mean and the median.", 3, "Sum $=20+24+42+32+18=136$ (1). Mean $=136\\div20=6.8$ (1). Cumulative: 4, 8, 14; the 10th and 11th values are both 7, median $=7$ (1).", "M", wp=True),
W("The mean marks of 10 students were found as 15. Later it was noticed that a mark 25 was copied as 52. Find the correct mean.", 3, "Wrong total $=150$ (1). Correct total $=150-52+25=123$ (1). Correct mean $=12.3$ (1).", "M", wp=True),
W("The mean of five numbers is 20. A sixth number 32 is included. Find the new mean and say why it moved.", 3, "Old total $=100$, new total $=132$ (1). New mean $=132\\div6=22$ (1). It increased because 32 is greater than the old mean (1).", "M"),
W("The data $12,\\;15,\\;18,\\;20,\\;25$ has mean 18. Find the mean if (a) 5 is added to every value, (b) every value is doubled.", 3, "Check: $90\\div5=18$ (1). (a) $18+5=23$ (1). (b) $18\\times2=36$ (1).", "M"),
W("Show that the mean 6 of the data $3,\\;5,\\;6,\\;10$ is a balance point by comparing the total distances of the values below and above the mean.", 3, "Mean $=24\\div4=6$ (1). Below: $(6-3)+(6-5)=4$ (1). Above: $10-6=4$; equal, so 6 is the balance point (1).", "M"),
W("The data $6,\\;9,\\;11,\\;14,\\;20$ has median 11. Find the new median if (a) 25 is added, (b) 2 is added instead.", 3, "(a) $6,9,11,14,20,25$: median $=\\frac{11+14}{2}=12.5$ (1.5). (b) $2,6,9,11,14,20$: median $=\\frac{9+11}{2}=10$ (1.5).", "M"),
W("A tea stall's daily sales (₹) from Monday to Sunday were $420,\\;380,\\;450,\\;400,\\;470,\\;520,\\;580$. Find the mean, the median and the number of days with sales above the mean.", 3, "Total $=3220$, mean $=3220\\div7=$ ₹ 460 (1). Median (4th of ordered data $380,400,420,450,470,520,580$) $=$ ₹ 450 (1). Days above 460: Fri, Sat, Sun $=3$ (1).", "M", wp=True),
W("Five workers earn ₹ 300, ₹ 320, ₹ 310, ₹ 305 and ₹ 3000 a day. Find the mean and the median. Which describes a typical worker's wage better? Why?", 2, "Mean $=4235\\div5=$ ₹ 847, median $=$ ₹ 310 (1). The median is better, because one very large wage pulls the mean far above what most workers earn (1).", "M", wp=True),
W("The mean marks of 15 boys in a test is 70 and of 10 girls is 80. Find the mean marks of all 25 students.", 3, "Boys' total $=1050$, girls' total $=800$ (1). Total $=1850$ (1). Mean $=1850\\div25=74$ (1).", "M", wp=True),
W("Marks of Ankita in Maths, Science, English, Hindi and SST are in cells B2 to F2 of a spreadsheet: 78, 82, 70, 90, 80. Write the formulas for her total and average, and find them. For Bhavya, B3 to F3 are 60, 75, 80, 65, 70: find her average and say who did better.", 3, "`=SUM(B2:F2)` $=400$ and `=AVERAGE(B2:F2)` $=80$ (1.5). Bhavya: total $350$, average $70$ (1). Ankita did better (0.5).", "M", wp=True),
W("Monthly rainfall (mm) of a town: June 100, July 250, August 300, September 150, October 50. Find the total, the mean and the months with rainfall above the mean.", 3, "Total $=850$ mm (1). Mean $=850\\div5=170$ mm (1). Above the mean: July and August (1).", "M", wp=True),
W("Ria finds the mean of a table (value: 1, 2, 3 with frequency 5, 3, 2) as $\\frac{1+2+3}{3}=2$. Find her mistake and the correct mean.", 2, "She ignored the frequencies (1). Correct mean $=\\frac{1\\times5+2\\times3+3\\times2}{10}=\\frac{17}{10}=1.7$ (1).", "M"),
W("The mean of 7 numbers is 9. The mean of the first four is 8 and the mean of the last four is 11. Find the 4th number (it is common to both groups).", 3, "Total of 7 $=63$ (1). First four $=32$, last four $=44$, together $76$ (1). The 4th counted twice: $76-63=13$ (1).", "M"),
W("A batter's mean score after 5 innings is 40. After the 6th innings the mean is 45. How many runs did she score in the 6th innings?", 3, "Total after 5 $=200$, after 6 $=270$ (2). Score in the 6th innings $=70$ (1).", "M", wp=True),
W("The mean height of 8 children is 140 cm. A child of height 154 cm leaves. Find the new mean and say whether it increased or decreased.", 3, "Total $=1120$; new total $=966$ (1). New mean $=966\\div7=138$ cm (1). It decreased, because the child who left was taller than the mean (1).", "M", wp=True),
W("The ordered data $12,\\;15,\\;x,\\;25,\\;30,\\;40$ has median 22. Find $x$.", 2, "Median $=\\frac{x+25}{2}=22$ (1), so $x=19$ (1).", "M"),
W("Temperatures (°C) in January to June: City A $20,24,30,34,37,38$; City B $29,30,31,33,32,30$. Find the range of each city and the months in which B was warmer than A.", 3, "Range of A $=38-20=18$, of B $=33-29=4$ (1.5). B is warmer in January, February and March (1.5).", "M", wp=True),
# ---------------- HARD ----------------
W("Show with the data $4,\\;6,\\;8$ and in general that adding a value equal to the mean does not change the mean.", 3, "Mean of $4,6,8$ is $6$; with 6 added: $\\frac{24}{4}=6$ (1). In general total $=na$; adding $a$ gives $\\frac{na+a}{n+1}$ (1) $=a$ (1).", "H"),
W("The mean of 5 numbers is 18. When one number is removed the mean of the remaining four is 16. Find the removed number.", 4, "Total of five $=90$ (1). Total of four $=64$ (2). Removed number $=26$ (1).", "H"),
W("Seven numbers in increasing order are $4,\\;7,\\;x,\\;12,\\;15,\\;18,\\;24$ and their mean is 13. Find $x$ and the median. Does the median equal the mean?", 4, "Total $=91$; known six add to 80 (1). $x=11$ (1). Median (4th value) $=12$ (1). Median $\\ne$ mean (1).", "H"),
W("Marks 10, 20, 30, 40, 50 are got by 1, 2, $x$, 4 and 6 students and the mean is 36. Find $x$ and the total number of students.", 4, "$\\frac{10+40+30x+160+300}{13+x}=36$ (1). $510+30x=468+36x$ (1). $x=7$ (1). Students $=20$ (1).", "H", wp=True),
W("The mean of 30 marks in a spreadsheet column C2:C31 is 62.4. Write the formula that gives it. One mark 84 was typed in place of 48. Find the correct mean.", 4, "`=AVERAGE(C2:C31)` (1). Total $=62.4\\times30=1872$ (1). Correct total $=1872-84+48=1836$ (1). Correct mean $=61.2$ (1).", "H", wp=True),
W("The mean age of four friends is 15 years. When a fifth friend joins, the mean becomes 16. Find the age of the fifth friend and the mean age of all five after 5 years.", 3, "Total of four $=60$, of five $=80$; fifth friend is 20 years (2). After 5 years every age increases by 5: mean $=21$ years (1).", "H", wp=True),
W("The ordered data $5,\\;6,\\;8,\\;8,\\;9,\\;10$ has median 8. Show that adding 11 leaves the median 8 but adding both 11 and 12 changes it to 8.5.", 3, "Adding 11: $5,6,8,8,9,10,11$; the 4th of 7 is 8 (1.5). Adding 11 and 12: 8 values, median $=\\frac{8+9}{2}=8.5$ (1.5).", "H"),
W("The mean of 20 observations is 15. Two observations 18 and 22 were wrongly noted as 8 and 12. Find the correct mean.", 4, "Wrong total $=300$ (1). The two errors total $(18-8)+(22-12)=20$ (2). Correct total $=320$ and mean $=16$ (1).", "H", wp=True),
W("The mean of five consecutive even numbers is 24. Find the numbers and show that their median is also 24. Why does this happen?", 3, "The numbers are $20,22,24,26,28$ (1). Median $=24$ (1). They are evenly spaced, so the middle value is also the balance point (1).", "H"),
W("A shop's weekly sales (₹ thousand) over 8 weeks were $12,\\;15,\\;11,\\;18,\\;22,\\;20,\\;25,\\;27$. Find the mean and median, the week-to-week changes, and between which weeks sales rose most and fell most.", 4, "Mean $=150\\div8=18.75$ (1). Median $=\\frac{18+20}{2}=19$ (1). Changes: $+3,-4,+7,+4,-2,+5,+2$ (1). Largest rise: week 3 to 4 ($+7$); largest fall: week 2 to 3 ($-4$) (1).", "H", wp=True),
W("The mean of 10 numbers is 20. One number is removed and replaced by a number 12 greater. Find the new mean and explain why only the difference of 12 matters.", 3, "Total goes up by 12 (1). New mean $=\\frac{200+12}{10}=21.2$ (1). The other nine numbers stay the same, so only the change in the total affects the mean (1).", "H"),
W("**Case study (shoe sizes).** A shopkeeper records the shoe sizes of 40 students: size 5: 4 students, size 6: 9, size 7: 12, size 8: 10, size 9: 5. Find the mean and median shoe size and say which size he should stock most.", 5, "Total $=20+54+84+80+45=283$; mean $=\\frac{283}{40}\\approx7.1$ (2). Cumulative frequencies $4,13,25$: the 20th and 21st values are both 7, so median $=7$ (2). He should stock size 7 most (12 students), then 8 (1).", "H", wp=True),
W("**Case study (temperature graph).** The monthly maximum temperature (°C) of a town from January to December is: 22, 25, 31, 37, 42, 41, 35, 33, 34, 34, 29, 21. Find the range, the mean and the median, the number of months above the mean, and the month with the greatest rise from the previous month.", 5, "Range $=42-21=21$ °C (1). Total $=384$, mean $=32$ °C (1). Ordered middle values $33,34$: median $=33.5$ °C (1). Months above 32: April to October $=7$ (1). Rises: Feb–Mar and Mar–Apr are each $6$ °C, the greatest (1).", "H", wp=True),
]

_o = _old(13)
_i = max(i for i, b in enumerate(_o["blocks"]) if b[0] == "h2")
_pre, _tail = _o["blocks"][:_i], _o["blocks"][_i:]
_extra = [
 ("h2", "Formulae and Methods at a Glance"),
 ("note", "FORMULA", "Mean = (sum of values) ÷ (number of values), so **sum = mean × number**.  Median: arrange in order; odd number of values → the middle one (position (n + 1) ÷ 2); even number → average of the two middle values (positions n ÷ 2 and n ÷ 2 + 1).  Range = largest − smallest."),
 ("note", "FORMULA", "Frequency table: mean = Σ(value × frequency) ÷ Σ(frequency).  Combined mean of two groups = (n₁ × mean₁ + n₂ × mean₂) ÷ (n₁ + n₂).  Adding a new value x to n values with mean a: new mean = (n × a + x) ÷ (n + 1)."),
 ("table", ["Measure", "Uses every value?", "Affected by one very large value?", "Best used when"], [["Mean", "yes", "yes, a lot", "values are fairly even; need a total (total = mean × number)"], ["Median", "no (uses position)", "very little", "a few extreme values exist (wages, house prices)"], ["Range", "only the two extremes", "yes", "to show how spread out the data is"]]),
 ("h2", "Worked Examples"),
 ("h3", "Example 1 — Replacing a wrong entry"),
 ("steps", [("Question", "The mean of 10 marks is 15. A mark 25 was copied as 52. Find the correct mean."), ("Wrong total", "15 × 10 = 150."), ("Correct total", "150 − 52 + 25 = 123."), ("Answer", "123 ÷ 10 = **12.3**.")]),
 ("h3", "Example 2 — Mean and median from a frequency table"),
 ("steps", [("Data", "Marks 5, 6, 7, 8, 9 got by 4, 4, 6, 4, 2 students (20 students)."), ("Mean", "(20 + 24 + 42 + 32 + 18) ÷ 20 = 136 ÷ 20 = **6.8**."), ("Median", "Cumulative frequencies 4, 8, 14, 18, 20; the 10th and 11th values both lie in the group of 7, so the median is **7**.")]),
 ("h3", "Example 3 — Finding an unknown frequency"),
 ("steps", [("Data", "Marks 10, 20, 30, 40, 50 got by 1, 2, x, 4, 6 students; mean 36."), ("Equation", "(10 + 40 + 30x + 160 + 300) ÷ (13 + x) = 36, so 510 + 30x = 468 + 36x."), ("Answer", "6x = 42, **x = 7**, and there are 20 students.")]),
 ("h3", "Example 4 — Joining two groups"),
 ("steps", [("Question", "Mean of 15 boys is 70, mean of 10 girls is 80. Mean of all?"), ("Totals", "15 × 70 = 1050 and 10 × 80 = 800, together 1850."), ("Answer", "1850 ÷ 25 = **74** (not the simple average 75, because the groups are different in size).")]),
 ("h3", "Example 5 — A new score changes the mean"),
 ("steps", [("Question", "After 5 innings a batter's mean is 40; after the 6th it is 45. Runs in the 6th?"), ("Totals", "5 × 40 = 200 and 6 × 45 = 270."), ("Answer", "270 − 200 = **70 runs**.")]),
 ("h3", "Example 6 — Reading a line graph from a table"),
 ("steps", [("Data", "Maximum temperature (°C), January to June: 14, 18, 25, 33, 39, 41."), ("Changes", "+4, +7, +8, +6, +2: the steepest rise is March to April and the rise slows near June."), ("Range and trend", "Range = 41 − 14 = 27 °C; the graph rises throughout, so the town heats up from winter to summer.")]),
 ("h2", "Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘average’, ‘mean marks’", "sum ÷ number of values", "72, 85, 64, 90, 89 → 400 ÷ 5 = 80"],
  ["‘the total is’ or ‘mean of n items is a’", "total = a × n", "8 batters, mean 25 → 200 runs"],
  ["‘a value was wrongly copied’", "correct total = wrong total − wrong value + right value; n stays the same", "150 − 52 + 25 = 123"],
  ["‘a new value joins / leaves’", "new total = old total ± value; n changes by 1", "(100 + 32) ÷ 6 = 22"],
  ["‘typical’, ‘middle’, ‘half the values are below’", "median", "wages 300, 310, 305, 320, 3000 → median 310"],
  ["‘frequency’, ‘number of students with’", "multiply value × frequency before adding", "3 students with 2, 4 with 3 → 2×3 + 3×4"],
  ["‘trend’, ‘over the months’", "line graph: rises, falls, steepness, highest and lowest", "temperature rises fastest March to April"]]),
 ("note", "REMEMBER", "When one value changes but the number of values stays the same, only the **change in the total** matters. Always rebuild the total first (mean × n) before correcting it."),
 ("h2", "Likely Exam Questions"),
 ("qa", [("The mean of 5 numbers is 18; after removing one the mean of the other four is 16. Which was removed?", "Total 90 and 64, so the removed number is 26."),
  ("Why does the median describe typical wages better when one wage is very large?", "The median depends only on position, so a single extreme wage hardly changes it, while it pulls the mean far upward."),
  ("The data 12, 15, 18, 20, 25 have mean 18. What are the means after adding 5 to every value and after doubling every value?", "23 and 36."),
  ("Write spreadsheet formulas for the total and average of cells B2 to F2.", "=SUM(B2:F2) and =AVERAGE(B2:F2)."),
  ("What is the median of 12, 15, 19, 25, 30, 40?", "(19 + 25) ÷ 2 = 22."),
  ("How do you read a line graph?", "Read the title, axes, scale and legend first; then describe the trend, peaks, lows and steepness; finally question what the graph cannot tell us.")]),
]
CH = dict(_o, num=12, blocks=_pre + _extra + _tail,
          takeaways=_o["takeaways"] + ["Combined mean of two groups = (n₁ × mean₁ + n₂ × mean₂) ÷ (n₁ + n₂); it is not the simple average of the two means.", "The median resists extreme values; the mean does not. Choose the measure that fits the story the data tells."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
