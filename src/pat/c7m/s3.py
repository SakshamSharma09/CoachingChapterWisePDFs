from lib8 import *
import mfigs as MF
from fractions import Fraction as Fr
# --- computed answers ---
assert 100 - 20*3 + 4//2 == 42 and 2*(30 - (4+6)//2) == 50
assert abs(0.8*0.5 - 0.4) < 1e-9 and abs(42.5*3.2 - 136) < 1e-9 and abs(0.36*0.25 - 0.09) < 1e-9
assert 30 + 12*7 == 114 and 360 - (90+110+100) == 60 and 5*15-20 == 3*15+10 == 55
assert Fr(5, 2) / Fr(1, 6) == 15
fib = [1, 2]
while len(fib) < 8: fib.append(fib[-1]+fib[-2])
assert fib == [1, 2, 3, 5, 8, 13, 21, 34]
assert round(7.864235) == 8 and 78642350 // 100000 == 786
assert Fr(90)*Fr(2, 3)*Fr(1, 4) == 15 and Fr(15, 4)/Fr(5, 8) == 6
assert (30, 60, 90) == (30, 2*30, 30+60) and 4+5-1 == 8
assert abs(5.5*105.4 - 579.7) < 1e-9
assert Fr(2, 3)*Fr(3, 8) == Fr(1, 4) and Fr(4, 5)/Fr(2, 15) == 6 and Fr(3, 2)*Fr(8, 3) == 4 and Fr(9)/Fr(3, 4) == 12
assert Fr(1, 3)*Fr(3, 5) == Fr(1, 5) and Fr(2, 5)+Fr(1, 5)*0 == Fr(2, 5) and 120/Fr(2, 5) == 300
assert 10+12+14+16 == 52 and 47+74 == 121 == 11*11
assert 11111*11111 == 123454321 and 12321 == 9*1369
assert 132000*800 == 105600000 and 10**7/132000 > 75
assert Fr(3, 5)*Fr(5, 6) == Fr(1, 2) and Fr(5, 6)-Fr(1, 2) == Fr(1, 3) and Fr(1, 3)/Fr(1, 12) == 4 and Fr(1, 3)+Fr(2, 3) == 1
q1 = mcqgroup([
 m("The smallest 8-digit number is:", "1,00,00,000", ["10,00,000", "99,99,999", "1,00,000"], "The smallest 8-digit number is 1 crore = 1,00,00,000."),
 m("How many zeros are there in one crore?", "7", ["5", "6", "8"], "1 crore = 1,00,00,000 = 10<sup>7</sup>."),
 m("The value of 100 − 20 × 3 + 4 ÷ 2 is:", "42", ["242", "82", "44"], "Multiplication and division first: 20 × 3 = 60 and 4 ÷ 2 = 2; then 100 − 60 + 2 = 42."),
 m("3 hundredths + 5 thousandths equals:", "0.035", ["0.35", "0.0035", "0.08"], "0.03 + 0.005 = 0.035."),
 m("The product 0.8 × 0.5 is:", "0.4", ["4", "0.04", "1.3"], "8 × 5 = 40 and there are two decimal places in all, so 0.40 = 0.4."),
 m("Which of the following is a like term of 5xy?", "7xy", ["5x", "5y", "x²y"], "Like terms have the same letter part, here xy."),
 m("The perimeter of a square of side 2.5 cm is:", "10 cm", ["6.25 cm", "5 cm", "12.5 cm"], "4 × 2.5 = 10 cm. (6.25 cm² is the area.)"),
 m("The supplement of an angle of 125° is:", "55°", ["35°", "65°", "235°"], "180° − 125° = 55°."),
 m("Two lines intersect so that vertically opposite angles are (5x − 20)° and (3x + 10)°. The value of x is:", "15", ["5", "10", "30"], "Vertically opposite angles are equal: 5x − 20 = 3x + 10 ⇒ 2x = 30 ⇒ x = 15."),
 m("Which of these numbers is divisible by 9?", "738", ["734", "736", "740"], "7 + 3 + 8 = 18, a multiple of 9. The other digit sums are 14, 16 and 11."),
 m("A triangle can have at most how many obtuse angles?", "One", ["Two", "Three", "None"], "Two obtuse angles would already add up to more than 180°."),
 m("How many pieces of 1/6 m can be cut from a ribbon 2 1/2 m long?", "15", ["12", "5/12", "25"], "5/2 ÷ 1/6 = 5/2 × 6 = 15.")])
