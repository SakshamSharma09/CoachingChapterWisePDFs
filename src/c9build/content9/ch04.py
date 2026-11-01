import sympy as sp
from lib import mcq, Q, OR
from mk9 import M4, build
x, y, z, a, b, c, p, q, r, n, m, s, t = sp.symbols("x y z a b c p q r n m s t")
L = sp.latex
def ex(e): return f"${L(sp.expand(e))}$"
def fa(e): return f"${L(sp.factor(e))}$"
def T(e): return f"${L(e)}$"
A = []; B = []; C = []; D = []
# A: (px+q)^2 (5)
for pp, qq in [(3, 4), (2, 5), (5, 2), (4, 3), (7, 1)]:
    w1 = (pp*x)**2 + qq**2; w2 = (pp*x)**2 + pp*qq*x + qq**2; w3 = (pp*x)**2 + 2*pp*qq*x - qq**2
    A.append(M4(f"Expand $({pp}x+{qq})^2$:", ex((pp*x+qq)**2), [ex(w1), ex(w2), ex(w3)], "$(a+b)^2=a^2+2ab+b^2$"))
# A: (px-q)^2 (3)
for pp, qq in [(2, 3), (5, 1), (3, 4)]:
    A.append(M4(f"Expand $({pp}x-{qq})^2$:", ex((pp*x-qq)**2), [ex((pp*x)**2 - qq**2), ex((pp*x)**2 + 2*pp*qq*x + qq**2), ex((pp*x)**2 - pp*qq*x + qq**2)], "$(a-b)^2=a^2-2ab+b^2$"))
# A: numeric squares (4)
for base, expr, val in [(43, "(40+3)^2", 1849), (29, "(30-1)^2", 841), (105, "(100+5)^2", 11025), (99, "(100-1)^2", 9801)]:
    A.append(M4(f"The value of ${base}^2$ using a suitable identity is:", str(val), [str(val + 20), str(val - 10), str(val + 100)], f"${base}^2={expr}$"))
# A: factor perfect squares (4)
for e, inner, wr in [(9*x**2 + 24*x + 16, 3*x + 4, [(3*x + 8)**2, (3*x - 4)**2, (9*x + 4)**2]),
                     (4*s**2 + 20*s*t + 25*t**2, 2*s + 5*t, [(2*s + 25*t)**2, (2*s - 5*t)**2, (4*s + 5*t)**2]),
                     (49*x**2 + 28*x*y + 4*y**2, 7*x + 2*y, [(7*x + 4*y)**2, (7*x - 2*y)**2, (49*x + 2*y)**2]),
                     (36*x**2 + 12*x + 1, 6*x + 1, [(6*x + 2)**2, (6*x - 1)**2, (36*x + 1)**2])]:
    A.append(M4(f"The expression ${L(sp.expand(e))}$ can be factorised as:", f"$\\left({L(inner)}\\right)^2$", [f"$\\left({L(w.base)}\\right)^2$" for w in wr], "identify $a^2+2ab+b^2=(a+b)^2$"))
# A: (x+a)(x+b) (4)
for u, v in [(3, 4), (5, -2), (-6, -3), (7, 8)]:
    A.append(M4(f"$(x{u:+d})(x{v:+d})$ equals:", ex((x+u)*(x+v)), [ex(x**2 + (u*v)*x + (u+v)), ex(x**2 + (u-v)*x + u*v), ex(x**2 + (u+v)*x - u*v)], "$(x+a)(x+b)=x^2+(a+b)x+ab$"))
# A: factor x^2+px+q (5)
for u, v in [(5, 6), (-2, -3), (-7, 6), (4, -9), (-6, -7)]:
    e = x**2 + (u+v)*x + u*v
    A.append(M4(f"Factorise ${L(sp.expand(e))}$:", fa(e), [T((x - u)*(x - v)), T((x + u)*(x - v)), T((x - u)*(x + v))], "find $a,b$ with $a+b$ = middle coefficient and $ab$ = constant"))
