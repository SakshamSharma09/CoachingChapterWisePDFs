"""Class 10 Maths Ch 14 - Probability (graded banks). Classical probability of single events; dice, coins, bags, numbered tickets, words.
No deck-of-cards problems and no empirical probability (kept out of the assessed scope)."""
from c10m_x import *
from mg import isp

SLUG, NAME, CHNO = "Probability", "Probability", 14

def pf(x):
    x = F(x)
    if x.denominator == 1: return str(x.numerator)
    return f"$\\frac{{{x.numerator}}}{{{x.denominator}}}$"
def frac_t(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"\\frac{{{x.numerator}}}{{{x.denominator}}}"
def prob_wrongs(fav, N, extra=()):
    p = F(fav, N); out = []
    for w in list(extra) + [1 - p, F(fav + 1, N), F(max(fav - 1, 0), N), F(fav, N + 1), F(fav, max(N - fav, 1)), F(N - fav + 1, N)]:
        w = F(w)
        if 0 <= w <= 1 and w != p and w not in out: out.append(w)
    return out
import re as _re
def SP(stem0, ask, fav, N, parts, extra=()):
    parts = [_re.sub(r"(\\frac\{\d+\}\{\d+\})=\1", r"\1", p) for p in parts]
    return SCG(stem0, ask, [F(fav, N)], prob_wrongs(fav, N, extra), parts, pf)
def lst(xs, limit=14):
    xs = list(xs)
    return ", ".join(map(str, xs)) if len(xs) <= limit else f"{len(xs)} outcomes"

# ----- sample spaces -----
DIE = list(range(1, 7))
def two_dice(): return [(a, b) for a in DIE for b in DIE]
def coins(k): return ["".join(c) for c in __import__("itertools").product("HT", repeat=k)]
def isprime(n): return isp(n)
def isqr(n): return isqrt(n) ** 2 == n

def die_ev(name, pred):
    fav = [x for x in DIE if pred(x)]
    return SP("A die is thrown once.", f"probability of getting {name}", len(fav), 6, ["Total possible outcomes $=6$: 1, 2, 3, 4, 5, 6", f"Favourable outcomes: {lst(fav)}; number $={len(fav)}$", f"$P=\\frac{{{len(fav)}}}{{6}}={frac_t(F(len(fav),6))}$"])
def dice2_ev(name, pred, thrown="Two dice are thrown simultaneously."):
    sp = two_dice(); fav = [o for o in sp if pred(*o)]
    shown = ", ".join(f"({a},{b})" for a, b in fav) if len(fav) <= 12 else f"{len(fav)} pairs"
    return SP(thrown, f"probability that {name}", len(fav), 36, ["Total number of outcomes $=6\\times6=36$", f"Favourable outcomes: {shown}; number $={len(fav)}$", f"$P=\\frac{{{len(fav)}}}{{36}}={frac_t(F(len(fav),36))}$"])
def coin_ev(k, name, pred):
    sp = coins(k); fav = [o for o in sp if pred(o)]
    who = {1: "A coin is tossed once.", 2: "A coin is tossed two times.", 3: "A coin is tossed three times."}[k]
    return SP(who, f"probability of getting {name}", len(fav), len(sp), [f"Total outcomes $=2^{k}={len(sp)}$: {', '.join(sp)}", f"Favourable outcomes: {lst(fav)}; number $={len(fav)}$", f"$P=\\frac{{{len(fav)}}}{{{len(sp)}}}={frac_t(F(len(fav),len(sp)))}$"])
def ticket_ev(N, name, pred, what="cards"):
    fav = [x for x in range(1, N + 1) if pred(x)]
    return SP(f"{N} {what} numbered 1 to {N} are placed in a box, mixed well and one is drawn at random." if what != "tickets" else f"A box contains {N} tickets numbered 1 to {N}. One ticket is drawn at random.", f"probability that the number drawn is {name}", len(fav), N,
              [f"Total possible outcomes $={N}$", f"Favourable numbers: {lst(fav, 16)}; number $={len(fav)}$", f"$P=\\frac{{{len(fav)}}}{{{N}}}={frac_t(F(len(fav),N))}$"])
def bag_ev(cols, name, pick, bagword="bag"):
    N = sum(cols.values()); fav = sum(c for k, c in cols.items() if pick(k))
    desc = ", ".join(f"{c} {k}" for k, c in cols.items())
    return SP(f"A {bagword} contains {desc} balls. One ball is drawn at random.", f"probability that it is {name}", fav, N, [f"Total balls $={'+'.join(map(str, cols.values()))}={N}$", f"Favourable balls $={fav}$", f"$P=\\frac{{{fav}}}{{{N}}}={frac_t(F(fav,N))}$"])
def word_ev(word, name, pred):
    ls = list(word); fav = [c for c in ls if pred(c)]
    return SP(f"A letter is chosen at random from the word '{word}'.", f"probability that it is {name}", len(fav), len(ls), [f"Number of letters in the word $={len(ls)}$", f"Favourable letters: {', '.join(fav)}; number $={len(fav)}$", f"$P=\\frac{{{len(fav)}}}{{{len(ls)}}}={frac_t(F(len(fav),len(ls)))}$"])
def comp_ev(p):
    p = F(p)
    return SCG(f"The probability of an event $E$ is ${frac_t(p)}$.", "probability of the event 'not $E$'", [1 - p], [p, F(1, 2) - p if p < F(1, 2) else p - F(1, 2) + F(1, 5), 1 + p, p / 2], ["$P(E)+P(\\text{not }E)=1$", f"$P(\\text{{not }}E)=1-{frac_t(p)}$", f"$P(\\text{{not }}E)={frac_t(1-p)}$"], pf)
def lot_ev(prizes, blanks):
    return SP(f"In a lottery there are {prizes} prizes and {blanks} blanks. A ticket is drawn at random.", "probability of getting a prize", prizes, prizes + blanks, [f"Total tickets $={prizes}+{blanks}={prizes+blanks}$", f"Favourable tickets (prizes) $={prizes}$", f"$P=\\frac{{{prizes}}}{{{prizes+blanks}}}={frac_t(F(prizes,prizes+blanks))}$"])
def pens_ev(total, bad):
    return SP(f"A lot of {total} ball pens contains {bad} defective pens. One pen is drawn at random from the lot.", "probability that the pen is good (not defective)", total - bad, total, [f"Total pens $={total}$; good pens $={total}-{bad}={total-bad}$", "Favourable outcomes $=$ number of good pens", f"$P=\\frac{{{total-bad}}}{{{total}}}={frac_t(F(total-bad,total))}$"])
def class_ev(total, girls, who="boy"):
    fav = total - girls if who == "boy" else girls
    return SP(f"A class has {total} students, of whom {girls} are girls. A student is selected at random to be the monitor.", f"probability that a {who} is selected", fav, total, [f"Total students $={total}$; boys $={total}-{girls}={total-girls}$", f"Favourable outcomes $={fav}$", f"$P=\\frac{{{fav}}}{{{total}}}={frac_t(F(fav,total))}$"])
def add_red(r, b, x):
    p = F(r + x, r + b + x)
    return SP(f"A bag contains {r} red and {b} blue balls. {x} more red balls are put into the bag and a ball is drawn at random.", "probability that the ball drawn is red", r + x, r + b + x, [f"After adding, red balls $={r}+{x}={r+x}$ and total balls $={r+b+x}$", "Favourable outcomes $=$ number of red balls", f"$P=\\frac{{{r+x}}}{{{r+b+x}}}={frac_t(p)}$"])
def find_x_ratio(r, k):
    x = k * r
    return SCG(f"A bag contains {r} red balls and $x$ blue balls. The probability of drawing a blue ball is {k} times the probability of drawing a red ball.", "value of $x$", [x], [x + r, x - 1, k, r + k], [f"$P(\\text{{blue}})=\\frac{{x}}{{{r}+x}}$ and $P(\\text{{red}})=\\frac{{{r}}}{{{r}+x}}$", f"$\\frac{{x}}{{{r}+x}}={k}\\times\\frac{{{r}}}{{{r}+x}}$ gives $x={k}\\times{r}$", f"$x={x}$"], lambda v: str(v))
def find_x_prob(r, b, x):
    p = F(r + x, r + b + x)
    return SCG(f"A bag contains {r} red and {b} blue balls. When $x$ more red balls are added, the probability of drawing a red ball becomes ${frac_t(p)}$.", "value of $x$", [x], [x + 1, x * 2, x - 1, r + b], [f"$\\frac{{{r}+x}}{{{r+b}+x}}={frac_t(p)}$", f"Cross-multiplying: ${p.denominator}({r}+x)={p.numerator}({r+b}+x)$", f"$x={x}$"], lambda v: str(v))
def sample_dice_multi(conds):
    sp = two_dice(); favs = [[o for o in sp if p(*o)] for _, p in conds]
    ask = "probabilities of these events (in this order): " + ", ".join(f"({'i' * (i+1) if i < 3 else 'iv'}) {n}" for i, (n, _) in enumerate(conds)) 
    return SCG("Two dice are thrown together.", ask, [F(len(f), 36) for f in favs], [], ["Total outcomes $=36$", "Favourable outcomes: " + "; ".join(f"{len(f)}" for f in favs), "Probabilities: " + ", ".join(f"${frac_t(F(len(f),36))}$" for f in favs)], pf)
def sample_bag_multi(cols, conds):
    N = sum(cols.values()); favs = [sum(c for k, c in cols.items() if p(k)) for _, p in conds]
    desc = ", ".join(f"{c} {k}" for k, c in cols.items())
    ask = "probability that the ball is: " + ", ".join(f"({'i' * (i+1) if i < 3 else 'iv'}) {n}" for i, (n, _) in enumerate(conds)) + " (in this order)"
    return SCG(f"A bag contains {desc} balls. One ball is drawn at random.", ask, [F(f, N) for f in favs], [], [f"Total balls $={N}$", "Favourable balls: " + ", ".join(map(str, favs)), "Probabilities: " + ", ".join(f"${frac_t(F(f,N))}$" for f in favs)], pf)
def sample_ticket_multi(N, conds):
    favs = [[x for x in range(1, N + 1) if p(x)] for _, p in conds]
    ask = "probability that the number is: " + ", ".join(f"({'i' * (i+1) if i < 3 else 'iv'}) {n}" for i, (n, _) in enumerate(conds)) + " (in this order)"
    return SCG(f"A box contains {N} cards numbered 1 to {N}. One card is drawn at random.", ask, [F(len(f), N) for f in favs], [], [f"Total outcomes $={N}$", "Favourable counts: " + ", ".join(str(len(f)) for f in favs), "Probabilities: " + ", ".join(f"${frac_t(F(len(f),N))}$" for f in favs)], pf)

def PC(q, c, w, why): return M4(q, c, w, why)
CONCEPT = [PC("The probability of a sure event is:", "1", ["0", "$\\frac12$", "2"], "A sure event always happens"),
           PC("The probability of an impossible event is:", "0", ["1", "$\\frac12$", "$-1$"], "It never happens"),
           PC("Which of the following cannot be the probability of an event?", "$\\frac{7}{6}$", ["0.4", "$\\frac{3}{5}$", "0.99"], "Probability lies between 0 and 1"),
           PC("Which of the following cannot be the probability of an event?", "$-0.3$", ["0", "$\\frac{2}{9}$", "1"], "Probability is never negative"),
           PC("If $P(E)=0.35$, then $P(\\text{not }E)$ is:", "0.65", ["0.35", "0.45", "1.35"], "$1-0.35$"),
           PC("The sum of the probabilities of all the elementary outcomes of an experiment is:", "1", ["0", "100", "$\\frac12$"], "Total probability")]
DP = [("an even number", lambda x: x % 2 == 0), ("an odd number", lambda x: x % 2 == 1), ("a number less than 3", lambda x: x < 3), ("a number greater than 4", lambda x: x > 4),
      ("a prime number", isprime), ("a multiple of 3", lambda x: x % 3 == 0), ("a perfect square", isqr), ("a factor of 6", lambda x: 6 % x == 0),
      ("a number between 2 and 5", lambda x: 2 < x < 5), ("a number less than 7", lambda x: x < 7), ("a number greater than 6", lambda x: x > 6), ("a number not less than 5", lambda x: x >= 5),
      ("a composite number", lambda x: x > 1 and not isprime(x)), ("a number that is both prime and even", lambda x: isprime(x) and x % 2 == 0)]
D2 = [("the sum of the numbers is 8", lambda a, b: a + b == 8), ("the sum of the numbers is 7", lambda a, b: a + b == 7), ("both dice show the same number (a doublet)", lambda a, b: a == b),
      ("the product of the numbers is 12", lambda a, b: a * b == 12), ("the sum is at least 10", lambda a, b: a + b >= 10), ("the sum is less than 5", lambda a, b: a + b < 5),
      ("the numbers differ by 2", lambda a, b: abs(a - b) == 2), ("both numbers are odd", lambda a, b: a % 2 == 1 and b % 2 == 1), ("the sum is a prime number", lambda a, b: isprime(a + b)),
      ("the product is a perfect square", lambda a, b: isqr(a * b)), ("the sum is a multiple of 4", lambda a, b: (a + b) % 4 == 0), ("the first number is greater than the second", lambda a, b: a > b),
      ("the sum is 12", lambda a, b: a + b == 12), ("the sum is 5", lambda a, b: a + b == 5), ("the sum is 9", lambda a, b: a + b == 9), ("both numbers are even", lambda a, b: a % 2 == 0 and b % 2 == 0),
      ("at least one die shows 6", lambda a, b: a == 6 or b == 6), ("the sum is 3 or 11", lambda a, b: a + b in (3, 11)), ("neither die shows a 3", lambda a, b: a != 3 and b != 3), ("the product is 6", lambda a, b: a * b == 6),
      ("the sum is a multiple of 3", lambda a, b: (a + b) % 3 == 0), ("one number is exactly double the other", lambda a, b: a == 2 * b or b == 2 * a), ("the product is less than 8", lambda a, b: a * b < 8), ("the larger number is 4", lambda a, b: max(a, b) == 4)]
C2 = [("two heads", lambda s: s == "HH"), ("at least one head", lambda s: "H" in s), ("no head", lambda s: "H" not in s), ("exactly one tail", lambda s: s.count("T") == 1), ("at most one head", lambda s: s.count("H") <= 1)]
C3 = [("exactly two heads", lambda s: s.count("H") == 2), ("at least two heads", lambda s: s.count("H") >= 2), ("all three faces the same", lambda s: len(set(s)) == 1), ("at most one tail", lambda s: s.count("T") <= 1),
      ("exactly one head", lambda s: s.count("H") == 1), ("at least one tail", lambda s: "T" in s), ("a head on the first toss", lambda s: s[0] == "H"), ("heads on the first and last tosses", lambda s: s[0] == "H" and s[2] == "H"),
      ("at most two heads", lambda s: s.count("H") <= 2), ("the same face in the first two tosses", lambda s: s[0] == s[1])]
TK = [("a multiple of 3", lambda x: x % 3 == 0), ("a prime number", isprime), ("a perfect square", isqr), ("divisible by both 2 and 3", lambda x: x % 6 == 0), ("a two-digit number", lambda x: x >= 10),
      ("greater than 12", lambda x: x > 12), ("a multiple of 4", lambda x: x % 4 == 0), ("a multiple of 3 or 5", lambda x: x % 3 == 0 or x % 5 == 0), ("an even prime number", lambda x: x == 2),
      ("a number divisible by 5", lambda x: x % 5 == 0), ("not a multiple of 7", lambda x: x % 7 != 0), ("a number less than 10", lambda x: x < 10), ("a composite number", lambda x: x > 1 and not isprime(x)), ("a multiple of 2 but not of 4", lambda x: x % 2 == 0 and x % 4 != 0)]
VOW = lambda c: c in "AEIOU"

RED = lambda k: k == "red"; BLUE = lambda k: k == "blue"; GREEN = lambda k: k == "green"
def col(c): return lambda k: k == c
NOT = lambda f: (lambda k: not f(k))
OR2 = lambda a, b: (lambda k: k in (a, b))
THROWN_M = "A red die and a blue die are rolled together."
THROWN_H = "Two fair dice are thrown together and the numbers on the upper faces are noted."

# ================= EASY =================
eA = [[MC(die_ev(n, p)) for n, p in DP[:5]],
      [MC(die_ev(n, p)) for n, p in DP[5:10]],
      [MC(coin_ev(2, n, p)) for n, p in C2],
      [MC(bag_ev(c, nm, col(nm))) for c, nm in (({"red": 3, "blue": 5}, "red"), ({"red": 4, "green": 6}, "green"), ({"white": 2, "black": 8}, "white"), ({"red": 7, "blue": 3}, "blue"), ({"yellow": 5, "green": 5}, "yellow"))],
      [MC(ticket_ev(N, n, p)) for N, (n, p) in ((10, TK[0]), (12, TK[1]), (15, TK[3]), (20, TK[6]), (16, TK[2]))],
      [MC(comp_ev(p)) for p in (F(1, 4), F(3, 7), F(2, 9), F(5, 12), F(7, 20))],
      CONCEPT]
eB = ([SQ(die_ev(n, p), 2) for n, p in DP[10:14]] + [SQ(coin_ev(2, n, p), 2) for n, p in C2[:4]]
      + [SQ(bag_ev(c, nm, col(nm)), 2) for c, nm in (({"red": 5, "blue": 3}, "blue"), ({"red": 2, "green": 6}, "red"), ({"white": 4, "black": 6}, "black"), ({"yellow": 8, "green": 2}, "green"))])
eC = ([SQ(lot_ev(p, b), 3) for p, b in ((10, 25), (8, 32), (5, 45), (12, 28), (6, 14), (9, 21))] + [SQ(pens_ev(t, d), 3) for t, d in ((144, 20), (100, 12), (50, 5), (80, 16), (120, 18), (60, 9))]
      + [SQ(class_ev(t, g), 3) for t, g in ((40, 24), (30, 12), (50, 28), (36, 20), (45, 18), (25, 10))])
eD = ([SQ(sample_bag_multi(c, cd), 5) for c, cd in (({"red": 3, "blue": 4, "green": 3}, [("red", RED), ("not blue", NOT(BLUE)), ("yellow", col("yellow"))]),
                                                     ({"red": 5, "blue": 7, "green": 8}, [("green", GREEN), ("red or blue", OR2("red", "blue")), ("white", col("white"))]),
                                                     ({"red": 2, "blue": 3, "green": 5}, [("blue", BLUE), ("not red", NOT(RED)), ("green or red", OR2("green", "red"))]),
                                                     ({"red": 6, "blue": 4, "green": 10}, [("red", RED), ("not green", NOT(GREEN)), ("black", col("black"))]),
                                                     ({"red": 9, "blue": 6, "green": 5}, [("blue", BLUE), ("neither red nor blue", GREEN), ("red or green", OR2("red", "green"))]),
                                                     ({"red": 4, "blue": 8, "green": 8}, [("not red", NOT(RED)), ("blue", BLUE), ("red, blue or green", lambda k: True)]))]
      + [SQ(sample_ticket_multi(N, cd), 5) for N, cd in ((12, [TK[11], TK[1], ("a number greater than 12", lambda x: x > 12)]), (20, [TK[0], TK[1], TK[6]]), (15, [TK[3], TK[5], ("a number less than 16", lambda x: x < 16)]),
                                                         (18, [TK[9], TK[2], TK[11]]), (25, [TK[2], TK[9], ("a number greater than 25", lambda x: x > 25)]), (30, [TK[3], TK[9], TK[1]]))])

# ================= NCERT =================
nA = [[MC(dice2_ev(n, p)) for n, p in D2[:5]],
      [MC(coin_ev(3, n, p)) for n, p in C3[:5]],
      [MC(word_ev(w, n, p)) for w, n, p in (("MATHEMATICS", "a vowel", VOW), ("PROBABILITY", "the letter B", lambda c: c == "B"), ("EXAMINATION", "a consonant", lambda c: not VOW(c)), ("ASSASSINATION", "the letter S", lambda c: c == "S"), ("ELEVATION", "the letter E", lambda c: c == "E"))],
      [MC(add_red(r, b, x)) for r, b, x in ((4, 6, 2), (5, 5, 5), (3, 7, 7), (6, 4, 4), (2, 8, 3))],
      [MC(ticket_ev(N, n, p, "tickets")) for N, (n, p) in ((20, TK[0]), (25, TK[2]), (30, TK[1]), (24, TK[3]), (50, TK[9]))],
      [MC(pens_ev(t, d)) for t, d in ((135, 15), (90, 10), (75, 12), (200, 24), (160, 8))]]
nB = ([SQ(coin_ev(3, n, p), 2) for n, p in C3[5:9]] + [SQ(dice2_ev(n, p, THROWN_M), 2) for n, p in D2[5:9]]
      + [SQ(word_ev(w, n, p), 2) for w, n, p in (("EDUCATION", "a vowel", VOW), ("SUCCESS", "the letter S", lambda c: c == "S"), ("COMMITTEE", "the letter M", lambda c: c == "M"), ("TRIGONOMETRY", "a consonant", lambda c: not VOW(c)))])
nC = ([SQ(dice2_ev(n, p), 3) for n, p in D2[9:15]] + [SQ(ticket_ev(N, n, p, "tickets"), 3) for N, (n, p) in ((18, TK[0]), (28, TK[1]), (40, TK[6]), (60, TK[3]), (32, TK[2]), (35, TK[9]))]
      + [SQ(add_red(r, b, x), 3) for r, b, x in ((3, 9, 3), (7, 5, 5), (4, 8, 4), (8, 6, 2), (5, 10, 5), (9, 3, 6))])
nD = ([SQ(sample_dice_multi(cd), 5) for cd in ([D2[0], D2[2], D2[3]], [D2[1], D2[4], D2[5]], [D2[6], D2[7], D2[8]], [D2[9], D2[10], D2[11]], [D2[12], D2[13], D2[14]], [D2[15], D2[16], D2[17]])]
      + [SQ(find_x_prob(r, b, x), 5) for r, b, x in ((4, 8, 4), (5, 7, 3), (3, 9, 9), (6, 6, 6), (2, 10, 4), (7, 5, 9))])

# ================= MEDIUM =================
mA = [[MC(dice2_ev(n, p, THROWN_M)) for n, p in D2[10:15]],
      [MC(coin_ev(3, n, p)) for n, p in C3[5:10]],
      [MC(ticket_ev(N, n, p)) for N, (n, p) in ((30, TK[7]), (40, TK[12]), (50, TK[13]), (45, TK[10]), (60, TK[8]))],
      [MC(find_x_ratio(r, k)) for r, k in ((3, 2), (4, 3), (5, 2), (6, 4), (2, 5))],
      [MC(find_x_prob(r, b, x)) for r, b, x in ((3, 5, 2), (4, 6, 6), (5, 9, 7), (2, 6, 4), (6, 8, 6))],
      [MC(dice2_ev(n, p, THROWN_M)) for n, p in D2[15:20]],
      [MC(word_ev(w, n, p)) for w, n, p in (("PERMUTATION", "a vowel", VOW), ("PROBABILITY", "a vowel", VOW), ("CALCULATION", "the letter C", lambda c: c == "C"), ("TRIANGLE", "a consonant", lambda c: not VOW(c)), ("INTEGRATION", "the letter I", lambda c: c == "I"))]]
mB = ([SQ(dice2_ev(n, p, THROWN_M), 2) for n, p in D2[20:24]] + [SQ(ticket_ev(N, n, p), 2) for N, (n, p) in ((36, TK[3]), (42, TK[1]), (48, TK[2]), (22, TK[7]))]
      + [SQ(bag_ev(c, nm, f), 2) for c, nm, f in (({"red": 6, "blue": 4, "green": 5}, "not green", NOT(GREEN)), ({"red": 5, "blue": 9, "green": 6}, "red or blue", OR2("red", "blue")), ({"red": 8, "blue": 2, "green": 10}, "not blue", NOT(BLUE)), ({"red": 3, "blue": 7, "green": 5}, "neither blue nor green", RED))])
mC = ([SQ(find_x_ratio(r, k), 3) for r, k in ((7, 2), (8, 3), (9, 2), (10, 4), (5, 3), (12, 2))] + [SQ(find_x_prob(r, b, x), 3) for r, b, x in ((3, 6, 3), (5, 5, 5), (4, 12, 4), (7, 3, 10), (6, 10, 2), (8, 4, 4))]
      + [SQ(dice2_ev(n, p, THROWN_M), 3) for n, p in D2[:6]])
mD = ([SQ(sample_dice_multi(cd), 5) for cd in ([D2[3], D2[8], D2[20]], [D2[21], D2[22], D2[23]], [D2[0], D2[11], D2[16]], [D2[2], D2[17], D2[18]], [D2[1], D2[19], D2[13]], [D2[7], D2[9], D2[10]])]
      + [SQ(sample_ticket_multi(N, cd), 5) for N, cd in ((40, [TK[0], TK[1], TK[6]]), (50, [TK[2], TK[9], TK[8]]), (36, [TK[3], TK[7], TK[12]]), (60, [TK[6], TK[10], TK[5]]), (45, [TK[9], TK[1], TK[13]]), (30, [TK[7], TK[2], TK[11]]))])

# ================= HARD =================
hA = [[MC(dice2_ev(n, p, THROWN_H)) for n, p in D2[:5]],
      [MC(dice2_ev(n, p, THROWN_H)) for n, p in D2[5:10]],
      [MC(find_x_ratio(r, k)) for r, k in ((15, 3), (11, 4), (14, 5), (9, 7), (13, 2))],
      [MC(find_x_prob(r, b, x)) for r, b, x in ((7, 9, 5), (11, 9, 5), (5, 13, 7), (9, 15, 6), (8, 12, 12))],
      [MC(add_red(r, b, x)) for r, b, x in ((11, 5, 9), (13, 7, 7), (14, 6, 6), (17, 3, 13), (19, 5, 11))],
      [MC(ticket_ev(N, n, p, "tickets")) for N, (n, p) in ((70, TK[1]), (80, TK[7]), (75, TK[12]), (90, TK[13]), (100, TK[2]))],
      [MC(pens_ev(t, d)) for t, d in ((250, 35), (180, 27), (320, 48), (400, 52), (360, 45))]]
hB = ([SQ(dice2_ev(n, p, THROWN_H), 2) for n, p in D2[10:14]] + [SQ(find_x_ratio(r, k), 2) for r, k in ((18, 3), (16, 5), (20, 2), (12, 7))] + [SQ(add_red(r, b, x), 2) for r, b, x in ((15, 9, 6), (12, 8, 8), (21, 9, 9), (10, 14, 6))])
hC = ([SQ(dice2_ev(n, p, THROWN_H), 3) for n, p in D2[14:20]] + [SQ(find_x_prob(r, b, x), 3) for r, b, x in ((9, 7, 5), (13, 11, 3), (17, 9, 7), (6, 14, 10), (10, 14, 8), (15, 5, 15))]
      + [SQ(ticket_ev(N, n, p, "tickets"), 3) for N, (n, p) in ((84, TK[8]), (66, TK[12]), (96, TK[7]), (72, TK[13]), (54, TK[10]), (90, TK[1]))])
hD = ([SQ(sample_dice_multi(cd), 5) for cd in ([D2[3], D2[9], D2[11]], [D2[6], D2[15], D2[22]], [D2[8], D2[18], D2[20]], [D2[4], D2[14], D2[23]], [D2[5], D2[12], D2[21]], [D2[16], D2[17], D2[19]])]
      + [SQ(find_x_prob(r, b, x), 5) for r, b, x in ((12, 8, 4), (9, 21, 15), (13, 7, 17), (11, 25, 5), (16, 14, 14), (19, 1, 21))])

TIERS = {"NCERT": T(nA, nB, nC, nD), "Easy": T(eA, eB, eC, eD), "Medium": T(mA, mB, mC, mD), "Hard": T(hA, hB, hC, hD)}
