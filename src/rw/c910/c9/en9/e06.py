from eng9_lib import mcq, Q, X

NAME = "Twin Melodies; Music poem"
MCQ = [
 mcq("'Twin Melodies' is a:", ["one-act play in three acts", "novel", "essay", "diary"], "a", "Play by Mitra Phukan"),
 mcq("Shruti plays the:", ["violin", "flute", "tabla", "keyboard"], "a", "Young violinist"),
 mcq("Shruti's father, Nabin Sharma, is:", ["a violinist and school principal", "a tabla player", "a singer only", "a journalist"], "a", "Sangeetika Music School"),
 mcq("The friends in Shruti's group play fusion music, which blends:", ["Indian and Western music", "only folk music", "only rock", "only classical vocal music"], "a", "Indo-Western fusion"),
 mcq("Shruti had not told her parents about:", ["the fusion concert practices", "her exams", "a holiday", "a prize"], "a", "She feared his reaction"),
 mcq("Nabin firmly believed that:", ["only Hindustani classical music is worthy", "all music is equal", "fusion is modern art", "violins are Western only"], "a", "Ragas and aalaaps"),
 mcq("Nabin's rule about performances was:", ["one performance every six months", "one every week", "none at all", "one every year"], "a", "Familiarity breeds contempt"),
 mcq("Nabin's mocking remark about the practice was that it was for:", ["'phoo' music", "classical music", "temple songs", "folk music"], "a", "He dismissed fusion"),
 mcq("Shruti's friends advised her to:", ["tell her parents about the concert", "lie to them", "quit the group", "leave town"], "a", "Bite the bullet"),
 mcq("The idiom 'to bite the bullet' means:", ["to face a difficult situation bravely", "to give up", "to hurt oneself", "to speak rudely"], "a", "Courage"),
 mcq("In Act III, Shruti's parents:", ["watched the rehearsal and applauded", "stopped the rehearsal", "scolded the group", "left the house"], "a", "A turning point"),
 mcq("Nabin offered the children:", ["the music room", "money", "his violin", "a trip"], "a", "More equipment"),
 mcq("Who opened Nabin's eyes about his own past?", ["Leela, his wife", "Iqbal", "Peter", "his father"], "a", "She reminded him"),
 mcq("Nabin's own father came from a family of:", ["vocalists", "tabla players", "painters", "doctors"], "a", "Traditional school"),
 mcq("The proverb 'each bay, its own wind' used by Nabin suggests:", ["every generation has its own approach", "winds are strong", "bays are dangerous", "music is loud"], "a", "Acceptance"),
 mcq("In the poem, music is compared to:", ["an ocean and a friend", "a book", "a mountain", "a city"], "a", "Metaphors"),
]
EXT = [
 X("The young band finishes its practice in Iqbal's room. A newspaper has praised Shruti's earlier concert with her father. The boys tease her and ask for a party, but Shruti is lost in thought. She fears her strict father will see fusion music as an insult to the violin and a betrayal of ragas.",
   [("Where does the practice take place?", "In Iqbal's room."),
    ("What are the boys teasing Shruti for?", "Her newspaper fame; they want a party."),
    ("Why is Shruti worried?", "She fears her father's disapproval of fusion music."),
    ("What does 'lost in thought' show?", "She is anxious and preoccupied.")]),
 X("At dinner Nabin sits upright and listens stiffly as Shruti speaks of the concert. He reminds her of his rule and says a single voice would drown in an orchestra's noise. When he hears the word fusion, he leaves the table. Leela scolds Shruti for hiding things, though she looks sympathetic.",
   [("What rule does Nabin remind Shruti of?", "One performance every six months."),
    ("What was his objection to fusion?", "He thinks it drowns individual style in noise."),
    ("How does Nabin react to the word 'fusion'?", "He leaves in displeasure."),
    ("What does Leela's scolding show?", "She disapproves of hiding things but is caring.")]),
 X("The poet calls music an ocean, a rhythm and a friend. It moves her to the core, lifts her spirits and comforts her when she is blue. Whenever she is cheerful or lonely, music is there, so it becomes the one dependable companion in her life.",
   [("What three things is music compared to?", "An ocean, a rhythm and a friend."),
    ("What does music do when the poet feels blue?", "It acts as therapy and lifts her spirits."),
    ("Name the device that makes 'music is the ocean' effective.", "Metaphor."),
    ("What is the mood of the poem?", "Warm and appreciative.")]),
]
SA = [
 Q("Why was Shruti afraid to tell her father about the concert?", "He believed only classical Hindustani music was worthy and would call fusion a disrespect to the violin.", "2"),
 Q("What did Nabin say about group performances?", "He said that a solo style would be drowned in the hubbub of an orchestra.", "2"),
 Q("How did Nabin's attitude change in Act III?", "He heard the fusion piece, found it soulful, applauded and offered his music room.", "2"),
 Q("What did Leela tell Shruti about Nabin's past?", "He had defied his family of vocalists by taking up the violin and worked very hard.", "2"),
 Q("What does Nabin mean by 'each bay, its own wind'?", "Each generation has its own way of expression and must be trusted.", "2"),
 Q("Which feeling does music give the poet in the poem?", "It gives comfort, joy and strength like a faithful friend.", "2"),
]
LA = [
 Q("Describe the conflict between Shruti and her father.", "Tradition vs fusion; Shruti wants to try something new; Nabin fears losing classical purity; she hides her practice; they clash at dinner.", "3"),
 Q("How is the generation gap shown in the play?", "Shruti loves fusion; Nabin loves classical music; he once defied his own father, yet repeats his father's attitude.", "3"),
 Q("Why does Shruti hide the practice sessions from her father?", "She fears his anger, wants to try fusion, and doesn't know how to tell him; her friends urge her to speak.", "3"),
 Q("Describe the role of Leela in resolving the conflict.", "She scolds Shruti but supports her, attends the rehearsal and reminds Nabin of his own past.", "3"),
 Q("What message does 'Twin Melodies' give about tradition and change?", "Tradition and new forms can live together; elders should listen; the young should respect roots; understanding resolves conflict.", "3"),
 Q("Write a character sketch of Nabin.", "Strict, proud of tradition, firm, but able to change; loving father; admits his mistake.", "3"),
 Q("What are the metaphors used in the poem?", "Music as an ocean, a rhythm, a therapy and a friend; they show its power to pull, move, heal and comfort.", "3"),
 Q("What is the message of the poem about music?", "Music is a constant companion that lifts spirits and comforts in all moods.", "3"),
]
