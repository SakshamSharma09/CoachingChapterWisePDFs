from lib8 import *
META = dict(set_no=3)
R1 = dict(passage="""<p><b>The Stepwells of Rajasthan</b></p><p>In the dry lands of Rajasthan, where rain is scarce and rivers are few, people built stepwells known as <i>baoris</i> to store water. A stepwell is a deep well with a flight of steps leading down to the water. As the water level rose and fell with the seasons, people simply walked up or down the steps to reach it.</p><p>The stepwell at Abhaneri, near Jaipur, has 3,500 narrow steps arranged in perfect patterns and is nearly 20 metres deep. The air at the bottom is about five degrees cooler than outside, so stepwells also became shady meeting places where travellers rested and villagers gathered. Today many stepwells are neglected and filled with garbage, though a few are being restored to protect this wonderful heritage.</p>""",
 qs=[mc("What is a stepwell?", ["A tall tower for storing grain", "A deep well with steps leading to the water", "A canal in the desert", "A pond made by rainfall"], 1),
     mc("Why did the people of Rajasthan build stepwells?", ["To store water in a dry region", "To grow rice", "To worship rivers", "To keep animals"], 0),
     mc("Why were stepwells also popular meeting places?", ["They were close to the market", "The air at the bottom was cooler", "They had musicians", "They were free of insects"], 1),
     mc("The word 'neglected' in the passage means:", ["Looked after", "Decorated", "Not taken care of", "Newly built"], 2),
     sa("How did people reach water when the level changed with the seasons? Write one sentence.", "They simply walked up or down the steps to the water level.", 2),
     sa("What is being done to protect stepwells today?", "A few are being restored.", 1)])
R2 = dict(poster=poster("BOOKS ARE FRIENDS", "Annual Library Week · School Library", [("1", "Read for 20 minutes every day"), ("2", "Return books on time"), ("3", "Handle books with clean hands"), ("4", "Join the Book Club every Friday")]),
 passage="<p>A library is a treasure house of knowledge and imagination. Students who read regularly develop a better vocabulary, concentrate for longer and write with greater confidence. Yet many children spend hours on screens and rarely open a book. School libraries therefore organise reading weeks, book clubs and storytelling sessions to bring back the joy of reading.</p>",
 qs=[mc("According to the passage, what do regular readers develop?", ["Poor eyesight", "A better vocabulary", "A dislike for screens", "Less homework"], 1),
     mc("On which day does the Book Club meet?", ["Monday", "Wednesday", "Friday", "Sunday"], 2),
     mc("Which poster instruction helps keep the books in good condition?", ["Read for 20 minutes", "Handle books with clean hands", "Join the Book Club", "Visit on Friday"], 1),
     mc("What does 'treasure house' stand for in the passage?", ["A bank", "A place full of valuable things", "A school store", "A museum of coins"], 1),
     sa("Why do school libraries organise book clubs and storytelling sessions? Give two points.", "To bring back the joy of reading; to draw children away from screens; to improve vocabulary and confidence (any two).", 2),
     sa("Name one rule from the poster that you will follow and say why.", "Any rule with a sensible reason (1).", 1)])
G = [dict(k=4, ins="by choosing the most appropriate options.", items=[
  mc("The meeting was ______ off because of heavy rain.", ["called", "called out", "called up", "called on"], 0),
  mc("Please ______ the form carefully before you submit it.", ["fill in", "fill up on", "fill away", "fill after"], 0),
  mc("The thief ______ with the necklace.", ["made off", "made up", "made out", "made into"], 0),
  mc("We must ______ our plan until next week.", ["put off", "put on", "put in", "put to"], 0),
  mc("He ______ the idea that the world is flat.", ["gave up", "gave over", "gave out", "gave off"], 0)]),
 dict(k=4, ins="as indicated against each one of them.", items=[
  mc("Choose the correct conjunction: He was tired ______ he kept working.", ["so", "but", "because", "or"], 1),
  mc("Choose the correct pronoun: Ravi and ______ went to the museum.", ["me", "I", "myself", "mine"], 1),
  tf("'Neither of the boys are present' is grammatically correct.", False),
  fb("Choose the correct word. Each of the students ______ a book. (has / have)", "has", ["has", "have"]),
  mc("Choose the sentence in which the subject agrees with the verb.", ["The children plays outside.", "The news are shocking.", "The team is winning.", "Two kilometres are a long way."], 2)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("______ I borrow your pen, please?", ["Shall", "May", "Must", "Would to"], 1),
  fb("Fill in with a modal: You ______ not park here; it is a no-parking zone. (should / must)", "must"),
  tf("'Can' is used to show ability.", True),
  mc("Choose the sentence that shows advice.", ["You must be on time.", "You should drink more water.", "You can swim.", "You may go now."], 1)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("Choose the correct sentence.", ["Me and him went shopping.", "He and I went shopping.", "Him and me went shopping.", "Myself and he went shopping."], 1),
  fb("Fill in the blank with a pronoun. The students did ______ homework on time.", "their"),
  tf("'Which' can be used as a relative pronoun for things.", True),
  mc("Choose the conjunction: She stayed at home ______ she was ill.", ["because", "beside", "although is", "ever"], 0)])]
