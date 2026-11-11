"""Class 8 Maths Ch 12 - Tales by Dots and Lines (data handling: mean, median, mode, range, dot plots, line graphs)."""
import random, statistics as st
from c8m_u import *

SLUG, NAME, CHNO = "Dots_and_Lines", "Tales by Dots and Lines", 12

def I(x):
    x = Fr(x); assert x.denominator == 1, x; return int(x)
def gen(seed, n, lo, hi, intmean=True, distinct=True):
    rng = random.Random(seed)
    while True:
        d = [rng.randint(lo, hi) for _ in range(n)]
        if distinct and len(set(d)) < n: continue
        if intmean and sum(d) % n: continue
        return d
def gen_mode(seed, n, lo, hi, k=3):
    rng = random.Random(seed)
    while True:
        d = [rng.randint(lo, hi) for _ in range(n - k)]
        if len(set(d)) < n - k: continue
        m = rng.choice(d); d = d + [m] * (k - 1)
        # mode m must appear k times exactly -> ensure m appears once in base
        if d.count(m) != k: continue
        rng.shuffle(d); return d, m
def L(d): return ", ".join(map(str, d))
def mean(d): return Fr(sum(d), len(d))
def med(d):
    s = sorted(d); n = len(s)
    return Fr(s[n // 2]) if n % 2 else Fr(s[n // 2 - 1] + s[n // 2], 2)
def uniq(items):
    seen = set(); out = []
    for it in items:
        k = it["q"] + "|".join(it.get("opts") or [])
        if k not in seen: seen.add(k); out.append(it)
    return out

# ================= EASY =================
e1 = [ND(f"The mean of {L(d)} is:", mean(d), f"Sum $={sum(d)}$; $\\div{len(d)}$") for d in [gen(s, 5, 5, 30) for s in range(100, 108)]]
e2 = [ND(f"The median of {L(d)} is:", med(d), "Arrange in order; take the middle value", wrong=[mean(d), sorted(d)[0], d[len(d) // 2]]) for d in [gen(s, 7, 4, 40, False) for s in range(110, 116)]]
e3 = []
for s in range(120, 126):
    d, m = gen_mode(s, 8, 2, 20)
    e3.append(ND(f"The mode of {L(d)} is:", m, "Most frequent value", wrong=[max(d), min(d), sorted(d)[len(d) // 2]]))
e4 = [ND(f"The range of {L(d)} is:", max(d) - min(d), "Highest − lowest", wrong=[max(d), sum(d) // len(d), max(d) + min(d)]) for d in [gen(s, 6, 3, 60, False) for s in range(130, 136)]]
e5 = [ND(f"The mean of {n} numbers is {m}. Their sum is:", n * m, "Sum = mean × number of values", wrong=[n + m, m // n if m % n == 0 else m + 1, n * m + n]) for n, m in [(6, 15), (8, 12), (10, 25), (7, 18), (9, 14), (5, 32)]]
e6 = [M4("In a dot plot each dot represents:", "one observation", ["the mean", "ten observations", "the median"], "One dot per data value"),
      M4("The most frequently occurring value in a data set is the:", "mode", ["mean", "median", "range"], "Definition of mode"),
      M4("The difference between the largest and smallest value is the:", "range", ["mode", "mean", "median"], "Definition of range"),
      M4("A line graph is best for showing:", "change over time", ["parts of a whole", "names of people", "a single number"], "Trend"),
      M4("If all values of a data set are equal to 7, the mean is:", "7", ["0", "14", "49"], "Mean of equal values"),
      M4("The middle value of arranged data (odd number of values) is the:", "median", ["mode", "range", "total"], "Definition of median")]
EASY_A = [e1, e2, e3, e4, e5, e6]
EASY_B = ([Q(f"Find the mean of {L(d)}.", f"Sum $={sum(d)}$ (1); mean $={sum(d)}\\div{len(d)}={g(mean(d))}$ (1).", "1+1") for d in [gen(s, 5, 10, 50) for s in range(140, 144)]]
          + [Q(f"Find the median of {L(d)}.", f"Ascending order: {L(sorted(d))} (1); median $={g(med(d))}$ (1).", "1+1") for d in [gen(s, 7, 5, 60, False) for s in range(145, 149)]]
          + [Q(f"Find the range and the mode of {L(d)}.", f"Range $={max(d)}-{min(d)}={max(d)-min(d)}$ (1); mode $={m}$ (1).", "1+1") for d, m in [gen_mode(s, 8, 3, 25) for s in range(150, 154)]])
EASY_C = ([Q(f"The marks of 6 students are {L(d)}. Find the mean mark and the number of students who scored above the mean.", f"Mean $={sum(d)}\\div6={g(mean(d))}$ (2); students above mean $={sum(1 for x in d if x > mean(d))}$ (1).", "2+1") for d in [gen(s, 6, 20, 90) for s in range(160, 166)]]
          + [Q(f"Arrange the data {L(d)} in ascending order and find its median.", f"Ascending: {L(sorted(d))} (1); {len(d)} values, middle one is the {len(d)//2+1}th (1); median $={g(med(d))}$ (1).", "1+1+1") for d in [gen(s, 9, 6, 70, False) for s in range(170, 176)]]
          + [Q(f"The temperatures (°C) at 6 am, 9 am, 12 noon and 3 pm were {t[0]}, {t[1]}, {t[2]} and {t[3]}. Between which two consecutive times was the rise greatest, and what was the rise?", f"Rises: {t[1]-t[0]}, {t[2]-t[1]}, {t[3]-t[2]} (2); greatest rise {max(t[1]-t[0], t[2]-t[1], t[3]-t[2])}°C (1).", "2+1") for t in [(14, 18, 25, 28), (12, 15, 24, 27), (16, 19, 22, 31), (10, 17, 21, 24), (18, 20, 29, 33), (11, 13, 20, 30)]])
EASY_D = ([Q(f"For the data {L(d)}, find the mean, median, mode and range.", f"Mean $={g(mean(d))}$ (1); median $={g(med(d))}$ (2); mode $={m}$ (1); range $={max(d)-min(d)}$ (1).", "1+2+1+1") for d, m in [(lambda z: (z[0], z[1]))(gen_mode(s, 7, 4, 30, 2)) for s in range(180, 186)]]
          + [Q(f"The mean of 5 numbers is {m}. Four of them are {L(k)}. Find the fifth number.", f"Sum of five $=5\\times{m}={5*m}$ (2); sum of four $={sum(k)}$ (1); fifth $={5*m-sum(k)}$ (2).", "2+1+2") for m, k in [(20, [12, 18, 25, 30]), (15, [10, 14, 22, 9]), (30, [28, 35, 22, 31]), (12, [8, 15, 11, 14]), (45, [40, 52, 38, 50]), (24, [20, 26, 18, 30])]])

# ================= NCERT =================
n1 = [ND(f"The median of {L(d)} is:", med(d), "Even number of values: mean of the two middle values", wrong=[sorted(d)[len(d) // 2], sorted(d)[len(d) // 2 - 1], mean(d)]) for d in [gen(s, 8, 5, 50, False) for s in range(200, 206)]]
n2 = [ND(f"The mean of {len(k)+1} numbers is {m}. If {len(k)} of them are {L(k)}, the remaining number is:", (len(k) + 1) * m - sum(k), "Total − known sum", wrong=[m, sum(k) // len(k), (len(k) + 1) * m - sum(k) + 5]) for m, k in [(16, [12, 18, 20, 10]), (25, [30, 22, 28, 20, 24]), (40, [35, 42, 48]), (18, [15, 20, 19, 12, 22]), (50, [45, 55, 60, 38]), (33, [30, 36, 28])]]
n3 = []
for s_ in range(210, 900):
    if len(n3) >= 6: break
    n_ = 5; x = [50, 8, 36, 62, 12, 90, 24, 70][s_ % 8]; d = gen(s_, n_, 10, 40)
    if (sum(d) + x) % (n_ + 1) == 0: n3.append(ND(f"The mean of {n_} observations {L(d)} is {g(mean(d))}. If a new observation {x} is added, the new mean is:", Fr(sum(d) + x, n_ + 1), f"New sum ${sum(d)+x}$, new count ${n_+1}$", wrong=[mean(d), mean(d) + x, mean(d) + 3]))
assert len(n3) >= 5, len(n3)
def rise_tab(seed):
    rng = random.Random(seed); v = [rng.randint(5, 12)]
    while True:
        v = [rng.randint(4, 12)]
        for _ in range(5): v.append(v[-1] + rng.randint(-3, 7))
        diffs = [v[i + 1] - v[i] for i in range(5)]
        if min(v) > 0 and diffs.count(max(diffs)) == 1 and max(diffs) > 2: return v, diffs
n4 = []
for s in range(230, 236):
    v, df = rise_tab(s)
    n4.append(M4(f"A plant's height (cm) at the end of weeks 1 to 6 is {L(v)}. Between which two consecutive weeks was the growth the greatest?", f"Between week {df.index(max(df))+1} and week {df.index(max(df))+2}", [f"Between week {i+1} and week {i+2}" for i in range(5) if i != df.index(max(df))][:3], f"Growth in each week: {L(df)}; largest is {max(df)}"))
n5 = []
for s in range(240, 246):
    rng = random.Random(s); fr_ = {k: rng.randint(1, 9) for k in range(3, 9)}
    top = max(fr_, key=fr_.get)
    if list(fr_.values()).count(fr_[top]) > 1: fr_[top] += 1
    ds = ", ".join(f"{fr_[k]} dot{'s' if fr_[k] > 1 else ''} at {k}" for k in fr_)
    n5.append(M4(f"A dot plot shows: {ds}. The mode of the data is:", top, [k for k in fr_ if k != top][:3], f"The value with most dots is {top}"))
n6 = []
for s in range(250, 300):
    if len(n6) >= 6: break
    rng = random.Random(s); xs = sorted(rng.sample(range(2, 12), 4)); fs = [rng.randint(1, 6) for _ in xs]
    if sum(x * f for x, f in zip(xs, fs)) % sum(fs): continue
    n6.append(ND("The values " + L(xs) + " occur " + L(fs) + " times respectively. The mean is:", Fr(sum(x * f for x, f in zip(xs, fs)), sum(fs)), f"$\\sum xf={sum(x*f for x,f in zip(xs,fs))}$, $\\sum f={sum(fs)}$", wrong=[mean(xs), sum(xs), Fr(sum(fs), len(fs))]))
NCERT_A = [n1, n2, n3, n4, n5, n6]
NCERT_B = ([Q(f"Find the median of {L(d)}.", f"Ascending: {L(sorted(d))} (1); mean of the two middle values $={g(med(d))}$ (1).", "1+1") for d in [gen(s, 6, 8, 60, False) for s in range(260, 264)]]
           + [Q(f"The mean of 4 numbers is {m}. Three of them are {L(k)}. Find the fourth.", f"Total $=4\\times{m}={4*m}$ (1); fourth $={4*m}-{sum(k)}={4*m-sum(k)}$ (1).", "1+1") for m, k in [(27, [20, 31, 25]), (36, [40, 33, 29]), (19, [15, 22, 18]), (52, [48, 60, 45])]]
           + [Q(f"Each of the data values {L(d)} is increased by {c}. Find the old and the new mean.", f"Old mean $={g(mean(d))}$ (1); new mean $={g(mean(d)+c)}$ (adds {c}) (1).", "1+1") for d, c in [(gen(s, 5, 6, 30), c) for s, c in zip(range(264, 268), [4, 7, 10, 3])]])
NCERT_C = ([Q(f"The runs scored by a batter in 6 innings are {L(d)}. Find the mean, the median and the range.", f"Mean $={g(mean(d))}$ (1); median $={g(med(d))}$ (1); range $={max(d)-min(d)}$ (1).", "1+1+1") for d in [gen(s, 6, 10, 90) for s in range(270, 276)]]
           + [Q("The marks " + L(xs) + " were obtained by " + L(fs) + " students respectively. Find the mean mark.", f"$\\sum xf={sum(x*f for x,f in zip(xs,fs))}$ (1); $\\sum f={sum(fs)}$ (1); mean $={g(Fr(sum(x*f for x,f in zip(xs,fs)),sum(fs)))}$ (1).", "1+1+1") for xs, fs in [([4, 5, 6, 7], [3, 4, 2, 1]), ([10, 20, 30, 40], [2, 3, 4, 1]), ([2, 4, 6, 8], [5, 3, 1, 1]), ([15, 25, 35, 45], [1, 3, 4, 2]), ([3, 6, 9, 12], [2, 4, 3, 1]), ([50, 60, 70, 80], [4, 2, 3, 1])]]
           + [Q(f"The mean of {len(d)} observations is {g(mean(d))}. One observation, {x}, is removed. Find the new mean.", f"Sum $={sum(d)}$ (1); new sum $={sum(d)-x}$ over {len(d)-1} values (1); mean $={g(Fr(sum(d)-x,len(d)-1))}$ (1).", "1+1+1") for d, x in [([12, 18, 24, 30, 36], 12), ([10, 20, 30, 40, 50, 60, 70], 70), ([8, 16, 24, 32, 40], 40), ([14, 21, 28, 35, 42, 49, 56], 35), ([5, 10, 15, 20, 25], 15), ([9, 18, 27, 36, 45, 54, 63], 36)] if (sum(d) - x) % (len(d) - 1) == 0])
NCERT_D = ([Q(f"The monthly rainfall (mm) from June to November is {L(d)}. (i) Find the mean rainfall. (ii) Which month had the greatest rise over the previous month? (iii) Find the range.", f"(i) mean $={g(mean(d))}$ (1); (ii) rises {L([d[i+1]-d[i] for i in range(5)])}; greatest in month {['July','August','September','October','November'][[d[i+1]-d[i] for i in range(5)].index(max([d[i+1]-d[i] for i in range(5)]))]} (2); (iii) range $={max(d)-min(d)}$ (2).", "1+2+2") for d in [gen(s, 6, 20, 200) for s in range(300, 306)]]
           + [Q(f"The runs of two players in 5 matches are: A: {L(a)}; B: {L(b)}. Find the mean of each and say who is more consistent (smaller range).", f"Mean A $={g(mean(a))}$, mean B $={g(mean(b))}$ (2); range A $={max(a)-min(a)}$, range B $={max(b)-min(b)}$ (2); more consistent: {'A' if max(a)-min(a) < max(b)-min(b) else 'B'} (1).", "2+2+1") for a, b in [(gen(s, 5, 10, 90), gen(s + 50, 5, 10, 90)) for s in range(310, 316)] if max(a) - min(a) != max(b) - min(b)][:6])

# ================= MEDIUM =================
def comb_pairs():
    out = []
    for n1_, m1_, n2_, m2_ in [(10, 40, 15, 60), (20, 35, 30, 45), (12, 50, 8, 75), (25, 24, 15, 40), (30, 18, 20, 33), (40, 55, 10, 80), (18, 22, 12, 37)]:
        out.append((n1_, m1_, n2_, m2_))
    return out
m1 = [ND(f"The mean mark of {a} students is {b} and of another {c} students is {d}. The mean of all {a+c} students is:", Fr(a * b + c * d, a + c), f"$({a}\\times{b}+{c}\\times{d})\\div{a+c}$", wrong=[Fr(b + d, 2), a * b + c * d, Fr(a * b + c * d, a + c) + 2]) for a, b, c, d in comb_pairs()[:6] if (a * b + c * d) % (a + c) == 0]
m2 = []
for s in range(400, 430):
    if len(m2) >= 5: break
    d = gen(s, 6, 10, 60); k = d[2]; new = k + 6 * (s % 4 + 1)
    m2.append(ND(f"The mean of {L(d)} is {g(mean(d))}. If {k} is replaced by {new}, the new mean is:", Fr(sum(d) - k + new, 6), f"Sum changes by ${new-k}$", wrong=[mean(d), mean(d) + new - k, Fr(sum(d) + new, 6)]))
m3 = [ND(f"The median of {L(d)} is:", med(d), "Arrange in ascending order first", wrong=[Fr(d[len(d) // 2]), mean(d), sorted(d)[len(d) // 2 - 1] + 1]) for d in [gen(s, 8, 12, 99, False) for s in range(430, 435)]]
m4_ = [ND(f"The mean of {len(d)} numbers is {g(mean(d))}. The number to be added so that the mean becomes {t} is:", t * (len(d) + 1) - sum(d), f"Required total ${t*(len(d)+1)}$ minus ${sum(d)}$", wrong=[t, t - sum(d) // len(d), t * (len(d) + 1) - sum(d) + len(d)]) for d, t in [(gen(s, 5, 10, 40), t) for s, t in [(440, 30), (441, 25), (442, 33), (443, 40), (444, 22)]]]
m5 = [ND(f"The mean of the first {n} multiples of {k} (that is {k}, {2*k}, ..., {n*k}) is:", Fr(k * (n + 1), 2), f"$k(n+1)/2={k}\\times{n+1}/2$") for n, k in [(9, 4), (11, 5), (15, 3), (13, 6), (7, 9)]]
m6 = [ND(f"On a line graph, a town's population (in thousands) rises from {a} to {a+a*inc//100}. The percentage increase is:", inc, f"Rise $={a*inc//100}$; $({a*inc//100}/{a})\times100$", wrong=[a * inc // 100, inc + 10, inc // 2], post="%") for a, inc in [(20, 50), (40, 25), (50, 20), (80, 25), (25, 40)]]
MED_A = [m1, m2, m3, m4_, m5, m6]
MED_B = ([Q(f"The mean marks of {a} boys is {b} and of {c} girls is {d}. Find the mean mark of the whole class of {a+c}.", f"Total marks $={a}\\times{b}+{c}\\times{d}={a*b+c*d}$ (1); mean $={g(Fr(a*b+c*d,a+c))}$ (1).", "1+1") for a, b, c, d in [(15, 60, 10, 70), (20, 45, 30, 55), (12, 80, 18, 70), (25, 32, 15, 48)]]
         + [Q(f"The mean of {len(d)} observations {L(d)} is {g(mean(d))}. Find the mean if {x} is added to every observation.", f"New mean $={g(mean(d))}+{x}={g(mean(d)+x)}$ (1+1).", "1+1") for d, x in [(gen(s, 5, 8, 40), x) for s, x in [(460, 6), (461, 9), (462, 12), (463, 15)]]]
         + [Q(f"Find the mean of the first {n} natural numbers that are multiples of {k}.", f"Numbers: {k}, {2*k}, ..., {n*k} (1); mean $=k(n+1)/2={g(Fr(k*(n+1),2))}$ (1).", "1+1") for n, k in [(10, 3), (12, 5), (9, 7), (14, 2)]])
MED_C = ([Q(f"The mean weight of {a} students is {b} kg and of another {c} students is {d} kg. Find the mean weight of all of them.", f"Total weight $={a}\\times{b}+{c}\\times{d}={a*b+c*d}$ kg (2); mean $={g(Fr(a*b+c*d,a+c))}$ kg (1).", "2+1") for a, b, c, d in [(10, 42, 15, 48), (20, 36, 30, 41), (8, 50, 12, 45), (16, 38, 24, 43), (25, 30, 25, 34), (30, 28, 20, 33)]]
         + [Q(f"The mean of {len(d)} numbers is {g(mean(d))}. If one number {k} is replaced by {new}, find the new mean and the change in the mean.", f"Sum changes by ${new-k}$ (1); new sum $={sum(d)-k+new}$ (1); new mean $={g(Fr(sum(d)-k+new,len(d)))}$, change $={g(Fr(new-k,len(d)))}$ (1).", "1+1+1") for d, k, new in [(gen(s, 5, 10, 50), None, None) for s in range(470, 476)] for k, new in [(d[1], d[1] + 10)]]
         + [Q(f"The median of {L(d)} is {g(med(d))}. If the largest value {max(d)} is changed to {max(d)*3}, what happens to the median and the mean?", f"Median stays $={g(med(d))}$ since the middle values are unchanged (1); mean increases by ${max(d)*2}/{len(d)}$ (1) to ${g(Fr(sum(d)+2*max(d),len(d)))}$ (1).", "1+1+1") for d in [gen(s, 7, 10, 80, False) for s in range(480, 486)]])
MED_D = ([Q(f"The temperatures (°C) at 8 am, 10 am, 12 noon, 2 pm, 4 pm and 6 pm were {L(t)}. (i) Find the rise or fall between each consecutive pair. (ii) Find the mean temperature. (iii) In which interval was the change largest?", f"(i) changes: {L([t[i+1]-t[i] for i in range(5)])} (2); (ii) mean $={g(mean(t))}$ (2); (iii) largest change {max(abs(t[i+1]-t[i]) for i in range(5))}°C (1).", "2+2+1") for t in [(18, 22, 27, 30, 26, 21), (20, 25, 31, 35, 30, 24), (15, 17, 24, 29, 28, 23), (22, 26, 33, 36, 31, 25), (12, 16, 23, 27, 22, 17), (19, 21, 30, 32, 29, 20)]]
          + [Q(f"A class of {n} students has a mean mark of {m}. Another {n2} students with mean {m2} join it. Find the mean of the combined group and the change in the original mean.", f"Total $={n}\\times{m}+{n2}\\times{m2}={n*m+n2*m2}$ (2); mean $={g(Fr(n*m+n2*m2,n+n2))}$ (2); change $={g(Fr(n*m+n2*m2,n+n2)-m)}$ (1).", "2+2+1") for n, m, n2, m2 in [(20, 50, 30, 60), (15, 64, 10, 74), (24, 45, 16, 60), (30, 52, 20, 62), (12, 70, 18, 80), (40, 35, 10, 60)] if (n * m + n2 * m2) % (n + n2) == 0])

# ================= HARD =================
h1 = [ND(f"The mean of 5 numbers is {m}. When one number is removed the mean of the remaining 4 becomes {m2}. The removed number is:", 5 * m - 4 * m2, f"$5\\times{m}-4\\times{m2}$", wrong=[m - m2, 5 * m2 - 4 * m, m]) for m, m2 in [(30, 27), (24, 21), (45, 40), (18, 20), (50, 44)]]
h2 = [ND(f"The mean of {n} values was found to be {m}. Later it was found that {a} was misread as {b}. The correct mean is:", Fr(n * m - b + a, n), f"Correct sum $={n*m}-{b}+{a}$", wrong=[m, Fr(n * m + b - a, n), m + a - b]) for n, m, a, b in [(20, 40, 52, 25), (10, 36, 80, 30), (25, 24, 90, 40), (15, 60, 75, 45), (12, 50, 62, 26)] if (n * m - b + a) % n == 0]
h3 = [ND(f"A class has {n} students with mean age {m} years. When the teacher's age is included, the mean rises to {m+1}. The teacher's age (years) is:", (n + 1) * (m + 1) - n * m, f"$({n}+1)({m+1})-{n}\\times{m}$", wrong=[m + 1, n + m, (n + 1) * (m + 1) - n * m - 5]) for n, m in [(29, 13), (24, 12), (34, 14), (19, 11)]]
h4 = [ND(f"The mean of the first {n} odd natural numbers is:", n, "Sum of first $n$ odd numbers is $n^2$, so mean $=n$", wrong=[n + 1, n * n, Fr(n + 1, 2)]) for n in [12, 15, 21, 30, 25]]
h5 = []
for s in range(500, 560):
    if len(h5) >= 4: break
    d = gen(s, 7, 10, 60, False); d2 = d + [d[0] * 10]
    h5.append(M4(f"A data set {L(d)} gets an extra (outlier) value {d[0]*10}. The median of the new data of 8 values is:", g(med(d2)), [g(med(d)), g(mean(d2)), g(max(d2))], f"Sort the 8 values; median is the mean of the 4th and 5th: {g(med(d2))}"))
h6 = [ND(f"A car travels {a} km at {s1} km/h and then {a} km at {s2} km/h. Its average speed (km/h) for the whole journey is:", Fr(2 * s1 * s2, s1 + s2), f"Total distance ${2*a}$ over total time", wrong=[Fr(s1 + s2, 2), s1 + s2 - 10, Fr(s1 * s2, s1 + s2)]) for a, s1, s2 in [(120, 40, 60), (90, 30, 45), (180, 60, 90), (150, 50, 75)] if (2 * s1 * s2) % (s1 + s2) == 0]
h7 = [ND(f"The mean of {n} numbers is {m}. If every number is multiplied by {k} and then {c} is added, the new mean is:", m * k + c, "Mean is multiplied by $k$, then $c$ is added", wrong=[(m + c) * k, m + c, m * k]) for n, m, k, c in [(8, 15, 3, 4), (10, 22, 2, 7), (6, 14, 5, 3), (12, 9, 4, 10), (9, 25, 3, 6)]]
HARD_A = [h1, h2, h3, h4, h5, h6, h7]
HARD_B = ([Q(f"The mean of 6 numbers is {m}. When one number is removed, the mean of the remaining 5 numbers is {m2}. Find the removed number.", f"Total $=6\\times{m}={6*m}$ (1); rest $=5\\times{m2}={5*m2}$, removed $={6*m-5*m2}$ (1).", "1+1") for m, m2 in [(20, 18), (35, 32), (14, 12), (48, 45)]]
         + [Q(f"The mean of the first {n} even natural numbers is {n+1}. Verify this for n = {n}.", f"Sum $=2+4+\\dots+{2*n}={n*(n+1)}$ (1); mean $={n*(n+1)}\\div{n}={n+1}$ (1).", "1+1") for n in [8, 11, 14, 20]]
         + [Q(f"A data set was recorded as {L([d[0] + 6] + d[1:])}, but the first value should have been {d[0]}. Find the correct mean.", f"Wrong sum $={sum(d)+6}$ (1); correct sum $={sum(d)}$; mean $={g(Fr(sum(d),len(d)))}$ (1).", "1+1") for d in [gen(s, 6, 12, 50) for s in range(560, 640) if gen(s, 6, 12, 50)] if sum(d) % len(d) == 0][:4])
HARD_C = ([Q(f"A class of {n} students has mean mark {m}. After rechecking, a score of {b} was corrected to {a}. Find the new mean.", f"New sum $={n*m}-{b}+{a}={n*m-b+a}$ (2); mean $={g(Fr(n*m-b+a,n))}$ (1).", "2+1") for n, m, a, b in [(40, 62, 80, 38), (25, 48, 70, 20), (30, 55, 66, 36), (20, 72, 92, 52), (50, 41, 60, 30), (35, 44, 70, 35)]]
         + [Q(f"The mean of {n} numbers is {m}. When {x} is added, the mean becomes {m+1}. Find {x} if {n} = {n}.", "", "") for n, m, x in []]
         + [Q(f"The mean age of {n} players is {m} years. When the coach is included the mean becomes {m+2}. Find the age of the coach.", f"Total age of players $={n*m}$ (1); total with coach $={(n+1)*(m+2)}$ (1); coach $={(n+1)*(m+2)-n*m}$ years (1).", "1+1+1") for n, m in [(11, 23), (15, 20), (14, 25), (9, 30), (19, 17), (24, 28)]]
         + [Q(f"A student's marks in 5 tests are {L(d)}. What mark must she score in the 6th test so that her mean becomes {t}?", f"Required total $=6\\times{t}={6*t}$ (1); present total $={sum(d)}$ (1); needed $={6*t-sum(d)}$ (1).", "1+1+1") for d, t in [(gen(s, 5, 45, 75), None) for s in range(600, 606)] for t in [int(mean(d)) + 4 + len(d) % 3]])
HARD_D = ([Q(f"The mean of {a} numbers is {b}, the mean of {c} numbers is {d} and the mean of {e} numbers is {f}. Find the mean of all {a+c+e} numbers.", f"Total $={a}\\times{b}+{c}\\times{d}+{e}\\times{f}={a*b+c*d+e*f}$ (3); mean $={g(Fr(a*b+c*d+e*f,a+c+e))}$ (2).", "3+2") for a, b, c, d, e, f in [(15, 65, 25, 15, 10, 25), (10, 40, 20, 50, 20, 30), (8, 30, 12, 55, 30, 65), (20, 30, 10, 25, 20, 70), (15, 45, 25, 35, 10, 15), (10, 35, 20, 15, 20, 70)] if (a * b + c * d + e * f) % (a + c + e) == 0]
          + [Q(f"The mean of {n} observations is {m}. If each observation is multiplied by {k} and then decreased by {c}, find the new mean and the new sum.", f"New mean $={m}\\times{k}-{c}={m*k-c}$ (3); new sum $={n}\\times{m*k-c}={n*(m*k-c)}$ (2).", "3+2") for n, m, k, c in [(12, 15, 4, 5), (15, 20, 3, 8), (20, 12, 5, 9), (10, 30, 2, 11), (18, 14, 6, 4), (25, 16, 3, 7)]])

def T(A, B, C, D): return dict(A=A, B=grp(B, 4), C=grp(C, 6), D=grp(D, 6))
TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
