from eng9_lib import mcq, Q, X

NAME = "The Pot Maker; Quality; vocation poems"
MCQ = [
 mcq("Sentila, the girl in 'The Pot Maker', belongs to a community of:", ["potters in Nagaland", "weavers in Kashmir", "fishermen in Goa", "farmers in Punjab"], "a", "Temsula Ao's story"),
 mcq("Sentila's mother Arenla did not want to teach her pot making because it:", ["was tiring and earned very little", "was forbidden for girls", "was dangerous", "needed expensive tools"], "a", "Hard labour, small pay"),
 mcq("Arenla wanted Sentila to learn which craft instead?", ["Weaving", "Carpentry", "Basket making", "Embroidery only"], "a", "Better income"),
 mcq("The clay for pots was dug from a place:", ["sixteen kilometres from the village", "inside the village", "at the market", "in the field"], "a", "Riverbank"),
 mcq("The village council asked Mesoba to explain because:", ["Arenla was not passing on the skill", "pots were stolen", "Sentila was missing", "clay was short"], "a", "Skill belongs to all"),
 mcq("The elders believed skills like pot making:", ["do not belong to any individual", "must be kept secret", "are only for the old", "should be sold"], "a", "Tradition to be passed on"),
 mcq("Onula was:", ["the supervisor of the girls' dormitory", "Sentila's sister", "a village elder", "a teacher"], "a", "A kind middle-aged widow"),
 mcq("Onula noticed that Sentila failed because she was too:", ["tense", "lazy", "careless", "proud"], "a", "Clay yields to a relaxed hand"),
 mcq("Which part of the pot did Onula say was wrong?", ["the mouth", "the base", "the handle", "the colour"], "a", "Rim needed a strip of dough"),
 mcq("When Sentila finished, how did her row of pots compare with her mother's?", ["one short of her mother's", "twice as many", "equal", "far fewer"], "a", "Same speed and skill"),
 mcq("At the end of the story Onula realised:", ["a new pot maker was born", "the pots were stolen", "the shed had been burnt", "Sentila had quit"], "a", "Two matching rows of pots"),
 mcq("The story shows that traditional skills are:", ["handed down through generations", "learned only in schools", "easy to master", "no longer useful"], "a", "Theme"),
 mcq("In 'Quality', Mr Gessler made boots by:", ["hand, only to order", "machines in bulk", "buying ready stock", "advertising widely"], "a", "Quiet distinction"),
 mcq("Mr Gessler said of his craft: 'Id is an ardt!' meaning:", ["it is an art", "it is hard work", "it is a hobby", "it is a business"], "a", "Pride in craft"),
 mcq("Gessler Brothers struggled because:", ["big firms won by advertisement, not work", "customers disliked leather", "boots were too costly", "the brother left"], "a", "Commercial competition"),
 mcq("The poem 'Gifts of Grace: Honouring Our Vocations' celebrates:", ["craftspeople and workers of Bharat", "kings and queens", "soldiers only", "scientists"], "a", "Dignity of vocations"),
]
EXT = [
 X("Sentila would slip away to the potters' yard and watch them mix, pound and shape the clay. She loved the tap of the spatula and the sight of a pot rising from a shapeless lump. She never told her mother. Villagers began to gossip about why Arenla would not teach her own daughter.",
   [("Where did Sentila go to watch pot making?", "To the potters' work area in the village."),
    ("What sound did she love?", "The tap of the spatula on the clay."),
    ("Why did she hide her visits from her mother?", "Her mother did not want her to learn the craft."),
    ("What was the village talking about?", "Why Arenla refused to teach Sentila.")]),
 X("The shoemaker stood before the customer in his leather apron, blinking as if woken from a dream of boots. He praised the piece of leather with great love and asked when the boots were wanted. Nothing in his shop was for show; every pair was made only when ordered, and each lasted for years.",
   [("What was Gessler wearing?", "A leather apron."),
    ("What does 'a dream of boots' suggest?", "He was lost in his craft."),
    ("How did his boots last?", "For years, very long."),
    ("What does the passage tell us about his work?", "He made quality boots with love and care, not for display.")]),
 X("The poet hears Bharat celebrating its many vocations. Artisans with their instruments and shoemakers proud of their work all raise a voice. The voice of each vocation is the voice of the worker herself. The poem presents work as something to be honoured and enjoyed.",
   [("What does the poet celebrate?", "The varied vocations of Bharat."),
    ("Name one vocation mentioned.", "Craftspeople, artisans or shoemakers."),
    ("What is the voice of a vocation, according to the poem?", "The voice of the worker."),
    ("What is the mood of the poem?", "Celebratory and respectful.")]),
]
SA = [
 Q("Why did Arenla not want Sentila to become a potter?", "Pot making was hard, tiring and poorly paid, whereas weaving earned more and could be done indoors.", "2"),
 Q("How did the village elders react to Arenla's refusal?", "They told Mesoba that skills belong to the community and must be shared with anyone who wishes to learn.", "2"),
 Q("How did Onula help Sentila?", "She noticed Sentila was tense, showed her how to make a pot and advised her to watch how her mother shaped the mouth.", "2"),
 Q("Why does Gessler say 'Dose are nod my boods'?", "The narrator wore factory-made boots that did not fit him; the shoemaker took pride in his own work.", "2"),
 Q("Why did Gessler's business decline?", "Big firms attracted customers by advertisement; he cared for quality and made only to order.", "2"),
 Q("What is the dignity of labour as presented in the poem?", "Every vocation, humble or skilled, deserves respect and celebration.", "2"),
]
LA = [
 Q("Describe the process of making a pot as shown in the story.", "Clay was dug at the river, soaked, pounded in bamboo cylinders, shaped by rotating the lump with spatula, dried in the sun and fired in a kiln covered with hay and bamboo.", "3"),
 Q("Why is Sentila's story one of passion and perseverance?", "She watched potters secretly, kept trying despite failure, learned from Onula and her mother, and finally made pots with speed and skill.", "3"),
 Q("What is the role of Onula in the story?", "She understands Sentila's difficulty, teaches her, and later senses the significance of two rows of pots; she is a guide.", "3"),
 Q("Why do you think Arenla left Sentila alone in the shed?", "She wanted Sentila to try without being watched; her absence helped Sentila trust her hands; it passed on the skill.", "3"),
 Q("What does the story say about the passing on of traditional skills?", "Skills belong to the community; experts must teach others; they preserve culture and history.", "3"),
 Q("Describe Mr Gessler as a craftsman.", "Proud, honest, skilled; made only on order; his boots lasted; he hated shoddy work and suffered when big firms took over.", "3"),
 Q("What does 'Quality' tell us about modern commerce and handicrafts?", "Advertisement and mass production beat handmade quality; craftsmen struggle; true quality is undervalued.", "3"),
 Q("How does the poem honour vocations?", "It describes many crafts, shows that each worker's voice is her vocation, and uses a celebratory tone.", "3"),
]
