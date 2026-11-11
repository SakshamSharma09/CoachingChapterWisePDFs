"""Class 8 Maths Ch 12 Tales by Dots and Lines - extras."""
from common import AR4, Q

AR = [
 AR4(r"The mean of 4, 6, 8, 10 and 12 is 8.", r"The mean of a data set is the sum of the observations divided by the number of observations.", "a",
     r"$\dfrac{4+6+8+10+12}{5}=\dfrac{40}5=8$; R is the definition used."),
 AR4(r"The median of 3, 7, 9, 12 and 15 is 9.", r"The mode of the data 2, 3, 3, 5 is 3.", "b",
     r"The middle value of the five ordered numbers is 9, so A is true; R is also true, but mode is a different measure and does not explain A."),
 AR4(r"The mode of 2, 3, 3, 5, 5, 5, 7 is 5.", r"The mode is the middle value of the ordered data.", "c",
     r"5 occurs most often, so A is true. R is false: the middle value is the median."),
 AR4(r"The median of the four observations 3, 5, 8, 10 is 8.", r"For an even number of observations, the median is the mean of the two middle values.", "d",
     r"Median $=\dfrac{5+8}{2}=6.5$, so A is false; R is true."),
 AR4(r"The range of the data 12, 25, 7, 40, 19 is 33.", r"Range $=$ largest value $-$ smallest value.", "a",
     r"$40-7=33$; R is the definition."),
 AR4(r"A dot plot shows how many times each value occurs in a data set.", r"The mean is the sum of the observations divided by their number.", "b",
     r"A dot plot puts one dot for each occurrence of a value, so A is true; R is also true but does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> A teacher records the marks (out of 20) of seven students in a quiz: 9, 12, 15, 15, 10, 18, 19. "
   r"(i) Find the mean. (ii) Find the median. (iii) Find the mode. (iv) Find the range, and the new mean if an eighth student scores 20.",
   r"(i) $\dfrac{98}{7}=14$ (1). (ii) Ordered: 9, 10, 12, 15, 15, 18, 19; median $=15$ (1). (iii) Mode $=15$ (1). (iv) Range $=19-9=10$ (1); new mean $=\dfrac{98+20}{8}=14.75$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A dot plot shows the number of siblings of 10 students in a class: two students have 0 siblings, four have 1, three have 2 and one has 3. "
   r"(i) How many students are there in all? (ii) What is the mode of the data? (iii) How many students have at least 2 siblings? (iv) Find the mean and the median number of siblings.",
   r"(i) $2+4+3+1=10$ (1). (ii) Mode $=1$ (1). (iii) $3+1=4$ students (1). (iv) Mean $=\dfrac{0+4+6+3}{10}=1.3$ (1); ordered data has 5th and 6th values both 1, so median $=1$ (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> The line graph of the maximum temperature (in $^\circ$C) of a town in Gujarat on five days reads: Monday 28, Tuesday 30, Wednesday 33, Thursday 31, Friday 28. "
   r"(i) On which day was the temperature the highest? (ii) By how much did it rise from Monday to Wednesday? (iii) Between which two consecutive days was the fall the greatest? (iv) Find the mean temperature and the number of days above the mean.",
   r"(i) Wednesday, $33^\circ$C (1). (ii) $33-28=5^\circ$C (1). (iii) Thursday to Friday, a fall of $3^\circ$C (Wednesday to Thursday fell $2^\circ$C) (1). (iv) Mean $=\dfrac{28+30+33+31+28}{5}=\dfrac{150}{5}=30^\circ$C (1); days above the mean: Wednesday and Thursday, 2 days (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Measures of central tendency", [
   r"Mean $=\dfrac{\text{sum of observations}}{\text{number of observations}}$.",
   r"Median: middle value of the data arranged in order. Odd $n$: the $\dfrac{n+1}{2}$th value. Even $n$: mean of the $\dfrac n2$th and $\left(\dfrac n2+1\right)$th values.",
   r"Mode: the observation that occurs most often (a data set may have more than one mode, or none)."]),
 ("Spread", [
   r"Range $=$ largest observation $-$ smallest observation."]),
 ("Useful results", [
   r"Sum of observations $=$ mean $\times$ number of observations.",
   r"Mean lies between the smallest and the largest observation.",
   r"Adding a value equal to the mean does not change the mean."]),
 ("Representing data", [
   r"Dot plot: one dot for each occurrence of a value above a number line; the tallest column marks the mode.",
   r"Line graph: points joined by lines; used to show change over time (rise, fall, trend).",
   r"Read a line graph by comparing values at consecutive points; change $=$ later value $-$ earlier value."]),
]

MISTAKES = [
 r"Finding the median without arranging the data in order first.",
 r"For an even number of observations, taking one of the middle values instead of the <b>mean of the two middle values</b>.",
 r"Confusing mode with median or mean: mode is the most frequent value, not the middle value.",
 r"Dividing the sum by the number of <i>distinct</i> values instead of the total number of observations (counting repeated values only once).",
 r"Computing range as the difference between the first and last values as listed, not the maximum and minimum.",
 r"Reading a line graph at the wrong point or ignoring the scale of the axes.",
]
