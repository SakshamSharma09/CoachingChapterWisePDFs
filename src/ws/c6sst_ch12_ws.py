"""Class 6 Social Science Ch 12 - Grassroots Democracy Part 3: Local Government in Urban Areas: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch12"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c12", str(REPO / "src/rn_work/c6_sst/c12.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Local government structures in towns and cities are called:", 1, "(c) urban local bodies", "E", opts=["Panchayati Raj institutions", "Gram Sabhas", "urban local bodies", "High Courts"]),
W("Cities and towns are divided into smaller units called:", 1, "(a) wards", "E", opts=["wards", "blocks", "districts", "tehsils"]),
W("The highest urban local body of a city with a population above 10 lakh is the:", 1, "(b) Municipal Corporation", "E", opts=["Nagar Panchayat", "Municipal Corporation", "Gram Panchayat", "Zila Parishad"]),
W("A Municipal Council is also called:", 1, "(d) Nagar Palika", "E", opts=["Mahanagar Nigam", "Panchayat Samiti", "Gram Sabha", "Nagar Palika"]),
W("A Municipal Corporation is also called:", 1, "(a) Mahanagar Nigam", "E", opts=["Mahanagar Nigam", "Nagar Palika", "Nagar Panchayat", "Ward Committee"]),
W("Which city has been the cleanest city in India under Swachh Survekshan for seven years in a row?", 1, "(c) Indore", "E", opts=["Chennai", "Mumbai", "Indore", "Kolkata"]),
W("The oldest municipal institution in India is the:", 1, "(b) Madras Corporation (now Greater Chennai Corporation)", "E", opts=["Bombay Municipal Corporation", "Madras Corporation (now Greater Chennai Corporation)", "Indore Municipal Corporation", "Delhi Municipal Corporation"]),
W("The Bombay Municipal Corporation was created in which year?", 1, "(a) 1865", "E", opts=["1865", "1688", "1792", "1949"]),
W("Fill in the blank: Ward committees report problems like a water leak or a blocked drain to the ______.", 1, "authorities (the local body). (1)", "E"),
W("Write True or False: Urban local bodies have elected members.", 1, "True. They are elected to represent the local citizens. (1)", "E"),
W("Write True or False: A city with a population of 50,000 can have a Municipal Corporation.", 1, "False. Only cities with a population above 10 lakh have a Municipal Corporation as their highest body; smaller towns have a Municipal Council or Nagar Panchayat. (1)", "E"),
W("What does 'decentralised' mean in the chapter?", 2, "Instead of everything being decided by a central authority at the top, local communities have a direct say in how their area is managed. (2)", "E"),
W("Name two functions of urban local bodies.", 2, "Any two: looking after infrastructure, garbage collection and disposal, maintaining the burial ground, checking implementation of government schemes, collecting local taxes and fines, planning development. (1+1)", "E"),
W("Name any two services of the Indore Municipal Corporation.", 2, "Any two: property tax, water charges, solid waste management, trade licences, marriage certificates, fire services, water tanker, ambulance, funeral van, mobile toilet. (1+1)", "E"),
W("Which body governs towns with a smaller population than a Municipal Council?", 2, "Smaller cities and towns with a smaller population are governed by a Nagar Panchayat. (2)", "E"),
W("Who was Rustom K. Sidhwa and when did he make his statement on local bodies?", 2, "A member of the Constituent Assembly; on 13 October 1949, during the Constituent Assembly Debates. (2)", "E"),
W("What does CRM stand for in Fig. 12.4?", 1, "Citizen Relationship Management. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Make a table with the population size of a city and its highest urban local body, for three sizes.", 3, "Above 10 lakh: Municipal Corporation (Mahanagar Nigam) (1); 1 to 10 lakh: Municipal Council (Nagar Palika) (1); smaller population: Nagar Panchayat (1).", "M"),
W("Aarav's town has a population of 4 lakh. Which type of urban local body is its highest body? Which type will a city of 25 lakh have?", 2, "Municipal Council (Nagar Palika) for 4 lakh (1); Municipal Corporation (Mahanagar Nigam) for 25 lakh (1).", "M", wp=True),
W("What do ward committees do? Give three examples.", 3, "They help in activities such as conducting health camps (1) and organising campaigns against single-use plastics (1), and they watch for problems like water leaks, blocked drains and damaged roads and report them to the authorities (1).", "M"),
W("Why must citizens also perform duties for urban local bodies to work well? Give two examples.", 3, "The system is a participatory democracy, so people must show care and concern for their area (1). Examples: following waste segregation instructions makes garbage collection easier (1); promptly reporting a water leak prevents wastage of water (1).", "M", wp=True),
W("On the way to school you and your friends see a leaking water pipe. What will you do?", 3, "Note the place and tell an adult (1), report to the ward committee or the local body (complaint or helpline) (1), and tell others not to waste water meanwhile. Reporting promptly prevents more wastage (1).", "M", wp=True),
W("Why is urban governance more complex than village governance?", 2, "Cities like Kolkata, Chennai and Mumbai are larger, more crowded and more diverse in communities and activities, so more types of work and more systems are needed. (2)", "M"),
W("How did the Madras Corporation begin? Write three facts.", 3, "It was established on 29 September 1688, and is the oldest municipal institution in India (1). The East India Company had issued a charter the year before, making the town of Fort St. George and territory within 16 km a corporation (1). A Parliamentary Act of 1792 gave it power to levy municipal taxes, from which municipal administration properly began (1).", "M"),
W("Arrange in order of time: (i) Parliamentary Act giving power to levy municipal taxes in Madras (ii) Bombay Municipal Corporation created (iii) Madras Corporation established.", 3, "(iii) 1688, (i) 1792, (ii) 1865. (1 each)", "M"),
W("Look at the services of the Indore Municipal Corporation. Which of them might be paid services, and how does it help the body?", 2, "Water tanker, septic tanker, auditorium, funeral van, mobile toilet and ambulance are likely paid services, along with taxes and fees (1). The money collected helps the body fund its activities (1).", "M"),
W("Find the mistake: \"A Nagar Panchayat is the highest body for a city of 20 lakh people.\"", 2, "A city of 20 lakh (above 10 lakh) has a Municipal Corporation as the highest body. A Nagar Panchayat is for smaller towns. (2)", "M"),
W("What role could Indore's citizens have played in making it the cleanest city in India for seven years?", 3, "They followed waste segregation instructions (1), kept public places clean and did not litter (1), and worked with the Municipal Corporation by reporting problems and using its services (1). Any sensible role.", "M", wp=True),
W("In the conversation, how did the village children get an electric wire problem solved?", 2, "They noticed a low-hanging wire almost touching a roof, reported it, and explained to a Gram Sabha member that the electric post should be shifted. It was done. (2)", "M"),
W("What happened in the city two streets away after heavy rain, as told by Anita? What does it show?", 3, "A house collapsed (1). Dozens of people gathered to clear the rubble and make sure no one was trapped (1). It shows that a sense of community exists in a city too, along with local government help (1).", "M"),
W("State two differences between the village and the city as told by Sameer and Anita.", 2, "In the city: busy, crowded, noisy, tall buildings, people are more independent and often do not know their neighbours (1). In the village: quiet, everyone knows everyone, they work and make decisions together (1).", "M"),
W("Write one similarity between Panchayati Raj institutions and urban local bodies.", 2, "Both have elected representatives who take care of local needs, and both are at the base of the governance pyramid. (2)", "M"),
W("Match: (a) Ward committee (b) Municipal Corporation (c) Nagar Panchayat with (1) smaller town (2) health camp in a ward (3) city above 10 lakh.", 3, "(a) with (2), (b) with (3), (c) with (1). (1 each)", "M"),
W("What does 'participatory democracy' mean?", 2, "A system where good governance empowers citizens to actively take part in their country's working, at the rural, urban, State or national level. (2)", "M"),
W("Name three types of urban local body services that depend on citizens' help.", 3, "Garbage collection (waste segregation), saving water (reporting leaks), cleanliness of public places (not littering), reporting damaged roads. Any three. (1 each)", "M", wp=True),
# ---------------- HARD ----------------
W("Read: Rustom Sidhwa wished that a full-fledged local body be formed so that people may know 'what is an administration, what are the franchise, what are the powers, what are the rights' in their own town. Explain in your own words why he wanted this.", 3, "He wanted people to learn how government works by taking part in it in a small area, in their own town or village (1). With local bodies, ordinary people understand voting, powers and rights (1). This trains citizens for larger democracy (1).", "H"),
W("Case study: The roads in your colony are damaged, the drains are blocked and garbage is not collected. Explain who in the urban local government you should approach and how.", 4, "First tell the ward committee, which watches for problems like blocked drains and damaged roads (1). They report to the authorities of the urban local body (Municipal Corporation, Council or Nagar Panchayat, according to the city size) (1). Citizens can write a complaint or use the corporation's grievances service (1). They should also cooperate in waste segregation and keep the area clean (1).", "H", wp=True),
W("Compare the Panchayati Raj system with urban local bodies: give three similarities and three differences.", 5, "Similarities (any three): elected members; decentralised; base of the governance pyramid; below the State government; looks after local needs; citizen participation (1.5 for three correct). Differences (any three): Panchayats in villages with Gram Sabha, Gram Panchayat, Panchayat Samiti and Zila Parishad; urban bodies in cities with wards, ward committees and Nagar Panchayat, Municipal Council and Municipal Corporation; type decided by population; urban more complex (3.5 for three correct).", "H"),
W("Why does the chapter say that, 'for these bodies to function efficiently, people must also perform their duties'? Suggest four more actions of responsible citizens.", 4, "Citizens are part of a participatory democracy and must cooperate (1). Four examples (3): do not litter, save water and electricity, use public transport or walk, keep common places clean, plant trees, report problems, pay taxes and bills on time.", "H", wp=True),
W("How can we find out which type of urban local body a city has? Show with three imaginary cities of different population.", 3, "Check the population: above 10 lakh has a Municipal Corporation; 1 to 10 lakh has a Municipal Council; smaller has a Nagar Panchayat (1). Examples with their approximate type, such as a metro city of 30 lakh (Corporation), a district town of 3 lakh (Council), a small town of 40,000 (Nagar Panchayat) (2).", "H", wp=True),
W("Study the services under the Indore Municipal Corporation. Which five services directly affect you or your family? Explain each in one line.", 4, "Sample: water charges and water tankers (supply of water) (1); solid waste management (garbage collection) (1); fire services (safety) (1); marriage certificates and licences (documents and trade) (1). Any four with a reason.", "H", wp=True),
W("Sameer says that in the village a lot more people can participate in discussion. Why is it easier in a village than in a big city? How can big cities still ensure participation?", 3, "In a village everyone knows each other, so more people can join and discuss (1). Cities have many people who are strangers (1), so they use wards, ward committees, elected representatives and services like grievance reporting so that everyone's voice is heard (1).", "H"),
W("The Madras Corporation was formed in the time of the East India Company. Why is it important to learn about it in a chapter about local democracy?", 3, "It shows that city governance began a long time ago, in 1688, and the power to levy taxes in 1792 started proper administration (1). Today's urban local bodies are elected by citizens and serve them (1). So we see how the idea of local government changed to include participation by the people (1). (Any sensible link.)", "H"),
W("Make a list of four characteristics of a good urban local body and give a reason for each.", 4, "(1 each) Honest (uses money properly); responsive (acts quickly on complaints); inclusive (listens to every ward and group); transparent (tells people about its work and services). Other sensible qualities accepted.", "H"),
W("Anita says, 'It seems more complicated in the city, but the idea is the same — everyone's voice matters.' Do you agree? Support your answer with two points from the chapter.", 3, "Yes. In both, members are elected to represent people (1.5). Both are decentralised, with ward committees in cities and the Gram Sabha in villages, so ordinary people can take part (1.5).", "H"),
W("Case study: Radha lives in a town of 60,000 people in Rajasthan. Her colony's park is neglected. Write a short plan, with three steps, for the people of her ward to get it repaired.", 4, "Step 1: gather neighbours and meet the ward committee member (1). Step 2: write a written complaint to the Nagar Panchayat/local body office with signatures (the type of body depends on the town size) (1). Step 3: follow up and offer help, such as a cleaning drive (1). Also take care of the park afterwards (1).", "H", wp=True),
W("What is meant by the 'pyramid' of governance in Fig. 12.2? Where do the people stand and where do rural and urban local governments stand in it?", 3, "The pyramid shows governance from local to national: Union government at the top, State government in the middle and local government below (1). People are at the base, closest to the local government (1). Rural (Panchayati Raj) is on the left side and urban local bodies on the right side of the local level (1).", "H"),
W("Why is Indore a good example of cooperation between citizens and the local government? Use the chapter's information.", 3, "Indore was the cleanest city in India under Swachh Survekshan seven years in a row (1). The Municipal Corporation provides many services including solid waste management (1). Citizens must follow instructions and cooperate, so the success is a team effort (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "12.6 Timeline"),
 ("table", ["Date", "Event"], [
  ["29 September 1688", "Madras Corporation established, the oldest municipal institution in India (charter of the East India Company a year earlier)"],
  ["1792", "Parliamentary Act gave the Madras Corporation power to levy municipal taxes; municipal administration properly began"],
  ["1865", "Municipal Corporation of Greater Mumbai (originally Bombay Municipal Corporation) created"],
  ["13 October 1949", "Rustom K. Sidhwa speaks on local bodies in the Constituent Assembly Debates"],
  ["Seven years in a row (recent)", "Indore named cleanest city under Swachh Survekshan"]]),
 ("h2", "12.7 Key Terms and People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Urban local bodies**", "Local government institutions of towns and cities"],
  ["**Decentralised**", "Power shared with local communities instead of one central authority"],
  ["**Ward**", "A smaller unit into which a city or town is divided"],
  ["**Ward committee**", "Group that organises activities in the ward and reports problems"],
  ["**Municipal Corporation (Mahanagar Nigam)**", "Highest body for cities above 10 lakh"],
  ["**Municipal Council (Nagar Palika)**", "Highest body for cities with 1 to 10 lakh"],
  ["**Nagar Panchayat**", "Body for smaller towns"],
  ["**Participatory democracy**", "Citizens actively take part in governance"],
  ["**CRM**", "Citizen Relationship Management, a service system of Indore Municipal Corporation"],
  ["**Swachh Survekshan**", "Government cleanliness survey scheme"],
  ["**Rustom K. Sidhwa**", "Member of Constituent Assembly who spoke for strong local bodies"]]),
 ("h2", "12.8 Map and Picture Pointers"),
 ("ul", ["On the map of India locate **Chennai (Tamil Nadu)**, **Mumbai (Maharashtra)**, **Kolkata (West Bengal)** and **Indore (Madhya Pradesh)**.",
  "In the governance pyramid (Fig. 12.2) note the left side is rural (Gram Sabha, Gram Panchayat, Panchayat Samiti, Zila Panchayat) and the right side is urban (people of the ward, ward committee, urban local body)."]),
 ("h2", "12.9 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Cities are large, crowded and diverse", "A more complex system of urban local bodies is needed"],
  ["City divided into wards", "Ward committees can watch for local problems and report them"],
  ["Different city sizes", "Different bodies: Corporation, Council, Nagar Panchayat"],
  ["Citizens follow waste segregation rules", "Garbage collection becomes easier; cities like Indore stay clean"],
  ["Municipal bodies get power to levy taxes (1792)", "Municipal administration properly began"]]),
 ("note", "IMPORTANT", "Remember: **above 10 lakh - Municipal Corporation; 1 to 10 lakh - Municipal Council; smaller - Nagar Panchayat.** Ward committees are the base of the urban pyramid, as the Gram Sabha is for villages."),
 ("h2", "12.11 Village and City Compared: Anita and Sameer"),
 ("ul", ["**City:** busy, crowded, noisy, tall buildings; people are more independent and often do not know their neighbours; yet in an emergency such as a collapsed house, dozens of people gather to help.",
  "**Village:** quiet; everyone knows everyone; people work in the fields, celebrate festivals and take decisions together; even children can be heard, for example in getting a low-hanging electric wire fixed through the Gram Sabha.",
  "**Common idea:** elected local bodies, participation and the belief that everyone's voice matters."]),
 ("h2", "12.10 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("What are urban local bodies and what are their functions? (5 marks)", "Urban local bodies are the local government institutions of towns and cities. They are decentralised and have elected members. They look after infrastructure, garbage collection and disposal, burial grounds, implementation of government schemes, collection of local taxes and fines, and planning for economic and social development. Wards and ward committees help with health camps and reporting problems."),
  ("Why are urban local bodies important in governance and democracy? (3 marks)", "They give people of a city a direct say in the management of their area, bring services close to the citizens and give practice in participatory democracy."),
  ("Describe the role of citizens in the working of the urban local bodies. (3 marks)", "Citizens must follow waste segregation instructions, report problems such as leaking pipes promptly and care for the area. Without citizen cooperation, bodies cannot work efficiently."),
 ]),
]
CH["takeaways"] += ["**Types by population:** above 10 lakh Corporation, 1 to 10 lakh Council, smaller Nagar Panchayat.",
  "Dates: **Madras Corporation 1688**, **Act of 1792**, **Bombay Corporation 1865**, **Sidhwa 13 Oct 1949**."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
