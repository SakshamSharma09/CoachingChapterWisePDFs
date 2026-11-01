from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
# A: think of a number trick (6)
for add, mul in [(5, 2), (3, 4), (7, 3), (4, 5), (6, 2), (8, 3)]:
    A.append(M4(f"Think of a number $n$. Add {add}, multiply by {mul}, then subtract {add*mul}. The result is:", f"${mul}n$", [f"${mul}n+{add}$", f"$n+{add}$", f"${add}n$"], f"${mul}(n+{add})-{add*mul}={mul}n$"))
# A: two-digit forms (4)
for a, b in [(3, 7), (5, 2), (8, 9), (6, 4)]:
    A.append(M4(f"The two-digit number with tens digit {a} and ones digit {b} can be written as:", f"$10\\times{a}+{b}$", [f"${a}+{b}$", f"${a}\\times{b}$", f"$10\\times{b}+{a}$"], "Place value"))
# A: reverse and add (3)
for a, b in [(3, 5), (4, 7), (2, 9)]:
    A.append(M4(f"The sum of {10*a+b} and its reverse {10*b+a} is:", str(11*(a+b)), [str(11*(a+b)+11), str(a+b), str(9*(a+b))], "$11(a+b)$"))
# A: number pyramid (4)
for r in [(4, 7, 2), (3, 5, 6), (8, 1, 9), (6, 6, 3)]:
    top = (r[0] + r[1]) + (r[1] + r[2])
    A.append(M4(f"In a number pyramid, each block is the sum of the two below it. The bottom row is {r[0]}, {r[1]}, {r[2]}. The top block is:", str(top), [str(top+r[1]), str(top-r[1]), str(sum(r)), str(top+2), str(top-3)], "Top = a + 2b + c"))
# A: expressions (10)
A += [
 M4("The algebraic expression for 'five more than twice a number $x$' is:", "$2x+5$", ["$5x+2$", "$2(x+5)$", "$x+10$"], "Translate"),
 M4("The expression $3(n+4)-2n$ simplifies to:", "$n+12$", ["$5n+12$", "$n+4$", "$n+7$"], "$3n+12-2n$"),
 M4("The sum of any two consecutive integers $n$ and $n+1$ is:", "odd", ["even", "a multiple of 4", "prime"], "$2n+1$"),
 M4("The sum of three consecutive integers is always divisible by:", "3", ["2", "4", "6"], "$3n+3$"),
 M4("Three consecutive even numbers starting with $2k$ are:", "$2k$, $2k+2$, $2k+4$", ["$2k$, $2k+1$, $2k+2$", "$k$, $k+2$, $k+4$", "$2k$, $3k$, $4k$"], "Even numbers differ by 2"),
 M4("The product of two numbers with a fixed sum is largest when the numbers are:", "equal (or as close as possible)", ["as different as possible", "one is zero", "both odd"], "Largest product"),
 M4("If $x+y=20$, the largest value of $xy$ is:", "100", ["96", "99", "120"], "10 × 10"),
 M4("A number is divisible by 9 if and only if the sum of its digits is divisible by:", "9", ["3", "6", "12"], "Divisibility rule"),
 M4("The number $100a+10b+c$ has digits:", "$a$, $b$, $c$", ["$a+b$, $c$", "$100$, $10$, 1", "$abc$ as product"], "Place value"),
 M4("The mean of $n$, $n+2$ and $n+4$ is:", "$n+2$", ["$n+6$", "$3n+6$", "$n+4$"], "(3n+6)/3"),
]
# A: grids (6)
for x in [5, 9, 12, 20, 31, 40]:
    A.append(M4(f"In a calendar, the dates in a $2\\times2$ block starting at {x} are {x}, {x+1}, {x+7}, {x+8}. Their sum is:", str(4*x+16), [str(4*x+8), str(4*x+14), str(4*x+18)], "$4x+16$"))
