from eng9_lib import mcq, Q, X

NAME = "Vitamin-M; I Cannot Remember My Mother"
MCQ = [
 mcq("Ravi's mother wished that someone would invent a vitamin for:", ["memory of old people", "strength", "eyesight", "hearing"], "a", "'Vitamin-M'"),
 mcq("Grandpa had come to live with Ravi's family because:", ["he was too old to live alone", "he lost his job", "he wanted a holiday", "his house was sold"], "a", "After a fall"),
 mcq("Grandpa's earlier profession was:", ["lawyer", "teacher", "doctor", "banker"], "a", "Trace of firmness"),
 mcq("Grandpa disliked the city because it was:", ["noisy and crowded", "too quiet", "too cold", "too clean"], "a", "Missed his town house"),
 mcq("Grandpa had earlier been admitted to hospital because he:", ["took a double dose of medicines", "fell from the stairs", "caught a fever", "lost his way"], "a", "Absent-mindedness"),
 mcq("Grandpa wished to buy the Tamil newspaper from:", ["the corner shop", "the market", "a library", "the bus stop"], "a", "Why he went out"),
 mcq("Ravi followed Grandpa because:", ["his mother told him not to let Grandpa go out alone", "he wanted to play", "he was bored", "Grandpa asked him"], "a", "Promise to Mamma"),
 mcq("At the tea stall Grandpa had sugary tea, bananas and ice cream, which were:", ["all forbidden at home", "his favourite healthy food", "given by Ravi", "his routine"], "a", "Doctor's restrictions"),
 mcq("Ravi was thrown out of the shop next to the barber's because it was a:", ["ladies' hairdressing salon", "bank", "bookshop", "gym"], "a", "Humorous incident"),
 mcq("The man in the bus wearing the yellow cap was:", ["a stranger given the cap by Grandpa", "Grandpa in disguise", "Ravi's father", "a policeman"], "a", "Grandpa's generosity"),
 mcq("When Ravi reached home he found Grandpa:", ["asleep and snoring", "watching TV", "gone out again", "angry"], "a", "Relief"),
 mcq("Grandpa's birthday custom was to:", ["give gifts to everyone at home", "receive gifts only", "hold a big party", "visit a temple"], "a", "Mother forgot the date"),
 mcq("The gift Ravi received was:", ["The Best Detective Stories", "a chess set", "a cricket bat", "a watch"], "a", "Hint to Ravi's following"),
 mcq("Which trait best describes Grandpa?", ["clever and humorous", "dull and forgetful", "angry and cruel", "shy and silent"], "a", "Proves memory is intact"),
 mcq("Tagore's poem is about the poet's:", ["memories of his mother", "love of travel", "school days", "garden"], "a", "I Cannot Remember My Mother"),
 mcq("In the poem the poet recalls his mother through:", ["tune, scent of shiuli flowers and sky", "her photographs", "her letters", "her sayings"], "a", "Senses"),
]
EXT = [
 X("Ravi's mother set out the tablets and sighed that if only someone could invent a vitamin for memory, she would give it to the old. Ravi pointed to the frail figure in the rocking chair and reminded her that Grandpa might hear. She replied that he could hardly see or hear well or remember well these days.",
   [("What did Ravi's mother wish for?", "A vitamin to improve old people's memory."),
    ("Who was in the rocking chair?", "Grandpa."),
    ("Which three faculties of Grandpa did she say were weak?", "Hearing, sight and memory."),
    ("What does her attitude show?", "She underestimated Grandpa and was anxious about him.")]),
 X("Ravi crawled behind benches and bushes to keep Grandpa in sight. A lady with an umbrella scolded him, and flower sellers noticed him hiding behind a tree. At last he reached the bus but found a stranger wearing Grandpa's cap. He wondered where Grandpa had gone.",
   [("Why was Ravi hiding?", "He did not want Grandpa to see him following."),
    ("Who scolded Ravi in the park?", "A little boy's mother with an umbrella."),
    ("Whose cap was the stranger wearing?", "Grandpa's."),
    ("What do these incidents add to the story?", "Humour and suspense.")]),
 X("The poet cannot recall his mother's face, yet a tune, a morning scent and the blue of the sky bring her near. Each stanza uses a different sense: hearing, smell and sight. The poem shows that love lives on in small things.",
   [("What can the poet not remember?", "His mother."),
    ("Name two things that remind him of her.", "A tune, the scent of shiuli flowers or the sky."),
    ("Which three senses are used?", "Hearing, smell and sight."),
    ("What is the mood of the poem?", "Tender and wistful.")]),
]
SA = [
 Q("Why was Ravi's mother worried about Grandpa?", "He was forgetful, had overdosed on medicines and got lost on a walk, so she feared he might go out alone.", "2"),
 Q("Why did Grandpa get upset with his daughter?", "She forbade him to go out alone, as though he were a child, which hurt his independence.", "2"),
 Q("How does Ravi try to follow Grandpa without being seen? Name two things he did.", "He hid behind benches, a tree, and a car and crept behind bushes.", "2"),
 Q("What did Grandpa do to show he knew Ravi had followed him?", "He gave Ravi a book about detective stories and said it would help one avoid being fooled while trailing.", "2"),
 Q("Why did Grandpa's gift for his daughter come with a remark about 'Vitamin-M'?", "She had forgotten his birthday, though it was marked on her calendar, so he teased her about her memory.", "2"),
 Q("Name two senses used in Tagore's poem.", "Hearing (a song hummed) and smell (shiuli flowers).", "2"),
]
LA = [
 Q("Describe Grandpa's character as revealed in the story.", "Independent, humorous, sharp, generous; a chess player with a good memory; hates being treated like a child; secretly aware of Ravi.", "3"),
 Q("What is the irony in the story's title?", "Mother thinks old people need Vitamin-M for memory, but it is she who forgot Grandpa's birthday; Grandpa's memory is sharp.", "3"),
 Q("How do we know that Grandpa's memory is not failing? Give two proofs.", "He recalls chess games of Karpov and Fischer; he knew Ravi had followed him; he remembered the birthday gifts and tricked everyone.", "3"),
 Q("Why is respect for the elderly the theme of the story?", "Grandpa wants dignity and independence; overprotection hurts him; the story urges children to listen and understand.", "3"),
 Q("Describe Ravi's day as detective.", "Followed Grandpa to the park, tea stall, barber's and bus; was scolded; was confused by the stranger; returned home worried and relieved.", "3"),
 Q("How does the writer use humour in the story?", "Through the comic chase, the lady with umbrella, the loud vendors, the wrong shop and the final twinkle in Grandpa's eye.", "3"),
 Q("How does Tagore recall his mother in the poem?", "He cannot remember her face, but a tune, the autumn scent of shiuli and the stillness of the sky bring her gaze to mind.", "3"),
 Q("What is the central idea of 'I Cannot Remember My Mother'?", "A mother's love lives in memories, senses and nature even when she is gone.", "3"),
]
