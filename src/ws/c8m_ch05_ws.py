"""Class 8 Maths Ch 5 - Number Play: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch05"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

def kap(n, w):
    s = str(n).zfill(w); return int("".join(sorted(s, reverse=True))) - int("".join(sorted(s)))
assert [kap(1234, 4), kap(3087, 4), kap(8352, 4)] == [3087, 8352, 6174]
assert [kap(352, 3), kap(297, 3), kap(693, 3), kap(594, 3)] == [297, 693, 594, 495]
assert 5481 % 9 == 0 and 4572 % 6 == 0 and 8316 % 9 == 0 and 7392 % 8 == 0 and 3652 % 11 == 0 and 252 % 9 == 0
assert [x for x in range(70000, 80000) if str(x)[2:4] == "36" and x % 4 == 0 and x % 9 == 0] == [72360, 73368, 77364]
assert [x for x in range(4000, 5000) if str(x)[2] == "5" and x % 45 == 0] == [4050, 4455, 4950]
assert [x for x in range(400, 500) if x % 8 == 7 and x % 12 == 7 and x % 15 == 7] == [487] and 99960 % 60 == 0 and 99999 // 60 * 60 == 99960
assert 1013 % 24 == 5 and 984 + 24 == 1008 and 74 - 47 == 27 and 47 + 74 == 121 and 3443 % 11 == 0
assert [n for n in range(10, 100) if n % 11 and int((n + int(str(n)[::-1])) ** .5) ** 2 == n + int(str(n)[::-1])] == [29, 38, 47, 56, 65, 74, 83, 92]

WS = [
# ---------------- EASY ----------------
W("Which of these numbers is divisible by 9?", 1, "(a) 5,481. Digit sum $5+4+8+1=18$, a multiple of 9. The others have digit sums 19, 20 and 21. (1)", "E", opts=["5,481", "5,482", "5,483", "5,484"]),
W("The LCM of 12 and 18 is:", 1, "(b) 36. $12=2^2\\times3$, $18=2\\times3^2$; LCM $=2^2\\times3^2=36$. (1)", "E", opts=["6", "36", "72", "216"]),
W("The sum of two odd numbers is always:", 1, "(b) even. For example $7+9=16$; in general $(2m+1)+(2n+1)=2(m+n+1)$. (1)", "E", opts=["odd", "even", "a prime number", "a multiple of 3"]),
W("Which of the following is a palindrome?", 1, "(b) 12,321. It reads the same from the left and from the right. (1)", "E", opts=["12,312", "12,321", "12,231", "21,312"]),
W("Which of these numbers is divisible by 6?", 1, "(a) 4,572. It is even and its digit sum $4+5+7+2=18$ is a multiple of 3, so it is divisible by 2 and 3. (1)", "E", opts=["4,572", "4,575", "4,574", "4,571"]),
W("A two-digit number has tens digit $a$ and ones digit $b$. The number is:", 1, "(b) $10a+b$. The tens digit is worth $10a$ and the ones digit $b$. (1)", "E", opts=["$a+b$", "$10a+b$", "$10b+a$", "$ab$"]),
W("Starting with any 4-digit number (not all digits equal) and repeating ‘largest arrangement minus smallest arrangement’, we reach the Kaprekar constant:", 1, "(b) 6,174. For example $7641-1467=6174$. (1)", "E", opts=["495", "6,174", "1,089", "9,999"]),
W("Without dividing, test whether 7,392 is divisible by 8.", 2, "A number is divisible by 8 if its last three digits are (1). $392=8\\times49$, so 7,392 **is** divisible by 8 (1).", "E"),
W("Find the digit that can replace $\\square$ so that $8\\square16$ is divisible by 9.", 2, "Digit sum $=8+\\square+1+6=15+\\square$ must be a multiple of 9 (1). So $\\square=3$ (and $8316=9\\times924$) (1).", "E"),
W("Ritu has 252 marbles. Can she share them equally among 9 friends with none left over? Give a reason.", 2, "Digit sum of 252 is $2+5+2=9$, a multiple of 9 (1). Yes; each friend gets $252\\div9=28$ marbles (1).", "E", wp=True),
W("Find the LCM of 6 and 8.", 1, "Multiples of 8: 8, 16, **24**; 24 is also a multiple of 6. LCM $=24$ (1).", "E"),
W("Two bells ring every 12 minutes and every 18 minutes. They ring together at 8:00 a.m. After how many minutes will they ring together again?", 2, "The time is the LCM of 12 and 18 (1) $=36$ minutes, i.e. at 8:36 a.m. (1).", "E", wp=True),
W("For the number 74 write it as $10a+b$, reverse it and find the difference between the larger and smaller numbers. Show that it is a multiple of 9.", 2, "$74=10\\times7+4$; reverse $=47$ (1). $74-47=27=9\\times3$ (1).", "E"),
W("True or false (give an example): a number is divisible by 4 if its last digit is even.", 1, "**False.** 14 ends in 4 (even) but is not divisible by 4; the last **two** digits must be divisible by 4 (1).", "E"),
W("Write the smallest and the greatest 4-digit palindromes.", 2, "Smallest: 1,001 (1). Greatest: 9,999 (1).", "E"),
W("Test whether 3,652 is divisible by 11.", 2, "(Sum of digits at odd places) − (sum at even places): from the right, $2+6=8$ and $5+3=8$ (1). The difference is 0, so it **is** divisible by 11 ($3652=11\\times332$) (1).", "E"),
W("A shop has 3,456 pens. Can they be packed with no pen left over in boxes of (i) 8 (ii) 9 (iii) 10 pens?", 2, "(i) last three digits $456=8\\times57$: yes. (ii) digit sum 18: yes. (iii) last digit 6, not 0: no (2).", "E", wp=True),
# ---------------- MEDIUM ----------------
W("Find the digit $\\square$ so that $3\\square52$ is divisible by 11.", 2, "From the right the odd-place digits are $2$ and $\\square$; even-place digits are $5$ and $3$. The difference $(2+\\square)-(5+3)$ must be 0 or $\\pm11$ (1). $\\square=6$, and $3652=11\\times332$ (1).", "M"),
W("Find the smallest number that is divisible by each of 15, 20 and 25.", 2, "$15=3\\times5$, $20=2^2\\times5$, $25=5^2$ (1). LCM $=2^2\\times3\\times5^2=300$ (1).", "M"),
W("Three traffic lights change colour every 40 s, 60 s and 90 s. They change together at 9:00:00 a.m. At what time will they next change together?", 3, "LCM of 40, 60, 90: $40=2^3\\times5$, $60=2^2\\times3\\times5$, $90=2\\times3^2\\times5$ (1). LCM $=2^3\\times3^2\\times5=360$ s (1). That is 6 minutes, so at **9:06:00 a.m.** (1).", "M", wp=True),
W("Find the smallest number greater than 3 that leaves remainder 3 when divided by 5, 6 and 8.", 3, "Number $-3$ is a common multiple of 5, 6, 8 (1). LCM $=120$ (1). Number $=120+3=123$ (1).", "M"),
W("Show that the sum of a two-digit number and its reverse is always a multiple of 11. Check with 47.", 3, "$(10a+b)+(10b+a)=11a+11b$ (1) $=11(a+b)$, a multiple of 11 (1). Check: $47+74=121=11\\times11$ (1).", "M"),
W("For any 3-digit number $abc$ with $a>c$, show that (number − reversed number) is a multiple of 99. Verify with 832.", 3, "$(100a+10b+c)-(100c+10b+a)=99a-99c=99(a-c)$ (2). $832-238=594=99\\times6$ (1).", "M"),
W("The sum of three consecutive numbers is 87. Find the numbers using $n$, $n+1$, $n+2$.", 2, "$3n+3=87$, so $n=28$ (1). The numbers are 28, 29, 30 (1).", "M", wp=True),
W("Without dividing fully, test 7,35,624 for divisibility by (i) 8 (ii) 11.", 3, "(i) last three digits $624=8\\times78$: **yes** (1). (ii) from the right: $4+6+3=13$ and $2+5+7=14$; the difference is $1$, not a multiple of 11: **no** (2).", "M"),
W("Which of 3,624; 5,126; 7,236 are divisible by 12? State the test used.", 3, "12 $=3\\times4$ with 3 and 4 co-prime: test both (1). 3,624: digit sum 15 and $24\\div4$ ✓ — yes. 5,126: last two digits 26 not divisible by 4 — no. 7,236: digit sum 18 and $36\\div4$ ✓ — yes (2).", "M"),
W("Sumit says 2,164 is divisible by 8 because it is divisible by 2 and 4. Is he right? Explain.", 2, "No (1). $164\\div8$ leaves remainder 4, so 2,164 is not divisible by 8. Divisible by 2 and 4 does not guarantee divisibility by 8; 2 and 4 are not co-prime (1).", "M"),
W("Apply this routine to 1,234 until you reach 6,174: arrange the digits to make the largest and the smallest number, then subtract. Write each step.", 3, "$4321-1234=3087$ (1); $8730-0378=8352$ (1); $8532-2358=6174$ (1).", "M"),
W("Explain why the sum of two consecutive whole numbers is always odd.", 2, "Let the numbers be $n$ and $n+1$ (1). Their sum $2n+1$ is one more than an even number, so it is odd (1).", "M"),
W("The odometer of a car shows the palindrome 15951 km. What is the next palindromic reading, and how many kilometres must the car travel to show it?", 2, "The next 5-digit palindrome is 16061 (1). Distance $=16061-15951=110$ km (1).", "M", wp=True),
W("Collatz rule: if a number is even, halve it; if it is odd, multiply by 3 and add 1. Write the sequence starting from 12 until you reach 1.", 3, "12 → 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1 (3).", "M"),
W("Find the greatest 4-digit number that is divisible by 6.", 2, "The number must be even and have digit sum a multiple of 3 (1). $9999$ is odd; $9998$ has digit sum 35; $9996$ has digit sum 33 and is even, so **9,996** ($=6\\times1666$) (1).", "M"),
W("The digits of a two-digit number add up to 11. If the digits are interchanged, the new number is 27 more than the original. Find the original number.", 3, "Let the number be $10a+b$ with $a+b=11$ (1). $(10b+a)-(10a+b)=9(b-a)=27$, so $b-a=3$ (1). $b=7$, $a=4$: the number is **47** (check: $74-47=27$) (1).", "M", wp=True),
W("A trader has 2,345 mangoes and wants to pack all of them in boxes of 9 with none left over. What is the smallest number of extra mangoes he must buy?", 2, "Digit sum $2+3+4+5=14$ (1). Next multiple of 9 is 18, so add $18-14=4$: $2349=9\\times261$ (1).", "M", wp=True),
W("Why is 2 the only even prime number?", 2, "A prime has exactly two factors, 1 and itself (1). Every even number greater than 2 has 2 as a third factor, so it is composite (1).", "M"),
W("Find the LCM of 24 and 36 using prime factorisation.", 2, "$24=2^3\\times3$ and $36=2^2\\times3^2$ (1). LCM $=2^3\\times3^2=72$ (1).", "M"),
# ---------------- HARD ----------------
W("Show that the sum of any four consecutive whole numbers is never divisible by 4.", 3, "Numbers: $n$, $n+1$, $n+2$, $n+3$. Sum $=4n+6$ (1). $4n$ is divisible by 4, so the remainder is that of 6, i.e. 2 (1). So the sum is never a multiple of 4 (1).", "H"),
W("Three temple bells ring every 15, 20 and 25 minutes. They ring together at 6:00 a.m. How many times in the next 10 hours (after 6:00 a.m.) will they ring together, and at what times?", 4, "LCM of 15, 20, 25 $=300$ minutes $=5$ hours (2). In the next 10 hours (600 minutes) they ring together at $300$ and $600$ minutes (1): at **11:00 a.m.** and **4:00 p.m.**, i.e. 2 times (1).", "H", wp=True),
W("Find the smallest 4-digit number that leaves remainder 5 when divided by 6, 8 and 12.", 4, "Number $-5$ is a multiple of LCM$(6,8,12)=24$ (1). The multiples of 24 near 1,000: $24\\times41=984$ (3-digit after adding 5: 989), $24\\times42=1008$ (1). Smallest number $=1008+5=$ **1,013** (2).", "H"),
W("Find the greatest 5-digit number that is divisible by 12, 15 and 20.", 3, "LCM$(12,15,20)=60$ (1). $99999\\div60$ gives quotient 1,666 and remainder 39 (1). Required number $=99999-39=$ **99,960** (1).", "H"),
W("Apply the routine ‘largest arrangement − smallest arrangement’ to the 3-digit number 352 until the answer stops changing.", 4, "$532-235=297$ (1); $972-279=693$ (1); $963-369=594$ (1); $954-459=495$ (1), and $954-459=495$ again, so the result stays at **495**.", "H"),
W("The 5-digit number $7a36b$ is divisible by both 4 and 9 ($a$, $b$ are digits). Find all possible numbers.", 5, "Divisible by 4: last two digits $6b$ divisible by 4, so $b=0,4$ or 8 (1). Divisible by 9: $7+a+3+6+b=16+a+b$ is a multiple of 9, so $a+b=2$ or 11 (1). $b=0\\Rightarrow a=2$: 72,360; $b=4\\Rightarrow a=7$: 77,364; $b=8\\Rightarrow a=3$: 73,368 (3).", "H"),
W("A 3-digit number $abc$ has $a+c=b$. Prove it is divisible by 11 and check with 462.", 4, "$abc=100a+10b+c$; with $b=a+c$: $100a+10a+10c+c=110a+11c$ (2) $=11(10a+c)$, divisible by 11 (1). Check: $4+2=6$ ✓, $462=11\\times42$ (1).", "H"),
W("Kabir adds a two-digit number to the number formed by reversing its digits and gets 143. Find all the numbers he could have started with.", 3, "$11(a+b)=143$, so $a+b=13$ (1). Digit pairs adding to 13: 49, 58, 67, 76, 85, 94 (2).", "H", wp=True),
W("The 4-digit number $4A5B$ is divisible by 45. Find all possible values of $A$ and $B$ and the numbers.", 3, "Divisible by 45 means by 5 and 9 (co-prime) (1). By 5: $B=0$ or 5. By 9: $4+A+5+B=9+A+B$ must be a multiple of 9: $B=0$: $A=0$ or 9; $B=5$: $A=4$ (1). Numbers: **4,050; 4,950; 4,455** (1).", "H"),
W("Prove that the product of two consecutive whole numbers is always even. Hence explain why $\\dfrac{n(n+1)}{2}$ is always a whole number.", 3, "Of two consecutive numbers one is even, so the product has a factor 2 and is even (2). Therefore $n(n+1)$ is divisible by 2 and $\\frac{n(n+1)}2$ is a whole number (1).", "H"),
W("The number of students in a school is between 400 and 500. When they stand in rows of 8, 12 or 15, 7 students are always left over. Find the number of students.", 4, "Number $-7$ is a common multiple of 8, 12, 15 (1). LCM $=120$ (1). Multiples of 120: 360, 480, 600; $480+7=487$ is the only number between 400 and 500 (1). Check: $487=8\\times60+7=12\\times40+7=15\\times32+7$ (1).", "H", wp=True),
W("**Case study.** Palindromes. (i) Show that every 4-digit palindrome $abba$ is divisible by 11. (ii) Verify for 3,443. (iii) How many 4-digit palindromes are there?", 4, "(i) $abba=1000a+100b+10b+a=1001a+110b=11(91a+10b)$ (2). (ii) $3443=11\\times313$ (1). (iii) $a$ can be 1–9 (9 choices) and $b$ 0–9 (10 choices): $9\\times10=90$ palindromes (1).", "H", wp=True),
W("Prem says: ‘The digit sum of 1,863 is 18, so it is divisible by 18.’ Is he right? What is the correct conclusion?", 3, "Digit sum 18 shows divisibility by 9 (1). 18 $=2\\times9$, so the number must also be even (1). 1,863 is odd, so it is divisible by 9 but **not** by 18 (1).", "H"),
W("Find all two-digit numbers (not palindromes) whose sum with their reversed number is a perfect square.", 4, "The sum is $11(a+b)$ (1). For a perfect square, $a+b$ must be a multiple of 11 giving $11\\times11=121$ (since $a+b\\le18$), so $a+b=11$ (2). The numbers are 29, 38, 47, 56, 65, 74, 83, 92 (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(5)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "5.5 Special Number Patterns"),
 ("ul", ["**Palindromes** read the same both ways (4,554; 12,321). Every 4-digit palindrome abba = 1001a + 110b = 11 (91a + 10b) is a multiple of **11**; there are 9 × 10 = **90** four-digit palindromes.", "**Kaprekar's constant 6174:** take any 4-digit number whose digits are not all equal, subtract its smallest arrangement from its largest arrangement, and repeat. Example: 1234 → 4321 − 1234 = 3087 → 8730 − 0378 = 8352 → 8532 − 2358 = **6174**, and 7641 − 1467 = 6174 stays fixed. For 3-digit numbers the constant is **495** (352 → 297 → 693 → 594 → 495).", "**Collatz sequence:** if the number is even halve it, if odd multiply by 3 and add 1. 12 → 6 → 3 → 10 → 5 → 16 → 8 → 4 → 2 → 1. Every number tried so far reaches 1 but nobody has proved it always happens.", "**Odd and even:** odd + odd = even; even + odd = odd; odd × odd = odd; any product with an even factor is even. The sum of two consecutive numbers n + (n + 1) = 2n + 1 is always **odd**; the sum of 4 consecutive numbers 4n + 6 is never a multiple of 4."]),
 ("h2", "5.6 Worked Examples"),
 ("h3", "Example 1 — Missing digits with more than one condition"),
 ("steps", [("7a36b divisible by 4 and 9", "By 4: the last two digits 6b must be divisible by 4, so b = 0, 4 or 8."), ("By 9", "Digit sum 16 + a + b must be a multiple of 9, so a + b = 2 or 11."), ("Combine", "b = 0, a = 2: 72,360; b = 4, a = 7: 77,364; b = 8, a = 3: 73,368.")]),
 ("h3", "Example 2 — LCM in a time problem"),
 ("steps", [("Lights change every 40 s, 60 s and 90 s, together at 9:00:00", "LCM(40, 60, 90): 40 = 2³ × 5, 60 = 2² × 3 × 5, 90 = 2 × 3² × 5."), ("Take the highest power of each prime", "2³ × 3² × 5 = 360 seconds."), ("Answer", "6 minutes later: **9:06:00 a.m.**")]),
 ("h3", "Example 3 — A number with the same remainder"),
 ("steps", [("Smallest 4-digit number leaving remainder 5 on division by 6, 8 and 12", "LCM(6, 8, 12) = 24; the number is 24k + 5."), ("Make it 4-digit", "24 × 41 = 984 gives 989 (3-digit); 24 × 42 = 1,008."), ("Answer", "1,008 + 5 = **1,013**.")]),
 ("h3", "Example 4 — Proving a trick with letters"),
 ("steps", [("A 3-digit number abc with b = a + c", "Number = 100a + 10b + c = 100a + 10(a + c) + c."), ("Simplify", "= 110a + 11c = 11(10a + c)."), ("Conclusion", "It is always divisible by **11** (e.g. 462 = 11 × 42). A single example would not prove this; the letters do.")]),
 ("h3", "Example 5 — Digits of a number from a condition"),
 ("steps", [("Digit sum 11 and reversal gives 27 more", "Let the number be 10a + b; a + b = 11."), ("Use the reversal", "(10b + a) − (10a + b) = 9(b − a) = 27, so b − a = 3."), ("Solve", "b = 7, a = 4: the number is **47**; 74 − 47 = 27.")]),
 ("h3", "Example 6 — Testing with co-prime factors"),
 ("steps", [("Is 7,236 divisible by 12?", "12 = 3 × 4 with 3 and 4 co-prime."), ("Test both", "Digit sum 18 (divisible by 3); last two digits 36 = 4 × 9 (divisible by 4)."), ("Answer", "Yes: 7,236 = 12 × 603.")]),
 ("h2", "5.7 Word Problems: How to Translate"),
 ("table", ["Words", "Mathematics", "Example"], [
  ["‘ring/blink/flash together again’", "LCM of the intervals", "12 and 18 min: together every 36 min"],
  ["‘divide equally with none left’", "divisibility test", "252 marbles among 9 friends: digit sum 9, yes"],
  ["‘leaves the same remainder r’", "N = LCM × k + r", "remainder 3 on 5, 6, 8: 120k + 3"],
  ["‘between 400 and 500’", "list the numbers of the form LCM × k + r in the range", "120k + 7: 487"],
  ["‘the number and its reverse’", "10a + b and 10b + a", "sum 11(a + b); difference 9(a − b)"],
  ["‘three consecutive numbers’", "n, n + 1, n + 2", "sum 3n + 3 = 87, n = 28"]]),
 ("h2", "5.8 Common Mistakes"),
 ("table", ["Wrong idea", "Why it is wrong", "Correct"], [
  ["Divisible by 2 and 4, therefore by 8", "2 and 4 are not co-prime; 4 already includes 2", "check the last three digits"],
  ["Digit sum 18, so divisible by 18", "digit sum tests only 3 and 9", "also need the number to be even"],
  ["Last digit even, so divisible by 4", "4 depends on the last two digits", "14 is not divisible by 4"],
  ["Divisible by 11 if the digit sum is a multiple of 11", "11 uses the **difference** of alternate digit sums", "3,652: (3 + 5) − (6 + 2) = 0"],
  ["One example proves a trick", "an example illustrates; letters prove for all", "write the number with a, b, c"]]),
 ]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["**Kaprekar's constants:** 6,174 for 4-digit and 495 for 3-digit numbers; **palindromic** 4-digit numbers are multiples of 11.", "**Time and remainder word problems** are LCM problems: ‘together again’ uses the LCM; ‘same remainder r’ uses LCM × k + r."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
