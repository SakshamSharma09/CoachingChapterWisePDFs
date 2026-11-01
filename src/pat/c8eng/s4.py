from lib8 import *
META = dict(set_no=4)
R1 = dict(passage="""<p><b>Chandrayaan-3: India Touches the Moon</b></p><p>On 23 August 2023, India became the first country to land a spacecraft near the Moon's south pole. The lander, named Vikram, touched down gently after a tense final descent of nearly twenty minutes, while scientists at ISRO watched anxiously. Soon after, the rover Pragyan rolled out to study the lunar soil.</p><p>The mission cost far less than similar missions of other countries, showing that careful planning and local engineering can achieve great results. Young students across the country celebrated by drawing rockets and writing poems, and many declared that they too wished to become scientists.</p>""",
 qs=[mc("What was the name of the lander of Chandrayaan-3?", ["Pragyan", "Vikram", "Aryabhata", "Mangal"], 1),
     mc("What did the rover Pragyan do?", ["Landed the spacecraft", "Studied the lunar soil", "Photographed Earth", "Launched the rocket"], 1),
     mc("What does the low cost of the mission show?", ["The mission was careless", "Careful planning and local engineering can succeed", "Rockets are cheap to build", "Other countries did not try"], 1),
     mc("The word 'anxiously' in the passage means:", ["Happily", "With worry and nervousness", "Lazily", "Proudly"], 1),
     sa("How did students across the country celebrate the success? Mention two ways.", "By drawing rockets; writing poems; declaring wish to become scientists (any two).", 2),
     sa("Why was the final descent of the lander 'tense'?", "Because a small mistake could ruin the mission / scientists were anxious about the landing.", 1)])
R2 = dict(poster=poster("SAY NO TO PLASTIC", "Plastic-Free Campus Drive · Eco Club", [("1", "Carry a cloth or jute bag"), ("2", "Use a steel bottle and tiffin"), ("3", "Refuse single-use plastic"), ("4", "Segregate dry and wet waste")]),
 passage="<p>Plastic bags and bottles take hundreds of years to break down. They choke drains, harm animals that mistake them for food and pollute rivers and oceans. Small changes in daily habits, like carrying our own bags and bottles, can reduce the amount of plastic that reaches landfills. Schools are urging students to take a pledge and spread the message at home.</p>",
 qs=[mc("What happens to plastic bags in drains?", ["They dissolve", "They choke the drains", "They help water flow", "They float away"], 1),
     mc("Which poster instruction deals with food and lunch?", ["Carry a jute bag", "Use a steel bottle and tiffin", "Refuse single-use plastic", "Segregate waste"], 1),
     mc("Why do animals suffer because of plastic?", ["They like plastic toys", "They mistake it for food", "It keeps them warm", "It makes them sleepy"], 1),
     mc("What is the purpose of the campaign?", ["To sell plastic goods", "To reduce plastic use", "To cut trees", "To build roads"], 1),
     sa("How can students spread the message at home? Suggest two ways.", "Take a pledge; tell family to use cloth bags; segregate waste at home; avoid plastic packaging (any two).", 2),
     sa("Name any one harm of plastic mentioned in the passage.", "Chokes drains / harms animals / pollutes rivers and oceans.", 1)])
G = [dict(k=4, ins="by choosing the most appropriate options.", items=[
  mc("The teacher asked us to ______ the poem by heart.", ["learn", "learned off", "learn off", "learning"], 0),
  mc("He ______ a bad cold last week and missed school.", ["caught", "catch", "catches", "catching"], 0),
  mc("Please ______ the lights when you leave.", ["switch off", "switch after", "switch of", "switch through"], 0),
  mc("The students ______ for the picnic when it began to rain.", ["were leaving", "leaves", "leave", "have left"], 0),
  mc("The old man ______ at the door for ten minutes before it opened.", ["has stood", "had been standing", "stands", "will stand"], 1)]),
 dict(k=4, ins="as indicated against each one of them.", items=[
  mc("Choose the correct comparative: Mount Everest is ______ than K2.", ["high", "higher", "highest", "most high"], 1),
  mc("Choose the superlative: She is the ______ girl in the class.", ["tall", "taller", "tallest", "more tall"], 2),
  tf("'Good, better, best' shows degrees of comparison.", True),
  fb("Fill in the blank with the correct degree. This is the ______ (beautiful) place I have ever seen.", "most beautiful"),
  mc("Choose the correct sentence.", ["He is more taller than Raj.", "He is taller than Raj.", "He is tallest than Raj.", "He is tall than Raj."], 1)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("Choose the correct past tense: She ______ the exam yesterday.", ["pass", "passed", "passes", "passing"], 1),
  fb("Fill in with the past tense of 'go'. They ______ to Mumbai last summer.", "went"),
  tf("'Had eaten' is the past perfect tense.", True),
  mc("When I reached the station, the train ______.", ["left", "had left", "leaves", "has left"], 1)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("Identify the voice: The cake was baked by my mother.", ["Active", "Passive", "Neither", "Both"], 1),
  fb("Change into passive voice. Ravi wrote the letter. → The letter ______ by Ravi.", "was written"),
  tf("'The boy kicked the ball' is in the passive voice.", False),
  mc("Change into active: The window was broken by the boy.", ["The boy broke the window.", "The boy breaks the window.", "The window broke the boy.", "The boy had broken the window."], 0)])]
