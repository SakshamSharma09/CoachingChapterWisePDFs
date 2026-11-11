"""Class 10 Maths Ch 13 Statistics - extras (mean by direct / assumed mean / step-deviation, median, mode of grouped data)."""
from common import AR4, Q

AR = [
 AR4(r"For the class interval 10-20, the class mark is 15.", r"The class mark of a class interval is $\dfrac{\text{upper limit}+\text{lower limit}}{2}$.", "a",
     r"$\tfrac{10+20}{2}=15$; R is the definition used."),
 AR4(r"For grouped data the median class is the class whose cumulative frequency is just greater than or equal to $\dfrac n2$.", r"The median class is the class which has the highest frequency.", "c",
     r"A is the correct rule; the class with the highest frequency is the <i>modal</i> class, so R is false."),
 AR4(r"The modal class of a grouped frequency distribution is the class with the lowest frequency.", r"The mode is the value that occurs most often in the data.", "d",
     r"The modal class has the <i>highest</i> frequency, so A is false; R is true."),
 AR4(r"The mean of 10, 20, 30, 40 and 50 is 30.", r"The sum of the deviations of the observations from their mean is zero.", "b",
     r"$\tfrac{150}5=30$, so A is true; R is also a true property but it is not what gives the value of the mean."),
 AR4(r"The mean of grouped data found by the step-deviation method is the same as the mean found by the direct method.", r"The step-deviation method uses $\bar x=a+h\,\dfrac{\sum f_iu_i}{\sum f_i}$ with $u_i=\dfrac{x_i-a}{h}$, which is a simplified form of the same formula.", "a",
     r"The formula in R is an algebraic rewriting of $\sum f_ix_i/\sum f_i$, so both methods give the same mean."),
 AR4(r"For a grouped distribution with $\sum f_i=50$, the median class is the class which contains the 25th observation.", r"The mean of grouped data is always equal to its median.", "c",
     r"The median class is found by $\tfrac n2=25$: A true; the mean and median are generally different, so R is false."),
]

CASE = [
 Q(r"<b>Case study.</b> A teacher recorded the time (in minutes) taken by 40 students to solve a puzzle. The classes 10-20, 20-30, 30-40, 40-50 and 50-60 had frequencies 2, 4, 10, 14 and 10 respectively. "
   r"(i) Find the class mark of the class 30-40. (ii) Write the modal class. (iii) Find the mean time taken. (iv) Find the mode of the data.",
   r"(i) $\tfrac{30+40}{2}=35$ (1). (ii) 40-50, the class with the highest frequency 14 (1). (iii) Class marks 15, 25, 35, 45, 55; $\sum fx=30+100+350+630+550=1660$; mean $=\tfrac{1660}{40}=41.5$ min (1). (iv) Mode $=l+\dfrac{f_1-f_0}{2f_1-f_0-f_2}\,h=40+\dfrac{14-10}{28-10-10}\times10=45$ min (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> The monthly electricity consumption (in units) of 50 houses of a colony is: 100-200: 5 houses, 200-300: 10 houses, 300-400: 20 houses, 400-500: 8 houses, 500-600: 7 houses. "
   r"(i) What is the value of $\tfrac n2$? (ii) Find the cumulative frequency of each class. (iii) Write the median class. (iv) Find the median consumption.",
   r"(i) $\tfrac{50}{2}=25$ (1). (ii) 5, 15, 35, 43, 50 (1). (iii) 300-400, the first class whose cumulative frequency (35) exceeds 25 (1). (iv) $l=300$, $cf=15$, $f=20$, $h=100$: median $=300+\dfrac{25-15}{20}\times100=350$ units (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> The marks (out of 100) of 40 students in a test are: 0-20: 5 students, 20-40: 8, 40-60: 12, 60-80: 10, 80-100: 5. Take assumed mean $a=50$ and class size $h=20$ and let $u_i=\dfrac{x_i-a}{h}$. "
   r"(i) Find the class mark of the class 20-40. (ii) Find $u_i$ for the class 60-80. (iii) Find $\sum f_iu_i$. (iv) Find the mean marks by the step-deviation method.",
   r"(i) 30 (1). (ii) $x=70$, $u=\tfrac{70-50}{20}=1$ (1). (iii) $u$ values are $-2,-1,0,1,2$; $\sum fu=-10-8+0+10+10=2$ (1). (iv) $\bar x=50+20\times\tfrac{2}{40}=51$ marks (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Class mark and basics", [r"Class mark $x_i=\dfrac{\text{upper limit}+\text{lower limit}}{2}$; class size $h=$ upper limit $-$ lower limit.",
   r"$n=\sum f_i$ = total frequency."]),
 ("Mean of grouped data", [r"Direct method: $\bar x=\dfrac{\sum f_ix_i}{\sum f_i}$.",
   r"Assumed mean method: $\bar x=a+\dfrac{\sum f_id_i}{\sum f_i}$, $\ d_i=x_i-a$.",
   r"Step-deviation method: $\bar x=a+h\,\dfrac{\sum f_iu_i}{\sum f_i}$, $\ u_i=\dfrac{x_i-a}{h}$.",
   r"Ungrouped data: mean $=\dfrac{\text{sum of observations}}{\text{number of observations}}$."]),
 ("Mode of grouped data", [r"Modal class = class with the highest frequency.",
   r"Mode $=l+\dfrac{f_1-f_0}{2f_1-f_0-f_2}\times h$.",
   r"l = lower limit of modal class, $f_1$ = its frequency, $f_0$ = frequency of preceding class, $f_2$ = frequency of succeeding class, h = class size."]),
 ("Median of grouped data", [r"Make a cumulative frequency (cf) column. Median class = class whose cf is just $\ge\dfrac n2$.",
   r"Median $=l+\dfrac{\dfrac n2-cf}{f}\times h$.",
   r"l = lower limit of median class, cf = cumulative frequency of the class preceding it, f = frequency of median class, h = class size."]),
 ("Remember", [r"Classes must be continuous (exclusive); convert inclusive classes by adjusting limits by half the gap.",
   r"Mean, median and mode are in the same units as the data."]),
]

MISTAKES = [
 r"Taking cf of the median class as its own cumulative frequency; cf in the formula is that of the class <i>before</i> the median class.",
 r"Choosing the median class by comparing with n instead of $\dfrac n2$.",
 r"Confusing $f_0$ and $f_2$ (preceding and succeeding class frequencies) in the mode formula.",
 r"Using the class limits instead of the class marks $x_i$ in $\sum f_ix_i$.",
 r"In the step-deviation method, forgetting to multiply $\dfrac{\sum f_iu_i}{\sum f_i}$ by h.",
 r"Using the modal class (highest frequency) as the median class, or vice versa.",
]