W = [[dict(q="As the Secretary of the Eco Club, write a notice in about 50 words for the notice board informing students about a tree-plantation drive on 2 January. Mention date, time, venue and what students should bring.", words="about 50 words", a="<b>SUNRISE PUBLIC SCHOOL</b><br><b>NOTICE</b> &nbsp; 20 December 2026<br><b>Tree-Plantation Drive</b><br>The Eco Club will hold a tree-plantation drive on 2 January 2027 at 8 a.m. in the school garden. Interested students of Classes VI–VIII should bring gloves and a water bottle, and report to the Eco Club room by 7.45 a.m.<br>Secretary, Eco Club", mk="Format 2; content 3; language 1."),
     dict(q="Write a diary entry in 100–120 words about your visit to a historical monument (fort, palace or stepwell). Mention what you saw, learned and felt.", words="100–120 words", a="Sunday, 20 December 2026 · 9 p.m.<br>Dear Diary,<br>Today my family and I visited Amer Fort. We reached early and climbed the winding path to the palace. The mirror-work of Sheesh Mahal sparkled like a sky full of stars. The guide told us how the Rajput kings once ruled from there and how the fort used clever systems to store water. I was amazed at the skill of the builders. I felt proud of our heritage and promised myself to read more about our history.<br>Good night!", mk="Format 1; content 3; fluency 1; accuracy 1.")],
    [dict(q="You are Meera/Manav of 12 Gandhi Road, Jaipur. Write a letter to the Station Master complaining about the poor condition of the railway platform at your local station. Suggest improvements. (100–120 words)", words="100–120 words", a="12 Gandhi Road<br>Jaipur<br>21 December 2026<br>The Station Master<br>Jaipur Junction<br>Subject: Poor condition of the platform<br>Sir,<br>I travel often by train and have noticed that the platform is dirty, dimly lit and without enough seats. Waste bins overflow and drinking water taps do not work. Elderly passengers find it very difficult to wait. I request you to arrange regular cleaning, repair the taps, install proper lights and put more seats. Kindly look into this matter at the earliest.<br>Yours faithfully<br>Meera", mk="Format 2; content 2; expression 2."),
     dict(q="Write a letter to your friend living in another city, describing how you celebrated the festival of Diwali this year. (100–120 words)", words="100–120 words", a="45 Sector 7<br>Jaipur<br>21 December 2026<br>Dear Kabir,<br>I hope you are well. I am writing to tell you about my Diwali. We cleaned and decorated the house with rangoli and diyas. In the evening we performed the Lakshmi puja and exchanged sweets with the neighbours. My cousins visited and we burst only a few green crackers. This year I also visited an orphanage with my parents to distribute sweets. It made the festival more meaningful. I missed you very much. Do come next year.<br>Yours lovingly<br>Aryan", mk="Format 2; content 2; expression 2.")]]
L = dict(q6=dict(passage="Tenali Ramakrishna was a poet and court jester at the court of King Krishnadevaraya of Vijayanagara. His wit was famous. When the king once asked him to bring the 'most useful thing', Tenali brought a simple bowl of water; he explained that no life could exist without it. The king laughed and rewarded him. Tenali's jokes always carried a lesson and he never used his cleverness to hurt anyone innocent.",
  qs=[fb("Tenali Ramakrishna was a court ______ at Vijayanagara. (jester / soldier)", "jester", ["jester", "soldier"]),
      tf("Tenali brought a bowl of water as the most useful thing.", True),
      mc("Why did Tenali choose water?", ["It was cheap", "No life could exist without it", "The king was thirsty", "It was sacred only"], 1),
      mc("Tenali's jokes always carried:", ["a danger", "a lesson", "an insult", "a prize"], 1),
      sa("What do you learn about Tenali's character from the extract?", "Clever, witty, kind, wise (any suitable trait).", 1)]),
 q7=dict(poem="<i>The moon peeps through the window pane<br>And silvers all the room;<br>The night wind sings a soft refrain<br>And chases off the gloom.</i>",
  qs=[sa("What does the moon do?", "It peeps through the window and silvers the room (2).", 2), sa("What does the night wind do?", "It sings a soft refrain and chases off the gloom (2).", 2), sa("Pick out a pair of rhyming words from the extract.", "room–gloom, or pane–refrain (2).", 2)]),
 q8=[sa("What qualities of Major Somnath Sharma would you like to develop in yourself? Give reasons.", "Courage, sense of duty, leadership, selflessness; any three with reasons.", 3),
     sa("How did Verghese Kurien's work change the lives of farmers in Kaira?", "Cooperative gave fair price; removed middlemen; increased income; Amul/Operation Flood (any three).", 3),
     sa("Describe one incident that shows Tenali's presence of mind.", "Any story such as the cats-and-milk or bowl-of-water incident, with a clear description (3).", 3),
     sa("How does the poet make us feel sympathy for the old woman in 'Somebody's Mother'?", "Description of her feeble, aged, anxious condition; the noisy crowd passing; the single boy who helps; the poet's gentle tone (any three).", 3),
     sa("Why is helping others an important value? Support your answer with examples from any two lessons.", "Selfless service from Kurien and the boy in Somebody's Mother; society benefits (3).", 3)])
SET = dict(R1=R1, R2=R2, G=G, W=W, L=L)
