"""Class 8 Maths Ch 3 - A Story of Numbers. Graded banks; conversions and arithmetic computed in code."""
from c8m_h import *

SLUG, NAME, CHNO = "Story_of_Numbers", "A Story of Numbers", 3

RV = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]
def roman(n):
    s = ""
    for v, r in RV:
        while n >= v: s += r; n -= v
    return s
def tb(n, b):
    if n == 0: return "0"
    s = ""
    while n: s = str(n % b) + s; n //= b
    return s
def fb(s, b): return int(s, b)
def BS(s, b): return f"${s}_{{{b}}}$"
def bs(s, b): return f"{s}_{{{b}}}"
def exp(s, b):
    L = len(s); return "+".join(f"{d}\\times{b}^{{{L-1-i}}}" for i, d in enumerate(s))
def divs(n, b):
    out = []
    while n:
        out.append(f"{n}={b}\\times{n//b}+{n%b}"); n //= b
    return "; ".join(f"${x}$" for x in out)
def rev(s): return s[::-1]
def numw(n, k=10): return [n + 2, n - 2, n + k]

# ================= EASY =================
eA1 = [M4(f"The value of the Roman numeral {roman(n)} is:", n, numw(n), "Add the values of the symbols, subtracting a smaller symbol placed before a larger one") for n in [17, 24, 39, 56, 90, 114]]
eA2 = [M4(f"The Roman numeral for {n} is:", roman(n), [roman(n + 1), roman(n - 1), roman(n + 10)], f"{n} is written as {roman(n)}") for n in [8, 19, 34, 49, 66, 91]]
eA3 = [M4(f"The decimal value of ${s}_2$ is:", fb(s, 2), numw(fb(s, 2), 4), f"Add the powers of 2 where there is a 1") for s in ["101", "110", "1001", "1011", "1101", "1111"]]
eA4 = [M4(f"The number {n} in binary is:", tb(n, 2), [tb(n + 1, 2), tb(n - 1, 2), tb(n + 2, 2)], "Divide repeatedly by 2 and read the remainders upwards") for n in [5, 9, 12, 13, 6, 14]]
eA5 = [M4(f"The place value of the digit {d} in {N} is:", d * 10 ** str(N)[::-1].index(str(d)), [d, d * 10 ** (str(N)[::-1].index(str(d)) + 1), d * 10 ** (str(N)[::-1].index(str(d)) + 2) if str(N)[::-1].index(str(d)) < 1 else d * 10 ** (str(N)[::-1].index(str(d)) - 1)], "Place value = digit x value of its position") for d, N in [(6, 3652), (4, 8409), (7, 2735), (9, 9140), (3, 6031)]]
eA6 = [M4(f"The digits used in the base-{b} system are:", f"0 to {b-1}", [f"1 to {b}", f"0 to {b}", f"1 to {b-1}"], f"Base {b} uses {b} digits starting from 0") for b in [2, 3, 4, 5, 6, 8]]
eA7 = [M4(f"The Roman symbol for {v} is:", s, [x for x in "IVXLCDM" if x != s][:3], "Learn the seven Roman symbols") for v, s in [(50, "L"), (100, "C"), (500, "D"), (1000, "M")]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7]
EASY_B = ([Q(f"Write the Roman numeral for {n}.", f"{n} = {roman(n)} (2).", "2") for n in [27, 44, 78, 95]]
          + [Q(f"Convert ${s}_2$ to a decimal number.", rf"${exp(s,2)}={fb(s,2)}$ (1+1).", "1+1") for s in ["111", "1010", "1100", "10001"]]
          + [Q(f"Write {n} in binary.", f"Repeated division by 2 gives {n} = ${tb(n,2)}_2$ (1+1).", "1+1") for n in [7, 10, 15, 18]])
