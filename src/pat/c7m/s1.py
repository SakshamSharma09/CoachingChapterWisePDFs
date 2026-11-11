from lib8 import *
import mfigs as MF
from fractions import Fraction as Fr
# --- computed answers ---
assert 36//6*3+2 == 20 and 48//(4+2*2)+3*2 == 12
assert 1250000*480 == 600000000 and 5*10**7+8*10**5+4*10**4 == 50840000
def kap(n):
    d = sorted(str(n).zfill(4)); return int(''.join(reversed(d))) - int(''.join(d))
k1 = kap(3524); k2 = kap(k1); k3 = kap(k2); assert (k1, k2, k3) == (3087, 8352, 6174)
assert Fr(2, 3) / Fr(4, 9) == Fr(3, 2) and Fr(9, 2) / Fr(3, 4) == 6
assert abs(2.5*48.6 - 121.5) < 1e-9 and abs(1.25*44.8 - 56) < 1e-9
assert 68548437 // 342239 == 200
q1 = mcqgroup([
 m("One billion is equal to how many crore?", "100 crore", ["10 crore", "1000 crore", "1 crore"], "1 billion = 10<sup>9</sup> and 1 crore = 10<sup>7</sup>, so 1 billion = 100 crore."),
 m("The number of seconds in one day is:", "86,400", ["14,400", "3,600", "8,640"], "24 × 60 × 60 = 86,400."),
 m("The value of 36 ÷ 6 × 3 + 2 is:", "20", ["4", "30", "8"], "Left to right: 36 ÷ 6 = 6; 6 × 3 = 18; 18 + 2 = 20."),
 m("In the decimal number 4.058, the digit 5 is in the:", "hundredths place", ["tenths place", "thousandths place", "tens place"], "4 . 0 5 8: tenths = 0, hundredths = 5, thousandths = 8."),
 m("Which of these decimals is the greatest?", "0.5", ["0.49", "0.499", "0.05"], "0.5 = 0.500 > 0.499 > 0.490 > 0.050."),
 m("'Five more than three times a number n' is written as:", "3n + 5", ["5n + 3", "3(n + 5)", "3n − 5"], "Three times n is 3n; five more gives 3n + 5."),
 m("The value of 2a² − 3b when a = 3 and b = 2 is:", "12", ["6", "0", "24"], "2 × 9 − 3 × 2 = 18 − 6 = 12."),
 m("One angle of a linear pair is 65°. The other angle is:", "115°", ["25°", "125°", "295°"], "Angles of a linear pair add up to 180°: 180 − 65 = 115°."),
 m("A transversal cuts two parallel lines. Each pair of co-interior angles (interior angles on the same side) adds up to:", "180°", ["90°", "360°", "a different value each time"], "Co-interior angles of parallel lines are supplementary."),
 m("The sum of the first 10 odd numbers is:", "100", ["55", "110", "90"], "Sum of the first n odd numbers is n²: 10² = 100."),
 m("Which three lengths can be the sides of a triangle?", "7 cm, 8 cm, 10 cm", ["4 cm, 5 cm, 9 cm", "3 cm, 3 cm, 7 cm", "6 cm, 6 cm, 13 cm"], "Each sum of two sides must exceed the third: 7 + 8 > 10 holds; in the others the two shorter sides add up to at most the longest."),
 m("The value of 2/3 ÷ 4/9 is:", "3/2", ["8/27", "4/3", "1/6"], "2/3 × 9/4 = 18/12 = 3/2.")])
b = [
 sa("Write 5 crore 8 lakh 40 thousand in figures using commas (i) in the Indian system and (ii) in the international system.", 2, "(i) 5,08,40,000 (1 mark)<br>(ii) 50,840,000 (1 mark)"),
 sa("Evaluate: 48 ÷ (4 + 2 × 2) + 3 × 2. Show each step.", 2, "Brackets first: 4 + 2 × 2 = 4 + 4 = 8 (1 mark)<br>48 ÷ 8 + 3 × 2 = 6 + 6 = 12 (1 mark)"),
 OR(sa("A ribbon 3.5 m long is cut into pieces of 0.25 m each. How many pieces are obtained?", 2, "3.5 ÷ 0.25 = 350 ÷ 25 (1 mark) = 14 pieces (1 mark)"),
    sa("Subtract 4.875 from 10.2.", 2, "10.200 − 4.875 (aligning decimal points) (1 mark) = 5.325 (1 mark)")),
 sa("Simplify: 5x + 3y − 2x + 4y.", 2, "Group like terms: (5x − 2x) + (3y + 4y) (1 mark)<br>= 3x + 7y (1 mark)"),
 sa("Two straight lines intersect and one of the four angles formed is 40°. Find the other three angles, giving reasons.", 2, "Vertically opposite angle = 40° (1 mark)<br>Each of the other two forms a linear pair with 40°: 180° − 40° = 140° and 140° (1 mark)"),
 sa("Start with 3524 and carry out the Kaprekar routine (arrange digits in descending and ascending order and subtract) until you reach 6174.", 2, f"5432 − 2345 = {k1} (1 mark)<br>8730 − 0378 = {k2}; 8532 − 2358 = {k3} (1 mark)")]
