from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
# A: quick multiplication with distributive (6)
for a, b, how in [(98, 12, "(100-2)"), (102, 15, "(100+2)"), (99, 25, "(100-1)"), (103, 17, "(100+3)"), (97, 14, "(100-3)"), (101, 36, "(100+1)")]:
    p = a * b
    A.append(M4(f"The value of ${a}\\times{b}$ is:", str(p), [str(p+b), str(p-b), str(p+10)], f"${how}\\times{b}$ using the distributive property"))
# A: squares via identities (6)
for n in [31, 49, 52, 68, 103, 97]:
    A.append(M4(f"The value of ${n}^2$ is:", str(n*n), [str(n*n+n), str(n*n-n), str(n*n+10)], f"Use $(a\\pm b)^2$"))
# A: difference of squares (5)
for a, b in [(53, 47), (86, 14), (105, 95), (72, 28), (64, 36)]:
    A.append(M4(f"The value of ${a}^2-{b}^2$ is:", str(a*a-b*b), [str((a-b)**2), str(a*a+b*b), str((a+b)**2)], r"$(a+b)(a-b)$"))
# A: expand (a+b)^2 for numbers (4)
for a, b in [(3, 5), (2, 7), (4, 9), (6, 1)]:
    A.append(M4(f"If $a={a}$ and $b={b}$, then $(a+b)^2$ equals:", str((a+b)**2), [str(a*a+b*b), str(a*a+b*b+a*b), str((a-b)**2)], r"$a^2+2ab+b^2$"))
# A: concepts (19)
A += [
 M4(r"$(a+b)^2$ equals:", r"$a^2+2ab+b^2$", [r"$a^2+b^2$", r"$a^2+ab+b^2$", r"$2a+2b$"], "Standard identity"),
 M4(r"$(a-b)^2$ equals:", r"$a^2-2ab+b^2$", [r"$a^2-b^2$", r"$a^2+2ab+b^2$", r"$a^2-ab+b^2$"], "Standard identity"),
 M4(r"$(a+b)(a-b)$ equals:", r"$a^2-b^2$", [r"$a^2+b^2$", r"$(a-b)^2$", r"$a^2-2ab+b^2$"], "Difference of squares"),
 M4("The property $a\\times(b+c)=a\\times b+a\\times c$ is called:", "distributive property", ["commutative property", "associative property", "closure property"], "Multiplication over addition"),
 M4("$7\\times8=8\\times7$ illustrates the:", "commutative property", ["distributive property", "associative property", "identity property"], "Order does not matter"),
 M4("$(3\\times4)\\times5=3\\times(4\\times5)$ illustrates the:", "associative property", ["commutative property", "distributive property", "inverse property"], "Grouping does not matter"),
 M4("The multiplicative identity is:", "1", ["0", "−1", "10"], "$a\\times1=a$"),
 M4("The product of any number and 0 is:", "0", ["1", "the number itself", "undefined"], "Zero property"),
 M4("$(x+3)(x+4)$ equals:", "$x^2+7x+12$", ["$x^2+12$", "$x^2+7x+7$", "$x^2+12x+7$"], "Distribute each term"),
 M4("The coefficient of $x$ in $(x+5)(x+2)$ is:", "7", ["10", "3", "5"], "$5+2$"),
 M4("The value of $(x+1)^2$ when $x=9$ is:", "100", ["81", "91", "99"], "$10^2$"),
 M4("The expression $a^2+2ab+b^2$ is the expansion of:", "$(a+b)^2$", ["$(a-b)^2$", "$a^2-b^2$", "$(a+b)(a-b)$"], "Identity"),
 M4("The common mistake in $(a+b)^2=a^2+b^2$ is:", "missing the term $2ab$", ["wrong sign", "extra $a$", "none of these"], "Mind the mistake"),
 M4("The value of $25\\times4\\times7$ using the best grouping is:", "700", ["350", "1400", "70"], "$(25\\times4)\\times7$"),
 M4("$-3\\times(4-6)$ equals:", "6", ["−6", "−30", "18"], "$-3\\times(-2)$"),
 M4("The area of a square of side $(x+2)$ is:", "$x^2+4x+4$", ["$x^2+4$", "$x^2+2x+4$", "$4x+4$"], "Expand"),
 M4("$101\\times99$ equals:", "9999", ["10000", "9899", "10001"], "$(100+1)(100-1)=10000-1$"),
 M4("$(a-b)^2$ is always:", "non-negative", ["negative", "zero", "odd"], "A square is never negative"),
 M4("The number of terms in the expansion of $(x+y)(p+q)$ is:", "4", ["2", "3", "6"], "$xp+xq+yp+yq$"),
]
assert len(A) == 40, len(A)
B = [
 Q("State the distributive property of multiplication over addition.", "$a(b+c)=ab+ac$ (2).", "2"),
 Q("Find $98\\times15$ using the distributive property.", "$(100-2)\\times15=1500-30=1470$ (2).", "2"),
 Q("Expand $(x+6)^2$.", "$x^2+12x+36$ (2).", "2"),
 Q("Expand $(2a-3)^2$.", "$4a^2-12a+9$ (2).", "2"),
 Q("Factorise $a^2-49$.", "$(a+7)(a-7)$ (2).", "2"),
 Q("Find $63\\times57$ using $(60+3)(60-3)$.", "$3600-9=3591$ (2).", "2"),
 Q("Is $(a+b)^2=a^2+b^2$? Verify with $a=2$, $b=3$.", "No: $25\\ne13$ (2).", "2"),
 Q("Write the commutative property with an example.", "$a\\times b=b\\times a$ (1); $6\\times9=9\\times6$ (1).", "1+1"),
 Q("Find $(x+3)(x+5)$.", "$x^2+8x+15$ (2).", "2"),
 Q("Find $(x-4)(x+4)$.", "$x^2-16$ (2).", "2"),
 Q("Simplify $15\\times27+15\\times73$.", "$15(27+73)=1500$ (2).", "2"),
 Q("Evaluate $52^2$ using $(50+2)^2$.", "$2500+200+4=2704$ (2).", "2"),
 Q("Find $19^2$ using $(20-1)^2$.", "$400-40+1=361$ (2).", "2"),
 Q("State the identity for $(a-b)^2$ and verify for $a=5$, $b=2$.", "$a^2-2ab+b^2$ (1); $9=25-20+4$ (1).", "1+1"),
 Q("Why is $0$ called the additive identity?", "Adding 0 to any number leaves it unchanged (2).", "2"),
 Q("Expand $(m+n)(m-n)$ and give the name of the identity.", "$m^2-n^2$ (1); difference of two squares (1).", "1+1"),
]
for a, b in [(41, 39), (68, 32), (97, 3), (205, 195), (73, 27), (111, 89)]:
    C.append(Q(f"Evaluate ${a}^2-{b}^2$ without calculating each square.", f"$(a+b)(a-b)=({a}+{b})({a}-{b})$ (2); $={a*a-b*b}$ (1).", "2+1"))
