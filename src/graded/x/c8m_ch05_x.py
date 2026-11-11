"""Class 8 Maths Ch 5 Number Play - extras."""
from common import AR4, Q

AR = [
 AR4(r"The number 4,236 is divisible by 3.", r"A number is divisible by 3 if the sum of its digits is divisible by 3.", "a",
     r"$4+2+3+6=15$, which is divisible by 3; R is the test used."),
 AR4(r"The number 7,424 is divisible by 4.", r"A number is divisible by 8 if the number formed by its last three digits is divisible by 8.", "b",
     r"The last two digits 24 are divisible by 4, so A is true. R is also a true test but is about 8, so it does not explain A."),
 AR4(r"A number divisible by both 2 and 3 is divisible by 6.", r"A number is divisible by 11 if the sum of its digits is divisible by 11.", "c",
     r"A is true. R is false: the test for 11 uses the difference of the sums of digits at odd and even places (e.g. 121 has digit sum 4 but is divisible by 11)."),
 AR4(r"The number 2,345 is divisible by 9.", r"A number is divisible by 9 if and only if the sum of its digits is divisible by 9.", "d",
     r"$2+3+4+5=14$ is not divisible by 9, so A is false; R is a true test."),
 AR4(r"The number 2,728 is divisible by 11.", r"A number is divisible by 11 if the difference between the sum of the digits at odd places and the sum of the digits at even places is 0 or a multiple of 11.", "a",
     r"From the right: odd places $8+7=15$, even places $2+2=4$; difference $11$, so divisible ($2728=11\times248$)."),
 AR4(r"Applying Kaprekar's routine to 3524 (largest arrangement minus smallest arrangement, repeatedly) leads to 6174.", r"Kaprekar's routine on any four-digit number whose digits are not all equal always ends at 495.", "c",
     r"$5432-2345=3087$, $8730-0378=8352$, $8532-2358=6174$, so A is true. R is false: 495 is reached for three-digit numbers, while four-digit numbers reach 6174."),
]

CASE = [
 Q(r"<b>Case study.</b> A school gives each student a four-digit locker code. Neha's code is 7,236 and Tarun's code is 52<b>d</b>4, where d is a missing digit. "
   r"(i) Is 7,236 divisible by 9? (ii) Is 7,236 divisible by 4? (iii) Is 7,236 divisible by 11? (iv) Find the digit d so that 52d4 is divisible by 9, and check that the number is then also divisible by 6.",
   r"(i) Digit sum $18$, divisible by 9, so yes (1). (ii) Last two digits 36 are divisible by 4, so yes (1). (iii) Odd places $6+2=8$, even places $3+7=10$; difference 2, so not divisible by 11 (1). (iv) $5+2+d+4=11+d$ must be 18, so $d=7$ (1); $5274$ is even and its digit sum 18 is divisible by 3, so it is divisible by 6 ($5274=6\times879$) (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Riya applies Kaprekar's routine to numbers: arrange the digits to form the largest and the smallest numbers and subtract. She starts with the three-digit number 352 and then tries the four-digit number 4312. "
   r"(i) Find the first step for 352. (ii) Find the second step for 352. (iii) Which number does 352 finally reach? (iv) Apply the routine to 4312 and find the number reached and how many steps are needed.",
   r"(i) $532-235=297$ (1). (ii) $972-279=693$ (1). (iii) $963-369=594$, $954-459=495$, so 495 (1). (iv) $4321-1234=3087$, $8730-0378=8352$, $8532-2358=6174$ (1); the number reached is 6174 in 3 steps (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Aman learns about palindromic numbers, which read the same from left to right and right to left. He also tries the reverse-and-add routine on 57. "
   r"(i) Is 12,321 a palindrome? (ii) Find the sum of 57 and its reverse. (iii) Repeat the process on that sum; what is obtained? (iv) Show that every four-digit palindrome $abba$ is divisible by 11, and verify with 3,663.",
   r"(i) Yes (1). (ii) $57+75=132$ (1). (iii) $132+231=363$, a palindrome (1). (iv) $abba=1000a+100b+10b+a=1001a+110b=11(91a+10b)$ (1); $3663=11\times333$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Divisibility tests", [
   r"By 2: units digit 0, 2, 4, 6, 8. By 5: units digit 0 or 5. By 10: units digit 0.",
   r"By 3: digit sum divisible by 3. By 9: digit sum divisible by 9.",
   r"By 4: last two digits divisible by 4. By 8: last three digits divisible by 8.",
   r"By 6: divisible by both 2 and 3.",
   r"By 11: (sum of digits at odd places) $-$ (sum of digits at even places) is 0 or a multiple of 11."]),
 ("Place-value expansions", [
   r"$\overline{ab}=10a+b$ and its reverse is $10b+a$; $\overline{ab}+\overline{ba}=11(a+b)$.",
   r"$\overline{abc}=100a+10b+c$; $\overline{abba}=11(91a+10b)$."]),
 ("Number patterns", [
   r"Palindrome: a number that reads the same forwards and backwards (e.g. 1331).",
   r"Kaprekar's routine (largest arrangement $-$ smallest arrangement): 3-digit numbers (not all digits equal) reach 495; 4-digit numbers reach 6174.",
   r"A number and the sum of its digits leave the same remainder on division by 9."]),
 ("Rules to use", [
   r"If a number is divisible by $a$ and $b$ (co-prime), it is divisible by $ab$.",
   r"The sum of any 3 consecutive numbers is divisible by 3; the sum of any $n$ consecutive numbers starting at $m$ is $nm+\dfrac{n(n-1)}{2}$."]),
]

MISTAKES = [
 r"Testing 11 with the digit <i>sum</i>; the test uses the <b>difference</b> of the sums at odd and even places.",
 r"Saying a number is divisible by 6 because it is divisible by 2 or 3; it must be divisible by <b>both</b>.",
 r"Thinking that divisibility by 4 needs the digit sum; look at the last <b>two</b> digits (last <b>three</b> for 8).",
 r"Subtracting in the wrong order in Kaprekar's routine: always take (largest arrangement) $-$ (smallest arrangement).",
 r"Ignoring the leading zero in the smallest arrangement (e.g. 0378 is 378), which gives a wrong difference.",
 r"Assuming a number divisible by 4 and 6 must be divisible by 24; check with 12 (divisible by both, not by 24).",
]