c = [
 OR(sa("In triangle ABC the angles are in the ratio ∠A : ∠B : ∠C = 2 : 3 : 4. Find the three angles and state whether the triangle is acute-angled, right-angled or obtuse-angled.", 3, "Angle sum 180°: 2k + 3k + 4k = 180 ⇒ k = 20 (1 mark)<br>∠A = 40°, ∠B = 60°, ∠C = 80° (1 mark)<br>All angles are less than 90°, so it is acute-angled (1 mark)"),
    sa("The exterior angle of a triangle is 110° and one of its interior opposite angles is 45°. Find the other interior opposite angle and the adjacent interior angle.", 3, "Exterior angle = sum of the two interior opposite angles (1 mark)<br>Other opposite angle = 110° − 45° = 65° (1 mark)<br>Adjacent interior angle = 180° − 110° = 70° (1 mark)")),
 sa("Meena's mother needs 3/4 cup of flour for one batch of rotis. She has 4 1/2 cups of flour. (i) How many batches can she make? (ii) She also uses 2/3 of a 9/10 kg pack of ghee; how many kg is that?", 3, "(i) 9/2 ÷ 3/4 = 9/2 × 4/3 (1 mark) = 6 batches (1 mark)<br>(ii) 2/3 × 9/10 = 18/30 = 3/5 kg (1 mark)"),
 sa("A city has 12,50,000 houses and every house uses about 480 litres of water a day. Find the total water used in a day (i) in litres, written in the Indian system and in crore, and (ii) in the international system (in millions).", 3, "1,250,000 × 480 = 600,000,000 (1 mark)<br>(i) 60,00,00,000 litres = 60 crore litres (1 mark)<br>(ii) 600,000,000 = 600 million litres (1 mark)")]
fig_tr = MF.transversal("(2x + 10)°", "(3x + 20)°", 70)
fig_ex = MF.tri_ext("(2x + 5)°", "(x + 25)°", "(4x − 10)°", 65, 30)
d = [
 OR(sa("Sunita buys 2.5 kg rice at ₹ 48.60 per kg and 1.25 kg sugar at ₹ 44.80 per kg. (i) Find the cost of the rice. (ii) Find the cost of the sugar. (iii) Find the total bill. (iv) She pays with a ₹ 200 note; how much change does she get? (v) How many 50-paise coins make up the cost of the rice?", 5, "(i) 2.5 × 48.60 = ₹ 121.50 (1 mark)<br>(ii) 1.25 × 44.80 = ₹ 56.00 (1 mark)<br>(iii) 121.50 + 56.00 = ₹ 177.50 (1 mark)<br>(iv) 200 − 177.50 = ₹ 22.50 (1 mark)<br>(v) 121.50 ÷ 0.50 = 243 coins (1 mark)"),
    sa("(i) Write 7/8 as a decimal. (ii) Write 0.375 as a fraction in simplest form. (iii) Arrange 0.6, 0.59, 0.605 and 0.06 in ascending order. (iv) Find 4.56 × 100. (v) Find 7.5 ÷ 10.", 5, "(i) 0.875 (1 mark)<br>(ii) 375/1000 = 3/8 (1 mark)<br>(iii) 0.06 &lt; 0.59 &lt; 0.6 &lt; 0.605 (1 mark)<br>(iv) 456 (1 mark)<br>(v) 0.75 (1 mark)")),
 OR(sa("In the figure, AB ∥ CD and PQ is a transversal. ∠BPQ = (2x + 10)° and ∠DQP = (3x + 20)°. (i) Name the relation between these two angles. (ii) Find x. (iii) Find ∠BPQ and ∠DQP. (iv) Find ∠APQ.", 5, "(i) Co-interior angles (interior angles on the same side), so they are supplementary (1 mark)<br>(ii) 2x + 10 + 3x + 20 = 180 ⇒ 5x = 150 ⇒ x = 30 (2 marks)<br>(iii) ∠BPQ = 70°, ∠DQP = 110° (1 mark)<br>(iv) ∠APQ = 180° − 70° = 110° (linear pair) (1 mark)", fig=fig_tr),
    sa("In the figure, side BC of triangle ABC is extended to D. ∠A = (2x + 5)°, ∠B = (x + 25)° and the exterior angle ∠ACD = (4x − 10)°. (i) State the exterior angle property. (ii) Find x. (iii) Find ∠A and ∠B. (iv) Find ∠ACB.", 5, "(i) An exterior angle equals the sum of the two interior opposite angles (1 mark)<br>(ii) 4x − 10 = 2x + 5 + x + 25 ⇒ x = 40 (2 marks)<br>(iii) ∠A = 85°, ∠B = 65° (1 mark)<br>(iv) ∠ACB = 180° − 150° = 30° (check: 85 + 65 + 30 = 180) (1 mark)", fig=fig_ex)),
 sa("Squares are made in a row using matchsticks: 1 square needs 4 sticks, 2 squares need 7 sticks, 3 squares need 10 sticks. (i) How many sticks are needed for 5 squares? (ii) Write a rule (expression) for n squares. (iii) How many squares can be made with exactly 100 sticks? (iv) Can exactly 50 sticks make a row of squares with none left over? Why? (v) Is the number of sticks for n squares always odd? Check for n = 1, 2, 3, 4.", 5,
    "(i) 3 × 5 + 1 = 16 sticks (1 mark)<br>(ii) 3n + 1 (1 mark)<br>(iii) 3n + 1 = 100 ⇒ n = 33 (1 mark)<br>(iv) 3n + 1 = 50 ⇒ 3n = 49, not a whole number; so No (1 mark)<br>(v) 4, 7, 10, 13 are alternately even and odd, so No (1 mark)")]
