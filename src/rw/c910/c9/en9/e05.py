from eng9_lib import mcq, Q, X

NAME = "The World of Limitless Possibilities; Nine Gold Medals"
MCQ = [
 mcq("The chapter 'The World of Limitless Possibilities' is mainly about:", ["Paralympics and para-athletes", "mountaineering", "space travel", "cooking"], "a", "Interview with Dr. Deepa Malik"),
 mcq("India first took part in the Paralympics in:", ["1968", "1948", "2008", "1992"], "a", "Debut year"),
 mcq("India's first Paralympic medal was won in:", ["swimming", "archery", "shot-put", "athletics"], "a", "1972"),
 mcq("Dr. Deepa Malik was diagnosed with a spinal tumour at the age of:", ["29", "19", "39", "9"], "a", "Surgery left her paralysed below waist"),
 mcq("After the surgery she was told she would:", ["be bound to a wheelchair", "walk normally", "need no treatment", "swim again immediately"], "a", "Doctors' verdict"),
 mcq("She chose to turn her life into:", ["a world of limitless possibilities", "a quiet retirement", "a life of regret", "a business"], "a", "Her decision"),
 mcq("Her first successful Paralympic event was:", ["shot-put at Rio 2016", "swimming at Tokyo", "javelin in Athens", "archery in London"], "a", "Silver medal"),
 mcq("The silver medal she won was in the year:", ["2016", "2012", "2020", "2008"], "a", "Rio Paralympic Games"),
 mcq("She believes that physical limitations:", ["do not define one's potential", "decide one's future", "end sporting careers", "are a sign of failure"], "a", "'Ability beyond disability'"),
 mcq("The greatest challenge she mentions was:", ["societal perceptions", "lack of money", "weather", "language"], "a", "People underestimated her"),
 mcq("According to her, sports help to:", ["challenge stereotypes", "promote rivalry", "end education", "avoid hard work"], "a", "Break preconceived notions"),
 mcq("Her advice to people facing setbacks is to treat each setback as:", ["an opportunity to prove strength", "a punishment", "a reason to quit", "luck"], "a", "Disability is unique strength"),
 mcq("The poem 'Nine Gold Medals' is set at:", ["a race for athletes", "a school classroom", "a farm", "a market"], "a", "Special Olympics"),
 mcq("In the race the youngest runner:", ["stumbled and fell", "won easily", "refused to run", "left early"], "a", "Triggers the kindness"),
 mcq("The other eight runners:", ["turned back to help him", "ran ahead", "laughed at him", "complained"], "a", "Sportsmanship"),
 mcq("The central message of the poem is:", ["compassion matters more than winning", "winning is everything", "cheating pays", "run alone"], "a", "Nine gold medals"),
]
EXT = [
 X("Dr. Malik says she had two choices after her surgery: to waste her life in regret or to make it a world of endless chances. Since she loved sports and had been a swimmer, she turned to para-athletics. Her breakthrough came at the Rio Paralympics where she took a silver medal in the shot-put.",
   [("What two choices did she face?", "To waste life in regret or to build a world of possibilities."),
    ("Which sport did she love earlier?", "Swimming."),
    ("Which event brought her a silver medal?", "Shot-put at Rio 2016."),
    ("What does her decision show about her?", "Courage and a positive attitude.")]),
 X("The interviewer notes that Dr. Malik has won many awards and is the first Indian woman Paralympic medallist. She replies that these honours show that physical limits do not decide anyone's potential. She supports the idea of 'ability beyond disability' and says the Paralympics helped her push boundaries.",
   [("Who is being interviewed?", "Dr. Deepa Malik."),
    ("What does she say about physical limitations?", "They do not define potential."),
    ("What idea does she support?", "Ability beyond disability."),
    ("Which word shows that she is grateful?", "Appreciate (or honoured).")]),
 X("A young runner fell at the start of a race and cried out in disappointment. The eight others stopped, turned back and helped him to his feet. All nine then joined hands and walked to the finish line together, and the crowd rose in applause.",
   [("What happened to the youngest runner?", "He stumbled and fell."),
    ("How did the other runners respond?", "They went back and helped him."),
    ("How did they finish the race?", "Holding hands together."),
    ("What does the incident show?", "Sportsmanship and kindness.")]),
]
SA = [
 Q("What choice did Deepa Malik make after her surgery?", "She chose not to waste life in regret but to turn it into a world of limitless possibilities through sport.", "2"),
 Q("What does 'ability beyond disability' mean?", "A person's talent and strength go beyond physical limits; disability does not decide potential.", "2"),
 Q("How do Paralympics change attitudes?", "The strength, skill and spirit of para-athletes break down preconceived notions about disability.", "2"),
 Q("Mention two ways in which Dr. Malik supports others.", "She empowers women through outdoor sports, helps persons from poor backgrounds with equipment and organises awareness sessions.", "2"),
 Q("Why did the eight runners go back for the fallen boy?", "They valued kindness and fairness above winning.", "2"),
 Q("Why does the poem say each runner got a gold medal?", "All finished together, so each won something greater than a race: compassion and unity.", "2"),
]
LA = [
 Q("How did Deepa Malik overcome adversity? Give two points.", "She refused to give in to regret, used her love of sport, trained for para-athletics, relied on family support and mental strength, and won medals.", "3"),
 Q("What challenges did Dr. Malik face?", "Societal perceptions and underestimation, physical limitations after paralysis, and the need for resilience and fortitude.", "3"),
 Q("Why is Dr. Malik an inspiration?", "First Indian woman Paralympic medallist; many awards; advocates inclusion and uses her influence to help others.", "3"),
 Q("What role does sport play in changing stereotypes?", "It showcases strength, skill and competitive spirit, breaking prejudice and building inclusiveness.", "3"),
 Q("What advice does Dr. Malik give to young people?", "Treat setbacks as chances, build a support system, believe in oneself, and let one's journey inspire others.", "3"),
 Q("Describe the incident in 'Nine Gold Medals'.", "A race begins; the youngest runner falls; the others return, lift him, and all cross the line hand in hand.", "3"),
 Q("What does the poem teach us about winning?", "True victory lies in care for others, teamwork and sportsmanship rather than medals alone.", "3"),
 Q("How does the poet create a joyful ending?", "Through the image of nine hand-holding winners, the standing ovation and beaming faces.", "3"),
]