W = [[dict(q="Your school is organising a Science Exhibition on 10 January. Write a notice in about 50 words inviting students to participate and giving the last date for registration. You are the Science Club Secretary.", words="about 50 words", a="<b>MODERN PUBLIC SCHOOL</b><br><b>NOTICE</b> &nbsp; 1 January 2027<br><b>Science Exhibition</b><br>A Science Exhibition will be held on 10 January 2027 in the school hall at 10 a.m. Students of Classes VI–VIII may submit working models or charts. Names should be given to the Science Club Secretary by 6 January.<br>Secretary, Science Club", mk="Format 2; content 3; language 1."),
     dict(q="Complete a short story in 100–120 words that begins: 'The lights went out suddenly and the whole house fell silent…'", words="100–120 words", a="…Aarav froze. Somewhere upstairs, a floorboard creaked. He took a deep breath and reached for the torch kept on the shelf. Its beam shook as he climbed the stairs. In the study, a curtain was fluttering and, in its shadow, two yellow eyes glowed. Aarav's heart pounded; then a small meow broke the silence. It was the neighbour's kitten that had slipped in through the open window. Aarav laughed with relief, picked it up and carried it down, realising that the dark often makes small things look scary.", mk="Content 3; organisation and fluency 2; accuracy 1.")],
    [dict(q="Write a letter to your Principal in 100–120 words requesting her to arrange a career-counselling session for the students of Class VIII. You are Neha/Nikhil, the Class Monitor.", words="100–120 words", a="Class VIII-B<br>Sunrise Public School<br>Jaipur<br>3 January 2027<br>The Principal<br>Sunrise Public School<br>Subject: Request for a career-counselling session<br>Respected Madam,<br>On behalf of the students of Class VIII, I request you to arrange a career-counselling session. Many of us are unsure about the subjects to choose in Class IX and about future careers. A counsellor can guide us about options, skills and examinations. We shall be thankful if the session is held during the activity period.<br>Yours obediently<br>Neha, Class Monitor", mk="Format 2; content 2; expression 2."),
     dict(q="You saw an advertisement for a second-hand bicycle. Write a letter to the seller in 100–120 words enquiring about its age, condition, price and the possibility of a test ride.", words="100–120 words", a="16 Lal Kothi<br>Jaipur<br>3 January 2027<br>The Seller<br>Subject: Enquiry about second-hand bicycle<br>Sir,<br>I read your advertisement about the second-hand bicycle in today's newspaper and am interested in buying it. Kindly inform me how old it is, what its present condition is and the lowest price you will accept. Please let me know if I may take a short test ride. I will visit as per your convenience.<br>Yours faithfully<br>Rohan", mk="Format 2; content 2; expression 2.")]]
L = dict(q6=dict(passage="Bibha Chowdhuri, an Indian physicist born in Kolkata in 1913, was among the first women scientists of India. She studied cosmic rays, the invisible particles that reach the earth from space. Working with limited equipment, she made discoveries that earned her international recognition. Though she faced the challenge of being a woman in a male-dominated field, she followed her curiosity and never gave up.",
  qs=[fb("Bibha Chowdhuri was a ______ . (physicist / poet)", "physicist", ["physicist", "poet"]),
      tf("She studied cosmic rays.", True),
      mc("What challenge did she face?", ["Lack of interest", "Being a woman in a male-dominated field", "No school", "Wars"], 1),
      mc("The passage shows that she was:", ["lazy", "curious and determined", "shy", "careless"], 1),
      sa("What can we learn from her life?", "Curiosity and determination can overcome obstacles (any suitable answer).", 1)]),
 q7=dict(poem="<i>The river runs from hill to sea,<br>It sings of how it longs to be<br>A part of something wide and blue,<br>And I would like to follow too.</i>",
  qs=[sa("Where does the river run from and to?", "From hill to sea (2).", 2), sa("What does the river long to be?", "A part of something wide and blue (2).", 2), sa("Which word rhymes with 'blue'?", "too (2).", 2)]),
 q8=[sa("How does 'Somebody's Mother' teach us kindness? Explain in about 50 words.", "Boys ignore her; one boy helps; his act is praised; lesson of kindness and respect for elders (3).", 3),
     sa("Why is Major Somnath Sharma remembered as a hero? Give three reasons.", "Led his men; fought bravely though wounded; sacrificed life; held the airfield (any three).", 3),
     sa("What challenges did Verghese Kurien face in his mission? How did he overcome them?", "Middlemen, opposition, lack of resources; overcame with cooperative idea, perseverance, teamwork (3).", 3),
     sa("In what ways was Tenali Ramakrishna different from the other courtiers?", "Wit; independence; honesty; used humour to teach; loved by common people (3).", 3),
     sa("If you could meet any one of the personalities you studied, whom would you meet and why? Write in 40–50 words.", "Any personality with a reasoned answer; content 2, language 1.", 3)])
SET = dict(R1=R1, R2=R2, G=G, W=W, L=L)
