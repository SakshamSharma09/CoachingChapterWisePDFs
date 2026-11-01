import statistics as st
from lib import mcq, Q, OR
from mk9 import M4, build
A = []; B = []; C = []; D = []
def g(x): return f"{x:g}"
SETS_ = [[12, 15, 18, 20, 25], [4, 7, 9, 10, 15, 21], [30, 35, 40, 45, 50, 60, 65], [8, 8, 10, 12, 14, 18], [22, 24, 26, 28, 30], [5, 6, 6, 9, 11, 13, 14], [100, 120, 140, 160, 180], [45, 52, 38, 60, 55, 40], [3, 9, 6, 12, 15, 21, 18], [16, 18, 20, 22, 24, 54]]
# A: mean (8)
for d in SETS_[:8]:
    m = sum(d) / len(d)
    A.append(M4(f"The mean of the data {', '.join(map(str,d))} is:", g(m), [g(m+2), g(m-2), g(st.median(d)+1 if st.median(d)+1 != m else m+5), g(m+5)], f"Sum {sum(d)} ÷ {len(d)}"))
# A: median (8)
for d in SETS_[2:10]:
    ds = sorted(d); md = st.median(ds)
    A.append(M4(f"The median of {', '.join(map(str,d))} is:", g(md), [g(md+1), g(md-1), g(sum(d)/len(d)+3 if sum(d)/len(d)+3 != md else md+7), g(md+4)], "Arrange in order and take the middle value" if len(d) % 2 else "Mean of the two middle values"))
# A: missing value to get a mean (5)
for known, n, mean in [([12, 15, 18, 20], 5, 16), ([8, 10, 14], 4, 11), ([25, 30, 35, 40], 5, 32), ([6, 9, 12, 15, 18], 6, 12), ([40, 50, 60], 4, 50)]:
    x = n * mean - sum(known)
    A.append(M4(f"The mean of {n} numbers is {mean}. {len(known)} of them are {', '.join(map(str,known))}. The remaining number is:", str(x), [str(x+2), str(x-2), str(x+5), str(mean)], "Total = mean × n"))
