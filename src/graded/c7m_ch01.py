"""Class 7 Maths Ch 1 - Large Numbers."""
from g67 import *

SLUG, NAME, CHNO = "Large_Numbers", "Large Numbers", 1

ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
def w99(n):
    if n < 20: return ONES[n]
    return TENS[n // 10] + ("-" + ONES[n % 10] if n % 10 else "")
def w999(n):
    h, r = divmod(n, 100)
    return (ONES[h] + " hundred" + (" " if r else "") if h else "") + (w99(r) if r else "")
def words(n):
    parts = []
    for name, v in [("crore", 10 ** 7), ("lakh", 10 ** 5), ("thousand", 1000)]:
        q, n = divmod(n, v)
        if q: parts.append(w99(q) + " " + name) if q < 100 else parts.append(w999(q) + " " + name)
    if n: parts.append(w999(n))
    return " ".join(parts)
def tz(n): return "$" + str(n) + "$"
def sci(k): return f"$10^{{{k}}}$"

# ---------- EASY ----------
eA1 = [tm(f"The number {ind(n)} is read as:", words(n), [words(n + 1000), words(n * 10), words(int(str(n)[::-1]))], "Read period by period: crore, lakh, thousand.") for n in [345678, 2060000, 8120305, 90001, 4007000]]
eA2 = [tm(f"In the Indian system, '{words(n)}' is written as:", ind(n), [ind(n * 10), ind(n // 10), ind(n + 1000)], "Place each period.") for n in [253400, 7005006, 18090000, 600350]]
eA3 = [tm(f"{ind(a)} + {ind(b)} =", ind(a + b), [ind(a + b + 1000), ind(a + b - 100), ind(a + b + 10000)], "Add and re-insert commas.") for a, b in [(125000, 348000), (234567, 123433), (1250000, 875000), (408090, 391910), (3500000, 2650000)]]
eA4 = [tm(f"{ind(a)} - {ind(b)} =", ind(a - b), [ind(a - b + 10000), ind(a - b - 1000), ind(a - b + 100)], "Subtract place by place.") for a, b in [(500000, 123456), (1000000, 349000), (7500000, 2450000), (900000, 456789)]]
eA5 = [tm(f"One {nm_} equals:", v, [x for x in ["1,00,000", "10,00,000", "1,00,00,000", "10,000"] if x != v][:3], "Indian place value system.") for nm_, v in [("lakh", "1,00,000"), ("crore", "1,00,00,000"), ("ten lakh", "10,00,000")]]
eA6 = [nm(f"Round {n} to the nearest thousand:", rnd(n, 1000), "Look at the hundreds digit.", offs=(1000, -1000, 100, 10000)) for n in [48376, 123789, 560499, 2345500]]
eA7 = [nm(f"How many digits does the number {ind(n)} have?", len(str(n)), "Count the digits.", offs=(1, -1, 2, 3)) for n in [3450000, 12500000, 99999, 100000]]
eA8 = [tm(f"The successor of {ind(n)} is:", ind(n + 1), [ind(n - 1), ind(n + 10), ind(n * 10)], "Add 1.") for n in [99999, 999999, 9999999, 49999]]
EASY_A = [eA1, eA2, eA3, eA4, eA5, eA6, eA7, eA8]
EASY_B = ([QQ(f"Write {ind(n)} in words (Indian system).", "Read period by period", words(n)) for n in [345600, 2090000, 7050300, 12000045]]
          + [QQ(f"Write '{words(n)}' in figures using commas.", "Place the periods", ind(n)) for n in [630500, 4008090, 25000300, 9040009]]
          + [QQ(f"Find {ind(a)} + {ind(b)}.", "Add column by column", f"${ind(a+b)}$") for a, b in [(234500, 187600), (1250300, 849700), (5000000, 2345678), (987654, 123456)]])
EASY_C = ([QQ(f"Write {ind(n)} in the international system (commas after every three digits) and in expanded form.", f"International: {intl(n)}", "Expanded: " + " + ".join(f"{int(c)*10**(len(str(n))-i-1)}" for i, c in enumerate(str(n)) if c != "0")) for n in [345678, 2060450, 7005300, 12040000, 800250, 3090900]]
          + [QQ(f"Find {ind(a)} - {ind(b)} and round the answer to the nearest lakh.", f"Difference $={ind(a-b)}$", f"Nearest lakh: ${ind(rnd(a-b,100000))}$") for a, b in [(5400000, 2345000), (9800000, 4567000), (3250000, 1180000), (7600000, 3290000), (6100000, 2450000), (8200000, 1670000)]]
          + [QQ(f"A town has {ind(n)} people. Write the number of people in words and round it to the nearest ten thousand.", f"Words: {words(n)}", f"Nearest ten thousand: ${ind(rnd(n,10000))}$") for n in [234567, 456789, 1234567, 875432, 3456780, 5600890]])
EASY_D = ([QQ(f"A school collected ₹{ind(a)} in the first month and ₹{ind(b)} in the second month. Find the total, and the difference in the collection of the two months. Write the total in words.", f"Total $={ind(a)}+{ind(b)}={ind(a+b)}$", f"Difference $={ind(abs(a-b))}$", f"Total in words: {words(a+b)}", "State units (rupees)") for a, b in [(1250000, 980000), (2340000, 1760000), (875000, 1245000), (3050000, 2475000), (1560000, 1890000), (4200000, 3125000)]]
          + [QQ(f"A factory makes {ind(a)} bottles each month. Find the number made in {m} months and write the answer in words.", f"${ind(a)}\\times{m}={ind(a*m)}$", f"In words: {words(a*m)}") for a, m in [(25000, 12), (150000, 8), (320000, 6), (45000, 15), (75000, 24), (125000, 10)]])

# ---------- NCERT ----------
nA1 = [nm(f"How many lakhs make {n} crore?", n * 100, "1 crore = 100 lakh.", offs=(10, -10, 1000, 1)) for n in [3, 7, 12, 25]]
nA2 = [nm(f"{ind(n)} written in the international system has how many commas?", len(intl(n).split(",")) - 1, "Group digits in threes.", offs=(1, -1, 2)) for n in [12500000, 345678, 5000000, 1234567890]]
nA3 = [tm(f"{ind(n)} in the international system is:", intl(n), [ind(n), intl(n * 10), intl(n // 10)], "Regroup the digits in threes.") for n in [4560000, 12345678, 90250000, 7050300]]
nA4 = [tm(f"The place value of the digit {d} in {ind(n)} (the leftmost {d}) is:", ind(d * 10 ** (len(str(n)) - str(n).index(str(d)) - 1)), [ind(d * 10 ** (len(str(n)) - str(n).index(str(d)) - 1) * 10), ind(d * 10 ** (len(str(n)) - str(n).index(str(d)) - 1) // 10), str(d)], "Digit times its place value.") for n, d in [(3456789, 4), (50820000, 8), (7345600, 3), (91200500, 9)]]
nA5 = [nm(f"The number of zeros in {ind(10**k)} is:", k, "Count the zeros.", offs=(1, -1, 2, 3)) for k in [5, 6, 7, 8]]
nA6 = [tm(f"The largest {k}-digit number is:", ind(10 ** k - 1), [ind(10 ** k), ind(10 ** (k - 1)), ind(10 ** k - 10)], "All digits are 9.") for k in [5, 6, 7, 8]]
nA7 = [tm(f"1,00,00,000 - {ind(n)} =", ind(10 ** 7 - n), [ind(10 ** 7 - n + 1000), ind(10 ** 7 - n - 1000), ind(10 ** 7 + n)], "Subtract.") for n in [2345678, 4500000, 987654, 6090909]]
nA8 = [nm(f"How many thousands make {n} lakh?", n * 100, "1 lakh = 100 thousand.", offs=(10, -10, 1000, 1)) for n in [4, 9, 15]]
NCERT_A = [nA1, nA2, nA3, nA4, nA5, nA6, nA7, nA8]
NCERT_B = ([QQ(f"Convert {ind(n)} from the Indian to the international system.", "Regroup in threes", intl(n)) for n in [2345678, 15000000, 9876543, 40505050]]
           + [QQ(f"What number is {ind(a)} + 1? What is the successor of the largest {k}-digit number?", f"Successor of {ind(a)} is {ind(a+1)}", f"Successor of {ind(10**k-1)} is {ind(10**k)}") for a, k in [(99999, 5), (999999, 6), (9999999, 7), (4999999, 5)]]
           + [QQ(f"Estimate {ind(a)} + {ind(b)} by rounding each to the nearest lakh.", f"{ind(a)} rounds to {ind(rnd(a,100000))}; {ind(b)} rounds to {ind(rnd(b,100000))}", f"Estimate $={ind(rnd(a,100000)+rnd(b,100000))}$") for a, b in [(3456789, 1234567), (4876543, 2345678), (5123456, 3987654), (6543210, 1456789)]])
NCERT_C = ([QQ(f"Write {ind(n)} in expanded form using powers of 10 and say how many lakhs it is (approx. to one decimal place).", "Break the number by place value", "$" + " + ".join(f"{c}\\times10^{{{len(str(n))-i-1}}}" for i, c in enumerate(str(n)) if c != "0") + "$", f"In lakhs: ${n/100000:.1f}$ lakh") for n in [3456789, 5025000, 7300450, 2900300, 8105060, 6040200]]
           + [QQ(f"A bus travels {ind(a)} km every year. How many kilometres does it travel in {y} years? Write in words and in the international system.", f"${ind(a)}\\times{y}={ind(a*y)}$", f"Words: {words(a*y)}", f"International: {intl(a*y)}") for a, y in [(125000, 8), (86000, 15), (250000, 12), (95000, 20), (140000, 9), (72000, 25)]]
           + [QQ(f"A population grows from {ind(a)} to {ind(b)}. Find the increase, and estimate it to the nearest ten thousand.", f"Increase $={ind(b)}-{ind(a)}={ind(b-a)}$", f"Estimate: ${ind(rnd(b-a,10000))}$", "State the answer in words: " + words(b - a)) for a, b in [(2345678, 2567890), (4500000, 4789432), (1234567, 1456321), (3200000, 3451789), (5600000, 5934567), (7200000, 7512340)]])
NCERT_D = ([QQ(f"A government school uses {ind(a)} litres of water per day. Find the water used in a year of 365 days, round it to the nearest lakh and write the rounded value in words.", f"Annual use $={ind(a)}\\times365={ind(a*365)}$ litres", f"Nearest lakh: ${ind(rnd(a*365,100000))}$", f"In words: {words(rnd(a*365,100000))}", "Check by estimation: 365 is about 400") for a in [1250, 2400, 3150, 4800, 5250, 7600]]
           + [QQ(f"The population of a state is {ind(p)}. A survey covers {k} of every 100 persons. Find the number of people surveyed.", f"People surveyed $=\\frac{{{k}}}{{100}}\\times{ind(p)}$", f"$={ind(p*k//100)}$", f"In words: {words(p*k//100)}") for p, k in [(25000000, 4), (12000000, 5), (48000000, 3), (36000000, 2), (64000000, 5), (80000000, 4)]])

# ---------- MEDIUM ----------
mA1 = [tm(f"{ind(a)} × {m} =", ind(a * m), [ind(a * m + 1000), ind(a * m * 10), ind(a * m - 10000)], "Multiply and place commas.") for a, m in [(125000, 8), (230000, 15), (45600, 25), (78000, 40)]]
mA2 = [nm(f"{ind(a*m)} ÷ {m} =", a, "Divide.", offs=(100, -100, 1000, 10)) for a, m in [(1250000, 25), (4800000, 16), (7200000, 12), (3600000, 45)]]
mA3 = [nm(f"A crore is how many times {ind(n)}?", 10 ** 7 // n, "Divide $10^7$.", offs=(1, -1, 10, 100)) for n in [1000, 100000, 10000, 500000, 2000000]]
mA4 = [tm(f"The sum of the largest 6-digit number and the smallest 7-digit number is:", ind(999999 + 1000000), [ind(2000000), ind(1999998), ind(2000001)], "999999 + 1000000.") ] + [tm(f"The difference between the smallest {k}-digit number and the largest {k-1}-digit number is:", "1", ["10", "100", "0"], "Consecutive numbers.") for k in [5, 6]] + [tm(f"The product of {ind(a)} and 100 is:", ind(a * 100), [ind(a * 10), ind(a * 1000), ind(a * 100 + 100)], "Append two zeros.") for a in [345, 1250, 87000]]
mA5 = [nm(f"Estimate {ind(a)} × {b} by rounding {ind(a)} to the nearest lakh and {b} as given:", rnd(a, 100000) * b, "Round first.", offs=(100000, -100000, 10000, b)) for a, b in [(345678, 6), (498765, 4), (1234567, 3), (2456789, 5)]]
mA6 = [nm(f"How many seconds are there in {h} hours?", h * 3600, "1 hour = 3600 seconds.", offs=(60, -60, 3600, 100)) for h in [24, 48, 72, 12, 36]]
mA7 = [nm(f"The number of days in {y} years (non-leap years of 365 days) is:", y * 365, "Multiply.", offs=(365, -365, 100, 10)) for y in [10, 25, 40, 100]]
MED_A = [mA1, mA2, mA3, mA4, mA5, mA6, mA7]
MED_B = ([QQ(f"Find {ind(a)} × {m}.", "Multiply and add commas", f"${ind(a*m)}$") for a, m in [(234000, 15), (56700, 40), (125000, 36), (98000, 75)]]
          + [QQ(f"Find {ind(a*m)} ÷ {m}.", "Divide step by step", f"${ind(a)}$") for a, m in [(3600000, 24), (7500000, 125), (2880000, 48), (9000000, 45)]]
          + [QQ(f"Find the number of minutes in {d} days. Write it in the Indian system.", f"1 day = 24 × 60 = 1440 minutes", f"${d}\\times1440={ind(d*1440)}$") for d in [30, 100, 365, 500]])
MED_C = ([QQ(f"A train covers {ind(d)} km in a year. How many kilometres will it cover in {y} years and how many such trains are needed to cover {ind(d*y*t)} km in {y} years?", f"In {y} years: ${ind(d)}\\times{y}={ind(d*y)}$ km", f"Trains needed $={ind(d*y*t)}\\div{ind(d*y)}={t}$") for d, y, t in [(125000, 8, 6), (84000, 12, 5), (250000, 5, 8), (96000, 15, 4), (175000, 6, 9), (68000, 20, 7)]]
          + [QQ(f"Round {ind(n)} to the nearest (i) thousand (ii) lakh and find the difference between the two rounded numbers.", f"(i) ${ind(rnd(n,1000))}$", f"(ii) ${ind(rnd(n,100000))}$", f"Difference $={ind(abs(rnd(n,1000)-rnd(n,100000)))}$") for n in [3456789, 5678123, 7234567, 9876543, 2345678, 4690321]]
          + [QQ(f"Find {ind(a)} + {ind(b)} - {ind(c)}. Estimate the answer by rounding each number to the nearest lakh and compare it with the exact answer.", f"Exact $={ind(a+b-c)}$", f"Estimate $={ind(rnd(a,100000)+rnd(b,100000)-rnd(c,100000))}$", "The estimate is close to the exact answer") for a, b, c in [(3456789, 2345678, 1234567), (5123456, 4876543, 2345678), (7654321, 1234567, 3456789), (2468013, 5791357, 1357913), (6543219, 3210987, 2109876), (4321098, 6789012, 3987654)]])
MED_D = ([QQ(f"A company earned ₹{ind(a)} in the first year, and in each next year the earning increased by ₹{ind(d)}. Find its earnings in the 2nd, 3rd and 4th years and the total of the four years.", f"2nd year $={ind(a+d)}$", f"3rd year $={ind(a+2*d)}$", f"4th year $={ind(a+3*d)}$", f"Total $={ind(4*a+6*d)}$") for a, d in [(1250000, 150000), (2400000, 250000), (3500000, 125000), (1800000, 200000), (4200000, 300000), (2750000, 175000)]]
          + [QQ(f"The distance between two cities is {ind(d)} m. A runner covers {ind(r)} m each day. How many full days does he run, how much distance is left after that, and how many days in all are needed to finish?", f"Full days: ${ind(d)}\\div{ind(r)}$ gives {d//r} full days", f"Remaining $={ind(d-r*(d//r))}$ m", "Total days to finish: " + str(d // r + (1 if d % r else 0))) for d, r in [(1250000, 40000), (2450000, 65000), (3600000, 85000), (1800000, 55000), (5200000, 125000), (3150000, 90000)]])

# ---------- HARD ----------
hA1 = [tm(f"The number of seconds in {d} days is:", ind(86400 * d), [ind(86400 * d + 1000), ind(86400 * d - 3600), ind(8640 * d)], "1 day = 86,400 seconds.") for d in [7, 30, 100, 365]]
hA2 = [nm(f"The number of zeros in {ind(a)} × {ind(b)} is:", len(str(a * b)) - len(str(a * b).rstrip("0")), "Count zeros in the product.", offs=(1, -1, 2, 3)) for a, b in [(25000, 400), (125000, 80), (4500, 2000), (3500, 600)]]
hA3 = [tm(f"1 crore = {ind(10**7)}; the number of crores in {ind(n)} is:", f"{n/10**7:g}", [f"{n/10**7*10:g}", f"{n/10**7/10:g}", f"{n/10**5:g}"], "Divide by 1,00,00,000.") for n in [250000000, 45000000, 8000000, 120000000]]
hA4 = [nm(f"A tank holds {ind(a)} litres. How many such tanks hold {ind(a*k)} litres?", k, "Divide.", offs=(1, -1, 10, 100)) for a, k in [(125000, 48), (350000, 36), (2500000, 12), (75000, 120)]]
hA5 = [tm(f"The smallest number that must be added to {ind(n)} to get the next lakh is:", ind(-n % 100000), [ind(-n % 100000 + 1000), ind(-n % 100000 - 100), ind(100000 - 1)], "Round up to the next lakh.") for n in [3456789, 7234560, 1250001, 9876543]]
hA6 = [nm(f"If 1 lakh = {ind(10**5)}, how many lakhs are there in {ind(n)}?", n // 100000, "Divide by a lakh.", offs=(1, -1, 10, 100)) for n in [12500000, 34000000, 7500000, 280000000]]
hA7 = [nm(f"The number of digits in the product {ind(a)} × {ind(b)} is:", len(str(a * b)), "Multiply and count.", offs=(1, -1, 2, 3)) for a, b in [(125000, 8000), (99999, 9999), (450000, 2500), (1000000, 100000)]]
hA8 = [nm(f"How many lakhs are there in {n} crore?", n * 100, "1 crore = 100 lakh.", offs=(10, -10, 1000, 1)) for n in [18, 35, 64]]
HARD_A = [hA1, hA2, hA3, hA4, hA5, hA6, hA7, hA8]
HARD_B = ([QQ(f"How many seconds are there in {d} days? Write it in the Indian and the international system.", f"1 day = 86,400 seconds", f"${d}\\times86400={ind(d*86400)}$; international: {intl(d*86400)}") for d in [7, 30, 100, 365]]
          + [QQ(f"Which is greater: {ind(a)} or {ind(b)}? By how much?", "Compare digit counts and then place values", f"Greater: {ind(max(a,b))}; difference ${ind(abs(a-b))}$") for a, b in [(9876543, 9867543), (12345678, 12354678), (45600789, 45600798), (7000999, 7001000)]]
          + [QQ(f"A number is 1 lakh more than {ind(n)}. Write the number and the number which is 1 crore less than it (if possible).", f"1 lakh more $={ind(n+100000)}$", "1 crore less: " + (f"${ind(n+100000-10**7)}$" if n+100000>=10**7 else "not possible (the result would be negative)")) for n in [12345678, 34567890, 5678901, 29876543]])
HARD_C = ([QQ(f"A bank gives ₹{ind(a)} loan to each of {k} persons. Find the total, write it in words and round it to the nearest crore.", f"Total $={ind(a)}\\times{k}={ind(a*k)}$", f"Words: {words(a*k)}", f"Nearest crore: ${ind(rnd(a*k,10**7))}$") for a, k in [(250000, 48), (125000, 96), (375000, 64), (500000, 72), (180000, 125), (450000, 88)]]
          + [QQ(f"Arrange {ind(a)}, {ind(b)}, {ind(c)} in descending order and find the difference between the largest and the smallest.", "Compare numbers digit by digit", f"Descending: {', '.join(ind(x) for x in sorted([a,b,c], reverse=True))}", f"Difference $={ind(max(a,b,c)-min(a,b,c))}$") for a, b, c in [(1234567, 1243567, 1234765), (9087654, 9078654, 9807654), (5000999, 5001000, 4999999), (3141592, 3141952, 3114592), (8765432, 8675432, 8765342), (2718281, 2781281, 2718821)]]
          + [QQ(f"The speed of light is about {ind(300000)} km per second. How far does it travel in {t} seconds? Write the answer in words.", f"Distance $=300000\\times{t}={ind(300000*t)}$ km", f"In words: {words(300000*t)}") for t in [8, 60, 120, 500, 1000, 3600]])
HARD_D = ([QQ(f"A city has {ind(a)} houses. Each house uses {u} units of electricity per month. Find the units used by the city in one month and in a year (12 months). Write the yearly figure in words and round it to the nearest crore.", f"Monthly $={ind(a)}\\times{u}={ind(a*u)}$", f"Yearly $={ind(a*u*12)}$", f"Words: {words(a*u*12)}", f"Nearest crore: ${ind(rnd(a*u*12,10**7))}$", "Show working with place values") for a, u in [(250000, 180), (420000, 150), (350000, 220), (560000, 125), (180000, 240), (640000, 175)]]
          + [QQ(f"Two numbers add up to {ind(s)} and differ by {ind(d)}. Find the numbers, and write both in words.", f"Larger $=({ind(s)}+{ind(d)})\\div2={ind((s+d)//2)}$", f"Smaller $={ind((s-d)//2)}$", f"Words: {words((s+d)//2)}; {words((s-d)//2)}", "Check: sum and difference match") for s, d in [(12500000, 1500000), (9800000, 2400000), (15000000, 3500000), (8600000, 1200000), (20000000, 5000000), (7400000, 900000)]])

TIERS = T4((NCERT_A, NCERT_B, NCERT_C, NCERT_D), (EASY_A, EASY_B, EASY_C, EASY_D), (MED_A, MED_B, MED_C, MED_D), (HARD_A, HARD_B, HARD_C, HARD_D))