EASY_C = ([Q(f"Write {roman(a)} and {roman(b)} as Hindu-Arabic numbers.", f"{roman(a)} = {a} (1); {roman(b)} = {b} (1); add the symbol values, subtract when a smaller symbol comes before a larger one (1).", "1+1+1") for a, b in [(47, 164), (38, 229), (84, 390), (59, 148), (73, 216), (96, 475)]]
          + [Q(f"Write {N} in expanded form.", rf"${exp(str(N),10)}$ (3).", "3") for N in [4086, 7305, 2918, 6420, 9057, 3764]]
          + [Q(f"Convert ${s}_5$ to a decimal number.", rf"${exp(s,5)}$ (1+1); $={fb(s,5)}$ (1).", "1+1+1") for s in ["123", "241", "304", "412", "134", "230"]])
EASY_D = ([Q(f"Write the Roman numerals for {', '.join(map(str, xs[:-1]))} and {xs[-1]}.", "; ".join(f"{x} = {roman(x)} (1)" for x in xs) + ".", "1+1+1+1+1") for xs in [[12, 25, 38, 46, 59], [14, 29, 43, 67, 82], [16, 33, 48, 74, 99], [18, 37, 52, 88, 94], [21, 45, 63, 79, 97], [24, 39, 56, 71, 86]]]
          + [Q(f"Convert {n} to binary by repeated division by 2 and show the steps.", f"Steps: {divs(n,2)} (3); reading remainders from last to first gives ${tb(n,2)}_2$ (2).", "3+2") for n in [19, 26, 35, 41, 52, 58]])

# ================= NCERT =================
VAL = ["IV", "IX", "XL", "XC", "CD", "CM", "VI", "XIV", "XIX", "XLIV"]; INV = ["IC", "VX", "IL", "XM", "VL", "IM", "LC", "DM"]
nA1 = [M4("Which of the following is NOT a correct Roman numeral?", INV[i], [VAL[(3 * i + j) % len(VAL)] for j in range(3)], "I can be subtracted only from V and X; X only from L and C; C only from D and M; V, L, D are never subtracted") for i in range(6)]
nA2 = [M4(f"The decimal value of ${s}_{{{b}}}$ is:", fb(s, b), numw(fb(s, b), 5), "Multiply each digit by the power of the base and add") for b, s in [(5, "243"), (8, "175"), (3, "1201"), (4, "3021"), (6, "254")]]
nA3 = [M4(f"The number {n} written in base {b} is:", tb(n, b), [rev(tb(n, b)) if rev(tb(n, b)) != tb(n, b) else tb(n + 2, b), tb(n + 1, b), tb(n - 1, b)], "Divide repeatedly by the base and read the remainders upwards") for b, n in [(5, 87), (8, 150), (3, 50), (4, 100), (6, 95)]]
nA4 = [M4(f"A Babylonian numeral has {a} group(s) of 60 and {b} units. Its value is:", a * 60 + b, [a + b, a * 60 - b, a * 6 + b], "Base 60: value = 60 x first + second") for a, b in [(2, 15), (3, 40), (1, 25), (4, 5), (5, 30)]]
nA5 = [M4(f"A Maya numeral has {a} in the 20s place and {b} in the units place. Its value is:", a * 20 + b, [a + b, a * 10 + b, a * 20 - b], "Base 20: value = 20 x first + second") for a, b in [(3, 12), (5, 7), (11, 4), (14, 9), (2, 18)]]
nA6 = [M4("The number system we use today is called the:", "Hindu-Arabic system", ["Roman system", "Babylonian system", "Maya system"], "Digits 0-9 with place value came from India and spread through Arabs"),
       M4("Which Roman symbols are never repeated?", "V, L and D", ["I, X and C", "I, V and X", "C, D and M"], "Only I, X, C and M may be repeated (up to three times)"),
       M4("The Roman symbol I can be repeated at most:", "3 times", ["2 times", "4 times", "5 times"], "III is 3; IIII is not used"),
       M4("Brahmagupta (628 CE) gave rules for operations with:", "zero and negative numbers", ["fractions only", "Roman numerals only", "binary numbers"], "Brahmagupta described how to add, subtract and multiply with zero and negatives"),
       M4("The base of the Maya number system was:", "20", ["10", "60", "5"], "Maya numerals used dots, bars and a shell with base 20"),
       M4("The base of the Babylonian number system was:", "60", ["10", "20", "12"], "Sexagesimal system"),
       M4("Computers store information using the base:", "2", ["8", "10", "16"], "Binary digits 0 and 1 (bits)")]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6]
