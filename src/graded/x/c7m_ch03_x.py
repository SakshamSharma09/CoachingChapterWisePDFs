"""Class 7 Maths Ch 3 A Peek Beyond the Point - extras."""
from common import AR4, Q

AR = [
 AR4("0.5 is greater than 0.45.", "Comparing digit by digit from the left, 5 tenths is more than 4 tenths.", "a",
     "0.50 > 0.45."),
 AR4("2.50 = 2.5.", "0.1 = 1/10.", "b",
     "Both true; a zero at the end of a decimal part does not change the value, but R does not explain it."),
 AR4("3.456 rounded to the nearest hundredth is 3.46.", "The digit 6 in 3.456 is in the hundredths place.", "c",
     "The digit after the hundredths place (5, 6) decides: 3.456 rounds to 3.46, so A is true. 6 is in the thousandths place, so R is false."),
 AR4("0.3 x 0.2 = 0.6.", "The product of two decimals has as many decimal places as the two factors have in all.", "d",
     "3 x 2 = 6 with two decimal places gives 0.06, so A is false. R is true."),
 AR4("4.5 / 0.5 = 9.", "Multiplying both numbers by 10 gives 45 / 5 = 9.", "a",
     "Multiplying dividend and divisor by the same number leaves the quotient unchanged."),
 AR4("0.07 is less than 0.1.", "0.7 = 7/10.", "b",
     "0.07 = 7/100 < 1/10. Both statements are true, but R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Radha buys 2.5 m of cloth at ₹85.50 per metre. (i) Find the cost of the cloth. (ii) She pays ₹250. How much change does she get? (iii) What would 4 m of this cloth cost? (iv) Her mother has ₹513. How many metres of this cloth can she buy?",
   r"(i) $85.5\times2.5=213.75$, i.e. ₹213.75 (1). (ii) $250-213.75=₹36.25$ (1). (iii) $85.5\times4=₹342$ (1). (iv) $513\div85.5=6$ m (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a school race, three runners finish in 12.45 s, 12.4 s and 12.504 s. (i) Arrange the times in ascending order. (ii) Who won the race (give the time)? (iii) Find the difference between the slowest and the fastest time. (iv) Round 12.504 s to the nearest tenth and to the nearest hundredth.",
   r"(i) 12.4, 12.45, 12.504 (1). (ii) The runner with 12.4 s (1). (iii) $12.504-12.4=0.104$ s (1). (iv) Nearest tenth: 12.5 (1); nearest hundredth: 12.50 (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A bottle holds 1.5 litres of juice. Glasses hold 0.25 litre each. (i) How many glasses can be filled from one bottle? (ii) How many litres are there in 4 bottles? (iii) Write 0.25 litre in millilitres. (iv) How many glasses can be filled from the 4 bottles?",
   r"(i) $1.5\div0.25=6$ glasses (1). (ii) $4\times1.5=6$ litres (1). (iii) $0.25\times1000=250$ mL (1). (iv) $6\div0.25=24$ glasses (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Place value of decimals", [r"Places after the point: tenths $\left(\frac1{10}\right)$, hundredths $\left(\frac1{100}\right)$, thousandths $\left(\frac1{1000}\right)$.",
   r"$0.375=\dfrac{3}{10}+\dfrac{7}{100}+\dfrac{5}{1000}=\dfrac{375}{1000}$.   Zeros at the end of the decimal part do not change the value: $2.50=2.5$."]),
 ("Comparing and rounding", [r"Compare whole parts first, then tenths, hundredths, ... digit by digit (give both numbers equal decimal places).",
   r"Rounding: look at the digit just after the required place; $5$ or more rounds up, less than $5$ rounds down."]),
 ("Addition and subtraction", [r"Write the numbers with the decimal points in a line and add or subtract as whole numbers."]),
 ("Multiplication", [r"Multiply ignoring the points; decimal places in the product $=$ sum of decimal places in the factors.",
   r"Multiplying by $10, 100, 1000$ moves the point $1, 2, 3$ places to the right."]),
 ("Division", [r"Dividing by a decimal: multiply dividend and divisor by $10, 100, \dots$ to make the divisor a whole number, e.g. $4.5\div0.5=45\div5$.",
   r"Dividing by $10, 100, 1000$ moves the point $1, 2, 3$ places to the left."]),
 ("Units", [r"$1\text{ m}=100\text{ cm}$, $1\text{ cm}=0.01\text{ m}$;  $1\text{ kg}=1000\text{ g}$;  $1\text{ L}=1000\text{ mL}$;  ₹$1=100$ paise."]),
]

MISTAKES = [
 r"Thinking 0.45 is greater than 0.5 because 45 is greater than 5; compare 0.45 with 0.50.",
 r"Not lining up the decimal points when adding or subtracting.",
 r"Wrong number of decimal places in a product: $0.3\times0.2=0.06$, not $0.6$.",
 r"Forgetting to shift the point in both the dividend and divisor when dividing by a decimal.",
 r"Rounding by looking at the rounding digit itself instead of the digit just after it.",
]
