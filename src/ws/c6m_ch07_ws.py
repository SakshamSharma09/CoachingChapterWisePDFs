"""Class 6 Maths Ch 7 - Fractions: worksheet + detailed notes."""
from libws import *
BANK = "c6m_ch07"

def f(a, b): return "«\\frac{" + str(a) + "}{" + str(b) + "}»"
def mx(w, a, b): return "«" + str(w) + "\\frac{" + str(a) + "}{" + str(b) + "}»"
F, X = f, mx
_W = W
def T(s):
    """markers are wrapped in $..$ when outside math and bare when already inside $..$"""
    import re as _re
    parts = s.split("$")
    for i, p in enumerate(parts):
        parts[i] = _re.sub("«(.*?)»", (lambda m: m.group(1)) if i % 2 else (lambda m: "$" + m.group(1) + "$"), p)
    return "$".join(parts)
def W(q, marks, ans, level, opts=None, fig=None, wp=False):
    return _W(T(q), marks, T(ans), level, opts=[T(o) for o in opts] if opts else None, fig=fig, wp=wp)

WS = [
# ---------------- EASY ----------------
W("A circle is divided into 8 equal parts and 3 parts are shaded. The fraction shaded is", 1, f"(a) {F(3,8)}. 3 shaded parts out of 8 equal parts. (1)", "E",
  opts=[F(3, 8), F(5, 8), F(3, 5), F(8, 3)]),
W("Which of these is an improper fraction?", 1, f"(c) {F(9,4)}. The numerator 9 is greater than the denominator 4. (1)", "E",
  opts=[F(2, 9), F(4, 11), F(9, 4), F(1, 6)]),
W(f"Which fraction is equivalent to {F(2,3)}?", 1, f"(d) {F(8,12)}. Multiply numerator and denominator by 4. (1)", "E",
  opts=[F(4, 9), F(5, 6), F(3, 2), F(8, 12)]),
W(f"{F(17,5)} written as a mixed fraction is", 1, f"(b) {X(3,2,5)}. $17\\div5$ gives quotient 3, remainder 2. (1)", "E",
  opts=[X(2, 3, 5), X(3, 2, 5), X(3, 5, 2), X(4, 1, 5)]),
W("Which is the greatest fraction?", 1, f"(c) {F(5,7)}. Same denominator, so the largest numerator wins. (1)", "E",
  opts=[F(3, 7), F(2, 7), F(5, 7), F(4, 7)]),
W(f"{F(3,8)} + {F(2,8)} =", 1, f"(a) {F(5,8)}. Add numerators, keep the denominator. (1)", "E",
  opts=[F(5, 8), F(5, 16), F(6, 8), F(1, 8)]),
W(f"The lowest form of {F(18,24)} is", 1, f"(d) {F(3,4)}. HCF of 18 and 24 is 6; divide both by 6. (1)", "E",
  opts=[F(9, 12), F(6, 8), F(2, 3), F(3, 4)]),
W("A pizza is cut into 8 equal slices. Aman eats 3 slices and Binu eats 2 slices. What fraction of the pizza did they eat together, and what fraction is left?", 2, f"Eaten $=\\frac{{3+2}}{{8}}={f(5,8)}$ (1). Left $=\\frac{{8-5}}{{8}}={f(3,8)}$. (1)", "E", wp=True),
W("In a class of 40 students, 15 are girls. What fraction of the class are girls? Write it in the lowest form.", 2, f"{F(15,40)} (1). Divide by the HCF 5: {F(3,8)}. (1)", "E", wp=True),
W("Sunita has 24 mangoes. She gives away three-fourths of them. How many mangoes does she give?", 2, f"$24\\div4=6$ is one-fourth (1); three-fourths $=3\\times6=18$ mangoes. (1)", "E", wp=True),
W(f"Write two fractions equivalent to {F(3,5)}.", 2, f"Multiply top and bottom by 2 and by 3: {F(6,10)} and {F(9,15)}. (1+1)", "E"),
W(f"Change {F(13,4)} into a mixed fraction.", 1, f"$13\\div4=3$ remainder 1, so {X(3,1,4)}. (1)", "E"),
W(f"Change {X(2,3,5)} into an improper fraction.", 1, f"$\\frac{{2\\times5+3}}{{5}}={f(13,5)}$. (1)", "E"),
W(f"Put the correct sign ($>$, $<$ or $=$): (i) {F(3,5)} ___ {F(2,5)}  (ii) {F(1,3)} ___ {F(1,2)}", 2, f"(i) {F(3,5)} $>$ {F(2,5)} (same denominator, bigger numerator). (1) (ii) {F(1,3)} $<$ {F(1,2)} (same numerator, bigger denominator means smaller parts). (1)", "E"),
W(f"The line from 0 to 1 on a number line is divided into 4 equal parts. Into how many equal parts and which mark gives the fraction {F(3,4)}? ", 2, "Each part is $\\frac14$ (1). Start at 0 and count 3 marks: the third mark from 0 is $\\frac34$. (1)", "E"),
W(f"True or false, with a reason: {F(1,3)} and {F(2,6)} are equivalent fractions.", 2, f"True. (1) Multiplying top and bottom of {F(1,3)} by 2 gives {F(2,6)}. (1)", "E"),
W(f"Subtract: {F(7,9)} $-$ {F(4,9)}. Write the answer in the lowest form.", 2, f"{F(3,9)} (1) $={F(1,3)}$. (1)", "E"),

# ---------------- MEDIUM ----------------
W("Seema walks $\\frac35$ km to a bus stop and then $\\frac12$ km more to reach school. How far is her school from home? Write the answer as a mixed fraction.", 3, f"{F(3,5)}+{F(1,2)} with LCM of 5 and 2 $=10$ (1). $={f(6,10)}+{f(5,10)}={f(11,10)}$ (1) $={X(1,1,10)}$ km. (1)", "M", wp=True),
W("Rohan ate $\\frac25$ of a cake and Mohan ate $\\frac14$ of it. What fraction of the cake is left?", 3, f"Eaten $={f(8,20)}+{f(5,20)}={f(13,20)}$ (2). Left $=1-{f(13,20)}={f(7,20)}$. (1)", "M", wp=True),
W(f"Arrange in ascending order: {F(2,3)}, {F(3,4)}, {F(5,6)}, {F(1,2)}.", 3, f"LCM $=12$: {F(8,12)}, {F(9,12)}, {F(10,12)}, {F(6,12)} (2). Ascending: {F(1,2)}, {F(2,3)}, {F(3,4)}, {F(5,6)}. (1)", "M"),
W(f"Reduce {F(36,48)} to the lowest form by finding the HCF of 36 and 48.", 2, f"HCF $=12$ (1). {F(36,48)} $={F(3,4)}$. (1)", "M"),
W("A shopkeeper sells $2\\frac14$ m of cloth to one customer and $3\\frac12$ m to another. How much cloth did he sell in all?", 3, f"{X(2,1,4)}+{X(3,1,2)}: whole parts $5$ (1); fractions {f(1,4)}+{f(2,4)}={f(3,4)} (1). Total $={X(5,3,4)}$ m. (1)", "M", wp=True),
W("A jug has $5\\frac12$ litres of milk. $2\\frac34$ litres are poured out. How much milk is left?", 3, f"{f(11,2)}-{f(11,4)}={f(22,4)}-{f(11,4)} (1) $={f(11,4)}$ (1) $={X(2,3,4)}$ litres. (1)", "M", wp=True),
W(f"Find the mistake. A student writes {F(2,5)} + {F(3,7)} = {F(5,12)}. Correct it and explain the error.", 3, f"The student added numerators and denominators. (1) Correct: LCM $=35$; {f(14,35)}+{f(15,35)}={f(29,35)} (2).", "M"),
W(f"Find the missing numbers: (i) {F(3,7)} $=\\frac{{\\square}}{{28}}$ (ii) {F(5,8)} $=\\frac{{35}}{{\\square}}$", 2, "(i) $28=7\\times4$, so numerator $=3\\times4=12$. (1) (ii) $35=5\\times7$, so denominator $=8\\times7=56$. (1)", "M"),
W("Ankit has read $\\frac58$ of a book and Bhavna has read $\\frac34$ of the same book. Who has read more and by what fraction of the book?", 3, f"{F(3,4)}={F(6,8)} (1). {F(6,8)} $>$ {F(5,8)}, so Bhavna has read more (1), by {f(6,8)}-{f(5,8)}={F(1,8)} of the book. (1)", "M", wp=True),
W(f"Write {X(4,2,3)} as an improper fraction and {F(29,6)} as a mixed fraction.", 2, f"{X(4,2,3)} $=$ {f(14,3)} (1). $29\\div6=4$ remainder 5, so {X(4,5,6)}. (1)", "M"),
W("A rope 2 m long is cut into pieces, each $\\frac14$ m long. How many pieces are there?", 2, "1 m has 4 pieces of $\\frac14$ m (1), so 2 m has $2\\times4=8$ pieces. (1)", "M", wp=True),
W("On a number line the gap between 2 and 3 is divided into 5 equal parts. Point P is the third mark after 2. Write the position of P as a mixed fraction and as an improper fraction.", 2, f"Each part is $\\frac15$. P $=2+{f(3,5)}={X(2,3,5)}$ (1) $={f(13,5)}$. (1)", "M"),
W("A farmer grows wheat on $\\frac12$ of his field, mustard on $\\frac13$ of it and vegetables on the rest. What fraction is used for vegetables?", 3, f"{f(1,2)}+{f(1,3)}={f(3,6)}+{f(2,6)}={f(5,6)} (2). Vegetables $=1-{f(5,6)}={f(1,6)}$. (1)", "M", wp=True),
W(f"Which pair is equivalent? (i) {F(4,9)} and {F(12,27)}  (ii) {F(5,6)} and {F(15,20)}. Give reasons.", 3, f"(i) {F(12,27)}: divide by 3 gives {F(4,9)}, so equivalent. (1) (ii) {F(15,20)} reduces to {F(3,4)}, not {F(5,6)}; not equivalent. (1) Reasons shown. (1)", "M"),
W("In a class of 40 students, $\\frac14$ come on foot, $\\frac38$ come by cycle and the rest by bus. How many students come by bus? What fraction is it?", 3, f"On foot $=40\\div4=10$; by cycle $=3\\times(40\\div8)=15$ (1). Bus $=40-25=15$ students (1). Fraction $={f(15,40)}={F(3,8)}$. (1)", "M", wp=True),
W(f"Add {F(5,6)} and {F(7,9)} and write the sum as a mixed fraction.", 3, f"LCM $=18$: {f(15,18)}+{f(14,18)}={f(29,18)} (2) $={X(1,11,18)}$. (1)", "M"),
W(f"Compare {F(7,12)} and {F(5,8)}. Which is greater?", 2, f"LCM $=24$: {F(14,24)} and {F(15,24)} (1). So {F(5,8)} is greater. (1)", "M"),
W("Heena uses $\\frac13$ of a ribbon for a gift and $\\frac14$ of it for her hair. What fraction of the ribbon is left? If the ribbon was 60 cm long, how many cm are left?", 3, f"Used $={f(4,12)}+{f(3,12)}={f(7,12)}$ (1). Left $={F(5,12)}$ (1). $60\\div12=5$, so $5\\times5=25$ cm. (1)", "M", wp=True),
W(f"Write three fractions that lie between {F(2,5)} and {F(3,5)}.", 2, f"Make the denominators 20: {F(8,20)} and {F(12,20)} (1). Between them: {F(9,20)}, {F(10,20)}, {F(11,20)}. (1)", "M"),

# ---------------- HARD ----------------
W("A water tank is $\\frac38$ full. Then $\\frac14$ of the tank is filled by a pipe. Later $\\frac16$ of the tank is used. What fraction of the tank is full now?", 4, f"LCM of 8, 4, 6 $=24$ (1). {f(9,24)}+{f(6,24)}={f(15,24)} (1). {f(15,24)}-{f(4,24)}={f(11,24)} (2). The tank is {F(11,24)} full.", "H", wp=True),
W("Ravi cycles $2\\frac12$ km from home to school, $1\\frac34$ km from school to the library and then $3\\frac14$ km straight back home. Find the total distance he travels.", 4, f"{f(5,2)}+{f(7,4)}+{f(13,4)}={f(10,4)}+{f(7,4)}+{f(13,4)} (2) $={f(30,4)}$ (1) $={X(7,1,2)}$ km. (1)", "H", wp=True),
W("Mother makes 3 kg of laddoos. She gives $1\\frac14$ kg to the neighbours and $\\frac34$ kg to the temple. How much is left for the family?", 3, f"Given away $={f(5,4)}+{f(3,4)}={f(8,4)}=2$ kg (2). Left $=3-2=1$ kg. (1)", "H", wp=True),
W("A fraction is equivalent to $\\frac35$ and the sum of its numerator and denominator is 56. Find the fraction.", 4, "Numerator $=3k$, denominator $=5k$ for some number $k$ (1). $3k+5k=8k=56$, so $k=7$ (2). Fraction $=\\frac{21}{35}$. (1)", "H"),
W("Explain why $\\frac58>\\frac59$ without finding a common denominator. Then arrange $\\frac47,\\frac49,\\frac45,\\frac4{11}$ in descending order.", 4, "With the same numerator, the larger denominator cuts the whole into smaller parts. So 5 eighths $>$ 5 ninths. (2) Descending: $\\frac45>\\frac47>\\frac49>\\frac4{11}$. (2)", "H"),
W("A rope is $5\\frac34$ m long. Rajesh cuts off $2\\frac12$ m and then another $1\\frac18$ m. How much rope remains?", 4, f"{f(23,4)}={f(46,8)}, {f(5,2)}={f(20,8)}, {f(9,8)} (1). Cut off $={f(20,8)}+{f(9,8)}={f(29,8)}$ (1). Remains $={f(46,8)}-{f(29,8)}={f(17,8)}$ (1) $={X(2,1,8)}$ m. (1)", "H", wp=True),
W("Find the error. A student works: $3\\frac12-1\\frac34=(3-1)+(\\frac34-\\frac12)=2\\frac14$. Why is it wrong? Give the correct answer.", 4, f"The student subtracted the smaller fraction from the larger one ({f(3,4)}-{f(1,2)}) instead of {f(1,2)}-{f(3,4)}, which cannot be done. (2) Correct: {f(7,2)}-{f(7,4)}={f(14,4)}-{f(7,4)}={f(7,4)}={X(1,3,4)}. (2)", "H"),
W("Asha, Bina and Chitra share a cake. Asha eats $\\frac14$, Bina $\\frac13$ and Chitra $\\frac16$. Who ate the least? What fraction of the cake is left?", 4, f"LCM $=12$: {f(3,12)}, {f(4,12)}, {f(2,12)} (1). Chitra ate the least (1). Eaten $={f(9,12)}={f(3,4)}$ (1). Left $={F(1,4)}$. (1)", "H", wp=True),
W("On a number line, the gap between 2 and 3 is divided into 6 equal parts. Point A is the first mark after 2 and point B is the fifth mark. Write A and B as mixed fractions, find the distance AB, and name the mark midway between them.", 4, f"A $={X(2,1,6)}$, B $={X(2,5,6)}$ (1). AB $={f(5,6)}-{f(1,6)}={f(4,6)}={F(2,3)}$ (2). Midway is the third mark $=2\\frac36={X(2,1,2)}$. (1)", "H"),
W("A school ground is used as follows: $\\frac25$ for cricket, $\\frac14$ for football, $\\frac1{10}$ for kabaddi and the rest for a garden. What fraction is the garden? If the ground is 800 m$^2$, find the area of the garden.", 5, f"LCM $=20$: {f(8,20)}+{f(5,20)}+{f(2,20)}={f(15,20)} (2). Garden $=1-{f(15,20)}={f(5,20)}={F(1,4)}$ (2). Area $=800\\div4=200$ m$^2$. (1)", "H", wp=True),
W("Find a fraction that lies between $\\frac58$ and $\\frac34$. Show that your answer is correct using a common denominator.", 3, f"Write with denominator 16: {f(5,8)}={f(10,16)}, {f(3,4)}={f(12,16)} (1). {F(11,16)} lies between (1) because {f(10,16)}<{f(11,16)}<{f(12,16)}. (1)", "H"),
W("Simran's doctor says she should drink at least 1 litre of water daily. She drinks $\\frac14$ L in the morning, $\\frac13$ L at noon and $\\frac12$ L in the evening. Does she meet the target? By how much is she above or below it?", 4, f"Total $={f(3,12)}+{f(4,12)}+{f(6,12)}={f(13,12)}$ (2) $={X(1,1,12)}$ L. (1) She meets the target and is {F(1,12)} L above it. (1)", "H", wp=True),
W("Arrange in ascending order: $3\\frac12$, $\\frac{10}3$, $3\\frac34$, $\\frac{13}4$. Show your working.", 3, f"Write each as a mixed fraction: {X(3,1,2)}; {f(10,3)}={X(3,1,3)}; {X(3,3,4)}; {f(13,4)}={X(3,1,4)} (1). All have whole part 3, so compare {f(1,2)}, {f(1,3)}, {f(3,4)}, {f(1,4)}: with LCM 12 these are 6, 4, 9, 3 (1). Ascending: {F(13,4)}, {F(10,3)}, {X(3,1,2)}, {X(3,3,4)}. (1)", "H"),
]

