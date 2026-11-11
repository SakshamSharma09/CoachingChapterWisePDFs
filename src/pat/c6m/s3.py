from h6 import *
# ---------- Set 3 : emphasis Data Handling, Fractions, Integers, Prime Time, Number Play ----------
cls_trees = [("VI-A", 20), ("VI-B", 35), ("VI-C", 25), ("VI-D", 40), ("VI-E", 30)]
tot = sum(v for _, v in cls_trees)
q1 = mcqgroup([
 mm("In the sequence 1, 2, 4, 8, 16, ... (each term is double the previous one), the 9th term is:", 2 ** 8, [128, 512, 144], "The nth term is 2^(n−1): 2⁸ = 256."),
 m("At 6 o'clock the hour hand and the minute hand of a clock form:", "a straight angle", ["a right angle", "an obtuse angle", "a reflex angle"], "6 × 30° = 180°, a straight angle."),
 mm("The number of terms (including 3 itself and 1) in the Collatz sequence that starts with 3 is:", len(collatz(3)), [6, 7, 10], "3, 10, 5, 16, 8, 4, 2, 1 → 8 terms."),
 mm("A tally chart shows 4 bundles of five and 3 single strokes. The number represented is:", 23, [43, 20, 19], "4 × 5 + 3 = 23."),
 mm("The bar graph shows trees planted by five classes. The total number of trees planted is:", tot, [tot - 30, tot + 10, 130], "20 + 35 + 25 + 40 + 30 = 150.", fig=G.bar(cls_trees, 40, 10, 'Trees', 'Class')),
 mm("The HCF of 24 and 36 is:", gcd(24, 36), [6, 24, 72], "24 = 2³ × 3, 36 = 2² × 3²; HCF = 2² × 3 = 12."),
 m("Which of the following numbers is divisible by 12?", "132", ["124", "138", "150"], "132 is divisible by 4 (last two digits 32) and by 3 (1+3+2 = 6)."),
 m("Which fraction is equivalent to 18/24?", imp(Fr(3, 4)), [imp(Fr(2, 3)), imp(Fr(5, 6)), imp(Fr(6, 7))], "Divide both by 6: 3/4."),
 m("The value of 3/4 − 2/5 is:", imp(Fr(3, 4) - Fr(2, 5)), [imp(Fr(1, 1) / 10), imp(Fr(1, 9)), imp(Fr(5, 20))], "15/20 − 8/20 = 7/20."),
 mm("The perimeter of an equilateral triangle of side 9 cm is:", "27 cm", ["18 cm", "81 cm", "36 cm"], "3 × 9 = 27 cm."),
 m("Which of the following integers is the greatest?", "−3", ["−15", "−9", "−21"], "Among negative numbers, the one closest to zero is the greatest."),
 mm("The number of lines of symmetry of a square is:", 4, [2, 1, 8], "Two diagonals, two lines through mid-points of opposite sides."),
])
rawcol = ["Red", "Blue", "Green", "Blue", "Red", "Blue", "Yellow", "Green", "Blue", "Red", "Blue", "Green", "Red", "Blue", "Yellow"]
from collections import Counter
cc = Counter(rawcol)
b = [
 sa("Write tally marks for (i) 13 (ii) 22. (Use bundles of five.)", 2, "(i) 2 bundles of five and 3 strokes (1 mark)<br>(ii) 4 bundles of five and 2 strokes (1 mark)"),
 sa("Subtract: " + fr(Fr(13, 3)) + " − " + fr(Fr(11, 6)) + ".", 2, f"26/6 − 11/6 (1 mark) = 15/6 = {fr(Fr(13,3)-Fr(11,6))} (1 mark)"),
 sa("Find: (i) (−12) + 7 (ii) 9 + (−15).", 2, f"(i) {-12+7} (1 mark) (ii) {9-15} (1 mark)"),
 OR(sa("Write 84 as a product of prime factors.", 2, f"84 = {pfs(84)} (2 marks)"),
    sa("Write 90 as a product of prime factors.", 2, f"90 = {pfs(90)} (2 marks)")),
 sa("Write the next three terms of 2, 6, 18, 54, ... and state the rule.", 2, "162, 486, 1458 (1 mark); rule: multiply the previous term by 3 (1 mark)"),
 sa("Measure the angle in the figure and write its type.", 2, "125° (1 mark; ±2° accepted); obtuse angle (1 mark)", fig=G.angle(125)),
]
rho, seq = 57, []
n = 57
steps = []
while str(n) != str(n)[::-1]:
    r = int(str(n)[::-1]); steps.append(f"{n} + {r} = {n + r}"); n += r
