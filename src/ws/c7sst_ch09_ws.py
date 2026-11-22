"""Class 7 Social Science Ch 9 - Understanding Types of Governments (NCERT Ch 9): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c7sst_ch09"

def _base():
    s = importlib.util.spec_from_file_location("c7sst_c09", str(REPO / "src/rn_work/c7_sst/c09.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The creation of rules for a country is known as the:", 1, "(a) legislative function", "E", opts=["legislative function", "executive function", "judicial function", "military function"]),
W("In which country do citizens take part directly in decisions in some forms of direct democracy, as the chapter mentions?", 1, "(c) Switzerland", "E", opts=["India", "Saudi Arabia", "Switzerland", "Iran"]),
W("The Upper House of the Indian Parliament is called the:", 1, "(b) Rajya Sabha", "E", opts=["Lok Sabha", "Rajya Sabha", "Senate", "National Assembly"]),
W("In a presidential democracy, the president:", 1, "(d) is elected by the people and does not need the legislature's confidence", "E", opts=["is chosen only by the Lok Sabha", "is a nominal head with no power", "is a hereditary ruler", "is elected by the people and does not need the legislature's confidence"]),
W("Which country is given as an example of an absolute monarchy in the chapter?", 1, "(a) Saudi Arabia", "E", opts=["Saudi Arabia", "United Kingdom", "South Korea", "Australia"]),
W("The word 'oligarchy' comes from Greek 'olígos', which means:", 1, "(c) a few", "E", opts=["a king", "religion", "a few", "all people"]),
W("The chapter says that in a constitutional monarchy, real executive power is exercised by the:", 1, "(b) prime minister", "E", opts=["king or queen", "prime minister", "Supreme Leader", "chancellor"]),
W("Fill in the blank: ______ means that the government is answerable to the people who elected it.", 1, "Accountability (1)", "E"),
W("Write True or False: In India, general elections are held every five years.", 1, "True. (1)", "E"),
W("Name the three functions of government.", 2, "Legislative (making rules), executive (implementing them) and judicial (ensuring they are followed). (1+1)", "E"),
W("Who described democracy as 'government of the people, by the people, for the people'?", 1, "Abraham Lincoln, a U.S. president. (1)", "E"),
W("What is a constitution?", 2, "It is a book of fundamental rules of the country that decides how the government will work. (2)", "E"),
W("Name any two countries mentioned as theocracies in the chapter.", 2, "Any two: Iran, Afghanistan, Vatican City. (1+1)", "E"),
W("What is a republic?", 2, "A form of government in which the head of state is elected and is not a hereditary monarch. (2)", "E"),
W("Which Indian ancient mahajanapada, with the Lichchhavi clan, is mentioned as an early republic?", 1, "The Vajji (Vriji) mahajanapada. (1)", "E"),
W("What do the Uttaramerur inscriptions of the Chola period describe?", 2, "They describe the election of members to the village sabha, including sealed ballot boxes, qualifications and duties of members, and conditions for dismissal. (2)", "E"),
W("In a school example, which method of forming the student committee was the democratic one?", 1, "Students from each grade choose their representatives by voting. (1)", "E"),
W("Name the two Houses of the Indian Parliament and say which is the Lower House.", 2, "Lok Sabha and Rajya Sabha; the Lok Sabha is the Lower House. (1+1)", "E"),
# ---------------- MEDIUM ----------------
W("Explain the three ways of forming the student committee in the chapter. Which one is best and why?", 3, "(i) All students join: difficult to decide and implement; (ii) Head Teacher chooses: many students have no voice; (iii) each grade elects a representative by voting (1+1). The third is best because every grade is represented and decisions can be taken practically (1).", "M"),
W("State any three of the four key questions on which one form of government differs from another.", 3, "Any three: who decides that 'this is the government' (source of authority); how the government is formed; what the different parts of government are and what they do; what the government is working for (its goals and values). (1 each)", "M"),
W("Distinguish between direct and representative democracy. Why is direct democracy difficult in a large country?", 3, "In direct democracy all citizens take part directly in all decisions (as in some forms in Switzerland); in representative democracy people elect representatives to govern (1+1). In a large country it is very hard to involve everyone in every decision, just as it would be hard if everyone in school sat on the student committee (1).", "M"),
W("Differentiate between parliamentary and presidential democracy with respect to the executive.", 3, "In a parliamentary democracy the executive (prime minister and council of ministers) are members of the legislature and continue only while they have its confidence (India) (1.5). In a presidential democracy the executive works independently of the legislature and the president is elected by the people, not needing the legislature's confidence (1.5).", "M"),
W("Complete the table from the chapter. India: executive ___; USA: executive ___; South Korea: legislature ___.", 3, "India: prime minister and council of ministers; USA: president; South Korea: single house (National Assembly). (1 each)", "M"),
W("What is 'separation of power'? Name the three organs.", 3, "It means that the three organs of government work independently and do not interfere in each other's functions (2). The organs are the legislature, the executive and the judiciary (1).", "M"),
W("Why is an independent judiciary important in a democracy? Give two reasons.", 3, "It ensures that every citizen's fundamental rights are protected (1.5), and that laws are followed by citizens and also by all parts of the government (1.5).", "M"),
W("Explain 'universal adult franchise' with the examples of India and Switzerland.", 3, "It gives every citizen above a certain age the right to vote for their representatives (1). India provided it from the beginning of the Republic in 1950 (1); in Switzerland women got the right to vote only in 1971 (1).", "M"),
W("Mark the mistake and correct it: 'In absolute monarchy the monarch shares law-making with an elected parliament, as in Britain.'", 2, "Wrong. In an absolute monarchy the monarch has complete control over making, enforcing and judging laws (e.g. Saudi Arabia) (1). Britain is a constitutional monarchy, where the elected parliament makes laws (1).", "M"),
W("How is a constitutional monarchy different from an absolute monarchy? Give an example of each.", 3, "In an absolute monarchy the monarch holds all power (Saudi Arabia) (1.5). In a constitutional monarchy the monarch is the nominal head of state, parliament makes laws and the prime minister with ministers holds executive power (United Kingdom) (1.5).", "M"),
W("Source-based. 'The Supreme Leader, who has the ultimate authority over the legislature, executive and judiciary, is selected by a group of Islamic clerics and his term is for life.' (i) Which country is described? (ii) Why is it a theocracy? (iii) What elected bodies exist there?", 3, "(i) Iran (1). (ii) Its constitution is based on Islamic principles and the head with ultimate authority is chosen by clerics, so religion and religious leaders rule (1). (iii) There is also an elected president and a parliament for everyday governance (1).", "M"),
W("What is a dictatorship? Name two dictators mentioned in the chapter and the countries they ruled.", 3, "A form of government in which one person or a small group has absolute power, with no limits from a constitution or law (1). Adolf Hitler (Germany) and Idi Amin (Uganda) (1+1).", "M"),
W("What is an oligarchy? How can a democracy show signs of oligarchy?", 3, "A government in which a small, powerful group, usually wealthy families or influential people, makes all the important decisions (1.5). A democracy can show signs of it when a small group of politicians and wealthy businesspeople hold too much influence in governance (1.5).", "M"),
W("Priya's grandfather says, 'In a democracy, the people can change a government that does not work.' How can they do this, and what does it show?", 3, "Through regular elections people can change their representatives (1.5). It shows the government is accountable to the people and there is a constant check on what it does (1.5).", "M", wp=True),
W("Match the practice with the type of government: (a) The government refers to a religious leader for each decision (b) After the queen's death her son became king (c) The ruler is not bound by any constitution with (1) Dictatorship (2) Monarchy (3) Theocracy.", 3, "(a) with (3) theocracy; (b) with (2) monarchy; (c) with (1) dictatorship. (1 each)", "M"),
W("Timeline. The chapter gives the year democracy was established in some countries. Arrange these in order from earliest to latest: Nepal, Germany, the USA, Kenya, Switzerland.", 3, "USA (1787), Switzerland (1848), Germany (1949), Kenya (1964), Nepal (2008). (1 mark for correct order of any three, 3 for all five)", "M"),
W("Explain how the Vajji republic shows that India has an old tradition of democratic practices.", 3, "In Vajji, especially the Lichchhavi clan practised collective decision-making (1). Leaders were chosen by merit rather than birth, key positions were filled by elections (1), and representatives of the clans met regularly to solve problems for people's welfare (1).", "M"),
W("In ancient Greece, free men could vote but not women, workers and slaves. What does this tell us about early republics compared to modern democracy?", 2, "Early republics gave voting rights only to some groups (1), whereas modern democracy aims at universal adult franchise and equality for all citizens (1).", "M"),
W("Why are elections held at regular, fixed intervals in a representative democracy? Give the examples of India and the USA.", 3, "They let people express changes in their choices and make the government answerable to them (2). General elections are held every five years in India and every four years in the USA (1).", "M"),
# ---------------- HARD ----------------
W("Source-based. King Chandrapida wanted to build a temple but a cobbler's hut stood in the way. The king sought the cobbler's permission respectfully and paid compensation. (i) Where is this story from? (ii) What does it say about rajadharma? (iii) Is it a democracy? Give a reason.", 4, "(i) Rajatarangini by Kalhana, a 12th-century CE Kashmiri scholar (1). (ii) A king should rule by dharma and respect even a lowly subject's rights, without false pride (1.5). (iii) No, it is a monarchy; but it shows that a king could be expected to follow dharma and treat people fairly (1.5).", "H"),
W("'In many parts of India the power of the raja was neither absolute nor beyond question.' Explain with two examples from the chapter.", 4, "Kings were guided by sabha and samiti, and ministers, officials and scholars advised them (2). The king was expected to follow rajadharma, ruling by dharma and ensuring the welfare of all people; Bhishma's advice to Yudhishthira says a king must apply law without bias and that his authority is temporary and bound by dharma (2).", "H"),
W("Case study. Shane lives in a country where the government decides every citizen's haircut and clothes, blocks the global internet and expects people to report anyone who breaks the rules. (i) Does it look like a democracy? (ii) Which type of government is it closest to? (iii) Two rights absent for its people.", 4, "(i) No, the government does not follow the principles of a democracy (1). (ii) It is closest to a dictatorship, where one person or a small group has absolute power with no limits (1). (iii) Any two: freedom of speech and expression, freedom to make one's own choices, equality and rights protected by an independent judiciary (2).", "H", wp=True),
W("Why did Hitler become a dictator, and what were the effects of his rule? Answer in five lines.", 4, "After he was appointed Chancellor of Germany in 1933, he passed laws giving himself full power and eliminated the opposition (1). He believed in the superiority of his own people and that Germany should rule the world (1). He was responsible for the killing of at least six million Jews (the Holocaust) and hundreds of thousands of Roma and others (1). His actions caused World War II (1939-1945), which led to huge loss of life and property (1).", "H"),
W("Compare India, the USA, South Korea and Australia on one feature of the legislature and one feature of the executive.", 4, "India: two houses, Lok Sabha more powerful than Rajya Sabha; executive is PM and council of ministers (1). USA: Senate and House of Representatives have equal power; executive is the president (1). South Korea: single house (National Assembly); president as executive (1). Australia: Senate and House of Representatives with equal power; PM and council of ministers (1).", "H"),
W("The chapter calls the principles of democracy 'ideals'. Support this with two facts from the chapter.", 4, "Democracies evolved over time: India gave universal adult franchise from 1950, while in Switzerland women got the vote only in 1971 (2). Effective universal adult suffrage came in the UK in 1928 and in the USA by 1965 (1). So not all democracies have fully practised the principles; citizens must keep the ideals in front of them (1).", "H"),
W("Fill in the characteristics for democracy and its rivals: universal adult franchise, equality among citizens, freedom of speech, separation of powers. What does the table tell us about why democracy is considered better?", 4, "In a democracy all four are present (Yes), while in a dictatorship, absolute monarchy and oligarchy they are absent (No) (2). In a democracy people choose their government, speak and believe freely so long as they do not harm others' rights, and can change representatives, so the government works for the well-being of all (2).", "H"),
W("Case study. A town council in the country 'X' has elected members, but a few rich businessmen decide every major decision and the people cannot get information. (i) Which form of government does it resemble? (ii) Which hurdles of democracy does it show? (iii) Suggest two things citizens can do.", 5, "(i) It resembles an oligarchy, a small powerful group making the decisions (1). (ii) Excessive control by a few over democratic institutions, wealth disparity and manipulation of information channels (2). (iii) Any two: vote and elect honest representatives, ask for information and question the government, support free media and independent institutions, stay vigilant (2).", "H", wp=True),
W("Justify the statement: 'India is a representative parliamentary democracy.' Give four points.", 4, "People elect representatives through universal adult franchise (1). General elections are held every five years (1). The prime minister and council of ministers are members of Parliament (1) and remain in office as long as they have the confidence of the Lok Sabha; the judiciary is independent (1).", "H"),
W("What are the hurdles to achieving the ideals of democracy? Suggest how individuals and society can minimise any three of them.", 5, "Hurdles: corruption, wealth disparity, excessive control by a few, erosion of the judiciary's independence, manipulation of information (any three named, 1.5). Ways: honest voting and refusal to take or give bribes; support for equal opportunities and welfare of the poor; free and fair media and awareness; respect for independent courts; staying vigilant and taking part in civic life (any three linked, 3.5).", "H"),
W("Compare Britain and Iran on head of state, who holds real power, and the role of religion.", 4, "Britain: king or queen is head of state with only nominal power; the elected parliament and the prime minister hold real power; it is really a parliamentary democracy (2). Iran: the Supreme Leader, selected by clerics for life, has ultimate authority over all organs; a president and parliament are elected but the constitution is based on Islam, so religion shapes the government (2).", "H"),
W("Role play. A class forms a student committee with the principles of a democracy. List four steps you would follow and say which principle each step shows.", 4, "(1 each) Define the committee's functions (rules, implementation, checking) which links with the functions of government; ask every grade to elect its own representative by secret vote (representative participation); give every student an equal right to vote and to stand (equality, universal franchise); let students voice opinions and hold the committee accountable (freedom and accountability).", "H", wp=True),
]

WS.append(W("Bhishma's advice in the Shanti Parva lists the duties of a raja. Write four of them and say how they connect with the principles of a modern democracy.", 4, "Welfare of the people is the highest priority; apply the law without bias; do not get attached to power as it fosters ego and corruption; seek guidance from wise advisors; understand that authority is temporary and bound by dharma (any four, 2). Links: equality before law, accountability, consultation and limited power, and working for all (2).", "H"))

CH = _base()
CH["blocks"] += [
 ("h2", "9.9 Timeline and Dates to Remember"),
 ("table", ["Year / period", "Event or fact"], [
  ["5th-4th century BCE", "Republics in Rome and Greece (only some groups could vote)"],
  ["Ancient India (mahajanapadas)", "Vajji (Lichchhavi) as an early republic with collective decision-making"],
  ["10th century CE", "Uttaramerur inscriptions of the Chola period describe village sabha elections"],
  ["12th century CE", "Kalhana's Rajatarangini (story of King Chandrapida and the cobbler)"],
  ["1787", "Democracy established in the USA"],
  ["1848", "Switzerland"],
  ["1928 / 1965", "Effective universal adult suffrage in the UK / the USA"],
  ["1933", "Hitler appointed Chancellor of Germany; later World War II (1939-1945)"],
  ["1947 / 1949", "India / Germany establish democracy"],
  ["1950", "India provides universal adult franchise from the beginning of the Republic"],
  ["1964 / 1971", "Kenya / Swiss women get the right to vote (1971)"],
  ["2008", "Nepal"]]),
 ("note", "REMEMBER", "The dates differ for different countries and some principles came late. The chapter reminds us that principles of democracy are ideals which have evolved over time."),
 ("h2", "9.10 Key Terms and Key People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Representative**", "A person chosen to act or decide on behalf of a group of people"],
  ["**Legislature / executive / judiciary**", "Organs that make laws / implement them / see that they are followed"],
  ["**Universal adult franchise**", "The right of every adult citizen to vote"],
  ["**Accountability**", "The government is answerable to the people who elected it"],
  ["**Separation of power**", "The three organs work independently without interfering in one another"],
  ["**Sovereign**", "The source of a country's power is independent of external influence"],
  ["**Monarch**", "King or queen who inherits the position, usually within the royal family"],
  ["**Theocracy**", "Rule by religious law and religious leaders"],
  ["**Dictatorship**", "One person or a small group holds absolute power"],
  ["**Oligarchy**", "Rule by a few, from Greek olígos (few) and árkhō (rule)"],
  ["**Subjugate**", "To take control of people or a place by force"],
  ["**Rajadharma**", "Ruling by dharma, ensuring the welfare of all"],
  ["**Kautilya**", "Wrote that a ruler's duties are raksha, palana and yogakshema"],
  ["**Abraham Lincoln**", "Described democracy as 'of the people, by the people, for the people'"]]),
 ("h2", "9.11 Map and Picture Pointers"),
 ("ul", ["On a world map locate the countries named: **India, USA, Switzerland, Germany, Kenya, Nepal, South Korea, Australia, Saudi Arabia, United Kingdom, Iran, Afghanistan, Vatican City, Uganda**. Group them by type of government.",
  "Within India: **Uttaramerur (Tamil Nadu)**; Vajji (the Lichchhavi clan; north Bihar region in the mahajanapada map); Rajasthan and Kerala as states under the Union government.",
  "Fig. 9.1 (Parliament), Fig. 9.5 (voting in India), Fig. 9.6 (Uttaramerur inscriptions), Fig. 9.8 (Bhishma teaching Yudhishthira) and Fig. 9.9 (King Charles III) are the pictures the chapter uses."]),
 ("h2", "9.12 Reading the Sources"),
 ("table", ["Source", "What we learn"], [
  ["Kautilya's Arthashastra", "Ruler's three duties: raksha, palana, yogakshema"],
  ["Abraham Lincoln", "Democracy as government of, by and for the people"],
  ["Uttaramerur inscriptions", "Detailed rules for the election of village sabha members, dismissal for corruption"],
  ["Shanti Parva (Bhishma to Yudhishthira)", "A king's duties: welfare of people, unbiased law, no attachment to power, advice of the wise"],
  ["Rajatarangini (Kalhana)", "King Chandrapida respects a cobbler's rights and pays him compensation"],
  ["Table 9.1", "Differences in executive, legislature and judiciary among India, USA, South Korea, Australia"]]),
 ("h2", "9.13 Comparison of the Main Forms of Government"),
 ("table", ["Form", "Who holds power", "Example"], [
  ["Direct democracy", "All citizens decide directly", "Some forms in Switzerland"],
  ["Parliamentary democracy", "Executive is part of the legislature and needs its confidence", "India, Australia"],
  ["Presidential democracy", "Elected president independent of the legislature", "USA, South Korea"],
  ["Absolute monarchy", "Monarch with complete control", "Saudi Arabia"],
  ["Constitutional monarchy", "Nominal monarch; elected parliament and PM", "United Kingdom"],
  ["Theocracy", "Religious law and leaders", "Iran, Vatican City"],
  ["Dictatorship", "One person or small group, absolute power", "Hitler, Idi Amin"],
  ["Oligarchy", "A small, wealthy or powerful group", "Ancient Greek aristocratic states"]]),
 ("h2", "9.14 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Why does democracy matter? (3 marks)", "In a democracy people choose and can change their government through elections, so it is accountable. People can speak, dress and believe freely as long as they do not harm others' rights. The government has to protect rights and provide basic needs, and works for the well-being of all."),
  ("Explain the difference between monarchy, dictatorship and democracy. (5 marks)", "In a monarchy a king or queen, usually from the royal family, rules; in an absolute monarchy he or she has complete power, while in a constitutional monarchy power is nominal and an elected parliament governs. In a dictatorship one person or small group holds absolute power without limits from constitution or law. In a democracy the people are the source of authority and elect representatives; there is equality, freedom, universal adult franchise, separation of powers and an independent judiciary."),
  ("What are the problems that democracies face today? How can citizens help? (5 marks)", "Corruption, wealth disparity, excessive control by a few over institutions, erosion of the judiciary's independence and manipulation of information channels. Citizens can stay vigilant, vote wisely, ask for accountability, support independent institutions and share correct information."),
  ("How does the chapter show that India has old roots of republican traditions? (3 marks)", "The Vajji mahajanapada, especially the Lichchhavi clan, chose leaders on merit and had regular meetings of representatives, so they are called early republics. The Uttaramerur inscriptions of the Chola period describe village sabha elections with sealed ballot boxes and dismissal for corruption."),
 ]),
]
CH["takeaways"] += ["Do not mix up: **parliamentary** (executive from the legislature) and **presidential** (executive elected separately); **absolute** and **constitutional** monarchy.",
  "Always give an example: Switzerland (direct), India (parliamentary), USA (presidential), Saudi Arabia, UK, Iran, Hitler."]

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
