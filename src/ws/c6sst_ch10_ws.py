"""Class 6 Social Science Ch 10 - Grassroots Democracy Part 1: Governance: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch10"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c10", str(REPO / "src/rn_work/c6_sst/c10.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The process of taking decisions, organising society with rules and making sure they are followed is called:", 1, "(c) governance", "E", opts=["trade", "migration", "governance", "tourism"]),
W("The organ of government that makes laws is the:", 1, "(a) legislature", "E", opts=["legislature", "executive", "judiciary", "police"]),
W("The organ of government that implements the laws is the:", 1, "(b) executive", "E", opts=["legislature", "executive", "judiciary", "Parliament only"]),
W("The system of courts that decides whether someone broke the law is the:", 1, "(d) judiciary", "E", opts=["legislature", "executive", "cyber police", "judiciary"]),
W("India's two houses of Parliament are:", 1, "(b) Lok Sabha and Rajya Sabha", "E", opts=["Vidhan Sabha and Lok Sabha", "Lok Sabha and Rajya Sabha", "Rajya Sabha and Gram Sabha", "High Court and Supreme Court"]),
W("The Government of India's motto is:", 1, "(a) Satyameva Jayate", "E", opts=["Satyameva Jayate", "Yato Dharmastato Jayah", "Vasudhaiva Kutumbakam", "Jai Hind"]),
W("Members of Parliament are called:", 1, "(c) MPs", "E", opts=["MLAs", "MLCs", "MPs", "MDs"]),
W("The word 'democracy' comes from which language?", 1, "(d) Greek", "E", opts=["Latin", "Sanskrit", "Persian", "Greek"]),
W("Fill in the blank: In India, the government works at three levels: local, State and ______.", 1, "Central (Union or national). (1)", "E"),
W("Write True or False: The President of India is the nominal head of the executive.", 1, "True. The Prime Minister is the real executive head at the Centre. (1)", "E"),
W("Write True or False: Rules and laws can never be changed.", 1, "False. Citizens have a say in the laws and rules, and they can be updated. (1)", "E"),
W("Who is the nominal head of a State government?", 1, "The Governor. (1)", "E"),
W("What is the Supreme Court's motto and what does it mean?", 2, "Yato Dharmastato Jayah: 'Where there is dharma, there is victory.' (2)", "E"),
W("Name the legislative house of a State.", 1, "The State Assembly or Vidhan Sabha. (1)", "E"),
W("What does 'dēmos' mean and what does 'kratos' mean?", 2, "Dēmos means 'people' and kratos means 'rule' or 'power'. (1+1)", "E"),
W("Give two examples of places where we have to follow rules, according to the chapter.", 2, "Any two: home, school, examinations, roads (traffic rules), the workplace. (1+1)", "E"),
W("What is the minimum age for an Indian citizen to vote?", 1, "18 years. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Write one-line meanings of 'governance', 'government' and 'law'.", 3, "Governance is the process of taking decisions, organising society with rules and ensuring they are followed (1). Government is the group or system that makes and enforces the rules (1). Laws are the more important rules (1).", "M"),
W("Why do we need rules when a large number of people live together?", 2, "Large groups can have disagreements and disorder. Rules maintain order and harmony so that society can function. (2)", "M"),
W("Explain how money transfers have changed in India in the last 30 years.", 2, "Earlier people stood in queues at the Post Office for a money order or at a bank for a demand draft sent by post. Now digital means send money instantly. (2)", "M"),
W("Explain how the three organs worked in the case of cybercrime in the chapter.", 3, "The legislature passed new laws against cybercrime (1). The executive, in the form of the cyber police, caught the criminals (1). The judiciary (courts) convicted them and decided on fines and jail (1).", "M"),
W("What is meant by 'separation of powers'? Why is it useful?", 3, "Keeping the three organs separate, though they work together (1). Each organ can check the others and restore balance if one acts beyond its role (1). This gives checks and balances (1).", "M"),
W("Match: (a) Defence (b) Irrigation (c) Currency with (1) Central government (2) State government.", 3, "(a) Central, (b) State, (c) Central. (1 each)", "M"),
W("Ramesh's village faces a small flood after heavy rain. Who will first deal with it? If it affects many towns and villages? If it is massive?", 3, "The local authorities (1); then the State government sends rescue teams (1); in a massive flood the Central government may send relief supplies and the army (1).", "M", wp=True),
W("Your bulb does not light. The chapter gives three levels of dealing with this. List them and match to local, State and national levels.", 3, "(1) Check the bulb, switch and fuse (local); (2) call an electrician (State); (3) complain to the Electricity Board (national). The chapter calls them three levels of dealing with a problem. (1 each)", "M", wp=True),
W("Why is a class monitor an example of a representative?", 2, "The whole class cannot go to the principal, so the monitor, elected by the class, speaks on behalf of everyone. (2)", "M", wp=True),
W("Explain the meaning of 'representative democracy' and why India is called one.", 3, "People elect representatives who take decisions for them (1). In India, citizens vote for MLAs in States and MPs at the national level (1), who discuss laws in the assemblies, so India is a representative democracy (1).", "M"),
W("Differentiate between direct democracy and representative democracy with one example each.", 3, "In direct democracy everyone takes part in the decision, for example the class votes by raising hands to choose a picnic place (1.5). In representative democracy people elect others to decide for them, for example MPs and MLAs (1.5).", "M"),
W("Find the mistake: \"The Governor is the real head of the State government and the Chief Minister is only the nominal head.\"", 2, "It is the other way round. The Governor is the nominal head, while the Chief Minister is the real executive head of the State. (2)", "M"),
W("What is meant by 'nominal head'? Give one example.", 2, "A head in name only, who normally does not interfere in the work of the government. Example: the President of India. (2)", "M"),
W("In 2024 India had about how many voters? What title does this give India?", 2, "About 970 million voters (1). India is the world's largest democracy (1).", "M"),
W("Give three activities of daily life in which the government plays a role.", 3, "Any three: schools and education, hospitals and public health, roads, post, water supply, electricity, police and safety. (1 each)", "M", wp=True),
W("What is a Member of Legislative Assembly (MLA)? What is the level at which they work?", 2, "An MLA is an elected representative who sits in the State assembly (1) and discusses State laws and problems (1).", "M"),
W("State one function of the Central government and two of the State governments from the chapter.", 3, "Central: any one of defence, foreign affairs, atomic energy, communications, currency (1). State: any two of police and law and order, public health, agriculture, irrigation (1+1).", "M"),
W("What do we learn from the Mahābhārata line 'The ruler protects dharma and dharma protects those who protect it'?", 2, "A ruler should protect justice and duty (dharma), and in turn dharma protects those who follow it. Good governance rests on fairness and duty. (2)", "M"),
# ---------------- HARD ----------------
W("Case study: Seema's school has no ramp for a student who uses a wheelchair. The class representative meets the principal. Which ideas of the chapter does this show? Explain two.", 4, "Rules and facilities of a community can be raised for change by citizens (1). A class representative speaks for the class, as MLAs and MPs speak for people (1). It also shows participation of ordinary people, which is grassroots democracy (1). Dialogue and convincing others, rather than force, is the democratic way (1).", "H", wp=True),
W("Case study: A group of criminals cheats people through fake online payment links. List the roles of the legislature, executive and judiciary in dealing with this.", 4, "Legislature: makes or updates laws against cybercrime (1). Executive: the cyber police investigate and arrest those involved (1). Judiciary: courts decide guilt and the punishment such as fine and jail (1). Together they protect people because the three organs work together while remaining separate (1).", "H", wp=True),
W("What might happen if all three organs of government were under the control of one group of people? Explain with reasons.", 3, "That group could make unfair laws (1), enforce them as it liked (1), and punish opponents without any court to check, leading to disorder and misuse of power. Separation of powers gives checks and balances (1).", "H"),
W("Why does India need three levels of government? Explain with the flood example.", 4, "Different problems are of different size and need different resources (1). A small flood can be handled by local authorities (1). A bigger flood over many towns needs the State's rescue teams (1). A massive flood needs the Centre, with army and relief (1).", "H", wp=True),
W("The chapter says the President and Governor are only 'nominal' heads. How did Dr A.P.J. Abdul Kalam show that a nominal post can still be important?", 3, "He stayed deeply connected with people, especially the youth (1), inspired them with his passion for good education and innovation (1), and impacted countless lives through humility and dedication, though his position was nominal (1).", "H"),
W("Read: 'F.A.I.L. means First Attempt In Learning; E.N.D. means Effort Never Dies.' (Dr Kalam). Explain what he wants students to learn and relate it to your own life.", 3, "He wants us to see failure as a step in learning and not as the end (1), so we keep trying with effort (1). Example: if I fail a test, I should find my mistakes and try again (1). (Any sensible personal example.)", "H"),
W("Do you agree that 'every person in a country cannot rule directly'? Give two reasons and say what is done instead.", 3, "Yes. In a huge country with about 970 million voters, everyone cannot sit together and decide (1.5). It would take too long and be impractical, so people elect representatives who discuss and decide in assemblies (1.5).", "H"),
W("Why is the example of the class picnic a case of direct democracy and not representative democracy?", 3, "Every student's opinion was taken by a show of hands (1). The decision was made by whichever option got more votes (1). No representative decided on their behalf, so it is direct democracy (1).", "H", wp=True),
W("What is grassroots democracy? Why is it described with the base of a pyramid?", 3, "It is a system that enables and encourages participation of ordinary citizens in decisions affecting them (1). In the pyramid of three levels (local, State, Centre), the local level at the base is closest to the people (1), so ordinary citizens can take part most directly there (1).", "H"),
W("Observe the national table of the chapter. Which functions affect a student's daily life the most (choose three) and which level handles each?", 3, "Sample: Education (Centre and State) (1), Public health (State) (1), Police and law and order (State) (1). (Any three with correct levels.)", "H", wp=True),
W("Arrange in logical order: (i) the court fines and jails the criminals (ii) Parliament passes a law against online cheating (iii) the cyber police arrest the cheats. Name the organ of each step.", 3, "(ii) Legislature, (iii) executive, (i) judiciary. Order: law, arrest, court decision. (1 each)", "H"),
W("The Supreme Court's motto, Yato Dharmastato Jayah, and the Government of India's motto, Satyameva Jayate, are taken from ancient texts. Explain what values they teach and why they suit these institutions.", 3, "Satyameva Jayate, 'truth alone triumphs', teaches honesty (1). Yato Dharmastato Jayah, 'where there is dharma there is victory', teaches justice and duty (1). Courts and governments must work with truth and fairness, so the mottos suit them (1).", "H"),
W("Make a table of the two levels of the Indian executive: head of state and real head, for the Centre and the State.", 3, "Centre: nominal head is the President (also Supreme Commander of the armed forces), real executive head is the Prime Minister. State: nominal head is the Governor, real executive head is the Chief Minister. (3)", "H"),
W("During the COVID-19 lockdown many actions were taken. Suggest which tier (local, State or Central) could have taken three different actions and why.", 3, "Sample: Central: nationwide lockdown and foreign flights rules (1); State: hospitals and public health arrangements, police enforcing rules (1); local: cleaning, supplying food and help to families in the neighbourhood (1). (Accept sensible allocations.)", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "10.6 Time Pointers in the Chapter"),
 ("table", ["When", "What"], [
  ["About 30 years ago", "People used the Post Office money order or bank demand draft to send money"],
  ["Today", "Digital payments are instant; cybercrime has led to new laws"],
  ["1931", "Dr A.P.J. Abdul Kalam born in Rameswaram, Tamil Nadu"],
  ["2002–2007", "Dr Kalam served as the 11th President of India"],
  ["2024", "About 970 million voters in India, the world's largest democracy"]]),
 ("h2", "10.7 Key Terms and People"),
 ("table", ["Term", "Meaning"], [
  ["**Governance**", "Taking decisions, organising society with rules, and making sure they are followed"],
  ["**Government**", "The people or system that make the rules and ensure they are followed"],
  ["**Law**", "A more important rule"],
  ["**Legislature**", "Makes laws; assembly of the people's representatives"],
  ["**Executive**", "Implements the laws; head of state, ministers and law-and-order agencies"],
  ["**Judiciary**", "System of courts"],
  ["**Separation of powers**", "Keeping the three organs separate but cooperating; gives checks and balances"],
  ["**Nominal**", "In name only"],
  ["**House**", "An assembly where laws are discussed or passed"],
  ["**MLA / MP**", "Member of Legislative Assembly (State) / Member of Parliament (national)"],
  ["**Representative democracy**", "People elect representatives to decide for them"],
  ["**Direct democracy**", "Everyone takes part directly, as in a class vote"],
  ["**Grassroots democracy**", "Participation of ordinary citizens at the base"],
  ["**Dr A.P.J. Abdul Kalam**", "Missile Man of India; 11th President"]]),
 ("h2", "10.8 Who Does What: Levels and Organs"),
 ("table", ["", "Legislature", "Executive", "Judiciary"], [
  ["National", "Parliament: Lok Sabha and Rajya Sabha", "President (nominal), Prime Minister (real head)", "Supreme Court of India"],
  ["State", "State Assembly (Vidhan Sabha); most States have one house, a few have two", "Governor (nominal), Chief Minister (real head)", "High Court"],
  ["Local", "Studied in Chapters 11 and 12", "Studied in Chapters 11 and 12", "-"]]),
 ("h2", "10.9 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Many people live together", "Disagreements possible, so rules and governance are needed"],
  ["Digital payments spread", "Cybercrime appears; new laws made; cyber police and courts act"],
  ["One group controlling all organs", "Danger of misuse of power; hence separation of powers"],
  ["Problems of different size", "Three levels: local, State and Central"],
  ["All people cannot rule directly", "People elect representatives (MLAs and MPs)"]]),
 ("h2", "10.10 Source Study: Reading the Quotations"),
 ("table", ["Quotation", "Meaning in simple words"], [
  ["'The ruler protects dharma and dharma protects those who protect it.' (Mahābhārata)", "A just ruler upholds duty and justice, and justice protects such rulers"],
  ["'There is no peace without justice; no justice without equality; ... no democracy without respect to the identity and dignity of cultures and peoples.' (Rigoberta Menchú Tum)", "Peace, justice, equality, development and democracy depend on each other and on respect for every culture"],
  ["Satyameva Jayate", "Truth alone triumphs (Government of India)"],
  ["Yato Dharmastato Jayah", "Where there is dharma there is victory (Supreme Court)"]]),
 ("note", "IMPORTANT", "Remember the pairs: **President - Prime Minister** (Centre), **Governor - Chief Minister** (State). First is nominal, second is the real executive head."),
 ("h2", "10.11 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Explain the three organs of government with an example. (5 marks)", "The legislature makes laws, the executive implements them and the judiciary decides whether the law is broken and punishes. In the cybercrime example, the legislature passed laws against online theft, the cyber police (executive) arrested the criminals and the courts (judiciary) fined and jailed them. They are kept separate but work together."),
  ("Why do we need a government? (3 marks)", "People living together need rules to keep order and harmony. The government makes the rules and laws, ensures they are followed and provides public services like education, health and defence."),
  ("What is democracy? Explain why India is called a representative democracy. (5 marks)", "Democracy means the rule of the people (dēmos + kratos). In a huge country everyone cannot rule directly, so citizens aged 18 and above elect representatives: MLAs in the State assemblies and MPs in Parliament. They discuss laws and problems and take decisions. About 970 million voters in 2024 make India the world's largest democracy."),
 ]),
]
CH["takeaways"] += ["**President - PM** and **Governor - CM**: nominal head and real executive head.",
  "Direct democracy: all decide (class vote). Representative democracy: elected persons decide (MLAs, MPs)."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
