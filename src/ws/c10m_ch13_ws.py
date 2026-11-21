"""Class 10 Maths Ch 13 - Statistics: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from math import isclose
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c10m_ch13"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c10_maths" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def T(head, *rows):
    """KaTeX table: head = list of header strings, rows = lists of cell strings."""
    n = len(head)
    s = r"$\begin{array}{|" + "c|" * n + r"}\hline " + " & ".join(r"\text{" + h + "}" for h in head) + r"\\\hline "
    for r in rows: s += " & ".join(str(c) for c in r) + r"\\\hline "
    return s + r"\end{array}$"

def stats(cls, f):
    N = sum(f); x = [(a + b) / 2 for a, b in cls]
    mean = sum(i * j for i, j in zip(x, f)) / N
    cf = 0
    for (a, b), fi in zip(cls, f):
        if cf + fi >= N / 2: med = a + (N / 2 - cf) / fi * (b - a); break
        cf += fi
    i = f.index(max(f)); a, b = cls[i]; f0 = f[i - 1] if i > 0 else 0; f2 = f[i + 1] if i < len(f) - 1 else 0
    return N, mean, med, a + (f[i] - f0) / (2 * f[i] - f0 - f2) * (b - a)
cl = lambda s, h, n: [(s + h * i, s + h * (i + 1)) for i in range(n)]
def rng(s, h, n): return [f"{s + h * i}-{s + h * (i + 1)}" for i in range(n)]
def tb(s, h, f, label="Class", flab="Frequency"):
    return T([label] + rng(s, h, len(f)), [flab] + [str(v) for v in f]).replace(r"\text{", r"\text{", 1)

# transposed table (classes across the top)
def tbl(s, h, f, label="Class", flab="Frequency"):
    n = len(f)
    top = r"$\begin{array}{|c|" + "c|" * n + r"}\hline \text{" + label + "} & " + " & ".join(rng(s, h, n)).replace("-", r"\text{–}") + r"\\\hline \text{" + flab + "} & " + " & ".join(str(v) for v in f) + r"\\\hline \end{array}$"
    return top

A = (cl(10, 10, 5), [5, 8, 12, 10, 5]); B = (cl(0, 20, 5), [6, 8, 14, 8, 4]); C = (cl(10, 20, 5), [4, 10, 16, 6, 4])
D = (cl(0, 10, 5), [7, 13, 20, 12, 8]); Ee = (cl(0, 10, 5), [4, 6, 15, 9, 6])
assert stats(*A)[:2] == (40, 35.5) and stats(*B)[1] == 48 and stats(*C)[1] == 58 and stats(*D)[2] == 25 and isclose(stats(*Ee)[3], 26)
assert isclose(stats(cl(0, 10, 4), [8, 12, 20, 10])[2], 22.5) and isclose(stats(cl(5, 10, 6), [6, 11, 21, 23, 14, 5])[3], 35 + 20 / 11)
assert isclose(stats(cl(0, 20, 5), [6, 4, 10, 4, 6])[3], 50) and isclose(stats(cl(0, 20, 5), [5, 10, 20, 10, 5])[2], 50)
assert isclose(stats(cl(0, 5, 5), [8, 16, 40, 24, 12])[1], 13.3) and isclose(stats(cl(0, 20, 5), [5, 9, 12, 8, 6])[2], 50)
assert isclose(stats(cl(0, 10, 5), [5, 10, 20, 9, 6])[1], 25.2) and isclose(stats(cl(0, 10, 5), [5, 10, 20, 9, 6])[2], 25)
assert isclose(stats(cl(0, 10, 5), [4, 13, 16, 9, 8])[2], 25) and 4 + 13 + 16 + 9 + 8 == 50
assert isclose(stats(cl(0, 20, 5), [17, 28, 32, 24, 19])[1], 50) and isclose(stats(cl(400, 100, 5), [12, 18, 30, 22, 18])[1], 666)
assert isclose(stats(cl(0, 20, 6), [5, 8, 10, 12, 7, 8])[1], 62.8) and isclose(stats(cl(0, 10, 5), [4, 6, 10, 20, 10])[2], 32.5)
assert isclose(stats(cl(0, 10, 5), [4, 6, 15, 9, 6])[1], 26.75) and isclose(stats(cl(0, 10, 5), [4, 6, 15, 9, 6])[2], 80 / 3)
assert isclose(stats(cl(0, 10, 5), [4, 6, 15, 9, 6])[3], 26) and 3 * 26.67 > 0 and 3 * 57 == 65 + 2 * 53 and 3 * 24 - 2 * 26 == 20
assert 3 * 13 == 9 + 30 and 3 * 27.2 - 2 * 26.4 > 28.7 and 25 * 36 == 900 and 13 * 32 + 13 * 40 - 900 == 36 and (20 * 60 + 30 * 70) / 50 == 66
assert 30 * 40 + 9 == 1209 and isclose(1209 / 30, 40.3) and 100 * 58 - 40 * 55 - 35 * 60 == 25 * 60 and 25 + 10 * (-15 / 50) == 22
assert isclose(20 + (25 - 14) / 12 * 10 - 0, 20 + 11 / 12 * 10) and 30 + (30 - 24) / 20 * 10 == 33
assert isclose(40 + (25 - 15) / 20 * 20 * 0 + 0, 40) and isclose(20 + (20 - 14) / 12 * 10, 25.0) and isclose(20.5 + (20 - 14) / 12 * 10, 25.5)
assert isclose(40 + (20 - 14) / 12 * 20, 50) and isclose(40 + (25 - 15) / 20 * 20, 50) and isclose(20 + (15 - 6) / (30 - 6 - 9) * 10, 26)
assert (50 + 40 + 20 * 0 == 90) and isclose(20 + (15 - 6) / (2 * 15 - 6 - 9) * 10, 26) and isclose(40 + (10 - 4) / (20 - 4 - 4) * 20, 50)

WS = [
# ---------------- EASY ----------------
W(r"The mean of grouped data by the direct method is given by:", 1, r"(a) $\bar x=\dfrac{\sum f_ix_i}{\sum f_i}$, where $x_i$ is the class mark. (1)", "E", opts=[r"$\dfrac{\sum f_ix_i}{\sum f_i}$", r"$\dfrac{\sum x_i}{\sum f_i}$", r"$\dfrac{\sum f_i}{\sum f_ix_i}$", r"$\sum f_ix_i\times\sum f_i$"]),
W(r"The class mark of the class $30\text{–}50$ is:", 1, r"(c) 40. Class mark $=\dfrac{30+50}2=40$. (1)", "E", opts=["20", "30", "40", "80"]),
W(r"The modal class of the following data is: " + tbl(0, 10, [3, 8, 15, 9], "Marks"), 1, r"(c) 20–30. It has the highest frequency, 15. (1)", "E", opts=["0–10", "10–20", "20–30", "30–40"]),
W(r"If the mode of a distribution is 9 and its mean is 15, then its median is (use $3\,\text{median}=\text{mode}+2\,\text{mean}$):", 1, r"(d) 13. $3\,\text{median}=9+30=39$, so median $=13$. (1)", "E", opts=["12", "11", "14", "13"]),
W(r"The median class of grouped data is the class:", 1, r"(b) whose cumulative frequency is the first one greater than or equal to $\dfrac N2$. (1)", "E", opts=["with the highest frequency", r"whose cumulative frequency is the first to reach or pass $\dfrac N2$", "in the middle of the table by position only", r"whose class mark is the mean"]),
W(r"In the step-deviation method, $u_i$ is defined as:", 1, r"(c) $\dfrac{x_i-a}h$, where $a$ is the assumed mean and $h$ the class size. (1)", "E", opts=[r"$x_i-h$", r"$\dfrac{x_i}h$", r"$\dfrac{x_i-a}h$", r"$a-x_i$"]),
W(r"For a data set $\sum f_i=50$ and $\sum f_ix_i=1750$. The mean is:", 1, r"(b) 35. $\bar x=\dfrac{1750}{50}=35$. (1)", "E", opts=["30", "35", "40", "3500"]),
W(r"Write the class marks of the classes $10\text{–}25$, $25\text{–}40$ and $40\text{–}55$.", 2, r"$\dfrac{10+25}2=17.5$ (½), $\dfrac{25+40}2=32.5$ (½), $\dfrac{40+55}2=47.5$ (1).", "E"),
W(r"The pocket money (in ₹) of 40 students is as follows. Find the mean by the direct method.\n" + tbl(10, 10, A[1], "Pocket money (₹)", "Students"), 2, r"Class marks 15, 25, 35, 45, 55; $\sum fx=75+200+420+450+275=1420$ (1). $\bar x=\dfrac{1420}{40}=35.5$, i.e. ₹ 35.50 (1).", "E", wp=True),
W(r"The marks of 40 students in a test are given below. Find the modal class and the mode.\n" + tbl(0, 10, Ee[1], "Marks", "Students"), 2, r"Modal class $20\text{–}30$ ($f_1=15$, $f_0=6$, $f_2=9$, $l=20$, $h=10$) (1). Mode $=20+\dfrac{15-6}{30-6-9}\times10=20+6=26$ (1).", "E", wp=True),
W(r"The daily wages (in ₹) of 60 workers are tabulated. Write the cumulative frequency column and name the median class.\n" + tbl(0, 10, D[1], "Wage (₹ hundreds)", "Workers"), 2, r"Cumulative frequencies: 7, 20, 40, 52, 60 (1). $\dfrac N2=30$; the first cumulative frequency $\ge30$ is 40, so the median class is $20\text{–}30$ (1).", "E", wp=True),
W(r"For a distribution the mean is 24 and the median is 22. Find the mode using the empirical relation.", 2, r"$\text{Mode}=3\,\text{median}-2\,\text{mean}$ (1) $=66-48=18$ (1).", "E"),
W(r"The frequencies of four classes are 3, 7, 12 and 8. Write the cumulative frequencies and the total number of observations $N$.", 2, r"Cumulative frequencies: 3, 10, 22, 30 (1). $N=30$ (1).", "E"),
W(r"The mean marks of 20 students in a quiz are 15. Find the total marks of the 20 students.", 2, r"$\text{Mean}=\dfrac{\sum fx}{\sum f}$ (1). $\sum fx=15\times20=300$ marks (1).", "E", wp=True),
W(r"True or false? Give a reason. The modal class of a frequency distribution is the class with the highest frequency.", 2, r"**True** (1). The mode lies in the class that occurs most often, i.e. with the maximum frequency (1).", "E"),
W(r"A shoe shop owner wants to decide which shoe size to stock the most. Which measure of central tendency (mean, median or mode) should he study, and why?", 2, r"The **mode** (1). It is the size that is sold most often, so stocking more of it matches demand (1).", "E", wp=True),
W(r"Students were asked how many hours they study daily. Class marks $x$ and frequencies $f$ are $x=1,3,5,7$ and $f=4,6,8,2$. Find $\sum f$, $\sum fx$ and the mean.", 2, r"$\sum f=20$ and $\sum fx=4+18+40+14=76$ (1). Mean $=\dfrac{76}{20}=3.8$ hours (1).", "E", wp=True),
# ---------------- MEDIUM ----------------
W(r"The marks of 40 students in a test of 100 are given. Find the mean by the assumed mean method (take $a=50$).\n" + tbl(0, 20, B[1], "Marks", "Students"), 3, r"Class marks 10, 30, 50, 70, 90; $d=x-50=-40,-20,0,20,40$ (1). $\sum fd=-240-160+0+160+160=-80$ (1). $\bar x=50+\dfrac{-80}{40}=48$ (1).", "M", wp=True),
W(r"The daily income (in ₹ hundreds) of 40 shopkeepers is given. Find the mean by the step-deviation method.\n" + tbl(10, 20, C[1], "Income", "Shopkeepers"), 3, r"Class marks 20, 40, 60, 80, 100; take $a=60$, $h=20$, $u=-2,-1,0,1,2$ (1). $\sum fu=-8-10+0+6+8=-4$ (1). $\bar x=60+20\times\dfrac{-4}{40}=58$ (1).", "M", wp=True),
W(r"The wages of 60 workers are shown. Find the median wage.\n" + tbl(0, 10, D[1], "Wage (₹ hundreds)", "Workers"), 3, r"$N=60$, $\dfrac N2=30$; cumulative frequencies 7, 20, 40, 52, 60 (1). Median class $20\text{–}30$: $l=20$, $cf=20$, $f=20$, $h=10$ (1). Median $=20+\dfrac{30-20}{20}\times10=25$, i.e. ₹ 2,500 (1).", "M", wp=True),
W(r"The time (minutes) taken by 50 students to reach school is given. Find the median time.\n" + tbl(0, 10, [8, 12, 20, 10], "Time", "Students"), 3, r"$\dfrac N2=25$; cumulative frequencies 8, 20, 40, 50 (1). Median class $20\text{–}30$, $cf=20$, $f=20$ (1). Median $=20+\dfrac{25-20}{20}\times10=22.5$ minutes (1).", "M", wp=True),
W(r"The ages of 80 patients visiting a clinic are given. Find the mode (to one decimal place).\n" + tbl(5, 10, [6, 11, 21, 23, 14, 5], "Age (yrs)", "Patients"), 3, r"Modal class $35\text{–}45$: $l=35$, $f_1=23$, $f_0=21$, $f_2=14$, $h=10$ (1). Mode $=35+\dfrac{23-21}{46-21-14}\times10$ (1) $=35+\dfrac{20}{11}\approx36.8$ years (1).", "M", wp=True),
W(r"The mean of the data below is 56. Find the missing frequency $p$. Class marks are 20, 40, 60, 80 with frequencies 4, 6, $p$, 8.", 3, r"$\sum f=18+p$; $\sum fx=80+240+60p+640=960+60p$ (1). $\dfrac{960+60p}{18+p}=56$ (1) $\Rightarrow960+60p=1008+56p$, $p=12$ (1).", "M", wp=True),
W(r"For 40 students the marks are given. Identify $l$, $cf$, $f$, $h$ for the median class and find the median.\n" + tbl(0, 20, [5, 9, 12, 8, 6], "Marks", "Students"), 3, r"$\dfrac N2=20$; cumulative frequencies 5, 14, 26, 34, 40, so median class $40\text{–}60$ (1). $l=40$, $cf=14$, $f=12$, $h=20$ (1). Median $=40+\dfrac{20-14}{12}\times20=50$ (1).", "M", wp=True),
W(r"For a moderately skewed distribution the mean is 26.4 and the median is 27.2. Find the mode.", 2, r"$\text{Mode}=3\,\text{median}-2\,\text{mean}$ (1) $=81.6-52.8=28.8$ (1).", "M"),
W(r"Kiran finds the mean of the data with class marks $x=15,25,35$ and frequencies $f=2,5,3$ as $\dfrac{15+25+35}3=25$. What is wrong? Find the correct mean.", 2, r"She ignored the frequencies (1). Correct mean $=\dfrac{\sum fx}{\sum f}=\dfrac{30+125+105}{10}=26$ (1).", "M"),
W(r"The weekly pocket money of 50 students is given. Find the median.\n" + tbl(0, 20, [5, 10, 20, 10, 5], "Money (₹)", "Students"), 3, r"$\dfrac N2=25$; cumulative frequencies 5, 15, 35, 45, 50 (1). Median class $40\text{–}60$: $l=40$, $cf=15$, $f=20$, $h=20$ (1). Median $=40+\dfrac{25-15}{20}\times20=50$, i.e. ₹ 50 (1).", "M", wp=True),
W(r"Write the continuous classes (class boundaries) for the inclusive classes $1\text{–}10$, $11\text{–}20$, $21\text{–}30$, and explain why this is needed before finding the median.", 2, r"$0.5\text{–}10.5$, $10.5\text{–}20.5$, $20.5\text{–}30.5$ (1). The median and mode formulas need continuous classes with no gaps, and the adjustment is half the gap on each side (1).", "M"),
W(r"The electricity used (units) by 30 households is given. Find the mode.\n" + tbl(0, 20, [6, 4, 10, 4, 6], "Units", "Households"), 3, r"Modal class $40\text{–}60$: $l=40$, $f_1=10$, $f_0=4$, $f_2=4$, $h=20$ (1). Mode $=40+\dfrac{10-4}{20-4-4}\times20$ (1) $=40+10=50$ units (1).", "M", wp=True),
W(r"The 'less than' cumulative frequencies of marks of 50 students are: less than 10: 5; less than 20: 15; less than 30: 35; less than 40: 45; less than 50: 50. Find the median.", 3, r"Class frequencies: 5, 10, 20, 10, 5 for classes $0\text{–}10,\dots,40\text{–}50$ (1). $\dfrac N2=25$, median class $20\text{–}30$, $cf=15$, $f=20$ (1). Median $=20+\dfrac{25-15}{20}\times10=25$ (1).", "M", wp=True),
W(r"In the step-deviation method the data has $\sum f=50$, assumed mean $a=25$, class size $h=10$ and $\sum fu=-15$. Find the mean.", 2, r"$\bar x=a+h\left(\dfrac{\sum fu}{\sum f}\right)$ (1) $=25+10\times\dfrac{-15}{50}=22$ (1).", "M"),
W(r"The mean of 30 numbers is 40. Later it was found that one number 43 had been copied as 34. Find the correct mean.", 2, r"Wrong sum $=30\times40=1200$ (½). Correct sum $=1200-34+43=1209$ (1). Correct mean $=\dfrac{1209}{30}=40.3$ (½).", "M", wp=True),
W(r"Class A has 20 students with mean marks 60 and class B has 30 students with mean marks 70. Find the mean marks of all 50 students together.", 2, r"Total marks $=20\times60+30\times70=1200+2100=3300$ (1). Combined mean $=\dfrac{3300}{50}=66$ (1).", "M", wp=True),
W(r"In a village, a few very rich families raise the mean income far above what most families earn. Explain which measure, the mean or the median, better describes a typical family, and why.", 2, r"The **median** (1). It depends on the middle position and is not pulled up by a few extremely high incomes, whereas the mean is (1).", "M", wp=True),
W(r"The waiting time (minutes) of 100 customers at a bank is given. Find the mean by the step-deviation method.\n" + tbl(0, 5, [8, 16, 40, 24, 12], "Time", "Customers"), 3, r"Class marks 2.5, 7.5, 12.5, 17.5, 22.5; take $a=12.5$, $h=5$, $u=-2,-1,0,1,2$ (1). $\sum fu=-16-16+0+24+24=16$ (1). $\bar x=12.5+5\times\dfrac{16}{100}=13.3$ minutes (1).", "M", wp=True),
W(r"For the median of grouped data, $N=60$, the cumulative frequency of the class before the median class is 24, the frequency of the median class is 20, its lower limit is 30 and its class size is 10. Find the median.", 2, r"Median $=l+\dfrac{\frac N2-cf}f\times h=30+\dfrac{30-24}{20}\times10$ (1) $=33$ (1).", "M"),
# ---------------- HARD ----------------
W(r"The following distribution has 50 observations and its median is 25. Find the missing frequencies $x$ and $y$.\n" + T(["Class", "0-10", "10-20", "20-30", "30-40", "40-50"], ["Frequency", "4", "x", "16", "y", "8"]), 4, r"$4+x+16+y+8=50\Rightarrow x+y=22$ (1). $\dfrac N2=25$ and the median class is $20\text{–}30$ with $cf=4+x$ (1). $25=20+\dfrac{25-(4+x)}{16}\times10\Rightarrow\dfrac{21-x}{16}=\dfrac12\Rightarrow x=13$ (1). Then $y=9$ (1).", "H"),
W(r"The mean of the distribution of 120 customers' bills is ₹ 50. Find the missing frequencies $f_1$ and $f_2$.\n" + T(["Bill (₹)", "0-20", "20-40", "40-60", "60-80", "80-100"], ["Customers", "17", r"f_1", "32", r"f_2", "19"]), 5, r"$17+f_1+32+f_2+19=120\Rightarrow f_1+f_2=52$ (1). $\sum fx=170+30f_1+1600+70f_2+1710=3480+30f_1+70f_2$ (1). Mean 50: $3480+30f_1+70f_2=6000\Rightarrow3f_1+7f_2=252$ (1). Substituting $f_1=52-f_2$: $156+4f_2=252$, $f_2=24$ (1), $f_1=28$ (1).", "H", wp=True),
W(r"For the marks of 40 students, find the mean, median and mode, and check how close $3\,\text{median}$ is to $\text{mode}+2\,\text{mean}$.\n" + tbl(0, 10, Ee[1], "Marks", "Students"), 5, r"Mean: $\sum fx=20+90+375+315+270=1070$, mean $=\dfrac{1070}{40}=26.75$ (2). Median: $\dfrac N2=20$, cumulative 4, 10, 25; class $20\text{–}30$; $20+\dfrac{20-10}{15}\times10=26.67$ (1). Mode $=26$ (1). $3\times26.67=80.0$ and $26+2\times26.75=79.5$, nearly equal (1).", "H", wp=True),
W(r"The daily wages (₹) of 100 workers are given. Find the mean wage by the step-deviation method.\n" + tbl(400, 100, [12, 18, 30, 22, 18], "Wage (₹)", "Workers"), 4, r"Class marks 450, 550, 650, 750, 850; $a=650$, $h=100$, $u=-2,-1,0,1,2$ (1). $fu=-24,-18,0,22,36$, $\sum fu=16$ (2). $\bar x=650+100\times\dfrac{16}{100}=₹\,666$ (1).", "H", wp=True),
W(r"For a moderately skewed distribution the mean is 53 and the mode is 65. Find the median and say whether the data is skewed to the right or left.", 3, r"$3\,\text{median}=\text{mode}+2\,\text{mean}=65+106=171$, median $=57$ (2). Mean < median < mode, so the long tail is on the left (skewed left) (1).", "H"),
W(r"The marks of 40 students are given in inclusive classes. Convert to continuous classes and find the median.\n" + tbl(1, 10, [5, 9, 12, 8, 6], "Marks", "Students").replace("1-10", "1\\text{–}10"), 4, r"Continuous classes: $0.5\text{–}10.5$, $10.5\text{–}20.5$, $20.5\text{–}30.5$, $30.5\text{–}40.5$, $40.5\text{–}50.5$ (1). Cumulative: 5, 14, 26, 34, 40; $\dfrac N2=20$, median class $20.5\text{–}30.5$ (1). Median $=20.5+\dfrac{20-14}{12}\times10$ (1) $=25.5$ (1).", "H", wp=True),
W(r"**Case study.** The marks of 50 students in the unit test are:\n" + tbl(0, 10, [5, 10, 20, 9, 6], "Marks", "Students") + r"\n(i) Write the cumulative frequencies. (ii) Find the median marks. (iii) Find the mean by the assumed mean method with $a=25$. (iv) Is the median close to the mean? What does that suggest?", 5, r"(i) 5, 15, 35, 44, 50 (1). (ii) $\dfrac N2=25$, class $20\text{–}30$: $20+\dfrac{25-15}{20}\times10=25$ (1). (iii) $d=-20,-10,0,10,20$; $\sum fd=-100-100+0+90+120=10$; mean $=25+\dfrac{10}{50}=25.2$ (2). (iv) Yes, 25 and 25.2 are nearly equal, so the marks are spread nearly symmetrically about the middle (1).", "H", wp=True),
W(r"The mean of 25 observations is 36. If the mean of the first 13 observations is 32 and of the last 13 is 40, find the 13th observation.", 3, r"Sum of 25 $=25\times36=900$ (1). Sum of first 13 $+$ sum of last 13 $=416+520=936$, which counts the 13th observation twice (1). 13th $=936-900=36$ (1).", "H", wp=True),
W(r"The mode of the following distribution of 40 marks is 26. Find the missing frequency $x$.\n" + T(["Marks", "0-10", "10-20", "20-30", "30-40", "40-50"], ["Frequency", "4", "6", "x", "9", "6"]), 3, r"Modal class $20\text{–}30$ ($f_0=6$, $f_1=x$, $f_2=9$) (1). $26=20+\dfrac{x-6}{2x-6-9}\times10\Rightarrow0.6=\dfrac{x-6}{2x-15}$ (1). $0.6(2x-15)=x-6\Rightarrow1.2x-9=x-6\Rightarrow x=15$ (1).", "H"),
W(r"The mean of the following distribution of 50 customers' ages is 62.8. Find the missing frequencies $f_1$ and $f_2$.\n" + T(["Age", "0-20", "20-40", "40-60", "60-80", "80-100", "100-120"], ["Customers", "5", r"f_1", "10", r"f_2", "7", "8"]), 5, r"$f_1+f_2=50-30=20$ (1). $\sum fx=50+30f_1+500+70f_2+630+880=2060+30f_1+70f_2$ (1). Mean 62.8: total $=50\times62.8=3140$, so $30f_1+70f_2=1080$, i.e. $3f_1+7f_2=108$ (1). Substitute $f_1=20-f_2$: $60+4f_2=108$, $f_2=12$ (1), $f_1=8$ (1).", "H", wp=True),
W(r"The 'more than' cumulative frequencies of the marks of 50 students are: more than 0: 50; more than 10: 46; more than 20: 40; more than 30: 30; more than 40: 10. Find the median marks.", 4, r"Class frequencies: $0\text{–}10$: $50-46=4$; $10\text{–}20$: 6; $20\text{–}30$: 10; $30\text{–}40$: 20; $40\text{–}50$: 10 (2). $\dfrac N2=25$; cumulative 4, 10, 20, 40, so median class $30\text{–}40$ (1). Median $=30+\dfrac{25-20}{20}\times10=32.5$ (1).", "H", wp=True),
W(r"Three sections of Class X have 40, 35 and 25 students. The mean marks of the first two are 55 and 60 and the mean of all 100 students is 58. Find the mean marks of the third section.", 3, r"Total marks of all $=100\times58=5800$ (1). First two sections $=40\times55+35\times60=2200+2100=4300$ (1). Third section total $=1500$, mean $=\dfrac{1500}{25}=60$ (1).", "H", wp=True),
W(r"The mean of a distribution is 27. Every observation is multiplied by 2 and then increased by 3. Find the new mean and justify.", 3, r"New observations $y_i=2x_i+3$ (1). $\bar y=\dfrac{\sum f_i(2x_i+3)}{\sum f_i}=2\bar x+3$ (1) $=2\times27+3=57$ (1).", "H"),
W(r"For a distribution the mean is 26 and the median is 24. Find the mode, and arrange mean, median and mode in order. What does the order suggest?", 3, r"$\text{Mode}=3(24)-2(26)=20$ (1). Order: mode $<$ median $<$ mean, i.e. $20<24<26$ (1). The long tail is on the higher side (skewed right) (1).", "H"),
]
for _w in WS:
    _w["q"] = _w["q"].replace("**", "").replace(r"\n", " "); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(13)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "13.6 More Worked Examples"),
 ("h3", "Example 1 — Mean by the direct method"),
 ("steps", [("Pocket money (₹): classes 10–20, 20–30, 30–40, 40–50, 50–60 with frequencies 5, 8, 12, 10, 5", "Class marks x: 15, 25, 35, 45, 55. Σf = 40."), ("Products f·x", "75, 200, 420, 450, 275; Σfx = 1420."), ("Mean", "1420 ÷ 40 = **₹ 35.50**.")]),
 ("h3", "Example 2 — Assumed mean method"),
 ("steps", [("Classes 0–20, …, 80–100 with f = 6, 8, 14, 8, 4. Take a = 50", "x = 10, 30, 50, 70, 90, so d = x − 50 = −40, −20, 0, 20, 40."), ("Σfd", "−240 − 160 + 0 + 160 + 160 = −80, Σf = 40."), ("Mean", "50 + (−80/40) = **48**.")]),
 ("h3", "Example 3 — Step-deviation method"),
 ("steps", [("Classes 400–500, …, 800–900 with f = 12, 18, 30, 22, 18; take a = 650, h = 100", "u = (x − 650)/100 = −2, −1, 0, 1, 2."), ("Σfu", "−24 − 18 + 0 + 22 + 36 = 16, Σf = 100."), ("Mean", "650 + 100 × (16/100) = **₹ 666**.")]),
 ("h3", "Example 4 — Median of grouped data"),
 ("steps", [("Wages: 0–10, 10–20, 20–30, 30–40, 40–50 with f = 7, 13, 20, 12, 8", "N = 60, N/2 = 30. Cumulative frequencies: 7, 20, 40, 52, 60."), ("Median class", "The first cumulative frequency ≥ 30 is 40, so the class is 20–30: l = 20, cf = 20, f = 20, h = 10."), ("Median", "20 + (30 − 20)/20 × 10 = **25**.")]),
 ("h3", "Example 5 — Mode of grouped data"),
 ("steps", [("Marks: 0–10, 10–20, 20–30, 30–40, 40–50 with f = 4, 6, 15, 9, 6", "Modal class: 20–30 (highest f = 15). f₁ = 15, f₀ = 6, f₂ = 9, l = 20, h = 10."), ("Mode", "20 + (15 − 6)/(30 − 6 − 9) × 10 = 20 + 6 = **26**.")]),
 ("h3", "Example 6 — Finding missing frequencies"),
 ("steps", [("Median = 25, N = 50, f = 4, x, 16, y, 8 for 0–10 … 40–50", "Total: 28 + x + y = 50, so x + y = 22."), ("Median class 20–30", "25 = 20 + (25 − (4 + x))/16 × 10, so (21 − x)/16 = ½ and x = 13."), ("Answer", "x = **13**, y = **9**.")]),
 ("h2", "13.7 Word Problems: How to Translate"),
 ("table", ["Question wording", "Measure", "Remark"], [
  ["‘average’, ‘on average’, ‘total divided equally’", "mean", "use Σfx ÷ Σf; combined mean = Σ(n × mean) ÷ Σn"],
  ["‘middle value’, ‘half the students score below’", "median", "find N/2 and the cumulative frequency; not affected by extremes"],
  ["‘most common’, ‘most popular size’, ‘maximum number of’", "mode", "identify the modal class (highest f) first"],
  ["‘a few very high incomes’", "median preferred", "the mean is pulled up by extreme values"],
  ["‘wrongly copied / misread value’", "correct the total", "new sum = old sum − wrong + right; recompute the mean"],
  ["classes 1–10, 11–20, …", "inclusive classes", "convert to 0.5–10.5, 10.5–20.5 before median or mode"]]),
 ("note", "IMPORTANT", "Always work with **continuous classes** for median and mode, and write down N, cf, f, h, l before substituting. When finding a missing frequency, use the **total** first (Σf) and then the mean, median or mode condition."),
 ("h2", "13.8 Choosing the Method for the Mean"),
 ("table", ["Method", "When to use", "Formula"], [
  ["Direct", "numbers are small", "x̄ = Σfx / Σf"],
  ["Assumed mean", "class marks are large", "x̄ = a + Σfd / Σf, d = x − a"],
  ["Step deviation", "class marks are large and have a common factor (class size h)", "x̄ = a + h × Σfu / Σf, u = (x − a)/h"]]),
 ("h2", "13.9 Common Mistakes"),
 ("table", ["Mistake", "Why it is wrong", "Correct idea"], [
  ["Using Σx / n instead of Σfx / Σf", "ignores frequencies", "multiply each class mark by its frequency"],
  ["Taking the class with highest cf as the median class", "median class is where cf first reaches N/2", "compute N/2 and compare"],
  ["Using N instead of N/2 in the median formula", "median is the middle value", "N/2 − cf"],
  ["Using cf of the median class (not the one before it)", "cf in the formula is for the class **before**", "list cumulative frequencies carefully"],
  ["Using inclusive limits for median or mode", "gaps change l and h", "convert to continuous classes"],
  ["Forgetting to multiply by h in the step-deviation formula", "u is in units of h", "x̄ = a + h × (Σfu/Σf)"]]),
]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["For the **median**, find N/2 first, then the first class whose cumulative frequency reaches it; use the cumulative frequency of the class **before** it.", "To find a **missing frequency**, use Σf first and then the given mean, median or mode.", "A **combined mean** is Σ(n × mean) ÷ Σn; a corrected mean needs the corrected total.", "Prefer the **median** when a few extreme values distort the mean, and the **mode** for the most common size or item."])

if __name__ == "__main__": run(__file__, BANK, 10, "Maths", WS, CH)
