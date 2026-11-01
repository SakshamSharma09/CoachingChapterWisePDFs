from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def dd(c, extra=()):
    out = []
    for v in [c+1, c-1, 2*c, c+10, c-10, -c, c+2, c-2, c+5, c-5, *extra]:
        if v != c and v not in out: out.append(v)
    return out
def sg(x):
    return str(x).replace("-", "−")
A = []; B = []; C = []; D = []
# explicit value (6)
for (txt, f, n) in [("3n-4", lambda n: 3*n-4, 12), ("2-5n", lambda n: 2-5*n, 6), ("5n-3", lambda n: 5*n-3, 10), ("n^2-2n+3", lambda n: n*n-2*n+3, 7), ("4n+1", lambda n: 4*n+1, 20), ("7-2n", lambda n: 7-2*n, 15)]:
    v = f(n)
    A.append(M4(f"For the sequence $t_n={txt}$, the value of $t_{{{n}}}$ is:", sg(v), [sg(x) for x in dd(v, [f(n+1), f(n-1)])[:3]], f"substitute $n={n}$"))
# which term (5)
for (a, b, tv) in [(5, -3, 607), (2, -1, 137), (3, -7, 332), (4, -3, 97), (7, 2, 261)]:
    n = (tv-b)//a; assert a*n+b == tv
    lbl = f"{a}n{'+' if b>0 else '-'}{abs(b)}"
    A.append(M4(f"Which term of the sequence $t_n={lbl}$ is ${tv}$?", f"$n={n}$", [f"$n={x}$" for x in (n+1, n-1, n+2)], f"${lbl}={tv}\\Rightarrow n={n}$"))
# AP nth term (6)
for a, d, n in [(3, 5, 10), (21, -3, 15), (11, -3, 9), (2, 4, 25), (-5, 4, 12), (7, 6, 11)]:
    v = a+(n-1)*d
    A.append(M4(f"The {n}th term of the AP ${sg(a)}, {sg(a+d)}, {sg(a+2*d)},\\ldots$ is:", sg(v), [sg(x) for x in dd(v, [a+n*d, a+(n-2)*d])[:3]], f"$a+(n-1)d={sg(a)}+{n-1}\\times({sg(d)})={sg(v)}$"))
# sum (5)
for lbl, v, why in [("the first 10 terms of the AP with $a=2,\\ d=3$", 155, "$\\frac{10}2(2\\cdot2+9\\cdot3)=155$"), ("the first 20 natural numbers", 210, "$\\frac{20\\cdot21}2$"),
                    ("the first 50 natural numbers", 1275, "$\\frac{50\\cdot51}2$"), ("the first 100 natural numbers", 5050, "$\\frac{100\\cdot101}2$"), ("the first 8 terms of the AP with $a=5,\\ d=5$", 180, "$\\frac82(10+35)=180$")]:
    A.append(M4(f"The sum of {lbl} is:", str(v), [str(x) for x in dd(v, [v+5, v-5, v*2])[:3]], why))
# GP term (5)
for a, r, n in [(3, 2, 6), (2, 3, 5), (5, 2, 7), (4, 3, 4), (1, -2, 7)]:
    v = a*r**(n-1)
    A.append(M4(f"The {n}th term of the GP with first term ${a}$ and common ratio ${sg(r)}$ is:", sg(v), [sg(x) for x in dd(v, [a*r**n, a*r**(n-2), a*(r*n)])[:3]], f"$ar^{{n-1}}={a}\\times({sg(r)})^{{{n-1}}}={sg(v)}$"))
