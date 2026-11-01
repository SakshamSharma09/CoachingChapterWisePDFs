import random
from decimal import Decimal as Dc
from c7maths.h import *
R = random.Random(703)
def f(x): 
    s = format(Dc(x).normalize(), 'f'); return s
A = []; B = []; C = []; D = []
# place value (6)
for n, d in [("34.567", "5"), ("128.049", "4"), ("7.806", "8"), ("0.352", "3"), ("56.931", "9"), ("9.074", "7")]:
    i = n.index(d); dot = n.index(".")
    pw = dot - i - 1 if i < dot else dot - i
    val = Dc(d) * Dc(10) ** pw
    nm = {-1: "tenths", -2: "hundredths", -3: "thousandths", 0: "ones", 1: "tens", 2: "hundreds"}[pw]
    A.append(M4(f"The value of the digit {d} in {n} is:", f(val), [f(val * 10), f(val / 10), f(Dc(d)), f(val * 100), f(val / 100)], f"{d} is in the {nm} place"))
# addition / subtraction (8)
for a, b in [("12.45", "7.8"), ("0.75", "0.6"), ("34.09", "5.91"), ("8.5", "3.75")]:
    v = Dc(a) + Dc(b)
    A.append(M4(f"{a} + {b} =", f(v), [f(v + Dc("0.1")), f(v - Dc("0.01")), f(v + 1)], "align the decimal points"))
for a, b in [("15.6", "7.85"), ("20", "6.45"), ("9.03", "4.5"), ("50.2", "18.75")]:
    v = Dc(a) - Dc(b)
    A.append(M4(f"{a} − {b} =", f(v), [f(v + Dc("0.1")), f(v - Dc("0.01")), f(Dc(b) - Dc(a) if Dc(b) > Dc(a) else v + 1)], "align the decimal points and borrow"))
# comparison (5)
for a, b in [("0.5", "0.45"), ("3.07", "3.7"), ("6.25", "6.205"), ("0.09", "0.1"), ("12.3", "12.30")]:
    big = max(Dc(a), Dc(b))
    if Dc(a) == Dc(b):
        A.append(M4(f"Which statement is true for {a} and {b}?", "They are equal", ["The first is greater", "The second is greater", "Cannot be compared"], "a zero at the end after the decimal point does not change the value")); continue
    A.append(M4(f"The greater number is:", f(big), [f(min(Dc(a), Dc(b))), "both are equal", f(big / 10)], "compare digit by digit from the left"))
