"""Class 10 Maths Ch 13 - Statistics (graded banks). Mean (direct / assumed mean / step-deviation), median and mode of grouped data.
Cumulative frequency graphs (ogives) and the empirical relation are not used."""
import random
from c10m_x import *

SLUG, NAME, CHNO = "Statistics", "Statistics", 13

# ---------- grouped-data helpers ----------
def stats(s0, h, fs):
    n = len(fs); N = sum(fs)
    xs = [F(s0) + h * i + F(h, 2) for i in range(n)]
    mean = F(sum(f * x for f, x in zip(fs, xs)), N)
    cf = 0; mc = None
    for i, f in enumerate(fs):
        if cf + f > F(N, 2): mc = i; break
        cf += f
    cfprev = cf
    med = F(s0) + h * mc + (F(N, 2) - cfprev) / fs[mc] * h
    m = max(fs); idx = [i for i, f in enumerate(fs) if f == m]
    mode = None; mi = None
    if len(idx) == 1 and 0 < idx[0] < n - 1:
        mi = idx[0]; den = 2 * fs[mi] - fs[mi - 1] - fs[mi + 1]
        mode = F(s0) + h * mi + F(fs[mi] - fs[mi - 1], den) * h
    return dict(n=n, N=N, xs=xs, mean=mean, mc=mc, cfprev=cfprev, med=med, mi=mi, mode=mode)

def find_tables(tag, count, need, ncls, Ns, h_choices=(10,), s0_choices=(0, 10, 20, 30, 40, 50), fmax=22, fmin=2):
    rng = random.Random(tag); out = []; seen = set()
    while len(out) < count:
        n = rng.choice(ncls); h = rng.choice(h_choices); s0 = rng.choice(s0_choices); N = rng.choice(Ns)
        fs = [rng.randint(fmin, fmax) for _ in range(n)]
        if sum(fs) != N:
            continue
        st = stats(s0, h, fs)
        if any(st[k] is None or dec(st[k]) is None for k in need): continue
        if 2 * st["cfprev"] == N: continue      # median exactly on a class boundary: avoid ambiguity
        key = (s0, h, tuple(fs))
        if key in seen: continue
        seen.add(key); out.append((s0, h, fs))
    return out

def classes(s0, h, n): return [f"{s0 + h*i}–{s0 + h*(i+1)}" for i in range(n)]
def inline(s0, h, fs):
    return f"classes {', '.join(classes(s0, h, len(fs)))} with frequencies {', '.join(map(str, fs))} respectively"
def tbl(s0, h, fs, what="Class interval", freq="Frequency"):
    return lib.table([what] + classes(s0, h, len(fs)), [[freq] + [str(f) for f in fs]])

CTX = [("The marks obtained by students in a test are given below.", "Marks", "Number of students"),
       ("The daily wages (in ₹) of workers in a factory are given below.", "Daily wage (₹)", "Number of workers"),
       ("The ages (in years) of patients admitted to a hospital in a month are given below.", "Age (years)", "Number of patients"),
       ("The weights (in kg) of students of a class are given below.", "Weight (kg)", "Number of students"),
       ("The daily electricity consumption (in units) of households in a colony is given below.", "Units consumed", "Number of households"),
       ("The lifetimes (in hours) of electric bulbs tested in a laboratory are given below.", "Lifetime (hours)", "Number of bulbs"),
       ("The distances (in km) travelled to office by employees of a company are given below.", "Distance (km)", "Number of employees"),
       ("The monthly pocket money (in ₹) of students is given below.", "Pocket money (₹)", "Number of students")]
def ctx(i): return CTX[i % len(CTX)]

def fmtn(x): return nd(x)
def SD(stem0, ask, ans, parts, ex=(), fmt=fmtn):
    ans = ans if isinstance(ans, list) else [ans]
    w = []
    if len(ans) == 1:
        c = F(ans[0]); w = [x for x in list(ex) + [c + 1, c - 1, c * 2, c + 5, c - 5, c + 10, c / 2] if x != c and x > 0]
    return SCG(stem0, ask, ans, w, parts, fmt)

def wordtab(i, s0, h, fs):
    c, lab, fl = ctx(i)
    return f"{c} {tbl(s0, h, fs, lab, fl)}"

