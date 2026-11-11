"""Class 6 Science Ch 1 The Wonderful World of Science - extras."""
from common import AR4, Q

AR = [
 AR4("A hypothesis is a guess that can be tested.", "An experiment can show whether a hypothesis is supported or not.", "a",
     "A hypothesis is a testable explanation, and testing it by an experiment is exactly how we check it."),
 AR4("Observation is the first step of the scientific method.", "A telescope helps us observe objects that are very far away in the sky.", "b",
     "Both are true, but the use of a telescope does not explain why observation comes first."),
 AR4("Scientists repeat an experiment several times before accepting the result.", "The result of one trial is always enough to be sure.", "c",
     "A is true because repeating avoids mistakes; R is false, a single trial can be wrong."),
 AR4("Once a scientific fact is found, it can never change.", "New observations and experiments can improve our understanding of nature.", "d",
     "A is false: science keeps growing and old ideas may be improved. R is true."),
 AR4("A microscope is used to study very tiny things like the cells of an onion peel.", "A microscope makes very small objects look larger.", "a",
     "Because it magnifies, tiny things become visible; R explains A."),
 AR4("Botany is the study of plants.", "Astronomy is the study of stars, planets and space.", "b",
     "Both statements are true, but one does not explain the other."),
]

CASE = [
 Q("<b>Case study.</b> Riya noticed that the plant on her balcony grew taller than the plant kept inside her cupboard. She guessed that plants need sunlight to grow well. She took two identical pots with the same soil and gave both the same amount of water. She kept one in sunlight and the other in a dark cupboard, and noted the height of both plants every two days for ten days. "
   "(i) What is Riya's guess called? (ii) Which one thing was different for the two pots? (iii) Name the step in which she noted the heights every two days. (iv) Why did she keep the soil and water the same? What is the likely conclusion?",
   "(i) A hypothesis (1). (ii) The amount of sunlight (1). (iii) Recording the observations (or results) (1). (iv) Only one thing should change so that any difference can be blamed on sunlight (1); the plant in sunlight grew better, so plants need sunlight (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Imran's grandfather says, 'Ants carry their eggs out before rain.' Imran decides not to simply believe it. For 15 days he watched an ant line near his house in Lucknow, wrote in his notebook whether ants moved eggs, and also noted whether it rained that day. "
   "(i) Which scientific habit does Imran show by not simply believing the claim? (ii) What should he do first: guess or observe carefully? (iii) Why is it important to write the data in a notebook? (iv) Why will 15 days of records be better than one day?",
   "(i) Questioning or checking claims (curiosity) (1). (ii) Observe carefully (1). (iii) Records stop us forgetting and let us compare and study the data later (1). (iv) Many observations show whether the pattern repeats, so the conclusion is more reliable (1) and a chance event on one day does not mislead us (1).", "1+1+1+2"),
 Q("<b>Case study.</b> At a science exhibition in Pune, Meera saw a stall showing a sample of pond water under a microscope, another stall showing the Moon through a telescope, and a third stall showing a stethoscope and a thermometer. The guide said each tool helps us find out things that our eyes alone cannot. "
   "(i) Which instrument helps to see tiny living things in pond water? (ii) Which instrument shows distant objects like the Moon? (iii) Name the branch of science that studies stars and planets. (iv) Why do scientists need instruments instead of depending only on their senses?",
   "(i) Microscope (1). (ii) Telescope (1). (iii) Astronomy (1). (iv) Our senses cannot see very tiny or very distant things (1); instruments also give more exact and reliable measurements (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Steps of the scientific method", ["Observe and ask a question.", "Make a hypothesis (a testable guess).", "Do an experiment and keep everything same except one thing.",
   "Record the results carefully.", "Draw a conclusion; repeat to be sure."]),
 ("Key words", ["Curiosity: the urge to ask why and how.", "Observation: looking carefully with our senses.", "Hypothesis: a guess that can be tested.",
   "Experiment: a test done to check a hypothesis.", "Conclusion: what the results tell us."]),
 ("Branches of science", ["Botany: plants. Zoology: animals.", "Astronomy: stars, planets and space.", "Physics: matter, energy, motion. Chemistry: substances and their changes."]),
 ("Tools and good habits", ["Microscope: tiny things. Telescope: faraway things.", "Be honest, record exactly what you see.", "Do not accept any claim without checking it.", "Science grows: new findings can improve old ideas."]),
]

MISTAKES = [
 "Calling a guess a <b>conclusion</b>: the guess before the experiment is a hypothesis; the conclusion comes after the results.",
 "Changing many things in an experiment at once; only <b>one</b> condition should be changed.",
 "Writing only what you expected to see instead of what you actually observed.",
 "Believing that one trial is enough; experiments are repeated to be sure.",
 "Mixing up the instruments: microscope is for tiny things, telescope is for faraway things.",
 "Saying science facts never change; new evidence can improve our understanding.",
]