NCERT_B = ([Q(f"Convert ${s}_{{{b}}}$ to a decimal number.", rf"${exp(s,b)}$ (1); $={fb(s,b)}$ (1).", "1+1") for b, s in [(5, "314"), (8, "263"), (3, "2102"), (6, "145")]]
           + [Q(f"Write {n} in the binary system.", f"{divs(n,2)} (1); ${tb(n,2)}_2$ (1).", "1+1") for n in [29, 37, 45, 53]]
           + [Q(f"A Babylonian numeral is made of {a} sixties and {b} units, and a Maya numeral has {c} twenties and {d} units. Find their values.", f"Babylonian: ${a}\\times60+{b}={a*60+b}$ (1); Maya: ${c}\\times20+{d}={c*20+d}$ (1).", "1+1") for a, b, c, d in [(3, 25, 4, 11), (2, 48, 6, 9), (5, 12, 8, 14), (4, 33, 9, 3)]])
NCERT_C = ([Q(f"Convert {n} to base {b} and check your answer by converting back to decimal.", f"{divs(n,b)} (1); ${tb(n,b)}_{{{b}}}$ (1); check ${exp(tb(n,b),b)}={n}$ (1).", "1+1+1") for n, b in [(137, 5), (214, 8), (89, 3), (175, 6), (250, 4), (333, 7)]]
           + [Q(f"Find {roman(a)} + {roman(b)} and write the answer in Roman numerals.", f"{roman(a)} = {a}, {roman(b)} = {b} (1); sum = {a+b} (1); {roman(a+b)} (1).", "1+1+1") for a, b in [(44, 67), (89, 123), (156, 249), (275, 318), (49, 951), (362, 438)]]
           + [Q(f"Write ${s}_{{{b}}}$ in expanded form and find its decimal value.", rf"${exp(s,b)}$ (2); $={fb(s,b)}$ (1).", "2+1") for b, s in [(5, "2431"), (8, "3704"), (3, "21012"), (6, "5043"), (4, "30213"), (7, "6150")]])
NCERT_D = ([Q(f"Add the binary numbers ${tb(a,2)}_2$ and ${tb(b,2)}_2$. Verify your answer by converting to decimal.", f"Column addition with carries gives ${tb(a+b,2)}_2$ (3); decimal check: ${a}+{b}={a+b}$ and ${tb(a+b,2)}_2={a+b}$ (2).", "3+2") for a, b in [(13, 7), (25, 14), (19, 11), (30, 21), (27, 9), (22, 18)]]
           + [Q(f"A shopkeeper has weights of 1, 2, 4, 8, 16 and 32 kg. Show how to weigh exactly {w} kg using these weights, each at most once. Explain the idea using binary numbers.", f"${w}={tb(w,2)}_2$ (2); weights used: {', '.join(str(2**i) for i, d in enumerate(reversed(tb(w,2))) if d=='1')} kg (2); each 1 in the binary number means that weight is used (1).", "2+2+1") for w in [13, 21, 27, 35, 44, 51]])