b = [
 sa("Round 7,86,42,350 (i) to the nearest crore and (ii) to the nearest lakh.", 2, "(i) 7.86 crore ≈ 8 crore = 8,00,00,000 (1 mark)<br>(ii) 786.4235 lakh ≈ 786 lakh = 7,86,00,000 (1 mark)"),
 sa("Evaluate: 2 × [30 − (4 + 6) ÷ 2].", 2, "Innermost bracket: 4 + 6 = 10; 10 ÷ 2 = 5 (1 mark)<br>2 × (30 − 5) = 2 × 25 = 50 (1 mark)"),
 OR(sa("A bus travels at a steady speed of 42.5 km per hour. How far does it go in 3.2 hours?", 2, "Distance = 42.5 × 3.2 (1 mark) = 136 km (1 mark)"),
    sa("Find 0.36 × 0.25.", 2, "36 × 25 = 900 (1 mark); four decimal places in all, so 0.0900 = 0.09 (1 mark)")),
 sa("An auto-rickshaw charges a fixed ₹ 30 plus ₹ 12 for each kilometre. Write an expression for the fare for k km and find the fare for 7 km.", 2, "Fare = 30 + 12k (1 mark)<br>k = 7: 30 + 84 = ₹ 114 (1 mark)"),
 sa("Four angles meet at a point O. Three of them measure 90°, 110° and 100°. Find the fourth angle.", 2, "Angles at a point add up to 360° (1 mark)<br>x = 360° − (90° + 110° + 100°) = 60° (1 mark)"),
 sa("Write the first eight terms of the Virahanka (Fibonacci) type sequence that starts with 1, 2, and in which each term is the sum of the two terms before it.", 2, "1, 2, 3, 5, 8, 13, 21, 34 (2 marks; 1 mark if one slip occurs)")]
c = [
 OR(sa("A tank of capacity 90 litres is 2/3 full. 3/4 of the water in it is used for watering plants. How much water is left in the tank?", 3, "Water in tank = 2/3 × 90 = 60 L (1 mark)<br>Used = 3/4 × 60 = 45 L (1 mark)<br>Left = 60 − 45 = 15 L (1 mark)"),
    sa("Divide: 3 3/4 ÷ 5/8. Verify your answer by multiplication.", 3, "3 3/4 = 15/4 (1 mark)<br>15/4 × 8/5 = 6 (1 mark)<br>Check: 6 × 5/8 = 15/4 = 3 3/4 (1 mark)")),
 OR(sa("In triangle PQR, ∠Q = 2 × ∠P and ∠R = ∠P + 60°. Find the three angles. What kind of triangle is it?", 3, "P + 2P + (P + 60) = 180 ⇒ 4P = 120 ⇒ P = 30° (1 mark)<br>∠Q = 60°, ∠R = 90° (1 mark)<br>It is a right-angled triangle (1 mark)"),
    sa("Two sides of a triangle are 4 cm and 5 cm. Between which two numbers must the third side lie? What is the greatest whole-number perimeter possible?", 3, "5 − 4 &lt; third side &lt; 5 + 4, i.e. between 1 cm and 9 cm (2 marks)<br>Greatest whole third side = 8 cm, so perimeter = 4 + 5 + 8 = 17 cm (1 mark)")),
 sa("Petrol costs ₹ 105.40 per litre. Rohit buys 5.5 litres. (i) Find the cost. (ii) He pays with a ₹ 600 note. How much change does he get?", 3, "(i) 5.5 × 105.40 (1 mark) = ₹ 579.70 (1 mark)<br>(ii) 600 − 579.70 = ₹ 20.30 (1 mark)")]
