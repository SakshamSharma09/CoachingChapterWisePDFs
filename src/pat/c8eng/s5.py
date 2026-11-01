from lib8 import *
META = dict(set_no=5)
R1 = dict(passage="""<p><b>Millets: The Forgotten Grains</b></p><p>Before wheat and rice became common in Indian kitchens, our ancestors ate millets like bajra, jowar and ragi. These small grains grow easily in dry regions with very little water, and they are rich in fibre, iron and calcium. In Rajasthan, bajra rotis with ghee are still a winter favourite.</p><p>In recent years doctors and farmers have rediscovered millets. They help control weight and blood sugar, and they need far fewer chemicals than other crops. The United Nations declared 2023 the International Year of Millets, encouraging the world to value these humble grains again.</p>""",
 qs=[mc("Which of the following is a millet?", ["Wheat", "Rice", "Bajra", "Maize oil"], 2),
     mc("Why do millets grow well in dry regions?", ["They need very little water", "They need heavy rain", "They need cold weather", "They grow only in water"], 0),
     mc("Which year was declared the International Year of Millets?", ["2019", "2021", "2023", "2025"], 2),
     mc("The word 'humble' in the passage means:", ["Proud", "Simple and ordinary", "Costly", "Colourful"], 1),
     sa("Mention two benefits of millets according to the passage.", "Rich in fibre, iron and calcium; help control weight and blood sugar; need fewer chemicals (any two).", 2),
     sa("What is a winter favourite in Rajasthan?", "Bajra rotis with ghee.", 1)])
R2 = dict(poster=poster("EAT HEALTHY, STAY HEALTHY", "School Health Week · 7–13 April", [("1", "Eat fresh fruits and vegetables daily"), ("2", "Drink 8 glasses of water"), ("3", "Avoid junk food and cold drinks"), ("4", "Play outdoors for one hour")]),
 passage="<p>Many students bring packets of chips and sugary drinks to school instead of home-cooked food. Such foods give quick energy but little nutrition and can lead to obesity and tiredness. Health experts recommend a balanced diet with grains, pulses, fruits and vegetables along with regular exercise. Small steps taken today can keep us fit for life.</p>",
 qs=[mc("What do chips and sugary drinks lack?", ["Salt", "Nutrition", "Taste", "Packaging"], 1),
     mc("How many glasses of water does the poster suggest?", ["4", "6", "8", "10"], 2),
     mc("Which poster rule matches the idea of exercise in the passage?", ["Drink water", "Play outdoors for one hour", "Eat fruits", "Avoid cold drinks"], 1),
     mc("The expression 'balanced diet' means:", ["Eating only sweets", "A variety of nutritious food in right amounts", "Eating once a day", "Eating only vegetables"], 1),
     sa("Why is junk food harmful? Give two reasons.", "Little nutrition; leads to obesity and tiredness (2).", 2),
     sa("Who recommends a balanced diet?", "Health experts.", 1)])
G = [dict(k=4, ins="by choosing the most appropriate options.", items=[
  mc("He is a very honest man; you can always ______ him.", ["rely on", "rely at", "rely for", "rely to"], 0),
  mc("The children are looking ______ to the holidays.", ["forward", "back", "up", "after"], 0),
  mc("I ran ______ my old friend in the market.", ["into", "off", "away", "down"], 0),
  mc("The chairman ______ the meeting at 5 p.m.", ["wound up", "wound off", "wound over", "wound out"], 0),
  mc("She ______ her younger brother while her mother was out.", ["looked after", "looked at", "looked for", "looked into"], 0)]),
 dict(k=4, ins="as indicated against each one of them.", items=[
  mc("Choose the plural of 'child':", ["childs", "children", "childes", "childrens"], 1),
  mc("Choose the plural: 'The ______ are playing in the field.'", ["sheep", "sheeps", "sheepes", "sheepe"], 0),
  tf("'Furniture' is an uncountable noun.", True),
  fb("Fill in the blank with the plural of 'knife'. The cook sharpened all the ______.", "knives"),
  mc("Identify the collective noun: <i>A flock of birds flew over the lake.</i>", ["flock", "birds", "lake", "flew"], 0)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("Choose the correct adjective: There is ______ milk in the glass.", ["a few", "many", "little", "a number"], 2),
  fb("Fill in the blank with the right form. He drank ______ (less / fewer) water than usual.", "less"),
  tf("'Beautiful' is an adjective.", True),
  mc("Identify the adjective: <i>She wore a red dress.</i>", ["She", "wore", "red", "dress"], 2)]),
 dict(k=3, ins="as indicated against each one of them.", items=[
  mc("Choose the correct preposition: The book is ______ the table.", ["on", "in", "at", "to"], 0),
  fb("Fill in the blank. She is good ______ mathematics. (at / in / on)", "at"),
  tf("'Between' is used for two persons or things.", True),
  mc("Choose the correct sentence.", ["He is senior than me.", "He is senior to me.", "He is senior from me.", "He is senior at me."], 1)])]
