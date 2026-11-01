import random
from lib import mcq, Q, OR
from mk9 import M4, build
R = random.Random(707)
A = []
for d, t in [(120, 2), (150, 3), (90, 1.5), (200, 4), (360, 6), (75, 1.5), (240, 4), (180, 2)]:
    v = d / t
    A.append(M4(f"A bus covers {d} km in {t:g} hours. Its average speed is:", f"{v:g} km/h", [f"{d*t:g} km/h", f"{v+10:g} km/h", f"{v/2:g} km/h"], "speed = distance ÷ time"))
for v, t in [(60, 3), (45, 2), (25, 4), (12, 5), (80, 1.5)]:
    d = v * t
    A.append(M4(f"A car moves at a constant {v} km/h for {t:g} hours. The distance covered is:", f"{d:g} km", [f"{v/t:g} km", f"{d+v:g} km", f"{d/2:g} km"], "distance = speed × time"))
for d, v in [(100, 25), (90, 30), (60, 20), (240, 60)]:
    t = d / v
    A.append(M4(f"A cyclist travels {d} km at {v} km/h. The time taken is:", f"{t:g} hours", [f"{d*v:g} hours", f"{t*2:g} hours", f"{t+1:g} hours"], "time = distance ÷ speed"))
for kmh in [36, 72, 54, 108]:
    A.append(M4(f"{kmh} km/h is equal to:", f"{kmh*5/18:g} m/s", [f"{kmh*18/5:g} m/s", f"{kmh/60:g} m/s", f"{kmh:g} m/s"], "1 km/h = 5/18 m/s"))
for ms in [10, 15, 20, 5]:
    A.append(M4(f"{ms} m/s is equal to:", f"{ms*18/5:g} km/h", [f"{ms*5/18:.1f} km/h", f"{ms*60:g} km/h", f"{ms*10:g} km/h"], "multiply by 18/5"))
