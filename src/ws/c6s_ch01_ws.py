"""Class 6 Science Ch 1 - The Wonderful World of Science: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch01"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch01", str(REPO / "src/rn_work/c6_sci/ch01.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("What is the most important quality of a learner of science?", 1, "(c) curiosity", "E", opts=["memorising", "speed", "curiosity", "silence"]),
W("The first step of the scientific method is to:", 1, "(b) observe and wonder about something", "E", opts=["write the conclusion", "observe and wonder about something", "buy a lab kit", "guess the final answer"]),
W("A guess that can be tested by an experiment or more observations is called a:", 1, "(a) hypothesis", "E", opts=["hypothesis", "rumour", "slogan", "habit"]),
W("Science is compared to a giant, unending ______ in the chapter.", 1, "(d) jigsaw puzzle", "E", opts=["race", "tree", "ladder", "jigsaw puzzle"]),
W("Which of these is the only planet known to support life?", 1, "(b) Earth", "E", opts=["Mars", "Earth", "Venus", "Jupiter"]),
W("Which person is using the scientific method when finding where the air leaks from a flat tyre?", 1, "(c) a bicycle repair person", "E", opts=["a singer", "a dancer", "a bicycle repair person", "a painter"]),
W("Fill in the blank: Science is a way of thinking, observing and ______ things.", 1, "doing.", "E"),
W("Write True or False: Science is only about memorising facts.", 1, "False. Science is a step-by-step process of finding answers to questions. (1)", "E"),
W("Write True or False: Only great scientists in big laboratories can use the scientific method.", 1, "False. A cook, a mechanic or an electrician also uses it in daily life. (1)", "E"),
W("Name the book of this class that is named after the most important quality of a science learner.", 1, "*Curiosity*. (1)", "E"),
W("Put these steps of the scientific method in the correct order: test the guess, observe and wonder, analyse the results, guess an answer.", 2, "Observe and wonder, guess an answer, test the guess, analyse the results. (2)", "E"),
W("Your pen stops writing. Write one possible guess (hypothesis) for why this happened.", 1, "The ink in the refill has finished. (Any sensible, testable guess, e.g. the ink has dried, is accepted.) (1)", "E"),
W("How can you test the guess that the ink of your pen has finished?", 1, "Open the pen and look at the refill. If the refill is empty, the guess is correct. (1)", "E"),
W("Give two places where we can find science, according to the chapter.", 2, "Any two: mountains, deserts, coasts, ocean depths, outer space, kitchen, playground. (1+1)", "E"),
W("Why is science compared to a jigsaw puzzle? Give one reason.", 2, "Every new discovery adds one more piece to the puzzle, and there is no end to what we can discover. (2)", "E"),
W("A cook says, \"Why did the dal spill out of the cooker?\" Which step of the scientific method is the cook doing?", 1, "The cook has observed something puzzling and is asking a question (the first steps of the method). (1)", "E"),
W("Name any two habits of a good learner of science.", 2, "Any two: being curious, observing keenly, asking how and why, working together with others, enjoying the journey. (1+1)", "E"),
# ---------------- MEDIUM ----------------
W("Which of these can be answered by doing a test: (i) Which colour is the nicest? (ii) Does a seed sprout faster in warm water than in cold water? Give a reason.", 2, "(ii). We can test it by keeping seeds in warm and cold water and observing them. A liking such as the nicest colour is an opinion and cannot be tested. (1+1)", "M"),
W("Rohan's torch does not light. Write the steps he can follow using the scientific method, with one guess and one test.", 3, "Observe: the torch does not light and he wonders why (1). Guess: the cells are used up (1). Test: put in new cells; if it glows the guess is right, otherwise guess another cause such as a loose bulb and test it (1).", "M", wp=True),
W("Meena's mother notices that the milk turns sour by evening in summer but not in winter. Which step of the scientific method is this and what can Meena do next?", 3, "This is observing and wondering (1). Meena can guess that heat makes milk go sour (1) and test it by keeping two cups of boiled milk, one in a cool place and one in a warm place, and comparing them (1).", "M", wp=True),
W("Why does the chapter say that a wrongly placed jigsaw piece may have to be moved? What does it show about science?", 2, "Sometimes an earlier idea is found to be wrong. New discoveries can change our understanding, so science keeps growing and correcting itself. (2)", "M"),
W("An electrician finds that a room's light is not working. List two guesses he can make and how he will test them.", 3, "Guess 1: the bulb is fused, test by fitting a good bulb (1.5). Guess 2: the switch is faulty, test by checking or replacing the switch (1.5). Any two sensible guess and test pairs are accepted.", "M", wp=True),
W("Anish's potted plant has dried up and he says, \"The Sun is the cause.\" What should he do before accepting this?", 2, "He should test his guess instead of accepting it at once, for example keep another similar plant in the same place and water it properly, and observe. (2)", "M", wp=True),
W("Explain the difference between a guess made at random and a hypothesis.", 2, "A hypothesis is a guess that can be tested by experiments or observations; a random guess is not tested. (2)", "M"),
W("A farmer sees that crops in one corner of the field grow poorly. Name the first two steps he will follow like a scientist.", 2, "He first observes and wonders why they grow poorly (1) and then asks a question and makes a guess, e.g. that the soil there is dry (1).", "M", wp=True),
W("Write True or False and give a reason: If a guess turns out to be wrong in a test, the whole effort is wasted.", 2, "False. A wrong guess still teaches us something, and we then make another guess and test it. (2)", "M"),
W("Why do scientists across the world work together in large teams?", 2, "Science is rarely done alone. Working together lets people share ideas and solve bigger problems. (2)", "M"),
W("Find the mistake: \"Aman guessed that his bicycle tyre was flat because of a puncture. Without checking, he told everyone it was a puncture.\"", 2, "He did not test his guess. He should check the tyre, e.g. put it in water and look for bubbles, before saying it is a puncture. (2)", "M", wp=True),
W("Write two questions about your school playground that you could answer by observing.", 2, "Any two sensible observable questions, e.g. Which part of the ground dries first after rain? Which tree gives the most shade at noon? (1+1)", "M", wp=True),
W("Match: (a) cook (b) cycle repair person (c) electrician with (1) Is the fault in the bulb or the switch? (2) Where has the air leaked from? (3) Was there too much water in the cooker?", 3, "(a) with (3), (b) with (2), (c) with (1). (1 each)", "M"),
W("In the chapter, which topics will we explore as we move from our home to the wider universe? Name any three.", 3, "Any three: living things, food, water, hot and cold, materials, things beyond Earth (Sun, Moon, stars), movement. (1 each)", "M"),
W("Water boils and turns to steam, and water freezes to ice. Which question from the chapter does this raise?", 1, "Why does water freeze to ice and boil to steam? (1)", "M"),
W("Radha says that science is only done in laboratories. Give two examples to prove her wrong.", 2, "A cook finding why dal spilled and a mechanic finding a leak in a tyre use the scientific method in the kitchen and in a workshop. (1+1)", "M", wp=True),
W("Why is it helpful to ask \"how\" and \"why\" about things around us?", 2, "These questions make us curious, and curiosity leads us to observe, test and understand how things work. (2)", "M"),
W("The chapter says that anyone following the scientific method is working like a scientist. Explain with a school example.", 2, "A student whose geometry box does not open guesses that it is rusty, looks at the hinge and puts oil on it. She followed the steps, so she worked like a scientist. (2)", "M", wp=True),
W("Why will we not find answers to all our questions in Class 6?", 2, "Science is a long journey of many years and each answer raises new questions, like new pieces in a jigsaw puzzle. (2)", "M"),
W("Name two things that science studies at a very small size and two at a very large size.", 2, "Small: a grain of sand, a leaf of grass. Large: a mountain, a forest, stars and galaxies. (1+1)", "M"),
# ---------------- HARD ----------------
W("Seema's tomato plant gets yellow leaves. She guesses it needs more water, waters it daily and the leaves stay yellow. Explain what she should do next.", 3, "Her guess was tested and found wrong (1). She should make a new guess, e.g. too much water, too little sunlight or poor soil (1), and test each guess one at a time (1).", "H", wp=True),
W("Imran's radio has stopped working. Write how he can find the fault using all steps of the scientific method.", 4, "Observe: the radio gives no sound (1). Question: why has it stopped? (1) Guess: the cells are weak (1). Test: change the cells; if it plays the guess was right, otherwise guess another cause and test it, then analyse results (1).", "H", wp=True),
W("Two friends test whether a plant grows better in sunlight. Ravi keeps one plant in sunlight and one in a dark cupboard but gives the cupboard plant less water. What is wrong and how will you correct it?", 3, "He changed two things, sunlight and water, so he cannot tell which caused the difference (1). Both plants should get the same water, soil and pot (1) and only the amount of light should differ (1).", "H", wp=True),
W("The jigsaw puzzle idea says that new knowledge raises more questions. Explain with an example from the chapter.", 3, "Each discovery adds a piece and shows new gaps (1). For example, we learn that Earth supports life and then ask how plants and animals in different regions survive (1) and how a seed becomes a plant (1).", "H"),
W("In a village school a student says, \"The cooker whistle came late because the dal was old.\" Another says, \"It was because the flame was low.\" How can the class decide who is right?", 3, "Each statement is a hypothesis (1). The class can cook old dal on a high flame and fresh dal on a low flame, changing one thing at a time (1), and compare the results to decide (1).", "H", wp=True),
W("Why is it important that scientists record results honestly even when the results do not match their guess?", 3, "A guess is only a possibility (1). Honest results show what is really true, and hiding them gives wrong knowledge (1). A wrong guess is also useful because it leads to a better guess (1).", "H"),
W("Explain why the scientific method is used by people \"knowingly or unknowingly\".", 3, "In daily life many people observe a problem, guess the reason and test it without knowing the name of the method (1), e.g. a cook or a mechanic (1). This shows the method is natural and everyone can use it (1).", "H"),
W("A student hears that mangoes ripen faster when kept with a ripe banana. Plan a simple test to check this claim.", 4, "Take two similar raw mangoes (1). Keep one with a ripe banana in a paper bag and the other alone in a similar bag in the same place (1). Observe both daily and note when each ripens (1). Compare the results and conclude (1).", "H", wp=True),
W("Suppose your guess about a problem is correct on the first attempt. Does that mean you need not test it? Explain.", 3, "No. A guess becomes knowledge only after it has been tested (1). Without a test we cannot be sure it is correct and may be fooled by luck (1). Testing is an essential step of the method (1).", "H"),
W("Pooja says science is a journey and not a destination. Explain what she means, using the jigsaw puzzle idea.", 3, "There is no final end to science (1). Each new piece of knowledge leads to more questions (1) and so we keep learning for many years (1).", "H"),
W("Kabir wants to find out whether the ink of his pen runs out sooner when he writes with strong pressure. Which things should he keep the same and which should he change?", 3, "Change only the pressure (1). Keep the same type of pen, same paper and same amount of writing (1), so the test is fair and the result is reliable (1).", "H", wp=True),
W("The chapter says some of the most important discoveries came from unexpected places. Why should we keep our eyes open in all places?", 3, "Science is everywhere (1), from the kitchen to the playground to space (1). A curious person who observes keenly may notice something puzzling anywhere and begin an enquiry (1).", "H"),
W("A bus will not start. Describe how the scientific method can be used, with an observation, a guess and a test, and say what it means if the test fails.", 5, "Observe: the engine does not start (1). Guess: there is no diesel (1). Test: check the fuel gauge or tank (1). If the tank is full the guess is wrong (1), so make another guess such as a weak battery and test it; repeat until the cause is found (1).", "H", wp=True),
W("Compare a person who asks questions and tests them with one who accepts every claim without checking. Which is closer to a scientist and why?", 3, "The first is closer to a scientist (1). Scientists question and test claims using observation and experiment (1). Accepting claims without checking can lead to wrong ideas (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "1.9 The Scientific Method in Action: Worked Examples"),
 ("steps", [("Example 1 — A torch does not light", "**Observe:** the torch gives no light. **Question:** why? **Guess:** the cells are used up. **Test:** put in new cells. **Result:** it glows, so the guess was correct. If it had not glowed, the next guess could be a loose bulb, tested by tightening the bulb."),
  ("Example 2 — Milk turns sour quickly", "**Observe:** milk turns sour by evening in summer. **Guess:** heat makes it sour faster. **Test:** keep two cups of boiled milk, one in a cool place and one in a warm place. **Analyse:** the warm one sours first, so the guess is supported."),
  ("Example 3 — Plant dries up", "**Observe:** a potted plant is drying. **Guess 1:** it needs water. **Test:** water it for a few days. **Result:** no change, so guess 1 is wrong. **Guess 2:** too little sunlight. **Test:** move it near a window. Each wrong guess narrows down the cause.")]),
 ("note", "IMPORTANT", "While testing a guess, change **only one thing at a time**. If you change two things together, you cannot tell which one caused the result. This is called a **fair test**."),
 ("h2", "1.10 Common Mistakes and Misconceptions"),
 ("table", ["Wrong idea", "Correct idea"],
  [["Science is only memorising facts and formulae.", "Science is a way of thinking, observing and doing; it is a step-by-step process to find answers."],
   ["Only scientists in laboratories use the scientific method.", "Anyone who follows the method, such as a cook, mechanic or electrician, is working like a scientist."],
   ["A wrong guess means failure.", "A wrong guess is useful; it tells us what is not the cause and leads to a better guess."],
   ["A guess is true if it feels sensible.", "A guess becomes reliable only after it has been tested."],
   ["Science has answers to everything now.", "Science is like an unending jigsaw puzzle; every answer raises new questions."]]),
 ("note", "REMEMBER", "The word to remember for a testable guess is **hypothesis**. The method is: **observe, question, guess, test, analyse**."),
 ("h2", "1.11 Good Habits of a Science Learner"),
 ("ul", ["Keep a small notebook and write down what you observe, with date and place.",
  "Do not accept a claim only because many people say it; ask how we can check it.",
  "Note down results honestly, even when they are not what you expected.",
  "Repeat a test to be sure of the result.",
  "Discuss with friends and teachers; scientists across the world work in teams and share ideas.",
  "Be careful and follow safety rules when doing any activity; ask an elder when needed."]),
 ("h2", "1.12 Likely Questions: Higher Order"),
 ("qa", [("Why should we not accept a guess without testing it?", "A guess may be right or wrong; only a test or more observation can tell us which."),
  ("What can we do if our first guess is wrong?", "Make another guess and test it, and keep doing so until the cause is found."),
  ("How does the pen example show the whole scientific method?", "We observe that the pen stops, guess the ink is finished, test by opening the refill, and analyse the result; if ink is present we make a new guess."),
  ("Why does the book say science is like a jigsaw puzzle that never ends?", "Each discovery adds a piece but also raises new questions, so the puzzle keeps growing.")]),
]
CH["takeaways"] += ["A guess must be **tested**; a wrong guess still helps us make a better one.", "While testing, change **only one thing at a time** (fair test)."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
