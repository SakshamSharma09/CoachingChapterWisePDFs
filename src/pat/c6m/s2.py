from h6 import *
# ---------- Set 2 : emphasis Patterns, Lines & Angles, Perimeter & Area, Symmetry, Constructions ----------
fib = [1, 1]
while len(fib) < 12: fib.append(fib[-1] + fib[-2])
q1 = mcqgroup([
 mm("The sum of the first 7 odd numbers (1 + 3 + 5 + ...) is:", 49, [14, 42, 56], "The sum of the first n odd numbers is n²; 7² = 49."),
 mm("In the sequence 1, 1, 2, 3, 5, 8, 13, ... each term is the sum of the two terms before it. The 9th term is:", fib[8], [29, 32, 55], "1, 1, 2, 3, 5, 8, 13, 21, 34 — the 9th term is 34."),
 mm("The hour hand of a clock turns from 12 to 9. The angle through which it turns is:", "270°", ["90°", "180°", "300°"], "9 × 30° = 270°, a reflex angle."),
 mm("The perimeter of a rectangle is 52 m and its length is 16 m. Its width is:", "10 m", ["36 m", "20 m", "26 m"], "Length + width = 26 m, so width = 26 − 16 = 10 m."),
 mm("A square piece of side 6 cm is cut from a rectangular sheet 10 cm × 8 cm. The area of the remaining sheet is:", "44 cm²", ["36 cm²", "80 cm²", "64 cm²"], "80 − 36 = 44 cm²."),
 m("Which of these capital letters has NO line of symmetry?", "F", ["A", "B", "O"], "A has a vertical line, B a horizontal line and O has many; F has none."),
 mm("The longest chord of a circle of radius 5 cm has length:", "10 cm", ["5 cm", "7.5 cm", "15 cm"], "The longest chord is the diameter = 2 × 5 = 10 cm."),
 mm("The number of prime numbers between 1 and 20 is:", len(primes(1, 20)), [7, 9, 10], "2, 3, 5, 7, 11, 13, 17, 19."),
 m("2/3 of the 45 laddoos in a box are sold. The number of laddoos sold is:", "30", ["15", "20", "35"], "45 ÷ 3 = 15; 15 × 2 = 30."),
 m("The numbers −2, 5, −7, 0 arranged in ascending order are:", "−7, −2, 0, 5", ["−2, −7, 0, 5", "5, 0, −2, −7", "0, −2, −7, 5"], "On the number line, the number farther left is smaller."),
 mm("In a bar graph 1 cm height stands for 4 students. A bar for 24 students has height:", "6 cm", ["4 cm", "8 cm", "20 cm"], "24 ÷ 4 = 6 cm."),
 m("Which of the following is a palindrome?", "1331", ["1332", "1231", "1310"], "1331 reads the same from both ends."),
])
b = [
 sa("Matchsticks are used to make a row of squares. One square needs 4 sticks, two squares need 7 sticks and three squares need 10 sticks. How many sticks are needed for a row of 6 squares?", 2, f"Pattern: sticks = 3n + 1 (1 mark); for n = 6: 3 × 6 + 1 = {3*6+1} sticks (1 mark)"),
 sa("Measure the angle in the figure and name its type.", 2, "Measure = 40° (1 mark); acute angle (1 mark)", fig=G.angle(40)),
 sa("Write the number of lines of symmetry of (i) an equilateral triangle (ii) a rectangle which is not a square (iii) a circle.", 2, "(i) 3 (ii) 2 (iii) infinite (any two correct = 1 mark; all three = 2 marks)"),
 OR(sa("The area of a rectangular carpet is 96 m² and its length is 12 m. Find its width and perimeter.", 2, f"Width = 96 ÷ 12 = {96//12} m (1 mark); perimeter = 2 × (12 + 8) = {2*20} m (1 mark)"),
    sa("The area of a square tile is 144 cm². Find its side and perimeter.", 2, f"Side = 12 cm (1 mark); perimeter = 4 × 12 = {4*12} cm (1 mark)")),
 sa("Write the steps for constructing an angle of 60° with a compass and ruler.", 2, "Draw ray OA; with centre O draw an arc cutting OA at P (1 mark). With the same radius and centre P cut the arc at Q; join OQ — ∠POQ = 60° (1 mark)."),
 sa("Find: (i) (−6) + (−9) (ii) 4 − 11.", 2, f"(i) {-6-9} (1 mark) (ii) {4-11} (1 mark)"),
]
dirs = ['North', 'East', 'South', 'West']
c = [
 sa("A robot faces North. It first turns 90° clockwise and then turns 180° anticlockwise. (i) Which direction does it face after the first turn? (ii) Which direction does it face finally? (iii) By what angle should it now turn anticlockwise to face South?", 3,
    "(i) East (1 mark)<br>(ii) East → 180° anticlockwise → West (1 mark)<br>(iii) West to South anticlockwise = 90° (1 mark)"),
 OR(sa("A hall is 12 m long and 8 m wide. It is to be covered with square tiles of side 2 m. (i) Find the number of tiles. (ii) Find the cost at ₹150 per tile.", 3, f"(i) Area of hall = 96 m², area of one tile = 4 m²; tiles = 96 ÷ 4 = {96//4} (2 marks)<br>(ii) Cost = 24 × 150 = ₹{24*150} (1 mark)"),
    sa("A rectangular plot 25 m × 16 m has a path 2 m wide built all around it on the outside. Find the area of the path.", 3, f"Outer rectangle = (25 + 4) × (16 + 4) = 29 × 20 = {29*20} m² (1 mark); plot = 400 m² (1 mark); path = {29*20-400} m² (1 mark)")),
 sa("Meena asked 20 friends how many brothers/sisters they have: 1, 2, 0, 1, 3, 2, 1, 1, 2, 0, 1, 2, 1, 3, 1, 0, 2, 1, 1, 2. (i) Make a frequency table. (ii) Which number is the most common?", 3,
    "".join(f"{k}: {[1,2,0,1,3,2,1,1,2,0,1,2,1,3,1,0,2,1,1,2].count(k)} &nbsp;" for k in range(4)) + "(2 marks)<br>(ii) 1 (1 mark; frequency 8)"),
]
d = [
 OR(sa("Ravi climbs a staircase taking either 1 step or 2 steps at a time. (i) In how many different ways can he climb 1, 2, 3, 4 and 5 stairs? (ii) Write the pattern you see and find the number of ways for 6 stairs. (iii) Name the sequence.", 5,
       "(i) 1, 2, 3, 5, 8 (2 marks)<br>(ii) Each number is the sum of the two before it; 5 + 8 = 13 ways for 6 stairs (2 marks)<br>(iii) Fibonacci / Virahanka sequence (1 mark)"),
    sa("A row of n squares uses 3n + 1 matchsticks. (i) Complete the table for n = 1 to 5. (ii) Find the sticks for n = 10. (iii) How many squares can be made with 40 sticks?", 5,
       "(i) 4, 7, 10, 13, 16 (2 marks)<br>(ii) 3 × 10 + 1 = 31 (1 mark)<br>(iii) 3n + 1 = 40 ⇒ n = 13 (2 marks)")),
 OR(sa("Construct an angle of 60° using a compass and then bisect it to obtain 30°. Write the steps and verify with a protractor.", 5,
       "Draw ray OA, arc with centre O cutting OA at P (1); arc of same radius from P cutting first arc at Q, join OQ: 60° (1). Arcs from P and Q with the same radius meet at R (1); join OR: 30° (1). Protractor check: ∠POR = 30° (1)."),
    sa("Draw a circle of radius 3.5 cm with centre O. Draw a diameter AB. Construct the perpendicular bisector of AB meeting the circle at C and D. Join AC, CB, BD, DA and name the figure obtained.", 5,
       "Circle (1); diameter AB = 7 cm (1); perpendicular bisector through O meeting circle at C, D (2); joining gives the square ACBD (1).")),
 sa("A rectangular garden is 20 m long and 14 m wide. A square flower bed of side 4 m is inside it. Find (i) the area of the garden (ii) the area of the flower bed (iii) the area of the remaining lawn (iv) the cost of fencing the garden at ₹30 per metre (v) the cost of grass on the lawn at ₹12 per m².", 5,
    f"(i) {20*14} m² (ii) {16} m² (iii) {280-16} m² (iv) perimeter {2*34} m, cost ₹{68*30} (v) {264}×12 = ₹{264*12} (1 mark each)"),
]
case1 = case("Ria draws a house-shaped design for a rangoli on squared paper. The dotted line in the figure is drawn through the top vertex and the middle of the base.",
 [sub("What name is given to the dotted line if the two halves fit exactly on each other when folded?", 1, "Line of symmetry."),
  sub("How many lines of symmetry does the design have?", 1, "One (the vertical one)."),
  OR(sub("A point P of the design lies 15 units to the left of the dotted line. Where does its mirror image lie?", 2, "On the right of the line (1 mark), at the same distance, 15 units (1 mark)."),
     sub("Name one shape (other than the house) that has more than one line of symmetry and write how many lines it has.", 2, "Any valid shape, e.g. square (4 lines), rectangle (2 lines), circle (many) (1 mark for shape, 1 mark for the correct number of lines)"))], fig=G.sym_shape())
