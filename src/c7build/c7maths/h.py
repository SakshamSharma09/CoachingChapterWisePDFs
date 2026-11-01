import random
from lib import mcq, Q, OR
from mk9 import M4, build
def ind(n):
    s = str(n)
    if len(s) <= 3: return s
    h, t = s[:-3], s[-3:]
    parts = []
    while len(h) > 2: parts.insert(0, h[-2:]); h = h[:-2]
    if h: parts.insert(0, h)
    return ",".join(parts + [t])
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def w2(n):
    if n < 20: return ONES[n]
    return TENS[n // 10] + ("" if n % 10 == 0 else " " + ONES[n % 10])
def words(n):
    out = []
    for val, nm in ((10**7, "crore"), (10**5, "lakh"), (10**3, "thousand"), (100, "hundred")):
        q, n = divmod(n, val)
        if q: out.append(f"{w2(q) if q < 100 else words(q)} {nm}")
    if n: out.append(w2(n))
    return " ".join(out)
