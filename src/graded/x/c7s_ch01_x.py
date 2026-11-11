"""Class 7 Science Ch 1 Acidic, Basic and Neutral - Hard-tier extras, formula sheet, mistakes box."""
from common import AR4, Q

AR = [
 AR4("Turmeric paper turns red when soap solution is dropped on it.", "Soap solution is basic in nature.", "a",
     "Turmeric turns red (reddish brown) with bases, and soap solution is a base, so R explains A."),
 AR4("Red litmus paper turns blue when dipped in lemon juice.", "Lemon juice is acidic in nature.", "d",
     "Acids turn blue litmus red and do not change red litmus; so A is false, but R is true."),
 AR4("Neutralisation is the reaction between an acid and a base to form salt and water.", "Heat is released during a neutralisation reaction.", "b",
     "Both statements are true, but the release of heat does not explain why salt and water form."),
 AR4("Antacid tablets give relief from indigestion.", "Antacids are bases that neutralise the excess acid in the stomach.", "a",
     "The stomach has hydrochloric acid; a base neutralises the extra acid, which explains the relief."),
 AR4("Baking soda solution is rubbed on an ant sting to soothe it.", "Baking soda is acidic in nature.", "c",
     "The sting has formic acid and baking soda (a base) neutralises it; so A is true, R is false."),
 AR4("Bases such as soap solution feel slippery to touch.", "Acids such as vinegar taste sour.", "b",
     "Both are true properties, but the sour taste of acids does not explain the slippery feel of bases."),
]

CASE = [
 Q("<b>Case study.</b> After eating too many spicy samosas at a mela in Lucknow, Rohan complains of burning in his stomach. His mother gives him a spoonful of milk of magnesia. Rohan's younger sister suggests giving him lemon juice instead, saying it is 'good for the stomach'. "
   "(i) Name the acid naturally present in the stomach. (ii) What is the nature of milk of magnesia? (iii) Name the type of reaction that gives relief to Rohan. (iv) Explain why lemon juice would not be a good choice.",
   "(i) Hydrochloric acid (1). (ii) It is a base (an antacid) (1). (iii) Neutralisation (1). (iv) Lemon juice is acidic (it contains citric acid) (1), so it would add more acid to the stomach and make the burning worse instead of neutralising the extra acid (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In the school laboratory, Meena crushes red China rose petals in water and filters the liquid to make an indicator. She adds a few drops to three samples: lemon juice, soap solution and sugar solution. "
   "(i) What colour does the China rose indicator give with lemon juice? (ii) What colour does it give with soap solution? (iii) What happens in the sugar solution? (iv) A fourth liquid turns turmeric paper red. State its nature and what it will do to red litmus paper, giving a reason.",
   "(i) Dark pink (magenta) (1). (ii) Green (1). (iii) No colour change, because sugar solution is neutral (1). (iv) The liquid is a base, because only bases turn turmeric red (1); it will turn red litmus paper blue, as bases do (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A farmer near Ludhiana finds that wheat grows poorly in one field. A soil test shows that the soil is too acidic. The agriculture officer advises him to spread quicklime (calcium oxide) over the field. A nearby factory also releases acidic waste into a canal, and fish in the canal are dying. "
   "(i) What is the nature of the farmer's soil? (ii) Which substance is added to the soil? (iii) Name the process by which the soil acidity is reduced. (iv) What should the factory do before releasing its waste, and why?",
   "(i) Acidic (1). (ii) Quicklime (a base) (1). (iii) Neutralisation (1). (iv) The factory should treat the acidic waste with a basic substance (1) so that the acid is neutralised and the water in the canal is not harmful to fish (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Acids, bases and neutral substances", [
   "Acids taste sour (lemon: citric acid; vinegar: acetic acid; curd: lactic acid; ant sting: formic acid).",
   "Bases taste bitter and feel soapy or slippery (soap solution, baking soda, lime water).",
   "Neutral substances (sugar solution, pure water) are neither acidic nor basic.",
   "Laboratory acids: hydrochloric acid HCl, sulphuric acid H$_2$SO$_4$, nitric acid HNO$_3$ (never taste them)."]),
 ("Indicators and their colour changes", [
   "Litmus: acid turns blue litmus RED; base turns red litmus BLUE; neutral: no change.",
   "Turmeric: base turns it RED (reddish brown); acid and neutral: no change.",
   "China rose: acid gives dark pink (magenta); base gives green; neutral: no change.",
   "An indicator is a substance that shows by a colour change whether a substance is acidic or basic."]),
 ("Neutralisation", [
   "Acid + Base $\\rightarrow$ Salt + Water (+ heat is released).",
   "Antacids (milk of magnesia) are bases that neutralise excess stomach acid.",
   "Baking soda or calamine soothes an ant sting (formic acid) or nettle sting.",
   "Acidic soil is treated with quicklime or slaked lime; acidic factory waste is treated with a base."]),
 ("Handling safely", [
   "Do not taste or touch unknown chemicals; use natural indicators for testing at home.",
   "Dilute the acid in water, never add water to a concentrated acid."]),
]

MISTAKES = [
 "Saying that acids turn red litmus blue; remember <b>acid: blue litmus becomes red</b>, and <b>base: red litmus becomes blue</b>.",
 "Expecting turmeric to change colour with an acid; turmeric changes (to red) only with a base.",
 "Forgetting that a neutral substance (sugar solution, water) gives <i>no change</i> with every indicator.",
 "Writing the products of neutralisation as only 'salt'; the products are <b>salt and water</b> (with heat).",
 "Mixing up the colours of China rose: acid gives <i>dark pink</i>, base gives <i>green</i>.",
 "Believing that every sour thing is dangerous; many edible substances (lemon, curd, vinegar) are weak acids, but laboratory acids must never be tasted.",
]