fig_tri = MF.tri("(x + 10)°", "(2x)°", "(3x − 10)°", 40, 60, 80)
fig_cor = MF.transversal("(3x + 5)°", "(5x − 35)°", 65, bot_below=True)
d = [
 OR(sa("Simplify each. (i) 2/3 × 3/8 (ii) 4/5 ÷ 2/15 (iii) 1 1/2 × 2 2/3 (iv) Find the reciprocal of 7/9 and the product of the number and its reciprocal. (v) How many pieces of cloth, each 3/4 m long, can be cut from a roll of 9 m?", 5, "(i) 6/24 = 1/4 (1 mark)<br>(ii) 4/5 × 15/2 = 6 (1 mark)<br>(iii) 3/2 × 8/3 = 4 (1 mark)<br>(iv) 9/7; 7/9 × 9/7 = 1 (1 mark)<br>(v) 9 ÷ 3/4 = 12 pieces (1 mark)"),
    sa("Rahul reads 2/5 of a book on Monday and 1/3 of the remaining part on Tuesday. (i) What fraction of the book remains after Monday? (ii) What fraction of the whole book does he read on Tuesday? (iii) What fraction is read in all? (iv) What fraction remains unread? (v) If 120 pages remain unread, how many pages does the book have?", 5, "(i) 1 − 2/5 = 3/5 (1 mark)<br>(ii) 1/3 × 3/5 = 1/5 (1 mark)<br>(iii) 2/5 + 1/5 = 3/5 (1 mark)<br>(iv) 1 − 3/5 = 2/5 (1 mark)<br>(v) 2/5 of total = 120 ⇒ total = 120 × 5/2 = 300 pages (1 mark)")),
 OR(sa("In the figure, the angles of triangle ABC are (x + 10)°, (2x)° and (3x − 10)°. (i) State the angle sum property. (ii) Find x. (iii) Find the three angles. (iv) Is the triangle acute, right or obtuse? (v) Find the exterior angle formed when side BC is extended at C (assume ∠C = (3x − 10)°).", 5, "(i) The three angles of a triangle add up to 180° (1 mark)<br>(ii) 6x = 180 ⇒ x = 30 (1 mark)<br>(iii) 40°, 60°, 80° (1 mark)<br>(iv) Acute-angled, all angles are below 90° (1 mark)<br>(v) 180° − 80° = 100° (= 40° + 60°) (1 mark)", fig=fig_tri),
    sa("In the figure, AB ∥ CD and PQ is a transversal. ∠BPQ = (3x + 5)° and the corresponding angle at Q below CD is (5x − 35)°. (i) Write the relation between the two angles. (ii) Find x. (iii) Find the measure of the angle. (iv) Find ∠DQP. (v) Find ∠CQP.", 5, "(i) Corresponding angles are equal (1 mark)<br>(ii) 3x + 5 = 5x − 35 ⇒ x = 20 (1 mark)<br>(iii) 3 × 20 + 5 = 65° (1 mark)<br>(iv) ∠DQP = 180° − 65° = 115° (co-interior) (1 mark)<br>(v) ∠CQP = 65° (alternate interior) (1 mark)", fig=fig_cor)),
 sa("(i) Write the sum of four consecutive even numbers n, n + 2, n + 4, n + 6 in its simplest form. (ii) Show that it is always divisible by 4. (iii) Check it for n = 10. (iv) A two-digit number has tens digit a and units digit b. Write it, and write the number with digits reversed. (v) Show that the sum of a two-digit number and its reverse is a multiple of 11; verify with 47.", 5,
    "(i) 4n + 12 (1 mark)<br>(ii) 4n + 12 = 4(n + 3) (1 mark)<br>(iii) 10 + 12 + 14 + 16 = 52 = 4 × 13 (1 mark)<br>(iv) 10a + b and 10b + a (1 mark)<br>(v) (10a + b) + (10b + a) = 11a + 11b = 11(a + b); 47 + 74 = 121 = 11 × 11 (1 mark)")]
e = [
 case("The Narendra Modi Stadium in Ahmedabad is one of the largest cricket stadiums in the world and can seat about 1,32,000 spectators. Suppose each ticket for a match costs ₹ 800.",
      [sub("Write 1,32,000 in the international system.", 1, "132,000"),
       sub("How many lakh is 1,32,000?", 1, "1.32 lakh"),
       OR(sub("Find the money collected if all the seats are sold at ₹ 800 each. Write the answer in the Indian system and in crore.", 2, "1,32,000 × 800 = 10,56,00,000 (1 mark) = 10.56 crore rupees (1 mark)"),
          sub("About how many such stadiums would be needed to seat 1 crore people?", 2, "1,00,00,000 ÷ 1,32,000 ≈ 75.8 (1 mark); so about 76 stadiums (1 mark)"))]),
 case("Rani has 5/6 kg of dal. She uses 3/5 of it to cook lunch.",
      [sub("How much dal does she use for lunch?", 1, "3/5 × 5/6 = 1/2 kg"),
       sub("How much dal is left?", 1, "5/6 − 1/2 = 5/6 − 3/6 = 1/3 kg"),
       OR(sub("She packs the remaining dal into packets of 1/12 kg each. How many packets does she fill?", 2, "1/3 ÷ 1/12 = 1/3 × 12 (1 mark) = 4 packets (1 mark)"),
          sub("Her neighbour gives her 2/3 kg more dal. How much dal does she have now?", 2, "1/3 + 2/3 (1 mark) = 1 kg (1 mark)"))]),
 case("Tara notices a pattern: 11 × 11 = 121, 111 × 111 = 12321, 1111 × 1111 = 1234321. All the answers read the same forwards and backwards.",
      [sub("What is the name for such numbers?", 1, "Palindromes"),
       sub("Predict 11111 × 11111.", 1, "123454321"),
       OR(sub("Is 12321 divisible by 9? Use the divisibility rule and verify by division.", 2, "Digit sum 1 + 2 + 3 + 2 + 1 = 9 (1 mark), so divisible by 9; 12321 ÷ 9 = 1369 (1 mark)"),
          sub("Is 1234321 divisible by 3? Give a reason.", 2, "Digit sum = 1 + 2 + 3 + 4 + 3 + 2 + 1 = 16 (1 mark), not a multiple of 3, so not divisible by 3 (1 mark)"))])]
META = meta(3); SECTIONS = secs(q1, b, c, d, e)