# A: misc (7)
A += [
 M4("If $n$ is any integer, $n^2+n$ is always:", "even", ["odd", "prime", "a square"], "$n(n+1)$ is a product of consecutive integers"),
 M4("The expression $(n+1)^2-n^2$ equals:", "$2n+1$", ["$2n$", "$n+1$", "1"], "Expand"),
 M4("$7\\times7-6\\times8$ equals:", "1", ["0", "2", "13"], "$n^2-(n-1)(n+1)=1$"),
 M4("For any integer $n$, $(n+2)^2-(n-2)^2$ equals:", "$8n$", ["$4n$", "$4$", "$8$"], "Expand"),
 M4("Which algebraic fact explains why $a\\times b=b\\times a$?", "commutativity", ["distributivity", "associativity", "closure"], "Property"),
 M4("The result of the trick 'Think of $n$, double it, add 10, halve, subtract $n$' is:", "5", ["10", "$n$", "0"], "$(2n+10)/2-n=5$"),
 M4("If a 3-digit number is written as $\\overline{aba}$ its value is:", "$101a+10b$", ["$a+b+a$", "$100a+b$", "$110a+b$"], "100a+10b+a"),
]
assert len(A) == 40, len(A)
B = [
 Q("Show that the trick 'Think of a number, add 7, double, subtract 14' always gives double the number.", "$2(n+7)-14=2n$ (2).", "2"),
 Q("Write a two-digit number $\\overline{ab}$ in algebraic form and its reverse.", "$10a+b$ and $10b+a$ (2).", "2"),
 Q("Show that the sum of a two-digit number and its reverse is divisible by 11.", "$11a+11b=11(a+b)$ (2).", "2"),
 Q("The bottom row of a number pyramid is 3, 5, 4. Find the top block.", "Second row 8, 9; top 17 (2).", "2"),
 Q("Show that the sum of three consecutive numbers is divisible by 3.", "$n+(n+1)+(n+2)=3(n+1)$ (2).", "2"),
 Q("Find the largest product of two numbers whose sum is 30.", "$15\\times15=225$ (2).", "2"),
 Q("Show that the difference of squares of consecutive numbers is odd.", "$(n+1)^2-n^2=2n+1$ (2).", "2"),
 Q("In a $2\\times2$ block of a calendar starting at $x$, write the sum of the four dates.", "$x+(x+1)+(x+7)+(x+8)=4x+16$ (2).", "2"),
 Q("Why is $n(n+1)$ always even?", "One of two consecutive integers is even (2).", "2"),
 Q("Explain why a number is divisible by 3 if the sum of its digits is.", "$100a+10b+c=99a+9b+(a+b+c)$; the first part is divisible by 3 (2).", "2"),
 Q("A trick: Think of $n$, multiply by 6, add 12, divide by 3, subtract $2n$. What is the answer?", "$4$ (2).", "2"),
 Q("Express 'the product of two consecutive even numbers' algebraically.", "$2n(2n+2)$ (2).", "2"),
 Q("Fill the pyramid: bottom row 2, 3, 5; find the top.", "5, 8; top 13 (2).", "2"),
 Q("Find the largest product of two whole numbers with sum 25.", "$12\\times13=156$ (2).", "2"),
 Q("Expand $(n+3)^2-n^2$.", "$6n+9$ (2).", "2"),
 Q("Write the expression for the sum of the first $n$ odd numbers.", "$n^2$ (2).", "2"),
]
for a, b, c in [(3, 5, 7), (2, 9, 4), (6, 1, 8), (4, 4, 9), (5, 8, 3), (7, 2, 6)]:
    C.append(Q(f"Use a number pyramid with bottom row {a}, {b}, {c}: find all rows and the top, and write the top in terms of the bottom numbers.", f"Second row {a+b}, {b+c} (1); top ${a+2*b+c}$ (1); top $=a+2b+c$ (1).", "1+1+1"))
for k in [4, 7, 9, 12, 15, 21]:
    C.append(Q(f"A $2\\times2$ block of a calendar has top-left date {k}. Find the four dates, their sum, and show sum $=4k+16$.", f"Dates {k}, {k+1}, {k+7}, {k+8} (1); sum ${4*k+16}$ (1); algebra check (1).", "1+1+1"))
for s in [18, 22, 30, 37]:
    a = s // 2; b = s - a
    C.append(Q(f"Two numbers add to {s}. Find the numbers that give the largest product and the product.", f"Choose equal or closest numbers (1); {a} and {b} (1); product ${a*b}$ (1).", "1+1+1"))