CH = dict(num=7, title="Fractions", tag="Maths (Part 2)",
 intro="A fraction tells us about equal parts of a whole or of a collection. In this chapter you place fractions on the number line, write mixed fractions, find equivalent fractions, compare them and add and subtract them, and then use all this to solve everyday problems about food, money, time and distance.",
 big_questions=["What does a fraction mean, and how can we show it on a number line?", "How do we find equivalent fractions and compare fractions?", "How do we add and subtract fractions, including mixed fractions?"],
 blocks=[
 ("h2", "7.1 Fractional Units and Equal Shares"),
 ("p", "When we cut a roti into 4 **equal** parts, each part is one fourth, written ½ for halves, ¼ for fourths and so on. A **fractional unit** is one equal part of a whole. The word *equal* is very important: a fraction counts equal parts only. If a chocolate bar is broken into 4 unequal pieces, a piece is not one fourth."),
 ("note", "DEFINITION", "A **fraction** a/b has a **numerator** a (the number of parts taken) and a **denominator** b (the number of equal parts the whole is divided into). The denominator can never be 0. The fraction 3/8 means 3 parts out of 8 equal parts, or 3 times the fractional unit 1/8."),
 ("p", "A fraction can describe a part of a single whole (3/8 of a pizza) or a part of a collection (15 of 40 students is 15/40 = 3/8 of the class). To find 3/4 of 24 mangoes: 24 ÷ 4 = 6 is one fourth, so three fourths = 3 × 6 = 18 mangoes."),
 ("table", ["Kind", "Meaning", "Examples"], [
  ["Proper fraction", "Numerator is smaller than the denominator; less than 1", "3/8, 2/9, 5/11"],
  ["Improper fraction", "Numerator is greater than or equal to the denominator; 1 or more", "9/4, 13/5, 7/7"],
  ["Mixed fraction", "A whole number and a proper fraction together", "2 3/5, 4 1/2"],
  ["Unit fraction", "Numerator is 1", "1/2, 1/7, 1/10"],
  ["Like fractions", "Same denominator", "3/9, 4/9, 8/9"],
  ["Unlike fractions", "Different denominators", "1/2, 2/3, 5/8"]]),
 ("h2", "7.2 Fractions on the Number Line"),
 ("p", "On the number line, the gap between 0 and 1 is the whole unit. To mark 3/4, divide the gap from 0 to 1 into **4 equal parts** and count **3 marks** from 0. The marks beyond 1 give improper fractions: with fourths, the marks after 1 are 5/4, 6/4, 7/4 and 8/4 = 2."),
 ("ul", ["The gap between 2 and 3 divided into 5 equal parts has marks 2 1/5, 2 2/5, 2 3/5 and 2 4/5; the third mark is 2 3/5 = 13/5.", "A point further to the right is always the greater fraction.", "Between any two fractions there are many other fractions (for example 11/16 lies between 5/8 and 3/4)."]),
 ("p", "**Fractions in daily life.** A cricket match uses half-century and quarter-final; a recipe says 1/2 cup of sugar; a tailor measures 2 1/4 m of cloth; a bus journey of 3 1/2 hours. Reading and comparing such measures correctly is the real use of this chapter. A good habit is to ask: is my answer more or less than 1, and does it fit on the number line where I expect it?"),
 ("h2", "7.3 Mixed and Improper Fractions"),
 ("table", ["Conversion", "Method", "Example"], [
  ["Improper → mixed", "Divide numerator by denominator: quotient is the whole part, remainder is the new numerator", "17/5: 17 ÷ 5 = 3 remainder 2, so 3 2/5"],
  ["Mixed → improper", "(whole × denominator + numerator) over the denominator", "2 3/5 = (2 × 5 + 3)/5 = 13/5"]]),
 ("note", "REMEMBER", "A mixed fraction is a **sum**: 3 2/5 means 3 + 2/5. When you add or subtract mixed fractions you can add the whole parts and fraction parts separately, but be careful when the fraction part you subtract is larger."),
 ("h2", "7.4 Equivalent Fractions and Lowest Form"),
 ("note", "DEFINITION", "**Equivalent fractions** are different-looking fractions that stand for the same part of the whole, such as 1/2, 2/4, 3/6 and 4/8. They are at the same point on the number line."),
 ("ul", ["**To make an equivalent fraction:** multiply (or divide) the numerator and denominator by the **same non-zero number**. 2/3 = (2 × 4)/(3 × 4) = 8/12.", "**Finding a missing number:** 3/7 = ?/28. Since 28 = 7 × 4, the numerator is 3 × 4 = 12.", "**Lowest form (simplest form):** divide the numerator and denominator by their **HCF**. 36/48: HCF = 12, so 36/48 = 3/4. In lowest form the numerator and denominator have no common factor except 1.", "**Test for equivalence:** reduce both to lowest form. 12/27 reduces to 4/9, so it is equivalent to 4/9; 15/20 reduces to 3/4, so it is **not** equivalent to 5/6."]),
 ("h2", "7.5 Comparing Fractions"),
 ("table", ["Situation", "Rule", "Example"], [
  ["Same denominator", "The larger numerator is the larger fraction", "5/7 > 3/7"],
  ["Same numerator", "The larger denominator is the smaller fraction (smaller parts)", "5/8 > 5/9; 1/3 < 1/2"],
  ["Different both", "Make like fractions using the **LCM** of the denominators, then compare numerators", "7/12 and 5/8: LCM 24, 14/24 < 15/24, so 5/8 is greater"],
  ["Compare with 1/2 or 1", "Find which side of ½ or 1 each lies on", "5/9 > ½ because 2 × 5 = 10 > 9"]]),
 ("h2", "7.6 Adding and Subtracting Fractions"),
 ("note", "FORMULA", "**Like fractions:** a/c + b/c = (a + b)/c and a/c − b/c = (a − b)/c. Only the numerators are added or subtracted; the denominator stays the same. **Unlike fractions:** first change to like fractions using the LCM of the denominators."),
 ("steps", [("Step 1 — LCM", "Find the LCM of the denominators."), ("Step 2 — Convert", "Write each fraction as an equivalent fraction with that denominator."), ("Step 3 — Operate", "Add or subtract the numerators."), ("Step 4 — Simplify", "Reduce to lowest form and, if the answer is improper, write it as a mixed fraction.")]),
 ("p", "**Mixed fractions:** change both to improper fractions and then add or subtract, or add the whole numbers and fractions separately. 5 1/2 − 2 3/4: 11/2 − 11/4 = 22/4 − 11/4 = 11/4 = 2 3/4."),
 ("note", "IMPORTANT", "Never add the denominators. 2/5 + 3/7 is **not** 5/12. Correct: LCM = 35, 14/35 + 15/35 = 29/35."),
 ("h2", "7.7 Worked Examples"),
 ("steps", [
  ("Example 1 — Add unlike fractions", "Seema walks 3/5 km and then 1/2 km. LCM of 5 and 2 is 10. 3/5 = 6/10 and 1/2 = 5/10. Sum = 11/10 = 1 1/10 km."),
  ("Example 2 — What is left", "Rohan ate 2/5 and Mohan 1/4 of a cake. LCM 20: 8/20 + 5/20 = 13/20. Left = 1 − 13/20 = 7/20."),
  ("Example 3 — Order", "Arrange 2/3, 3/4, 5/6, 1/2 in ascending order. LCM 12: 8/12, 9/12, 10/12, 6/12. Ascending: 1/2, 2/3, 3/4, 5/6."),
  ("Example 4 — Mixed fractions", "A shopkeeper sells 2 1/4 m and 3 1/2 m of cloth. Whole parts: 2 + 3 = 5. Fractions: 1/4 + 2/4 = 3/4. Total 5 3/4 m."),
  ("Example 5 — Fraction of a quantity", "40 students: 1/4 walk, 3/8 cycle. Walk = 10, cycle = 15, so bus = 40 − 25 = 15 students = 15/40 = 3/8."),
  ("Example 6 — Unknown fraction", "A fraction is equivalent to 3/5 and its numerator and denominator add up to 56. Write it as 3k/5k. 8k = 56, so k = 7 and the fraction is 21/35."),
 ]),
 ("h2", "7.8 Word Problems: How to Translate"),
 ("ul", ["**Eaten, walked, used, poured out, sold** → usually subtraction from the whole or addition of parts used.", "**Together, in all, total** → add the fractions.", "**Left, remaining** → subtract from 1 (the whole) or from the given quantity.", "**More than, less than, difference** → subtract the smaller from the greater (compare first!).", "**Fraction of a collection:** divide the collection by the denominator, then multiply by the numerator."]),
 ("h2", "7.9 A Pinch of History and Common Mistakes"),
 ("p", "Ancient Indians used fractions in measuring land, grain and time. Mathematicians in India wrote fractions with the numerator above the denominator, as we do now, but without the bar; the bar came later."),
 ("note", "REMEMBER", "1) Adding denominators. 2) Comparing only numerators when the denominators differ. 3) Forgetting to reduce the answer. 4) Writing the remainder as the whole part when changing improper to mixed. 5) Cutting unequal parts and still calling them fractions. 6) In mixed subtraction, taking the smaller fraction part minus the larger."),
 ("h2", "7.10 Likely Exam Questions"),
 ("qa", [
  ("What is a fraction? Name its two parts.", "A fraction names equal parts of a whole. The top number is the numerator and the bottom number is the denominator."),
  ("Convert 17/5 into a mixed fraction.", "17 ÷ 5 = 3 remainder 2, so 3 2/5."),
  ("Write three fractions equivalent to 2/3.", "4/6, 6/9 and 8/12 (multiply top and bottom by 2, 3, 4)."),
  ("Reduce 18/24 to its lowest form.", "HCF = 6, so 3/4."),
  ("Which is greater, 7/12 or 5/8?", "LCM 24: 14/24 and 15/24, so 5/8 is greater."),
  ("Find 3/4 of 24.", "24 ÷ 4 = 6; 3 × 6 = 18."),
  ("Subtract 2 3/4 from 5 1/2.", "11/2 − 11/4 = 11/4 = 2 3/4."),
  ("Why is 5/8 greater than 5/9?", "Same numerator; eighths are bigger parts than ninths."),
 ]),
 ],
 takeaways=["A **fraction** names equal parts of a whole or of a collection: numerator (parts taken) over denominator (equal parts).", "Know proper, improper, mixed, unit, like and unlike fractions.", "Convert improper to mixed by division; mixed to improper by whole × denominator + numerator.", "**Equivalent fractions:** multiply or divide both numerator and denominator by the same number; use the HCF for the lowest form.", "To compare unlike fractions, make like fractions with the **LCM**; same numerator, bigger denominator means smaller fraction.", "To add or subtract, make the denominators equal, then work on **numerators only**.", "For a fraction of a collection, divide by the denominator then multiply by the numerator.", "Always reduce answers and check by estimating on the number line."])

if __name__ == "__main__": run(__file__, BANK, 6, "Maths", WS, CH)