# A: difference of squares (3)
for u, v in [(7*x + 2, 7*x - 2), (3*s + 5*t, 3*s - 5*t), (2*n + 7, 2*n - 7)]:
    A.append(M4(f"$({L(u)})({L(v)})$ equals:", ex(u*v), [ex(u**2), ex(v**2), T(sp.expand(u*v) + 4)], "$(a+b)(a-b)=a^2-b^2$"))
# A: cubes (3)
A.append(M4(r"$(x+2)^3$ equals:", ex((x+2)**3), [ex(x**3 + 8), ex(x**3 + 2*x**2 + 4*x + 8), ex(x**3 + 6*x**2 + 6*x + 8)], "$(a+b)^3=a^3+3a^2b+3ab^2+b^3$"))
A.append(M4(r"$(2x-1)^3$ equals:", ex((2*x-1)**3), [ex(8*x**3 - 1), ex(8*x**3 + 12*x**2 + 6*x + 1), ex(8*x**3 - 6*x**2 + 3*x - 1)], "$(a-b)^3=a^3-3a^2b+3ab^2-b^3$"))
A.append(M4(r"The side of a cube of volume $p^3+6p^2q+12pq^2+8q^3$ is:", r"$p+2q$", [r"$p+q$", r"$p+4q$", r"$2p+q$"], "$a=p,\\ b=2q$"))
# A: three-variable identities (3)
A.append(M4(r"The coefficient of $ab$ in $(a+b+c)^2$ is:", "2", ["1", "3", "4"], "$(a+b+c)^2=a^2+b^2+c^2+2ab+2bc+2ca$"))
A.append(M4(r"If $x+y+z=0$, then $x^3+y^3+z^3$ equals:", "$3xyz$", ["$0$", "$xyz$", "$x+y+z$"], "from $x^3+y^3+z^3-3xyz=(x+y+z)(\\ldots)$"))
A.append(M4(r"$(x-y)(x^2+xy+y^2)$ equals:", "$x^3-y^3$", ["$x^3+y^3$", "$(x-y)^3$", "$x^2-y^2$"], "standard identity"))
# A: hand (5)
A += [
 M4(r"Which of the following is an identity?", r"$(x+y)^2=x^2+2xy+y^2$", [r"$x^2-1=24$", r"$x+5=9$", r"$2x=10$"], "true for all values of the variables"),
 M4(r"If $a=10$ and $b=2$, then $(a+b)^2-(a^2+b^2)$ equals:", "40", ["0", "20", "144"], "$2ab=40$"),
 M4(r"Śhrīdharāchārya's method gives $55^2=(55+5)(55-5)+5^2=$", "3025", ["3000", "3050", "2925"], "$60\\times50+25$"),
 M4(r"The three consecutive squares 25, 36, 49: (smallest + largest) − 2 × middle equals:", "2", ["0", "1", "4"], "$(n-1)^2+(n+1)^2-2n^2=2$"),
 M4(r"A student writes $(a+b)^2=a^2+b^2$. The correct response is:", r"Incorrect; the term $2ab$ is missing", ["Correct for all $a,b$", "Correct only for $a>b$", "Correct for all positive $a,b$"], "$(a+b)^2=a^2+2ab+b^2$"),
]
A.append(M4(r"$(x+y+z)^2$ contains how many terms when fully expanded (no like terms)?", "6", ["3", "4", "9"], "$x^2,y^2,z^2,2xy,2yz,2zx$"))
assert len(A) == 40, len(A)

# B (16): 2 marks
for inner in [7*x + 4*y, sp.Rational(5, 2)*p + sp.Rational(3, 2)*q, 3*s - 4*t, x + sp.Rational(1, 2)*y]:
    B.append(Q(f"Expand $\\left({L(inner)}\\right)^2$ using a suitable identity.", f"{ex(inner**2)}", "2"))
for e in [9*x**2 + 24*x*y + 16*y**2, 4*s**2 + 20*s*t + 25*t**2, 16*y**2 - 24*y + 9, 49*x**2 + 14*x*y + y**2]:
    B.append(Q(f"Factorise ${L(sp.expand(e))}$.", f"{fa(e)}", "2"))
