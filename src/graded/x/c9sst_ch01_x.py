"""Class 9 SST Ch 1 The Problem of Choice - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("Opportunity cost can arise even when no money is spent.", "Time is also a scarce resource and has alternative uses.", "a",
     "Spending an hour on play means giving up the next best use of that hour (such as study), so opportunity cost exists without money."),
 AR4("India is regarded as a mixed economy.", "The Economic Survey of India is presented in Parliament before the Union Budget.", "b",
     "Both statements are true (private enterprise and government participation co-exist), but the timing of the Survey does not explain why India is mixed."),
 AR4("Human wants are unlimited.", "Resources available to an economy are also unlimited.", "c",
     "Wants keep growing, so A is true; resources are limited (scarce) with alternative uses, so R is false."),
 AR4("A point lying inside the production possibility curve shows that all resources are being used efficiently.", "A point on the curve shows the maximum output combination that can be produced with the given resources.", "d",
     "A point inside the PPC means resources are not fully or efficiently used, so A is false; R is a correct description of points on the PPC."),
 AR4("A PPC slopes downward.", "Producing more of one good means using resources taken away from the other good.", "a",
     "Because the resources are fixed, more barley means less wheat; this trade-off gives the downward slope."),
 AR4("Street lights and public parks are usually provided by the government.", "Such public goods are available to all without exclusion and may not yield direct profit to private firms.", "a",
     "Because no one can be excluded and profit is hard to earn, private firms under-provide them and the government steps in."),
]

CASE = [
 Q("<b>Case study.</b> Meena has one field and fixed resources. She can produce 100 kg wheat and 0 barley (A), or 90 kg wheat and 25 kg barley (B), or 70 kg wheat and 50 kg barley (C), or 40 kg wheat and 75 kg barley (D), or 0 wheat and 100 kg barley (E). "
   "(i) What does she give up when she moves from A to B? (ii) What is the opportunity cost of the extra 25 kg barley in moving from B to C? (iii) Can she produce 50 kg barley and 90 kg wheat together with these resources? (iv) Find the opportunity cost of one kg of barley in moving from D to E and explain why this cost keeps rising.",
   "(i) She gives up 10 kg of wheat (100 - 90) (1). (ii) 90 - 70 = 20 kg of wheat (1). (iii) No; this point lies outside the PPC, so it cannot be produced with the given resources (1). (iv) She gives up 40 kg wheat for 25 kg barley, i.e. 40/25 = 1.6 kg wheat per kg barley (1); the cost rises because the resources are not equally suited to producing both goods (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In country X a central planning authority fixes what is produced and at what price. In country Y prices and output are decided by demand and supply, and the government mainly makes rules and provides public goods. Country Z has private hospitals as well as free government hospitals, and private factories beside public-sector ones. "
   "(i) Name the economic system of X. (ii) Name the system of Y and one country cited as its example. (iii) Which system does Z follow, and which of the three systems is India regarded as? (iv) State one likely drawback of X and one likely strength of Y.",
   "(i) Planned economy (1). (ii) Market economy; the USA (1). (iii) Z has a mixed economy; India is also regarded as a mixed economy (1). (iv) Drawback of a planned economy: little motive to improve quality or innovate (1); strength of a market economy: competition leads to better quality and innovation (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A garment firm in Tiruppur finds that wages of workers have risen sharply, while the cost of stitching machines has fallen. Earlier the firm employed 100 workers; now it plans to run 10 machines instead. The firm also decides to make low-cost school uniforms for daily buyers rather than costly designer clothes. "
   "(i) Which of the three key questions of economics is the firm answering when it chooses machines or workers? (ii) What is meant by a labour-intensive method? (iii) Which method is the firm moving towards? (iv) Which key question is answered by choosing uniforms instead of designer clothes, and why does a change in the cost of labour influence the firm's technique?",
   "(i) How to produce (1). (ii) A method using many workers and relatively few machines (1). (iii) Capital-intensive (1). (iv) 'For whom to produce' (1); producers choose the cheaper way of production, so when labour becomes costly and machines become cheap, using more machines lowers the cost (1).", "1+1+1+2"),
]

MISTAKES = [
 "Opportunity cost is <b>not</b> the money spent or every alternative given up; it is the value of the <b>next best</b> alternative given up.",
 "Do not confuse <i>needs</i> and <i>wants</i>: food, water and shelter are needs; a designer watch or holiday trip is a want. Wants keep changing and growing.",
 "A PPC slopes <b>downward</b>. A point inside it means resources are under-used; a point outside it is not attainable with the given resources.",
 "Scarcity means limited resources compared with unlimited wants. It does not mean poverty, and it affects governments and firms as well as households.",
 "Match systems correctly: Cuba and North Korea are planned economies, the USA is a market economy, and India is a <b>mixed</b> economy.",
 "Do not mix up labour-intensive (handicrafts, traditional farming) with capital-intensive (steel, automobiles), or the three questions: what, how and for whom to produce.",
]