# conversions (8)
A += [
 M4("5 cm 3 mm in centimetres is:", "5.3 cm", ["5.03 cm", "53 cm", "0.53 cm"], "1 mm = 0.1 cm"),
 M4("2 m 45 cm in metres is:", "2.45 m", ["24.5 m", "2.045 m", "245 m"], "1 cm = 0.01 m"),
 M4("3 kg 250 g in kilograms is:", "3.25 kg", ["3.025 kg", "32.5 kg", "3.5 kg"], "250 g = 0.25 kg"),
 M4("₹7 and 5 paise is written as:", "₹7.05", ["₹7.5", "₹75", "₹0.75"], "5 paise = ₹0.05"),
 M4("0.6 km in metres is:", "600 m", ["60 m", "6,000 m", "6 m"], "1 km = 1000 m"),
 M4("1.5 litres in millilitres is:", "1,500 mL", ["150 mL", "15 mL", "15,000 mL"], "1 L = 1000 mL"),
 M4("125 g in kilograms is:", "0.125 kg", ["1.25 kg", "0.0125 kg", "12.5 kg"], "divide by 1000"),
 M4("37 mm in centimetres is:", "3.7 cm", ["0.37 cm", "37 cm", "370 cm"], "divide by 10"),
]
# concepts (11)
A += [
 M4("One tenth is written in decimal form as:", "0.1", ["0.01", "1.0", "10"], "1/10"),
 M4("One hundredth is written as:", "0.01", ["0.1", "0.001", "1.01"], "1/100"),
 M4("The fraction 3/4 as a decimal is:", "0.75", ["0.34", "0.43", "7.5"], "3 ÷ 4"),
 M4("The decimal 0.125 as a fraction is:", "1/8", ["1/12", "1/5", "125/10"], "125/1000"),
 M4("Which decimal lies between 2.3 and 2.4?", "2.35", ["2.5", "2.25", "2.45"], "2.30 < 2.35 < 2.40"),
 M4("Multiplying 4.56 by 10 gives:", "45.6", ["456", "0.456", "4.056"], "the point moves one place right"),
 M4("Dividing 82.5 by 100 gives:", "0.825", ["8.25", "8,250", "0.0825"], "the point moves two places left"),
 M4("In 6.347 the digit in the hundredths place is:", "4", ["3", "7", "6"], "6 . 3 4 7"),
 M4("Which is equal to 0.5?", "0.50", ["0.05", "5.0", "0.005"], "trailing zero adds nothing"),
 M4("The smallest number among 0.3, 0.03, 0.303 is:", "0.03", ["0.3", "0.303", "all are equal"], "compare place by place"),
 M4("0.7 + 0.3 equals:", "1", ["0.10", "1.1", "0.21"], "7 tenths + 3 tenths = 1"),
]
A += [
 M4("0.25 + 0.75 =", "1", ["0.100", "10", "0.99"], "25 + 75 hundredths = 100 hundredths"),
 M4("Which of these is a decimal fraction?", "3/10", ["3/7", "2/3", "5/9"], "denominator is a power of 10"),
]
A = A[:40]
B = [
 Q("Write 4 tenths and 5 hundredths as a decimal.", "0.45 (2).", "2"),
 Q("Write 25/100 and 3/5 in decimal form.", "0.25 (1); 0.6 (1).", "1+1"),
 Q("Find 6.45 + 3.8.", "10.25 (2).", "2"),
 Q("Find 10 − 3.76.", "6.24 (2).", "2"),
 Q("Convert 4 km 75 m into kilometres.", "4.075 km (2).", "2"),
 Q("Convert 2.5 kg into grams and ₹3.40 into paise.", "2,500 g (1); 340 paise (1).", "1+1"),
 Q("Write the decimal 3.206 in expanded form.", "3 + 2/10 + 0/100 + 6/1000 (2).", "2"),
 Q("Which is greater, 0.8 or 0.75? Give a reason.", "0.8; 0.80 > 0.75 (2).", "2"),
 Q("Arrange in ascending order: 0.5, 0.05, 0.55, 0.505.", "0.05 < 0.5 < 0.505 < 0.55 (2).", "2"),
 Q("Find a decimal between 1.4 and 1.5.", "1.45 (any such answer) (2).", "2"),
 Q("Why do we need decimals? Give one example.", "To measure parts smaller than a unit (1); e.g. length 3.5 cm or ₹2.50 (1).", "1+1"),
 Q("Multiply 3.25 by 100.", "325 (2).", "2"),
 Q("Divide 47.5 by 10.", "4.75 (2).", "2"),
 Q("Express 0.375 as a fraction in the lowest terms.", "375/1000 = 3/8 (2).", "2"),
 Q("A ribbon is 2.5 m long; 80 cm is cut off. How much remains?", "250 cm − 80 cm = 170 cm = 1.7 m (2).", "2"),
 Q("Round 4.678 to one decimal place.", "4.7 (2).", "2"),
]
C = [
 Q("Add 12.6, 8.45 and 0.075.", "Align decimal points (1); sum = 21.125 (2).", "1+2"),
 Q("Subtract 18.75 from 40.2.", "40.20 − 18.75 (1); = 21.45 (2).", "1+2"),
 Q("A bag has 3 kg 450 g of rice and 2 kg 75 g of wheat. Find the total weight in kg.", "3.45 + 2.075 (1.5); = 5.525 kg (1.5).", "1½+1½"),
 Q("Write the place value chart for 253.714.", "2 hundreds, 5 tens, 3 ones (1.5); 7 tenths, 1 hundredth, 4 thousandths (1.5).", "1½+1½"),
 Q("Convert 7/20, 9/25 and 3/8 to decimals.", "0.35 (1); 0.36 (1); 0.375 (1).", "1+1+1"),
 Q("Arrange 6.07, 6.7, 6.007, 6.707 in descending order.", "6.707 > 6.7 > 6.07 > 6.007 (3).", "3"),
 Q("A pencil is 17.35 cm long and a pen is 14.9 cm long. How much longer is the pencil?", "17.35 − 14.9 = 2.45 cm (3).", "3"),
 Q("The price of milk is ₹52.50 per litre. Find the cost of 4 litres.", "4 × 52.50 (1.5); = ₹210 (1.5).", "1½+1½"),
 Q("Express 3 m 7 cm, 45 mm and 2 km 50 m in the units shown: m, cm, km.", "3.07 m (1); 4.5 cm (1); 2.05 km (1).", "1+1+1"),
 Q("Show 0.3 and 0.30 are equal on the number line idea or with fractions.", "3/10 = 30/100 (2); hence equal (1).", "2+1"),
 Q("Round 56.4783 to (i) two decimal places (ii) the nearest whole number.", "(i) 56.48 (1.5); (ii) 56 (1.5).", "1½+1½"),
 Q("The temperature rose from 36.4 °C to 38.9 °C. Find the rise.", "38.9 − 36.4 = 2.5 °C (3).", "3"),
 Q("Find 0.2 × 0.3 by converting to fractions.", "2/10 × 3/10 = 6/100 (1.5); = 0.06 (1.5).", "1½+1½"),
 Q("Sarita runs 1.25 km every day. How far does she run in 8 days?", "1.25 × 8 = 10 km (3).", "3"),
 Q("Write four decimals between 0.1 and 0.2.", "0.11, 0.12, 0.15, 0.19 (any four) (3).", "3"),
 Q("A can holds 2.5 L. Pouring 750 mL leaves how much?", "2,500 − 750 = 1,750 mL (1.5); = 1.75 L (1.5).", "1½+1½"),
 Q("Divide 6.3 by 9 and check by multiplication.", "0.7 (2); 0.7 × 9 = 6.3 (1).", "2+1"),
 Q("A rectangle is 4.2 m by 3.5 m. Find its area and perimeter.", "Area 14.7 m² (1.5); perimeter 15.4 m (1.5).", "1½+1½"),
 Q("Why is 0.4 greater than 0.399? Explain.", "0.400 vs 0.399 (1.5); 4 tenths exceed 3 tenths (1.5).", "1½+1½"),
 Q("Write 0.0075 in words and as a fraction.", "Seventy five ten-thousandths (1.5); 75/10000 = 3/400 (1.5).", "1½+1½"),
 Q("Sum of two decimals is 8.5. One is 3.275. Find the other.", "8.5 − 3.275 = 5.225 (3).", "3"),
 Q("A shopkeeper buys 12.5 m cloth and sells 9.75 m. How much is left?", "12.5 − 9.75 = 2.75 m (3).", "3"),
 Q("Rahul weighs 42.5 kg and Mohan 39.75 kg. Find the difference and the combined weight.", "2.75 kg (1.5); 82.25 kg (1.5).", "1½+1½"),
 Q("Round ₹39.85 to the nearest rupee and to the nearest 10 rupees.", "₹40 (1.5); ₹40 (1.5).", "1½+1½"),
]
D = [
 Q("(i) Write the place values of all digits of 508.693. (ii) Write it in expanded form. (iii) Write it in words.", "(i) 5 hundreds, 0 tens, 8 ones, 6 tenths, 9 hundredths, 3 thousandths (2). (ii) 500 + 8 + 6/10 + 9/100 + 3/1000 (2). (iii) Five hundred eight and six hundred ninety three thousandths (1).", "2+2+1"),
 Q("(i) Add 45.6, 3.075 and 12.9. (ii) Subtract 8.456 from 20. (iii) Check (ii) by adding.", "(i) 61.575 (2). (ii) 11.544 (2). (iii) 11.544 + 8.456 = 20 (1).", "2+2+1"),
 Q("<b>Case study:</b> A tailor buys 3.5 m of cloth at ₹120 per m, 2.25 m at ₹80 per m and 1.75 m at ₹60 per m. (i) Total length. (ii) Cost of each piece. (iii) Total cost. (iv) Average cost per metre.", "(i) 7.5 m (1). (ii) ₹420, ₹180, ₹105 (2). (iii) ₹705 (1). (iv) ₹94 (1).", "1+2+1+1"),
 Q("(i) Convert 5 km 40 m, 3 kg 8 g and ₹7 and 5 paise to decimals of km, kg, rupees. (ii) Add the first two as numbers. (iii) State why units must match.", "(i) 5.04 km, 3.008 kg, ₹7.05 (3). (ii) 8.048 (1). (iii) Adding different units gives wrong sums (1).", "3+1+1"),
 Q("(i) Compare 0.58 and 0.6 and 0.059. (ii) Order from the greatest. (iii) Insert one decimal between the greatest two.", "(i) 0.58 < 0.6; 0.059 is smallest (2). (ii) 0.6 > 0.58 > 0.059 (2). (iii) 0.59 (1).", "2+2+1"),
 Q("<b>Case study:</b> A 100 m race: Anu 12.46 s, Bela 12.4 s, Chitra 12.405 s, Dia 12.5 s. (i) Who wins? (ii) Order the girls. (iii) Difference between first and last. (iv) Round Anu's time to one decimal.", "(i) Bela (12.400) (1). (ii) Bela, Chitra, Anu, Dia (2). (iii) 0.1 s (1). (iv) 12.5 s (1).", "1+2+1+1"),
 Q("(i) Express 2/5, 7/8 and 11/20 as decimals. (ii) Order them. (iii) Add them.", "(i) 0.4, 0.875, 0.55 (2). (ii) 0.875 > 0.55 > 0.4 (1). (iii) 1.825 (2).", "2+1+2"),
 Q("(i) Multiply 2.35 by 10, 100, 1000. (ii) Divide 6,450 by 10, 100, 1000. (iii) State the rule.", "(i) 23.5; 235; 2,350 (1.5). (ii) 645; 64.5; 6.45 (1.5). (iii) Point moves right/left by number of zeros (2).", "1½+1½+2"),
 Q("(i) A rope is 15.5 m. Pieces of 1.25 m are cut. How many pieces? (ii) What is left? (iii) Express leftover in cm.", "(i) 12 pieces (2). (ii) 0.5 m (2). (iii) 50 cm (1).", "2+2+1"),
 Q("<b>Case study:</b> A petrol pump sells 45.5 L to a car, 7.25 L to a scooter and 12.75 L to an auto. Petrol costs ₹98.40 per litre. (i) Total litres. (ii) Cost for the car. (iii) Cost for the scooter. (iv) Difference of costs.", "(i) 65.5 L (1). (ii) ₹4,477.20 (2). (iii) ₹713.40 (1). (iv) ₹3,763.80 (1).", "1+2+1+1"),
 Q("(i) Round 7.8549 to 1, 2, 3 decimal places. (ii) Find the rounding error for each.", "(i) 7.9; 7.85; 7.855 (3). (ii) 0.0451, 0.0049, 0.0001 (2).", "3+2"),
 Q("(i) Find 0.4 + 0.04 + 0.004. (ii) Find 1 − 0.001. (iii) Find 5 × 0.25 × 4.", "(i) 0.444 (1.5). (ii) 0.999 (1.5). (iii) 5 (2).", "1½+1½+2"),
 Q("(i) How many 0.25 L cups fill a 5 L jug? (ii) How many 0.2 kg packets from 8.6 kg flour? (iii) Explain by division.", "(i) 20 (2). (ii) 43 (2). (iii) 5 ÷ 0.25 and 8.6 ÷ 0.2 (1).", "2+2+1"),
 Q("<b>Case study:</b> A tank has 250.5 L. In the morning 48.75 L is used, in the evening 62.4 L. (i) Total used. (ii) Left. (iii) Fraction used (approx). (iv) Is it more than half?", "(i) 111.15 L (1). (ii) 139.35 L (2). (iii) ≈ 0.44 (1). (iv) No (1).", "1+2+1+1"),
 Q("(i) Express 3 m 5 cm, 7 mm and 2 km 60 m as m. (ii) Add all. (iii) Round to one decimal place.", "(i) 3.05 m; 0.007 m; 2,060 m (2). (ii) 2,063.057 m (2). (iii) 2,063.1 m (1).", "2+2+1"),
 Q("(i) A decimal is between 4.2 and 4.3 and has two digits after the point. Give three. (ii) Which has the greater value? 4.25 or 4.205.", "(i) 4.21, 4.25, 4.29 (3). (ii) 4.25 (2).", "3+2"),
]
D = D[:16]
SETS, POOL = build(A, B, C, D)