e = [
 case("Rajasthan is the largest state of India by area. According to the 2011 Census, its population was 6,85,48,437 and its area is 3,42,239 square kilometres.",
      [sub("Write the population correct to the nearest lakh.", 1, "6,85,48,437 lies between 685 lakh and 686 lakh and 48,437 is less than half a lakh, so ≈ 6,85,00,000 (685 lakh)"),
       sub("How many crore people is this, approximately (to two decimal places)?", 1, "≈ 6.85 crore"),
       OR(sub("Find the approximate population per square kilometre (nearest whole number).", 2, "68,548,437 ÷ 342,239 ≈ 200.3 (1 mark) ≈ 200 persons per km² (1 mark)"),
          sub("If the population increases by 25,00,000, write the new population in the Indian system.", 2, "6,85,48,437 + 25,00,000 (1 mark) = 7,10,48,437 (1 mark)"))]),
 case("A triangular flower bed ABC in a school garden has AB = 9 m and BC = 7 m. The third side CA = x metres is a whole number. The angles at A and B are 50° and 70°. The gardener extends side BC beyond C to lay a path.",
      [sub("Can CA be 17 m? Give a reason.", 1, "No. 9 + 7 = 16 is less than 17, violating the triangle inequality."),
       sub("Write the greatest and the smallest whole number value of x.", 1, "2 &lt; x &lt; 16, so x can be at most 15 and at least 3."),
       OR(sub("Find ∠C and the exterior angle at C.", 2, "∠C = 180° − (50° + 70°) = 60° (1 mark); exterior angle = 180° − 60° = 120° (= 50° + 70°) (1 mark)"),
          sub("If a similar flower bed is isosceles with a vertex angle of 40°, find its base angles.", 2, "Base angles are equal: (180° − 40°) ÷ 2 (1 mark) = 70° each (1 mark)"))]),
 case("Kavya's mother has 12 1/2 litres of milk in a can. She pours it into glasses, each holding 1/4 litre.",
      [sub("How many glasses can she fill?", 1, "25/2 ÷ 1/4 = 25/2 × 4 = 50 glasses"),
       sub("Write the reciprocal of 5/8.", 1, "8/5"),
       OR(sub("She sells 3/5 of the milk. How many litres are left?", 2, "Left = 2/5 of 25/2 (1 mark) = 5 litres (1 mark)"),
          sub("Each glass is sold at ₹ 15. Find the money received if 3/5 of the milk is sold.", 2, "Sold = 3/5 × 25/2 = 7.5 L = 30 glasses (1 mark); 30 × 15 = ₹ 450 (1 mark)"))])]
META = meta(1); SECTIONS = secs(q1, b, c, d, e)
