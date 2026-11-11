"""Class 6 Maths Ch 2 Lines and Angles - extras."""
from common import AR4, Q

AR = [
 AR4(r"An angle of $135^\circ$ is an obtuse angle.", r"An obtuse angle is more than $90^\circ$ and less than $180^\circ$.", "a",
     "135 lies between 90 and 180, and R is exactly the definition."),
 AR4(r"A straight angle measures $180^\circ$.", r"A right angle measures $90^\circ$.", "b",
     "Both statements are true, but the value of a right angle does not explain the value of a straight angle."),
 AR4(r"The minute hand of a clock turns through $90^\circ$ in 15 minutes.", r"The minute hand turns through $30^\circ$ in every minute.", "c",
     r"It turns $360^\circ$ in 60 minutes, i.e. $6^\circ$ per minute, so $15\times6=90^\circ$. A is true, R is false."),
 AR4(r"An angle of $200^\circ$ is an obtuse angle.", r"A reflex angle is more than $180^\circ$ and less than $360^\circ$.", "d",
     r"$200^\circ$ is a reflex angle, so A is false. R is true."),
 AR4("Four points lie on a line. The number of line segments with end points among these points is 6.", "Every pair of points gives exactly one line segment.", "a",
     "Pairs: AB, AC, AD, BC, BD, CD = 6, and R is the reason we count pairs."),
 AR4(r"At 6 o'clock the angle between the hands of a clock is $180^\circ$.", r"At 3 o'clock the angle between the hands of a clock is $90^\circ$.", "b",
     "Both are true, but the 3 o'clock fact does not explain the 6 o'clock fact."),
]

CASE = [
 Q(r"<b>Case study.</b> The clock on the wall of Anil's school shows 2 o'clock. The hour hand turns slowly, and the minute hand moves faster. (i) Through how many degrees does the minute hand turn in 20 minutes? (ii) Through how many degrees does the hour hand turn in 1 hour? (iii) What is the type of the angle between the hands at 4 o'clock? (iv) Find the smaller angle between the hands at 7 o'clock and name the type of the other angle formed.",
   r"(i) $20\times6=120^\circ$ (1). (ii) $30^\circ$ (1). (iii) At 4 o'clock the angle is $4\times30=120^\circ$, an obtuse angle (1). (iv) At 7 o'clock one angle is $210^\circ$ and the smaller angle is $360^\circ-210^\circ=150^\circ$ (1); the $210^\circ$ angle is a reflex angle (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Five bus stops A, B, C, D and E lie along a straight road. The bus conductor notes the distance between every pair of stops. (i) How many line segments have both end points at these stops? (ii) If there were 6 stops, how many segments would there be? (iii) How many new segments are formed when a new stop F is added to the 5 stops? (iv) Find the number of segments for 8 stops and explain your method.",
   r"(i) $\dfrac{5\times4}{2}=10$ (1). (ii) $\dfrac{6\times5}{2}=15$ (1). (iii) $15-10=5$, since F pairs with each of the 5 stops (1). (iv) Each of the 8 stops pairs with 7 others, giving 56, and each segment is counted twice, so $56\div2=28$ segments (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Rohan has a toy robot that faces north. He makes it turn clockwise through $90^\circ$ and then through a further $135^\circ$. (i) What is the type of the first turn? (ii) What is the total angle turned? (iii) What is the type of the total angle? (iv) How many more degrees must the robot turn to complete one full turn? What fraction of a full turn has it already made?",
   r"(i) Right angle (1). (ii) $90^\circ+135^\circ=225^\circ$ (1). (iii) Reflex angle, as $180^\circ<225^\circ<360^\circ$ (1). (iv) $360^\circ-225^\circ=135^\circ$ more (1); fraction made $=\dfrac{225}{360}=\dfrac58$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Basic figures", [r"Line segment: two end points, fixed length. Ray: one end point, goes on forever in one direction. Line: no end points, extends both ways.",
   r"$n$ points on a line give $\dfrac{n(n-1)}{2}$ line segments."]),
 ("Types of angles", [r"Acute: $0^\circ<\theta<90^\circ$.   Right: $\theta=90^\circ$.",
   r"Obtuse: $90^\circ<\theta<180^\circ$.   Straight: $\theta=180^\circ$.",
   r"Reflex: $180^\circ<\theta<360^\circ$.   Complete angle (full turn): $360^\circ$.",
   r"Quarter turn $=90^\circ$; half turn $=180^\circ$; three-quarter turn $=270^\circ$."]),
 ("Clocks", [r"Minute hand: $360^\circ$ in 60 min, i.e. $6^\circ$ per minute.",
   r"Hour hand: $360^\circ$ in 12 h, i.e. $30^\circ$ per hour.",
   r"At $h$ o'clock the angle between the hands is $30h^\circ$; if this is more than $180^\circ$, the smaller angle is $360^\circ-30h^\circ$."]),
 ("Measuring and adding angles", [r"Protractor: place the centre on the vertex and the base line along one arm; read the scale that starts from $0^\circ$ on that arm.",
   r"Adjacent angles add up: $\angle AOB+\angle BOC=\angle AOC$.",
   r"A bisector divides an angle into two equal parts: a $60^\circ$ angle is split into $30^\circ+30^\circ$."]),
]

MISTAKES = [
 r"Reading the wrong scale on the protractor (inner vs outer). Decide first whether the angle is acute or obtuse.",
 r"Using $30^\circ$ per minute for the minute hand; it is $6^\circ$ per minute, and $30^\circ$ per hour is for the hour hand.",
 r"Calling a $200^\circ$ or $225^\circ$ angle obtuse. Obtuse angles are less than $180^\circ$; larger ones are reflex.",
 r"Saying a ray has two end points; a ray has exactly one end point.",
 r"Counting line segments for $n$ points as $n(n-1)$ without dividing by 2 (segment AB and BA are the same).",
 r"Placing the protractor's centre off the vertex, or starting the scale from the wrong arm.",
]
