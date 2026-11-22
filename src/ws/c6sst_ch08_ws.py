"""Class 6 Social Science Ch 8 - Unity in Diversity, or 'Many in the One': worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch08"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c08", str(REPO / "src/rn_work/c6_sst/c08.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("India has about what share of the world's population?", 1, "(c) about 18 per cent", "E", opts=["about 5 per cent", "about 10 per cent", "about 18 per cent", "about 40 per cent"]),
W("The 'People of India' project was carried out by the:", 1, "(a) Anthropological Survey of India", "E", opts=["Anthropological Survey of India", "Reserve Bank of India", "Election Commission", "Survey of India (map makers)"]),
W("The 'People of India' project counted languages written in how many scripts?", 1, "(b) 25", "E", opts=["5", "25", "250", "325"]),
W("Which of these is a millet?", 1, "(d) Ragi", "E", opts=["Rajma", "Basmati", "Masoor", "Ragi"]),
W("The printed Indian cotton that became very popular in 17th-century Europe was called:", 1, "(a) chintz", "E", opts=["chintz", "muslin", "velvet", "denim"]),
W("Makara Sankranti is celebrated around:", 1, "(c) 14 January", "E", opts=["14 April", "15 August", "14 January", "2 October"]),
W("In Punjab, the harvest festival of this season is known as:", 1, "(b) Maghi / Lohri", "E", opts=["Pongal", "Maghi / Lohri", "Uttarayan", "Magh Bihu"]),
W("The Pañchatantra has stories in which the main characters are:", 1, "(d) animals", "E", opts=["kings only", "gods only", "children only", "animals"]),
W("Fill in the blank: The sari is a plain length of ______ cloth.", 1, "unstitched. (1)", "E"),
W("Write True or False: Diversity divides India and makes it weak.", 1, "False. According to the chapter, diversity does not divide, it enriches. (1)", "E"),
W("Write True or False: The same grains and spices are used in many parts of India.", 1, "True. Rice, wheat, millets, pulses, turmeric, cumin and ginger are used almost everywhere. (1)", "E"),
W("Who said that India offers 'unity in diversity' while asking how a history of India could be written?", 1, "The British historian Vincent Smith. (1)", "E"),
W("Name the two great Sanskrit epics of India.", 1, "The Rāmāyaṇa and the Mahābhārata. (1)", "E"),
W("Name any two silk saris mentioned in the chapter.", 2, "Any two: Banarasi, Kanjivaram, Paithani, Patan Patola, Muga, Mysore. (1+1)", "E"),
W("Give two examples of staple grains.", 2, "Any two: rice, wheat, barley, bajra, jowar, ragi, dals. (1+1)", "E"),
W("What is meant by 'unity in diversity'? Answer in one sentence.", 2, "It means that in spite of many differences in language, dress, food and customs, there is a deeper oneness that joins the people together. (2)", "E"),
W("Name the festival that marks the beginning of the harvest season in many parts of India around 14 January.", 1, "Makara Sankrānti. (1)", "E"),
# ---------------- MEDIUM ----------------
W("The 'People of India' project was directed by K.S. Singh. Besides the numbers of communities and languages, what else did the project observe about Indians?", 2, "It observed that many Indians are migrants, that is, people not living near their birthplace or with their original community. (2)", "M"),
W("Read the quotation: \"There is hardly a place in the country which the epic heroes such as the Pandavas did not visit according to folklores.\" What does K.S. Singh want to tell us about the epics?", 2, "The Mahābhārata is known in every part of India, and local people have their own legends that connect their land with the epic heroes. This shows how the epics join the country together. (2)", "M"),
W("Read the words of Nehru: \"Illiterate villagers would know hundreds of verses by heart.\" What does it show about the epics?", 2, "The epics were known even to people who could not read. They were passed on by listening, retelling and songs, and every village had a share in them. (2)", "M"),
W("Match: (a) Pongal (b) Magh Bihu (c) Uttarayan with (1) Gujarat (2) Tamil Nadu (3) Assam.", 3, "(a) with (2), (b) with (3), (c) with (1). (1 each)", "M"),
W("Priya's mother in Rajasthan makes aloo paratha, and her aunt in Tamil Nadu makes potato curry with rice. How do these dishes show unity and diversity?", 3, "Both use common ingredients such as potato and spices (unity) (1), but the grain, cooking style and spice mixes differ by region (diversity) (1). So one vegetable can make many dishes, as the chapter says (1).", "M", wp=True),
W("Why did England and France ban the import of chintz from India?", 2, "Indian chintz was so popular that the sale of some European dresses dropped sharply. To protect their own products, they banned its import. (2)", "M"),
W("Explain with an example why the sari is a good example of 'unity in diversity'.", 3, "Unity: it is one single unstitched length of cloth worn in most parts of India (1). Diversity: there are hundreds of kinds made of cotton, silk and synthetic fabrics, by different weaving methods, designs and colours (1), and it is draped in many ways in different regions and communities (1).", "M"),
W("What is an epic? Give the main story of the Rāmāyaṇa in two lines.", 3, "An epic is a long poem narrating the adventures of heroes and other great figures of the past (1). In the Rāmāyaṇa, Rāma, with the help of his brother Lakṣhmaṇa and of Hanuman, defeats the demon Rāvaṇa who had kidnapped his wife Sītā (2).", "M"),
W("Give the main story of the Mahābhārata in two lines.", 2, "The Pāṇḍavas, with Kṛiṣhṇa's help, fight their own cousins, the Kauravas, to recover their kingdom. (2)", "M"),
W("Why can the Pañchatantra be called an example of 'one becoming many'?", 3, "The original Sanskrit text is at least 2,200 years old (1). Its stories were adapted in almost every Indian language and travelled to Southeast Asia, the Arab world and Europe (1). About 200 adaptations exist in more than 50 languages, so one collection became many (1).", "M"),
W("Find the mistake: \"Chintz was a kind of silk sari worn only in Banaras.\"", 2, "Chintz was a beautiful printed cotton, not a silk sari, and it was exported to Europe where it became very popular. (2)", "M"),
W("Arrange in order from oldest to newest: (i) chintz is popular in Europe (ii) the 'People of India' project (iii) the stone relief of a sari at Vaiśhali.", 3, "(iii) stone relief at Vaiśhali (a few centuries BCE), (i) chintz popular in Europe (17th century), (ii) People of India project (late 20th century). (1 each)", "M"),
W("A traveller in a train notices new scripts, dresses and foods at each station. Which idea of the chapter does this describe, and why is it usually the first thing visitors notice?", 2, "It describes India's rich diversity (1). Diversity is easy to see in dress, language, food and scripts, so it is usually the first thing that strikes visitors (1).", "M", wp=True),
W("Name three different names of the festival celebrated around 14 January and say what is common to all of them.", 2, "Any three: Pongal, Magh Bihu, Maghi/Lohri, Uttarayan, Khichdi Parv, Pedda Panduga, Shishur Saenkraat. All are forms of Makara Sankrānti and mark the beginning of the harvest season at about the same time of year. (2)", "M"),
W("What are staple grains? Why are they a sign of unity?", 2, "Staple grains such as rice, wheat, millets and pulses are the basic food for most Indians (1). They are common to almost every part of the country, though cooked in different ways (1).", "M"),
W("How do tribal communities show the spread of the epics? Give one example from the chapter.", 3, "Many tribes such as the Bhils, Gonds and Mundas, and tribes of the northeast and Himalayan regions, have their own oral versions and legends of the epic heroes visiting their land (2). Example: the 'Pañcha Pāṇḍavar' stone shrine kept by the Irula tribals in the Nilgiris, Tamil Nadu (1).", "M"),
W("Anil says, \"If we all dressed and ate alike India would be stronger.\" Using the chapter, explain why this is not the view of Indian culture.", 2, "Indian culture celebrates diversity as an enrichment. Diversity does not divide; it adds beauty and richness, while an underlying unity nourishes it. (2)", "M", wp=True),
W("Make a two-part list, 'Unity' and 'Diversity', for the topic 'Food'.", 3, "Unity: staple grains (rice, wheat, millets, pulses) and common spices (turmeric, cumin, cardamom, ginger) (1.5). Diversity: thousands of regional dishes and preparations made from the same ingredients (1.5).", "M"),
W("Why did the sari draw the admiration of many travellers in the past?", 2, "They marvelled at its simplicity, its economy and the diverse ways in which it is worn. Women also put it to many uses beyond a dress. (2)", "M"),
# ---------------- HARD ----------------
W("Read: \"Oh, grant me my prayer, that I may never lose the bliss of the touch of the one in the play of the many.\" (Tagore). Explain in your own words what the poet wants and link it to the chapter title.", 3, "The poet prays that he may always feel the oneness that lies behind the many different things (1). In the chapter, 'the many' are India's languages, clothes, foods and festivals (1), and 'the one' is the common thread joining them; that is 'Many in the One' (1).", "H"),
W("Sri Aurobindo wrote that 'the Many in the One' is India's very nature. Why does the chapter use this phrase in its title?", 3, "The phrase sums up the chapter (1). India has countless forms in food, dress, festivals and stories, but all share common ingredients, ideas and values (1). The chapter shows this with examples, so the phrase explains India's nature (1).", "H"),
W("Case study: Ravi's family moved from Jaipur to Chennai. His new friend tells him about Pongal in mid-January. Ravi says that in Jaipur they fly kites and eat til sweets around the same date. What do the two festivals show? Explain using the chapter.", 4, "Both are celebrated at about the same time, around 14 January, and mark the harvest season (1). In the chapter they are examples of Makara Sankrānti, which has different names such as Pongal in Tamil Nadu and Uttarayan in Gujarat (1). The names and customs differ (diversity) (1), but the season and the reason are the same (unity). Ravi's observation shows that one festival can have many forms (1).", "H", wp=True),
W("Why is the travel of the Pañchatantra to Southeast Asia, the Arab world and Europe important for understanding Indian culture?", 3, "It shows that Indian stories were so useful and attractive that people far away adapted them (1). Each region retold the stories in its own language (diversity) while keeping the same lessons (unity) (1). It also shows that Indian culture influenced the wider world (1).", "H"),
W("How do the two epics create 'a dense web of cultural interactions across India and many parts of Asia'? Explain in five or six lines.", 4, "The epics have been translated and adapted into regional literatures for over two millenniums (1). Folk versions exist everywhere, for example about a hundred versions of the Mahābhārata in Tamil Nadu alone (1). Tribal communities keep legends of the epic heroes visiting their areas (1). Because people everywhere share the same stories, values and questions about right and wrong, they feel connected to each other across regions and in other parts of Asia (1).", "H"),
W("Hari says: \"The 'People of India' project proves that India is a divided country.\" Do you agree? Give two reasons from the chapter.", 3, "No. The project found 4,635 communities, 325 languages and 25 scripts, which shows great diversity (1). But the chapter says diversity does not divide, it enriches (1), and an underlying unity joins people through common food, dress, festivals and stories (1).", "H", wp=True),
W("Why is 'making sense of diversity' not easy? How does Vincent Smith's question show this?", 3, "Where there are thousands of communities, many languages and many customs, it is hard to see what holds everything together (1). Vincent Smith asked how a history of India could be written 'in the face of such bewildering diversity' (1). His answer was that India offers unity in diversity (1).", "H"),
W("Compare the Rāmāyaṇa and the Mahābhārata: state two things that are the same and two that are different, according to the chapter.", 4, "Same: both are long Sanskrit epics (1) and both tell of heroes who fight to re-establish dharma, with shorter stories on right and wrong inside them (1). Different: in the Mahābhārata the Pāṇḍavas fight their cousins the Kauravas with Kṛiṣhṇa's help (1), while in the Rāmāyaṇa Rāma defeats the demon Rāvaṇa to rescue Sītā (1).", "H"),
W("A school makes a 'Unity in Diversity' exhibition. Suggest four stalls based on the chapter and one thing to show at each.", 4, "(1 mark each) Food: staple grains and spices from many regions. Clothing: sari and dhoti styles and fabrics. Festivals: a map showing the names of the 14 January harvest festival. Literature: Pañchatantra stories and local folk versions of the epics.", "H", wp=True),
W("Why is the example of chintz important in the story of Indian textiles? What does it tell us about India's place in the world?", 3, "India produced the finest cotton for a very long time and exported textiles as far as Europe (1). Chintz became so popular in 17th-century Europe that England and France banned it to protect their own products (1). It shows that Indian crafts were of high quality and in great demand abroad (1).", "H"),
W("Read the Nehru passage: the epics were 'engraved on the popular mind and gave a richness and content to it.' What does this suggest about the effect of the epics on ordinary people?", 3, "The stories gave people values, moral lessons and a shared stock of verses and examples (1). Even without formal schooling, villagers could talk about right and wrong using stories from the epics (1). They enriched everyday life and thought (1).", "H"),
W("Explain how 'one' can become 'many' in India, with three examples from three different parts of the chapter.", 3, "(1 each) One dress, the sari, becomes hundreds of types by fabric, weave and drape. One harvest festival becomes many with regional names. One collection of stories, the Pañchatantra, becomes about 200 adaptations in over 50 languages. (Epics or food are also accepted.)", "H"),
W("Do you think a country with great diversity needs an 'underlying unity'? Give your opinion with two reasons based on the chapter.", 3, "Yes. Unity gives a shared base of values and culture so people can live together despite differences (1.5). The chapter says unity nourishes diversity, and diversity is celebrated as enrichment only when people feel they belong together (1.5). (Any well-reasoned answer is accepted.)", "H"),
W("Choose any two features of life in your own region (language, festival, food, folk tale or dress) and show how each is a case of 'Many in the One'.", 3, "Sample: Rajasthani folk tales carry a moral like the Pañchatantra stories (1), and the mid-January harvest festival is celebrated with kite flying, like Uttarayan in Gujarat (1). Both are local forms of ideas shared across India (1). (Any two sensible links with a clear unity and diversity are accepted.)", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "8.7 Timeline: How Old Are These Traditions?"),
 ("table", ["Period", "What the chapter tells us"], [
  ["A few centuries BCE", "Stone relief of a woman in a sari from Vaiśhali (in today's Bihar) shows that the sari is very old"],
  ["At least 2,200 years ago", "Original Sanskrit text of the Pañchatantra"],
  ["More than two millenniums (2,000+ years)", "The Rāmāyaṇa and Mahābhārata translated, adapted and retold in regional literatures"],
  ["17th century", "Indian printed cotton (chintz) so popular in Europe that England and France banned its import"],
  ["Late 20th century", "Anthropological Survey of India's 'People of India' project (4,635 communities, 325 languages, 25 scripts)"],
  ["Today", "India has over 1.4 billion people, about 18 per cent of the world's population"]]),
 ("h2", "8.8 Key Terms and Key People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Diversity**", "Variety — many kinds of people, languages, dress, food, customs"],
  ["**Unity**", "Oneness — the common ideas, values, stories and basic things that join people"],
  ["**Staple grains**", "Basic foods of most people: cereals, millets and pulses"],
  ["**Relief**", "A design that stands out from the surface of a panel (stone, wood, ceramic)"],
  ["**Chintz**", "A beautiful printed cotton cloth of India, much liked in 17th-century Europe"],
  ["**Epic**", "A long poem narrating the adventures of heroes and great figures of the past"],
  ["**Folklore**", "Stories, songs and beliefs of ordinary people passed on from person to person"],
  ["**Vincent Smith**", "British historian who said India offers unity in diversity"],
  ["**K.S. Singh**", "Anthropologist who directed the People of India project"],
  ["**Rabindranath Tagore**", "Poet who prayed never to lose 'the touch of the one in the play of the many'"],
  ["**Jawaharlal Nehru**", "India's first Prime Minister; wrote how villagers knew hundreds of epic verses by heart"]]),
 ("h2", "8.9 Map and Picture Pointers"),
 ("ul", ["On the map of festival names (Fig. 8.5), locate **Tamil Nadu (Pongal)**, **Kerala (Makara Vilakku)**, **Karnataka (Makara Sankramana)**, **Andhra Pradesh (Pedda Panduga)**, **Gujarat (Uttarayan)**, **Punjab (Maghi/Lohri)**, **Assam (Magh Bihu)**, **Kashmir (Shishur Saenkraat)**. All of them fall about **14 January**.",
  "Locate **Vaiśhali** in today's **Bihar** (stone relief of a sari) and the **Nilgiris in Tamil Nadu** (Pañcha Pāṇḍavar stone shrine kept by the Irula).",
  "In the pictures of sari uses (Fig. 8.4), the sari is used for many things beyond a dress, showing how one object serves many purposes."]),
 ("h2", "8.10 Reading the Sources"),
 ("table", ["Source", "What it says", "What we learn"], [
  ["Vincent Smith's question", "'How can a history of India be written in the face of such bewildering diversity?' The answer: unity in diversity", "Diversity may look confusing; unity is the key to understanding India"],
  ["Tagore's prayer", "Never lose the bliss of 'the touch of the one in the play of the many'", "The oneness behind the variety is a source of joy"],
  ["Sri Aurobindo", "'The Many in the One' is India's own nature (*Swabhava*) and *Swadharma*", "Unity in diversity is basic to India's character"],
  ["K.S. Singh", "'Hardly a place in the country which the epic heroes did not visit according to folklores'", "Local legends tie every region to the epics"],
  ["Nehru's travels", "Illiterate villagers knew hundreds of epic verses by heart", "The epics shaped the thinking of ordinary people"]]),
 ("note", "IMPORTANT", "When answering 'why / how' questions, always give **both sides**: first the **unity** (the one common thing) and then the **diversity** (its many forms), with a named example."),
 ("h2", "8.11 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["India is very large with 1.4 billion people and thousands of communities", "Great diversity of language, dress, food and customs"],
  ["Shared staple grains and spices", "An endless variety of dishes from the same ingredients"],
  ["Indian chintz was highly popular in Europe", "England and France banned its import to protect their own products"],
  ["The epics were retold for 2,000+ years in every region", "A dense web of cultural links across India and Asia; many folk and tribal versions"],
  ["Indian culture values both diversity and unity", "Diversity is seen as enrichment and not as a cause of division"]]),
 ("h2", "8.12 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Explain how India's festivals show unity in diversity. (3 marks)", "Many festivals are celebrated across India at almost the same time but with different names. Makara Sankrānti around 14 January marks the beginning of the harvest season. It is called Pongal in Tamil Nadu, Magh Bihu in Assam, Maghi/Lohri in Punjab and Uttarayan in Gujarat. The names and customs differ (diversity) but the season and the meaning are the same (unity)."),
  ("'Diversity does not divide, it enriches.' Explain with examples from the chapter. (5 marks)", "India has 4,635 communities, 325 languages and 25 scripts, yet people share staple grains, spices, the sari and dhoti, harvest festivals and the same epics and Pañchatantra stories. The variety in food, clothes and stories makes our culture rich and interesting, like many colours in one painting. The common values keep people together, so differences do not become divisions."),
  ("Why are the Rāmāyaṇa and Mahābhārata called the most striking case of unity in diversity? (5 marks)", "They are two long Sanskrit epics that might fill some 7,000 pages. They have been translated for over two millenniums into many languages, and regions and tribes have their own folk and oral versions, for example about a hundred Mahābhārata versions in Tamil Nadu alone. Tribes like the Bhils and Gonds, and the Irula of the Nilgiris, have legends of the heroes visiting their land. Thus one story is told in countless ways and links people across India and Asia."),
 ]),
]
CH["takeaways"] += ["Remember the numbers: **4,635 communities, 325 languages, 25 scripts**; Pañchatantra **2,200+ years old**, about **200 adaptations in 50+ languages**.",
  "In every example give **unity first, then diversity** with a named instance."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
