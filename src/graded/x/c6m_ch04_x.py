"""Class 6 Maths Ch 4 Data Handling and Presentation - extras."""
from common import AR4, Q

AR = [
 AR4("In a pictograph where one symbol stands for 10 children, 3 and a half symbols show 35 children.", "A half symbol stands for half of the value of a whole symbol.", "a",
     "3.5 x 10 = 35, and R says what the half symbol means."),
 AR4("In a bar graph all the bars are drawn with the same width.", "The height (or length) of a bar shows the quantity.", "b",
     "Both are true: equal widths keep the graph fair, heights show the data, but R does not explain A."),
 AR4("In a bar graph with scale 1 cm = 20 students, a bar 4 cm tall shows 80 students.", "To find the number from a bar, divide the bar height by the scale value.", "c",
     "4 x 20 = 80, so A is true. You multiply the height by the scale value, so R is false."),
 AR4("A pictograph can use only whole symbols and never a half symbol.", "A half symbol can be used to show half of the value of one symbol.", "d",
     "Half symbols are allowed, so A is false and R is true."),
 AR4("In the data 4, 6, 4, 9, 4, 6 the number 4 occurs 3 times.", "The number of times a value occurs in the data is called its frequency.", "a",
     "4 appears three times, so its frequency is 3."),
 AR4("In a bar graph, the tallest bar belongs to the largest value.", "Bars in a bar graph are drawn on a chosen scale.", "b",
     "Both statements are true, but the scale does not explain why the tallest bar is the largest value."),
]

CASE = [
 Q(r"<b>Case study.</b> A teacher asked 45 children of Class 6 to choose one favourite game. The table shows the votes: Cricket 18, Football 12, Kabaddi 9, Hockey 6. (i) Which game is the most popular? (ii) How many children chose Cricket and Hockey together? (iii) How many more children chose Cricket than Kabaddi? (iv) Which game got exactly twice as many votes as Hockey, and how many children chose the two least popular games together?",
   r"(i) Cricket (1). (ii) $18+6=24$ children (1). (iii) $18-9=9$ more (1). (iv) Football, as $12=2\times6$ (1); Hockey and Kabaddi together: $6+9=15$ children (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A bar graph shows the number of books read last month by four friends. The scale is 1 cm = 5 books. The bar heights are Asha 6 cm, Bilal 4 cm, Charu 7 cm and Dev 3 cm. (i) How many books did Asha read? (ii) How many books did Dev read? (iii) Who read the most books? (iv) How many books did the four friends read in all, and how many more did Charu read than Dev?",
   r"(i) $6\times5=30$ books (1). (ii) $3\times5=15$ books (1). (iii) Charu (35 books) (1). (iv) Bilal read $4\times5=20$, so the total is $30+20+35+15=100$ books (1); Charu read $35-15=20$ more than Dev (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Meera counted the vehicles passing the school gate in one hour and made a tally chart: Cycles 25, Scooters 15, Cars 10, Buses 5. (i) How many vehicles passed in all? (ii) How is the number 15 written in tally marks? (iii) Which kind of vehicle appeared most often? (iv) She draws a bar graph with scale 1 cm = 5 vehicles. Find the bar heights for Cycles and for Cars.",
   r"(i) $25+15+10+5=55$ vehicles (1). (ii) Three groups of five (four strokes crossed by a fifth) (1). (iii) Cycles (1). (iv) Cycles: $25\div5=5$ cm (1); Cars: $10\div5=2$ cm (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Collecting and organising data", [r"Data: information collected as numbers or facts. Tally marks: groups of five (four strokes crossed by a fifth) make counting easy.",
   r"Frequency: the number of times a value occurs. A frequency table lists each value with its frequency.",
   r"Total of all frequencies $=$ total number of observations."]),
 ("Pictograph", [r"One symbol stands for a fixed number of items (the key). A half symbol stands for half that number.",
   r"Number shown $=$ (number of symbols) $\times$ (value of one symbol).",
   r"Number of symbols needed $=$ (quantity) $\div$ (value of one symbol)."]),
 ("Bar graph", [r"Bars have equal width and equal gaps; the height shows the quantity on a chosen scale.",
   r"Quantity $=$ bar height $\times$ scale value (e.g. 4 cm at 1 cm = 20 gives 80).",
   r"Bar height $=$ quantity $\div$ scale value.",
   r"A graph needs a title, labels on both axes, and the scale written clearly."]),
 ("Reading data", [r"Most popular: highest frequency (the value that occurs most often). Least popular: lowest frequency.",
   r"Difference between two items: subtract their values. Total: add all the values."]),
]

MISTAKES = [
 r"Dividing the bar height by the scale (instead of multiplying) to find the quantity, or the reverse when drawing a bar.",
 r"Ignoring the key of a pictograph: one symbol may stand for 5, 10 or 50, not always 1.",
 r"Forgetting the half symbol, or counting it as a whole symbol.",
 r"Counting tally marks wrongly: the crossed bundle is 5, not 4.",
 r"Bars of unequal width or no scale/labels, which makes the graph misleading.",
]
