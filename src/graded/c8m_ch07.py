"""Class 8 Maths Ch 7 - Proportional Reasoning-1. Graded banks; all values computed in code."""
from math import gcd
from fractions import Fraction as F
from c8m_h import *

SLUG, NAME, CHNO = "Proportional_Reasoning_1", "Proportional Reasoning-1", 7

def rt(a, b): return f"{a} : {b}"
def simp(a, b): g = gcd(a, b); return a // g, b // g
def srt(a, b): return rt(*simp(a, b))
def R(x): return f"₹ {fmt(F(x))}"
def N(x): return fmt(F(x))
def near(v, d=(1, -1, 2)): return [v + x for x in d]
def ratwrong(p, q): return [rt(q, p), rt(p + 1, q), rt(p, q + 1)]
def share3(n, a, b, c): s = a + b + c; return n // s * a, n // s * b, n // s * c
def lcm3(*x):
    r = 1
    for t in x: r = r * t // gcd(r, t)
    return r

# ================= EASY =================
eA1 = [M4(f"The ratio {a} : {b} in simplest form is:", srt(a, b), ratwrong(*simp(a, b)), f"Divide both terms by {gcd(a,b)}") for a, b in [(12, 18), (20, 35), (14, 21), (24, 40), (45, 30), (16, 56)]]
eA2 = [M4(f"If {p} : {q} = {p*k} : x, then x is:", q * k, near(q * k, (k, -k, 2)), f"Multiply both terms by {k}") for p, q, k in [(2, 3, 4), (3, 5, 6), (4, 7, 3), (5, 6, 5), (3, 8, 7), (7, 9, 2)]]
eA3 = [M4("In which of the following are the two ratios in proportion?", f"${a} : {b}$ and ${k*a} : {k*b}$", [f"${a} : {b}$ and ${k*a} : {k*b+1}$", f"${a} : {b}$ and ${k*a+1} : {k*b}$", f"${a} : {b}$ and ${k*b} : {k*a}$"], f"Product of extremes $={a}\\times{k*b}$ equals product of means $={b}\\times{k*a}$") for a, b, k in [(2, 3, 4), (4, 5, 3), (3, 7, 3), (5, 6, 4), (3, 8, 2)]]
eA4 = [M4(q, srt(a, b), ratwrong(*simp(a, b)), "Convert to the same unit first") for q, a, b in [("The ratio of 50 cm to 2 m is:", 50, 200), ("The ratio of 250 g to 1 kg is:", 250, 1000), ("The ratio of 30 minutes to 2 hours is:", 30, 120), ("The ratio of 75 paise to ₹ 3 is:", 75, 300), ("The ratio of 600 m to 3 km is:", 600, 3000)]]
eA5 = [M4(f"₹ {n} is shared in the ratio {p} : {q}. The larger share is:", R(n // (p + q) * max(p, q)), [R(n // (p + q) * min(p, q)), R(n // 2), R(n // (p + q))], f"One part $={n}\\div{p+q}={n//(p+q)}$") for n, p, q in [(400, 3, 5), (720, 4, 5), (900, 2, 7), (660, 5, 6), (840, 3, 4)]]
eA6 = [M4(f"The cost of {n} pencils is ₹ {c}. The cost of 1 pencil is:", R(F(c, n)), [R(F(c, n) + 1), R(F(c, n) * 2), R(c - n)], f"${c}\\div{n}$") for n, c in [(6, 48), (8, 72), (12, 108), (5, 65), (9, 135)]]
eA7 = [M4(f"If {n} books cost ₹ {c}, then {m} books cost:", R(F(c, n) * m), [R(F(c, n) * m + n), R(F(c, n) * (m - 1)), R(c + m)], "Find the cost of 1 book first") for n, c, m in [(4, 120, 7), (6, 90, 10), (5, 200, 8), (3, 75, 9), (8, 160, 5)]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([Q(f"Write the ratio of {a} cm to {b} m in simplest form.", f"{b} m = {b*100} cm (1); ratio $={srt(a,b*100)}$ (1).", "1+1") for a, b in [(40, 2), (75, 3), (60, 5), (90, 4)]]
          + [Q(f"Find $x$ if {p} : {q} = {p*k} : $x$.", f"Both terms of the first ratio are multiplied by {k} (1); $x={q*k}$ (1).", "1+1") for p, q, k in [(5, 9, 3), (4, 11, 6), (7, 2, 4), (3, 10, 5)]]
          + [Q(f"If {n} notebooks cost ₹ {c}, find the cost of {m} notebooks.", f"Cost of 1 notebook $={c}\\div{n}={N(F(c,n))}$ (1); cost of {m} $={R(F(c,n)*m)}$ (1).", "1+1") for n, c, m in [(7, 91, 12), (9, 135, 4), (6, 114, 11), (8, 96, 15)]])
EASY_C = ([Q(f"Divide ₹ {n} between Ria and Sia in the ratio {p} : {q}.", f"Total parts {p+q} (1); one part ₹ {n//(p+q)} (1); shares {R(n//(p+q)*p)} and {R(n//(p+q)*q)} (1).", "1+1+1") for n, p, q in [(1200, 3, 5), (840, 2, 5), (1350, 4, 5), (960, 5, 7), (1080, 7, 2), (770, 3, 8)]]
          + [Q(f"Check whether {a} : {b} and {c} : {d} are in proportion.", f"Product of extremes {a}x{d}$={a*d}$ (1); product of means {b}x{c}$={b*c}$ (1); {'equal, so in proportion' if a*d==b*c else 'not equal, so not in proportion'} (1).", "1+1+1") for a, b, c, d in [(3, 4, 15, 20), (5, 8, 20, 30), (6, 9, 14, 21), (4, 7, 12, 22), (8, 12, 10, 15), (9, 5, 27, 16)]]
          + [Q(f"{n} kg of rice cost ₹ {c}. Find the cost of {m} kg of rice.", f"Cost per kg $={c}\\div{n}={N(F(c,n))}$ (1); cost of {m} kg $={N(F(c,n))}\\times{m}$ (1); $={R(F(c,n)*m)}$ (1).", "1+1+1") for n, c, m in [(5, 225, 8), (4, 180, 7), (6, 270, 10), (3, 126, 11), (8, 360, 5), (9, 297, 6)]])
EASY_D = ([Q(f"Two numbers are in the ratio {p} : {q} and their sum is {s*(p+q)}. Find the numbers and their difference.", f"Total parts {p+q}, one part $={s}$ (2); numbers {p*s} and {q*s} (2); difference {abs(p-q)*s} (1).", "2+2+1") for p, q, s in [(3, 5, 6), (2, 7, 8), (4, 9, 5), (5, 6, 12), (7, 3, 4), (8, 5, 3)]]
          + [Q(f"{n} pens cost ₹ {c}. Find the cost of 1 pen, the cost of {m} pens and the number of pens that can be bought for ₹ {c//n*k}.", f"Cost of 1 pen ₹ {c//n} (1); cost of {m} pens {R(c//n*m)} (2); pens for ₹ {c//n*k}: {k} (2).", "1+2+2") for n, c, m, k in [(6, 90, 10, 14), (8, 120, 15, 9), (5, 100, 12, 11), (9, 135, 4, 13), (7, 105, 20, 6), (4, 72, 9, 15)]])

# ================= NCERT =================
nA1 = [M4(f"The ratio of {a} m {b} cm to {c} cm is:", srt(a * 100 + b, c), ratwrong(*simp(a * 100 + b, c)), "Convert to the same unit") for a, b, c in [(2, 40, 60), (1, 50, 30), (3, 20, 80), (4, 80, 120), (2, 25, 50)]]
nA2 = [M4(f"If A : B = {a} : {b} and B : C = {b2} : {c}, then A : B : C is:", rt(a * (b2 // gcd(b, b2)), b * (b2 // gcd(b, b2)), ) + f" : {c * (b // gcd(b, b2))}", [rt(a, b) + f" : {c}", rt(a, b2) + f" : {c}", rt(a, b) + f" : {b2 * c}"], "Make the middle terms equal") for a, b, b2, c in [(2, 3, 6, 5), (3, 4, 8, 7), (1, 2, 6, 5), (4, 5, 10, 9), (2, 3, 9, 4)]]
nA3 = [M4(f"On a map, 1 cm represents {k} km. A distance of {d} cm on the map is actually:", f"{N(F(str(d))*k)} km", [f"{N(F(str(d))*k+k)} km", f"{N(F(str(d))*k/10)} km", f"{N(F(str(d))+k)} km"], f"${d}\\times{k}$") for k, d in [(5, 3.5), (12, 4), (8, 6.5), (25, 2.4), (15, 7)]]
nA4 = [M4(f"{m} workers can finish a job in {d} days. {n} workers will finish it in:", f"{N(F(m*d,n))} days", [f"{N(F(n*d,m))} days", f"{N(F(m*d,n)+2)} days", f"{N(d+m-n)} days"], "Fewer or more workers: days vary inversely") for m, d, n in [(8, 15, 12), (12, 20, 16), (6, 24, 9), (10, 18, 15), (15, 12, 20)]]
nA5 = [M4(f"A car covers {D} km in {t} hours at a steady speed. In {T} hours it covers:", f"{N(F(D,t)*T)} km", [f"{N(D+T)} km", f"{N(F(D,t)+T)} km", f"{N(F(D,t)*(T+1))} km"], f"Speed ${D}\\div{t}$") for D, t, T in [(240, 4, 7), (180, 3, 5), (330, 5, 8), (150, 2, 9), (420, 6, 4)]]
nA6 = [M4(f"₹ {n} is divided among A, B and C in the ratio {a} : {b} : {c}. The smallest share is:", R(share3(n, a, b, c)[0]), [R(share3(n, a, b, c)[1]), R(share3(n, a, b, c)[2]), R(n // 5)], f"One part $={n//(a+b+c)}$") for n, a, b, c in [(1200, 1, 3, 4), (1800, 2, 3, 4), (2400, 3, 4, 5), (1500, 2, 5, 8), (3000, 4, 5, 6)]]
nA7 = [M4("If the number of workers increases and the job remains the same, the time taken:", "decreases", ["increases", "stays the same", "becomes zero"], "Inverse proportion"),
       M4("The cost of articles and the number of articles (same price each) are in:", "direct proportion", ["inverse proportion", "no proportion", "equal ratio always 1 : 1"], "Double the articles, double the cost"),
       M4("Speed and time taken to cover a fixed distance are in:", "inverse proportion", ["direct proportion", "no proportion", "ratio 1 : 1"], "Speed x time = distance"),
       M4("In a proportion $a:b=c:d$, the product of the extremes equals:", "the product of the means", ["the sum of the means", "the sum of the extremes", "the first term"], "$ad=bc$")]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7]
NCERT_B = ([Q(f"Find the ratio of {a} m {b} cm to {c} cm in simplest form.", f"{a} m {b} cm $={a*100+b}$ cm (1); ratio $={srt(a*100+b,c)}$ (1).", "1+1") for a, b, c in [(3, 60, 90), (2, 10, 70), (5, 40, 180), (1, 80, 45)]]
           + [Q(f"{m} workers complete a task in {d} days. How many days will {n} workers take?", f"Total work $={m}\\times{d}={m*d}$ worker-days (1); days $={m*d}\\div{n}={N(F(m*d,n))}$ (1).", "1+1") for m, d, n in [(9, 16, 12), (14, 15, 10), (20, 9, 15), (7, 24, 8)]]
           + [Q(f"A map scale is 1 cm = {k} km. Find the actual distance for {d} cm and the map distance for {k*5} km.", f"{d} cm $\\to{N(F(str(d))*k)}$ km (1); {k*5} km $\\to5$ cm (1).", "1+1") for k, d in [(20, 3.5), (30, 4.2), (50, 2.6), (40, 6.5)]])
NCERT_C = ([Q(f"If A : B = {a} : {b} and B : C = {b2} : {c}, find A : B : C.", f"Make B equal: multiply first ratio by {b2//gcd(b,b2)}, second by {b//gcd(b,b2)} (1); A : B : C $={a*(b2//gcd(b,b2))}:{b*(b2//gcd(b,b2))}:{c*(b//gcd(b,b2))}$ (2).", "1+2") for a, b, b2, c in [(2, 3, 6, 5), (3, 4, 8, 7), (1, 2, 6, 5), (4, 5, 10, 9), (2, 3, 9, 4), (5, 6, 12, 7)]]
           + [Q(f"{m} men can build a wall in {d} days. How many days will {n} men take to build it?", f"Man-days $={m}\\times{d}={m*d}$ (1); days for {n} men $={m*d}\\div{n}$ (1); ${N(F(m*d,n))}$ days (1).", "1+1+1") for m, d, n in [(10, 18, 15), (12, 25, 20), (8, 30, 12), (14, 21, 7), (16, 15, 10), (9, 20, 6)]]
           + [Q(f"The ages of two friends are in the ratio {p} : {q} and the sum of their ages is {s*(p+q)} years. Find their ages after {k} years.", f"One part $={s}$ (1); present ages {p*s} and {q*s} (1); after {k} years {p*s+k} and {q*s+k} (1).", "1+1+1") for p, q, s, k in [(3, 5, 6, 4), (2, 3, 12, 5), (4, 7, 3, 6), (5, 6, 4, 8), (3, 4, 9, 3), (7, 8, 2, 10)]])
def nd1(n, a, b, c, x):
    sh = share3(n, a, b, c); new = (sh[0] + x, sh[1], sh[2] - x); g = gcd(gcd(new[0], new[1]), new[2])
    return Q(f"Divide ₹ {n} among A, B and C in the ratio {a} : {b} : {c}. If C gives ₹ {x} to A, find the new ratio of their amounts.", f"One part ₹ {n//(a+b+c)} (1); shares {R(sh[0])}, {R(sh[1])}, {R(sh[2])} (2); after the transfer {R(new[0])}, {R(new[1])}, {R(new[2])} (1); new ratio ${new[0]//g}:{new[1]//g}:{new[2]//g}$ (1).", "1+2+1+1")
def nd2(D, t, T, D2):
    return Q(f"A bus covers {D} km in {t} hours at a uniform speed. Find (i) its speed (ii) the distance it covers in {T} hours (iii) the time it takes to cover {D2} km.", f"(i) speed $={D}\\div{t}={N(F(D,t))}$ km/h (1.5); (ii) ${N(F(D,t))}\\times{T}={N(F(D,t)*T)}$ km (1.5); (iii) ${D2}\\div{N(F(D,t))}={N(F(D2*t,D))}$ hours (2).", "1½+1½+2")
NCERT_D = [nd1(*r) for r in [(1200, 1, 3, 4, 100), (1800, 2, 3, 4, 200), (2400, 3, 4, 5, 300), (1500, 2, 5, 8, 100), (3000, 4, 5, 6, 400), (2100, 1, 2, 4, 150)]] + [nd2(*r) for r in [(240, 4, 7, 360), (180, 3, 5, 270), (330, 5, 8, 462), (150, 2, 9, 600), (420, 6, 4, 210), (270, 3, 2, 405)]]

# ================= MEDIUM =================
mA1 = [M4(f"Two numbers are in the ratio {p} : {q} and their sum is {s*(p+q)}. The larger number is:", s * max(p, q), [s * min(p, q), s * (p + q) // 2, s * max(p, q) + s], f"One part $={s}$") for p, q, s in [(4, 7, 9), (5, 8, 6), (3, 10, 7), (6, 11, 4), (7, 9, 5)]]
mA2 = [M4(f"Two numbers are in the ratio {p} : {q}. If {k} is added to each, the numbers become {p*s+k} and {q*s+k}. The original smaller number is:", p * s if p < q else q * s, [(p * s if p < q else q * s) + k, (p * s if p < q else q * s) - k, (p * s if p < q else q * s) * 2], "Subtract the added number") for p, q, s, k in [(3, 5, 8, 4), (2, 7, 6, 3), (4, 9, 5, 5), (5, 6, 7, 2), (3, 8, 4, 6)]]
mA3 = [M4(f"A mixture of {V} L has milk and water in the ratio {p} : {q}. The quantity of water is:", f"{V*q//(p+q)} L", [f"{V*p//(p+q)} L", f"{V*q//(p+q)-5} L", f"{V*q//(p+q)+5} L"], f"$\\frac{{{q}}}{{{p+q}}}\\times{V}$") for V, p, q in [(60, 7, 3), (84, 5, 2), (90, 4, 5), (72, 5, 7), (110, 6, 5)]]
mA4 = [M4(f"{m} pipes fill a tank in {d} hours. {n} such pipes will fill it in:", f"{N(F(m*d,n))} hours", [f"{N(d+m-n)} hours", f"{N(m*d)} hours", f"{N(F(m*d,n)+3)} hours"], "More pipes, less time") for m, d, n in [(6, 10, 4), (8, 9, 12), (5, 12, 15), (9, 8, 6), (10, 12, 15)]]
def abc(a, b, b2, c):
    g = gcd(b, b2); m1, m2 = b2 // g, b // g
    return a * m1, b * m1, c * m2
def _mA5(a, b, b2, c, S):
    x = abc(a, b, b2, c); assert S % sum(x) == 0; s = S // sum(x)
    return M4(f"A : B = {a} : {b} and B : C = {b2} : {c}. If A + B + C = {S}, then C equals:", x[2] * s, [x[0] * s, x[1] * s, S // 5], f"A : B : C = {x[0]} : {x[1]} : {x[2]}, so one part is {s}")
mA5 = [_mA5(*t) for t in [(2, 3, 6, 5, 165), (1, 2, 4, 3, 135), (3, 4, 8, 7, 210), (2, 5, 10, 3, 119), (3, 2, 6, 5, 200)]]
mA6 = [M4(f"On a map with scale 1 : {N(s)}, a distance of {d} cm represents:", f"{N(F(s*d,100000))} km", [f"{N(F(s*d,10000))} km", f"{N(F(s*d,1000))} km", f"{N(F(s*d,100000)+d)} km"], "1 km = 100000 cm") for s, d in [(50000, 4), (200000, 3), (100000, 7), (25000, 8), (500000, 6)]]
mA7 = [M4(f"{v} km/h expressed in m/s is:", f"{N(F(v*5,18))} m/s", [f"{N(F(v*18,5))} m/s", f"{N(F(v,3))} m/s", f"{N(F(v,6))} m/s"], "Multiply by $\\frac{5}{18}$") for v in [36, 54, 72, 90, 108]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([Q(f"Two numbers are in the ratio {p} : {q} and their sum is {s*(p+q)}. Find the numbers.", f"One part $={s*(p+q)}\\div{p+q}={s}$ (1); numbers {p*s} and {q*s} (1).", "1+1") for p, q, s in [(5, 9, 7), (4, 11, 6), (7, 8, 5), (3, 13, 4)]]
         + [Q(f"Convert {v} km/h into m/s.", f"{v} km/h $={v}\\times\\frac{{1000}}{{3600}}$ (1) $={N(F(v*5,18))}$ m/s (1).", "1+1") for v in [45, 63, 81, 126]]
         + [Q(f"A map has scale 1 : {s}. Two places are {d} cm apart on the map. Find the actual distance in km.", f"Actual distance $={d}\\times{s}$ cm $={d*s}$ cm (1); $={N(F(d*s,100000))}$ km (1).", "1+1") for s, d in [(50000, 6), (200000, 4), (100000, 9), (250000, 5)]])
def waterx(V, p, q, p2, q2):
    milk = V * p // (p + q); water = V - milk; need = F(milk * q2, p2) - water
    return milk, water, need
MED_C = ([Q(f"A mixture of {V} L contains milk and water in the ratio {p} : {q}. How much water must be added to make the ratio {p} : {q2}?", f"Milk {waterx(V,p,q,p,q2)[0]} L, water {waterx(V,p,q,p,q2)[1]} L (1); new water $=\\frac{{{q2}}}{{{p}}}\\times{waterx(V,p,q,p,q2)[0]}={N(F(waterx(V,p,q,p,q2)[0]*q2,p))}$ L (1); add {N(waterx(V,p,q,p,q2)[2])} L (1).", "1+1+1") for V, p, q, q2 in [(40, 7, 1, 3), (60, 3, 2, 4), (45, 4, 5, 8), (72, 5, 3, 6), (66, 5, 6, 9), (80, 3, 1, 2)]]
         + [Q(f"A : B = {a} : {b} and B : C = {b2} : {c}. If A + B + C = {S}, find the three numbers.", f"A : B : C $={a*(b2//gcd(b,b2))}:{b*(b2//gcd(b,b2))}:{c*(b//gcd(b,b2))}$ (1); one part $={S//(a*(b2//gcd(b,b2))+b*(b2//gcd(b,b2))+c*(b//gcd(b,b2)))}$ (1); numbers {a*(b2//gcd(b,b2))*(S//(a*(b2//gcd(b,b2))+b*(b2//gcd(b,b2))+c*(b//gcd(b,b2))))}, {b*(b2//gcd(b,b2))*(S//(a*(b2//gcd(b,b2))+b*(b2//gcd(b,b2))+c*(b//gcd(b,b2))))}, {c*(b//gcd(b,b2))*(S//(a*(b2//gcd(b,b2))+b*(b2//gcd(b,b2))+c*(b//gcd(b,b2))))} (1).", "1+1+1") for a, b, b2, c, S in [(1, 2, 6, 5, 150), (3, 4, 8, 5, 143), (2, 3, 9, 4, 255), (1, 3, 9, 7, 195), (4, 5, 10, 3, 168), (2, 5, 10, 9, 190)]]
         + [Q(f"The ages of a mother and daughter are in the ratio {p} : {q}. The mother is {p*s} years old. Find their ages {k} years ago and the ratio then.", f"One part $={s}$; daughter {q*s} (1); {k} years ago: {p*s-k} and {q*s-k} (1); ratio ${srt(p*s-k,q*s-k)}$ (1).".replace("$", "$"), "1+1+1") for p, q, s, k in [(7, 3, 6, 4), (5, 2, 8, 6), (9, 4, 5, 5), (8, 3, 4, 2), (6, 1, 7, 7), (4, 1, 9, 3)]])
def md1(m, d, n, t):
    return Q(f"{m} men can complete a piece of work in {d} days. (i) How many days will {n} men take? (ii) How many men are needed to finish it in {t} days?", f"Total work $={m}\\times{d}={m*d}$ man-days (1); (i) ${m*d}\\div{n}={N(F(m*d,n))}$ days (2); (ii) ${m*d}\\div{t}={N(F(m*d,t))}$ men (2).", "1+2+2")
def md2(a, b, P):
    s = P // (a + b)
    return Q(f"Anil and Bhanu start a business with ₹ {a*1000} and ₹ {b*1000}. They share a profit of ₹ {P} in the ratio of their investments. Find the ratio of investments and each person's share.", f"Ratio ${srt(a,b)}$ (1); one part ₹ {s} (1); Anil {R(s*simp(a,b)[0])} (1.5); Bhanu {R(s*simp(a,b)[1])} (1.5).", "1+1+1½+1½") if (P % sum(simp(a, b))) == 0 else None
def md2b(a, b, P):
    sa, sb = simp(a, b); s = P // (sa + sb)
    return Q(f"Anil and Bhanu start a business with ₹ {a*1000} and ₹ {b*1000}. They share a profit of ₹ {P} in the ratio of their investments. Find the ratio of investments and each person's share.", f"Ratio ${sa}:{sb}$ (1); one part ₹ {s} (1); Anil {R(s*sa)} (1.5); Bhanu {R(s*sb)} (1.5).", "1+1+1½+1½")
MED_D = [md1(*r) for r in [(12, 15, 18, 9), (20, 24, 16, 30), (9, 40, 15, 12), (14, 18, 21, 12), (16, 21, 12, 14), (25, 12, 20, 15)]] + [md2b(*r) for r in [(15, 25, 800), (12, 18, 1500), (20, 30, 2000), (14, 21, 1750), (16, 24, 1200), (9, 15, 960)]]

# ================= HARD =================
def tri(x, y, c, d):
    g1, g2 = simp(x, y), simp(c, d); k1 = g2[0] // gcd(g1[1], g2[0]); k2 = g1[1] // gcd(g1[1], g2[0])
    return g1[0] * k1, g1[1] * k1, g2[1] * k2
hA1 = [M4(f"If x : y = {a} : {b} and y : z = {c} : {d}, then x : y : z is:", " : ".join(map(str, tri(a, b, c, d))), [f"{a} : {b} : {d}", f"{a*c} : {b*c} : {b*d}" if (a * c, b * c, b * d) != tri(a, b, c, d) else f"{a} : {c} : {d}", f"{a} : {b+c} : {d}"], "Make the middle terms equal using their LCM") for a, b, c, d in [(2, 3, 4, 7), (3, 4, 6, 5), (5, 6, 9, 4), (2, 5, 10, 3), (4, 9, 6, 7)]]
def age_pairs(p, q, s, k):
    p2, q2 = simp(p * s + k, q * s + k); assert (p2, q2) != simp(p, q)
    return p2, q2
hA2 = [M4(f"The present ages of two brothers are in the ratio {p} : {q}. After {k} years the ratio becomes {age_pairs(p,q,s,k)[0]} : {age_pairs(p,q,s,k)[1]}. The present age of the elder brother is:", f"{p*s} years", [f"{p*s+k} years", f"{q*s} years", f"{(p+q)*s} years"], f"Let the ages be ${p}x$ and ${q}x$; solving $({p}x+{k})\\times{age_pairs(p,q,s,k)[1]}=({q}x+{k})\\times{age_pairs(p,q,s,k)[0]}$ gives $x={s}$") for p, q, s, k in [(3, 2, 8, 4), (5, 3, 6, 6), (4, 3, 5, 5), (7, 5, 3, 3), (6, 5, 4, 8)]]
def recip(n, a, b, c):
    l = lcm3(a, b, c); w = (l // a, l // b, l // c); assert n % sum(w) == 0, (n, a, b, c); s = n // sum(w); return tuple(x * s for x in w)
hA3 = [M4(f"₹ {n} is divided in parts proportional to $\\frac{{1}}{{{a}}}$, $\\frac{{1}}{{{b}}}$ and $\\frac{{1}}{{{c}}}$. The largest part is:", R(max(recip(n, a, b, c))), [R(min(recip(n, a, b, c))), R(n // 5), R(sorted(recip(n, a, b, c))[1])], "Convert the reciprocals to whole-number ratio using the LCM") for n, a, b, c in [(1300, 2, 3, 4), (1900, 2, 4, 5), (1050, 3, 5, 6), (1880, 2, 5, 10), (1200, 2, 3, 6)]]
def rem_days(m, d, t, j): done = m * t; left = m * d - done; return F(left, m + j)
hA4 = [M4(f"{m} men can finish a job in {d} days. After {t} days, {j} more men join. The remaining work will be finished in:", f"{N(rem_days(m,d,t,j))} days", [f"{N(d-t)} days", f"{N(rem_days(m,d,t,j)+2)} days", f"{N(F(m*d,m+j))} days"], "Find the work left in man-days and divide by the new number of men") for m, d, t, j in [(12, 20, 8, 4), (10, 24, 6, 5), (15, 18, 6, 5), (8, 30, 10, 2), (24, 20, 5, 6)]]
hA5 = [M4(f"Two trains cover the same distance at speeds in the ratio {a} : {b}. The ratio of the times they take is:", rt(b, a), [rt(a, b), rt(a + b, a), rt(a * a, b * b)], "Time is inversely proportional to speed") for a, b in [(4, 5), (3, 7), (5, 9), (2, 11), (6, 7)]]
hA6 = [M4(f"If {a} : {b} = {a*k} : {b*k}, then ({a}+{b}) : {b} = $x$ : {b*k}, where $x$ is:", (a + b) * k, [a * k, (a + b) * k + b, b * k], "Adding the denominators keeps the ratio") for a, b, k in [(3, 5, 4), (2, 7, 3), (5, 6, 5), (4, 9, 2)]]
hA7 = [M4(f"The sides of two squares are in the ratio {p} : {q}. The ratio of their areas is:", rt(p * p, q * q), [rt(p, q), rt(p, q * q), rt(p * p, q)], "Area $=$ side$^2$") for p, q in [(2, 3), (3, 5), (4, 7), (5, 6)]]
hA8 = [M4(f"The number $x$ for which {a} : {b} = {c} : $x$ is:", b * c // a, [b + c, c - a + b + 1, a + b + c], f"$x=\\frac{{{b}\\times{c}}}{{{a}}}$") for a, b, c in [(4, 9, 12), (6, 5, 18), (5, 8, 15), (7, 3, 21), (9, 4, 27)]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([Q(f"The sides of two squares are in the ratio {p} : {q}. Find the ratio of their perimeters and of their areas.", f"Perimeters ${p}:{q}$ (1); areas ${p*p}:{q*q}$ (1).", "1+1") for p, q in [(3, 7), (4, 5), (6, 11), (2, 9)]]
          + [Q(f"If x : y = {a} : {b}, find the ratio (x + y) : (x - y).", f"Take $x={a}k$, $y={b}k$ (1); $({a+b}k):({a-b}k)={srt(a+b,a-b)}$ (1).", "1+1") for a, b in [(7, 3), (9, 5), (11, 4), (13, 7)]]
          + [Q(f"Divide ₹ {n} into parts proportional to $\\frac{{1}}{{{a}}}$ and $\\frac{{1}}{{{b}}}$.", f"Ratio $\\frac1{{{a}}}:\\frac1{{{b}}}={b}:{a}$ (1); parts {R(n//(a+b)*b)} and {R(n//(a+b)*a)} (1).", "1+1") for n, a, b in [(1200, 2, 3), (1400, 3, 4), (1500, 2, 3), (1800, 4, 5)]])
assert all(n % (a + b) == 0 for n, a, b in [(1200, 2, 3), (1400, 3, 4), (1500, 2, 3), (1800, 4, 5)])
HARD_C = ([Q(f"The ratio of the present ages of a father and son is {p} : {q}. After {k} years the ratio will be {age_pairs(p,q,s,k)[0]} : {age_pairs(p,q,s,k)[1]}. Find their present ages.", f"Let ages be ${p}x$ and ${q}x$ (1); $({p}x+{k})\\times{age_pairs(p,q,s,k)[1]}=({q}x+{k})\\times{age_pairs(p,q,s,k)[0]}$ gives $x={s}$ (1); ages {p*s} and {q*s} years (1).", "1+1+1") for p, q, s, k in [(3, 1, 8, 4), (5, 2, 6, 6), (4, 1, 10, 10), (7, 3, 4, 2), (5, 3, 6, 6), (8, 3, 4, 4)]]
          + [Q(f"{m} men can finish a job in {d} days. After {t} days, {j} more men join them. In how many more days is the job finished?", f"Total work $={m*d}$ man-days; done $={m*t}$ (1); left $={m*d-m*t}$ (1); days $={m*d-m*t}\\div{m+j}={N(rem_days(m,d,t,j))}$ (1).", "1+1+1") for m, d, t, j in [(15, 24, 8, 5), (10, 21, 6, 5), (16, 18, 6, 8), (18, 20, 4, 6), (20, 15, 5, 5), (12, 24, 6, 6)]]
          + [Q(f"Divide ₹ {n} into three parts proportional to $\\frac{{1}}{{{a}}}$, $\\frac{{1}}{{{b}}}$ and $\\frac{{1}}{{{c}}}$.", f"LCM of {a}, {b}, {c} is {lcm3(a,b,c)}; ratio ${lcm3(a,b,c)//a}:{lcm3(a,b,c)//b}:{lcm3(a,b,c)//c}$ (2); parts {', '.join(R(x) for x in recip(n,a,b,c))} (1).", "2+1") for n, a, b, c in [(2600, 2, 3, 4), (3800, 2, 4, 5), (2100, 3, 5, 6), (3760, 2, 5, 10), (2400, 2, 3, 6), (2850, 2, 4, 5)]])
for _m, _d, _t, _j in [(15, 24, 8, 5), (10, 21, 6, 5), (16, 18, 6, 8), (18, 20, 4, 6), (20, 15, 5, 5), (12, 24, 6, 6)]:
    assert rem_days(_m, _d, _t, _j).denominator == 1
def hd1(a, m, b, n, c, o, unit):
    w = (a * m, b * n, c * o); g = gcd(gcd(w[0], w[1]), w[2]); w = tuple(x // g for x in w); P = sum(w) * unit
    return Q(f"A, B and C invest ₹ {a*1000}, ₹ {b*1000} and ₹ {c*1000} for {m}, {n} and {o} months respectively. A profit of ₹ {P} is shared in the ratio of (investment $\\times$ time). Find the ratio and each share.", f"Investment $\\times$ time: {a*m}, {b*n}, {c*o} (1); ratio ${w[0]}:{w[1]}:{w[2]}$ (1); one part ₹ {unit} (1); shares {R(w[0]*unit)}, {R(w[1]*unit)}, {R(w[2]*unit)} (2).", "1+1+1+2")
def hd2(V, p, q, x):
    milk = F(V * p, p + q); water = F(V * q, p + q); mr = F(x * p, p + q); wr = F(x * q, p + q)
    m2 = milk - mr; w2 = water - wr + x; f = m2 / w2
    return Q(f"A vessel holds {V} L of a mixture of milk and water in the ratio {p} : {q}. {x} L of the mixture is removed and replaced by {x} L of water. Find the new ratio of milk to water.", f"Milk {N(milk)} L, water {N(water)} L (1); in {x} L removed: milk {N(mr)} L, water {N(wr)} L (1); milk left {N(m2)} L (1); water now ${N(water)}-{N(wr)}+{x}={N(w2)}$ L (1); ratio ${f.numerator}:{f.denominator}$ (1).", "1+1+1+1+1")
HARD_D = [hd1(*r) for r in [(2, 6, 3, 4, 5, 3, 100), (3, 4, 2, 6, 4, 2, 150), (5, 3, 4, 3, 6, 2, 120), (4, 6, 5, 4, 3, 8, 80), (6, 5, 4, 6, 2, 9, 90), (3, 8, 5, 4, 2, 6, 110)]] + [hd2(*r) for r in [(60, 2, 1, 15), (90, 5, 4, 18), (80, 3, 1, 20), (100, 7, 3, 10), (70, 4, 3, 14), (120, 5, 3, 24)]]

TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}

from c8m_fix import tidy
tidy(TIERS)