W = [[dict(q="Your school is celebrating Sports Day on 15 February. Write a notice in about 50 words informing students about the events, date, time and venue. You are Aman/Anita, the Sports Captain.", words="about 50 words", a="<b>DELHI PUBLIC SCHOOL, JAIPUR</b><br><b>NOTICE</b> &nbsp; 5 February 2027<br><b>Annual Sports Day</b><br>The Annual Sports Day will be held on 15 February 2027 at 9 a.m. at the school ground. Races, relay, long jump and tug of war will be conducted. Students should report in sports uniform by 8.30 a.m.<br>Sports Captain", mk="Format 2; content 3; language 1."),
     dict(q="Write a short story of 100–120 words with the title 'The Honest Boy'. Include a clear beginning, middle and end, and a moral.", words="100–120 words", a="Gopal was a poor boy who sold flowers near a temple. One morning he found a purse full of money lying on the road. Though he needed money badly, he went to the temple office and handed it over. Soon a rich merchant came looking for his purse and was overjoyed. He offered Gopal a reward, but Gopal accepted only the cost of a few flowers. Impressed, the merchant paid for Gopal's education. <b>Moral:</b> Honesty is always rewarded.", mk="Content 3; organisation and fluency 2; accuracy 1.")],
    [dict(q="You are Pooja/Pankaj. Write a letter to the Editor of 'The Rajasthan Times' in 100–120 words about the increasing cases of littering in public parks and suggest remedies.", words="100–120 words", a="9 Shyam Nagar<br>Jaipur<br>6 February 2027<br>The Editor<br>The Rajasthan Times<br>Jaipur<br>Subject: Littering in public parks<br>Sir,<br>Through your newspaper I wish to draw attention to the growing problem of littering in our parks. Plastic wrappers, bottles and leftover food are strewn on the grass and the benches. This spoils the beauty of the parks and harms birds. The authorities should place more dustbins, impose fines on offenders and run awareness campaigns in schools.<br>Yours truly<br>Pooja", mk="Format 2; content 2; expression 2."),
     dict(q="Write a letter to your cousin congratulating him/her on winning a state-level debate competition. (100–120 words)", words="100–120 words", a="25 Model Town<br>Jaipur<br>6 February 2027<br>Dear Sameer,<br>I was delighted to hear that you won the state-level debate competition. Congratulations! I know how hard you worked, practising every evening and reading newspapers. Your confidence and clear thinking have won you this prize. The whole family is proud of you. I hope you will teach me some tips when we meet. Do share the video of your speech.<br>With love<br>Anita", mk="Format 2; content 2; expression 2.")]]
L = dict(q6=dict(passage="In 'Somebody's Mother', an old woman stands at the edge of a busy street, waiting to cross. Boys and girls rush past her, laughing and shouting, none stopping to help. Finally a boy offers his arm and guides her safely across. She blesses him and the poet says that someone, somewhere, will bless his own mother for his kindness.",
  qs=[fb("The old woman wanted to ______ the street. (cross / paint)", "cross", ["cross", "paint"]),
      tf("Many children stopped to help her.", False),
      mc("Who helped the old woman?", ["A girl", "A boy", "A policeman", "A teacher"], 1),
      mc("What does the poet hope for the boy's mother?", ["That she will be blessed for her son's kindness", "That she will be rich", "That she will travel", "That she will be famous"], 0),
      sa("What lesson does the extract give?", "Be kind and help the elderly (any suitable lesson).", 1)]),
 q7=dict(poem="<i>The morning bird begins to sing,<br>It wakes the world with wing on wing;<br>The flowers open, one by one,<br>To welcome in the rising sun.</i>",
  qs=[sa("What does the morning bird do?", "It sings and wakes the world (2).", 2), sa("What do the flowers do?", "They open one by one to welcome the sun (2).", 2), sa("Pick out a pair of rhyming words.", "sing–wing, or one–sun (2).", 2)]),
 q8=[sa("What does the story of Major Somnath Sharma teach us about duty?", "Duty before self; courage in danger; loyalty to the nation (3).", 3),
     sa("'Dreams come true through determination.' How is this illustrated in Kurien's life?", "Dream of helping farmers; continued despite hurdles; created Amul and Operation Flood (3).", 3),
     sa("How did Tenali Ramakrishna use humour to solve problems? Give an example.", "Humour made people listen; example of an incident, e.g., clever reply to the king (3).", 3),
     sa("What contrast do you see between the old woman and the crowd in 'Somebody's Mother'?", "Frail, alone vs strong, careless and hurried; indifference vs kindness (3).", 3),
     sa("Which of the lessons you have studied this year did you like best and why? Answer in 40–50 words.", "Any lesson with a reasoned answer; content 2, language 1.", 3)])
SET = dict(R1=R1, R2=R2, G=G, W=W, L=L)