for e in [x**2 - 7*x + 12, s**2 - 11*s + 24, x**2 + 11*x + 30, x**2 - 5*x + 6]:
    B.append(Q(f"Factorise ${L(sp.expand(e))}$ by splitting the middle term.", f"{fa(e)}", "2"))
B += [
 Q(r"Evaluate $119^2$ using $(a+b+c)^2$.", r"$119^2=(100+10+9)^2=10000+100+81+2000+1800+180=14161$.", "2"),
 Q(r"Evaluate $23\times17$ using a suitable identity.", r"$23\times17=(20+3)(20-3)=400-9=391$.", "2"),
 Q(r"Find $55^2$ and $65^2$ using $a^2=(a+b)(a-b)+b^2$ with $b=5$.", r"$55^2=60\times50+25=3025$; $65^2=70\times60+25=4225$.", "1+1"),
 Q(r"Show that the identity $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ holds for $a=2,\ b=1$.", r"LHS $=27$; RHS $=8+12+6+1=27$ ✓.", "1+1"),
]
assert len(B) == 16, len(B)

# C (24): 3 marks
for e in [9*x**2 + 4*y**2 + z**2 + 12*x*y + 6*x*z + 4*y*z]:
    C.append(Q(f"Factorise ${L(e)}$.", f"Write as $(3x)^2+(2y)^2+z^2+2(3x)(2y)+2(3x)(z)+2(2y)(z)=(3x+2y+z)^2$. Answer: {fa(e)}", "3"))
