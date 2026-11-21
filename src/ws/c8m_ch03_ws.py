"""Class 8 Maths Ch 3 - A Story of Numbers: worksheet (50 graded questions) + detailed chapter notes."""
import sys, importlib.util
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from libws import *          # W, run

BANK = "c8m_ch03"

def _old(n):
    p = Path(__file__).resolve().parents[1] / "rn_work" / "c8_maths1" / f"c{n:02d}.py"
    s = importlib.util.spec_from_file_location(f"old{n}", p); m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
    return m.CH

for _b, _s, _v in [(5, "323", 88), (4, "1031", 77), (2, "101101", 45), (2, "100111", 39), (5, "2430", 365), (5, "2200", 300), (12, "1001", 1729), (6, "532", 200), (2, "10010", 18)]:
    assert int(_s, _b) == _v, (_b, _s)
assert int("1234", 5) == 194 and int("734", 8) == 476 and int("212", 3) == 23 and int("120", 5) == 35 and int("4210", 7) == 1477 == 7 * 211
assert int("777", 8) == 511 and int("357", 8) == 239 and 3 * 3600 + 25 * 60 + 40 == 12340 and int("1000", 4) == 64

WS = [
# ---------------- EASY ----------------
W("The Roman numeral for 49 is:", 1, "(c) XLIX. $49=40+9=\\text{XL}+\\text{IX}$. IL is not allowed (only I, X, C can be subtracted from the next two larger symbols in the specified way). (1)", "E", opts=["IL", "XXXXIX", "XLIX", "VL"]),
W("The value of the Roman numeral CDXL is:", 1, "(c) 440. CD $=500-100=400$ and XL $=50-10=40$, so $400+40=440$. (1)", "E", opts=["640", "460", "440", "340"]),
W("Which of the following is **absent** in the Roman number system?", 1, "(c) a symbol for zero. The Roman system has no zero and no place value. (1)", "E",
  opts=["a symbol for 50", "use of subtraction (IV, IX)", "a symbol for zero", "a symbol for 1,000"]),
W("Which digit can **not** appear in a numeral written in base 5?", 1, "(d) 5. In base 5 only the digits 0, 1, 2, 3, 4 are used; five units make one group of the next place. (1)", "E", opts=["0", "3", "4", "5"]),
W("The binary number $1011_2$ equals the decimal number:", 1, "(b) 11. $1\\times8+0\\times4+1\\times2+1\\times1=11$. (1)", "E", opts=["9", "11", "13", "15"]),
W("In the number 3,52,418 the place value of the digit 5 is:", 1, "(b) 50,000. The digits from the right are ones, tens, hundreds, thousands, ten-thousands; 5 is in the ten-thousands place. (1)", "E", opts=["5,000", "50,000", "5,00,000", "500"]),
W("The people of Mesopotamia (Babylon) counted in groups of:", 1, "(d) 60. Their number system used base 60, which survives in 60 minutes in an hour. (1)", "E", opts=["10", "12", "20", "60"]),
W("Write 1,994 in Roman numerals.", 2, "$1994=1000+900+90+4$ (1) $=\\text{M}+\\text{CM}+\\text{XC}+\\text{IV}=$ **MCMXCIV** (1).", "E"),
W("Write the Roman numeral XLVII in the Hindu–Arabic system.", 1, "XL $=40$, VII $=7$, so XLVII $=$ **47** (1).", "E"),
W("A shepherd lets his sheep out in the morning and drops one pebble in a bag for each sheep. In the evening he removes one pebble for each sheep that returns, and 3 pebbles are left. How many sheep did not return? What counting idea does this use?", 2, "Each pebble left stands for one sheep that has not returned, so **3 sheep** are missing (1). The idea is **one-to-one mapping** (matching one object with one pebble) (1).", "E", wp=True),
W("A tally of the number of students present uses groups of five strokes. If there are 4 complete groups and 3 more strokes, how many students are present?", 1, "$4\\times5+3=$ **23** students (1).", "E", wp=True),
W("Expand 3,407 using place value.", 1, "$3407=3\\times1000+4\\times100+0\\times10+7\\times1$ (1).", "E"),
W("Convert $101_2$ to a decimal number.", 2, "$1\\times4+0\\times2+1\\times1$ (1) $=5$ (1).", "E"),
W("Write the decimal number 9 in base 2.", 2, "$9=8+1=1\\times8+0\\times4+0\\times2+1$ (1), so $9=1001_2$ (1).", "E"),
W("The foundation stone of an old building has the year MCMXLVII carved on it. Which year is this?", 2, "M $=1000$, CM $=900$, XL $=40$, VII $=7$ (1). Year **1947** (1).", "E", wp=True),
W("True or false (give a reason): the Roman numerals IX and XI have the same value because they use the same symbols.", 1, "**False.** IX $=9$ but XI $=11$; in the Roman system the order decides whether a symbol is subtracted or added (1).", "E"),
W("Add XIV and XXVI and write the sum in Roman numerals.", 2, "$14+26=40$ (1) $=$ **XL** (1).", "E"),
# ---------------- MEDIUM ----------------
W("Convert 88 (decimal) into base 5.", 2, "$88=5\\times17+3$, $17=5\\times3+2$, $3=5\\times0+3$ (1). Reading the remainders upward: $88=$ **$323_5$** (check: $75+10+3=88$) (1).", "M"),
W("Convert $1234_5$ into a decimal number.", 2, "$1\\times125+2\\times25+3\\times5+4$ (1) $=125+50+15+4=$ **194** (1).", "M"),
W("Convert 77 into base 4.", 2, "$77=4\\times19+1$; $19=4\\times4+3$; $4=4\\times1+0$; $1=4\\times0+1$ (1). Remainders upward: **$1031_4$** (check $64+0+12+1=77$) (1).", "M"),
W("Write 2,499 in Roman numerals.", 2, "$2499=2000+400+90+9$ (1) $=\\text{MM}+\\text{CD}+\\text{XC}+\\text{IX}=$ **MMCDXCIX** (1).", "M"),
W("Find the sum MCDXL + DLX in Roman numerals.", 2, "MCDXL $=1000+400+40=1440$ and DLX $=500+60=560$ (1). Sum $=2000=$ **MM** (1).", "M"),
W("A farmer keeps a tally of sacks of wheat: 12 complete groups of five strokes and 3 more strokes. Each sack weighs 50 kg. Find the total weight of the wheat.", 3, "Sacks $=12\\times5+3=63$ (1). Weight $=63\\times50$ (1) $=$ **3,150 kg** (1).", "M", wp=True),
W("Convert $734_8$ to a decimal number.", 2, "$7\\times64+3\\times8+4\\times1$ (1) $=448+24+4=$ **476** (1).", "M"),
W("Write 1,888 in Roman numerals and count the symbols used. Compare with the number of digits in the Hindu–Arabic numeral and say what this shows.", 3, "$1888=\\text{M}+\\text{DCCC}+\\text{LXXX}+\\text{VIII}=$ **MDCCCLXXXVIII** (1). It uses 13 symbols (1) against 4 digits; place value makes numbers short and calculation easy (1).", "M"),
W("In the number 7,070 find the place value of each 7. What job is done by the zeros?", 2, "The first 7 stands for $7000$ and the second for $70$ (1). The zeros hold the empty hundreds and ones places, so the 7s keep their correct positions (otherwise 77 would be read) (1).", "M"),
W("Write 5,03,408 in expanded form using powers of 10.", 2, "$5\\times10^5+0\\times10^4+3\\times10^3+4\\times10^2+0\\times10+8$ (2).", "M"),
W("Add $1101_2$ and $101_2$ and write the answer in base 2.", 3, "$1101_2=13$ and $101_2=5$ (1). Sum $=18$ (1). $18=16+2$, so the answer is **$10010_2$** (1).", "M"),
W("The digits of a locker code are written 357 in base 8. Find the code as an ordinary (decimal) number.", 2, "$3\\times64+5\\times8+7$ (1) $=192+40+7=$ **239** (1).", "M", wp=True),
W("A Babylonian scribe measures a journey. Express 3 hours 25 minutes 40 seconds in seconds using the base-60 idea (1 hour $=60\\times60$ s).", 3, "$3\\times3600+25\\times60+40$ (1) $=10800+1500+40$ (1) $=$ **12,340 seconds** (1).", "M", wp=True),
W("Ravi writes 40 as XXXX and 900 as DCCCC. Are these correct in the standard Roman system? Correct them.", 2, "No: a symbol is not repeated more than three times; the subtractive forms are used (1). $40=$ **XL** and $900=$ **CM** (1).", "M"),
W("Convert 45 into base 2.", 2, "Dividing by 2: 45 → 22 r1; 22 → 11 r0; 11 → 5 r1; 5 → 2 r1; 2 → 1 r0; 1 → 0 r1 (1). Remainders upward: **$101101_2$** (32 + 8 + 4 + 1 = 45) (1).", "M"),
W("Which is larger: $212_3$ or $120_5$? Show your working.", 3, "$212_3=2\\times9+1\\times3+2=23$ (1). $120_5=1\\times25+2\\times5+0=35$ (1). **$120_5$ is larger** (1).", "M"),
W("Find MM − CMXCIX and write the answer in Roman numerals.", 2, "MM $=2000$, CMXCIX $=999$ (1). Difference $=1001=$ **MI** (1).", "M"),
W("What is the largest 3-digit number in base 8? Convert it to decimal and say what number comes next in base 8.", 3, "Largest 3-digit numeral is $777_8$ (1). $=7\\times64+7\\times8+7=511$ (1). The next number is $1000_8=512$ (1).", "M"),
W("A clock face has Roman numerals. The hour hand points exactly halfway between IX and X and the minute hand points at VI. What time does the clock show? Write the time using Roman numerals for the hour.", 2, "The minute hand at VI means 30 minutes (1). Time $=9{:}30$, the hour is IX (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Write 3,999 in Roman numerals. Why can 4,000 not be written by the same rules?", 3, "$3999=3000+900+90+9=$ **MMMCMXCIX** (2). 4,000 would need M four times, but a symbol is not repeated more than three times and there is no larger symbol (1).", "H"),
W("An old film is 7,265 seconds long. Express its length in hours, minutes and seconds using the base-60 idea.", 3, "$7265=2\\times3600+65$ (1); $65=1\\times60+5$ (1). Length $=$ **2 h 1 min 5 s** (1).", "H", wp=True),
W("Convert 365 into base 5.", 3, "$365=5\\times73+0$; $73=5\\times14+3$; $14=5\\times2+4$; $2=5\\times0+2$ (2). Remainders upward: **$2430_5$** (check: $250+100+15+0=365$) (1).", "H"),
W("In which base $b$ does $123_b$ equal 38 in decimal? (The digits show $b>3$.)", 4, "$123_b=b^2+2b+3$ (1). $b^2+2b+3=38\\Rightarrow b^2+2b-35=0$ (1), so $(b+7)(b-5)=0$ (1). $b=$ **5** (check: $25+10+3=38$) (1).", "H"),
W("A shopkeeper has weights of 1 kg, 2 kg, 4 kg, 8 kg and 16 kg (one of each). Which weights should be used together to weigh exactly 27 kg of sugar? Connect your answer with base 2.", 4, "$27=16+8+2+1$ (2): use the 16, 8, 2 and 1 kg weights, leave out the 4 kg (1). In base 2, $27=11011_2$; the digits 1 mark the weights used (1).", "H", wp=True),
W("Multiply $1101_2$ by $11_2$ and give the answer in base 2.", 4, "$1101_2=13$, $11_2=3$ (1). Product $=39$ (1). $39=32+4+2+1$ (1) $=$ **$100111_2$** (1).", "H"),
W("Write 1,000 (decimal) in base 4.", 4, "$1000=4\\times250+0$; $250=4\\times62+2$; $62=4\\times15+2$; $15=4\\times3+3$; $3=4\\times0+3$ (3). Remainders upward: **$33220_4$** (check: $768+192+32+8+0=1000$) (1).", "H"),
W("**Case study.** The Hindu system uses ten symbols 0–9 with place value and a symbol for zero. (i) Give two reasons why this system is better than the Roman system for calculation. (ii) Write the place values of the two 5s in 5,005 and say what 55 would mean if the zeros were not written.", 4, "(i) Any number, however large, is written with only ten symbols; place value and zero allow simple column addition and multiplication, whereas Roman needs long strings and has no zero (2). (ii) The 5s stand for $5000$ and $5$ (1). Without the zeros it would be read as 55 (1).", "H", wp=True),
W("Write 200 (decimal) in base 6.", 3, "$200=6\\times33+2$; $33=6\\times5+3$; $5=6\\times0+5$ (2). Remainders upward: **$532_6$** (check: $180+18+2=200$) (1).", "H"),
W("Ranjit has coins of ₹ 1, ₹ 5, ₹ 25 and ₹ 125 only (as many as needed). Using the idea of base 5, find the smallest number of coins needed to pay ₹ 300 and name them.", 4, "$300=5\\times60+0$, $60=5\\times12+0$, $12=5\\times2+2$, $2=5\\times0+2$ (2). So $300=2200_5=2\\times125+2\\times25$ (1): **4 coins**, two of ₹ 125 and two of ₹ 25 (1).", "H", wp=True),
W("Sonal converts 100 into base 5 by repeated division, gets remainders 0, 0, 4 (in that order) and writes $004_5$. Find her mistake, give the correct numeral and verify it.", 3, "She read the remainders in the wrong order (1). The remainders must be read **from the last to the first**: **$400_5$** (1). Check: $4\\times25+0+0=100$ ✓ (1).", "H"),
W("Write 1,729 in base 12 and comment on what you notice.", 3, "$1729=12^3+1=1\\times1728+0\\times144+0\\times12+1$ (2). So $1729=1001_{12}$; it is one more than $12^3$, which is why its base-12 form looks so simple (1).", "H"),
W("The date on an old coin reads MDCCCXLVII. Find the year and how many years ago (from 2026) it was struck.", 3, "M $=1000$, DCCC $=800$, XL $=40$, VII $=7$ (1). Year $=1847$ (1). $2026-1847=$ **179 years ago** (1).", "H", wp=True),
W("Show that a numeral in base 7 that ends in 0 is a multiple of 7. Verify with $4210_7$.", 3, "The last digit is the number of ones; every other place value ($7,49,343,\\dots$) is a multiple of 7, so the whole number is a multiple of 7 when the ones digit is 0 (1). $4210_7=4\\times343+2\\times49+1\\times7+0=1477$ (1), and $1477=7\\times211$ ✓ (1).", "H"),
]

