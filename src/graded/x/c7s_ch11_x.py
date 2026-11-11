"""Class 7 Science Ch 11 Earth, Moon and the Sun - extras."""
from common import AR4, Q

AR = [
 AR4("Day and night occur because of the rotation of the Earth.", "The Earth rotates on its axis once in about 24 hours.", "a",
     "Rotation turns each part of the Earth to and away from the Sun every 24 hours."),
 AR4("The seasons are caused by the changing distance of the Earth from the Sun.", "The axis of the Earth is tilted.", "d",
     "Seasons are due to the tilt of the axis and revolution, not distance, so A is false; R is true."),
 AR4("The Moon is a natural satellite of the Earth.", "The Moon does not produce its own light.", "b",
     "Both are true but unrelated: being a satellite is not the reason it has no light of its own."),
 AR4("A lunar eclipse occurs on a full moon day.", "During a lunar eclipse, the Earth comes between the Sun and the Moon.", "a",
     "Earth's shadow falls on the Moon only when the Earth is between the Sun and the Moon, which happens at full moon."),
 AR4("A solar eclipse occurs on a new moon day.", "During a solar eclipse, the Earth comes between the Sun and the Moon.", "c",
     "A is true; in a solar eclipse the Moon comes between the Sun and the Earth, so R is false."),
 AR4("A leap year has 366 days.", "The Earth takes about $365\\tfrac14$ days to go around the Sun, so the extra quarter days add up to one day in four years.", "a",
     "The extra days are added as 29 February every fourth year."),
]

CASE = [
 Q("<b>Case study.</b> Prakash lives in Delhi. He notices that in June the days are very long and hot, while in December the days are short and cold. His cousin in Sydney, Australia, says that it is cold there in June. "
   "(i) Name the main causes of seasons. (ii) What season is it in Delhi in June? (iii) On about which dates are day and night nearly equal? (iv) Why is it winter in Sydney when it is summer in Delhi?",
   "(i) The tilt of the Earth's axis and its revolution around the Sun (1). (ii) Summer (1). (iii) About 21 March and 23 September (equinoxes) (1). (iv) Sydney is in the southern hemisphere (1), which is tilted away from the Sun in June, so it gets less direct sunlight and a shorter day (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Riya watches the Moon for a month from her balcony in Bhopal. On one night she cannot see it at all, about two weeks later it appears as a full bright circle, and a week after that it looks like a half circle. "
   "(i) What is the phase when the Moon is not visible? (ii) What is the phase when the whole face is seen? (iii) After about how many days does the same phase repeat? (iv) Why does the Moon seem to change its shape?",
   "(i) New moon (1). (ii) Full moon (1). (iii) About 29 to 30 days (1). (iv) The Moon revolves around the Earth, so we see different amounts of its sunlit half (1); the Moon does not change its shape and shines only by reflected sunlight (1).", "1+1+1+2"),
 Q("<b>Case study.</b> During a solar eclipse, Rani's school arranges safe viewing with special filters. A week later, a lunar eclipse is seen and Rani notices that the Moon appears dark red. "
   "(i) Which body lies between the other two during a solar eclipse? (ii) On which Moon-day does a solar eclipse occur? (iii) Why should we never look at the Sun directly during an eclipse? (iv) During a lunar eclipse, whose shadow falls on which body, and on which Moon-day does it occur?",
   "(i) The Moon lies between the Sun and the Earth (1). (ii) New moon day (1). (iii) It can damage the eyes (1). (iv) The Earth's shadow falls on the Moon (1); it occurs on a full moon day (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Rotation and revolution of the Earth", [
   "Rotation: spinning of the Earth on its axis from west to east once in about 24 hours; causes day and night.",
   "Revolution: motion of the Earth around the Sun in about $365\\tfrac14$ days (one year).",
   "Leap year: 366 days; 29 February is added every 4 years to account for the extra quarter day."]),
 ("Seasons", [
   "The Earth's axis is tilted by about $23.5^\\circ$; seasons are caused by this tilt and the revolution, not by the Earth's distance from the Sun.",
   "Around 21 June: longest day in the northern hemisphere; around 22 December: shortest day.",
   "Equinoxes (about 21 March and 23 September): day and night are nearly equal everywhere.",
   "When it is summer in the northern hemisphere, it is winter in the southern hemisphere."]),
 ("The Moon and its phases", [
   "The Moon is the natural satellite of the Earth; it shines by reflecting sunlight and takes about 27 days to revolve around the Earth.",
   "Phases: new moon (not visible), crescent, half moon, gibbous, full moon; the cycle repeats in about 29 to 30 days.",
   "Waxing: the bright part increases; waning: the bright part decreases."]),
 ("Eclipses", [
   "Solar eclipse: the Moon comes between the Sun and the Earth; occurs on a new moon day.",
   "Lunar eclipse: the Earth comes between the Sun and the Moon; occurs on a full moon day.",
   "Never look at the Sun directly or through a telescope during a solar eclipse; use proper filters."]),
]

MISTAKES = [
 "Saying that seasons are caused by the Earth being closer to or farther from the Sun; they are caused by the <b>tilt of the axis</b> and revolution.",
 "Mixing up rotation (day and night, 24 hours) with revolution (year, $365\\tfrac14$ days).",
 "Interchanging eclipses: <b>solar</b> eclipse = Moon between Sun and Earth (new moon); <b>lunar</b> eclipse = Earth between Sun and Moon (full moon).",
 "Writing that the Moon gives its own light; it only <b>reflects</b> sunlight.",
 "Thinking the phases of the Moon are caused by the Earth's shadow; they are due to how much of the sunlit half we see.",
 "Writing that it is summer in both hemispheres at the same time; the seasons are <b>opposite</b> in the two hemispheres.",
]
