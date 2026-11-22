"""Class 7 Social Science Ch 10 - The Constitution of India: An Introduction (NCERT Ch 10): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c7sst_ch10"

def _base():
    s = importlib.util.spec_from_file_location("c7sst_c10", str(REPO / "src/rn_work/c7_sst/c10.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The Constitution of India came into effect on:", 1, "(c) 26 January 1950", "E", opts=["15 August 1947", "26 November 1949", "26 January 1950", "9 December 1946"]),
W("The Drafting Committee of the Constitution was chaired by:", 1, "(a) Dr. B.R. Ambedkar", "E", opts=["Dr. B.R. Ambedkar", "Dr. Rajendra Prasad", "Dr. Sachidananda Sinha", "Begum Aizaz Rasul"]),
W("The original Constitution is preserved in a glass case filled with:", 1, "(b) helium", "E", opts=["oxygen", "helium", "nitrogen", "carbon dioxide"]),
W("The idea of the Directive Principles of State Policy was inspired by the constitution of:", 1, "(d) Ireland", "E", opts=["France", "the USA", "Australia", "Ireland"]),
W("The ideals of liberty, equality and fraternity were adopted from the constitution of:", 1, "(a) France", "E", opts=["France", "the UK", "the USA", "Ireland"]),
W("The Preamble term which means that there is no official religion is:", 1, "(c) Secular", "E", opts=["Sovereign", "Socialist", "Secular", "Republic"]),
W("'Part IV-A: Fundamental Duties' was added to the Constitution in:", 1, "(b) 1976", "E", opts=["1950", "1976", "1992", "2004"]),
W("Fill in the blank: The Constituent Assembly was formed on ______ December 1946.", 1, "9 (1)", "E"),
W("Write True or False: The Constitution of India is the world's largest written constitution.", 1, "True. (1)", "E"),
W("Name the three organs of government.", 2, "The legislature, the executive and the judiciary. (1+1)", "E"),
W("Who took the oath to 'preserve, protect and defend' the Constitution, according to the chapter?", 1, "The president. (1)", "E"),
W("Who was the calligrapher who hand-wrote the text of the Constitution?", 1, "Prem Behari Narain Raizada. (1)", "E"),
W("Which artist, with his team, illustrated the pages of the Constitution?", 1, "Nandalal Bose. (1)", "E"),
W("What is a constitution? Define in one sentence.", 2, "It is a document that spells out a nation's basic principles and laws. (2)", "E"),
W("Name any two Fundamental Duties listed in the chapter.", 2, "Any two: to abide by the Constitution and respect its ideals and institutions, the National Flag and the National Anthem; to defend the country; to value our composite culture; to protect the natural environment; to strive for excellence; to provide opportunities for education to a child between 6 and 14 years. (1+1)", "E"),
W("What does 'We, the People of India' in the Preamble show?", 2, "It shows that the Constitution has been drawn up and enacted by the people through their representatives, not handed down by a king or any outside power. (2)", "E"),
W("What does the Preamble mean by 'Republic'?", 1, "The head of the state is an elected person and not a hereditary position. (1)", "E"),
W("Who was the Chairman of the Constituent Assembly, as stated in the chapter?", 1, "Dr. Rajendra Prasad. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Why do we need a constitution? Use the kabaddi example.", 3, "A constitution is like a rulebook for the country (1). In the kabaddi match the referee and captains settled the dispute with the rulebook (1). Without a rulebook that all agree to follow, disputes cannot be settled fairly; in the same way a country needs a constitution accepted by all (1).", "M"),
W("List any three things that a constitution lays out, according to the chapter.", 3, "Any three: the framework of the three organs and their roles; checks and balances among them; the rights and duties of citizens; the long-term goals and aspirations of the nation. (1 each)", "M"),
W("Describe the Constituent Assembly: when it was formed, its membership and how members were chosen.", 3, "Formed on 9 December 1946 with 389 members, later reduced to 299 after the Partition, of which 15 were women (1.5). Members were elected by the legislative assemblies of the provinces (who had in turn been elected by the people), and represented India's diverse regions, professions and social groups (1.5).", "M"),
W("Timeline. Arrange: (i) Constitution came into effect (ii) Constitution adopted (iii) Constituent Assembly formed (iv) Fundamental Duties added. Give the date or year.", 3, "(iii) 9 December 1946; (ii) 26 November 1949; (i) 26 January 1950; (iv) 1976. (3 for all correct, 2 for three correct)", "M"),
W("Why was it important for the Constituent Assembly to have members from diverse backgrounds?", 3, "India is a large, culturally diverse country with many regions and social groups (1). Members from diverse backgrounds could bring different problems and viewpoints (1), so the Constitution would represent all and be accepted by all (1).", "M"),
W("Source-based. 'I wish your labours success... a vision which may restore India to her pristine glory.' (Dr. Sachidananda Sinha). (i) Who was he? (ii) What qualities did he wish for the proceedings?", 3, "(i) President of the Constituent Assembly at the start of the writing of the Constitution (1). (ii) Good sense, public spirit, genuine patriotism, wisdom, toleration, justice and fairness to all (2, any four qualities).", "M"),
W("Name three ways in which the Indian freedom movement influenced the Constitution.", 3, "Ideals of equality, justice, freedom and fraternity; preservation of India's cultural heritage (1); many leaders of the freedom movement were in the Constituent Assembly and carried their experience (1); the idea of using the Constitution as a tool to achieve these ideals (1).", "M"),
W("How did India's civilisational heritage shape the Constitution? Give two examples.", 3, "Principles in our culture, such as acceptance of different points of view, respect for nature, learning, respect for women, vasudhaiva kutumbakam and sarve bhavantu sukhinah, find a place in the Constitution (1.5). Our tradition's emphasis on the duties of people in governance led to Fundamental Duties (1.5).", "M"),
W("Match the borrowing: (a) liberty, equality, fraternity (b) Directive Principles (c) independent judiciary with (1) USA (2) Ireland (3) France.", 3, "(a) with (3); (b) with (2); (c) with (1). (1 each)", "M"),
W("Differentiate between Fundamental Rights and Directive Principles of State Policy.", 3, "Fundamental Rights are promises that must be kept: if someone is treated unfairly, one can go to court and the judge can help (1.5). Directive Principles are goals that the government should try to achieve, like guidelines; one cannot go to court if the government does not follow them (1.5).", "M"),
W("Why did the framers keep both Fundamental Rights and Directive Principles?", 2, "They wanted some rights that could be demanded immediately (Fundamental Rights) (1) and some bigger goals that might take time to achieve as the country progressed (Directive Principles) (1).", "M"),
W("Mark the mistake and correct it: 'The Constitution cannot be changed, so no changes have happened since 1950.'", 2, "Wrong. The Constitution is a living document and can be amended after rigorous debate in Parliament (1). Examples: Fundamental Duties were added in 1976 and Panchayati Raj in 1992 (1).", "M"),
W("Explain the 2004 flag case. Which right did the Supreme Court say it protects?", 3, "Earlier people could not fly the national flag at their homes (1). In 2004 a citizen challenged this rule in court as his right to express pride in his country (1). The Supreme Court agreed that flying the flag is part of the Fundamental Right to Freedom of Expression, though the flag must never be dishonoured (1).", "M"),
W("Explain 'Sovereign' and 'Democratic' as used in the Preamble.", 3, "Sovereign: the people have supreme right to make decisions on internal and external matters; no external power can dictate to India (1.5). Democratic: people enjoy equal political rights, elect their rulers and hold them accountable; the government is run by basic rules (1.5).", "M"),
W("What does the Preamble mean by 'Socialist'? When was the word added?", 2, "Wealth is generated socially and should be shared by society; the government should regulate the ownership of land and industry to reduce socio-economic inequalities (1). It was added, with 'Secular', by the 42nd Amendment in 1976 (1).", "M"),
W("Match the Preamble words with the meaning: (a) Justice (b) Liberty (c) Fraternity with (1) all behave like members of one family (2) no unreasonable restriction on thought and expression (3) no discrimination on caste, religion or gender.", 3, "(a) with (3); (b) with (2); (c) with (1). (1 each)", "M"),
W("Name three guiding Directive Principles shown in the chapter's infographic.", 3, "Any three of: social, political and economic justice; protection of the environment and wildlife; nutrition, standard of living and public health; protection of monuments and places of national importance; a uniform civil code; welfare government. (1 each)", "M"),
W("Why do the president, the prime minister, ministers and judges take an oath to the Constitution? What does the oath show about its position?", 3, "The president takes an oath to preserve, protect and defend the Constitution, and the prime minister, ministers and judges promise to follow its provisions (1.5). It shows that the Constitution is the supreme document and all officials and organs must act within it (1.5).", "M"),
# ---------------- HARD ----------------
W("Source-based. 'We have prepared a democratic Constitution. But the successful working of democratic institutions requires... willingness to respect the viewpoint of others, capacity for compromise and accommodation.' (Dr. Rajendra Prasad). Explain what he is telling the people and the representatives.", 4, "He says that only writing a democratic Constitution is not enough (1). Democracy works only when people respect others' viewpoints (1) and are ready to compromise and accommodate (1). So it needs the efforts of all citizens and leaders, with hard work and moral regeneration (1).", "H"),
W("Source-based. Begum Aizaz Rasul said on 22 November 1949 that the equality of women was 'no new concept'. (i) What is her main argument? (ii) Which principle of the Preamble does it link with?", 4, "(i) She argued that complete equality of women with men is an ideal long cherished in India, even though social conditions had at times tragically debased it, and the Constitution affirms it and assures that women's rights in law will be honoured (2). (ii) Equality (and justice): the Preamble says all are equal before law, and that social inequalities must end, with equal opportunity for all (2).", "H"),
W("Case study. In Rohan's village the well is used only by some castes. His teacher says that 'all citizens are equal before the law' and 'Justice' is a Preamble value. Explain how the Constitution supports Rohan's argument that all should use it and suggest two actions.", 4, "The Preamble's Justice means citizens cannot be discriminated on caste, religion or gender, and social inequalities must be reduced (1.5). Equality means all are equal before the law (1). Actions: awareness and discussion in the village, complaining to the authorities or going to court if rights are denied, and treating all as fellow citizens (fraternity) (1.5).", "H", wp=True),
W("The chapter says the Constitution is both a guide and a 'living document'. Explain with three examples of change over time.", 4, "It is a guide because it lays out the framework of government, rights, duties and values (1). It is living because new needs arise and it can be amended after rigorous debate in Parliament (and sometimes in legislative assemblies, with public views) (1). Examples: Fundamental Duties added 1976; Socialist and Secular added to the Preamble in 1976; Panchayati Raj added by the 73rd Amendment in 1992; also the number of parts grew from 22 to 25 and schedules from 8 to 12 (2, any two).", "H"),
W("Case study. A class wants to make a 'class constitution' for its monitors, with rules, rights, duties and goals. Using the chapter, list four things it should contain and say which feature of the national Constitution each is similar to.", 4, "(1 each) Rules for how monitors are chosen and work (framework and structure of government); rights of all students to be heard (Fundamental Rights); duties of students to keep the class clean and help each other (Fundamental Duties); goals such as helping every child to learn (Directive Principles / Preamble values).", "H", wp=True),
W("How do the 'checks and balances' and 'separation of powers' protect democracy? Use the three organs in your answer.", 4, "The legislature makes laws, the executive implements them, and the judiciary ensures laws are in accordance with the Constitution and decides whether a law has been broken (2). The Constitution defines the roles and accountability of each organ, and the organs work independently, so no one organ can misuse power (2).", "H"),
W("'Fundamental Rights are promises that must be kept.' Support this with one example from the chapter and say how the court helps.", 3, "A person treated unfairly for who they are can go to court and the judge can help (1). Example: Right to Equality (equality before law), Right to Freedom (protection of life and personal liberty) or the Right to Education; the Supreme Court also protected the right to fly the flag as freedom of expression (2).", "H"),
W("Why did India give universal adult franchise from the beginning? Give two reasons from the chapter.", 3, "The Constitution's ideals are equality of all and justice for all (1), and the freedom struggle's values show that every adult citizen should have a say in choosing representatives (1). A large, diverse country needs everyone's voice; the Constitution answers the 'how do we make sure every adult has the right to vote' question (1).", "H"),
W("Read the Preamble terms. Choose three and give an example of each from daily life in India.", 4, "(any three, 1.5 each, 4 marks total) Sovereign: India takes its own decisions in internal and foreign matters; Secular: a person can practise the rituals of any religion, as no religion is official; Republic: head of state, the President, is elected; Justice: equal opportunity in jobs regardless of gender, caste, religion; Liberty: free to express thoughts; Equality: all treated equally before law; Fraternity: treating all fellow citizens as family.", "H", wp=True),
W("Describe the work of the Drafting Committee and Dr. B.R. Ambedkar's role. Distinguish the date of adoption from the date the Constitution came into effect.", 4, "The initial text of the Constitution was prepared by the Drafting Committee chaired by Dr. Ambedkar, an eminent social reformer and the first Law and Justice minister (2). Drafting took almost three years; it was adopted on 26 November 1949 but came into effect on 26 January 1950 (Republic Day) (2).", "H"),
W("Do you agree: 'The Constitution has fully achieved all its ideals'? Give two points showing the challenges and two ways citizens can help.", 5, "The chapter asks us to think about whether we have achieved all ideals; there are still problems such as discrimination and inequality (any two, 2). Citizens can: follow the Fundamental Duties, treat everyone with respect, vote, protect the environment, give feedback on laws, avoid discrimination (any two, 2). Concluding view with reason (1).", "H"),
W("Which values and ideals from the freedom struggle and from civilisational heritage appear in the Preamble? Link at least four of them.", 4, "Freedom struggle: justice, liberty, equality, fraternity (2). Heritage: fraternity ('world is one family'), the idea of all well-being, respect for different viewpoints which supports liberty and secularism, and duties of people (2).", "H"),
]

WS += [
W("Case study. Meera, a farmer's daughter in Rajasthan, is the first girl in her family to go to school. Her father says the government has made a promise about the education of children aged 6 to 14. (i) Which Fundamental Duty or right is involved? (ii) Whose responsibility is it? (iii) Why is education linked to the Preamble's values?", 4, "(i) Article 21-A, the right to education, and the Fundamental Duty of a parent or guardian to provide opportunities for education to a child between six and fourteen (2). (ii) Shared: the State must provide, and parents or guardians must send their children (1). (iii) Education helps equality of opportunity, justice and the liberty to think and act freely (1).", "H", wp=True),
W("Use the Constitution's three-tier structure and separation of powers to explain: who makes laws, who implements them and who decides disputes, at the central level, and which local system was added in 1992?", 4, "At the centre, the legislature (Parliament) makes laws, the executive headed by the prime minister implements them, and the judiciary decides whether a law is in accordance with the Constitution and whether it has been broken (3). The three-tier system has central, state and local levels; the Panchayati Raj system was added by the 73rd Amendment in 1992 (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "10.8 Timeline of the Making of the Constitution"),
 ("table", ["Date / year", "Event"], [
  ["1789", "French Revolution; Declaration of the Rights of Man and of the Citizen (liberty, equality, fraternity)"],
  ["9 December 1946", "Constituent Assembly formed: 389 members (later 299 after Partition), 15 women"],
  ["22 November 1949", "Begum Aizaz Rasul speaks in the Assembly on women's equality"],
  ["26 November 1949", "Constitution adopted after almost three years of work"],
  ["26 January 1950", "Constitution comes into effect (Republic Day)"],
  ["1976", "Part IV-A, Fundamental Duties added; 'Socialist' and 'Secular' added to the Preamble (42nd Amendment)"],
  ["1992", "73rd Amendment brings the Panchayati Raj system into the Constitution"],
  ["2004", "Supreme Court: flying the national flag is part of freedom of expression"]]),
 ("note", "IMPORTANT", "Keep two dates apart: **26 November 1949** (adopted) and **26 January 1950** (came into effect, celebrated as Republic Day)."),
 ("h2", "10.9 Key Terms and Key People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Constitution**", "The document that spells out a nation's basic principles and laws"],
  ["**Constituent Assembly**", "The body that wrote the Constitution (1946-1949)"],
  ["**Drafting Committee**", "Prepared the initial text, chaired by Dr. B.R. Ambedkar"],
  ["**Fundamental Rights**", "Promises the courts will enforce, e.g. equality and freedom"],
  ["**Fundamental Duties**", "Duties of citizens, such as respecting the flag, protecting the environment"],
  ["**DPSP**", "Directive Principles of State Policy: goals the government should try to achieve; not enforceable in court"],
  ["**Amendment**", "A change made to the Constitution"],
  ["**Preamble**", "The statement at the beginning that tells the values the Constitution upholds"],
  ["**Dr. Rajendra Prasad**", "Chairman of the Constituent Assembly; first President of India"],
  ["**Dr. Sachidananda Sinha**", "President of the Constituent Assembly at the start of the process"],
  ["**Begum Aizaz Rasul**", "Member who spoke on women's equality"],
  ["**Nandalal Bose / Prem Behari Narain Raizada**", "Illustrator / calligrapher of the original Constitution"]]),
 ("h2", "10.10 Sources of Influence at a Glance"),
 ("table", ["Source", "What the Constitution took"], [
  ["Indian freedom movement", "Equality, justice, freedom, fraternity; universal adult franchise; rights; the Constitution as a tool to achieve ideals"],
  ["India's civilisational heritage", "Acceptance of different views, nature as sacred, respect for women, vasudhaiva kutumbakam, duties of people"],
  ["France", "Liberty, equality, fraternity"],
  ["Ireland", "Directive Principles of State Policy"],
  ["USA", "An independent judiciary"],
  ["UK, Australia and others", "Studied for their democratic systems"]]),
 ("h2", "10.11 Map and Picture Pointers"),
 ("ul", ["Locate **Kartavya Path** in Delhi (the Republic Day Parade); the Constitution is preserved in **Parliament**.",
  "Look at the illustrations in the Constitution (Figs. 10.6 to 10.13): a gurukula, scene from the Ramayana, Krishna and Arjuna (Gita), Orissan sculpture, Nataraja, the Bhagiratha relief at Mahabalipuram, Akbar and Mughal architecture, Nalanda. They show the heritage from ancient to modern India.",
  "Fig. 10.14 groups the parts of the Constitution (Fundamental Rights, Fundamental Duties and Directive Principles) with examples; Fig. 10.16 shows the Preamble with the meaning of each key word."]),
 ("h2", "10.12 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Need to decide how a large and diverse India would govern itself", "Constituent Assembly set up in 1946"],
  ["Freedom struggle leaders sat in the Assembly", "Values of equality, justice, freedom, fraternity entered the Constitution"],
  ["India's tradition stressed the duties of people", "Fundamental Duties included in 1976"],
  ["Need for new laws over time", "Provision for amendments; e.g. Panchayati Raj in 1992"],
  ["Citizen challenged the flag rule", "2004 Supreme Court ruling on freedom of expression"]]),
 ("h2", "10.13 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("How was the Constitution of India prepared? (5 marks)", "A Constituent Assembly was formed on 9 December 1946 with 389 members (299 after Partition), including 15 women. Its members were elected by the provincial legislative assemblies and represented diverse regions, professions and groups. Dr. Rajendra Prasad was its Chairman and a Drafting Committee chaired by Dr. B.R. Ambedkar prepared the initial text. After almost three years the Constitution was adopted on 26 November 1949 and came into effect on 26 January 1950."),
  ("Explain the Preamble and its key words. (5 marks)", "The Preamble states the guiding values. 'We, the People of India' means the people enacted it. India is Sovereign, Socialist, Secular, Democratic and a Republic. It secures Justice, Liberty, Equality and Fraternity. Sovereign means no external power can dictate; Socialist means wealth shared and inequalities reduced; Secular means no official religion and equal respect to all; Democratic means people elect rulers and hold them accountable; Republic means an elected head of state; Justice means no discrimination; Liberty means no unreasonable restrictions on thoughts; Equality means equal before law; Fraternity means behaving like one family."),
  ("Why is the Constitution called a living document? (3 marks)", "New needs arise over time, so the Constitution can be amended after rigorous debate in Parliament and sometimes in the state legislatures and with public views. Fundamental Duties were added in 1976 and Panchayati Raj in 1992. Popular movements and citizens' cases, like the flag case in 2004, can lead to change."),
  ("Differentiate between Fundamental Rights and the DPSP. (3 marks)", "Fundamental Rights can be demanded in court right away; DPSP are goals or guidelines which the government should work towards, and one cannot go to court if they are not followed."),
 ]),
]
CH["takeaways"] += ["Learn the numbers: **389 to 299** members, **15** women, **9 Dec 1946**, **26 Nov 1949**, **26 Jan 1950**, **22 parts and 8 schedules** (then) to **25 parts and 12 schedules** (now).",
  "Preamble words: **Sovereign, Socialist, Secular, Democratic, Republic**; **Justice, Liberty, Equality, Fraternity**."]

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
