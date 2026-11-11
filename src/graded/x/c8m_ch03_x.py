"""Class 8 Maths Ch 3 A Story of Numbers - extras."""
from common import AR4, Q

AR = [
 AR4(r"The binary number $101_2$ equals 5 in decimal.", r"In base 2, the value of a number is the sum of each digit times a power of 2, with the rightmost place being $2^0$.", "a",
     r"$1\times4+0\times2+1\times1=5$; R is the method used."),
 AR4(r"The Roman numeral XL represents 40.", r"The Roman symbols V, L and D are never repeated.", "b",
     r"XL = 50 $-$ 10 = 40, so A is true; R is also true but does not explain why XL means 40."),
 AR4(r"The Babylonian number system had base 60.", r"The Maya number system also used base 10.", "c",
     r"The Babylonians used base 60 (true); the Maya used base 20, so R is false."),
 AR4(r"The Roman numeral IC represents 99.", r"In Roman numerals, I can be subtracted only from V and X.", "d",
     r"99 is written XCIX; IC is not a valid numeral, so A is false, while R is a true rule."),
 AR4(r"The number 13 is written $1101_2$ in binary.", r"Repeated division of 13 by 2 gives remainders 1, 0, 1, 1 from the first division, and these read upwards form the binary number.", "a",
     r"$13=8+4+0+1$, so $13=1101_2$; the division method in R produces it."),
 AR4(r"$111_2=7$.", r"The binary system uses only the digits 0 and 1.", "b",
     r"$4+2+1=7$ so A is true; R is true but is not the reason for the value 7."),
]

CASE = [
 Q(r"<b>Case study.</b> The foundation stone of a school in Nagpur reads MCMLXXXV, and the plaque on the new building reads XXIV. "
   r"(i) Convert MCMLXXXV to a Hindu-Arabic number. (ii) Convert XXIV to a Hindu-Arabic number. (iii) Write 2024 in Roman numerals. (iv) The school year is 2024; find the age of the school and write it in Roman numerals.",
   r"(i) $1000+900+80+5=1985$ (1). (ii) $10+10+4=24$ (1). (iii) MMXXIV (1). (iv) $2024-1985=39$ (1); XXXIX (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Gopal runs a grain shop in Lucknow and owns weights of 1, 2, 4, 8 and 16 kg, each only once. He wants to weigh 13 kg and 27 kg of grain using binary numbers. "
   r"(i) Write 13 in binary. (ii) Which weights are used for 13 kg? (iii) Write 27 in binary. (iv) Show that these five weights can measure every whole number of kg from 1 to 31.",
   r"(i) $13=1101_2$ (1). (ii) 8, 4 and 1 kg (1). (iii) $27=11011_2$, i.e. $16+8+2+1$ (1). (iv) The largest five-digit binary number $11111_2=16+8+4+2+1=31$ (1), and every number from 1 to 31 can be written with at most five binary digits, i.e. as a sum of distinct weights from 1, 2, 4, 8, 16 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A teacher writes the number $2143_5$ on the board, in base 5, and asks students to analyse it. "
   r"(i) Which digits are allowed in base 5? (ii) Write $2143_5$ in expanded form. (iii) Find its value in decimal. (iv) Express the decimal number 59 in base 5.",
   r"(i) 0, 1, 2, 3, 4 (1). (ii) $2\times5^3+1\times5^2+4\times5+3$ (1). (iii) $250+25+20+3=298$ (1). (iv) $59=2\times25+1\times5+4$, so $59=214_5$ (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Roman numerals", [
   r"I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000.",
   r"I, X, C, M may be repeated up to 3 times; V, L, D are never repeated.",
   r"Subtraction: I before V or X; X before L or C; C before D or M (e.g. IX = 9, XL = 40, CM = 900).",
   r"Value = sum of symbol values, with a smaller symbol before a larger one subtracted."]),
 ("Place value and bases", [
   r"In base $b$ the digits are $0,1,\dots,b-1$ and the place values are $\dots,b^3,b^2,b,1$.",
   r"$(d_3d_2d_1d_0)_b=d_3b^3+d_2b^2+d_1b+d_0$.",
   r"Hindu-Arabic (decimal) system: base 10, uses the digits 0 to 9 and zero as a place holder."]),
 ("Changing the base", [
   r"Decimal to base $b$: divide repeatedly by $b$; read the remainders from the last to the first.",
   r"Base $b$ to decimal: expand with powers of $b$ and add.",
   r"Largest $k$-digit number in base $b$ is $b^k-1$; there are $b^k$ numbers with at most $k$ digits."]),
 ("Binary system", [
   r"Base 2, digits 0 and 1; place values $1,2,4,8,16,32,\dots$",
   r"Binary addition: $1+1=10_2$, $1+1+1=11_2$ (carry 1).",
   r"Computers store information in bits (binary digits)."]),
 ("Other ancient systems", [
   r"Babylonian system: base 60. Maya system: base 20 (dots, bars and a shell for zero).",
   r"Brahmagupta (628 CE) gave rules for operations with zero and negative numbers."]),
]

MISTAKES = [
 r"Repeating V, L or D, or writing IC, IL, XM for 99, 49, 990; use XCIX, XLIX and CMXC.",
 r"Reading the remainders from the first to the last when converting decimal to another base; they must be read from the <b>last to the first</b>.",
 r"Using a digit equal to or larger than the base (for example $135_5$ is not a valid number).",
 r"Taking the place values of binary as 1, 2, 3, 4 instead of 1, 2, 4, 8.",
 r"Not carrying properly in binary: $1+1=10_2$, not 2.",
 r"Confusing bases of ancient systems: Babylonian is base 60 and Maya is base 20, not base 10.",
]