C.append(Q(r"Expand $(p+3q+7r)^2$.", f"{ex((p+3*q+7*r)**2)}", "3"))
C.append(Q(r"Expand $(3x-2y+4z)^2$.", f"{ex((3*x-2*y+4*z)**2)}", "3"))
C.append(Q(r"Expand $(2x+3)^3$ using $(a+b)^3=a^3+3a^2b+3ab^2+b^3$.", f"$a=2x,\\ b=3$: {ex((2*x+3)**3)}", "3"))
C.append(Q(r"Expand $(3m-2n)^3$.", f"{ex((3*m-2*n)**3)}", "3"))
C.append(Q(r"Factorise $8n^3-60n^2m+150nm^2-125m^3$.", r"$(2n)^3-3(2n)^2(5m)+3(2n)(5m)^2-(5m)^3=(2n-5m)^3$.", "3"))
C.append(Q(r"What is the side of the cube whose volume is $p^3+6p^2q+12pq^2+8q^3$?", r"$(p)^3+3p^2(2q)+3p(2q)^2+(2q)^3=(p+2q)^3$, so the side is $p+2q$.", "3"))
C.append(Q(r"Simplify $\dfrac{x^2-7x+12}{5x^2+5x-100}$, assuming the denominator is non-zero.", r"Numerator $=(x-3)(x-4)$; denominator $=5(x^2+x-20)=5(x-4)(x+5)$. Cancelling $(x-4)$: $\dfrac{x-3}{5(x+5)}$.", "1+1+1"))
C.append(Q(r"Simplify $\dfrac{36s^2-12st+t^2}{t^2+2ts-48s^2}$ (denominator $\ne0$).", r"Numerator $=(6s-t)^2$. Denominator: $a+b=2s,\ ab=-48s^2\Rightarrow(t+8s)(t-6s)=-(6s-t)(t+8s)$. So the fraction $=\dfrac{(6s-t)^2}{(t-6s)(t+8s)}=-\dfrac{6s-t}{t+8s}=\dfrac{t-6s}{t+8s}$.", "1+1+1"))
C.append(Q(r"Simplify $\dfrac{p^4-16}{p^2-4p+4}$ ($p\ne2$).", r"$p^4-16=(p^2-4)(p^2+4)=(p-2)(p+2)(p^2+4)$; denominator $=(p-2)^2$. Result: $\dfrac{(p+2)(p^2+4)}{p-2}$.", "1+1+1"))
C.append(Q(r"Using $x^3+y^3+z^3-3xyz=(x+y+z)(x^2+y^2+z^2-xy-yz-zx)$ show that if $x+y+z=0$ then $x^3+y^3+z^3=3xyz$. Evaluate $(-5)^3+2^3+3^3$.", r"If $x+y+z=0$ the right side is 0 ⇒ $x^3+y^3+z^3=3xyz$. Here $-5+2+3=0$, so the sum $=3(-5)(2)(3)=-90$. (Check: $-125+8+27=-90$ ✓)", "1+1+1"))
C.append(Q(r"The sum of three numbers is 10 and the sum of their squares is 38. Find $xy+yz+zx$.", r"$(x+y+z)^2=100=38+2(xy+yz+zx)\Rightarrow xy+yz+zx=31$.", "1+1+1"))
C.append(Q(r"Prove that the difference of the squares of two consecutive integers equals their sum.", r"$(n+1)^2-n^2=2n+1=n+(n+1)$ ✓.", "1+1+1"))
C.append(Q(r"Show that $(a+b)^2+(a-b)^2=2(a^2+b^2)$ and use it to find $(105)^2+(95)^2$.", r"LHS $=2a^2+2b^2$ ✓. With $a=100,b=5$: $105^2+95^2=2(10000+25)=20050$.", "1+1+1"))
C.append(Q(r"Without multiplying directly, find $104\times96$ and $98^2$.", r"$104\times96=(100+4)(100-4)=9984$; $98^2=(100-2)^2=10000-400+4=9604$.", "1+1+1"))
C.append(Q(r"A square has side $(2x+3)$ units. Find its area and perimeter.", f"Area $=(2x+3)^2=4x^2+12x+9$ sq. units; perimeter $=4(2x+3)=8x+12$ units.", "2+1"))
C.append(Q(r"Is $(a+b-c)^2+(a-b+c)^2+(a-b-c)^2=2a^2+2b^2+2c^2$ an identity? Test with $a=1,b=1,c=1$.", r"For $a=b=c=1$: $1+1+1=3$ while RHS $=6$. So it is NOT an identity.", "2+1"))
C.append(Q(r"Saira arranges a square of side $x$, 8 strips $x\times1$ and 15 unit squares into a rectangle. Find its length and breadth.", r"Area $=x^2+8x+15=(x+3)(x+5)$: sides $x+5$ and $x+3$.", "2+1"))
C.append(Q(r"The breadth of a pool is 4 m less than its length and its area is 96 m². Find its dimensions.", r"$x(x-4)=96\Rightarrow x^2-4x-96=0\Rightarrow(x-12)(x+8)=0$. $x=12$ m (reject −8); breadth 8 m.", "1+1+1"))
C.append(Q(r"Factorise $r^2-r-42$ and $x^2+7x+12$.", r"$r^2-r-42=(r-7)(r+6)$; $x^2+7x+12=(x+3)(x+4)$.", "1½+1½"))
C.append(Q(r"Fill the blanks: $(px+a)(qx+b)=(\_\_)x^2+(\_\_)x+\_\_$. Verify with $(2x+3)(3x+1)$.", r"$=pqx^2+(pb+qa)x+ab$. For $(2x+3)(3x+1)$: $6x^2+(2+9)x+3=6x^2+11x+3$.", "1+2"))
C.append(Q(r"Factorise $6x^2+7x+2$ by splitting the middle term.", r"$6\times2=12$; split $7x=3x+4x$: $6x^2+3x+4x+2=3x(2x+1)+2(2x+1)=(2x+1)(3x+2)$.", "1+1+1"))
C.append(Q(r"Use $(x-y)(x^2+xy+y^2)=x^3-y^3$ to factorise $27a^3-8b^3$.", r"$(3a)^3-(2b)^3=(3a-2b)(9a^2+6ab+4b^2)$.", "1+2"))
C.append(Q(r"If $x+\frac1x=3$, find $x^2+\frac1{x^2}$ and $\left(x-\frac1x\right)^2$.", r"$x^2+\frac1{x^2}=\left(x+\frac1x\right)^2-2=9-2=7$. $\left(x-\frac1x\right)^2=x^2+\frac1{x^2}-2=5$.", "1+1+1"))
assert len(C) == 24, len(C)