def mean_sc(i, tb, method="direct", inl=False):
    s0, h, fs = tb; st = stats(s0, h, fs); N = st["N"]; xs = st["xs"]; n = st["n"]
    stem = (f"For the data with {inline(s0, h, fs)}, " if inl else f"{wordtab(i, s0, h, fs)} ")
    fx = sum(f * x for f, x in zip(fs, xs)); a = xs[n // 2]
    if method == "direct":
        parts = [f"Class marks $x_i$: {', '.join(nd(x) for x in xs)}", f"$\\sum f_i={N}$ and $\\sum f_ix_i={nd(fx)}$", f"Mean $=\\frac{{\\sum f_ix_i}}{{\\sum f_i}}=\\frac{{{nd(fx)}}}{{{N}}}={nd(st['mean'])}$"]
    elif method == "assumed":
        d = [x - a for x in xs]; fd = sum(f * x for f, x in zip(fs, d))
        parts = [f"Take assumed mean $a={nd(a)}$; deviations $d_i=x_i-a$: {', '.join(nd(x) for x in d)}", f"$\\sum f_i={N}$ and $\\sum f_id_i={nd(fd)}$", f"Mean $=a+\\frac{{\\sum f_id_i}}{{\\sum f_i}}={nd(a)}+\\frac{{{nd(fd)}}}{{{N}}}={nd(st['mean'])}$"]
    else:
        u = [(x - a) / h for x in xs]; fu = sum(f * x for f, x in zip(fs, u))
        parts = [f"Take $a={nd(a)}$, $h={h}$; $u_i=\\frac{{x_i-a}}{{h}}$: {', '.join(nd(x) for x in u)}", f"$\\sum f_i={N}$ and $\\sum f_iu_i={nd(fu)}$", f"Mean $=a+h\\,\\frac{{\\sum f_iu_i}}{{\\sum f_i}}={nd(a)}+{h}\\times\\frac{{{nd(fu)}}}{{{N}}}={nd(st['mean'])}$"]
    return SD(stem.strip(), "mean" if not inl else "mean of the data", st["mean"], parts, [a, (fx / n)])
def median_sc(i, tb, inl=False):
    s0, h, fs = tb; st = stats(s0, h, fs); N = st["N"]; mc = st["mc"]; l = s0 + h * mc
    cfs = []; c = 0
    for f in fs: c += f; cfs.append(c)
    stem = (f"For the data with {inline(s0, h, fs)}, " if inl else f"{wordtab(i, s0, h, fs)} ")
    parts = [f"Cumulative frequencies: {', '.join(map(str, cfs))}; $N={N}$, so $\\frac{{N}}{{2}}={nd(F(N,2))}$", f"Median class ${l}$–${l+h}$: $l={l}$, $cf={st['cfprev']}$, $f={fs[mc]}$, $h={h}$", f"Median $=l+\\frac{{\\frac N2-cf}}{{f}}\\times h={l}+\\frac{{{nd(F(N,2))}-{st['cfprev']}}}{{{fs[mc]}}}\\times{h}={nd(st['med'])}$"]
    return SD(stem.strip(), "median" if not inl else "median of the data", st["med"], parts, [l, l + h, st["mean"]])
def mode_sc(i, tb, inl=False):
    s0, h, fs = tb; st = stats(s0, h, fs); mi = st["mi"]; l = s0 + h * mi
    stem = (f"For the data with {inline(s0, h, fs)}, " if inl else f"{wordtab(i, s0, h, fs)} ")
    f1, f0, f2 = fs[mi], fs[mi - 1], fs[mi + 1]
    parts = [f"Highest frequency is {f1}, so the modal class is ${l}$–${l+h}$", f"$l={l}$, $f_1={f1}$, $f_0={f0}$, $f_2={f2}$, $h={h}$", f"Mode $=l+\\frac{{f_1-f_0}}{{2f_1-f_0-f_2}}\\times h={l}+\\frac{{{f1-f0}}}{{{2*f1-f0-f2}}}\\times{h}={nd(st['mode'])}$"]
    return SD(stem.strip(), "mode" if not inl else "mode of the data", st["mode"], parts, [l, l + h, st["mean"]])
def modal_class_sc(tb):
    s0, h, fs = tb; st = stats(s0, h, fs); i = fs.index(max(fs)); assert fs.count(max(fs)) == 1
    return SCG(f"For the data with {inline(s0, h, fs)},", "modal class", [i], [j for j in range(len(fs)) if j != i], [f"Highest frequency is {fs[i]}", f"It belongs to the class ${s0+h*i}$–${s0+h*(i+1)}$", f"Modal class $={s0+h*i}$–${s0+h*(i+1)}$"], lambda j, s0=s0, h=h: f"${s0+h*j}$–${s0+h*(j+1)}$")
def median_class_sc(tb):
    s0, h, fs = tb; st = stats(s0, h, fs); mc = st["mc"]
    return SCG(f"For the data with {inline(s0, h, fs)},", "median class", [mc], [j for j in range(len(fs)) if j != mc], [f"$N={st['N']}$, $\\frac{{N}}{{2}}={nd(F(st['N'],2))}$", "The median class is the class whose cumulative frequency first exceeds $\\frac N2$", f"Median class $={s0+h*mc}$–${s0+h*(mc+1)}$"], lambda j, s0=s0, h=h: f"${s0+h*j}$–${s0+h*(j+1)}$")
def class_mark_sc(a, b):
    return SD(f"The class interval is ${a}$–${b}$.", "class mark", F(a + b, 2), ["Class mark $=\\frac{\\text{lower limit}+\\text{upper limit}}{2}$", f"$\\frac{{{a}+{b}}}{{2}}$", f"Class mark $={nd(F(a+b,2))}$"], [a, b, b - a])
def sumf_sc(tb):
    s0, h, fs = tb
    return SD(f"For the data with {inline(s0, h, fs)},", "total number of observations $\\sum f_i$", sum(fs), ["$\\sum f_i$ is the sum of all frequencies", "$" + "+".join(map(str, fs)) + "$", f"$\\sum f_i={sum(fs)}$"], [sum(fs) - fs[0], sum(fs) + 1])
def cf_sc(tb, k):
    s0, h, fs = tb; v = sum(fs[:k])
    return SD(f"For the data with {inline(s0, h, fs)},", f"cumulative frequency of the class ${s0+h*(k-1)}$–${s0+h*k}$", v, ["Cumulative frequency $=$ sum of the frequencies up to and including the class", "$" + "+".join(map(str, fs[:k])) + "$", f"$cf={v}$"], [fs[k - 1], sum(fs[:k - 1]), sum(fs)])
def missing_freq_sc(tb, k, inl=True):
    s0, h, fs = tb; st = stats(s0, h, fs); x = st["xs"][k]; assert x != st["mean"]
    fshow = [("$p$" if j == k else str(f)) for j, f in enumerate(fs)]
    known = sum(f * xx for j, (f, xx) in enumerate(zip(fs, st["xs"])) if j != k); kn = st["N"] - fs[k]
    stem = f"The mean of a distribution with {inline(s0, h, fs).split(' with frequencies')[0]} and frequencies {', '.join(fshow)} respectively is ${nd(st['mean'])}$."
    return SD(stem, "value of $p$", fs[k], [f"$\\sum f_i={kn}+p$ and $\\sum f_ix_i={nd(known)}+{nd(x)}p$", f"$\\frac{{{nd(known)}+{nd(x)}p}}{{{kn}+p}}={nd(st['mean'])}$ gives $({nd(x)}-{nd(st['mean'])})p={nd(st['mean']*kn-known)}$", f"$p={fs[k]}$"], [fs[k] + 2, fs[k] - 1, fs[k] + 5])
def median_two_missing(tb, ix, iy, which="x"):
    s0, h, fs = tb; st = stats(s0, h, fs); mc = st["mc"]; assert ix < mc < iy
    fshow = [("$x$" if j == ix else "$y$" if j == iy else str(f)) for j, f in enumerate(fs)]
    kn = st["N"] - fs[ix] - fs[iy]
    stem = f"The median of a distribution with {inline(s0, h, fs).split(' with frequencies')[0]} and frequencies {', '.join(fshow)} respectively, and total frequency {st['N']}, is ${nd(st['med'])}$."
    l = s0 + h * mc; cfp = st["cfprev"]
    ans = fs[ix] if which == "x" else fs[iy]
    return SD(stem, f"value of ${which}$", ans, [f"Median class is ${l}$–${l+h}$ with $f={fs[mc]}$, and the cumulative frequency before it is $cf={cfp-fs[ix]}+x$", f"${nd(st['med'])}={l}+\\frac{{{nd(F(st['N'],2))}-({cfp-fs[ix]}+x)}}{{{fs[mc]}}}\\times{h}$ gives $x={fs[ix]}$", f"$x={fs[ix]}$; then $y={st['N']}-{kn}-x={fs[iy]}$"], [fs[ix] + 1, fs[iy] + 2, fs[ix] - 1])

def both_sc(i, tb):
    s0, h, fs = tb; a = mean_sc(i, tb); b = mode_sc(i, tb)
    return SCG(a["stem0"], "mean and the mode (in this order)", [a["ans"][0], b["ans"][0]], [], [a["parts"][1] + "; " + a["parts"][2], b["parts"][1], "Mode: " + b["parts"][2].replace("Mode $=", "$=")], fmtn)

CONCEPT_N = [M4("The class mark of the class $10$–$25$ is:", "17.5", ["15", "35", "7.5"], "$\\frac{10+25}{2}$"),
    M4("In the formula $\\bar x=a+h\\dfrac{\\sum f_iu_i}{\\sum f_i}$ (step-deviation method), $u_i$ equals:", "$\\dfrac{x_i-a}{h}$", ["$x_i-a$", "$\\dfrac{x_i}{h}$", "$h(x_i-a)$"], "Definition of $u_i$"),
    M4("The median of grouped data is found using:", "cumulative frequencies", ["class marks only", "the highest frequency only", "deviations from the mean"], "Median class from cumulative frequency"),
    M4("The modal class of a frequency distribution is the class:", "with the highest frequency", ["with the highest class mark", "with the lowest frequency", "in the middle of the table"], "Definition"),
    M4("If the assumed mean is $a$ and the deviations $d_i=x_i-a$ are used, then $\\bar x=$:", "$a+\\dfrac{\\sum f_id_i}{\\sum f_i}$", ["$a-\\dfrac{\\sum f_id_i}{\\sum f_i}$", "$\\dfrac{\\sum f_id_i}{\\sum f_i}$", "$a\\sum f_id_i$"], "Assumed mean method"),
    M4("For a frequency distribution with 5 classes, the number of class marks is:", "5", ["4", "6", "10"], "One class mark per class")]
CONCEPT_E = [M4("The upper limit of a class $20$–$30$ is:", "30", ["20", "25", "10"], "Class limits"),
    M4("The width of the class interval $40$–$55$ is:", "15", ["40", "55", "47.5"], "$55-40$"),
    M4("Which measure of central tendency is the value that occurs most often?", "mode", ["mean", "median", "range"], "Definition of mode"),
    M4("The sum of all the frequencies of a distribution is equal to:", "the total number of observations", ["the mean", "the number of classes", "the highest frequency"], "$\\sum f_i=N$"),
    M4("The class mark of the class $0$–$10$ is:", "5", ["0", "10", "15"], "$\\frac{0+10}{2}$")]
CONCEPT_M = [M4("If $\\sum f_i=40$ and $\\sum f_ix_i=1200$, the mean is:", "30", ["300", "40", "1160"], "$\\frac{1200}{40}$"),
    M4("The median class of a distribution is the class whose cumulative frequency is:", "just greater than $\\dfrac N2$", ["just less than $\\dfrac N2$", "equal to $N$ always", "the highest frequency"], "Median class definition"),
    M4("In a distribution, $\\sum f_id_i=-60$, $\\sum f_i=30$ and the assumed mean is 50. The mean is:", "48", ["52", "-2", "50"], "$50+\\frac{-60}{30}$"),
    M4("If every observation of a grouped data is increased by 5 (every class shifted by 5), the mean:", "increases by 5", ["remains the same", "becomes 5 times", "decreases by 5"], "Mean shifts with the data"),
    M4("The modal class is $30$–$40$ with $f_1=18$, $f_0=10$, $f_2=12$. The value of $2f_1-f_0-f_2$ is:", "14", ["16", "20", "40"], "$36-10-12$")]
CONCEPT_H = [
    M4("For a distribution with median class $20$–$30$, $N=50$, $cf=18$ and $f=14$, the median is:", "25", ["24", "28", "22.5"], "$20+\\frac{25-18}{14}\\times10=25$"),
    M4("The modal class is $20$–$30$ with $f_1=16$, $f_0=6$, $f_2=8$. The mode is:", "$20+\\dfrac{10}{18}\\times10$", ["$20+\\dfrac{10}{22}\\times10$", "$20+\\dfrac{10}{16}\\times10$", "$20+\\dfrac{8}{18}\\times10$"], "$\\frac{f_1-f_0}{2f_1-f_0-f_2}=\\frac{10}{32-14}$"),
    M4("If the mean of $n$ classes' marks is found by the step-deviation method with $h=10$ and $\\sum f_iu_i=-12$, $\\sum f_i=60$, $a=45$, the mean is:", "43", ["33", "47", "45.2"], "$45+10\\times\\frac{-12}{60}$"),
    M4("The mean of a data is 24 and the assumed mean taken is 20. Then $\\dfrac{\\sum f_id_i}{\\sum f_i}$ equals:", "4", ["44", "-4", "20"], "$\\bar x-a$"),
    M4("A distribution has $N=60$ and the median class has $cf=22$, $f=16$, $l=40$, $h=10$. The median is:", "45", ["50", "42.5", "48"], "$40+\\frac{30-22}{16}\\times10$")]

ALL3 = ("mean", "med", "mode")
def tabs(tag, n, **kw):
    kw.setdefault("need", ALL3)
    return find_tables(tag, n, **kw)
def med_tables(tag, n, **kw):
    """tables whose median class has a class before and a class after it (needed for two missing frequencies)"""
    out = []; k = 0
    while len(out) < n:
        for tb in tabs(f"{tag}{k}", n, **kw):
            st = stats(*tb)
            if 0 < st["mc"] < st["n"] - 1 and tb not in out and len(out) < n: out.append(tb)
        k += 1
    return out

# ================= EASY =================
E1 = tabs("E1", 12, ncls=(4, 5), Ns=(20, 25, 50))
E2 = tabs("E2", 12, ncls=(4, 5), Ns=(20, 25, 50), s0_choices=(0, 10, 20))
eA = [[MC(class_mark_sc(a, b)) for a, b in ((10, 20), (20, 30), (30, 40), (40, 50), (60, 70))],
      [MC(modal_class_sc(tb)) for tb in E1[:5]],
      [MC(median_class_sc(tb)) for tb in E1[5:10]],
      [MC(sumf_sc(tb)) for tb in E2[:5]],
      [MC(cf_sc(tb, k)) for tb, k in zip(E2[5:10], (2, 3, 2, 3, 4))],
      [MC(mean_sc(0, tb, inl=True)) for tb in E1[:5]],
      [MC(mode_sc(0, tb, inl=True)) for tb in E2[:5]],
      [MC(median_sc(0, tb, inl=True)) for tb in E2[5:10]],
      CONCEPT_E]
eB = ([SQ(mean_sc(i, tb), 2) for i, tb in enumerate(E1[:4])] + [SQ(mode_sc(i + 4, tb), 2) for i, tb in enumerate(E1[4:8])] + [SQ(median_sc(i + 8, tb), 2) for i, tb in enumerate(E1[8:12])])
E3 = tabs("E3", 18, ncls=(5,), Ns=(25, 50, 100))
eC = ([SQ(mean_sc(i, tb), 3) for i, tb in enumerate(E3[:6])] + [SQ(median_sc(i + 1, tb), 3) for i, tb in enumerate(E3[6:12])] + [SQ(mode_sc(i + 2, tb), 3) for i, tb in enumerate(E3[12:18])])
E4 = tabs("E4", 12, ncls=(5, 6), Ns=(50, 100, 40))
eD = ([SQ(mean_sc(i, tb, "assumed"), 5) for i, tb in enumerate(E4[:3])] + [SQ(mean_sc(i + 3, tb, "step"), 5) for i, tb in enumerate(E4[3:6])]
      + [SQ(median_sc(i + 6, tb), 5) for i, tb in enumerate(E4[6:9])] + [SQ(mode_sc(i + 1, tb), 5) for i, tb in enumerate(E4[9:12])])

# ================= NCERT =================
N1 = tabs("N1", 20, ncls=(5, 6), Ns=(50, 100, 40, 25, 20))
nA = [[MC(mean_sc(0, tb, inl=True)) for tb in N1[:5]],
      [MC(median_sc(0, tb, inl=True)) for tb in N1[5:10]],
      [MC(mode_sc(0, tb, inl=True)) for tb in N1[10:15]],
      [MC(modal_class_sc(tb)) for tb in N1[15:20]],
      [MC(missing_freq_sc(tb, k)) for tb, k in zip(N1[:5], (1, 2, 3, 2, 1))],
      CONCEPT_N]
N2 = tabs("N2", 18, ncls=(5, 6), Ns=(50, 100, 40, 25, 20), s0_choices=(0, 10, 20, 30, 40, 50, 60, 70))
nB = ([SQ(mean_sc(i, tb), 2) for i, tb in enumerate(N2[:4])] + [SQ(mode_sc(i + 3, tb), 2) for i, tb in enumerate(N2[4:8])] + [SQ(median_sc(i + 5, tb), 2) for i, tb in enumerate(N2[8:12])])
nC = ([SQ(mean_sc(i, tb, "assumed"), 3) for i, tb in enumerate(N2[:6])] + [SQ(median_sc(i + 2, tb), 3) for i, tb in enumerate(N2[12:18])] + [SQ(mode_sc(i + 4, tb), 3) for i, tb in enumerate(N1[:6])])
NM = med_tables("NM", 6, ncls=(6, 7), Ns=(100, 50, 40), fmin=3)
nD = [SQ(missing_freq_sc(tb, k), 5) for tb, k in zip(N1[5:11], (3, 2, 1, 2, 3, 4))] + [SQ(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1), 5) for tb in NM]