# ================= MEDIUM =================
mA1 = [M4(f"The decimal value of ${s}_{{{b}}}$ is:", fb(s, b), numw(fb(s, b), 6), "Expand with powers of the base") for b, s in [(2, "10110"), (2, "11011"), (3, "2102"), (5, "1431"), (8, "374")]]
mA2 = [M4(f"The binary form of {n} is:", tb(n, 2), [tb(n + 1, 2), tb(n - 1, 2), rev(tb(n, 2)) if rev(tb(n, 2)) != tb(n, 2) else tb(n + 4, 2)], "Repeated division by 2") for n in [45, 54, 37, 62, 29]]
mA3 = [M4(f"{roman(a)} + {roman(b)} equals:", roman(a + b), [roman(a + b + 1), roman(a + b - 10), roman(a + b + 10)], f"{a}+{b}={a+b}") for a, b in [(44, 67), (78, 134), (96, 208), (189, 311), (245, 369)]]
mA4 = [M4(f"The largest 3-digit number in base {b}, written in decimal, is:", b ** 3 - 1, [b ** 3, b ** 2 - 1, 3 * b - 1], f"It is ${b-1}{b-1}{b-1}_{{{b}}}={b}^3-1$") for b in [2, 3, 5, 6, 8]]
mA5 = [M4(f"The number of digits in the binary form of {n} is:", len(tb(n, 2)), [len(tb(n, 2)) + 1, len(tb(n, 2)) - 1, len(tb(n, 2)) + 2], f"{n} lies between $2^{{{len(tb(n,2))-1}}}$ and $2^{{{len(tb(n,2))}}}$") for n in [20, 50, 127, 128, 300]]
mA6 = [M4(rf"${tb(a,2)}_2+{tb(b,2)}_2$ equals:", f"${tb(a+b,2)}_2$", [f"${tb(a+b+1,2)}_2$", f"${tb(a+b-1,2)}_2$", f"${tb(a+b+2,2)}_2$"], f"{a}+{b}={a+b}") for a, b in [(11, 6), (13, 5), (9, 7), (14, 3), (21, 10)]]
mA7 = [M4(f"In ${s}_{{{b}}}$, the value (in decimal) contributed by the digit {s[i]} in position {i+1} from the left is:", int(s[i]) * b ** (len(s) - 1 - i), [int(s[i]) * b ** (len(s) - i), int(s[i]) * b, int(s[i]) + b ** (len(s) - 1 - i)], "Digit x (base)^(position from right, starting 0)") for s, b, i in [("2403", 5, 1), ("3721", 8, 0), ("1202", 3, 1), ("45", 6, 0)]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([Q(f"Convert ${s}_{{{b}}}$ to decimal.", rf"${exp(s,b)}$ (1); $={fb(s,b)}$ (1).", "1+1") for b, s in [(2, "110101"), (3, "20121"), (5, "3402"), (8, "5163")]]
         + [Q(f"Write {roman(a)} + {roman(b)} as a Roman numeral.", f"{a} + {b} = {a+b} (1); {roman(a+b)} (1).", "1+1") for a, b in [(139, 262), (87, 513), (176, 424), (348, 267)]]
         + [Q(f"Subtract ${tb(a,2)}_2-{tb(b,2)}_2$ and give the answer in binary.", f"In decimal {a}-{b}={a-b} (1); ${tb(a-b,2)}_2$ (1).", "1+1") for a, b in [(26, 9), (35, 12), (47, 18), (58, 23)]])
MED_C = ([Q(f"Convert ${s}_{{{a}}}$ to base {b} by first converting to decimal.", f"${exp(s,a)}={fb(s,a)}$ (1); {divs(fb(s,a),b)} (1); ${tb(fb(s,a),b)}_{{{b}}}$ (1).", "1+1+1") for a, s, b in [(2, "101101", 8), (5, "1432", 8), (8, "571", 5), (3, "2201", 5), (2, "110011", 4), (6, "243", 8)]]
         + [Q(f"Multiply ${tb(a,2)}_2\\times{tb(b,2)}_2$ and give the answer in binary.", f"Decimal values {a} and {b} (1); product {a*b} (1); ${tb(a*b,2)}_2$ (1).", "1+1+1") for a, b in [(5, 3), (6, 5), (7, 3), (9, 5), (11, 3), (6, 7)]]
         + [Q(f"Write {a} and {b} in Roman numerals and find their difference in Roman numerals.", f"{a} = {roman(a)}, {b} = {roman(b)} (1); difference = {a-b} (1); {roman(a-b)} (1).", "1+1+1") for a, b in [(1994, 449), (2024, 1999), (1486, 349), (3000, 1776), (2450, 899), (1999, 749)]])
MED_D = ([Q(f"Find the sum of ${tb(a,2)}_2$, ${tb(b,2)}_2$ and ${tb(c,2)}_2$. Verify the result in decimal.", f"Add in binary: ${tb(a+b+c,2)}_2$ (3); decimal check ${a}+{b}+{c}={a+b+c}$ (2).", "3+2") for a, b, c in [(13, 9, 6), (17, 11, 5), (22, 7, 12), (25, 14, 9), (30, 11, 7), (19, 15, 8)]]
         + [Q(f"Write the smallest and the largest {k}-digit numbers in base {b} and find their decimal values. How many {k}-digit numbers are there in base {b}?", f"Smallest ${bs('1'+'0'*(k-1),b)}={b**(k-1)}$ (2); largest ${bs(str(b-1)*k,b)}={b**k-1}$ (2); count ${b**k}-{b**(k-1)}={b**k-b**(k-1)}$ (1).", "2+2+1") for b, k in [(2, 5), (3, 4), (5, 3), (4, 4), (6, 3), (7, 3)]])

# ================= HARD =================
def unk(b, p, q): return p * b + q
hA1 = [M4(f"If $({p}{q})_b={unk(b,p,q)}$ in decimal (a two-digit number in base $b$), then $b$ equals:", b, [b + 1, b - 1, b + 2], f"${p}b+{q}={unk(b,p,q)}$") for b, p, q in [(5, 3, 4), (6, 2, 5), (7, 4, 3), (8, 5, 6), (9, 3, 7)]]
hA2 = [M4(f"Weights of 1, 2, 4, 8, ... kg (powers of 2) are available. The least number of weights needed to weigh any whole number of kg up to {W} kg is:", W.bit_length(), [W.bit_length() + 1, W.bit_length() - 1, W // 10], "Number of binary digits of the largest weight to be measured") for W in [31, 100, 63, 200, 1000]]
HS = [([("1101", 2), ("32", 5), ("14", 8), ("16", 10)], "greatest"), ([("10110", 2), ("41", 5), ("24", 8), ("19", 10)], "smallest"), ([("111101", 2), ("203", 5), ("76", 8), ("60", 10)], "greatest"), ([("1011", 2), ("13", 5), ("11", 8), ("10", 10)], "smallest")]
def pick(s, w):
    f = (max if w == "greatest" else min)(s, key=lambda t: fb(*t)); vs = [fb(*t) for t in s]; assert len(set(vs)) == 4
    return [BS(*f)] + [BS(*t) for t in s if t != f]
hA3 = [M4(f"Which of the following numbers is the {w}?", pick(s, w)[0], pick(s, w)[1:], "Convert every number to decimal and compare") for s, w in HS]
hA4 = [M4(f"The number of 1s in the binary form of {n} is:", bin(n).count("1"), [bin(n).count("1") + 1, bin(n).count("1") - 1, bin(n).count("1") + 2], f"{n} = ${tb(n,2)}_2$") for n in [77, 150, 255, 341, 100, 219]]
hA5 = [M4(f"The Roman numeral for {n} is:", roman(n), [roman(n + 1), roman(n - 1), roman(n + 10)], f"Break {n} into thousands, hundreds, tens and units") for n in [1994, 2449, 3888, 1649]]
hA6 = [M4(f"The number that comes immediately after ${s}_2$ in the binary system is:", f"${tb(fb(s,2)+1,2)}_2$", [f"${tb(fb(s,2)+2,2)}_2$", f"${s}1_2$".replace("_2$", "$") if False else f"${tb(fb(s,2)-1,2)}_2$", f"${s+'0'}_2$"], "Add 1 and carry in base 2") for s in ["10111", "11011", "101111", "110011"]]
hA7 = [M4(f"A number written in base {b} ending in the digit 0 is always divisible by:", b, [b + 1, b - 1, 10], f"The last place has value {b}, so the number is a multiple of {b}") for b in [3, 5, 6, 8]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7]
HARD_B = ([Q(f"Find the base $b$ if $({p}{q})_b={unk(b,p,q)}$ in decimal.", f"${p}b+{q}={unk(b,p,q)}$ (1); $b={b}$ (1).", "1+1") for b, p, q in [(5, 2, 3), (7, 5, 2), (8, 4, 6), (9, 6, 1)]]
          + [Q(f"Write {n} in binary and count the number of 1s in it.", f"{divs(n,2)} (1); ${tb(n,2)}_2$ has {bin(n).count('1')} ones (1).", "1+1") for n in [90, 157, 203, 118]]
          + [Q(f"Convert the Roman numeral {roman(n)} to binary.", f"{roman(n)} = {n} (1); ${tb(n,2)}_2$ (1).", "1+1") for n in [127, 244, 169, 330]])
HARD_C = ([Q(f"A trader has weights of 1, 2, 4, 8, 16, 32 and 64 g. How can she weigh exactly {w} g? Explain using binary numbers.", f"${w}={tb(w,2)}_2$ (1); weights used: {', '.join(str(2**i) for i, d in enumerate(reversed(tb(w,2))) if d=='1')} g (1); each 1 means the weight is used (1).", "1+1+1") for w in [45, 77, 102, 89, 111, 58]]
          + [Q(f"Add ${tb(a,b)}_{{{b}}}$ and ${tb(c,b)}_{{{b}}}$ (numbers in base {b}) and give the answer in base {b}.", f"Decimal values {a} and {c} (1); sum {a+c} (1); ${tb(a+c,b)}_{{{b}}}$ (1).", "1+1+1") for b, a, c in [(5, 98, 57), (8, 205, 134), (3, 40, 29), (6, 131, 85), (4, 70, 53), (7, 150, 99)]]
          + [Q(f"How many different numbers can be written using at most {k} digits in base {b}? What is the largest of them in decimal?", f"Each of the {k} places has {b} choices, so ${b}^{{{k}}}={b**k}$ numbers (2); largest ${b**k-1}$ (1).", "2+1") for b, k in [(2, 8), (3, 5), (5, 4), (4, 5), (6, 4), (8, 3)]])
HARD_D = ([Q(f"In some base $b$ the number $({x}{y}{z})_b$ equals {unk(b,x,0)*b+y*b+z if False else x*b*b+y*b+z} in decimal. Find $b$ and write the number in base 10 form.", f"Digits are all less than $b$, so $b>{max(x,y,z)}$ (1); ${x}b^2+{y}b+{z}={x*b*b+y*b+z}$ (2); trying $b={b}$ gives ${x*b*b}+{y*b}+{z}={x*b*b+y*b+z}$ (1); so $b={b}$ (1).", "1+2+1+1") for b, x, y, z in [(5, 2, 3, 4), (6, 1, 4, 5), (7, 3, 2, 6), (8, 2, 5, 7), (9, 1, 7, 8), (4, 3, 2, 1)]]
          + [Q(f"Subtract ${tb(a,b)}_{{{b}}}-{tb(c,b)}_{{{b}}}$ in base {b}. Verify your answer in decimal.", f"Decimal values {a} and {c} (1); difference {a-c} (2); ${tb(a-c,b)}_{{{b}}}$ (1); check by converting back (1).", "1+2+1+1") for b, a, c in [(5, 187, 96), (8, 300, 149), (6, 211, 98), (3, 77, 35), (7, 260, 133), (4, 150, 71)]])

TIERS = {"NCERT": T(NCERT_A, NCERT_B, NCERT_C, NCERT_D), "Easy": T(EASY_A, EASY_B, EASY_C, EASY_D),
         "Medium": T(MED_A, MED_B, MED_C, MED_D), "Hard": T(HARD_A, HARD_B, HARD_C, HARD_D)}
