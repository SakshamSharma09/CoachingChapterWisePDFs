"""Class 6 Maths Ch 4 - Data Handling and Presentation: worksheet + detailed notes."""
from collections import Counter
from libws import *          # W, run
BANK = "c6m_ch04"

# ---- helpers for figures / tables -------------------------------------------
def tbl(head, rows, w="auto"):
    th = "".join(f"<th style='border:1px solid #13286b;background:#e8edf8;padding:1px 7px;font-size:8.6pt'>{h}</th>" for h in head)
    body = "".join("<tr>" + "".join(f"<td style='border:1px solid #13286b;padding:1px 7px;font-size:8.6pt'>{c}</td>" for c in r) + "</tr>" for r in rows)
    return f"<table style='border-collapse:collapse;width:{w};margin:2px 0'><tr>{th}</tr>{body}</table>"

def pic(rows, sym="●", half="◐"):
    """rows = [(name, value_in_half_symbols)] -> table with symbols"""
    out = []
    for n, h in rows:
        out.append([n, sym * (h // 2) + (half if h % 2 else "")])
    return tbl(["", "Symbols"], out)

def bars(labels, vals, step, ymax, unit="", w=330, h=165):
    L, B, T = 38, h - 26, 8; n = len(vals); bw = (w - L - 10) / n * 0.5
    s = f"<svg width='{w}' height='{h}' viewBox='0 0 {w} {h}' xmlns='http://www.w3.org/2000/svg'><line x1='{L}' y1='{T}' x2='{L}' y2='{B}' stroke='#222'/><line x1='{L}' y1='{B}' x2='{w-5}' y2='{B}' stroke='#222'/>"
    k = 0
    while k <= ymax:
        y = B - (B - T) * k / ymax
        s += f"<line x1='{L-3}' y1='{y:.1f}' x2='{L}' y2='{y:.1f}' stroke='#222'/><text x='{L-6}' y='{y+3:.1f}' font-size='8' text-anchor='end'>{k}</text>"
        if k: s += f"<line x1='{L}' y1='{y:.1f}' x2='{w-5}' y2='{y:.1f}' stroke='#e3e8f3'/>"
        k += step
    for i, (lb, v) in enumerate(zip(labels, vals)):
        cx = L + (w - L - 10) * (i + .5) / n; y = B - (B - T) * v / ymax
        s += f"<rect x='{cx-bw/2:.1f}' y='{y:.1f}' width='{bw:.1f}' height='{B-y:.1f}' fill='#4a6fc4'/><text x='{cx:.1f}' y='{B+12}' font-size='9' text-anchor='middle'>{lb}</text>"
    if unit: s += f"<text x='{L+4}' y='{T+8}' font-size='8'>{unit}</text>"
    return s + "</svg>"

def ft(counter, order):
    return "; ".join(f"{k}: {counter[k]}" for k in order)

# ---- data (answers are computed from these) ---------------------------------
fruit = "Apple Mango Banana Mango Apple Apple Banana Mango Apple Mango Orange Apple Banana Mango Apple".split()
cf = Counter(fruit); assert (cf["Apple"], cf["Mango"], cf["Banana"], cf["Orange"], len(fruit)) == (6, 5, 3, 1, 15)
marks = [7, 8, 6, 9, 7, 5, 8, 7, 6, 10, 7, 8, 9, 6, 7, 8, 5, 7, 9, 6]; cm = Counter(marks); assert len(marks) == 20
shoe = [5, 6, 5, 7, 6, 5, 8, 6, 5, 7]; cs = Counter(shoe); assert (cs[5], cs[6], cs[7], cs[8]) == (4, 3, 2, 1)
d14 = [2, 3, 5, 2, 3, 2, 5, 3, 2, 2]; c14 = Counter(d14); assert (c14[2], c14[3], c14[5]) == (5, 3, 2)
sib = [1, 2, 0, 1, 3, 2, 1, 1, 2, 0, 4, 1, 2, 1, 3, 2, 1, 0, 2, 1, 2, 3, 1, 2]; csb = Counter(sib); assert len(sib) == 24
more2 = sum(v for k, v in csb.items() if k > 2)
veh = dict(Cycle=35, Bike=60, Car=45, Bus=15, Auto=25); assert sum(veh.values()) == 180
assert 18 + 12 + 8 == 38 and 50 - 38 == 12 and 40 + 55 + 35 + 70 == 200 and 20 + 35 + 10 == 65
assert 70 + 45 + 85 + 30 + 55 == 285 and 14 + 7 + 6 + 9 + 4 == 40 and 18 + 25 + 21 == 64 and 22 + 20 + 26 == 68
assert 8 + 6 + 8 + 5 + 3 == 30 and 8 + 6 + 5 == 19 and 45 * 8 == 360 and 195 * 8 == 1560 and 35 + 45 + 40 == 120
assert 40 + 25 + 10 == 75 and 55 + 20 + 18 == 93 and 120 + 135 + 110 + 95 == 460 and 12 + 18 + 15 + 24 + 21 == 90
assert 45 + 50 + 40 + 55 + 60 == 250 and 60 + 90 + 40 + 110 == 300

WS = [
# ------------------------------------------------------------------ EASY
W("Tally marks show one bundle of five strokes and 3 more single strokes. The frequency is", 1, "(c) 8. A bundle stands for 5, so $5+3=8$. (1)", "E", opts=["3", "5", "8", "15"]),
W("In a pictograph one symbol stands for 20 books. The number of books shown by $4\\frac{1}{2}$ symbols is", 1, "(b) 90. $4\\times20=80$ and half a symbol is 10, so $80+10=90$. (1)", "E", opts=["80", "90", "85", "100"]),
W("In a bar graph the scale is 1 cm = 5 books. A bar 6 cm long shows", 1, "(a) 30 books. $6\\times5=30$. (1)", "E", opts=["30 books", "11 books", "56 books", "6 books"]),
W("In the data 3, 5, 3, 2, 3, 5, the frequency of 3 is", 1, "(d) 3. The number 3 appears three times. (1)", "E", opts=["1", "2", "5", "3"]),
W("A graph that uses small pictures or symbols to show numbers is called a", 1, "(b) pictograph. (1)", "E", opts=["bar graph", "pictograph", "tally table", "number line"]),
W("Data that has just been collected and has not yet been arranged is called", 1, "(c) raw data. (1)", "E", opts=["frequency data", "key data", "raw data", "scale data"]),
W("The class wrote the favourite fruit of 15 children in this order: " + ", ".join(fruit) + ". Make a frequency table using tally marks and check that the total is 15.", 2,
  f"Apple 6, Mango 5, Banana 3, Orange 1 (tally: Apple ||||̸ |, Mango ||||̸, Banana |||, Orange |). Total $6+5+3+1=15$. (2)", "E", wp=True),
W("The pictograph shows the books read by three children in a month. One ● stands for 10 books and ◐ stands for 5 books. How many books did each read, and who read the most?", 2,
  "Anil: 4 symbols $=40$ books. Binu: 3 symbols and a half $=35$ books. Chitra: 6 symbols $=60$ books. Chitra read the most. (2)", "E", wp=True,
  fig=tbl(["Child", "Books read"], [["Anil", "●●●●"], ["Binu", "●●●◐"], ["Chitra", "●●●●●●"]])),
W("The bar graph shows the number of students in four school houses. (i) Which house has the most students? (ii) How many students are in Green house? (iii) What is the total?", 2,
  "(i) Blue house (40). (ii) 30 students. (iii) $25+40+30+15=110$ students. (1+0.5+0.5)", "E", wp=True,
  fig=bars(["Red", "Blue", "Green", "Yellow"], [25, 40, 30, 15], 5, 40, "Students")),
W("Write the tally marks for the number 13 using bundles of five.", 1, "Two bundles of five and three single strokes: ||||̸ ||||̸ |||, since $5+5+3=13$. (1)", "E"),
W("In a pictograph of cycles sold in a shop, one symbol stands for 20 cycles. How would you show 70 cycles?", 2, "$70=3\\times20+10$. So draw 3 full symbols and 1 half symbol ($3\\frac{1}{2}$ symbols). (2)", "E", wp=True),
W("A shopkeeper sold 40, 55, 35 and 70 notebooks in four weeks. A bar graph is to be drawn with 1 cm = 10 notebooks. Find the length of each bar.", 2, "Lengths $=40\\div10=4$ cm, $55\\div10=5.5$ cm, $35\\div10=3.5$ cm, $70\\div10=7$ cm. (2)", "E", wp=True),
W("True or False? Give a reason. “The bars of a bar graph can have different widths.”", 2, "False. All bars must have the same width (and equal gaps) so that only the length of the bar tells the value. (1+1)", "E"),
W("The rainfall in a village was 20 mm on Monday, 35 mm on Tuesday and 10 mm on Wednesday. Find the total rainfall and the difference between the greatest and the least.", 2, "Total $=20+35+10=65$ mm. Difference $=35-10=25$ mm. (1+1)", "E", wp=True),
W("Fill in the blanks: (i) The number of times a value occurs is called its ____. (ii) The picture in a pictograph that tells what one symbol means is called the ____.", 1, "(i) frequency; (ii) key. (1)", "E"),
W("Out of 50 students, 18 like cricket, 12 like football, 8 like hockey and the rest like badminton. How many like badminton?", 2, "Total of the three games $=18+12+8=38$. Badminton $=50-38=12$ students. (2)", "E", wp=True),
W("Name two things that every graph should have.", 2, "A title (what the graph is about) and labels or a scale on the axes (and a key for a pictograph). (1+1)", "E"),

# ------------------------------------------------------------------ MEDIUM
W("The marks of 20 students in a test out of 10 are: " + ", ".join(map(str, marks)) + ". Make a frequency table for the marks 5 to 10. Which mark is the most common?", 3,
  f"Frequencies {ft(cm, [5, 6, 7, 8, 9, 10])}. Total $=20$. The most common mark is 7 (it occurs {cm[7]} times). (2+1)", "M", wp=True),
W("The bar graph shows the vehicles that passed a school gate in one hour. (i) How many vehicles passed in all? (ii) How many more bikes than cars passed?", 3,
  "(i) $35+60+45+15+25=180$ vehicles. (2) (ii) $60-45=15$ more bikes. (1)", "M", wp=True,
  fig=bars(["Cycle", "Bike", "Car", "Bus", "Auto"], [35, 60, 45, 15, 25], 10, 60, "Vehicles")),
W("The pictograph shows trees planted by four classes. One ● stands for 20 trees and ◐ for 10 trees. Find the trees planted by each class, the total, and the difference between the most and the fewest.", 3,
  "6A: 3 symbols $=60$; 6B: $4\\frac12=90$; 6C: 2 symbols $=40$; 6D: $5\\frac12=110$. Total $=60+90+40+110=300$. Difference $=110-40=70$. (3)", "M", wp=True,
  fig=tbl(["Class", "Trees planted"], [["6A", "●●●"], ["6B", "●●●●◐"], ["6C", "●●"], ["6D", "●●●●●◐"]])),
W("Fruit sold in a week (kg): Apple 45, Banana 60, Grapes 30, Orange 55. A bar graph is drawn with the scale 1 cm = 10 kg. Find the length of each bar.", 2, "Apple 4.5 cm, Banana 6 cm, Grapes 3 cm, Orange 5.5 cm. (2)", "M", wp=True),
W("In a bar graph the scale is 1 cm = 8 students. (i) The bar for Class 6A is 4.5 cm long. How many students are in 6A? (ii) How long should the bar be for 52 students?", 2, "(i) $4.5\\times8=36$ students. (ii) $52\\div8=6.5$ cm. (1+1)", "M", wp=True),
W("In a pictograph one symbol stands for 10 pens. Meera says 5½ symbols show 5.5 pens. Find her mistake and the correct number.", 2, "She forgot the key. One symbol is 10 pens, so $5\\frac12$ symbols $=5\\times10+5=55$ pens. (2)", "M"),
W("The table shows the number of students absent each day. (i) On which day was nobody absent? (ii) How many absences were there in the week?", 2,
  "(i) Thursday. (ii) $4+7+3+0+6+5=25$ absences. (1+1)", "M", wp=True,
  fig=tbl(["Day", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], [["Absent", "4", "7", "3", "0", "6", "5"]])),
W("For each task, say whether data is collected by asking, counting, measuring or observing: (a) the heights of 10 friends, (b) the favourite sports of classmates, (c) the number of vehicles passing the gate, (d) the number of birds seen on a tree.", 2,
  "(a) measuring; (b) asking (survey); (c) counting; (d) observing (and counting). (2)", "M"),
W("Shoe sizes of 10 children are: " + ", ".join(map(str, shoe)) + ". Make a frequency table and say which size is the most common.", 3,
  f"{ft(cs, [5, 6, 7, 8])}. Total 10. Size 5 is the most common (4 children). (2+1)", "M", wp=True),
W("Four values to be shown in a bar graph are 120, 80, 200 and 160. The graph paper allows a tallest bar of 10 cm. Choose a suitable scale and find the bar lengths.", 2, "Take 1 cm = 20 (largest bar $200\\div20=10$ cm). Lengths: 6 cm, 4 cm, 10 cm, 8 cm. (2)", "M", wp=True),
W("A bar graph shows that Vanilla ice-creams sold are 30 and Mango ice-creams sold are 60. How many times as many Mango as Vanilla? If the Vanilla bar is 3 cm long, how long is the Mango bar?", 2, "$60\\div30=2$ times. The Mango bar is twice as long, 6 cm. (2)", "M", wp=True),
W("A village's rainfall (mm): June 120, July 300, August 240, September 90, October 30. Find (i) the month of the heaviest rain, (ii) the total, (iii) how many times July's rain is October's.", 3,
  "(i) July. (ii) $120+300+240+90+30=780$ mm. (iii) $300\\div30=10$ times. (1+1+1)", "M", wp=True),
W("A bar graph has its vertical axis starting at 30 instead of 0. A bar for 40 is drawn 10 units tall and a bar for 60 is drawn 30 units tall. The second bar looks how many times the first? What is the true ratio? Why can this mislead?", 3,
  "It looks $30\\div10=3$ times as tall. The true ratio is $60\\div40=1.5$. A graph that does not start at zero exaggerates differences and misleads the reader. (3)", "M"),
W("Data: " + ", ".join(map(str, d14)) + ". Write the frequency of 2, 3 and 5. Check that the total is 10.", 2, f"{ft(c14, [2, 3, 5])}. $5+3+2=10$. (2)", "M"),
W("The school canteen sold this number of samosas from Monday to Friday: 45, 50, 40, 55, 60. Find the total sold and how many more were sold on Friday than on Wednesday.", 2, "Total $=45+50+40+55+60=250$. Friday $-$ Wednesday $=60-40=20$ more. (1+1)", "M", wp=True),
W("In a pictograph, one symbol stands for 50 cans. How many symbols (full and half) are needed to show 175 cans?", 2, "Half a symbol $=25$. $175=3\\times50+25$, so 3 full symbols and 1 half symbol ($3\\frac12$ symbols). (2)", "M", wp=True),
W("Aman wants to find the favourite subject of the 40 students of his class. Write the steps he should follow, in order.", 3, "(1) Decide the question and the choices (e.g. Maths, Science, English, Hindi, Other). (2) Ask every student and record each answer with a tally mark. (3) Count the tally marks to get the frequency of each subject. (4) Write them in a frequency table and check the total is 40. (5) Draw a bar graph or pictograph with title, scale and labels. (3)", "M", wp=True),
W("School enrolment: Class VI 120, VII 135, VIII 110, IX 95. Write the classes in order from the most to the fewest students and find the total.", 2, "VII (135), VI (120), VIII (110), IX (95). Total $=120+135+110+95=460$ students. (2)", "M", wp=True),
W("The bar graph shows the water used by a hostel on five days. (i) On which day was the most water used? (ii) Find the total use. (iii) How much more was used on the highest day than on the lowest day?", 3,
  "(i) Tuesday (55 hundred litres). (ii) $40+55+30+45+50=220$ hundred litres $=22{,}000$ L. (iii) $55-30=25$ hundred litres $=2{,}500$ L. (1+1+1)", "M", wp=True,
  fig=bars(["Mon", "Tue", "Wed", "Thu", "Fri"], [40, 55, 30, 45, 50], 10, 60, "Water (hundred litres)")),

# ------------------------------------------------------------------ HARD
W("The bar graph shows the runs scored by five batters in a match. (i) Find the team total. (ii) Which batters scored more than 50 runs? (iii) How many more runs did the highest scorer make than the lowest scorer?", 4,
  "(i) $70+45+85+30+55=285$ runs. (2) (ii) Asha (70), Chetan (85) and Esha (55). (1) (iii) $85-30=55$ runs. (1)", "H", wp=True,
  fig=bars(["Asha", "Bhanu", "Chetan", "Dev", "Esha"], [70, 45, 85, 30, 55], 10, 90, "Runs")),
W("The milk collected by a dairy was 175 L on Monday, 250 L on Tuesday and 325 L on Wednesday. A pictograph is to be drawn in which a half symbol stands for 25 L. What does one full symbol stand for, and how many symbols (full and half) are needed for each day?", 4,
  "Half symbol $=25$ L, so one full symbol $=50$ L. Monday $175=3\times50+25$: $3\frac12$ symbols. Tuesday $250=5\times50$: 5 symbols. Wednesday $325=6\times50+25$: $6\frac12$ symbols. (4)", "H", wp=True),
W("Thirty students were asked their favourite colour. Red 8, Blue 6, Green ?, Yellow 5, Pink 3. (i) Find the number who chose Green. (ii) If a bar graph uses 1 cm = 2 students, find the length of each bar.", 4,
  "(i) $8+6+5+3=22$, so Green $=30-22=8$. (1.5) (ii) Red 4 cm, Blue 3 cm, Green 4 cm, Yellow 2.5 cm, Pink 1.5 cm. (2.5)", "H", wp=True),
W("A student draws a bar graph of the marks of four friends. She gives no title, makes the bars of different widths, and the vertical scale reads 0, 10, 20, 50, 60. Write three mistakes and say how to correct them.", 3,
  "(1) No title: add a title saying what the graph shows. (2) Unequal bar widths: draw all bars with the same width and equal gaps. (3) Scale not uniform (20 to 50 jumps 30 while others jump 10): use equal steps 0, 10, 20, 30, 40, 50, 60. (1 each)", "H"),
W("A shop's yearly sales: Cycles 40 in 2022 and 55 in 2023; Scooters 25 and 20; Cars 10 and 18. (i) Which items increased and by how much? (ii) Find the total sales in each year and the change.", 4,
  "(i) Cycles up by 15; Cars up by 8; Scooters down by 5. (2) (ii) 2022: $40+25+10=75$. 2023: $55+20+18=93$. Increase $=93-75=18$. (2)", "H", wp=True,
  fig=tbl(["Item", "2022", "2023"], [["Cycles", "40", "55"], ["Scooters", "25", "20"], ["Cars", "10", "18"]])),
W("In a class of 40 students: Cricket 14, Football ?, Hockey 6, Kabaddi 9, Badminton 4. (i) Find the number for Football. (ii) Which is the second most popular game? (iii) If a pictograph uses ● for 2 students, how many symbols are needed for Kabaddi?", 3,
  "(i) $14+6+9+4=33$, Football $=40-33=7$. (1) (ii) Kabaddi (9), after Cricket (14). (1) (iii) $9\\div2=4\\frac12$, so 4 full symbols and 1 half symbol. (1)", "H", wp=True),
W("Ria wants to show 55 students in a pictograph. She chooses a key of 1 symbol = 20 students. Why is this a poor choice? Suggest two better keys and the number of symbols they need.", 3,
  "55 is not a multiple of 10 or 20 and would need a quarter of a symbol, which is hard to draw. Key 1 symbol = 10: $5\\frac12$ symbols. Key 1 symbol = 5: 11 symbols. (3)", "H"),
W("In a bar graph the scale starts at 0. Bar A is twice as long as bar B. Is the value of A twice the value of B? What if the scale started at 20? Take A = 80 and B = 50 as an example.", 3,
  "With the scale starting at 0, yes: length is proportional to value. If the scale starts at 20, the bar lengths show (value $-20$): A $=60$ and B $=30$ units, so A looks twice as long as B, but $80\\div50=1.6$, not 2. So the rule works only when the scale starts at 0. (3)", "H"),
W("The number of brothers and sisters of 24 students is: " + ", ".join(map(str, sib)) + ". Make a frequency table for 0, 1, 2, 3, 4. How many students have more than 2 brothers and sisters?", 4,
  f"{ft(csb, [0, 1, 2, 3, 4])}. Total $=24$. More than 2: $3$ brothers/sisters ({csb[3]}) + $4$ ({csb[4]}) $={more2}$ students. (3+1)", "H", wp=True),
W("A hospital had these numbers of patients Monday to Sunday: 24, 30, 18, 36, 42, 12, 6. A bar graph is drawn with 1 cm = 6 patients. Find each bar length. Is a graph paper 8 cm tall enough?", 3,
  "Lengths: 4, 5, 3, 6, 7, 2, 1 cm. The tallest bar is 7 cm, so an 8 cm graph paper is enough. (3)", "H", wp=True),
W("The table gives boys and girls in classes 6, 7 and 8. Find (i) the total boys, (ii) the total girls, (iii) the class with most students, (iv) how many more girls than boys there are.", 4,
  "(i) $18+25+21=64$. (ii) $22+20+26=68$. (iii) Class 6: 40; Class 7: 45; Class 8: $21+26=47$. So Class 8. (iv) $68-64=4$ more girls. (1 each)", "H", wp=True,
  fig=tbl(["Class", "Boys", "Girls"], [["6", "18", "22"], ["7", "25", "20"], ["8", "21", "26"]])),
W("Anil's frequency table of favourite fruit has: Apple 8, Mango 6, Banana 5 and says the total is 20. Check it. What should the total be, and what could Anil have done wrong? How many votes are missing if 20 children were asked?", 3,
  "$8+6+5=19$, not 20. The total should be 19. He may have counted or tallied one answer twice or missed one. If 20 children were asked, one answer is missing from the table. (3)", "H", wp=True),
W("A bar graph shows a stationery shop's sales of notebooks from Monday to Saturday. (i) On which days did it sell more than 30? (ii) Find the total sold in the week. (iii) If the profit is ₹8 on each notebook, find the profit on Thursday and in the whole week.", 5,
  "(i) Tuesday (35), Thursday (45), Saturday (40). (1) (ii) $20+35+30+45+25+40=195$ notebooks. (2) (iii) Thursday: $45\\times8=₹360$. Week: $195\\times8=₹1560$. (2)", "H", wp=True,
  fig=bars(["Mon", "Tue", "Wed", "Thu", "Fri", "Sat"], [20, 35, 30, 45, 25, 40], 5, 45, "Notebooks")),
W("Three shops sold cycles in a month. In the pictograph one ● stands for 10 cycles and ◐ for 5. (i) Find the cycles sold by each shop and the total. (ii) How many more did shop C sell than shop B? (iii) If each cycle sells for ₹3,500, how much did shop A earn?", 4,
  "(i) A: 5 symbols $=50$; B: $3\frac12=35$; C: 7 symbols $=70$. Total $=50+35+70=155$. (2) (ii) $70-35=35$ more. (1) (iii) $50\times3500=₹1{,}75{,}000$. (1)", "H", wp=True,
  fig=tbl(["Shop", "Cycles sold"], [["A", "●●●●●"], ["B", "●●●◐"], ["C", "●●●●●●●"]])),
]

CH = dict(num=4, title="Data Handling and Presentation", tag="Maths (Part 1)",
 intro="We meet data every day: marks in a test, runs in a match, rain in a month, items sold in a shop. This chapter shows how to collect data, organise it with tally marks and frequency tables, present it in pictographs and bar graphs, read the graphs correctly and spot graphs that mislead.",
 big_questions=["How do we collect and organise data?", "How do we draw and read pictographs and bar graphs with a key or scale?", "How can a graph mislead us?"],
 blocks=[
 ("h2", "4.1 What Is Data? Collecting It"),
 ("note", "DEFINITION", "**Data** is a collection of facts, numbers or observations gathered to get information. **Raw data** is data as it is first collected, before it is arranged. A **survey** is a way of collecting data by asking many people the same question."),
 ("p", "Data can be collected by **asking** (the favourite subject), **counting** (vehicles passing the gate), **measuring** (heights, rainfall) or **observing** (birds on a tree). Before collecting, decide the question, the group to ask, the possible answers and how to record them."),
 ("h2", "4.2 Organising Data: Tally Marks and Frequency Tables"),
 ("steps", [("Step 1 — Tally", "Make one stroke for every answer. After four strokes the fifth stroke is drawn across them, making a bundle of 5, so counting is quick and neat."), ("Step 2 — Count", "Convert each tally group to a number called the **frequency**."), ("Step 3 — Table", "Write the categories and their frequencies in a **frequency table** and check that the total equals the number of answers collected.")]),
 ("note", "DEFINITION", "The **frequency** of a value is the number of times it occurs in the data."),
 ("table", ["Fruit", "Tally marks", "Frequency"], [["Apple", "||||̸ |", "6"], ["Mango", "||||̸", "5"], ["Banana", "|||", "3"], ["Orange", "|", "1"], ["**Total**", "", "**15**"]]),
 ("p", "In the data 3, 5, 3, 2, 3, 5 the frequency of 3 is 3, of 5 is 2 and of 2 is 1, total 6. The value with the highest frequency is the most common (popular) one; in the table above it is Apple. **Two bundles of five and three strokes** show 13. A good habit is to check that the frequencies add up to the number of observations."),
 ("h2", "4.3 Pictographs"),
 ("p", "A **pictograph** uses a small picture or symbol to stand for a fixed number of items. The meaning of one symbol is written in the **key**. A full symbol stands for the whole number; a **half symbol** stands for half of it."),
 ("table", ["Key", "Symbols shown", "Value"], [["1 symbol = 20 books", "4½ symbols", "4 × 20 + 10 = 90 books"], ["1 symbol = 10 pens", "5½ symbols", "5 × 10 + 5 = 55 pens"], ["1 symbol = 50 cans", "3½ symbols", "3 × 50 + 25 = 175 cans"], ["1 symbol = 20 cycles", "3½ symbols", "70 cycles"]]),
 ("table", ["Aspect", "Pictograph"], [["Good for", "attractive, quick to read, good for small numbers"], ["Weak", "hard to show exact values or very large numbers; half or quarter symbols are inexact"], ["Always give", "title, key (what one symbol means), labels"]]),
 ("note", "REMEMBER", "Choose a key that divides the numbers neatly. For 55 students a key of 10 (5½ symbols) or 5 (11 symbols) is easy; a key of 20 would need a quarter symbol."),
 ("h2", "4.4 Bar Graphs"),
 ("note", "DEFINITION", "A **bar graph** shows data as bars of **equal width** with **equal gaps**. The **length (height)** of each bar is proportional to the value. The **scale** tells how much one unit of length stands for, e.g. 1 cm = 10 notebooks."),
 ("steps", [("Step 1", "Decide the title and what each axis shows (categories on one axis, numbers on the other)."), ("Step 2", "Choose a **scale** so that the largest value fits the paper, e.g. 1 cm = 10 notebooks, or 1 cm = 20 when the values go up to 200 and the paper allows 10 cm."), ("Step 3", "Draw bars of the same width with equal gaps; **bar length = value ÷ scale**."), ("Step 4", "Label both axes, mark the scale on the number axis and write the title.")]),
 ("note", "FORMULA", "**Bar length = value ÷ scale** and **value = bar length × scale**. With 1 cm = 5 books a 6 cm bar shows 6 × 5 = 30 books; with 1 cm = 8 students, 52 students need 52 ÷ 8 = 6.5 cm."),
 ("table", ["Question on a bar graph", "How to answer"], [["Which is largest or smallest?", "compare the bar lengths"], ["Total", "add all the values"], ["Difference (how many more)", "subtract the two values"], ["How many times as much?", "divide the larger value by the smaller"], ["Which are more than 30?", "pick the bars that go above the 30 line"]]),
 ("h2", "4.5 Reading Graphs Carefully"),
 ("ul", ["Read the **title**, the **scale** and the **labels** first.", "If one bar is twice as long as another, its value is twice as much, **provided the scale starts at zero**.", "A graph with **uneven bar widths**, a **non-uniform scale** or a scale that is **cut off** (does not start at 0) makes small differences look large and can mislead.", "Pictures enlarged in both directions look much more than twice as big and also mislead.", "Good presentation (neat bars, clear labels, a title) makes a graph honest and easy to use."]),
 ("note", "IMPORTANT", "Example of misleading: an axis starts at 30 and bars for 40 and 60 are drawn 10 and 30 units tall. The second bar looks 3 times as tall, but the real ratio is 60 ÷ 40 = 1.5."),
 ("h2", "4.6 Choosing the Right Way to Show Data"),
 ("table", ["Way of showing", "Best used when", "What to remember"], [["Frequency table with tally marks", "you are collecting raw data and want to count quickly", "bundles of 5; total must match the number of observations"], ["Pictograph", "numbers are small and you want an attractive, easy picture", "give a key; half symbol = half of the key"], ["Bar graph", "numbers are large or you want to compare categories exactly", "equal width, equal gaps, uniform scale starting at 0"]]),
 ("p", "A table gives the exact numbers, a pictograph gives a quick picture and a bar graph makes comparison of sizes easy. The same data can be shown in all three ways. For example, the favourite fruit of 15 children (Apple 6, Mango 5, Banana 3, Orange 1) can be a table, a pictograph with 1 symbol = 1 child, or a bar graph with 1 cm = 1 child."),
 ("ul", ["**Largest and smallest:** look for the tallest and shortest bar, or the row with the most and fewest symbols.", "**Increase or decrease:** when two years are given, subtract the old value from the new value; a negative change is a decrease (Scooters fell from 25 to 20, down by 5).", "**Profit or cost problems:** first read the number from the graph, then multiply by the price or profit per item (45 notebooks × ₹8 = ₹360).", "**Checking:** the parts must add up to the whole. If 8 + 6 + 5 = 19 but the table says 20, one answer has been missed or the total is wrong."]),
 ("h2", "4.7 Worked Examples"),
 ("steps", [
  ("Example 1 — Frequency table", "Shoe sizes 5, 6, 5, 7, 6, 5, 8, 6, 5, 7 give 5: 4, 6: 3, 7: 2, 8: 1 (total 10). The most common size is 5."),
  ("Example 2 — Pictograph (key = 20)", "6A 3 symbols = 60; 6B 4½ = 90; 6C 2 = 40; 6D 5½ = 110. Total = 300 trees. Most − fewest = 110 − 40 = 70."),
  ("Example 3 — Bar lengths", "Sales 40, 55, 35, 70 notebooks with 1 cm = 10: bars of 4, 5.5, 3.5 and 7 cm."),
  ("Example 4 — Reading a bar graph", "Vehicles: Cycle 35, Bike 60, Car 45, Bus 15, Auto 25. Total = 180. Bikes − cars = 15."),
  ("Example 5 — Finding a missing frequency", "40 students: Cricket 14, Hockey 6, Kabaddi 9, Badminton 4, Football ?. 14 + 6 + 9 + 4 = 33, so Football = 7."),
  ("Example 6 — Comparing two years", "2022: 40 + 25 + 10 = 75. 2023: 55 + 20 + 18 = 93. Increase = 18."),
  ("Example 7 — Profit from a graph", "Thursday sales 45 notebooks at ₹8 profit each: 45 × 8 = ₹360. Week total 195 notebooks: 195 × 8 = ₹1,560.")]),
 ("h2", "4.8 Word Problems: How to Translate"),
 ("steps", [
  ("Step 1 — Read the title, key or scale", "This tells what one symbol or one unit of length means."),
  ("Step 2 — Find the numbers", "Convert symbols to numbers (count × key) or bar lengths to values (length × scale)."),
  ("Step 3 — Decide the operation", "‘in all’ means add; ‘how many more’ means subtract; ‘how many times’ means divide."),
  ("Step 4 — Answer with the unit", "Write the unit (kg, books, mm, ₹) and check the answer against the graph.")]),
 ("note", "REMEMBER", "Common mistakes: (1) forgetting the key and reading 5½ symbols as 5.5; (2) drawing bars of different widths; (3) a scale with unequal steps; (4) a total in the frequency table that does not match the number of observations; (5) forgetting a title and labels."),
 ("h2", "Quick Revision: Likely Exam Questions"),
 ("qa", [
  ("What is data? Give an example.", "Facts or numbers collected to get information, e.g. the marks of students in a test."),
  ("Show 13 with tally marks.", "Two bundles of five and three single strokes."),
  ("A pictograph symbol stands for 20. What do 4½ symbols stand for?", "4 × 20 + 10 = 90."),
  ("Why is a scale needed in a bar graph?", "It decides the bar lengths so that the values fit on the paper and can be read correctly."),
  ("State two rules for drawing a bar graph.", "Bars have equal width and equal gaps; the scale is uniform and the axes and title are labelled."),
  ("What is the frequency of 5 in 5, 3, 5, 2, 3, 5?", "3."),
  ("A bar of 6 cm with scale 1 cm = 5 books shows how many books?", "6 × 5 = 30 books."),
  ("Out of 50 students 18 like cricket, 12 football, 8 hockey and the rest badminton. How many like badminton?", "50 − (18 + 12 + 8) = 12."),
  ("How can a graph mislead?", "Uneven bar widths, a non-uniform or cut-off scale, or enlarged pictures exaggerate differences."),
  ("Why should every graph have a title and a key or scale?", "The title says what the graph is about; the key or scale tells what each symbol or unit of length means."),
 ]),
 ],
 takeaways=["**Data** is collected by asking, counting, measuring or observing and organised with **tally marks** (bundles of 5) in a **frequency table**.",
  "**Frequency** = how many times a value occurs; the frequencies must add up to the total number of observations.",
  "A **pictograph** needs a **key**: number of symbols × key = value; a half symbol is half of the key.",
  "A **bar graph** has bars of equal width and gaps and a uniform **scale**: bar length = value ÷ scale; value = bar length × scale.",
  "‘In all’ means add, ‘how many more’ means subtract, ‘how many times’ means divide; give the unit in the answer.",
  "A scale that does not start at **zero**, uneven bars or unequal steps make a graph **misleading**.",
  "Always read the title, labels, key and scale first and check that the totals match."])

if __name__ == "__main__": run(__file__, BANK, 6, "Maths", WS, CH)