c = [
 sa("Meena asked 15 classmates their favourite colour: " + ", ".join(rawcol) + ". Make a frequency table and tell which colour is the most popular.", 3,
    "Frequency: " + ", ".join(f"{k} {v}" for k, v in sorted(cc.items())) + " (2 marks); most popular colour: Blue (1 mark)"),
 OR(sa("Ramu has " + fr(Fr(5, 2)) + " m of cloth. He uses 3/4 m for each of 3 cushion covers. How much cloth is left?", 3, f"Used = 3 × 3/4 = {fr(Fr(9,4))} m (2 marks); left = 5/2 − 9/4 = {imp(Fr(5,2)-Fr(9,4))} m (1 mark)"),
    sa("Maya reads 1/5 of a book on Monday and 3/10 on Tuesday. (i) What fraction has she read? (ii) How many pages remain if the book has 200 pages?", 3, f"(i) 2/10 + 3/10 = {imp(Fr(1,5)+Fr(3,10))} = 1/2 (1 mark)<br>(ii) Remaining = 1/2 of 200 = 100 pages (2 marks)")),
 sa("Take 57. Reverse its digits and add. Keep repeating with each new sum until you get a palindrome. Show every step.", 3, "<br>".join(steps) + f"<br>A palindrome ({n}) is reached in {len(steps)} steps (1 mark per correct step, 1 mark for stating the palindrome)"),
]
fl = 40 * 25
d = [
 OR(sa("(i) Write all the factors of 72. (ii) Write 72 and 108 as products of primes. (iii) Find the HCF and the LCM of 72 and 108.", 5,
       f"(i) {', '.join(str(k) for k in range(1,73) if 72%k==0)} (1 mark)<br>(ii) 72 = {pfs(72)}; 108 = {pfs(108)} (2 marks)<br>(iii) HCF = {gcd(72,108)}, LCM = {lcm(72,108)} (2 marks)"),
    sa("(i) List all primes up to 50 using the Sieve of Eratosthenes (write the first four steps in words). (ii) Write all pairs of twin primes up to 50.", 5,
       f"(i) Write 1 to 50, cross out 1, keep 2 and strike its multiples, then 3, then 5, then 7 and strike their multiples (2 marks). Primes: {', '.join(map(str, primes(1,50)))} (1 mark)<br>(ii) Twin primes: " + ", ".join(f"({p}, {p+2})" for p in primes(1, 48) if p + 2 in primes(1, 50)) + " (2 marks)")),
 OR(sa("A teacher recorded the books read by 20 students in a month: 2, 3, 1, 2, 4, 2, 3, 1, 2, 5, 3, 2, 4, 1, 2, 3, 2, 5, 3, 2. (i) Make a frequency table. (ii) Draw a bar graph (1 cm = 1 student on the vertical axis). (iii) How many students read at least 4 books?", 5,
       "Frequencies: " + ", ".join(f"{k} book(s): {[2,3,1,2,4,2,3,1,2,5,3,2,4,1,2,3,2,5,3,2].count(k)}" for k in range(1, 6)) + " (2 marks)<br>(ii) Bars of those heights, equal width, labelled axes (2 marks)<br>(iii) 4-book + 5-book students = " + str(sum([2,3,1,2,4,2,3,1,2,5,3,2,4,1,2,3,2,5,3,2].count(k) for k in (4, 5))) + " (1 mark)"),
    sa("The number of cycles sold in a shop in six months is: Jan 25, Feb 40, Mar 30, Apr 15, May 35, Jun 20. (i) Draw a pictograph using 1 symbol = 5 cycles. (ii) In which month were the most cycles sold? (iii) Find the total cycles sold.", 5,
       "(i) Symbols: Jan 5, Feb 8, Mar 6, Apr 3, May 7, Jun 4 (2 marks for correct symbols, 1 mark for key and title)<br>(ii) February (1 mark)<br>(iii) 25 + 40 + 30 + 15 + 35 + 20 = " + str(25 + 40 + 30 + 15 + 35 + 20) + " (1 mark)")),
 sa("A farmer's rectangular field is 40 m long and 25 m wide. 2/5 of the field is used for wheat, 1/4 for mustard and the rest for vegetables. Find (i) the area of the field (ii) the area for wheat (iii) the area for mustard (iv) the area for vegetables (v) the fraction of the field used for vegetables.", 5,
    f"(i) {fl} m² (ii) {fl*2//5} m² (iii) {fl//4} m² (iv) {fl - fl*2//5 - fl//4} m² (v) 1 − 2/5 − 1/4 = {imp(1 - Fr(2,5) - Fr(1,4))} (1 mark each)"),
]
sales = [("Mon", 18), ("Tue", 24), ("Wed", 30), ("Thu", 12), ("Fri", 36)]
case1 = case("The school canteen records the number of glasses of lassi sold from Monday to Friday in a bar graph.",
 [sub("On which day were the fewest glasses sold?", 1, "Thursday (12 glasses)"),
  sub("How many glasses were sold in the whole week?", 1, f"18 + 24 + 30 + 12 + 36 = {sum(v for _, v in sales)}"),
  OR(sub("How many more glasses were sold on Friday than on Monday?", 2, "36 − 18 (1 mark) = 18 glasses (1 mark)"),
     sub("One glass costs ₹20. Find the money collected on Wednesday.", 2, "30 × 20 (1 mark) = ₹600 (1 mark)"))], fig=G.bar(sales, 36, 6, 'Glasses', 'Day'))
case2 = case("A submarine is at 35 m below sea level. We write this as −35 m. It rises 12 m to take photographs and then dives 20 m to study a coral reef.",
 [sub("At what level is the submarine after rising 12 m?", 1, "−35 + 12 = −23 m"),
  sub("At what level is it after diving 20 m?", 1, "−23 − 20 = −43 m"),
  OR(sub("How many metres is the final position below sea level?", 2, "Final level −43 m (1 mark) → 43 m below sea level (1 mark)"),
     sub("A bird flies at +18 m. Find the vertical distance between the bird and the submarine's final position.", 2, "18 − (−43) (1 mark) = 61 m (1 mark)"))])
case3 = case("Pooja designs a square floor tile for the school hall. She asks: which symmetries does a square tile have, and how does a plain rectangular (non-square) tile differ?",
 [sub("Write the number of lines of symmetry of a square tile.", 1, "4"),
  sub("What is the order of rotational symmetry of a square tile?", 1, "4"),
  OR(sub("Through how many degrees must a square tile be rotated (smallest turn) to look the same?", 2, "360° ÷ 4 (1 mark) = 90° (1 mark)"),
     sub("Give the number of lines of symmetry and the order of rotational symmetry of a rectangular (non-square) tile.", 2, "2 lines of symmetry (1 mark); order 2 (1 mark)"))])
META = meta(3); SECTIONS = secs(q1, b, c, d, [case1, case2, case3])