# ================= MEDIUM =================
M1 = tabs("M1", 25, ncls=(6, 7), Ns=(100, 50, 40), s0_choices=(0, 10, 20, 30, 40, 50, 60, 70, 80))
M2 = med_tables("M2", 12, ncls=(6, 7), Ns=(100, 50, 40), fmin=3, s0_choices=(0, 10, 20, 30, 40, 50, 60, 70, 80))
mA = [[MC(mean_sc(0, tb, inl=True)) for tb in M1[:5]],
      [MC(median_sc(0, tb, inl=True)) for tb in M1[5:10]],
      [MC(mode_sc(0, tb, inl=True)) for tb in M1[10:15]],
      [MC(missing_freq_sc(tb, k)) for tb, k in zip(M1[15:20], (2, 3, 1, 4, 2))],
      [MC(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1, "x")) for tb in M2[:5]],
      [MC(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1, "y")) for tb in M2[5:10]],
      CONCEPT_M]
mB = ([SQ(mean_sc(i, tb, "step"), 2) for i, tb in enumerate(M1[:4])] + [SQ(median_sc(i, tb), 2) for i, tb in enumerate(M1[20:24])] + [SQ(mode_sc(i, tb), 2) for i, tb in enumerate(M1[10:14])])
mC = ([SQ(mean_sc(i, tb, "step"), 3) for i, tb in enumerate(M1[5:11])] + [SQ(median_sc(i + 3, tb), 3) for i, tb in enumerate(M1[:6])] + [SQ(both_sc(i, tb), 3) for i, tb in enumerate(M1[14:20])])
mD = [SQ(missing_freq_sc(tb, k), 5) for tb, k in zip(M1[:6], (3, 2, 4, 1, 3, 2))] + [SQ(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1), 5) for tb in M2[6:12]]

