"""Class 8 Maths Ch 10 Proportional Reasoning-2 - extras."""
from common import AR4, Q

AR = [
 AR4(r"If 5 kg of rice costs ₹300, then 8 kg of rice costs ₹480.", r"The cost of rice is directly proportional to its quantity, so $\dfrac{\text{cost}}{\text{quantity}}$ is constant.", "a",
     r"$300\div5=60$ per kg, and $60\times8=480$; R is the property used."),
 AR4(r"For a fixed distance, the speed of a vehicle and the time taken are inversely proportional.", r"For a fixed time, the work done by workers is directly proportional to the number of workers.", "b",
     r"Both statements are true but are about different situations; R does not explain A."),
 AR4(r"On a map with the scale 1 cm : 5 km, a distance of 4 cm represents 20 km.", r"The scale 1 cm : 5 km means that 5 cm on the map represents 1 km on the ground.", "c",
     r"$4\times5=20$ km, so A is true. R is false: 1 cm on the map represents 5 km."),
 AR4(r"If $x$ and $y$ are inversely proportional, then $\dfrac{x}{y}$ is constant.", r"If $x$ and $y$ are inversely proportional, then $xy$ is constant.", "d",
     r"For inverse proportion the product $xy$ is constant, so A is false and R is true."),
 AR4(r"In a pie chart, a sector of angle $90^\circ$ represents 25% of the data.", r"The whole circle of a pie chart, $360^\circ$, represents 100% of the data.", "a",
     r"$\dfrac{90}{360}\times100=25\%$; R is the basis of the calculation."),
 AR4(r"If 12 pencils cost ₹60, then 18 pencils cost ₹90.", r"If the speed is doubled, the time taken to cover a fixed distance is halved.", "b",
     r"$60\div12=5$ per pencil and $5\times18=90$ so A is true; R is also true but unrelated to the pencil cost."),
]

CASE = [
 Q(r"<b>Case study.</b> The scale of a road map of Rajasthan is 1 cm : 20 km. Two towns are 7.5 cm apart on the map. "
   r"(i) Find the actual distance between the towns. (ii) Two other towns are 260 km apart. What is their distance on the map? (iii) Write the scale as a ratio of the same units. (iv) A bus covers the first distance at 50 km/h. How long does it take, and how long would it take at 75 km/h?",
   r"(i) $7.5\times20=150$ km (1). (ii) $260\div20=13$ cm (1). (iii) $20\text{ km}=20{,}00{,}000$ cm, so $1:20{,}00{,}000$ (1). (iv) At 50 km/h: $150\div50=3$ h (1); at 75 km/h: $150\div75=2$ h (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> 15 workers can build a village road in 24 days, working at the same rate. "
   r"(i) Find the total work in worker-days. (ii) In how many days will 20 workers complete the road? (iii) In how many days will 9 workers complete it? (iv) How many more workers are needed to finish the road in 12 days?",
   r"(i) $15\times24=360$ worker-days (1). (ii) $360\div20=18$ days (1). (iii) $360\div9=40$ days (1). (iv) Workers needed $=360\div12=30$ (1); so $30-15=15$ more workers (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> A survey of 240 students of a school about their favourite sport is shown in a pie chart. Cricket: 96, Football: 60, Kabaddi: 48, Others: 36 students. "
   r"(i) Find the angle of the sector for cricket. (ii) What percentage of students like football? (iii) Find the angle for kabaddi. (iv) Find the percentage and the sector angle for Others, and show that the four angles add up to $360^\circ$.",
   r"(i) $\dfrac{96}{240}\times360^\circ=144^\circ$ (1). (ii) $\dfrac{60}{240}\times100=25\%$ (1). (iii) $\dfrac{48}{240}\times360^\circ=72^\circ$ (1). (iv) Others: $\dfrac{36}{240}\times100=15\%$ and $54^\circ$ (1); $144+90+72+54=360$ (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Direct proportion", [
   r"$x$ and $y$ vary directly if $\dfrac{x}{y}$ is constant, i.e. $\dfrac{x_1}{y_1}=\dfrac{x_2}{y_2}$.",
   r"Increase in one quantity gives a proportional increase in the other (cost and quantity, distance and time at fixed speed)."]),
 ("Inverse proportion", [
   r"$x$ and $y$ vary inversely if $xy$ is constant, i.e. $x_1y_1=x_2y_2$.",
   r"Examples: workers and days (fixed work), speed and time (fixed distance).",
   r"Work $=$ (number of workers) $\times$ (number of days)."]),
 ("Scale and maps", [
   r"Scale $=\dfrac{\text{map distance}}{\text{actual distance}}$; actual distance $=$ map distance $\times$ scale factor.",
   r"Convert to the same unit: 1 km = 1,00,000 cm."]),
 ("Pie charts", [
   r"Sector angle $=\dfrac{\text{value of category}}{\text{total}}\times360^\circ$.",
   r"Percentage of a category $=\dfrac{\text{angle}}{360^\circ}\times100$.",
   r"All sector angles add up to $360^\circ$ and all percentages to 100%."]),
]

MISTAKES = [
 r"Treating inverse proportion as direct: more workers means <b>fewer</b> days, so use $x_1y_1=x_2y_2$.",
 r"Not converting the map scale to the same units (cm to km) before computing.",
 r"Dividing instead of multiplying (or the other way) when converting map distance to actual distance.",
 r"Computing the pie-chart angle as $\dfrac{\text{value}}{\text{total}}\times100$ (percentage) instead of $\times360^\circ$.",
 r"Using direct proportion for quantities that are not proportional (e.g. age and height).",
 r"Not checking that all sector angles add up to $360^\circ$.",
]