for _w in WS:
    _w["q"] = _w["q"].replace("**", ""); _w["ans"] = _w["ans"].replace("**", "")

_o = _old(3)
_pre = _o["blocks"][:-2]
_extra = [
 ("h2", "3.6 Roman Numerals: Rules and Examples"),
 ("table", ["Symbol", "Value", "Rule"], [["I, X, C, M", "1, 10, 100, 1000", "can be repeated up to **three** times (III, XXX, CCC, MMM)"], ["V, L, D", "5, 50, 500", "never repeated, never subtracted"], ["IV, IX", "4, 9", "I before V or X is subtracted"], ["XL, XC", "40, 90", "X before L or C is subtracted"], ["CD, CM", "400, 900", "C before D or M is subtracted"]]),
 ("p", "Read from the left: add values that fall or stay equal, and subtract a smaller symbol that stands **before** a larger one. 1994 = M + CM + XC + IV = **MCMXCIV**; 3,999 = MMM + CM + XC + IX = **MMMCMXCIX**. 4,000 cannot be written by these rules because M would have to be repeated four times. Roman numerals have **no zero** and no place value, so even simple sums such as MCDXL + DLX (1440 + 560 = 2000 = MM) are done by first converting to our system."),
 ("h2", "3.7 Worked Examples"),
 ("h3", "Example 1 — Decimal to another base"),
 ("steps", [("Convert 365 to base 5", "Divide repeatedly by 5 and keep the remainders: 365 = 5 × 73 + 0; 73 = 5 × 14 + 3; 14 = 5 × 2 + 4; 2 = 5 × 0 + 2."), ("Read upward", "The last remainder comes first: 2, 4, 3, 0."), ("Answer and check", "365 = **2430 in base 5**; 2 × 125 + 4 × 25 + 3 × 5 + 0 = 365.")]),
 ("h3", "Example 2 — Another base to decimal"),
 ("steps", [("Convert 357 in base 8", "Place values from the right: 1, 8, 64."), ("Multiply and add", "3 × 64 + 5 × 8 + 7 × 1 = 192 + 40 + 7."), ("Answer", "**239**.")]),
 ("h3", "Example 3 — Finding the base"),
 ("steps", [("123 in base b equals 38. Find b", "123 in base b = b² + 2b + 3."), ("Form the equation", "b² + 2b + 3 = 38, so b² + 2b − 35 = 0, that is (b + 7)(b − 5) = 0."), ("Answer", "b cannot be negative, so **b = 5** (25 + 10 + 3 = 38).")]),
 ("h3", "Example 4 — Binary arithmetic through decimals"),
 ("steps", [("Multiply 1101 by 11 in base 2", "1101 in base 2 = 13 and 11 in base 2 = 3."), ("Multiply", "13 × 3 = 39."), ("Convert back", "39 = 32 + 4 + 2 + 1, so the product is **100111 in base 2**.")]),
 ("h3", "Example 5 — Base 60 in everyday life"),
 ("steps", [("Express 3 h 25 min 40 s in seconds", "1 h = 60 × 60 = 3600 s; 1 min = 60 s."), ("Add", "3 × 3600 + 25 × 60 + 40 = 10,800 + 1,500 + 40."), ("Answer", "**12,340 seconds**. The reverse (7,265 s → 2 h 1 min 5 s) uses repeated division by 60, exactly like changing base.")]),
 ("h3", "Example 6 — Weights and the binary system"),
 ("steps", [("Weigh 27 kg with 1, 2, 4, 8, 16 kg weights", "Write 27 in base 2: 16 + 8 + 2 + 1."), ("Choose the weights", "Use 16, 8, 2 and 1; leave out 4."), ("Binary form", "27 = 11011 in base 2; each 1 marks a weight used. Every weight from 1 to 31 kg can be made this way.")]),
 ("h2", "3.8 Comparing the Number Systems"),
 ("table", ["Feature", "Tally / Egyptian", "Roman", "Mesopotamian", "Hindu (Indian)"], [
  ["Base", "10 (Egyptian)", "10 and 5 (mixed)", "60", "10"],
  ["Place value", "no", "no", "yes (no early zero)", "yes"],
  ["Zero", "no", "no", "no (empty place left in early form)", "**yes**, as placeholder and number"],
  ["Symbols needed for big numbers", "many repeated symbols", "long strings", "few", "only ten digits"],
  ["Calculation", "difficult", "difficult", "possible", "easy"]]),
 ("h2", "3.9 Word Problems: How to Translate"),
 ("table", ["Words", "Idea", "Example"], [
  ["‘a pebble for each animal’, ‘pebbles left over’", "one-to-one mapping", "3 pebbles left means 3 sheep missing"],
  ["tally strokes in groups of five", "total = 5 × groups + extra", "12 groups + 3 = 63"],
  ["a year or date in Roman numerals", "convert, then subtract from the present year", "MDCCCXLVII = 1847; 2026 − 1847 = 179 years"],
  ["hours, minutes, seconds", "base 60", "7,265 s = 2 h 1 min 5 s"],
  ["coins or weights of 1, 5, 25, 125 or 1, 2, 4, 8", "powers of 5 or 2: write the amount in that base", "₹300 = 2200 in base 5: two ₹125 and two ₹25 coins"]]),
 ("h2", "3.10 Common Mistakes"),
 ("table", ["Wrong working", "Why it is wrong", "Correct"], [
  ["IL for 49, VX for 5", "only I, X, C may be subtracted, and only from the next two larger symbols", "49 = XLIX; 5 = V"],
  ["XXXX for 40", "no symbol repeated more than three times", "XL"],
  ["Remainders read from the top (004 for 100 in base 5)", "the last remainder is the leading digit", "400 in base 5"],
  ["A digit 5 in a base-5 numeral", "digits in base b run from 0 to b − 1", "base 5 uses 0–4"],
  ["In base 2: 1 + 1 = 2", "there is no digit 2; carry to the next place", "1 + 1 = 10 in base 2"]]),
 ]
CH = dict(_o, blocks=_pre + _extra + _o["blocks"][-2:], takeaways=_o["takeaways"] + ["To **convert to base b** divide repeatedly by b and read the remainders **upward**; to convert **back**, multiply each digit by its place value.", "Everyday base-60 and base-2 ideas (time, weights) turn many **word problems** into base conversions."])

if __name__ == "__main__": run(__file__, BANK, 8, "Maths", WS, CH)