# ================= HARD =================
H1 = tabs("H1", 25, ncls=(7, 8), Ns=(100,), h_choices=(10, 20), s0_choices=(0, 20, 40, 100, 200), fmax=25)
H2 = med_tables("H2", 12, ncls=(7, 8), Ns=(100,), h_choices=(10, 20), s0_choices=(0, 20, 40, 100, 200), fmax=25, fmin=3)
hA = [[MC(missing_freq_sc(tb, k)) for tb, k in zip(H1[:5], (2, 4, 3, 5, 1))],
      [MC(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1, "x")) for tb in H2[:5]],
      [MC(mean_sc(0, tb, inl=True)) for tb in H1[5:10]],
      [MC(median_sc(0, tb, inl=True)) for tb in H1[10:15]],
      [MC(mode_sc(0, tb, inl=True)) for tb in H1[15:20]],
      CONCEPT_H]
hB = ([SQ(missing_freq_sc(tb, k), 2) for tb, k in zip(H1[20:24], (2, 3, 4, 3))] + [SQ(mode_sc(i, tb), 2) for i, tb in enumerate(H1[:4])] + [SQ(median_sc(i, tb), 2) for i, tb in enumerate(H1[5:9])])
hC = ([SQ(both_sc(i, tb), 3) for i, tb in enumerate(H1[9:15])] + [SQ(mean_sc(i, tb, "step"), 3) for i, tb in enumerate(H1[15:21])] + [SQ(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1), 3) for tb in H2[5:11]])
hD = [SQ(median_two_missing(tb, stats(*tb)["mc"] - 1, stats(*tb)["mc"] + 1), 5) for tb in H2[:3]] + [SQ(missing_freq_sc(tb, k), 5) for tb, k in zip(H1[10:13], (2, 3, 4))] + [SQ(both_sc(i, tb), 5) for i, tb in enumerate(H1[21:24])] + [SQ(mean_sc(i, tb, "assumed"), 5) for i, tb in enumerate(H1[:3])]

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
