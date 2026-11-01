import random
from c7maths.h import *
R = random.Random(701)
A = []; B = []; C = []; D = []
# A: number names (6)
for n in [305204, 4070000, 12678830, 8008080, 90450000, 2300109]:
    w = words(n); alts = [words(n + 1000) if n % 1000 == 0 else words(n + 10), words(int(str(n)[::-1])), words(n * 10)]
    A.append(M4(f"The number {ind(n)} is read as:", w, alts, "read digit groups from the left: crore, lakh, thousand, hundred"))
# A: numeral from words (4)
for n in [3040506, 70050000, 9900099, 15020300]:
    w = words(n)
    A.append(M4(f"In the Indian system, “{w}” is written as:", ind(n), [ind(n * 10), ind(n // 10), ind(int(str(n)[::-1])), ind(n + 1)], "place each period correctly"))
# A: place value (6)
for n, d in [(48275916, 7), (9340568, 3), (62810457, 8), (7305921, 5), (80416235, 4), (5629043, 6)]:
    pos = str(n).index(str(d)); pw = len(str(n)) - pos - 1
    nm = {0: "ones", 1: "tens", 2: "hundreds", 3: "thousands", 4: "ten thousands", 5: "lakhs", 6: "ten lakhs", 7: "crores"}
    val = d * 10 ** pw
    A.append(M4(f"The value of the digit {d} in {ind(n)} is:", ind(val), [ind(val * 10), ind(val // 10 if val >= 10 else val * 100), ind(d * 10 ** max(pw - 2, 0)) if d * 10 ** max(pw - 2, 0) != val else ind(val * 100)], f"digit {d} is in the {nm[pw]} place"))
# A: conversions (8)
A += [
 M4("One lakh equals:", "100 thousand", ["10 thousand", "1000 thousand", "10 million"], "1,00,000 = 100 × 1000"),
 M4("One crore equals:", "100 lakh", ["10 lakh", "1000 lakh", "10,000 lakh"], "1,00,00,000 = 100 × 1,00,000"),
 M4("The smallest 6-digit number is:", "1,00,000", ["99,999", "10,000", "10,00,000"], "one lakh"),
 M4("The largest 7-digit number is:", "99,99,999", ["1,00,00,000", "9,99,999", "99,99,990"], "one less than one crore"),
 M4("10 lakh is called ___ in the international system.", "one million", ["one billion", "ten million", "one hundred thousand"], "1 million = 10,00,000"),
 M4("One crore is equal to ___ in the international system.", "ten million", ["one million", "one billion", "hundred million"], "1,00,00,000 = 10 million"),
 M4("If we add 1 to the largest 5-digit number we get:", "1,00,000", ["99,999", "10,00,000", "1,000"], "99,999 + 1"),
 M4("How many days are there in 100 years, ignoring leap years?", "36,500", ["3,650", "3,65,000", "35,600"], "365 × 100"),
]
# A: arithmetic with large numbers (8)
for a, b in [(7432000, 1568000), (12500000, 7500000), (3456000, 1234000), (9000000, 4750000)]:
    A.append(M4(f"{ind(a)} + {ind(b)} =", ind(a + b), [ind(a + b + 100000), ind(a + b - 10000), ind(abs(a - b))], "add place by place"))
for a, b in [(9000000, 2500000), (10000000, 3456000)]:
    A.append(M4(f"{ind(a)} − {ind(b)} =", ind(a - b), [ind(a - b + 100000), ind(a - b - 10000), ind(a + b)], "subtract carefully with borrowing"))
for a, b in [(250, 40000), (125, 8000)]:
    A.append(M4(f"{a} × {ind(b)} =", ind(a * b), [ind(a * b * 10), ind(a * b // 10), ind(a * b + b)], "multiply, then place the commas"))
# A: estimation / rounding (6)
for n in [4873261, 6149999, 2506000]:
    r = round(n, -5)
    A.append(M4(f"{ind(n)} rounded to the nearest lakh is:", ind(r), [ind(r + 100000), ind(r - 100000), ind(round(n, -4))], "look at the ten-thousands digit"))
A += [
 M4("Estimate: 4,98,000 + 2,01,000 is about:", "7,00,000", ["6,00,000", "8,00,000", "5,00,000"], "5,00,000 + 2,00,000"),
 M4("A road is 49,950 m long. To the nearest thousand it is:", "50,000 m", ["49,000 m", "49,900 m", "51,000 m"], "round up"),
 M4("Which of these is an approximate value?", "The village has about 3,000 people", ["Our class has 42 students", "A week has 7 days", "A triangle has 3 sides"], "'about' signals approximation"),
]
A += [
 M4("The number of zeros in one crore is:", "7", ["5", "6", "8"], "1,00,00,000"),
 M4("1,00,000 − 1 equals:", "99,999", ["9,99,999", "99,990", "1,00,001"], "largest 5-digit number"),
 M4("The comma after the first three digits from the right separates the:", "hundreds from thousands", ["thousands from lakhs", "lakhs from crores", "tens from hundreds"], "Indian system groups 3 then 2, 2"),
]
A = A[:40]
# B
B = [
 Q("Write 5,06,04,030 in words.", "Five crore six lakh four thousand thirty (2).", "2"),
 Q("Write ‘two crore five lakh sixty thousand’ in figures.", "2,05,60,000 (2).", "2"),
 Q("How many lakhs make one crore? How many thousands make one lakh?", "100 lakh (1); 100 thousand (1).", "1+1"),
 Q("What is the largest 6-digit number? What do we get on adding 1 to it?", "9,99,999 (1); 10,00,000 (1).", "1+1"),
 Q("Round 7,48,630 to the nearest ten thousand.", "7,50,000 (2).", "2"),
 Q("What is the difference between exact and approximate values? Give one example of each.", "An exact value is the true count (e.g. 36 students) (1); an approximate value is a nearby rounded figure (about 3 lakh people) (1).", "1+1"),
 Q("Find 3,45,000 + 2,67,500.", "6,12,500 (2).", "2"),
 Q("A school has 1,250 students. How many students are there in 400 such schools?", "1,250 × 400 = 5,00,000 (2).", "2"),
 Q("Write the place value of 6 in 36,25,481 and the face value.", "Place value 6,00,000 (lakhs place) (1); face value 6 (1).", "1+1"),
 Q("Express 12,00,000 in the international system.", "1.2 million = 1,200,000 (2).", "2"),
 Q("A seed bank has 1,00,000 seeds packed 250 per packet. How many packets?", "1,00,000 ÷ 250 = 400 (2).", "2"),
 Q("Estimate 9,87,000 − 4,02,000 by rounding to the nearest lakh.", "10,00,000 − 4,00,000 = 6,00,000 (2).", "2"),
 Q("How many seconds are there in one day? Give your answer in the Indian system.", "24 × 60 × 60 = 86,400 (2).", "2"),
 Q("Arrange in ascending order: 54,30,000; 5,43,000; 53,40,000; 5,34,000.", "5,34,000 < 5,43,000 < 53,40,000 < 54,30,000 (2).", "2"),
 Q("Write the number that is 1 lakh more than 9,45,600.", "10,45,600 (2).", "2"),
 Q("The population of a town is 2,48,750. Round it to the nearest thousand.", "2,49,000 (2).", "2"),
]
C = [
 Q("Write 4,07,06,059 in words and state the place value of the digit 7.", "Four crore seven lakh six thousand fifty nine (2); the place value of 7 (lakhs place) is 7,00,000 (1).", "2+1"),
 Q("Find the sum of 8,45,67,320 and 1,54,32,680 and write it in words.", "10,00,00,000 (1); ten crore (2).", "1+2"),
 Q("One person eats 3 varieties of rice every day. Will they taste 1 lakh varieties in a lifetime of 100 years? Explain.", "Days in 100 years ≈ 36,500 (1); 36,500 × 3 = 1,09,500 (1); yes, just over 1 lakh (1).", "1+1+1"),
 Q("A stadium has 1,32,000 seats. 3 stands have 28,500 seats each. How many seats are in the other stands?", "3 × 28,500 = 85,500 (1.5); 1,32,000 − 85,500 = 46,500 (1.5).", "1½+1½"),
 Q("Round 38,47,625 to the nearest (i) ten thousand (ii) lakh (iii) ten lakh.", "(i) 38,50,000 (1); (ii) 38,00,000 (1); (iii) 40,00,000 (1).", "1+1+1"),
 Q("Estimate the product 4,980 × 302 and compare it with the exact product.", "5,000 × 300 = 15,00,000 (1); exact = 15,03,960 (1); estimate is close (1).", "1+1+1"),
 Q("A truck carries 1,250 kg per trip. How many trips are needed to carry 5 lakh kg?", "5,00,000 ÷ 1,250 = 400 trips (3).", "3"),
 Q("Explain with an example why 1 lakh may be a ‘big’ number in one situation and ‘small’ in another.", "1 lakh days = about 274 years, which is huge (1.5); 1 lakh people can sit in a stadium, which is a small area (1.5).", "1½+1½"),
 Q("The population of a town was 75,000 in 2011 and 1,06,000 in 2024. Find the increase and say by how much it exceeds 1 lakh.", "Increase = 31,000 (1.5); exceeds 1 lakh by 6,000 (1.5).", "1½+1½"),
 Q("Write the following in the Indian system: (a) 25,000,000 (b) 1,200,500.", "(a) 2,50,00,000 (1.5); (b) 12,00,500 (1.5).", "1½+1½"),
 Q("A lakh coins of ₹1 are stacked, each 2 mm thick. How tall is the stack in metres?", "1,00,000 × 2 mm = 2,00,000 mm (1.5); = 200 m (1.5).", "1½+1½"),
 Q("Find the number of minutes in a year of 365 days and round it to the nearest ten thousand.", "365 × 24 × 60 = 5,25,600 (2); ≈ 5,30,000 (1).", "2+1"),
 Q("A shop sold goods worth ₹3,45,000, ₹2,78,500 and ₹4,06,250 in three months. Find the total.", "3,45,000 + 2,78,500 + 4,06,250 (1); = 10,29,750 (2).", "1+2"),
 Q("Find the missing digit: 4,3_,500 is a multiple of 500 whenever the blank is any digit. Why?", "Divisibility by 500 depends only on the last three digits 500 (2); so any digit works (1).", "2+1"),
 Q("A tank holds 2,50,000 litres. Pumps fill 5,000 litres per hour. How many hours to fill it?", "2,50,000 ÷ 5,000 = 50 hours (3).", "3"),
 Q("State the pattern: 9 × 1 = 9, 99 × 1 = 99; 99 × 99 = ? Continue it for 999 × 999.", "99 × 99 = 9,801 (1.5); 999 × 999 = 9,98,001 (1.5).", "1½+1½"),
 Q("Write the numbers 10, 100, 1000 … up to 1 crore using powers of 10 notation.", "10¹, 10², 10³, … 10⁷ = 1 crore (3).", "3"),
 Q("Compare 7,05,000 and 70,500 by saying how many times the first is the second.", "7,05,000 ÷ 70,500 = 10 times (3).", "3"),
 Q("A farmer earns ₹2,45,000 per year. How much does he earn in 12 years?", "2,45,000 × 12 = 29,40,000 (3).", "3"),
 Q("Put commas and read: 120500000.", "12,05,00,000 (1.5); twelve crore five lakh (1.5).", "1½+1½"),
 Q("The distance from Earth to the Moon is about 3,84,400 km. Round it to the nearest ten thousand and to the nearest lakh.", "3,80,000 km (1.5); 4,00,000 km (1.5).", "1½+1½"),
 Q("Which is larger: 98,76,543 or 98,67,543? Give a reason.", "98,76,543 (1); compare lakhs digit: 7 > 6 (2).", "1+2"),
 Q("A book has 240 pages. A library has 12,500 such books. Find the total pages.", "240 × 12,500 = 30,00,000 (3).", "3"),
 Q("Round 6,49,999 and 6,50,000 to the nearest lakh. What do you notice?", "6,00,000 and 7,00,000 (2); a tiny change at the halfway mark changes the rounding (1).", "2+1"),
]
D = [
 Q("(i) Write 3,05,40,206 in words. (ii) Write the place value of each digit 0 and 5. (iii) Add 1,00,000 to it. (iv) Round it to the nearest lakh.", "(i) Three crore five lakh forty thousand two hundred six (1). (ii) The 5 is in the lakhs place: 5,00,000; the zeros have place value 0 (1). (iii) 3,06,40,206 (1). (iv) 3,05,00,000 (2).", "1+1+1+2"),
 Q("(i) How many lakhs make a crore? (ii) How many seconds are in a day? (iii) How many days in 274 years approximately make 1 lakh days? (iv) Why is the number of days in a lifetime less than a lakh?", "(i) 100 (1). (ii) 86,400 (1). (iii) 1,00,000 ÷ 365 ≈ 274 (1). (iv) 100 years × 365 = 36,500 < 1,00,000 (2).", "1+1+1+2"),
 Q("<b>Case study:</b> A city has 12,48,000 people. Of these, 2,35,000 are children, 7,86,500 are adults and the rest are senior citizens. (i) Find the number of senior citizens. (ii) Write it in words. (iii) Round the city population to the nearest lakh. (iv) If 40 lakh litres of water is supplied per day, find the litres per person to the nearest litre.", "(i) 12,48,000 − (2,35,000 + 7,86,500) = 2,26,500 (2). (ii) Two lakh twenty six thousand five hundred (1). (iii) 12,00,000 (1). (iv) 40,00,000 ÷ 12,48,000 ≈ 3 L (1).", "2+1+1+1"),
 Q("(i) Estimate 49,800 × 2,010 by rounding. (ii) Find the exact product. (iii) Find the difference between them. (iv) Write the exact product in words.", "(i) 50,000 × 2,000 = 10,00,00,000 (1). (ii) 10,00,98,000 (2). (iii) 98,000 (1). (iv) Ten crore ninety eight thousand (1).", "1+2+1+1"),
 Q("(i) Show that 1 crore = 100 lakh = 10,000 thousand. (ii) Express 7 crore in thousands. (iii) How many lakh in 3.5 crore? (iv) Write 3.5 crore in figures.", "(i) 1,00,00,000 ÷ 1,00,000 = 100; ÷ 1,000 = 10,000 (2). (ii) 70,000 thousand (1). (iii) 350 lakh (1). (iv) 3,50,00,000 (1).", "2+1+1+1"),
 Q("(i) Round 8,46,725 to the nearest thousand, ten thousand and lakh. (ii) Which rounding is closest to the actual number? (iii) What is the error in the lakh rounding?", "(i) 8,47,000; 8,50,000; 8,00,000 (3). (ii) Nearest thousand (1). (iii) 46,725 (1).", "3+1+1"),
 Q("<b>Case study:</b> A stadium seats 1,32,000 and ticket price is ₹450. (i) Find the money from a full house. (ii) Round it to the nearest lakh. (iii) Express it in crores. (iv) If 4,500 seats were empty, find the loss.", "(i) 1,32,000 × 450 = 5,94,00,000 (2). (ii) 5,94,00,000 (already a lakh multiple) (1). (iii) 5.94 crore (1). (iv) 4,500 × 450 = 20,25,000 (1).", "2+1+1+1"),
 Q("(i) Find 1,000 × 1,000. (ii) Name the result in the Indian and international system. (iii) Find the number of lakhs in a million. (iv) How many millions in a crore?", "(i) 10,00,000 (1). (ii) Ten lakh = one million (1). (iii) 10 lakh (1). (iv) 10 million (2).", "1+1+1+2"),
 Q("(i) Divide 5,00,00,000 by 25,000. (ii) Interpret the answer. (iii) Is the answer larger than a lakh? (iv) Check by multiplication.", "(i) 2,000 (2). (ii) 2,000 groups of 25,000 (1). (iii) No (1). (iv) 2,000 × 25,000 = 5,00,00,000 (1).", "2+1+1+1"),
 Q("(i) State the largest and smallest 8-digit numbers. (ii) Find their difference. (iii) Write the smallest number in words.", "(i) 9,99,99,999 and 1,00,00,000 (2). (ii) 8,99,99,999 (1). (iii) One crore (2).", "2+1+2"),
 Q("<b>Case study:</b> A farmer's field grows 2,400 kg of rice per acre. He has 35 acres, and sells at ₹30 per kg. (i) Total rice. (ii) Sale amount. (iii) Express in lakhs. (iv) Estimate if each acre gave 2,500 kg.", "(i) 84,000 kg (1). (ii) ₹25,20,000 (2). (iii) 25.2 lakh (1). (iv) ≈ 35 × 2,500 × 30 = ₹26,25,000 (1).", "1+2+1+1"),
 Q("(i) Complete the pattern: 11 × 11, 111 × 111. (ii) Predict 1111 × 1111. (iii) Explain why it works.", "(i) 121; 12,321 (2). (ii) 12,34,321 (2). (iii) Digits add by place and counts rise then fall (1).", "2+2+1"),
 Q("(i) Write 9 crore 9 lakh 9 thousand 9 hundred 9 in figures. (ii) Round it to the nearest crore. (iii) How much must be added to reach the next crore (10,00,00,000)?", "(i) 9,09,09,909 (2). (ii) 9,00,00,000 (1). (iii) 10,00,00,000 − 9,09,09,909 = 90,90,091 (2).", "2+1+2"),
 Q("(i) A bus covers 1,000 km a week. How far in a year (52 weeks)? (ii) In 10 years? (iii) Compare with 1 lakh km. (iv) Express in international system.", "(i) 52,000 km (1). (ii) 5,20,000 km (1). (iii) 5.2 times (1). (iv) 520,000 km (2).", "1+1+1+2"),
 Q("(i) Add 3,48,62,500; 1,25,37,500 and 6,26,00,000. (ii) Write the sum in words. (iii) Is the sum above 10 crore?", "(i) 11,00,00,000 (2). (ii) Eleven crore (1). (iii) Yes (2).", "2+1+2"),
 Q("(i) Explain what ‘exact’ and ‘approximate’ mean using the census population of your town. (ii) When is rounding preferred? (iii) Give one case where an exact number is needed.", "(i) Exact is the true count; approximate is rounded (2). (ii) For quick reporting and estimates (1). (iii) Money in a bank account or medicine doses (2).", "2+1+2"),
 Q("(i) A river is 2,525 km long. A canal is 1,25,000 m long. Which is longer? (ii) By how much (in km)? (iii) Express both in metres.", "(i) 125 km vs 2,525 km: river (2). (ii) 2,400 km (1). (iii) 25,25,000 m and 1,25,000 m (2).", "2+1+2"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
