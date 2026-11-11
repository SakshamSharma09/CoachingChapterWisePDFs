from lib8 import *
import mfigs as MF
from fractions import Fraction as Fr
# --- computed answers ---
assert 15 - 3*(2+4)//2 == 6 and (7+3)*2-1 == 19
assert 2*30//1 == 60
assert Fr(5, 2)*Fr(8, 5)/Fr(4, 5) == 5 and Fr(15, 2)/Fr(3, 4) == 10 and Fr(5, 6)*Fr(18, 5) == 3
assert 12543000 - 9876500 == 2666500 and 12543000 + 9876500 == 22419500
assert 4*20+1 == 81 and (101-1) % 4 == 0 and 150 % 2 == 0
def collatz(n):
    s = [n]
    while n != 1: n = n//2 if n % 2 == 0 else 3*n+1; s.append(n)
    return s
cz = collatz(12); assert len(cz)-1 == 9
assert sum(range(1, 11)) == 55 and (5+2+3+4+1+2) == 17 and sum(range(14, 19)) == 80
assert 3*7+1 == 22 and 3*(2*25)//2 == 75
assert 120*10 + 80*25 == 3200 and 1450+350 == 1800 and 3200-1800 == 1400 and 1400//7 == 200 and 80*5 == 400
assert abs(3.85+3.9+3.805-11.555) < 1e-9 and abs(3.9-3.805-0.095) < 1e-9
# transversal data: BPQ=(4x+5)=105, DQP=(2x+25)=75 at x = 25
assert 4*25+5 == 105 and 2*25+25 == 75 and (25+25)+(2*25+25)*0 == 50
assert (30+10, 2*30-20, 3*30+10) == (40, 40, 100)
q1 = mcqgroup([
 m("In the number 3,07,45,218, the place value of the digit 7 is:", "7,00,000", ["70,000", "70,00,000", "7,000"], "Reading from the right: 8, 1, 2 | 5 (thousands) | 4 (ten-thousands) | 7 (lakhs) | 0 | 3 (crore). So 7 is in the lakh place: 7,00,000."),
 m("The sum 4,87,000 + 3,12,500 correct to the nearest lakh is about:", "8 lakh", ["7 lakh", "9 lakh", "80 lakh"], "4,87,000 + 3,12,500 = 7,99,500 ≈ 8 lakh."),
 m("The value of 15 − 3 × (2 + 4) ÷ 2 is:", "6", ["36", "9", "18"], "Brackets: 6; then 3 × 6 = 18, 18 ÷ 2 = 9; 15 − 9 = 6."),
 m("0.3 + 0.04 + 0.005 equals:", "0.345", ["0.0345", "0.35", "3.45"], "3 tenths + 4 hundredths + 5 thousandths = 0.345."),
 m("The fraction 1/8 written as a decimal is:", "0.125", ["0.18", "0.8", "1.25"], "1 ÷ 8 = 0.125."),
 m("The perimeter of a rectangle of length l and breadth b is:", "2(l + b)", ["l + b", "2lb", "l + 2b"], "Two lengths plus two breadths: 2l + 2b = 2(l + b)."),
 m("How many terms are there in the expression 4x² − 3x + 7?", "3", ["2", "4", "1"], "The terms are 4x², −3x and 7."),
 m("Two angles forming a linear pair are in the ratio 2 : 3. The smaller angle is:", "72°", ["36°", "60°", "108°"], "2k + 3k = 180 ⇒ k = 36; smaller = 2 × 36 = 72°."),
 m("A transversal cuts two parallel lines and one alternate interior angle is 62°. The other alternate interior angle is:", "62°", ["118°", "28°", "31°"], "Alternate interior angles between parallel lines are equal."),
 m("In the Collatz process, the number that follows 7 is:", "22", ["21", "8", "11"], "7 is odd, so 3 × 7 + 1 = 22."),
 m("An isosceles triangle has a vertex angle of 100°. Each base angle is:", "40°", ["80°", "50°", "100°"], "(180° − 100°) ÷ 2 = 40°."),
 m("The value of 3/4 of 2/3 is:", "1/2", ["9/8", "8/9", "5/7"], "3/4 × 2/3 = 6/12 = 1/2.")])
