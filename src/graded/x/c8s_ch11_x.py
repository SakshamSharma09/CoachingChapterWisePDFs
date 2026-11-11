"""Class 8 Science Ch 11 Keeping Time with the Skies - extras."""
from common import AR4, Q

AR = [
 AR4("The shadow of a vertical stick is shortest around noon.", "At noon the Sun is highest in the sky.", "a", "A higher Sun casts a shorter shadow."),
 AR4("We always see the same side of the Moon from the Earth.", "The Moon takes the same time to rotate once on its axis as to revolve once around the Earth.", "a", "Equal rotation and revolution periods keep one face towards us."),
 AR4("A solar eclipse can occur only on a new moon day.", "At new moon the Moon lies between the Sun and the Earth.", "a", "Only then can the Moon block sunlight from reaching the Earth."),
 AR4("The Pole Star appears almost fixed in the sky.", "The Earth revolves around the Sun once a year.", "b", "Both are true, but the Pole Star seems fixed because it lies near the line of the Earth's axis, not because of revolution."),
 AR4("A leap year has 365 days.", "The Earth takes about 365 and a quarter days to go around the Sun.", "d", "A is false (a leap year has 366 days); R is true."),
 AR4("Seasons are caused by the tilt of the Earth's axis.", "The distance of the Earth from the Sun changes greatly through the year, making it hotter when closer.", "c", "A is true; R is false, the distance changes only slightly and is not the cause of seasons."),
]

CASE = [
 Q("<b>Case study.</b> Kavya fixes a vertical stick in the playground of her school in Nagpur and marks the tip of its shadow every hour from 8 a.m. to 4 p.m. She finds that the shadow is longest in the morning and evening and shortest around midday. "
   "(i) In which direction does the shadow point in the morning? (ii) At what time of day is the shadow shortest? (iii) Name the device that works on this principle. (iv) Explain why the shadow length changes during the day.",
   "(i) West (1). (ii) Around noon (1). (iii) Sundial (1). (iv) The Earth rotates, so the Sun appears to move across the sky; when the Sun is low the shadow is long, and when it is highest at noon the shadow is shortest (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A new moon (Amavasya) was observed on 1 November. Hari records that the Moon grows bigger every night and appears as a full disc about two weeks later. The Moon again becomes invisible after about 29.5 days from the first new moon. "
   "(i) What is this phase on 1 November called? (ii) After about how many days is the next full moon? (iii) After about how many days does the next new moon come? (iv) Why does the Moon show different phases?",
   "(i) New moon (1). (ii) About 14 to 15 days (1). (iii) About 29.5 days (1). (iv) Half of the Moon is always lit by the Sun, but as the Moon moves around the Earth we see different amounts of the lit half (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A calendar year has 365 days, but the Earth takes about 365 and a quarter days to go around the Sun. To correct the difference, an extra day is added to February once in four years. A lunar year of 12 months of about 29.5 days each is shorter than a solar year. "
   "(i) What is a year with an extra day called? (ii) How many days does it have? (iii) 2024 was such a year; which is the next? (iv) Calculate the length of 12 lunar months and its difference from 365 days.",
   "(i) Leap year (1). (ii) 366 days (1). (iii) 2028 (1). (iv) 12 x 29.5 = 354 days (1); the difference is 365 - 354 = 11 days (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Earth's motions", ["Rotation on its axis: about 24 hours (gives day and night, apparent motion of Sun and stars).", "Revolution around the Sun: about $365\\frac{1}{4}$ days (one year; with the tilt of the axis it gives seasons).",
   "Four extra quarters make 1 day, so a leap year of 366 days comes every 4 years."]),
 ("Shadows and sundial", ["Shadow is longest at sunrise and sunset, shortest at noon.", "Morning shadow points west; evening shadow points east.", "A sundial (gnomon) tells time from the Sun's apparent motion."]),
 ("Moon", ["Moon revolves around the Earth in about 27 days; new moon to new moon is about 29.5 days.", "Phases: new moon, crescent, first quarter, gibbous, full moon, and back.",
   "Same side of the Moon always faces the Earth. Solar eclipse: new moon; lunar eclipse: full moon."]),
 ("Calendars and stars", ["Solar calendar follows the Sun; lunar calendar follows the Moon phases ($12 \\times 29.5 = 354$ days).", "Lunar festivals fall on different dates of the solar calendar each year.",
   "Pole Star lies almost above the North Pole and appears fixed; other stars seem to circle it."]),
]

MISTAKES = [
 "Saying day and night are caused by the Earth's revolution; they are caused by rotation.",
 "Saying seasons come from the Earth's distance from the Sun; the cause is the tilt of its axis.",
 "Thinking the Moon disappears at new moon; it is still there, but the lit half faces away from us.",
 "Mixing up the eclipses: a solar eclipse is on a new moon day, a lunar eclipse on a full moon day.",
 "Writing a leap year as 365 or 367 days; it has 366 days with 29 February.",
 "Giving the shadow direction wrongly; the morning shadow falls to the west, the evening shadow to the east.",
]
