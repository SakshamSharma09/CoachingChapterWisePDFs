from lib_eng import *
S = dict(set_no=5)
p1 = [
 "In a small workshop in Assam, a craftsman splits a green bamboo pole into thin strips and begins to weave a basket. His hands move without hesitation, for the skill was passed down from his grandfather. Bamboo, often called the 'poor man's timber', has been used for centuries in India to build houses, make furniture, carry water and fish in the rivers, and in many villages a family's wealth was once counted by the size of its bamboo grove. Today, this humble grass is being seen in a new light as a material for a greener future. Architects have used it to build graceful pavilions and even whole schools, showing that something so ordinary can be both strong and beautiful.",
 "The qualities of bamboo explain this change. It is one of the fastest-growing plants on earth, and some varieties grow nearly a metre in a single day. Unlike trees, it does not need to be replanted after cutting, since new shoots arise from the same roots. Its roots also hold the soil together, which prevents landslides on slopes, and it absorbs large amounts of carbon dioxide while giving out more oxygen than many trees of the same size.",
 "These advantages have encouraged designers to use bamboo in unexpected ways. Bamboo flooring, toothbrushes, water bottles and even bicycle frames are now sold in cities around the world, and exporters report that orders rise every year. In rural areas, women's groups produce baskets, lamps and mats that are bought by shops and online buyers, and their income allows them to send their children to school.",
 "Still, the industry faces many difficulties. Old laws classified bamboo as a tree, which made it hard to cut and transport it, though the rule has been relaxed. Artisans often lack modern tools and training, and they depend on traders who pay low prices. Cheap plastic products also compete with handmade goods, since they cost less and are easier to produce in large numbers. Many young people in craft villages therefore leave for factory jobs in towns, and the skills of generations are in danger of being lost.",
 "To protect this craft, experts recommend training centres, fair-trade markets and better designs that appeal to young buyers. When people choose a bamboo product over a plastic one, they support both the forest and the family who made it. In this way, a simple grass can strengthen livelihoods and the environment together. The challenge for the coming years is to make sure that the benefits reach the weaver in the village and not only the businessman in the city.",
]
p1parts = [
 P("Why is bamboo called the 'poor man's timber'? (Paragraph 1)", 1, "Because it is cheap and has been used by ordinary people to make many things."),
 P("According to Paragraph 2, bamboo helps the environment in all of the following ways EXCEPT", 1, "Nothing is said about bamboo producing minerals.", ["holding the soil together", "absorbing carbon dioxide", "growing quickly without replanting", "providing minerals to the soil"], 'd'),
 P("Complete the following by selecting the correct option from those in the brackets: Bamboo grows back from its roots after cutting, which makes it a __________ resource. (renewable / scarce) (Paragraph 2)", 1, "renewable"),
 P("Select the option that is TRUE according to Paragraph 3.", 1, "Women's groups earn income from bamboo products.", ["Bamboo is used only in villages.", "Women's groups earn income from bamboo products.", "Plastic bottles are replacing bamboo.", "Bamboo bicycles are not sold anywhere."], 'b'),
 P("Complete the analogy by selecting the correct option.<br>Training centre : Skill :: Fair-trade market : ______", 1, "Fair price.", ["Fair price", "Waste"], 'a'),
 P("Why is it difficult for artisans to compete with plastic goods? (Paragraph 4)", 2, "Plastic products cost less and are easier to make in large numbers (1); artisans lack modern tools and training and depend on traders who pay low prices (1)."),
 P("What are the main ideas of Paragraph 2 and Paragraph 4?<br>i. Bamboo has several special qualities.<br>ii. The bamboo industry faces difficulties.<br>iii. Bamboo is harmful to the soil.<br>iv. Plastic should be banned.<br>v. Artisans are well paid.", 1, "Paragraph 2 — i; Paragraph 4 — ii.", None, 'c', table(["Option", "Main idea of Paragraph 2", "Main idea of Paragraph 4"], [["A", "iii", "iv"], ["B", "ii", "i"], ["C", "i", "ii"], ["D", "v", "iii"]])),
 P("How does choosing a bamboo product 'support both the forest and the family'? (Paragraph 5)", 2, "It encourages a renewable, eco-friendly material instead of plastic (1); it gives income to the artisan family who made it (1)."),
]
p2 = [
 "A survey of 600 students from Classes 8 to 12 studied their participation in sports. The findings were encouraging. About 65% of the students (390) said that they play a sport or exercise at least three times a week, while the other 35% (210) do so less often. Among all the students, cricket was the most popular game with 36% (216), followed by badminton with 20% (120) and football with 14% (84). Surprisingly, only 7% (42) took part in athletics, even though the school has a well-maintained track.",
 "The researchers also asked about stress. Among the 390 active students, 70% (273) said that they felt calm and less stressed during examinations, whereas only 84 of the 210 less active students (40%) said the same. Moreover, 150 of the 390 active students (about 38%) were girls, which was lower than the girls' share in the school, pointing to a need for more opportunities for them.",
 "Coaches suggest that schools should offer a wider range of games, arrange mixed teams and keep the playground open for an hour after classes. Regular physical activity, they say, builds fitness, teamwork and the confidence to face challenges in the classroom. A few students added that games helped them make friends from other classes, and gave them a happy break from long hours of study.",
]
p2parts = [
 P("Why does the author describe the findings as 'encouraging'? (Paragraph 1)", 1, "Because a majority (65%) play or exercise at least three times a week."),
 P("Complete the following by selecting the correct option from the brackets. The most popular game among the students is __________. (cricket / football) (Paragraph 1)", 1, "cricket"),
 P("Select the option that is TRUE according to Paragraph 2.", 1, "Active students were more likely to feel calm during examinations.", ["Less active students felt calmer.", "Active students were more likely to feel calm during examinations.", "Most active students were girls.", "Stress was not studied."], 'b'),
 P("Which of the following is the best meaning of 'opportunities' as used in Paragraph 2?", 1, "Chances to take part.", ["Penalties", "Chances to take part", "Punishments", "Obstacles"], 'b'),
 P("Complete the analogy by selecting the correct option.<br>Mixed teams : Cooperation :: Coach : ______", 1, "Guidance.", ["Guidance", "Confusion"], 'a'),
 P("Complete the following appropriately. 120 students play badminton, which is ____ % of the 600 students. (Paragraph 1)", 1, "20"),
 P("What do the figures 70% and 40% in Paragraph 2 indicate?", 1, "Active students reported lower stress than less active ones."),
 P("Why do the researchers say there is a need for more opportunities for girls? (Paragraph 2)", 1, "Because girls form a smaller share of active students than of the school."),
 P("According to the coaches, how does regular physical activity help students? Mention any two benefits. (Paragraph 3)", 2, "It builds fitness, teamwork and confidence (any two) (1+1)."),
]
S['passages'] = [dict(paras=p1, parts=p1parts), dict(paras=p2, parts=p2parts)]
S['grammar'] = [
 P("Fill in the blank using the correct form of the word in brackets for a school notice:<br>The teacher praised her ______ (diligent) in completing the project.", 1, "diligence"),
 P("Identify the error and write the correction.<br>He do not know the answer to the question.", 1, "Error: do — Correction: does.", extra=errtab()),
 P("Fill in the blank with the correct form of the verb.<br>She ______ (live) in Jaipur since 2015.", 1, "has lived / has been living"),
 P("Read the given statement.<br>The guide said to the tourists, “You should not touch the monuments.”<br>Report: The guide told the tourists that ______________________.", 1, "they should not touch the monuments."),
 P("Fill in the blank by choosing the correct option.<br>The teacher was pleased ______ his progress.", 1, "pleased with", ["of", "with", "for", "from"], 'b'),
 P("Report the following.<br>“Please wait here till I return,” the clerk said to the visitor.<br>The clerk requested ______________________.", 1, "the visitor to wait there till he returned."),
 P("Complete the sentence by choosing the correct option.<br>She is interested ______ classical music.", 1, "interested in.", ["in", "on", "at", "for"], 'a'),
 P("The sentence has an error. Select the option that correctly identifies the error and the correction.<br>The news were broadcast at nine.", 1, "‘News’ is singular: were → was.", None, 'b', table(["No.", "Error", "Correction"], [["A.", "news", "newses"], ["B.", "were", "was"], ["C.", "broadcast", "broadcasts"], ["D.", "nine", "ninth"]])),
 P("Report the following question.<br>“Which book do you prefer?” the librarian asked me.", 1, "The librarian asked me which book I preferred."),
 P("Choose the correct option from the brackets.<br>I ______ (would / used to) play cricket every evening when I was young.", 1, "used to"),
 P("Fill in the blank with the correct option.<br>There are ______ apples in the basket; we can make a pie.", 1, "‘enough’ is correct.", ["enough", "much", "little", "a little"], 'a'),
 P("Identify the error and write the correction.<br>The women's club have organised a fair.", 1, "Error: have — Correction: has (club is singular).", extra=errtab()),
]
S['q4'] = (
 dict(q="You are Ananya/Aman, living in Shanti Nagar. The park in your locality is full of weeds and broken benches. Write a letter to the Secretary of the Residents' Welfare Association, in about 120 words, requesting action to restore it.",
      sol="<b>Format (1), Content (2), Fluency (2).</b> Points: current condition, importance of a park, children and elderly, proposed work, volunteer help.<br><i>Sample:</i> The Secretary, Residents' Welfare Association, Shanti Nagar, Jaipur / Subject: Request to restore the neighbourhood park. Sir, I write to draw your attention to the poor condition of our park, which is overgrown with weeds and has several broken benches. Children no longer find a safe place to play, and elderly residents cannot sit and walk comfortably. I request the Association to arrange for cleaning, repair of benches and regular gardening. Young residents, including me, are willing to volunteer on weekends. A clean park will improve the health and community life of the colony. Yours sincerely, Ananya Rao."),
 dict(q="You are Gaurav/Garima, a student of Class X. You want to encourage students to adopt reading habits. Write a letter to the Editor of a youth magazine, in about 120 words, suggesting ways to promote reading among teenagers.",
      sol="<b>Format (1), Content (2), Fluency (2).</b> Points: decline in reading, benefits, ways — book clubs, reading hours, libraries, digital books.<br><i>Sample:</i> The Editor, Youth Times, New Delhi / Subject: Encouraging reading among teenagers. Sir, Reading has declined among teenagers as screens take up most of their free time. I believe this is a loss, because books improve language, imagination and concentration. I suggest that schools begin a daily reading period, form book clubs and set up well-stocked libraries with popular titles. Magazines such as yours can introduce book reviews written by students. E-books may also be used by those who prefer devices. If these steps are adopted, a new generation of readers will grow up. Yours truly, Gaurav Bansal."),
)
S['q5'] = (
 dict(q="The school is to choose one student for the 'Best Volunteer' award. <b>Mira:</b> regularly helps in the library and organises donation drives, but she is often absent from school events. <b>Zayn:</b> attends every event and helps with decoration, but he rarely takes the initiative and waits to be told what to do. Analyse the profiles and decide who deserves the award. (100–120 words)",
      sol="<b>Content (2), Organisation (1), Fluency (2).</b><br><i>Sample:</i> Mira deserves the Best Volunteer award. Volunteering is about initiative and service, and Mira has shown both by organising donation drives and regularly helping in the library. Her absence from school events is a weakness, but her work benefits the wider community. Zayn's attendance and willingness to help with decoration are admirable, yet he waits to be told what to do, which suggests less personal commitment. A good volunteer identifies a need and acts upon it. Mira's record of independent work therefore outweighs Zayn's dependable presence. Zayn can be encouraged to take initiative in the future."),
 dict(q="The table compares two options for a school picnic.<br>" + table(["Features", "Water Park", "Nature Reserve"], [["Cost per student", "₹750", "₹450"], ["Distance", "15 km", "60 km"], ["Activities", "Rides and pools", "Trekking, bird watching"], ["Safety staff", "Lifeguards", "Forest guides"], ["Learning value", "Low", "High"]]) + "Study the data and write an analytical paragraph in 100–120 words comparing the options and recommending the better one for a school picnic.",
      sol="<b>Content (2), Analysis/recommendation (1), Fluency (2).</b><br><i>Sample:</i> The water park is nearer, at 15 km, and offers rides and pools that students enjoy, but it costs ₹750 per student and has little educational value. The nature reserve is cheaper at ₹450, though it is 60 km away and the journey will be longer. It offers trekking and bird watching led by trained forest guides, giving both recreation and learning. For a school picnic, learning value and cost matter alongside enjoyment. The nature reserve is therefore the better choice, provided transport is arranged safely. The water park may suit those who prefer a quick and purely recreational outing."),
)
S['q6'] = [
 dict(extract="Griffin, the stranger wrapped in bandages, arrives at the inn on a snowy evening and demands a room with a fire. He pays little attention to the landlady's questions and spends hours in his room among bottles and tubes. When she complains, he answers rudely, and her curiosity about the strange guest grows with every passing day.", src="Footprints Without Feet — extract adapted",
      parts=[P("How is Griffin dressed when he arrives?", 1, "In bandages / wrapped up.", ["In uniform", "In bandages", "In a suit", "In a cloak of fur"], 'b'),
             P("What does Griffin keep in his room?", 1, "Bottles and tubes / scientific apparatus."),
             P("The landlady's attitude towards Griffin is one of __________.", 1, "curiosity.", ["friendship", "curiosity", "respect", "pity"], 'b'),
             P("What do Griffin's actions suggest about his character? Answer in about 40 words.", 2, "He is secretive and rude (1); he hides his experiments and avoids questions, which arouses suspicion (1).")]),
 dict(extract="After ten years of hard work and debt, Matilda meets her old friend again. She looks worn and rough, but she speaks with pride of having paid every franc. When the friend reveals that the necklace had been a cheap imitation, Matilda is left speechless.", src="The Necklace — extract adapted",
      parts=[P("Whom does Matilda meet?", 1, "Her old friend, Madame Forestier.", ["Her cousin", "Her old friend", "Her husband", "A stranger"], 'b'),
             P("What did Matilda feel proud of?", 1, "Having paid back the whole debt."),
             P("The twist in the extract is that the necklace was __________.", 1, "an imitation.", ["stolen", "an imitation", "pure gold", "sold"], 'b'),
             P("How does the extract bring out the irony of Matilda's situation? Answer in about 40 words.", 2, "She sacrificed ten years to replace a necklace (1); it was worthless, so her suffering was needless (1).")]),
]
S['q7'] = [
 dict(extract="A young boy watches his ball roll down the street and into the water. The poet does not offer him another ball. Instead he says the boy must learn that things are lost, and that he will have to stand with his grief and understand the meaning of loss.", src="The Ball Poem — paraphrased",
      parts=[P("Where did the ball go?", 1, "Into the water.", ["Into a field", "Into the water", "Into the sky", "Under a car"], 'b'),
             P("Why does the poet not offer the boy another ball?", 1, "He wants him to learn about loss and responsibility."),
             P("The boy is learning to deal with __________.", 1, "loss and responsibility.", ["laziness", "loss and responsibility", "anger", "friendship"], 'b'),
             P("How does the poem present the boy's growing up? Answer in about 40 words.", 2, "He faces the loss of something he loves (1); he must accept it and learn responsibility rather than be given a replacement (1).")]),
 dict(extract="The tiger in the zoo walks to and fro behind bars, paying no attention to visitors. At night, in his imagination, he stalks across the village, lurks near the water-hole, and hears the footsteps of men who fear him. His rage burns quietly in his cage.", src="A Tiger in the Zoo — paraphrased",
      parts=[P("What does the tiger do in the cage?", 1, "Walks to and fro.", ["Sleeps all day", "Walks to and fro", "Plays", "Roars"], 'b'),
             P("What does the tiger do in his dreams?", 1, "Stalks the village and the water-hole."),
             P("The phrase 'burns quietly' suggests the tiger's __________.", 1, "suppressed anger.", ["delight", "suppressed anger", "weakness", "sleepiness"], 'b'),
             P("What contrast does the poet draw between the zoo and the wild? Answer in about 40 words.", 2, "In the zoo the tiger is confined and powerless (1); in the wild he is free, fierce and feared (1).")]),
]
S['q8'] = [
 ("How does Ausable save himself from Max in 'The Midnight Visitor'? (The Midnight Visitor)", "He invents a story about the police (1); makes Max believe the room is watched (1); Max leaves in panic (1)."),
 ("Describe the unusual nature of Mijbil's behaviour in his new home. (Mijbil the Otter)", "He loved water and played in the bath (1); he tore things and showed energy (1); he treated the writer as a friend (1)."),
 ("How did Ebright's early hobby lead him towards science? (The Making of a Scientist)", "He collects butterflies and sends specimens to the museum (1); his curiosity grows through experiments (1); his mother encourages him (1)."),
 ("What does Mandela mean by saying courage is not the absence of fear? (Nelson Mandela: Long Walk to Freedom)", "A brave man feels fear (1); he conquers it (1); courage is shown in acting despite fear (1)."),
 ("How does Anne's diary show her loneliness? (From the Diary of Anne Frank)", "She writes of having no true friend (1); she finds people unsympathetic (1); the diary becomes her companion (1)."),
]
S['q9'] = [
 ("How do the Martians misread the book in 'The Book That Saved the Earth'? (The Book That Saved the Earth)", "They find a nursery rhyme book (1); they interpret 'Humpty Dumpty' as a threat (1); they leave Earth in fear (1)."),
 ("Why was Lencho's faith in God both strong and naive? (A Letter to God)", "He believed God sees everything (1); he asked for money by letter (1); he accused the postal staff of stealing without proof (1)."),
 ("How does Madam's ride on the bus end in 'Madam Rides the Bus'? What does Valli learn? (Madam Rides the Bus)", "She sees a dead cow and feels sad (1); she takes the return bus and pretends to be unaffected (1); she learns that life has both beauty and cruelty (1)."),
]
S['q10'] = (
 ("Compare how 'A Tiger in the Zoo' and 'The Trees' use nature to speak about freedom and captivity. (A Tiger in the Zoo / The Trees)", "<b>Points:</b> tiger's caged rage; trees pressing against the window; personification; both long for freedom; poet's sympathy; message about nature. (2+2+2)"),
 ("Compare Mrs Pumphrey and Matilda as characters who pay a price for vanity or excess. (A Triumph of Surgery / The Necklace)", "<b>Points:</b> Mrs Pumphrey's pampering; Matilda's vanity; consequences — Tricki's illness vs ten years of drudgery; irony; moral — moderation. (2+2+2)"),
)
S['q11'] = (
 ("'The Necklace' is a story of pride, loss and irony. Discuss how Matilda's life changes. (The Necklace)", "<b>Points:</b> discontent; the ball; the loss; debt; ten years of labour; meeting Madame Forestier; irony of the imitation necklace. (2+2+2)"),
 ("Discuss how Mandela's speech shows his dream for a free South Africa and his belief in forgiveness. (Nelson Mandela: Long Walk to Freedom)", "<b>Points:</b> end of apartheid; the new society; courage; freedom of the oppressor too; honour to the heroes; hope and reconciliation. (2+2+2)"),
)
if __name__ == '__main__':
    for i, ps in enumerate(S['passages']): print(i, wc(ps['paras']))
    build(S, '/home/claude/pat/out/Class10_English/'); print('built')
