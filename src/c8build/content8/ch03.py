from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def roman(n):
    out = ""
    for v, s in [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]:
        while n >= v: out += s; n -= v
    return out
def to_base(n, b):
    d = ""
    while n: d = str(n % b) + d; n //= b
    return d or "0"
# A: Roman to number (6) and number to Roman (4)
for n in [49, 94, 149, 444, 1994, 2024]:
    A.append(M4(f"The Roman numeral {roman(n)} stands for:", str(n), [str(n+10), str(n-10), str(n+1)], "Add the values, subtracting a smaller symbol that comes before a larger one"))
for n in [38, 76, 99, 400]:
    r = roman(n)
    A.append(M4(f"{n} in Roman numerals is:", r, [roman(n+1) if roman(n+1) != r else roman(n+2), roman(n-1), roman(n+10)], f"{n} = {r}"))
# A: base conversions (8)
for n, b in [(13, 2), (25, 2), (30, 2), (17, 3), (26, 3), (38, 5), (44, 6), (100, 7)]:
    r = to_base(n, b)
    wrong = [to_base(n + 1, b), to_base(n - 1, b), to_base(n + 2, b)]
    A.append(M4(f"The decimal number {n} written in base {b} is:", r, [w for w in wrong if w != r], f"Repeated division of {n} by {b}"))
# A: base to decimal (6)
for s, b in [("1101", 2), ("10110", 2), ("212", 3), ("1000", 4), ("43", 5), ("35", 8)]:
    n = int(s, b)
    A.append(M4(f"The value of ${s}$ in base {b}, in the decimal system, is:", str(n), [str(n+1), str(n-1), str(n+2)], f"Add digit × place value in base {b}"))
# A: facts (16)
A += [
 M4("Our present system of writing numbers with the digits 0 to 9 originated in:", "India", ["Greece", "Rome", "Egypt"], "Hindu numerals"),
 M4("The first known written use of the digit zero as a dot is in the:", "Bakhshali manuscript", ["Rigveda", "Arthashastra", "Lilavati"], "c. 3rd century CE"),
 M4("The mathematician who fully explained computation with the Indian ten-symbol system around 499 CE was:", "Aryabhata", ["Fibonacci", "Euclid", "Al-Kindi"], "Aryabhatiya"),
 M4("The word 'algorithm' is named after:", "Al-Khwarizmi", ["Aryabhata", "Fibonacci", "Euclid"], "He wrote on calculation with Hindu numerals"),
 M4("The Italian mathematician who argued for adopting Indian numerals in Europe around 1200 was:", "Fibonacci", ["Brahmagupta", "Al-Kindi", "Laplace"], "Liber Abaci"),
 M4("The Mesopotamian number system was based on:", "60", ["10", "20", "5"], "Sexagesimal"),
 M4("The Maya number system was based on:", "20", ["60", "10", "12"], "Vigesimal"),
 M4("Which Roman symbol stands for 500?", "D", ["C", "L", "M"], "I=1, V=5, X=10, L=50, C=100, D=500, M=1000"),
 M4("In Roman numerals, a smaller symbol written before a larger one is:", "subtracted", ["added", "multiplied", "ignored"], "IV = 4"),
 M4("The idea of mapping each object to exactly one stick or pebble is called:", "one-to-one mapping", ["place value", "base conversion", "rounding"], "Basic mechanism of counting"),
 M4("The base of the binary number system is:", "2", ["10", "8", "16"], "Digits are 0 and 1"),
 M4("The digits used in base 5 are:", "0, 1, 2, 3, 4", ["1 to 5", "0 to 5", "0, 1"], "Digits are less than the base"),
 M4("The value of the digit 4 in 5400 (decimal) is:", "4 hundreds, i.e. 400", ["4 tens", "4 thousands", "4 ones"], "Place value"),
 M4("The Roman system does not have a symbol for:", "zero", ["five", "fifty", "one thousand"], "No zero and no place value"),
 M4("Ancient Indian texts named powers of ten such as eka, dasha, shata and:", "sahasra", ["lakh only", "crore only", "yojana"], "Thousand"),
 M4("The Indian numerals were transmitted to the Arab world by around:", "800 CE", ["500 BCE", "1500 CE", "1900 CE"], "Later reached Europe"),
]
assert len(A) == 40, len(A)
B = [
 Q("What is one-to-one mapping? Give an example from counting cattle.", "Pairing each object with exactly one other object (1); each cow paired with one stick (1).", "1+1"),
 Q("Write 2024 in Roman numerals.", "MMXXIV (2).", "2"),
 Q("What do we mean by the base of a number system?", "The number of distinct digits used, and the number each place is multiplied by (2).", "2"),
 Q("Why is the Roman system not suitable for large calculations?", "No zero or place value, long strings of symbols (2).", "2"),
 Q("Convert $1011_2$ to decimal.", r"$8+0+2+1=11$ (2).", "2"),
 Q("Convert 19 to base 2.", r"$19=10011_2$ (2).", "2"),
 Q("Why is the Hindu number system considered a great invention?", "Ten symbols give every number using place value and zero, making arithmetic simple (2).", "2"),
 Q("Name two ancient civilisations that had their own number systems.", "Egyptian, Mesopotamian (also Roman, Maya) (1+1).", "1+1"),
 Q("Who named 'Hindu numerals' and who spread them in Europe?", "Al-Khwarizmi and Al-Kindi used the name Hindu numerals (1); Fibonacci promoted them in Europe (1).", "1+1"),
 Q("What is a tally mark system?", "Counting by marking a stroke for each object, grouped in fives (2).", "2"),
 Q("Write $XLIV$ in decimal.", "$40+4=44$ (2).", "2"),
 Q("In base 60 (Mesopotamia), how many minutes make an hour? Why is that a relic of base 60?", "60 minutes (1); our time measurement still uses 60 (1).", "1+1"),
 Q("State the place values of digits in $734_8$.", r"$7\times64,\ 3\times8,\ 4\times1$ (2).", "2"),
 Q("Which digit appears in base 2 numbers? Write 5 in base 2.", r"0 and 1 (1); $101_2$ (1).", "1+1"),
 Q("Why did Europeans call Hindu numerals 'Arabic numerals'?", "They learnt them from the Arab world (2).", "2"),
 Q("What is the role of zero in a place value system?", "It holds a place when a position is empty, distinguishing 305 from 35 (2).", "2"),
]
for n in [1444, 399, 2499, 1666, 3888, 949]:
    C.append(Q(f"Write {n} in Roman numerals and explain the grouping.", f"{n} = {roman(n)} (2); grouped by thousands, hundreds, tens and ones (1).", "2+1"))