case2 = case("The school library has 48 notebooks and 36 pens to be packed into identical prize kits. Every kit must have the same number of notebooks and the same number of pens, and nothing should be left over.",
 [sub("What is the greatest number of kits that can be made?", 1, f"HCF(48, 36) = {gcd(48,36)} kits"),
  sub("How many notebooks and pens will each kit contain?", 1, f"Notebooks {48//12}, pens {36//12}"),
  OR(sub("Write 48 and 36 as products of prime factors.", 2, f"48 = {pfs(48)} (1 mark); 36 = {pfs(36)} (1 mark)"),
     sub("Is 36 a perfect square? Is 48? Explain with prime factorisation.", 2, "36 = 2² × 3², all powers even, so a perfect square (1 mark); 48 = 2⁴ × 3, power of 3 is odd, so not a perfect square (1 mark)"))])
case3 = case("A water tank in a society holds 1200 litres when full. At present it is 3/4 full. The gardener uses 1/3 of the water in the tank to water the plants.",
 [sub("How many litres of water are in the tank now?", 1, "3/4 × 1200 = 900 litres"),
  sub("How many litres does the gardener use?", 1, "1/3 × 900 = 300 litres"),
  OR(sub("What fraction of the full tank remains after the gardening?", 2, "Used = 300/1200 = 1/4 of the tank (1 mark); remaining = 3/4 − 1/4 = 1/2 (1 mark)"),
     sub("How many litres remain in the tank after the gardening?", 2, "900 − 300 (1 mark) = 600 litres (1 mark)"))])
META = meta(2); SECTIONS = secs(q1, b, c, d, [case1, case2, case3])
