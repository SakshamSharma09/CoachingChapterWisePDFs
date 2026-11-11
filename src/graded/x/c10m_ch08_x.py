"""Class 10 Maths Ch 8 Introduction to Trigonometry - extras (ratios, standard angles, complementary angles, identities)."""
from common import AR4, Q

AR = [
 AR4(r"$\sin^2 60^\circ+\cos^2 60^\circ=1$.", r"For every angle $\theta$, $\sin^2\theta+\cos^2\theta=1$.", "a",
     r"$\tfrac34+\tfrac14=1$; A is a particular case of the identity in R."),
 AR4(r"$\tan45^\circ=1$.", r"$\tan\theta=\dfrac{\cos\theta}{\sin\theta}$.", "c",
     r"$\tan45^\circ=\tfrac{1/\sqrt2}{1/\sqrt2}=1$: A true; $\tan\theta=\dfrac{\sin\theta}{\cos\theta}$, so R is false."),
 AR4(r"$\sin\theta$ can be equal to 1.5 for some acute angle $\theta$.", r"In a right triangle the hypotenuse is the longest side, so $\sin\theta=\dfrac{\text{perpendicular}}{\text{hypotenuse}}\le1$.", "d",
     r"$\sin\theta$ never exceeds 1, so A is false; R is true."),
 AR4(r"$\sin30^\circ=\cos60^\circ$.", r"$\tan60^\circ=\sqrt3$.", "b",
     r"Both equal $\tfrac12$ (A true) and R is also true, but R does not explain A."),
 AR4(r"If $\sin A=\dfrac35$ for an acute angle A, then $\cos A=\dfrac45$.", r"$\sin^2A+\cos^2A=1$ for every angle A.", "a",
     r"$\cos A=\sqrt{1-\tfrac9{25}}=\tfrac45$, using the identity in R."),
 AR4(r"$1+\tan^2\theta=\sec^2\theta$ for every acute angle $\theta$.", r"$1+\cot^2\theta=\sec^2\theta$ for every acute angle $\theta$.", "c",
     r"A is a standard identity (true). The correct identity is $1+\cot^2\theta=\operatorname{cosec}^2\theta$, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> In a right-angled triangle PQR, the right angle is at Q, with $PQ=5$ cm, $QR=12$ cm and $PR=13$ cm. "
   r"(i) Write $\sin P$. (ii) Write $\cos R$. (iii) Write $\tan P$. (iv) Verify that $1+\tan^2P=\sec^2P$ for this triangle.",
   r"(i) $\sin P=\dfrac{QR}{PR}=\dfrac{12}{13}$ (1). (ii) $\cos R=\dfrac{QR}{PR}=\dfrac{12}{13}$ (1). (iii) $\tan P=\dfrac{QR}{PQ}=\dfrac{12}{5}$ (1). (iv) $\sec P=\dfrac{13}{5}$; LHS $=1+\dfrac{144}{25}=\dfrac{169}{25}=\left(\dfrac{13}{5}\right)^2=$ RHS (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Riya is practising standard-angle values for her unit test. "
   r"(i) Find $\sin30^\circ+\cos60^\circ$. (ii) Find $\tan60^\circ\times\tan30^\circ$. (iii) Find $\sin60^\circ\cos30^\circ-\cos60^\circ\sin30^\circ$. (iv) If $\sin(A+B)=1$ and $\cos(A-B)=\dfrac{\sqrt3}{2}$, where $0^\circ<A+B\le90^\circ$ and $A>B$, find A and B.",
   r"(i) $\tfrac12+\tfrac12=1$ (1). (ii) $\sqrt3\times\tfrac1{\sqrt3}=1$ (1). (iii) $\tfrac{\sqrt3}{2}\cdot\tfrac{\sqrt3}{2}-\tfrac12\cdot\tfrac12=\tfrac34-\tfrac14=\tfrac12$ (1). (iv) $A+B=90^\circ$ and $A-B=30^\circ$ (1), so $A=60^\circ$, $B=30^\circ$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher draws a right triangle for an acute angle $\theta$ with $\cot\theta=\dfrac{7}{24}$. "
   r"(i) Find the hypotenuse if the sides are in the ratio of the given cotangent (take 7k and 24k). (ii) Find $\sin\theta$ and $\cos\theta$. (iii) Find $\tan\theta$. (iv) Evaluate $\dfrac{\sin35^\circ}{\cos55^\circ}+\dfrac{\cot20^\circ}{\tan70^\circ}$ using complementary angles.",
   r"(i) Adjacent $=7k$, opposite $=24k$, hypotenuse $=\sqrt{49k^2+576k^2}=25k$ (1). (ii) $\sin\theta=\dfrac{24}{25}$, $\cos\theta=\dfrac7{25}$ (1). (iii) $\tan\theta=\dfrac{24}{7}$ (1). (iv) $\sin35^\circ=\cos55^\circ$ and $\cot20^\circ=\tan70^\circ$ (1), so the value is $1+1=2$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Trigonometric ratios (right angle at B, angle A)", [r"$\sin A=\dfrac{\text{perpendicular}}{\text{hypotenuse}}$, $\ \cos A=\dfrac{\text{base}}{\text{hypotenuse}}$, $\ \tan A=\dfrac{\text{perpendicular}}{\text{base}}$.",
   r"$\operatorname{cosec}A=\dfrac1{\sin A}$, $\ \sec A=\dfrac1{\cos A}$, $\ \cot A=\dfrac1{\tan A}$.",
   r"$\tan A=\dfrac{\sin A}{\cos A}$, $\ \cot A=\dfrac{\cos A}{\sin A}$.",
   r"$0\le\sin A\le1$, $\ 0\le\cos A\le1$; $\sec A,\operatorname{cosec}A\ge1$."]),
 ("Values of standard angles", [r"$\sin$: $0,\ \tfrac12,\ \tfrac1{\sqrt2},\ \tfrac{\sqrt3}{2},\ 1$ for $0^\circ,30^\circ,45^\circ,60^\circ,90^\circ$.",
   r"$\cos$: $1,\ \tfrac{\sqrt3}{2},\ \tfrac1{\sqrt2},\ \tfrac12,\ 0$ for the same angles.",
   r"$\tan$: $0,\ \tfrac1{\sqrt3},\ 1,\ \sqrt3,\ \text{not defined}$ for the same angles."]),
 ("Complementary angles", [r"$\sin(90^\circ-A)=\cos A$, $\ \cos(90^\circ-A)=\sin A$.",
   r"$\tan(90^\circ-A)=\cot A$, $\ \cot(90^\circ-A)=\tan A$.",
   r"$\sec(90^\circ-A)=\operatorname{cosec}A$, $\ \operatorname{cosec}(90^\circ-A)=\sec A$."]),
 ("Identities", [r"$\sin^2A+\cos^2A=1$.",
   r"$1+\tan^2A=\sec^2A$.",
   r"$1+\cot^2A=\operatorname{cosec}^2A$."]),
 ("Handy results", [r"Pythagorean triples $(3,4,5),(5,12,13),(8,15,17),(7,24,25)$ give exact ratios.",
   r"To find all ratios from one: draw the right triangle, find the third side by Pythagoras."]),
]

MISTAKES = [
 r"Treating $\sin A$ as $\sin\times A$ and cancelling; $\sin A$ is a single ratio of the angle A.",
 r"Mixing up the sides: for angle A, perpendicular is the side <i>opposite</i> A and base is the side <i>adjacent</i> to it.",
 r"Writing $\tan\theta=\dfrac{\cos\theta}{\sin\theta}$; that is $\cot\theta$.",
 r"Writing $\sin2A=2\sin A$ or $\sin(A+B)=\sin A+\sin B$, which are false.",
 r"Wrong table values, e.g. $\sin30^\circ=\dfrac{\sqrt3}{2}$ or $\tan60^\circ=\dfrac1{\sqrt3}$.",
 r"Using the wrong identity: $1+\cot^2\theta=\operatorname{cosec}^2\theta$, not $\sec^2\theta$; and forgetting that $\tan90^\circ$ is not defined.",
]