for n, b in [(45, 2), (60, 3), (88, 5), (123, 6), (200, 8), (77, 4)]:
    C.append(Q(f"Convert {n} to base {b} showing the steps.", f"Repeated division by {b} (2); {n} = ${to_base(n,b)}_{{{b}}}$ (1).", "2+1"))
for s, b in [("11011", 2), ("2201", 3), ("1234", 5), ("707", 8)]:
    n = int(s, b)
    C.append(Q(rf"Convert ${s}_{{{b}}}$ to decimal.", rf"Expand using powers of {b} (2); value $={n}$ (1).", "2+1"))
C += [
 Q("Compare Roman and Hindu numeral systems on two points.", "Hindu uses place value and zero (1.5); Roman has no zero and needs many symbols (1.5).", "1½+1½"),
 Q("Describe how the Mesopotamians wrote numbers.", "Used base 60 (1); two wedge symbols for 1 and 10 (1); place value without a true zero in early times (1).", "1+1+1"),
 Q("How did Indian numerals travel to Europe?", "From India to the Arab world around 800 CE (1.5); then to Europe via Fibonacci and others around 1100–1200 CE (1.5).", "1½+1½"),
 Q("Describe the Egyptian method of writing numbers.", "Separate symbols for 1, 10, 100, 1000 and so on (1.5); repeated to show quantities, additive (1.5).", "1½+1½"),
]
C += [
 Q("Add $MCDXL$ and $DLX$ in decimal and write the sum in Roman numerals.", "$1440+560=2000$ (2); MM (1).", "2+1"),
 Q("Write the numbers 1 to 10 in Roman numerals.", "I, II, III, IV, V, VI, VII, VIII, IX, X (3).", "3"),
 Q("Explain why base 2 needs only two digits.", "In base $b$ digits run from 0 to $b-1$ (1.5); for $b=2$ these are 0 and 1 (1.5).", "1½+1½"),
 Q("A herd of 37 cows is to be counted in groups of 6. Express the count in base 6.", r"$37=6\times6+1$ (2); $101_6$ (1).", "2+1"),
]
C = C[:24]
assert len(C) == 24, len(C)
D = [
 Q("(i) Why did early humans need to count? (ii) Describe how pebbles or sticks help in counting. (iii) What is the limitation of using letters of the alphabet for counting?", "(i) To track livestock, trade and time (2). (ii) One-to-one mapping (2). (iii) Cannot count beyond the number of letters (1).", "2+2+1"),
 Q("(i) Convert 1994 to Roman numerals. (ii) Convert MCMXLIV to decimal.", "(i) MCMXCIV (2.5). (ii) 1944 (2.5).", "2½+2½"),
 Q(r"(i) Convert $111010_2$ to decimal. (ii) Convert 58 to binary. (iii) Add $1011_2+110_2$.", r"(i) $58$ (2). (ii) $111010_2$ (2). (iii) $10001_2=17$ (1).", "2+2+1"),
 Q("<b>Case study:</b> A clock tower shows time using base-60 minutes and seconds, a tradition traced to Mesopotamia. (i) How many seconds are in 3 hours? (ii) Why is 60 convenient? (iii) Write 3 h 25 min in minutes.", r"(i) $3\times3600=10800$ s (1). (ii) 60 has many divisors: 2, 3, 4, 5, 6, 10, 12, 15, 20, 30 (2). (iii) $205$ min (2).", "1+2+2"),
 Q("(i) Describe the contribution of Aryabhata and Al-Khwarizmi to numbers. (ii) Why do we say 'Hindu–Arabic numerals'?", "(i) Aryabhata explained the ten-symbol system fully; Al-Khwarizmi spread it in the Arab world (3). (ii) Originated in India, transmitted through the Arab world (2).", "3+2"),
 Q(r"(i) Write the expanded form of $2304$ in base 10. (ii) Write $2304_5$ in decimal.", r"(i) $2\times10^3+3\times10^2+0\times10+4$ (2). (ii) $2\times125+3\times25+0+4=329$ (3).", "2+3"),
 Q("<b>Case study:</b> Computers store data in binary. A byte has 8 binary digits. (i) How many different values can a byte store? (ii) Write the largest value in decimal. (iii) Convert 200 to binary.", r"(i) $2^8=256$ (2). (ii) 255 (1). (iii) $11001000_2$ (2).", "2+1+2"),
 Q(r"(i) Subtract $XLVII$ from $C$ in Roman numerals. (ii) Write the answer in Roman numerals.", "(i) $100-47=53$ (3). (ii) LIII (2).", "3+2"),
 Q("(i) Compare the Maya and Mesopotamian number systems. (ii) State one similarity.", "(i) Maya base 20, Mesopotamian base 60; Maya had a shell for zero (3). (ii) Both used place value (2).", "3+2"),
 Q("(i) What is the Bakhshali manuscript? (ii) What does it tell us about zero?", "(i) An ancient Indian manuscript from about the 3rd century CE (2). (ii) It shows a dot used as zero (3).", "2+3"),
 Q(r"(i) Convert $0.5$ and $75$ to base 2 where possible. (ii) What do the digits of $1000_2$ represent?", r"(i) $0.1_2$ and $1001011_2$ (3). (ii) $2^3=8$ (2).", "3+2"),
 Q("<b>Case study:</b> A shopkeeper counts apples in groups of 5, 25 and 125. (i) Which base is this? (ii) Write 163 apples in this base. (iii) Write the digits.", r"(i) Base 5 (1). (ii) $163=1\times125+1\times25+2\times5+3$ i.e. $1123_5$ (3). (iii) 1, 1, 2, 3 (1).", "1+3+1"),
 Q("(i) Why are Roman numerals poor for multiplication? (ii) Illustrate by trying $IX\\times XI$.", "(i) No place value (2). (ii) $9\\times11=99$ is XCIX, but the method is not systematic (3).", "2+3"),
 Q(r"(i) Show how 1 lakh and 1 crore are written in Indian place value. (ii) How many lakhs make one crore?", r"(i) $1,00,000$ and $1,00,00,000$ (3). (ii) 100 (2).", "3+2"),
 Q("(i) Trace the history of Hindu numerals from India to Europe. (ii) Name two persons involved.", "(i) India, Arab world around 800 CE, Europe around 1100–1200 CE (3). (ii) Al-Khwarizmi and Fibonacci (2).", "3+2"),
 Q(r"(i) Write the first 10 numbers in base 3. (ii) Which digit is missing?", r"(i) $1,2,10,11,12,20,21,22,100,101$ (3). (ii) 3 and higher digits (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