# D (16): 5 marks
D += [
 Q(r"(i) Expand $(5x+2y)^2$ and find $43^2$ using the identity. (ii) Show that $(a+b)^2>a^2+b^2$ when $ab>0$ and give an example of $a,b$ with $(a+b)^2<a^2+b^2$.", r"(i) $25x^2+20xy+4y^2$; $43^2=(40+3)^2=1849$. (ii) $(a+b)^2-(a^2+b^2)=2ab>0$ when $ab>0$. For $ab<0$, e.g. $a=3,b=-1$: $4<10$.", "2+3"),
 Q(r"<b>Case study:</b> Three consecutive square numbers are $(n-1)^2$, $n^2$, $(n+1)^2$. (i) Add the smallest and largest and subtract twice the middle one for $n=6$. (ii) Prove the result is always 2. (iii) Does the pattern hold for consecutive even-square numbers $(n-2)^2,n^2,(n+2)^2$? Find (smallest + largest) − 2 × middle.", r"(i) $25+49-72=2$. (ii) $(n-1)^2+(n+1)^2-2n^2=2$ (2). (iii) $(n-2)^2+(n+2)^2-2n^2=8$ — a constant 8, not 2.", "1+2+2"),
 Q(r"(i) Factorise $9a^2+b^2+4c^2-6ab+12ac-4bc$. (ii) Factorise $16s^2+25t^2-40st$.", r"(i) $(3a-b+2c)^2$ [check: $9a^2+b^2+4c^2-6ab+12ac-4bc$ ✓]. (ii) $(4s-5t)^2$.", "3+2"),
 Q(r"<b>Case study:</b> Saira arranges 1 square of side $x$, 8 rectangular strips of $x\times1$ and 15 unit squares into a rectangle. A rectangular pool has breadth 4 m less than its length and area 96 m². (i) Find Saira's rectangle's length and breadth. (ii) Form and solve the equation for the pool. (iii) Find the pool's perimeter.", r"(i) $x^2+8x+15=(x+3)(x+5)$. (ii) $x(x-4)=96\Rightarrow(x-12)(x+8)=0$, so $x=12$ m, breadth 8 m. (iii) $2(12+8)=40$ m.", "1+3+1"),
 Q(r"(i) Expand $(x+2)^3$. (ii) Factorise $x^3-8$. (iii) Evaluate $103^3$ using $(100+3)^3$.", r"(i) $x^3+6x^2+12x+8$. (ii) $(x-2)(x^2+2x+4)$. (iii) $10^6+3\times10^4\times3+3\times100\times9+27=1000000+90000+2700+27=1092727$.", "1+2+2"),
 Q(r"The sum of three numbers is 10, the sum of their squares is 38 and their product is 25. (i) Find $xy+yz+zx$. (ii) Hence find the sum of their cubes.", r"(i) $100=38+2(xy+yz+zx)\Rightarrow31$. (ii) $x^3+y^3+z^3-3xyz=(10)(38-31)=70\Rightarrow x^3+y^3+z^3=70+75=145$.", "2+3"),
 Q(r"Simplify (i) $\dfrac{3p^2-3pq-18q^2}{p^2+3pq-10q^2}$ and (ii) $\dfrac{4y^2-20yz+25z^2}{25z^2-4y^2}$ (denominators non-zero).", r"(i) Numerator $=3(p-3q)(p+2q)$; denominator $=(p+5q)(p-2q)$ — check: $p^2+3pq-10q^2=(p+5q)(p-2q)$. Result $\dfrac{3(p-3q)(p+2q)}{(p+5q)(p-2q)}$. (ii) $\dfrac{(2y-5z)^2}{(5z-2y)(5z+2y)}=\dfrac{5z-2y}{5z+2y}$.", "3+2"),
 Q(r"<b>Case study:</b> Śhrīdharāchārya (750 CE) gave $a^2=(a+b)(a-b)+b^2$ for quick squaring. (i) Find $35^2$, $65^2$ and $85^2$ with $b=5$. (ii) Observe the pattern in the units and tens of these squares. (iii) Find $105^2$ using the same method.", r"(i) $35^2=40\times30+25=1225$; $65^2=70\times60+25=4225$; $85^2=90\times80+25=7225$. (ii) Each ends in 25; the leading digits are $n(n+1)$ for numbers $n5$ ($3\times4=12$, $6\times7=42$, $8\times9=72$). (iii) $105^2=110\times100+25=11025$.", "2+2+1"),
 Q(r"(i) Prove $(a+b)^3=a^3+3a^2b+3ab^2+b^3$ using $(a+b)(a+b)^2$. (ii) Deduce $(a-b)^3$ and use it to compute $97^3$.", r"(i) $(a+b)(a^2+2ab+b^2)=a^3+2a^2b+ab^2+a^2b+2ab^2+b^3=a^3+3a^2b+3ab^2+b^3$. (ii) Replace $b$ by $-b$: $a^3-3a^2b+3ab^2-b^3$. $97^3=(100-3)^3=1000000-90000+2700-27=912673$.", "3+2"),
 Q(r"Factorise (i) $x^2-5x+6$, (ii) $r^2-r-42$, (iii) $6x^2+7x+2$, (iv) $10x^2-11x-6$.", r"(i) $(x-2)(x-3)$; (ii) $(r-7)(r+6)$; (iii) $(2x+1)(3x+2)$; (iv) $(2x-3)(5x+2)$ [since $10x^2-15x+4x-6$].", "1+1+1+2"),
 Q(r"<b>Case study:</b> A cube has edge $(a+b)$. (i) Split it into 2 cubes and 6 cuboids and state their volumes. (ii) Write the identity. (iii) If $a=2$, $b=3$, verify the identity numerically.", r"(i) Cubes $a^3$ and $b^3$; three cuboids $a\times a\times b$ (vol. $a^2b$) and three $a\times b\times b$ (vol. $ab^2$). (ii) $(a+b)^3=a^3+3a^2b+3ab^2+b^3$. (iii) $5^3=125$; $8+3(4)(3)+3(2)(9)+27=8+36+54+27=125$ ✓.", "2+1+2"),
 Q(r"Prove that $(x+y+z)(x^2+y^2+z^2-xy-yz-zx)=x^3+y^3+z^3-3xyz$ and evaluate $1^3+2^3+(-3)^3$.", r"Multiplying out and cancelling cross terms gives $x^3+y^3+z^3-3xyz$ (3). Since $1+2-3=0$, the sum $=3(1)(2)(-3)=-18$ (2). (Check: $1+8-27=-18$ ✓.)", "3+2"),
 Q(r"Find the values of $(i)\ 1104^2$ and $(ii)\ 198^2$ using suitable identities. (iii) Which identity makes each easier?", r"(i) $(1100+4)^2=1210000+8800+16=1218816$. (ii) $(200-2)^2=40000-800+4=39204$. (iii) $(a+b)^2$ for (i), $(a-b)^2$ for (ii).", "2+2+1"),
 Q(r"<b>Case study:</b> A rectangular garden has length $(2x+3)$ m and breadth $(3x+1)$ m. (i) Write and simplify its area. (ii) Find the area when $x=4$. (iii) A square flower bed has side $(x+2)$; expand its area and compare with a $(x+3)\times(x+1)$ plot.", r"(i) $6x^2+11x+3$. (ii) $96+44+3=143$ m$^2$ (check $11\times13=143$ ✓). (iii) $(x+2)^2=x^2+4x+4$; $(x+3)(x+1)=x^2+4x+3$ — the square is larger by 1 sq. unit.", "2+1+2"),
 Q(r"<b>Case study:</b> Explore $(x-y)(x^2+xy+y^2)$ and $(x+y)(x^2-xy+y^2)$. (i) Multiply and state the identities. (ii) Factorise $27p^3+8q^3$ and $64-a^3$.", r"(i) $x^3-y^3$ and $x^3+y^3$. (ii) $(3p+2q)(9p^2-6pq+4q^2)$; $(4-a)(16+4a+a^2)$.", "3+2"),
 Q(r"If $x+\frac1x=5$, find $x^2+\frac1{x^2}$ and $x^3+\frac1{x^3}$.", r"$x^2+\frac1{x^2}=25-2=23$. $x^3+\frac1{x^3}=\left(x+\frac1x\right)^3-3\left(x+\frac1x\right)=125-15=110$.", "2+3"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