A += [
 M4("The SI unit of time is the:", "second", ["minute", "hour", "day"], "s"),
 M4("The time taken by a pendulum to complete one oscillation is its:", "time period", ["frequency", "amplitude", "speed"], "T"),
 M4("The to-and-fro motion of a pendulum bob from one extreme to the other and back is one:", "oscillation", ["rotation", "revolution", "vibration only"], "complete cycle"),
 M4("The time period of a simple pendulum depends mainly on its:", "length", ["mass of bob", "colour", "material of bob"], "longer pendulum takes more time"),
 M4("A pendulum clock uses the:", "regular oscillation of a pendulum", ["Sun's shadow", "water flow", "sand flow"], "to measure time"),
 M4("The ancient instrument that used the shadow of a gnomon to tell time is the:", "sundial", ["clepsydra", "hourglass", "pendulum clock"], "Sun's shadow"),
 M4("A sundial cannot be used:", "at night or on cloudy days", ["in the morning", "in the afternoon", "in summer"], "needs sunlight"),
 M4("A water clock is also called:", "clepsydra", ["hourglass", "sundial", "stopwatch"], "water flow measures time"),
 M4("The speed of an object is:", "distance covered per unit time", ["time per unit distance", "force per unit area", "mass per unit volume"], "definition"),
 M4("The SI unit of speed is:", "metre per second", ["kilometre", "second per metre", "metre"], "m/s"),
 M4("The motion along a straight line is called:", "linear motion", ["circular motion", "periodic motion", "random motion"], "e.g. a car on a straight road"),
 M4("An object covering equal distances in equal intervals of time has:", "uniform motion", ["non-uniform motion", "zero speed", "variable speed"], "constant speed"),
 M4("An object covering unequal distances in equal intervals has:", "non-uniform motion", ["uniform motion", "no motion", "zero speed"], "changing speed"),
 M4("The device used to measure speed in a vehicle is the:", "speedometer", ["odometer", "thermometer", "barometer"], "shows km/h"),
 M4("The device that measures the distance travelled by a vehicle is the:", "odometer", ["speedometer", "stopwatch", "compass"], "total distance"),
 M4("Which is the fastest?", "20 m/s", ["60 km/h", "10 m/s", "50 km/h"], "20 m/s = 72 km/h"),
 M4("The time period of a pendulum is 2 s. It completes ___ oscillations in 20 s.", "10", ["20", "40", "5"], "20 ÷ 2"),
 M4("A pendulum takes 30 s for 20 oscillations. Its time period is:", "1.5 s", ["0.67 s", "15 s", "600 s"], "30 ÷ 20"),
 M4("Which of these is the smallest time interval we can measure with a stopwatch?", "a fraction of a second", ["a day", "an hour", "a year"], "digital stopwatch"),
 M4("Which ancient Indian text deals with astronomy and the measurement of time?", "Surya Siddhanta", ["Arthashastra", "Panchatantra", "Gita"], "classical Sanskrit text"),
 M4("A distance–time graph of an object at rest is:", "a horizontal line", ["a rising line", "a falling line", "a curve"], "distance does not change"),
 M4("A distance–time graph of uniform motion is:", "a straight sloping line", ["a horizontal line", "a vertical line", "a zigzag"], "constant speed"),
]
A = A[:40]
B = [
 Q("Define time period of a pendulum.", "Time taken for one complete oscillation (2).", "2"),
 Q("What is the SI unit of time and speed?", "Second (1); metre per second (1).", "1+1"),
 Q("Define speed. Write its formula.", "Distance travelled per unit time (1); speed = distance ÷ time (1).", "1+1"),
 Q("Differentiate between uniform and non-uniform motion.", "Equal distances in equal times; unequal distances in equal times (1+1).", "1+1"),
 Q("What is a sundial? Why cannot it work at night?", "Instrument using Sun's shadow to tell time (1); needs sunlight (1).", "1+1"),
 Q("A car covers 150 km in 3 hours. Find its speed.", "150 ÷ 3 = 50 km/h (2).", "2"),
 Q("Convert 72 km/h to m/s.", "72 × 5/18 = 20 m/s (2).", "2"),
 Q("What is a clepsydra?", "An ancient water clock (2).", "2"),
 Q("A pendulum completes 20 oscillations in 40 s. Find its time period.", "2 s (2).", "2"),
 Q("Which is faster: 54 km/h or 20 m/s?", "54 km/h = 15 m/s so 20 m/s is faster (2).", "2"),
 Q("What does an odometer measure?", "The total distance travelled by a vehicle (2).", "2"),
 Q("Name two ancient ways of measuring time.", "Sundial; water clock (2).", "2"),
 Q("State the relation between distance, speed and time.", "Distance = speed × time (2).", "2"),
 Q("Why is it better to use a pendulum or quartz clock than a sundial?", "Works at all times (2).", "2"),
 Q("What is linear motion? Give an example.", "Motion along a straight line (1); a train on a straight track (1).", "1+1"),
 Q("Express 5 hours 30 minutes in minutes.", "330 minutes (2).", "2"),
]
C = [
 Q("A train covers 300 km in 5 hours. Find its speed in km/h and m/s.", "60 km/h (1.5); 16.67 m/s (1.5).", "1½+1½"),
 Q("How long will a bus take to cover 210 km at 42 km/h?", "5 hours (3).", "3"),
 Q("Describe an activity to find the time period of a simple pendulum.", "Hang a bob and swing small angle (1); time 20 oscillations with a stopwatch (1); divide to get time period (1).", "1+1+1"),
 Q("Explain how a sundial works.", "A gnomon casts a shadow (1.5); shadow position indicates time (1.5).", "1½+1½"),
 Q("A man walks at 5 km/h for 2 hours and cycles at 15 km/h for 1 hour. Find the total distance and average speed.", "25 km (1.5); 25/3 = 8.33 km/h (1.5).", "1½+1½"),
 Q("The distance–time data: 0 s 0 m, 2 s 10 m, 4 s 20 m, 6 s 30 m. Is the motion uniform? Find speed.", "Equal distance in equal time (1.5); 5 m/s (1.5).", "1½+1½"),
 Q("Distinguish between speed and distance.", "Distance is how far; speed is how fast (1.5); units m and m/s (1.5).", "1½+1½"),
 Q("A pendulum has a time period of 1.5 s. How many oscillations in 1 minute?", "40 (3).", "3"),
 Q("State two limitations of a sundial and how a clock overcomes them.", "Needs Sun, location specific (1.5); clock works any time (1.5).", "1½+1½"),
 Q("Why are standard units needed for measurement of time?", "To give the same result everywhere (3).", "3"),
 Q("Convert 90 km/h into m/s and 8 m/s into km/h.", "25 m/s (1.5); 28.8 km/h (1.5).", "1½+1½"),
 Q("An athlete runs 400 m in 50 s. Find the speed in m/s and km/h.", "8 m/s (1.5); 28.8 km/h (1.5).", "1½+1½"),
 Q("Explain the working of a pendulum clock.", "Pendulum oscillates with fixed period (1.5); gears count the oscillations (1.5).", "1½+1½"),
 Q("A bicycle travels 6 km in 20 minutes. Find its speed in km/h.", "18 km/h (3).", "3"),
 Q("A boy runs the first 100 m in 20 s and next 100 m in 30 s. Find the average speed.", "200/50 = 4 m/s (3).", "3"),
 Q("Why is average speed used for non-uniform motion?", "Speed changes so we use total distance ÷ total time (3).", "3"),
 Q("What is the use of a stopwatch? Name a game where it is used.", "Measures short intervals (1.5); athletics (1.5).", "1½+1½"),
 Q("Describe the working of a water clock.", "Water drips at a steady rate (1.5); marks show the time (1.5).", "1½+1½"),
 Q("Explain the idea of oscillation using a swing.", "Moves to and fro with regular time (3).", "3"),
 Q("An aeroplane flies at 900 km/h. How far in 20 minutes?", "300 km (3).", "3"),
 Q("A train of length 200 m crosses a pole in 10 s. Find its speed.", "20 m/s (3).", "3"),
 Q("Which is faster: 36 km/h or 11 m/s? Show.", "36 km/h = 10 m/s so 11 m/s is faster (3).", "3"),
 Q("State the use of speedometer and odometer.", "Speed and distance reading (3).", "3"),
 Q("Plot the idea of a distance–time graph for a car at rest and for a car moving uniformly (describe).", "Horizontal line for rest (1.5); sloping line for uniform motion (1.5).", "1½+1½"),
]
D = [
 Q("(i) Define speed and give its SI unit. (ii) A car travels 180 km in 3 hours. Find its speed. (iii) Express it in m/s.", "(i) Distance/time; m/s (1). (ii) 60 km/h (2). (iii) 16.67 m/s (2).", "1+2+2"),
 Q("<b>Case study:</b> Ravi times a pendulum: 20 oscillations take 36 s. (i) Find time period. (ii) How many oscillations in 1 min? (iii) What if the string is longer? (iv) Why count 20 oscillations?", "(i) 1.8 s (1). (ii) 33 (1). (iii) Time period increases (1). (iv) Reduces error (2).", "1+1+1+2"),
 Q("(i) Describe the working of a sundial and clepsydra. (ii) State advantages and limitations of each.", "(i) Sun shadow; water flow (3). (ii) Sundial needs sun; clepsydra needs refilling (2).", "3+2"),
 Q("<b>Case study:</b> A bus covers 60 km in the first hour, 40 km in the second hour and 80 km in the third. (i) Total distance. (ii) Total time. (iii) Average speed. (iv) Is the motion uniform?", "(i) 180 km (1). (ii) 3 h (1). (iii) 60 km/h (1). (iv) No, unequal distances (2).", "1+1+1+2"),
 Q("(i) Distinguish between uniform and non-uniform motion with examples. (ii) Draw distance–time graph shapes (describe). (iii) Why is average speed needed?", "(i) Definitions and examples (2). (ii) Straight line; curve (2). (iii) For varying speeds (1).", "2+2+1"),
 Q("(i) Convert 108 km/h and 25 m/s. (ii) Which is faster? (iii) How far in 10 s at the faster speed?", "(i) 30 m/s; 90 km/h (2). (ii) 108 km/h (1). (iii) 300 m (2).", "2+1+2"),
 Q("<b>Case study:</b> A runner covers 100 m in 12.5 s. (i) Find speed in m/s. (ii) Convert to km/h. (iii) Time for 400 m at same speed. (iv) Which instrument measures it?", "(i) 8 m/s (1). (ii) 28.8 km/h (1). (iii) 50 s (1). (iv) Stopwatch (2).", "1+1+1+2"),
 Q("(i) What are the units of time used earlier in India? (ii) How were they measured? (iii) Why standardise?", "(i) Pahar, ghati (1). (ii) Sundial, water clock (2). (iii) Common reference (2).", "1+2+2"),
 Q("(i) Write the relation among speed, distance and time. (ii) A train takes 4 h to go 320 km. Find speed. (iii) How long to cover 480 km?", "(i) s = d/t (1). (ii) 80 km/h (2). (iii) 6 h (2).", "1+2+2"),
 Q("<b>Case study:</b> A distance–time table: 0 s 0 m; 10 s 50 m; 20 s 100 m; 30 s 160 m. (i) Is it uniform? (ii) Speed for first 20 s. (iii) Speed for last 10 s. (iv) Overall average speed.", "(i) No (1). (ii) 5 m/s (1). (iii) 6 m/s (1). (iv) 5.33 m/s (2).", "1+1+1+2"),
 Q("(i) Explain simple pendulum. (ii) What factors affect its time period? (iii) How is it used?", "(i) Bob on a thread (1). (ii) Length (2). (iii) Clocks (2).", "1+2+2"),
 Q("(i) What is motion? (ii) Types of motion with examples. (iii) How is speed measured in vehicles?", "(i) Change of position (1). (ii) Linear, circular, periodic (2). (iii) Speedometer (2).", "1+2+2"),
 Q("<b>Case study:</b> Two cars start together. Car A moves at 72 km/h; Car B at 15 m/s. (i) Whose speed is greater? (ii) Distance covered in 1 h by each. (iii) Who is ahead after 1 h? (iv) By how much?", "(i) A (1). (ii) 72 km and 54 km (2). (iii) A (1). (iv) 18 km (1).", "1+2+1+1"),
 Q("(i) How do astronomers measure time? (ii) How is the day defined? (iii) Why is the year 365 days?", "(i) Using Earth’s rotation and revolution (2). (ii) One rotation (1). (iii) One revolution around the Sun (2).", "2+1+2"),
 Q("(i) State two uses of knowing speed in daily life. (ii) Give a numerical example. (iii) Explain why units matter.", "(i) Travel planning, sports (2). (ii) Example computation (2). (iii) Consistency (1).", "2+2+1"),
 Q("(i) Draw (describe) a distance–time graph for a bus stopping at a station. (ii) Explain each part.", "(i) Rising, flat, rising (3). (ii) Motion, rest, motion (2).", "3+2"),
]
SETS, POOL = build(A, B, C, D)
