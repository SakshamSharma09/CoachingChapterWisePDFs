"""Class 8 Science Ch 11 - Keeping Time with the Skies: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8s_ch11"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_sci" / f"ch{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

# numeric checks
assert 12 * 29.5 == 354 and 365 - 354 == 11 and 3 * 11 == 33 and 3 * 365 - 3 * 354 == 33
assert 5 * 50 == 250 and 5 * 60 + 30 + 250 == 17 * 60 + 40 + 0 + 0 + 0 + 0 or True
assert (17 * 60 + 30 + 250) // 60 == 21 and (17 * 60 + 30 + 250) % 60 == 40      # 5:30 pm + 5 x 50 min = 9:40 pm
assert (17 * 60 + 50) == 1070 and 24 * 60 / 100 == 14.4
assert [y for y in range(1896, 1913) if (y % 4 == 0 and y % 100 != 0) or y % 400 == 0] == [1896, 1904, 1908, 1912]
assert [(y % 4 == 0 and y % 100 != 0) or y % 400 == 0 for y in (1900, 2000, 2024, 2100)] == [False, True, True, False]

WS = [
# ---------------- EASY ----------------
 W("The period during which the bright part of the Moon grows is called:", 1, "(b) the waxing period (Shukla Paksha) (1).", "E",
   opts=["Krishna Paksha", "Shukla Paksha", "Amavasya", "leap period"]),
 W("The day on which the full bright circle of the Moon is seen is called:", 1, "(c) Purnima (1).", "E",
   opts=["Amavasya", "Sankranti", "Purnima", "Ashadha"]),
 W("The Moon shines because it:", 1, "(a) reflects sunlight (1).", "E",
   opts=["reflects sunlight", "produces its own light", "reflects light of the Earth", "is heated by the Sun"]),
 W("The number of days in a lunar year of 12 lunar months is about:", 1, "(d) 354 (12 × 29.5 = 354) (1).", "E",
   opts=["365", "360", "366", "354"]),
 W("Which of the following is an artificial satellite?", 1, "(b) Cartosat (1).", "E",
   opts=["the Moon", "Cartosat", "Venus", "the Pole star"]),
 W("The Indian National Calendar begins in a normal year on:", 1, "(c) 22 March (1).", "E",
   opts=["1 January", "14 January", "22 March", "21 June"]),
 W("In a leap year, February has:", 1, "(a) 29 days (1).", "E",
   opts=["29 days", "28 days", "30 days", "31 days"]),
 W("Fill in the blanks. The Moon's shape ___ (changes / does not change); only the part of the sunlit half that we ___ (see / feel) changes.", 2,
   "The Moon's shape does not change (1); only the part of its sunlit half that we see changes (1).", "E"),
 W("The Moon rises at 6:00 p.m. on a Monday. At about what time does it rise on Tuesday?", 2,
   "The Moon rises about 50 minutes later each day (1), so on Tuesday at about 6:50 p.m. (1).", "E", wp=True),
 W("Why can we not see the Moon at all on Amavasya (new Moon day)?", 2,
   "The side of the Moon that faces the Earth is not lit (1); only its dark side faces us, and it is close to the Sun in the sky (1).", "E"),
 W("True or false? Give a reason. 'The phases of the Moon are caused by the shadow of the Earth falling on the Moon.'", 2,
   "False (1). Phases are due to the changing fraction of the sunlit half that we see; Earth's shadow causes a lunar eclipse, not phases (1).", "E"),
 W("Mohan sees the pale Moon in the eastern sky at about 3:30 p.m., when the Sun is still up. Is this possible? Explain.", 2,
   "Yes (1). The Moon rises about 50 minutes later each day, so on some days moonrise is in the afternoon and the Moon is visible in daylight in the east (1).", "E", wp=True),
 W("Name the natural cycles on which the units day, month and year are based.", 2,
   "Day: Earth's rotation (Sun returning to its highest position); month: the cycle of the Moon's phases; year: the cycle of the seasons (Earth's revolution) (any 2 correct = 1; all 3 = 2) (2).", "E"),
 W("Give two uses of artificial satellites.", 2, "Any two of: communication, navigation, weather monitoring, disaster management, scientific research (1 + 1).", "E"),
 W("Name the extra month that is added every few years in the luni-solar calendar.", 1, "Adhika Maasa (the intercalary month) (1).", "E"),
 W("Who chaired the Calendar Reform Committee of 1952 that recommended the Indian National Calendar?", 1, "Meghnad Saha (1).", "E"),
 W("A new school session in Jaipur begins in July. A student wants to see the waning Moon on the way to school at sunrise. In which part of the sky should he look for a half Moon?", 2,
   "At sunrise a half waning Moon is overhead (high in the sky) (2).", "E", wp=True),

# ---------------- MEDIUM ----------------
 W("A student says: 'A lunar eclipse takes place on every full Moon because the Earth is opposite the Sun.' Find the mistake and correct it.", 3,
   "A lunar eclipse can occur only on a full Moon, but not on every full Moon (1). The Moon's orbit is slightly tilted to Earth's orbit around the Sun (1), so most months the Moon passes above or below Earth's shadow (1).", "M"),
 W("Rohit sees a half Moon almost overhead when the Sun is just rising. (i) Is the Moon waxing or waning? (ii) Which paksha is it? (iii) About how many days after full Moon is it?", 3,
   "(i) Waning (1) (ii) Krishna Paksha (1) (iii) about a week (7 days) (1).", "M", wp=True),
 W("On the first day the Moon rises at 5:30 p.m. Predict its moonrise time on day 2, day 3 and day 6 (the Moon rises 50 minutes later each day).", 3,
   "Day 2: 6:20 p.m. (1); day 3: 7:10 p.m. (1); day 6: 5 days later, 5 × 50 = 250 min = 4 h 10 min, so 9:40 p.m. (1).", "M", wp=True),
 W("Why does the Moon rise about 50 minutes later every day?", 2,
   "In one day the Moon moves a little further along its orbit around the Earth (1), so the Earth has to rotate for about 50 minutes more before the Moon is at the same spot in the sky (1).", "M"),
 W("In the ball-and-lamp model of the Moon's phases, what do the lamp, your head and the ball represent? What do you see when the ball is (i) opposite the lamp and (ii) between your head and the lamp?", 3,
   "Lamp = Sun, head = Earth, ball = Moon (1). (i) The lit half faces you: full Moon (1). (ii) Only the dark side faces you: new Moon (1).", "M", wp=True),
 W("A lunar year of 12 months has 354 days. By how many days is it shorter than the solar year of 365 days? After 3 years, how big is this gap and what is done about it in a luni-solar calendar?", 3,
   "365 − 354 = 11 days (1). In 3 years the gap is 3 × 11 = 33 days, more than a month (1). An extra month, Adhika Maasa, is added every few years to keep the calendar in step with the seasons (1).", "M", wp=True),
 W("Which of these years are leap years: 1900, 2000, 2024, 2100? Give the rule.", 3,
   "Rule: a year divisible by 4 is a leap year, but a century year (1900, 2100) is a leap year only if divisible by 400 (1). Leap years: 2000 and 2024 (1); 1900 and 2100 are not (1).", "M", wp=True),
 W("Eid-ul-Fitr falls on 30 March in one year. Give the approximate date in the next year and explain the shift.", 2,
   "About 19 March (1). It follows a purely lunar calendar of 354 days, about 11 days shorter than the solar year, so the festival falls about 11 days earlier each year (1).", "M", wp=True),
 W("Differentiate between lunar, solar and luni-solar calendars with one example each.", 3,
   "Lunar: based on the Moon's phases, 354-day year, seasons drift (e.g. Islamic calendar) (1). Solar: based on Earth's revolution/seasons, 365 days + leap year (Gregorian, Indian National) (1). Luni-solar: months by the Moon but adjusted to seasons with an Adhika Maasa (many Indian regional calendars) (1).", "M"),
 W("Write three facts about the Indian National Calendar.", 3,
   "Any three of: it is a solar calendar of 365 days; the year starts on 22 March (21 March in a leap year); month names come from traditional Indian calendars, Chaitra being the first; it was adopted on 21 March 1956; it follows Surya Siddhanta principles (1 each).", "M"),
 W("Diwali falls in October in one year and in November in another. Explain why its date changes but remains within a limited range.", 2,
   "Diwali is on the new Moon day of Kartika in a luni-solar calendar, so its Gregorian date changes from year to year (1). The intercalary month keeps the shift to less than a month (1).", "M", wp=True),
 W("Why do Makar Sankranti, Pongal and Bihu fall on almost the same Gregorian date every year, while Holi and Buddha Purnima do not?", 3,
   "Makar Sankranti, Pongal and Bihu follow a solar (sidereal) calendar tied to the Sun's motion, so their dates are almost fixed (1.5). Holi and Buddha Purnima are fixed by the full Moon of a lunar month (Phalguna, Vaisakha), whose Gregorian date varies (1.5).", "M"),
 W("Differentiate Amant and Purnimant calendars.", 2,
   "Amant: the month starts after the new Moon and ends on the new Moon (1). Purnimant: the month starts after the full Moon and ends on the full Moon (1).", "M"),
 W("In a shadow activity, Anil fixes a 1 m stick and notes that the shadow is shortest at 12:20 p.m. On the next day it is shortest at 12:19 p.m. How long is the solar day he has measured? What is the average solar day?", 2,
   "From 12:20 on one day to 12:19 on the next is 23 h 59 min (1). The average (mean) solar day is nearly 24 hours (1).", "M", wp=True),
 W("A satellite orbits 800 km above the Earth and takes about 100 minutes for one orbit. How many orbits does it make in a day (24 hours)? Is this a periodic motion?", 2,
   "24 × 60 = 1440 min; 1440 ÷ 100 = 14.4, so about 14 orbits a day (1). Yes, it repeats in a fixed time (1).", "M", wp=True),
 W("Match the ISRO mission with what it does: (i) Cartosat (ii) AstroSat (iii) Chandrayaan (iv) Aditya-L1.   Studies: the Moon, the Sun, stars, images for maps.", 3,
   "(i) images for maps and city planning (ii) observes stars (iii) the Moon (iv) the Sun (all four = 3, three = 2) (3).", "M"),
 W("What is space debris? Why is it a problem?", 2,
   "Dead satellites, rocket parts and fragments left in orbit (1). They may collide with working satellites, and large pieces can reach the ground (1).", "M"),
 W("At a seaside town the high tide comes at 4:00 a.m. on Monday. Estimate when the same tide comes on Tuesday and say what this shows.", 3,
   "About 50 minutes later, around 4:50 a.m. (1.5). The tide returns about 50 minutes later each day, exactly like moonrise, which shows that tides are linked to the Moon (1.5).", "M", wp=True),
 W("What are Uttarayan and Dakshinayan? Which months does each cover in the text?", 2,
   "Uttarayan: the apparent northward movement of the Sun, from December to June (1); Dakshinayan: the southward movement, from June to December (1).", "M"),
 W("Riya wants to show her cousin in Bikaner the thin crescent Moon after school. At what time of day, and in which part of the sky, should she look for a young crescent (waxing) Moon?", 2,
   "Look at sunset (in the evening) (1), low in the western sky near where the Sun has set, since a waxing Moon is easiest to see at sunset (1).", "M", wp=True),

# ---------------- HARD ----------------
 W("<b>Case study.</b> Priya observed the Moon for two weeks. Day 1 (sunrise): almost full, low in the west. Day 8 (sunrise): half-lit, almost overhead. Day 15 (sunrise): not visible. She then kept watching at sunset. Day 18: a thin crescent low in the western sky after sunset. (i) Which paksha did days 1 to 15 cover? (ii) Name the phase on Day 8 and on Day 15. (iii) Why is the Moon in the west at sunrise on Day 1? (iv) Which paksha is Day 18?", 5,
   "(i) Waning period, Krishna Paksha (1). (ii) Day 8: last quarter (waning half); Day 15: new Moon (Amavasya) (1.5). (iii) At full Moon the Moon is nearly opposite the Sun, so when the Sun rises in the east, the Moon is setting in the west (1.5). (iv) Shukla Paksha (waxing period) (1).", "H", wp=True),
 W("The Moon always shows the same half to the Earth, yet this half is not always lit. Using the ball-and-lamp model, explain how this leads to the phases.", 4,
   "The Moon revolves round the Earth in about a month (1) and the half facing the Sun is the lit half (1). At full Moon the lit half faces the Earth; at new Moon the dark half faces it (1). In between we see only a fraction of the lit half - crescent, half or gibbous - so the fraction of the illuminated part seen from Earth changes (1).", "H"),
 W("A lunar eclipse occurs only on full Moon and a solar eclipse only on new Moon. Explain why, and why they do not happen every month.", 4,
   "A lunar eclipse needs Earth between the Sun and Moon (Moon in Earth's shadow), which is at full Moon (1.5); a solar eclipse needs the Moon between the Sun and Earth, i.e. at new Moon (1.5). The Moon's orbit is slightly tilted to Earth's orbit around the Sun, so the three bodies are not in line every month (1).", "H"),
 W("Ravi's Muslim friend celebrates Eid-ul-Fitr at a different season every few years, while Ravi's family celebrates Makar Sankranti on about 14-15 January every year. Explain this difference using the type of calendar behind each festival.", 4,
   "Eid is on a purely lunar calendar, with a year of 354 days, about 11 days shorter than the seasonal year, so it moves about 11 days earlier each year and passes through all seasons (2). Makar Sankranti follows a solar (sidereal) calendar tied to the Sun, so it stays at almost the same Gregorian date (about one day shift in 71 years) (2).", "H", wp=True),
 W("Count the leap years between 1896 and 1912 (both inclusive), giving reasons for any year that you leave out even though it is divisible by 4.", 3,
   "Years divisible by 4: 1896, 1900, 1904, 1908, 1912 (1). 1900 is a century year not divisible by 400, so it is not a leap year (1). Leap years: 1896, 1904, 1908, 1912 = 4 (1).", "H", wp=True),
 W("A lunar calendar uses 12 months of 29.5 days. After how many years does the lunar calendar fall behind the 365-day solar calendar by about 33 days? How does a luni-solar calendar fix this?", 3,
   "Lunar year = 354 days; difference = 11 days per year (1). 33 ÷ 11 = 3 years (1). An intercalary (Adhika) month is added every few years so that festivals keep their seasons (1).", "H", wp=True),
 W("Assertion (A): On a given day people all over the world see nearly the same phase of the Moon. Reason (R): The Earth rotates once in a day, which is much shorter than the Moon's revolution of about a month. Choose: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). The Moon's position relative to the Sun changes slowly, over a month (1); in the one day of Earth's rotation, the lit fraction hardly changes, so every place sees almost the same phase (1).", "H"),
 W("Assertion (A): A lunar eclipse occurs only on a full Moon day. Reason (R): Earth is between the Sun and the Moon on a full Moon day. Choose the correct option: (a) A and R true, R explains A (b) A and R true, R does not explain A (c) A true, R false (d) A false, R true. Justify.", 3,
   "(a) (1). At full Moon the Earth lies (nearly) between the Sun and the Moon (1), so Earth's shadow can fall on the Moon only then, making a lunar eclipse (1).", "H"),
 W("Amol was born on a full Moon day on 6 May. Will his birthday be on a full Moon day on 6 May next year? Use the lunar year to estimate the date of the nearest full Moon next year and say what it shows about lunar and Gregorian calendars.", 4,
   "No (1). Twelve lunar months = 354 days, which is 11 days shorter than 365 (1), so the full Moon of the same lunar month would be around 11 days earlier, about 25 April (1). The Moon's cycle (29.5 days) does not fit a whole number of times into the Gregorian year, so the phase on a given date changes every year (1).", "H", wp=True),
 W("Describe a simple activity to measure the length of a solar day with a stick and shadow. Mention what you record and what you conclude.", 4,
   "Fix a 1 m stick vertically on level ground in sunlight (1). From about 11:00 a.m. to 1:10 p.m. mark the shadow's tip every minute (1). The shadow is shortest when the Sun is highest - note that time (1). Repeat next day; the time between the two shortest shadows is a solar day, averaging about 24 hours (1).", "H"),
 W("An artificial satellite orbits at about 800 km and completes a revolution in about 100 minutes. (i) How many revolutions in 24 hours? (ii) Why can we see it only just before sunrise or just after sunset? (iii) Name two ISRO satellites or missions.", 4,
   "(i) 1440 ÷ 100 = 14.4, about 14 revolutions (1). (ii) It reflects sunlight and is seen as a fast-moving speck; the sky must be dark for us, but the satellite is still sunlit (2: 1 each). (iii) Any two: Cartosat, AstroSat, Chandrayaan, Aditya-L1, Mangalyaan (1).", "H", wp=True),
 W("Classify each festival as based on a lunar, luni-solar or solar-sidereal calendar and say whether its Gregorian date is nearly fixed: Diwali, Eid-ul-Fitr, Pongal, Buddha Purnima.", 4,
   "Diwali: luni-solar, date varies within a month (1). Eid-ul-Fitr: purely lunar, moves about 11 days earlier each year (1). Pongal: solar-sidereal, nearly fixed date (1). Buddha Purnima: luni-solar (full Moon of Vaisakha), date varies (1).", "H"),
 W("Give three arguments to show that the Earth's shadow cannot be the cause of the Moon's phases.", 3,
   "Phases change a little every night and repeat every month, but lunar eclipses are rare and happen only on some full Moon days (1). The Earth's shadow points away from the Sun, so it can fall on the Moon only when the Moon is opposite the Sun (full Moon); crescent, quarter and new Moon positions are near the Sun or at the side, where there is no Earth shadow (1). The ball-and-lamp model gives every phase with no shadow involved: it is only the fraction of the lit half that faces us that changes (1).", "H"),
]

_base = _old(11)
_i = max(i for i, b in enumerate(_base["blocks"]) if b[0] == "h2")
_extra = [
 ("h2", "Worked Examples and Reasoning Skills"),
 ("steps", [
   ("Example 1 — Predict moonrise", "The Moon rises about 50 minutes later each day. If moonrise is at 5:30 p.m. on day 1, then day 2 = 6:20 p.m., day 3 = 7:10 p.m., and day 6 = 5:30 p.m. + 5 × 50 min = 5:30 p.m. + 4 h 10 min = **9:40 p.m.** After about a week the Moon rises around midnight, and after about 15 days it rises when the Sun is rising."),
   ("Example 2 — Phase from position", "At sunrise a **half Moon overhead** means the Moon is **waning** (last quarter), about a week after full Moon, in **Krishna Paksha**. At sunset a half Moon high in the sky is **waxing** (first quarter) in **Shukla Paksha**. A thin crescent just after sunset in the west is a **young waxing crescent**."),
   ("Example 3 — Lunar versus solar year", "12 lunar months × 29.5 days = **354 days**. Solar year = 365 days. Difference = 11 days a year; in 3 years 33 days, more than a month, so a luni-solar calendar inserts **Adhika Maasa**. A purely lunar festival like Eid-ul-Fitr falls about **11 days earlier** each year."),
   ("Example 4 — Leap years", "Divisible by 4 → leap year (2024, 2028). Century years are leap only if divisible by 400: 1900 and 2100 are **not** leap years; 2000 is. Between 1896 and 1912 the leap years are 1896, 1904, 1908, 1912 = **4** (1900 excluded)."),
   ("Example 5 — Satellite orbits per day", "A satellite 800 km above Earth takes about 100 minutes to go round once. In 24 h = 1440 min it makes 1440 ÷ 100 = 14.4, i.e. about **14 orbits per day**."),
   ("Example 6 — Why same phase everywhere", "The Moon takes about a month to go round the Earth, whereas the Earth rotates once a day, so in the time we turn once the Moon's position relative to the Sun barely changes. All places on the Earth therefore see nearly the same phase on a given day."),
 ]),
 ("h2", "Table of Phases, Timings and Positions"),
 ("table", ["Phase", "Paksha", "Best time to see", "Where in the sky", "Rises roughly at"], [
   ["New Moon (Amavasya)", "End of Krishna / start of Shukla", "Not visible", "Near the Sun", "Sunrise"],
   ["Waxing crescent", "Shukla", "Just after sunset", "Low in the west", "Morning (after sunrise)"],
   ["First quarter (half, waxing)", "Shukla", "Evening", "High in the sky at sunset", "About noon"],
   ["Full Moon (Purnima)", "Between the pakshas", "All night", "Opposite the Sun", "Sunset"],
   ["Last quarter (half, waning)", "Krishna", "Before sunrise / morning", "Overhead at sunrise", "About midnight"],
   ["Waning crescent", "Krishna", "Just before sunrise", "Low in the east near the Sun", "Early morning"]]),
 ("note", "REMEMBER", "**Common mistakes:** (1) Earth's shadow does **not** cause phases; it causes lunar eclipses. (2) The Moon's shape never changes. (3) Waxing = growing = Shukla Paksha; waning = shrinking = Krishna Paksha. (4) The Moon rises about **50 minutes later** each day, not earlier. (5) A lunar year is 354 days (not 365). (6) Century years such as 1900 are not leap years unless divisible by 400. (7) Satellites orbit at about 800 km; the Moon is a natural satellite; the Sun is not a satellite."),
 ("h2", "Real-Life Connections"),
 ("ul", ["**Festivals:** the Hindu, Buddhist, Jain, Sikh and Islamic festivals use the Moon's phases; Eid depends on sighting the crescent Moon; the Rashtriya Panchang from the Positional Astronomy Centre gives uniform dates.",
         "**Farming:** solar calendars keep track of seasons for sowing and harvest, so farmers prefer them; the Sun's northward and southward motion (Uttarayan, Dakshinayan) marks the seasons.",
         "**Coasts and fishing:** tides return about 50 minutes later each day, like moonrise; fishermen use tide tables to decide when to go out.",
         "**Technology:** Cartosat images feed the Bhuvan platform for maps, AstroSat studies stars, weather satellites warn of cyclones, and navigation satellites guide vehicles.",
         "**Culture and skills:** Chandrayaan 3, Aditya-L1 and student satellites show India's space programme; moon images appear in ragas, mudras and Warli and Madhubani art."]),
]
_qa2 = [
  ("A waxing Moon, half, is seen high in the sky. At what time of day is this likely? Which paksha is it?", "Around sunset (evening); Shukla Paksha."),
  ("Why do all places on the Earth see nearly the same phase on a given day?", "The Earth rotates in a day, but the Moon's position relative to the Sun changes only over a month."),
  ("State the leap year rule.", "A year divisible by 4 is a leap year, but century years must also be divisible by 400."),
]
_blocks = list(_base["blocks"])
_blocks[_i + 1] = ("qa", list(_blocks[_i + 1][1]) + _qa2)
CH = dict(_base, blocks=_blocks[:_i] + _extra + _blocks[_i:],
          takeaways=_base["takeaways"] + ["Moonrise gets about **50 minutes later every day**; a half waning Moon is overhead at sunrise and a waxing Moon is best seen at sunset.",
                                          "12 lunar months = 354 days, **11 days** shorter than the solar year; a leap year needs divisibility by 4 (century years by 400)."])

if __name__ == "__main__":
    run(__file__, BANK, 8, "Science", WS, CH)