b = [
 sa("Write 3,06,07,008 in words according to the Indian system.", 2, "3,06,07,008 = three crore six lakh seven thousand eight (2 marks; 1 mark if one place value is misread)"),
 sa("Insert one pair of brackets in 7 + 3 × 2 − 1 so that its value becomes 19. Verify your answer.", 2, "(7 + 3) × 2 − 1 (1 mark)<br>= 10 × 2 − 1 = 20 − 1 = 19 (1 mark)"),
 OR(sa("Express 3/5 and 7/20 as decimals and find their sum.", 2, "3/5 = 0.6 and 7/20 = 0.35 (1 mark); sum = 0.95 (1 mark)"),
    sa("Round 28.4567 to (i) the nearest tenth and (ii) the nearest hundredth.", 2, "(i) 28.5 (1 mark)<br>(ii) 28.46 (1 mark)")),
 sa("Find the value of 3p² − 2q + 5 when p = 2 and q = 4.", 2, "3 × 4 − 2 × 4 + 5 (1 mark)<br>= 12 − 8 + 5 = 9 (1 mark)"),
 sa("A transversal cuts two parallel lines. A pair of corresponding angles is (3x − 10)° and (2x + 25)°. Find x and the measure of each angle.", 2, "Corresponding angles are equal: 3x − 10 = 2x + 25 ⇒ x = 35 (1 mark)<br>Each angle = 3 × 35 − 10 = 95° (1 mark)"),
 sa("Show that the sum of any three consecutive numbers is divisible by 3. Verify with 14, 15, 16.", 2, "n + (n + 1) + (n + 2) = 3n + 3 = 3(n + 1) (1 mark)<br>14 + 15 + 16 = 45 = 3 × 15 (1 mark)")]
c = [
 OR(sa("Simplify: 2 1/2 × 1 3/5 ÷ 4/5.", 3, "2 1/2 = 5/2 and 1 3/5 = 8/5 (1 mark)<br>5/2 × 8/5 = 4 (1 mark)<br>4 ÷ 4/5 = 4 × 5/4 = 5 (1 mark)"),
    sa("A rope 7 1/2 m long is cut into pieces of 3/4 m each. How many pieces are obtained? How much of the rope is left?", 3, "7 1/2 = 15/2 m (1 mark)<br>15/2 ÷ 3/4 = 15/2 × 4/3 = 10 pieces (1 mark)<br>Nothing is left, because 10 × 3/4 = 7 1/2 m exactly (1 mark)")),
 sa("An isosceles triangle has two sides of 3 cm and 8 cm. (i) Find the length of the third side, giving a reason. (ii) Find its perimeter.", 3, "(i) If the third side were 3 cm, then 3 + 3 = 6 &lt; 8, which violates the triangle inequality, so the third side is 8 cm (2 marks)<br>(ii) Perimeter = 3 + 8 + 8 = 19 cm (1 mark)"),
 sa("The populations of two towns are 1,25,43,000 and 98,76,500. (i) Which town has more people? (ii) Find the difference between the populations. (iii) Find their total, correct to the nearest lakh.", 3, "(i) The first town (1,25,43,000 &gt; 98,76,500) (1 mark)<br>(ii) 1,25,43,000 − 98,76,500 = 26,66,500 (1 mark)<br>(iii) Total = 2,24,19,500 ≈ 2,24,00,000 (224 lakh) (1 mark)")]
fig_tr = MF.transversal("(4x + 5)°", "(2x + 25)°", 105)
d = [
 OR(sa("A rangoli border is made with dots: pattern 1 has 5 dots, pattern 2 has 9 dots, pattern 3 has 13 dots. (i) Write the number of dots in pattern 4. (ii) Write a rule for pattern n. (iii) How many dots are in pattern 20? (iv) Which pattern has 101 dots? (v) Can a pattern have exactly 150 dots? Why?", 5, "(i) 17 (1 mark)<br>(ii) 4n + 1 (1 mark)<br>(iii) 4 × 20 + 1 = 81 (1 mark)<br>(iv) 4n + 1 = 101 ⇒ n = 25 (1 mark)<br>(v) 4n + 1 is always odd, so 150 is not possible (1 mark)"),
    sa("(i) Simplify (3a + 2b) + (a − 5b) − (2a − b). (ii) Find its value when a = 6 and b = 3. (iii) Subtract 3x − 2y + 5 from 7x + 4y − 1. (iv) A rectangle has length (3x + 2) cm and breadth (x + 5) cm; write its perimeter. (v) Find that perimeter for x = 3.", 5, "(i) 3a + 2b + a − 5b − 2a + b = 2a − 2b (1 mark)<br>(ii) 12 − 6 = 6 (1 mark)<br>(iii) 7x + 4y − 1 − 3x + 2y − 5 = 4x + 6y − 6 (1 mark)<br>(iv) 2(3x + 2 + x + 5) = 8x + 14 cm (1 mark)<br>(v) 8 × 3 + 14 = 38 cm (1 mark)")),
 OR(sa("In the figure, AB ∥ CD and PQ is a transversal. ∠BPQ = (4x + 5)° and ∠DQP = (2x + 25)°. (i) Name the pair of angles. (ii) Find x. (iii) Find ∠BPQ and ∠DQP. (iv) Find ∠CQP. (v) Find ∠APQ.", 5, "(i) Co-interior angles, which are supplementary (1 mark)<br>(ii) 6x + 30 = 180 ⇒ x = 25 (1 mark)<br>(iii) ∠BPQ = 105°, ∠DQP = 75° (1 mark)<br>(iv) ∠CQP = 105° (alternate to ∠BPQ; or linear pair with ∠DQP) (1 mark)<br>(v) ∠APQ = 180° − 105° = 75° (1 mark)", fig=fig_tr),
    sa("The angles of a triangle are (x + 10)°, (2x − 20)° and (3x + 10)°. (i) Write the equation formed using the angle sum property. (ii) Find x. (iii) Find the three angles. (iv) Classify the triangle by sides and by angles. (v) Find the exterior angle at the vertex with the largest angle.", 5, "(i) (x + 10) + (2x − 20) + (3x + 10) = 180 (1 mark)<br>(ii) 6x = 180 ⇒ x = 30 (1 mark)<br>(iii) 40°, 40°, 100° (1 mark)<br>(iv) Isosceles (two equal angles) and obtuse-angled (1 mark)<br>(v) 180° − 100° = 80° (1 mark)")),
 sa("(i) Write the Collatz sequence starting with 12 and state how many steps are taken to reach 1. (ii) Find 1 + 2 + 3 + … + 10 using pairs. (iii) Is 5,23,412 divisible by 3? Give a reason. (iv) Write the smallest 4-digit palindrome. (v) Find the sum of 14, 15, 16, 17, 18 without adding term by term.", 5,
    f"(i) {' → '.join(map(str, cz))}; 9 steps (1 mark)<br>(ii) 5 pairs, each with sum 11: 5 × 11 = 55 (1 mark)<br>(iii) Digit sum = 5 + 2 + 3 + 4 + 1 + 2 = 17, not a multiple of 3, so not divisible (1 mark)<br>(iv) 1001 (1 mark)<br>(v) 5 × middle term = 5 × 16 = 80 (1 mark)")]