C += [
 Q("Show that 78 and its reverse add to a multiple of 11 and explain algebraically.", "$78+87=165=11\\times15$ (1.5); $11(a+b)$ (1.5).", "1½+1½"),
 Q("Show that the difference of a two-digit number and its reverse is a multiple of 9.", "$(10a+b)-(10b+a)=9(a-b)$ (3).", "3"),
]
C += [
 Q("Show that the trick 'Think of $n$, add 3, square, subtract $n^2$, subtract 9, divide by $n$' always gives 6.", "$(n+3)^2-n^2-9=6n$ (2); $6n/n=6$ (1).", "2+1"),
 Q("Prove that the sum of any three consecutive even numbers is a multiple of 6.", "$2n+(2n+2)+(2n+4)=6n+6=6(n+1)$ (3).", "3"),
 Q("A number pyramid has the top 25 and the bottom row $a$, 6, $c$ with $a=7$. Find $c$.", "$a+2\\times6+c=25$ (1.5); $c=6$ (1.5).", "1½+1½"),
 Q("Find the largest product of two whole numbers with sum 41 and verify against 20 × 21.", "$20\\times21=420$ (2); nearest equal pair (1).", "2+1"),
 Q("Show that $\\overline{ab}\\times11$ gives $a\\,(a+b)\\,b$ for $a+b<10$. Check 43×11.", "$11(10a+b)=100a+10(a+b)+b$ (2); $473$ (1).", "2+1"),
 Q("Find $x$ in the grid trick: sum of 2×2 block starting at $x$ equals 92.", "$4x+16=92$ (1.5); $x=19$ (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Show the number trick: 'Think of $n$, add 5, multiply by 3, subtract 15, divide by 3'. (ii) What does the trick give? (iii) Create a new trick giving 10 always.", "(i) $3(n+5)-15=3n$, $\\div3=n$ (2). (ii) Returns the original number (1). (iii) e.g. $(n+5)\\times2-2n=10$ (2).", "2+1+2"),
 Q("<b>Case study:</b> A teacher makes a number pyramid with bottom row $a$, $b$, $c$. (i) Write rows 2 and 3. (ii) If the bottom is 5, 2, 7, find the top. (iii) What should $b$ be for the top to be 30 if $a=6$ and $c=8$?", "(i) $a+b,\\,b+c$; $a+2b+c$ (2). (ii) 16 (1). (iii) $14+2b=30$, $b=8$ (2).", "2+1+2"),
 Q("(i) Prove that the sum of the four dates of a $2\\times2$ block of a calendar is $4x+16$. (ii) Can the sum be 100? 130?", "(i) $x+(x+1)+(x+7)+(x+8)$ (2). (ii) $4x=84$, $x=21$ yes; $4x=114$ no (3).", "2+3"),
 Q("(i) Prove that the product of two numbers with fixed sum is largest when they are equal. (ii) Find the largest area of a rectangle with perimeter 36 m.", "(i) $(s/2)^2-xy=((x-y)/2)^2\\ge0$ (3). (ii) 9×9=81 m² (2).", "3+2"),
 Q("<b>Case study:</b> A fence of 40 m is used to make a rectangular pen against a wall (three sides). (i) Write area in terms of width $w$ (ii) Find $w$ for maximum area. (iii) Find the maximum area.", "(i) $A=w(40-2w)$ (2). (ii) $w=10$ (2). (iii) 200 m² (1).", "2+2+1"),
 Q("(i) Show that $\\overline{abc}-\\overline{cba}$ is a multiple of 99. (ii) Verify with 721.", "(i) $99(a-c)$ (3). (ii) $721-127=594=99\\times6$ (2).", "3+2"),
 Q("(i) Prove that the sum of 5 consecutive integers is divisible by 5. (ii) Find the five numbers with sum 85.", "(i) $5(n+2)$ (3). (ii) 15, 16, 17, 18, 19 (2).", "3+2"),
 Q("<b>Case study:</b> Anu says: pick a 3-digit number, write it twice to get a 6-digit number; it is divisible by 7, 11, 13. (i) Test with 345. (ii) Explain algebraically. (iii) Test another.", "(i) $345345=345\\times1001$ (2). (ii) $1001=7\\times11\\times13$ (2). (iii) Another example (1).", "2+2+1"),
 Q("(i) Show that $n^2-1$ is divisible by 8 for any odd $n$. (ii) Check for $n=9$.", "(i) $(n-1)(n+1)$ is a product of two consecutive even numbers (3). (ii) $80=8\\times10$ (2).", "3+2"),
 Q("(i) Explain how grids of numbers (e.g. $3\\times3$ blocks) have a sum equal to 9 times the centre. (ii) Verify with centre 15.", "(i) Pair opposite entries symmetrically (3). (ii) Sum 135 (2).", "3+2"),
 Q("<b>Case study:</b> A magician asks: pick a two-digit number, subtract the sum of its digits, and the result is a multiple of 9. (i) Prove it. (ii) Test with 47. (iii) Why is it magic?", "(i) $10a+b-(a+b)=9a$ (2). (ii) $47-11=36$ (1). (iii) Always a multiple of 9 (2).", "2+1+2"),
 Q("(i) Find the maximum product of two numbers that sum to 48. (ii) Of three numbers summing to 30 (whole).", "(i) 576 (2). (ii) 1000 (3).", "2+3"),
 Q("(i) Show that the sum of two odd numbers is even and of an odd and an even is odd algebraically. (ii) Give an example.", "(i) $(2a+1)+(2b+1)=2(a+b+1)$ (3). (ii) $5+7=12$ (2).", "3+2"),
 Q("(i) Expand and simplify $(n+4)^2-(n-4)^2$. (ii) Evaluate for $n=9$.", "(i) $16n$ (3). (ii) 144 (2).", "3+2"),
 Q("<b>Case study:</b> In a $3\\times3$ calendar block starting at date $x$ (dates $x, x+1, x+2$ then $x+7$, etc.). (i) Write the centre. (ii) Show the sum is 9 times the centre. (iii) Find the sum if the centre is 17.", "(i) $x+8$ (1). (ii) Pair symmetric entries (2). (iii) 153 (2).", "1+2+2"),
 Q("(i) Why do divisibility tests work for 9 and 11? (ii) Decode: is 8,57,162 divisible by 11?", "(i) $10\\equiv1$ mod 9; $10\\equiv-1$ mod 11 (3). (ii) Digits 8,5,7,1,6,2: $(2+1+5)-(6+7+8)=-13$, no (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