for n in [304, 99, 1002, 47, 205, 998]:
    nearest = round(n, -2) if n < 400 else round(n, -3 if n > 500 else -2)
    C.append(Q(f"Find ${n}^2$ using a suitable identity.", f"Write ${n}$ as a sum or difference near a round number (1); apply $(a\\pm b)^2$ (1); ${n}^2={n*n}$ (1).", "1+1+1"))
for p, q in [(3, 4), (5, 7), (2, 9), (6, 8), (4, 11)]:
    C.append(Q(f"Expand and simplify $(x+{p})(x+{q})$. Verify for $x=1$.", f"$x^2+{p+q}x+{p*q}$ (2); at $x=1$: $({1+p})({1+q})={(1+p)*(1+q)}=1+{p+q}+{p*q}$ (1).", "2+1"))
C += [
 Q("Mind the mistake: a student writes $(x+5)^2=x^2+25$. Find the mistake and correct it.", "The middle term $10x$ is missing (1.5); correct is $x^2+10x+25$ (1.5).", "1½+1½"),
 Q("Show that $(a+b)^2-(a-b)^2=4ab$.", "$(a^2+2ab+b^2)-(a^2-2ab+b^2)=4ab$ (3).", "3"),
 Q("Find the area of a square of side 4.5 m using $(4+0.5)^2$.", "$16+4+0.25=20.25$ m² (3).", "3"),
 Q("Multiply $(3x+2)(2x-5)$.", "$6x^2-15x+4x-10=6x^2-11x-10$ (3).", "3"),
]
C += [
 Q("Expand $(3m-2n)^2$ and find its value when $m=2$, $n=1$.", "$9m^2-12mn+4n^2$ (2); $36-24+4=16$ (1).", "2+1"),
 Q("A rectangle has length $(x+5)$ and breadth $(x-2)$. Find its area as an expression and at $x=6$.", "$x^2+3x-10$ (2); $44$ (1).", "2+1"),
 Q("Show by an example that $(a-b)^2\\ne a^2-b^2$.", "Take $a=5,b=2$: $9\\ne21$ (3).", "3"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Derive $(a+b)^2$ using an area model. (ii) Evaluate $73^2$ using it.", "(i) A square of side $a+b$ split into $a^2$, two $ab$ and $b^2$ (3). (ii) $(70+3)^2=4900+420+9=5329$ (2).", "3+2"),
 Q("(i) State the identity for $(a-b)^2$. (ii) Evaluate $196^2$ using $(200-4)^2$.", "(i) $a^2-2ab+b^2$ (2). (ii) $40000-1600+16=38416$ (3).", "2+3"),
 Q("(i) Prove $(a+b)(a-b)=a^2-b^2$. (ii) Compute $52\\times48$ and $103\\times97$ using it.", "(i) Expansion: $a^2-ab+ab-b^2$ (2). (ii) $2496$ and $9991$ (3).", "2+3"),
 Q("<b>Case study:</b> A square courtyard of side $(n+3)$ m has a square flower bed of side $n$ m at one corner. (i) Write the area of the courtyard. (ii) Write the area of the remaining part. (iii) Find it for $n=7$.", "(i) $(n+3)^2=n^2+6n+9$ (1). (ii) $6n+9$ (2). (iii) $51$ m² (2).", "1+2+2"),
 Q("(i) Expand $(2x+3y)^2$. (ii) Expand $(5a-4b)^2$. (iii) Find $x^2+y^2$ if $x+y=7$ and $xy=12$.", "(i) $4x^2+12xy+9y^2$ (1.5). (ii) $25a^2-40ab+16b^2$ (1.5). (iii) $49-24=25$ (2).", "1½+1½+2"),
 Q("(i) Multiply $(x+7)(x-3)$ and verify at $x=2$. (ii) Find the product $(2a+1)(a-4)$.", "(i) $x^2+4x-21$; at 2: $9\\times(-1)=-9=4+8-21$ (3). (ii) $2a^2-7a-4$ (2).", "3+2"),
 Q("<b>Case study:</b> A shopkeeper sells 98 notebooks at ₹ 24 each. (i) Find the total using the distributive property. (ii) If he sells 102 pens at ₹ 15, find that total. (iii) Find the combined total.", "(i) $(100-2)\\times24=2352$ (2). (ii) $(100+2)\\times15=1530$ (2). (iii) ₹ 3882 (1).", "2+2+1"),
 Q("(i) Find $a^2+b^2$ if $a-b=5$ and $ab=14$. (ii) Find $(a+b)^2$.", "(i) $25+28=53$ (3). (ii) $53+28=81$ (2).", "3+2"),
 Q("(i) Show that $(a+b)^2=(a-b)^2+4ab$. (ii) Use it to find $(15+9)^2-(15-9)^2$.", "(i) Expansion (3). (ii) $4\\times15\\times9=540$ (2).", "3+2"),
 Q("(i) State and illustrate the commutative, associative and distributive properties for multiplication. (ii) Which property is used in $18\\times25\\times4$?", "(i) Statements with numbers (3). (ii) Commutative and associative: $18\\times(25\\times4)=1800$ (2).", "3+2"),
 Q("<b>Case study:</b> A student multiplies $(a+b)(a+b)$ as $a^2+b^2$. (i) What is wrong? (ii) Test with $a=4$, $b=1$. (iii) Write the correct result.", "(i) The cross terms $ab+ab$ are lost (2). (ii) $25\\ne17$ (2). (iii) $a^2+2ab+b^2$ (1).", "2+2+1"),
 Q("(i) Find the product $(x^2+2)(x^2-2)$. (ii) Evaluate it at $x=3$.", "(i) $x^4-4$ (3). (ii) $77=11\\times7$ (2).", "3+2"),
 Q("(i) Evaluate $\\dfrac{86^2-14^2}{72}$. (ii) Evaluate $\\dfrac{58^2-42^2}{16}$.", "(i) $100\\times72/72=100$ (2.5). (ii) $100\\times16/16=100$ (2.5).", "2½+2½"),
 Q("(i) Express 40 as a difference of two squares. (ii) Express 99 as a difference of two squares in two ways.", "(i) $11^2-9^2=40$ (2). (ii) $50^2-49^2$ and $18^2-15^2$ (3).", "2+3"),
 Q("(i) Show $(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$ with $a=1,b=2,c=3$. (ii) Evaluate $(10+2+1)^2$.", "(i) $36=1+4+9+4+12+6$ (3). (ii) $169$ (2).", "3+2"),
 Q("<b>Case study:</b> A farmer has a square field of side 20 m. He extends one side by 3 m and shortens the other by 3 m. (i) New area? (ii) Compare with the original. (iii) What identity explains?", "(i) $23\\times17=391$ m² (2). (ii) $400-391=9$ m² less (1). (iii) $(a+b)(a-b)=a^2-b^2$ (2).", "2+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
