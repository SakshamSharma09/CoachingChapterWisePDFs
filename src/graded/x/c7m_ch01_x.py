"""Class 7 Maths Ch 1 Large Numbers - extras."""
from common import AR4, Q

AR = [
 AR4("1 crore = 100 lakh.", "1 lakh = 1,00,000 and 1 crore = 1,00,00,000.", "a",
     "1,00,00,000 / 1,00,000 = 100."),
 AR4("1 million = 10 lakh.", "1 billion = 1000 million.", "b",
     "1,000,000 = 10,00,000 = 10 lakh, and 1 billion = 1000 million. Both true, but R does not explain A."),
 AR4("45,00,000 is written as 4,500,000 in the international system.", "In the international system, commas are placed after the first three digits and then after every two digits.", "c",
     "A is true. The international system puts a comma after every three digits, so R is false."),
 AR4("10 lakh has 5 zeros.", "1 lakh has 5 zeros.", "d",
     "10 lakh = 10,00,000 has 6 zeros, so A is false. R is true."),
 AR4("4,82,935 rounded to the nearest ten thousand is 4,80,000.", "The thousands digit is 2, which is less than 5, so the number is rounded down.", "a",
     "The ten-thousands digit is 8; the thousands digit 2 means round down."),
 AR4("9,99,999 + 1 = 10,00,000.", "10,00,000 is read as ten lakh.", "b",
     "Both are true but R only reads the number and does not explain the addition."),
]

CASE = [
 Q(r"<b>Case study.</b> The population of a town in Gujarat is 45,67,890. (i) Write this number in words (Indian system). (ii) Write it in the international system. (iii) What is the place value of the digit 5? (iv) Round it to the nearest lakh. If 3,33,110 more people move in, what is the new population?",
   r"(i) Forty-five lakh sixty-seven thousand eight hundred ninety (1). (ii) 4,567,890 (1). (iii) 5,00,000 (five lakh) (1). (iv) Nearest lakh: 46,00,000 (1); new population $=45{,}67{,}890+3{,}33{,}110=49{,}01{,}000$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A company earned ₹2,50,00,000 in one year. (i) Write this amount in crore. (ii) Write it in the international system. (iii) If it earns the same amount in each of 4 years, find the total in crore. (iv) Its expenses were ₹1,20,00,000 in the first year. Find the profit and write it in crore.",
   r"(i) 2.5 crore (1). (ii) 25,000,000 (25 million) (1). (iii) $4\times2.5=10$ crore, i.e. ₹10,00,00,000 (1). (iv) Profit $=2{,}50{,}00{,}000-1{,}20{,}00{,}000=₹1{,}30{,}00{,}000$ (1), which is 1.3 crore (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> The Moon is about 3,84,000 km from the Earth. A spacecraft goes to the Moon and returns by the same path. (i) Write 3,84,000 in words. (ii) Write it in the international system. (iii) Find the distance of the round trip. (iv) Another spacecraft travels 30,72,000 km in all. How many times the Earth to Moon distance is this?",
   r"(i) Three lakh eighty-four thousand (1). (ii) 384,000 (1). (iii) $2\times3{,}84{,}000=7{,}68{,}000$ km (1). (iv) $3072000\div384000=8$ times (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Indian system", [r"Place values from the right: ones, tens, hundreds, thousands, ten thousands, lakhs, ten lakhs, crores, ten crores.",
   r"Commas: first after three digits, then after every two digits, e.g. $12{,}34{,}56{,}789$.",
   r"$1\text{ lakh}=1{,}00{,}000=10^5$.   $1\text{ crore}=1{,}00{,}00{,}000=10^7=100$ lakh."]),
 ("International system", [r"Commas after every three digits, e.g. $123{,}456{,}789$.",
   r"$1\text{ million}=1{,}000{,}000=10^6=10$ lakh.   $1\text{ billion}=10^9=1000$ million $=100$ crore.",
   r"$1\text{ crore}=10$ million."]),
 ("Reading, writing and comparing", [r"Expanded form: $45{,}67{,}890=4\times10^6+5\times10^5+6\times10^4+7\times10^3+8\times10^2+9\times10$.",
   r"More digits means a greater number. With equal digits, compare from the left, digit by digit."]),
 ("Rounding and estimation", [r"Round to a place: look at the digit just to its right; $5$ or more rounds up, less than $5$ rounds down.",
   r"Estimate before calculating: round each number and then add, subtract or multiply."]),
 ("Operations", [r"Multiplying by $10, 100, 1000, \dots$ adds that many zeros: $a\times10^n$.",
   r"Conversions: crore $\to$ lakh multiply by 100; lakh $\to$ thousand multiply by 100."]),
]

MISTAKES = [
 r"Putting commas after every three digits in the Indian system, or after every two digits in the international system.",
 r"Thinking 1 crore $=$ 10 lakh; 1 crore $=$ 100 lakh.",
 r"Confusing 1 million with 1 lakh: $1$ million $=10$ lakh.",
 r"Counting the wrong number of zeros: 1 lakh has 5 zeros, 1 crore has 7 zeros.",
 r"When rounding, looking at the digit in the rounding place instead of the digit just to its right.",
]