fig_rail = MF.transversal("65°", "x°", 65, names=('A', 'B', 'C', 'D', 'P', 'Q'))
e = [
 case("Two straight railway tracks AB and CD are parallel. A road PQ crosses both tracks, as shown. The road makes an angle of 65° with the upper track at P. The angle at Q, between the road and the lower track on the same side, is x°.",
      [sub("Find ∠APQ.", 1, "∠APQ = 180° − 65° = 115° (linear pair)"),
       sub("Name the relation between 65° and x° and find x.", 1, "Co-interior angles (supplementary): x = 180 − 65 = 115"),
       OR(sub("Find ∠CQP and the angle vertically opposite to ∠DQP.", 2, "∠CQP = 65° (alternate interior angle to ∠BPQ) (1 mark); the angle vertically opposite to ∠DQP is also 115° (1 mark)"),
          sub("Are ∠BPQ and ∠CQP alternate interior or corresponding angles? Why are they equal?", 2, "Alternate interior angles (1 mark); equal because AB ∥ CD (1 mark)"))], fig=fig_rail),
 case("Class VII runs a food stall at the school fair. They sell 120 samosas at ₹ 10 each and 80 sandwiches at ₹ 25 each. The cost of ingredients is ₹ 1,450 and the helpers are paid ₹ 350.",
      [sub("Write and evaluate an arithmetic expression for the total sales (income).", 1, "120 × 10 + 80 × 25 = 1200 + 2000 = ₹ 3,200"),
       sub("Find the profit.", 1, "Total expenses = 1,450 + 350 = ₹ 1,800; profit = 3,200 − 1,800 = ₹ 1,400"),
       OR(sub("The profit is shared equally among 7 students. Write one expression for each student's share and evaluate it.", 2, "(120 × 10 + 80 × 25 − 1450 − 350) ÷ 7 (1 mark) = 1400 ÷ 7 = ₹ 200 (1 mark)"),
          sub("If each sandwich were sold for ₹ 5 more (same number sold), how much extra money would come in? Find the new total sales.", 2, "Extra = 80 × 5 = ₹ 400 (1 mark); new sales = 3,200 + 400 = ₹ 3,600 (1 mark)"))]),
 case("In the school sports day, three friends recorded their long-jump distances: Arjun 3.85 m, Bela 3.9 m and Chirag 3.805 m.",
      [sub("Who jumped the farthest?", 1, "Bela: 3.900 &gt; 3.850 &gt; 3.805"),
       sub("Find the difference between the longest and the shortest jump.", 1, "3.900 − 3.805 = 0.095 m"),
       OR(sub("Find the total of the three jumps and round it to the nearest tenth.", 2, "3.85 + 3.9 + 3.805 = 11.555 m (1 mark) ≈ 11.6 m (1 mark)"),
          sub("Find the average of Arjun's and Bela's jumps.", 2, "(3.85 + 3.9) ÷ 2 (1 mark) = 7.75 ÷ 2 = 3.875 m (1 mark)"))])]
META = meta(2); SECTIONS = secs(q1, b, c, d, e)