# A: percentage / dot plot (5)
A += [
 M4("In a dot plot, each dot represents:", "one observation", ["the mean", "ten observations", "the median"], "Dot plot"),
 M4("A line graph is most useful for showing:", "change over time", ["parts of a whole", "colours", "a single value"], "Trend"),
 M4("If every value in a data set is increased by 5, the mean:", "increases by 5", ["stays the same", "doubles", "increases by 25"], "Shift"),
 M4("If one very large value (outlier) is added to a data set, the median changes:", "less than the mean changes", ["more than the mean", "exactly equal to the mean", "to zero"], "Median is robust"),
 M4("The mean is called the 'balancing point' because:", "the total deviation on both sides is equal", ["it is the middle value", "it is the most frequent", "it is the largest"], "Balancing act"),
 M4("The difference between the highest and lowest values is called the:", "range", ["mean", "median", "mode"], "Spread"),
 M4("In a line graph, a steep upward line segment shows:", "a rapid increase", ["no change", "a decrease", "an error"], "Slope"),
 M4("In a line graph, a horizontal segment means:", "no change", ["fast increase", "fast decrease", "missing data"], "Constant value"),
 M4("The average of 4, 6 and 8 is:", "6", ["8", "5", "7"], "18 ÷ 3"),
 M4("For the data 2, 2, 3, 4, 9, the best measure of a typical value unaffected by 9 is the:", "median", ["mean", "range", "sum"], "Median"),
 M4("If the mean of 10 numbers is 15, their sum is:", "150", ["25", "1.5", "15"], "10 × 15"),
 M4("A bar graph uses:", "bars of heights proportional to values", ["circles", "dots only", "lines only"], "Category comparison"),
 M4("The median of an even number of observations is:", "mean of the two middle values", ["the larger middle value", "the first value", "the mean"], "Definition"),
 M4("The data 10, 10, 10, 10 has a mean of:", "10", ["40", "0", "1"], "All equal"),
]
A += [
 M4("The mean of 2, 4, 6, 8, 10 is:", "6", ["5", "8", "30"], "30 ÷ 5"),
 M4("The median of 3, 1, 4, 1, 5 is:", "3", ["1", "4", "2.8"], "Ordered 1, 1, 3, 4, 5"),
 M4("A line graph is drawn by joining plotted points with:", "line segments", ["circles", "bars", "sectors"], "Trend"),
 M4("If the mean of 5 numbers is 8, the sum of the numbers is:", "40", ["13", "8", "1.6"], "5 × 8"),
 M4("The range of 2, 3, 3, 5, 3, 7 is:", "5", ["3", "7", "4"], "7 − 2"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Find the mean of 12, 18, 24, 30, 36.", "$120/5=24$ (2).", "2"),
 Q("Find the median of 7, 3, 9, 5, 12, 15, 1.", "Ordered: 1, 3, 5, 7, 9, 12, 15; median 7 (2).", "2"),
 Q("Find the median of 4, 8, 6, 10, 14, 12.", "Ordered: 4, 6, 8, 10, 12, 14; median $(8+10)/2=9$ (2).", "2"),
 Q("What does a dot plot show?", "The frequency of each value using dots above a number line (2).", "2"),
 Q("The mean of 5 numbers is 20. If one number 28 is removed, what is the mean of the rest?", "Total 100, remaining 72; mean 18 (2).", "2"),
 Q("Why is the median preferred to the mean for incomes?", "A few very large incomes distort the mean (2).", "2"),
 Q("State when a line graph is suitable.", "To display how a quantity changes with time (2).", "2"),
 Q("Find the range of 14, 8, 22, 5, 19.", "$22-5=17$ (2).", "2"),
 Q("The mean of 6 numbers is 9. When a seventh is added the mean becomes 10. Find the number.", "Total 54 then 70; number 16 (2).", "2"),
 Q("Explain 'mean as a balancing point'.", "On a number line with dots as weights, the mean is where the line balances (2).", "2"),
 Q("Is the mean always one of the data values? Give an example.", "No: mean of 2 and 3 is 2.5 (2).", "2"),
 Q("How does adding 10 to every observation change the median?", "The median also increases by 10 (2).", "2"),
 Q("Marks of 5 students: 40, 45, 50, 55, 60. Find the mean and median.", "Both 50 (2).", "2"),
 Q("What are outliers? Give an example.", "Values far from the rest (1); 54 in 16, 18, 20, 22, 54 (1).", "1+1"),
 Q("A line graph shows temperature rising from 20°C to 30°C between 6 a.m. and 12 noon. Find the average rise per hour.", "$10/6\\approx1.67$°C per hour (2).", "2"),
 Q("If the mean of $x, x+2, x+4$ is 10, find $x$.", "Mean $x+2=10$; $x=8$ (2).", "2"),
]
for i, d in enumerate(SETS_[:6]):
    m = sum(d) / len(d); md = st.median(d)
    C.append(Q(f"Find the mean and the median of: {', '.join(map(str,d))}. Which is greater?", f"Mean $={g(round(m,2))}$ (1); median $={g(md)}$ (1); {'mean' if m>md else 'median' if md>m else 'both are equal'} (1).", "1+1+1"))
for d in SETS_[6:10]:
    m = sum(d) / len(d); md = st.median(d)
    C.append(Q(f"The data {', '.join(map(str,d))} is given. Compute the mean and median and comment on which is a better measure.", f"Mean ${g(round(m,2))}$ (1); median ${g(md)}$ (1); comment on spread/outliers (1).", "1+1+1"))
for known, n, mean in [([12, 15, 18, 20], 5, 16), ([8, 10, 14], 4, 11), ([25, 30, 35, 40], 5, 32), ([6, 9, 12, 15, 18], 6, 12), ([40, 50, 60], 4, 50)]:
    x = n * mean - sum(known)
    C.append(Q(f"The mean of {n} observations is {mean}. If {len(known)} of them are {', '.join(map(str,known))}, find the remaining observation.", f"Total $={n*mean}$ (1); sum of known $={sum(known)}$ (1); missing value $={x}$ (1).", "1+1+1"))
C += [
 Q("A line graph shows sales: Jan 20, Feb 25, Mar 30, Apr 28, May 35. Find the month of greatest rise and the average sales.", "Greatest rise is between April and May (a rise of 7) (1.5); average $=138/5=27.6$ (1.5).", "1½+1½"),
 Q("The mean weight of 8 boys is 45 kg. When one boy leaves, the mean becomes 44 kg. Find the weight of the boy who left.", "Total 360; remaining 308 (2); left boy 52 kg (1).", "2+1"),
 Q("Draw a dot plot for 2, 3, 3, 4, 4, 4, 5 and state the most frequent value.", "Dots stacked above each value (2); 4 (1).", "2+1"),
 Q("Find the mean and median of the first ten natural numbers.", "Mean 5.5 (1.5); median 5.5 (1.5).", "1½+1½"),
]
C += [
 Q("The mean of five numbers is 12. If each number is increased by 3, find the new mean and new total.", "New mean 15 (1.5); new total 75 (1.5).", "1½+1½"),
 Q("A bar graph and a line graph show the same data. State one difference in what they emphasise.", "Bar graph compares categories (1.5); line graph shows trend over time (1.5).", "1½+1½"),
 Q("The median of 5 numbers 4, 7, $x$, 12, 15 is 9. Find $x$ and the mean.", "$x=9$ (1); mean $47/5=9.4$ (2).", "1+2"),
 Q("Show that the mean of $a$ and $b$ lies between them.", "Mean $(a+b)/2$ is halfway (3).", "3"),
 Q("Two students' scores in 4 tests are A: 60, 65, 70, 75 and B: 50, 60, 75, 85. Compare means and ranges.", "Both means 67.5 and 67.5 (1.5); ranges 15 and 35 (1.5).", "1½+1½"),
]
C = C[:24]
assert len(B) == 16 and len(C) == 24, (len(B), len(C))
D = [
 Q("(i) Define mean and median. (ii) Find both for 14, 20, 12, 16, 18, 40. (iii) Which is a better measure of the typical value?", "(i) Sum ÷ number; middle value (1.5). (ii) Mean 20, median 17 (2). (iii) Median due to the outlier 40 (1.5).", "1½+2+1½"),
 Q("<b>Case study:</b> A line graph shows the daily temperature: Mon 28, Tue 30, Wed 33, Thu 31, Fri 29, Sat 27, Sun 30. (i) Find the mean. (ii) On which day is the temperature highest? (iii) Find the range and describe the trend.", "(i) $208/7\\approx29.7$°C (2). (ii) Wednesday (1). (iii) Range 6; rises then falls (2).", "2+1+2"),
 Q("(i) The mean of 10 numbers is 24. If two numbers 18 and 30 are removed, find the new mean. (ii) Explain.", "(i) Total 240, remaining 192; mean 24 (3). (ii) Removed numbers average 24 (2).", "3+2"),
 Q("(i) How is a dot plot made? (ii) Construct one for marks 6, 7, 7, 8, 8, 8, 9, 9, 10 and read the mean and median.", "(i) Mark each value on a number line with a dot (2). (ii) Mean 8, median 8 (3).", "2+3"),
 Q("<b>Case study:</b> Five friends' pocket money (₹): 200, 250, 300, 350, 900. (i) Find the mean. (ii) Find the median. (iii) Which better represents them? (iv) What happens without 900?", "(i) 400 (1). (ii) 300 (1). (iii) Median (1). (iv) Mean 275 (2).", "1+1+1+2"),
 Q("(i) Show that the mean of the first $n$ natural numbers is $(n+1)/2$. (ii) Hence find the mean of the first 50.", "(i) Sum $n(n+1)/2$ divided by $n$ (3). (ii) 25.5 (2).", "3+2"),
 Q("(i) A class of 30 has mean 62. A class of 20 has mean 72. Find the combined mean. (ii) Compare.", "(i) $(1860+1440)/50=66$ (3). (ii) Lies between the two means (2).", "3+2"),
 Q("<b>Case study:</b> The monthly rainfall (cm) in a town is Jan 2, Feb 3, Mar 5, Apr 8, May 12, Jun 20. (i) Draw (describe) the line graph. (ii) Find the mean. (iii) Between which months is the rise greatest?", "(i) Plot months against rainfall and join (2). (ii) 8.33 cm (2). (iii) May to June (1).", "2+2+1"),
 Q("(i) Find the median of 17 numbers where the sorted 9th value is 42. (ii) Why?", "(i) 42 (2). (ii) For 17 numbers, the median is the 9th value (3).", "2+3"),
 Q("(i) If each of 9 observations is multiplied by 2, how do the mean and median change? (ii) Illustrate with 3, 5, 7.", "(i) Both are multiplied by 2 (3). (ii) Mean 5 to 10, median 5 to 10 (2).", "3+2"),
 Q("<b>Case study:</b> Marks of two students in 5 tests: A: 70, 72, 74, 76, 78; B: 40, 60, 74, 88, 98. (i) Find both means. (ii) Which is more consistent? (iii) Find the ranges.", "(i) Both 74 (2). (ii) A (1). (iii) 8 and 58 (2).", "2+1+2"),
 Q("(i) Find $x$ if the median of 3, 5, $x$, 9, 11 is 8. (ii) Find the mean.", "(i) $x=8$ (2). (ii) 7.2 (3).", "2+3"),
 Q("(i) Describe how a line graph is read. (ii) Name two real situations best shown by line graphs.", "(i) Axes, plotted points, trend (3). (ii) Temperature, stock prices (2).", "3+2"),
 Q("(i) Show that the sum of deviations of values from their mean is zero for 4, 6, 8, 10, 12. (ii) Explain the balancing idea.", "(i) Mean 8; deviations $-4,-2,0,2,4$ sum 0 (3). (ii) Left and right deviations balance (2).", "3+2"),
 Q("<b>Case study:</b> A cricketer's runs in 8 matches: 12, 45, 0, 38, 62, 18, 45, 90. (i) Find mean and median. (ii) Find range. (iii) Comment.", "(i) Mean 38.75; median $(38+45)/2=41.5$ (2). (ii) 90 (1). (iii) Large variation (2).", "2+1+2"),
 Q("(i) Four numbers have mean 12. If three of them are 8, 10 and 14, find the fourth. (ii) Find the median of the four numbers.", "(i) $4\\times12=48$; $48-32=16$ (3). (ii) Sorted 8, 10, 14, 16; median $(10+14)/2=12$ (2).", "3+2"),
]
assert len(D) == 16, len(D)
SETS, POOL = build(A, B, C, D)
