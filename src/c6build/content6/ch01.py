import random
from lib import mcq, Q, OR
from mk9 import M4, build
R = random.Random(601)
A = []; B = []; C = []; D = []
# A: number sequences – next term / nth term (generated)
def seq_next(name, f, k, wr):
    terms = [f(i) for i in range(1, 6)]
    A.append(M4(f"The next number in the {name} sequence ${', '.join(map(str, terms))}, \\dots$ is:", str(f(6)), [str(f(6) + d) for d in wr], f"the rule gives {f(6)}"))
seq_next("square number", lambda n: n * n, 6, [1, 2, 4])
seq_next("triangular number", lambda n: n * (n + 1) // 2, 6, [1, -1, 3])
seq_next("cube number", lambda n: n ** 3, 6, [-16, 10, 24])
seq_next("powers of 2", lambda n: 2 ** (n - 1), 6, [4, -8, 16])
seq_next("odd number", lambda n: 2 * n - 1, 6, [1, -1, 2])
seq_next("even number", lambda n: 2 * n, 6, [1, -2, 2])
seq_next("powers of 3", lambda n: 3 ** (n - 1), 6, [3, -9, 9])
A += [
 M4("The 10th triangular number is:", "55", ["45", "50", "66"], "$1+2+\\dots+10=55$"),
 M4("The 8th square number is:", "64", ["56", "72", "81"], "$8\\times8$"),
 M4("The 5th cube number is:", "125", ["25", "100", "216"], "$5\\times5\\times5$"),
 M4("The sum of the first 6 odd numbers is:", "36", ["21", "30", "49"], "sum of first $n$ odd numbers is $n^2$"),
 M4("The sum of the first 9 odd numbers is:", "81", ["72", "90", "64"], "$9^2$"),
 M4("Which of these is NOT a square number?", "50", ["49", "64", "81"], "$7^2,8^2,9^2$ are squares"),
 M4("Which of these numbers is a triangular number?", "28", ["27", "30", "32"], "$1+2+\\dots+7=28$"),
 M4("Adding two consecutive triangular numbers 6 and 10 gives:", "16", ["15", "18", "20"], "a square number"),
 M4("In the Virahānka (Fibonacci) sequence 1, 2, 3, 5, 8, 13, … each term after the first two is:", "the sum of the two terms before it", ["double the previous term", "the difference of the previous two", "the product of the previous two"], "rule of the sequence"),
 M4("The term after 21 and 34 in the Virahānka sequence is:", "55", ["45", "65", "56"], "$21+34$"),
 M4("The number of sides in the shape sequence of regular polygons starting with the triangle is:", "3, 4, 5, 6, …", ["2, 4, 6, 8, …", "1, 3, 6, 10, …", "3, 6, 9, 12, …"], "one more each time"),
 M4("A complete graph with 4 points has how many lines joining them?", "6", ["4", "8", "12"], "$3+2+1$"),
 M4("A complete graph with 5 points has how many lines?", "10", ["5", "15", "20"], "$4+3+2+1$"),
 M4("The Koch snowflake is built by repeatedly:", "adding a ‘speed bump’ to each line segment", ["removing corners", "doubling every angle", "joining midpoints"], "shape pattern"),
 M4("Which sequence is obtained by adding 1+3, 1+3+5 …?", "square numbers", ["triangular numbers", "cube numbers", "powers of 2"], "odd sums"),
 M4("The pattern 1, 4, 7, 10, … adds ___ each time:", "3", ["2", "4", "1"], "common difference"),
 M4("The next term in 5, 10, 20, 40, … is:", "80", ["60", "70", "100"], "doubling"),
 M4("Which sequence contains only the number 1 repeated?", "the ‘all 1’s’ sequence", ["counting numbers", "even numbers", "cubes"], "constant sequence"),
 M4("The 100th even number is:", "200", ["100", "198", "202"], "$2\\times100$"),
 M4("The 50th odd number is:", "99", ["100", "101", "97"], "$2\\times50-1$"),
 M4("Hexagonal numbers 1, 7, 19, 37, … are formed by:", "dots arranged in hexagons around a centre", ["dots in a square grid", "dots in a triangle", "dots in a line"], "centred shape"),
 M4("A rule that tells how to get each term of a sequence is called a:", "pattern rule", ["fraction", "angle", "perimeter"], "describes sequence"),
 M4("Which is the rule for the sequence 3, 6, 9, 12, …?", "multiples of 3", ["powers of 3", "squares of 3", "add 6 each time"], "$3\\times n$"),
]
for n in (4, 6, 9, 11, 12):
    t = n * (n + 1) // 2
    A.append(M4(f"The {n}th triangular number is:", str(t), [str(t + 1), str(t - 2), str(t + n)], f"$1+2+\\dots+{n}={t}$"))
for n in (7, 12, 15, 20, 25):
    A.append(M4(f"The sum of the first {n} odd numbers is:", str(n * n), [str(n * n + n), str(n * n - n), str(2 * n)], f"$n^2={n*n}$"))
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Write the first five square numbers.", "1, 4, 9, 16, 25.", "1+1"),
 Q("Write the first five triangular numbers.", "1, 3, 6, 10, 15.", "1+1"),
 Q("Why are the numbers 1, 4, 9, 16, … called square numbers?", "Dots equal to these numbers can be arranged to form a perfect square.", "1+1"),
 Q("Find the sum $1+3+5+7+9$ without adding one by one.", "Sum of the first 5 odd numbers is $5^2=25$.", "1+1"),
 Q("What is a sequence? Give one example.", "A list of numbers or shapes in a particular order following a rule; e.g. 2, 4, 6, 8.", "1+1"),
 Q("Write the first six terms of the powers of 2.", "1, 2, 4, 8, 16, 32.", "1+1"),
 Q("What is the 7th term of the cube-number sequence?", "$7^3=343$.", "1+1"),
 Q("Write the next two terms: 1, 2, 3, 5, 8, …", "13 and 21 (each term is the sum of the previous two).", "1+1"),
 Q("State the rule of the sequence 2, 5, 8, 11, … and give the next term.", "Add 3 each time; next term is 14.", "1+1"),
 Q("How many dots are there in the 6th triangular arrangement?", "$1+2+3+4+5+6=21$ dots.", "1+1"),
 Q("Write the 12th even number and the 12th odd number.", "24 and 23.", "1+1"),
 Q("What do we get on adding 1+2+1, 1+2+3+2+1, … ?", "Square numbers: 4, 9, 16, …", "1+1"),
 Q("How many lines are there in a complete graph of 6 points?", "$5+4+3+2+1=15$ lines.", "1+1"),
 Q("Name two uses of patterns in everyday life.", "Calendars, designs on floors and cloth, music and nature (any two).", "1+1"),
 Q("Is 100 a square number? Give a reason.", "Yes; $10\\times10=100$.", "1+1"),
 Q("Add two consecutive triangular numbers 15 and 21. What do you get?", "36, a square number.", "1+1"),
]
C = [
 Q("Explain with a picture why the sum of the first $n$ odd numbers is $n^2$.", "Add one L-shaped layer of odd number of dots to a square each time; 1, 1+3 = 4, 1+3+5 = 9 (dots form bigger squares).", "1½+1½"),
 Q("Explain why 1, 3, 6, 10, … are called triangular numbers.", "Dots equal to each number can be arranged in a triangle with 1, 2, 3 … dots in rows (1½); each new number adds one more row (1½).", "1½+1½"),
 Q("Describe the Virahānka (Fibonacci) sequence and write its first 10 terms.", "Each term is the sum of the two before it (1); 1, 2, 3, 5, 8, 13, 21, 34, 55, 89 (2).", "1+2"),
 Q("Find the sum $1+2+3+\\dots+10$ using a pattern. Explain.", "Triangular number: 55 (1); pairs $(1+10),(2+9)\\dots$ make 5 pairs of 11 (2).", "1+2"),
 Q("Write the rule and the next three terms of 4, 7, 10, 13, …", "Add 3 each time (1); 16, 19, 22 (2).", "1+2"),
 Q("Draw the next shape in a sequence of squares with 1, 4, 9 dots and say how many dots it has.", "The next shape has 16 dots (1); a 4 by 4 grid (2).", "1+2"),
 Q("What patterns are seen in the sequence of cube numbers?", "1, 8, 27, 64, … (1); each is a number multiplied by itself thrice (1); they can be shown as cubes of unit blocks (1).", "1+1+1"),
 Q("Why is the pattern 1, 1+3, 1+3+5, … true forever? Explain.", "Each new odd number adds a layer around the earlier square (1.5); so squares keep growing (1.5).", "1½+1½"),
 Q("Write four properties of triangular numbers.", "Formed by adding counting numbers; two consecutive ones add to a square; shown by dot triangles; 1, 3, 6, 10, … (any three with one more).", "1½+1½"),
 Q("What is a shape sequence? Describe one example.", "A series of shapes following a pattern (1); e.g. regular polygons with 3, 4, 5, … sides (2).", "1+2"),
 Q("The number of lines in complete graphs of 2, 3, 4, 5 points are 1, 3, 6, 10. What sequence is this and what will be the next term?", "Triangular numbers (1.5); next is 15 (1.5).", "1½+1½"),
 Q("Find the 20th term of the sequence 3, 6, 9, … and explain.", "Multiples of 3: $3\\times20=60$ (3).", "1+2"),
 Q("Why does the powers-of-2 sequence grow so fast? Give the first 8 terms.", "Each term doubles the previous one (1); 1, 2, 4, 8, 16, 32, 64, 128 (2).", "1+2"),
 Q("Write a rule of your own for a number pattern and give its first five terms.", "Any valid rule with five correct terms, e.g. multiply by 3: 1, 3, 9, 27, 81.", "1+2"),
 Q("What is the connection between the number of sides of a regular polygon and the counting numbers?", "A regular polygon has 3, 4, 5, … sides (1.5); the sides increase by one each time just like counting numbers from 3 (1.5).", "1½+1½"),
 Q("Hexagonal numbers are 1, 7, 19, 37. Find the differences between consecutive ones and describe the pattern.", "6, 12, 18 (1.5); the differences are multiples of 6 (1.5).", "1½+1½"),
 Q("Why do mathematicians study patterns?", "Patterns help make predictions (1); explain nature and science (1); lead to new ideas and theories (1).", "1+1+1"),
 Q("Find the sum $1+2+3+4+3+2+1$ and describe the pattern.", "16 (1); adding counting numbers up and down gives square numbers (2).", "1+2"),
 Q("How can a picture help us understand a number pattern? Illustrate with squares.", "Pictures make the relation visible (1.5); example of dots in squares for 1, 4, 9 (1.5).", "1½+1½"),
 Q("Write the Virahānka numbers up to 55. Which term is the sum of 13 and 21?", "1, 2, 3, 5, 8, 13, 21, 34, 55 (2); 34 (1).", "2+1"),
 Q("Which is greater: the 7th square number or the 5th cube number? Show working.", "$7^2=49$, $5^3=125$ (2); so the 5th cube is greater (1).", "2+1"),
 Q("Explain how the Koch snowflake is built by repeating a rule.", "Start with a triangle (1); replace each line segment by a speed bump (1); repeat and get a snowflake-like shape (1).", "1+1+1"),
 Q("Find the 15th odd number and the sum of the first 15 odd numbers.", "29 (1); $15^2=225$ (2).", "1+2"),
 Q("Observe 1×1=1, 11×11=121, 111×111=12321. Predict 1111×1111.", "1234321 (2); pattern rises to the number of ones then falls (1).", "2+1"),
]
D = [
 Q("(i) Write the first eight triangular numbers. (ii) Show that two consecutive triangular numbers give a square. (iii) Draw the 4th triangular arrangement.", "(i) 1, 3, 6, 10, 15, 21, 28, 36 (2). (ii) e.g. 10+15 = 25 (1.5). (iii) Rows of 1, 2, 3, 4 dots (1.5).", "2+1½+1½"),
 Q("(i) Define square numbers and write the first ten. (ii) Show visually that 1+3+5+7 = 16. (iii) Find the sum of the first 12 odd numbers.", "(i) 1, 4, 9, 16, 25, 36, 49, 64, 81, 100 (2). (ii) L-layers forming 4 by 4 square (1.5). (iii) $12^2=144$ (1.5).", "2+1½+1½"),
 Q("(i) What is the Virahānka sequence? (ii) Write its first twelve terms. (iii) Where do you see this in nature?", "(i) Each term is the sum of the previous two (1.5). (ii) 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233 (2). (iii) Petals, spirals of sunflower seeds (1.5).", "1½+2+1½"),
 Q("(i) Write the sequences of cubes and powers of 2 up to six terms. (ii) Which grows faster? (iii) Give the 10th term of each.", "(i) 1, 8, 27, 64, 125, 216; 1, 2, 4, 8, 16, 32 (2). (ii) Powers of 2 grow faster later on (1.5). (iii) 1000 and 512 (1.5).", "2+1½+1½"),
 Q("<b>Case study:</b> A tile worker lays tiles in a triangle with 1 tile in the first row, 2 in the second, 3 in the third and so on. (i) How many tiles in row 7? (ii) How many tiles in the first 7 rows? (iii) Which sequence does the total follow? (iv) How many rows are needed for 36 tiles?", "(i) 7 (1). (ii) 28 (1). (iii) Triangular numbers (1). (iv) 8 rows (2).", "1+1+1+2"),
 Q("(i) Complete: 2, 6, 18, 54, __, __. (ii) State the rule. (iii) Find the 7th term.", "(i) 162, 486 (2). (ii) Multiply by 3 (1.5). (iii) $2\\times3^6=1458$ (1.5).", "2+1½+1½"),
 Q("(i) How many lines are there in complete graphs of 2 to 7 points? (ii) Name the sequence. (iii) Predict the number for 10 points.", "(i) 1, 3, 6, 10, 15, 21 (2). (ii) Triangular numbers (1). (iii) 45 (2).", "2+1+2"),
 Q("(i) Explain what a shape sequence is. (ii) Draw the first three shapes of a stacked-squares sequence. (iii) Find the number of small squares in the 5th shape.", "(i) Shapes following a rule (1). (ii) 1, 4, 9 squares (2). (iii) 25 (2).", "1+2+2"),
 Q("<b>Case study:</b> Meena saves ₹1 on day 1, ₹2 on day 2, ₹4 on day 3, doubling each day. (i) How much on day 6? (ii) What sequence is this? (iii) Total saved in 5 days? (iv) On which day does she first save more than ₹100?", "(i) ₹32 (1). (ii) Powers of 2 (1). (iii) ₹31 (1). (iv) Day 8 (₹128) (2).", "1+1+1+2"),
 Q("(i) Explain with dots why the sum 1+2+3+2+1 equals 9. (ii) Find 1+2+3+4+5+4+3+2+1. (iii) Generalise for a sum up to 10 and down.", "(i) Two triangles form a 3 by 3 square (2). (ii) 25 (1.5). (iii) 100 (1.5).", "2+1½+1½"),
 Q("(i) Make a table of the first 6 terms of the sequences: counting, odd, even, square. (ii) Compare the growth of odd and even numbers.", "(i) Correct table (3). (ii) Both increase by 2; odd numbers are one less than even (2).", "3+2"),
 Q("(i) What are hexagonal numbers? (ii) Find the first five. (iii) Find the differences and describe the pattern.", "(i) Dots arranged in hexagons (1). (ii) 1, 7, 19, 37, 61 (2). (iii) 6, 12, 18, 24 multiples of 6 (2).", "1+2+2"),
 Q("<b>Case study:</b> A pattern: Figure 1 has 3 matchsticks, Figure 2 has 5, Figure 3 has 7. (i) What is the rule? (ii) Matchsticks in Figure 10? (iii) Which figure uses 41? (iv) Which sequence is this?", "(i) Add 2 each time (1). (ii) 21 (1). (iii) Figure 20 (1). (iv) Odd numbers from 3 (2).", "1+1+1+2"),
 Q("(i) Show that 1+3+5+7+9+11 = 36 with a picture. (ii) What is the sum of the first 20 odd numbers? (iii) Is 169 the sum of some odd numbers starting from 1? How many?", "(i) 6 by 6 square (2). (ii) 400 (1.5). (iii) Yes; 13 (1.5).", "2+1½+1½"),
 Q("(i) Write a story problem that leads to a number pattern. (ii) Solve it for 6 terms. (iii) State the rule.", "Any valid situation with correct six terms and a stated rule.", "2+2+1"),
 Q("(i) Explain the idea of ‘mathematics is the study of patterns’. (ii) Give three examples from nature or daily life. (iii) Why is it important?", "(i) Sequences and shapes follow rules (2). (ii) Petals, honeycomb, calendar, rangoli (2). (iii) Predicts and explains (1).", "2+2+1"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