# recursive (4)
A += [
 M4(r"If $u_1=1$ and $u_n=2u_{n-1}+3$, then $u_4$ is:", "29", ["13", "15", "27"], "1, 5, 13, 29"),
 M4(r"If $s_1=3$ and $s_n=s_{n-1}(s_{n-1}-1)$, then $s_3$ is:", "30", ["6", "870", "18"], "3, 6, 30"),
 M4(r"In the Virahānka–Fibonacci sequence $1,2,3,5,8,13,\ldots$ the 7th term is:", "21", ["20", "18", "34"], "13+8=21"),
 M4(r"If $T_1=1,T_2=2,T_3=4$ and $T_n=T_{n-1}+T_{n-2}+T_{n-3}$, then $T_5$ is:", "13", ["11", "14", "12"], "$T_4=7$, $T_5=4+2+7=13$"),
]
# classify (4)
A += [
 M4(r"The sequence $2,5,8,11,\ldots$ is:", r"an AP with $d=3$", [r"a GP with $r=3$", "neither an AP nor a GP", r"an AP with $d=2$"], "constant difference 3"),
 M4(r"The sequence $3,6,12,24,\ldots$ is:", r"a GP with $r=2$", [r"an AP with $d=3$", "neither an AP nor a GP", r"a GP with $r=3$"], "constant ratio 2"),
 M4(r"The sequence $1,4,9,16,\ldots$ is:", "neither an AP nor a GP", ["an AP", "a GP", "both an AP and a GP"], "differences 3,5,7; ratios 4, 2.25, …"),
 M4(r"The sequence $1,3,6,10,15,\ldots$ (triangular numbers) is:", "neither an AP nor a GP", ["an AP with d = 2", "a GP with r = 3", "an AP with d = 5"], "differences 2,3,4,5 are not constant"),
]
# hand (5)
A += [
 M4("The 10th triangular number is:", "55", ["45", "50", "66"], "$1+2+\\cdots+10$"),
 M4("The sum of the first $n$ odd numbers is:", r"$n^2$", [r"$2n$", r"$n(n+1)$", r"$\frac{n(n+1)}2$"], "$1+3+5+\\cdots+(2n-1)=n^2$"),
 M4("In a geometric progression, the constant multiplier is called the:", "common ratio", ["common difference", "first term", "nth term"], "definition"),
 M4("The number of black triangles at Stage $n$ of the Sierpiński triangle is:", r"$3^n$", [r"$2^n$", r"$3n$", r"$4^n$"], "each black triangle becomes three"),
 M4("The Virahānka–Fibonacci sequence was first written down in connection with:", "Prakrit metre and poetry", ["planetary motion", "the area of circles", "calendar design"], "7th century CE, Vṛttajātisamuchaya"),
]
assert len(A) == 6+5+6+5+5+4+4+5 == 40, len(A)
# B (16)
B += [
 Q(r"Find the first five terms of the sequence $t_n=3n-4$.", r"$t_1=-1,\ t_2=2,\ t_3=5,\ t_4=8,\ t_5=11$.", "1+1"),
 Q(r"Find the first five terms of $t_n=2-5n$.", r"$-3,\ -8,\ -13,\ -18,\ -23$.", "1+1"),
 Q(r"Find the first five terms of $t_n=n^2-2n+3$.", r"$t_1=2,\ t_2=3,\ t_3=6,\ t_4=11,\ t_5=18$.", "1+1"),
 Q(r"Find the 10th and 15th terms of $t_n=5n-3$.", r"$t_{10}=47$ and $t_{15}=72$.", "1+1"),
 Q(r"Determine whether 97 and 172 are terms of $t_n=5n-3$.", r"$5n-3=97\Rightarrow n=20$ — yes (20th term). $5n-3=172\Rightarrow n=35$ — yes (35th term).", "1+1"),
 Q(r"Which term of $t_n=5n-3$ is 607?", r"$5n-3=607\Rightarrow5n=610\Rightarrow n=122$; the 122nd term.", "1+1"),
 Q(r"A sequence is given by $t_1=-5$, $t_{n+1}=t_n+3$. Write the first five terms and decide whether 52 is a term.", r"$-5,-2,1,4,7$ (1). $t_n=-5+3(n-1)=52\Rightarrow n=20$, so 52 is the 20th term (1).", "1+1"),
 Q(r"Let $T_1=1,T_2=2,T_3=4$ and $T_n=T_{n-1}+T_{n-2}+T_{n-3}$. Find $T_4,T_5,T_6$.", r"$T_4=7,\ T_5=13,\ T_6=24$.", "1+1"),
 Q(r"Find the 10th and 26th terms of the AP $3,8,13,18,\ldots$", r"$a=3,d=5$: $t_{10}=3+9\times5=48$; $t_{26}=3+25\times5=128$.", "1+1"),
 Q(r"Which term of the AP $21,18,15,\ldots$ is $-81$? Is 0 a term?", r"$21-3(n-1)=-81\Rightarrow n=35$ (1). $21-3(n-1)=0\Rightarrow n=8$, so 0 is the 8th term (1).", "1+1"),
 Q(r"Find the nth term of the AP $11,8,5,2,\ldots$ and write its recursive rule.", r"$t_n=11+(n-1)(-3)=14-3n$ (1). Recursive: $t_1=11,\ t_n=t_{n-1}-3$ (1).", "1+1"),
 Q(r"Find the sum of the first 20 natural numbers and of the first 100 natural numbers.", r"$S_{20}=\frac{20\times21}2=210$; $S_{100}=\frac{100\times101}2=5050$.", "1+1"),
 Q(r"Show that $2,6,18,54,\ldots$ is a GP and write its nth term.", r"Ratios $\frac62=\frac{18}6=\frac{54}{18}=3$, a constant (1). $t_n=2\cdot3^{n-1}$ (1).", "1+1"),
 Q(r"A taxi charges a fixed ₹200 and ₹40 per km. Write the fare after 1, 2, 3 km and find the fare for 10 km.", r"₹240, ₹280, ₹320 — an AP with $d=40$ (1). $t_n=200+40n$; $t_{10}=₹600$ (1).", "1+1"),
 Q(r"Is $1,-1,1,-1,1,\ldots$ a GP? Give the common ratio and the nth term.", r"Yes — every term is $-1$ times the previous one: $r=-1$, $t_n=(-1)^{n-1}$.", "1+1"),
 Q(r"How many black triangles are there at Stages 4 and 5 of the Sierpiński triangle?", r"Stage $n$ has $3^n$ black triangles: Stage 4 has 81 and Stage 5 has 243.", "1+1"),
]
assert len(B) == 16, len(B)
# C (24)
C += [
 Q(r"Which term of $t_n=3n-7$ is 332? Is 557 a term of this sequence?", r"$3n-7=332\Rightarrow n=113$ (1). $3n-7=557\Rightarrow3n=564\Rightarrow n=188$, a natural number, so 557 is the 188th term (2).", "1+2"),
 Q(r"Check whether 308 and 471 are terms of $s_n=5n-2$.", r"$5n-2=308\Rightarrow n=62$: yes (1+). $5n-2=471\Rightarrow n=94.6$, not a natural number ⇒ not a term (2).", "1+2"),
 Q(r"An AP has 50 terms; its 3rd term is 12 and its last term is 106. Find the 29th term.", r"$a+2d=12$, $a+49d=106$ ⇒ $47d=94$, $d=2$, $a=8$ (2). $t_{29}=8+28\times2=64$ (1).", "2+1"),
 Q(r"How many two-digit numbers are divisible by 3? Find their sum.", r"12, 15, …, 99: $99=12+(n-1)3\Rightarrow n=30$ (1). Sum $=\frac{30}2(12+99)=1665$ (2).", "1+2"),
 Q(r"Harish starts at ₹5,00,000 a year and gets a raise of ₹20,000 each year. After how many raises does his salary reach ₹6,00,000?", r"$500000+20000k=600000\Rightarrow k=5$ raises (so he earns ₹6,00,000 in his 6th year).", "2+1"),
 Q(r"A child arranges marbles in rows: 1 in the first row, 2 in the second, … up to 25 rows. How many marbles are used?", r"$S_{25}=\frac{25\times26}2=325$ marbles.", "2+1"),
 Q(r"Find $12+13+14+\cdots+40$ using $S_n=\frac{n(n+1)}2$.", r"$S_{40}-S_{11}=\frac{40\times41}2-\frac{11\times12}2=820-66=754$.", "2+1"),
 Q(r"Find the sum of the first 20 terms of the AP $3,8,13,\ldots$ using ‘average of first and last × number of terms’.", r"Last term $=3+19\times5=98$ (1). Sum $=\frac{3+98}2\times20=1010$ (2).", "1+2"),
 Q(r"For the sequence $1,4,7,10,\ldots$ write the explicit rule and the recursive rule.", r"$d=3$: $t_n=1+(n-1)3=3n-2$ (2). Recursive: $t_1=1,\ t_n=t_{n-1}+3$ (1).", "2+1"),
 Q(r"Find the 10th, 17th and 80th triangular numbers.", r"$t_n=\frac{n(n+1)}2$: $t_{10}=55$, $t_{17}=153$, $t_{80}=3240$.", "1+1+1"),
 Q(r"Verify that $1+3+5+7+9=5^2$ and prove that the sum of the first $n$ odd numbers is $n^2$ using the AP sum.", r"$1+3+5+7+9=25$ ✓ (1). For the AP $1,3,\dots,(2n-1)$: $S=\frac n2(1+(2n-1))=n^2$ (2).", "1+2"),
 Q(r"Find the 10th term of the GP $3,6,12,\ldots$ and its recursive rule.", r"$t_{10}=3\cdot2^9=1536$ (2). $t_1=3,\ t_n=2t_{n-1}$ (1).", "2+1"),
 Q(r"Which term of the GP $2,6,18,\ldots$ is 486?", r"$2\cdot3^{n-1}=486\Rightarrow3^{n-1}=243=3^5\Rightarrow n=6$.", "2+1"),
 Q(r"A ball dropped from 24 ft rebounds to $\frac34$ of its previous height each time. Find the heights after the first three bounces and state the type of sequence.", r"$18,\ 13.5,\ 10.125$ ft (2). It is a GP with $r=\frac34$ (1).", "2+1"),
 Q(r"In the Sierpiński triangle the black area at Stage 0 is 1 sq. unit. Find the black area at Stage 3 and show it equals (number of black triangles) × (area of each).", r"Area at Stage $n$ is $\left(\frac34\right)^n$ ⇒ Stage 3: $\frac{27}{64}$ (2). 27 triangles each of area $\frac1{64}$ give $\frac{27}{64}$ ✓ (1).", "2+1"),
 Q(r"A bacterial colony of 500 doubles every hour. How many bacteria are there after 6 hours?", r"GP with $r=2$: $500\times2^6=32000$.", "2+1"),
 Q(r"Write the first ten terms of the Virahānka–Fibonacci sequence ($V_1=1,V_2=2$).", r"$1,2,3,5,8,13,21,34,55,89$.", "3"),
 Q(r"Find the first five terms of $u_1=1,\ u_n=2u_{n-1}+3$ and decide whether 133 is a term.", r"$1,5,13,29,61,125,253,\ldots$ (2). 133 does not appear and the terms increase, so it is not a term (1).", "2+1"),
 Q(r"Find the first four terms of $s_1=3,\ s_n=s_{n-1}(s_{n-1}-1)$.", r"$3,\ 6,\ 30,\ 870$.", "3"),
 Q(r"Show that $1,3,6,10,\ldots$ is neither an AP nor a GP.", r"Differences $2,3,4$ — not constant ⇒ not an AP (1+). Ratios $3,2,\frac53$ — not constant ⇒ not a GP (1).", "1+1+1"),
 Q(r"The points $(n,t_n)$ of the AP $2,5,8,\ldots$ are plotted. Show they lie on a straight line and find its slope.", r"$t_n=3n-1$ is linear: points $(1,2),(2,5),(3,8)$ lie on $y=3x-1$ (2). Slope $=3$, the common difference (1).", "2+1"),
 Q(r"Show that the points $(1,3),(2,6),(3,12)$ from the GP $3,6,12,\ldots$ do not lie on a straight line.", r"Slope between first two $=3$; between the next two $=6$ (2). Unequal slopes ⇒ not collinear (1).", "2+1"),
 Q(r"Derive the formula for the sum of the first $n$ natural numbers.", r"$S=1+2+\cdots+n$ and $S=n+(n-1)+\cdots+1$ (1). Adding: $2S=n(n+1)$ since there are $n$ pairs, each $n+1$ (1). So $S=\frac{n(n+1)}2$ (1).", "1+1+1"),
 Q(r"Show that the sum of two consecutive triangular numbers is a perfect square; verify for $t_{10}$ and $t_9$.", r"$t_n+t_{n-1}=\frac{n(n+1)}2+\frac{(n-1)n}2=n^2$ (2). $55+45=100=10^2$ ✓ (1).", "2+1"),
]
assert len(C) == 24, len(C)
# D (16)
D += [
 Q(r"(i) Prove that $1+2+3+\cdots+n=\frac{n(n+1)}2$. (ii) Hence find $S_{20}$ and $S_{50}$. (iii) Find $25+26+\cdots+58$.", r"(i) Write the sum forwards and backwards and add: $2S=n(n+1)$ (2). (ii) $S_{20}=210$, $S_{50}=1275$ (1). (iii) $S_{58}-S_{24}=1711-300=1411$ (2).", "2+1+2"),
 Q(r"<b>Case study:</b> A taxi company charges a fixed booking fee of ₹200 plus ₹40 per km. (i) Write the fares for 1, 2 and 3 km. (ii) Show the sequence is an AP and find the nth term. (iii) Find the fare for 10 km. (iv) For how many km is the fare ₹1,000?", r"(i) ₹240, ₹280, ₹320 (1). (ii) Constant difference 40; $t_n=200+40n$ (2). (iii) ₹600 (1). (iv) $200+40n=1000\Rightarrow n=20$ km (1).", "1+2+1+1"),
 Q(r"<b>Case study:</b> A child arranges marbles in rows of 1, 2, 3, … (i) How many marbles are in the first 10 rows? (ii) How many in 25 rows? (iii) How many rows are needed for exactly 210 marbles? (iv) Which triangular number is the answer to (i)?", r"(i) $S_{10}=55$ (1). (ii) $S_{25}=325$ (1). (iii) $\frac{n(n+1)}2=210\Rightarrow n=20$ (2). (iv) The 10th triangular number (1).", "1+1+2+1"),
 Q(r"<b>Case study (Sierpiński triangle):</b> Stage 0 is a black triangle of area 1 sq. unit. (i) Give the number of black triangles at Stages 0 to 3. (ii) Give the number at Stages 4 and 5. (iii) Write the rule for Stage $n$. (iv) Find the black area at Stage 3 and at Stage $n$. (v) What happens to the area as $n$ grows?", r"(i) 1, 3, 9, 27 (1). (ii) 81, 243 (1). (iii) $3^n$, a GP with $r=3$ (1). (iv) $\frac{27}{64}$; $\left(\frac34\right)^n$ (1). (v) It decreases towards 0, while the number of triangles increases rapidly (1).", "1+1+1+1+1"),
 Q(r"<b>Case study:</b> A ball is dropped from 24 ft and rebounds to $\frac34$ of its previous height each time. (i) Find the heights after the first five bounces. (ii) Write the nth term. (iii) After how many bounces does the height first fall below 3 ft?", r"(i) $18,\ 13.5,\ 10.125,\ 7.59375,\ 5.695$ (2). (ii) $t_n=24\left(\frac34\right)^n$ (1). (iii) After 7 bounces 3.20 ft; after the 8th 2.40 ft ⇒ 8 bounces (2).", "2+1+2"),
 Q(r"<b>Case study:</b> Harish's starting salary is ₹5,00,000 and he gets an increment of ₹20,000 each year. (i) Write his salary in the first three years. (ii) Find the salary in the 8th year. (iii) In which year will it be ₹8,00,000? (iv) Find his total earnings in 10 years.", r"(i) 5,00,000; 5,20,000; 5,40,000 (1). (ii) $500000+7\times20000=₹6,40,000$ (1). (iii) $500000+20000(n-1)=800000\Rightarrow n=16$ (1). (iv) $\frac{10}2(2\cdot500000+9\cdot20000)=5\times1180000=₹59,00,000$ (2).", "1+1+1+2"),
 Q(r"An AP has 50 terms with $t_3=12$ and $t_{50}=106$. (i) Find $a$ and $d$. (ii) Find the 29th term. (iii) Find the sum of all 50 terms.", r"(i) $a+2d=12$, $a+49d=106$ ⇒ $d=2$, $a=8$ (2). (ii) $8+28\times2=64$ (1). (iii) $\frac{50}2(8+106)=2850$ (2).", "2+1+2"),
 Q(r"(i) Write the first ten terms of the Virahānka–Fibonacci sequence. (ii) Find the sum of the first 8 terms and compare with $V_{10}$. (iii) State where and when it was first written down.", r"(i) $1,2,3,5,8,13,21,34,55,89$ (2). (ii) $1+2+3+5+8+13+21+34=87=V_{10}-2$ (2). (iii) By Virahānka, 7th century CE, in connection with Prakrit metre (1).", "2+2+1"),
 Q(r"Classify each as AP, GP or neither, and give the nth term where it exists: (a) $7,11,15,19,\ldots$ (b) $2,6,18,54,\ldots$ (c) $1,4,9,16,\ldots$ (d) $100,50,25,12.5,\ldots$", r"(a) AP, $d=4$, $t_n=4n+3$ (1). (b) GP, $r=3$, $t_n=2\cdot3^{n-1}$ (1). (c) Neither (differences 3,5,7; ratios 4, 2.25) but $t_n=n^2$ (1). (d) GP, $r=\frac12$, $t_n=100\left(\frac12\right)^{n-1}$ (2).", "1+1+1+2"),
 Q(r"A sequence has $t_1=-5$ and $t_{n+1}=t_n+3$. (i) Write the first five terms. (ii) Find the explicit rule. (iii) Is 52 a term? (iv) Find the sum of the first 20 terms.", r"(i) $-5,-2,1,4,7$ (1). (ii) $t_n=3n-8$ (1). (iii) $3n-8=52\Rightarrow n=20$, yes (1). (iv) $\frac{20}2(-5+52)=470$ (2).", "1+1+1+2"),
 Q(r"(i) Plot the points $(n,t_n)$ for the AP $1,5,9,13,17$ and say what you observe. (ii) Plot the points for the GP $3,6,12,24,48$ and compare. (iii) What does this tell you about growth in an AP and a GP?", r"(i) Points $(1,1),(2,5),(3,9),(4,13),(5,17)$ lie on the line $y=4x-3$ (2). (ii) $(1,3),(2,6),(3,12),(4,24),(5,48)$ do not lie on a line; slopes 3, 6, 12, 24 keep rising (2). (iii) An AP grows by a fixed amount (linear), a GP by a fixed multiple (much faster) (1).", "2+2+1"),
 Q(r"<b>Case study:</b> Meera saves ₹100 in the first month and ₹50 more each month than in the previous month. (i) Write her savings for the first three months. (ii) Find the nth term. (iii) Find her saving in the 12th month and her total in a year. (iv) In which month does she save ₹1,000?", r"(i) 100, 150, 200 (1). (ii) $t_n=100+50(n-1)=50n+50$ (1). (iii) $t_{12}=650$; total $=\frac{12}2(100+650)=₹4,500$ (2). (iv) $50n+50=1000\Rightarrow n=19$ (1).", "1+1+2+1"),
 Q(r"<b>Case study:</b> A colony of 500 bacteria doubles every hour. (i) Write the numbers at the end of hours 1 to 4. (ii) Write the nth term. (iii) How many bacteria after 6 hours? (iv) After how many hours does the number first exceed 10,000?", r"(i) 1000, 2000, 4000, 8000 (1). (ii) $500\cdot2^n$ (1). (iii) $500\times64=32000$ (1). (iv) $500\cdot2^n>10000\Rightarrow2^n>20\Rightarrow n=5$ (16,000) (2).", "1+1+1+2"),
 Q(r"(i) Show that the sum of the first $n$ odd numbers is $n^2$. (ii) Find $1+3+5+\cdots+49$. (iii) Express 144 as the sum of consecutive odd numbers starting at 1.", r"(i) AP with $a=1$, last term $2n-1$: $S=\frac n2(1+2n-1)=n^2$ (2). (ii) 25 terms ⇒ $25^2=625$ (1). (iii) $1+3+\cdots+23=12^2=144$ (2).", "2+1+2"),
 Q(r"(i) Show that $25+26+\cdots+58=1411$ using $S_{58}-S_{24}$. (ii) Check the answer using ‘average of first and last × number of terms’. (iii) Who first recorded this result and where?", r"(i) $S_{58}-S_{24}=29\times59-12\times25=1711-300=1411$ (2). (ii) 34 terms; $\frac{25+58}2\times34=1411$ ✓ (2). (iii) Āryabhaṭa, in the Āryabhaṭīya, Chapter 2, verse 19 (1).", "2+2+1"),
 Q(r"(i) Prove that $t_n+t_{n-1}=n^2$ for triangular numbers. (ii) Verify for $n=10$. (iii) Find the 17th and 80th triangular numbers.", r"(i) $\frac{n(n+1)}2+\frac{n(n-1)}2=\frac{n(2n)}2=n^2$ (2). (ii) $55+45=100$ ✓ (1). (iii) $t_{17}=153$, $t_{80}=3240$ (2).", "2+1+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
