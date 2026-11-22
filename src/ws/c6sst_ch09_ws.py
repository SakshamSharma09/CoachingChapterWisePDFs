"""Class 6 Social Science Ch 9 - Family and Community: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch09"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c09", str(REPO / "src/rn_work/c6_sst/c09.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The most ancient and fundamental unit of any society is the:", 1, "(b) family", "E", opts=["school", "family", "market", "town"]),
W("A family with several generations living together is called a:", 1, "(a) joint family", "E", opts=["joint family", "nuclear family", "tribal family", "single family"]),
W("A nuclear family is limited to:", 1, "(c) a couple and their children", "E", opts=["grandparents only", "all cousins and uncles", "a couple and their children", "neighbours"]),
W("In most Indian languages, a cousin is called:", 1, "(d) a brother or a sister", "E", opts=["a neighbour", "a friend", "an uncle", "a brother or a sister"]),
W("The Bhil tradition of coming together to support anyone in crisis is called:", 1, "(a) halma", "E", opts=["halma", "panchayat", "mela", "jajmani"]),
W("The Bhil community worked to solve the water crisis near which town of Madhya Pradesh?", 1, "(b) Jhabua", "E", opts=["Bhopal", "Jhabua", "Indore", "Ujjain"]),
W("Residents' Welfare Associations are an example of:", 1, "(c) a modern urban community", "E", opts=["a joint family", "a tribal council", "a modern urban community", "a government office"]),
W("Which festival was Shalini's family preparing for?", 1, "(d) Onam", "E", opts=["Diwali", "Holi", "Pongal", "Onam"]),
W("Fill in the blank: 'Cooperation' means ______ together.", 1, "working. (1)", "E"),
W("Write True or False: Every member of a family has a role and responsibility.", 1, "True. Relationships are based on love, care, cooperation and interdependence. (1)", "E"),
W("Write True or False: Communities do not need any rules.", 1, "False. Communities agree on rules, often unwritten, for example on the use of water, grazing land and forest produce. (1)", "E"),
W("Name any two values that children learn in the family, according to the chapter.", 2, "Any two: ahimsa, dāna (giving), sevā (service), tyāga (sacrifice). (1+1)", "E"),
W("Who said 'Love and dharma are the flower and fruit of family life'?", 1, "Tiruvalluvar. (1)", "E"),
W("Write two Hindi words for relatives that do not have a single English word.", 2, "Any two: bua, tau, tai, chacha, mausi, nana, nani. (1+1)", "E"),
W("Name two communities that you can be part of in school.", 2, "Any two: your class, sports community, NSS, NCC, science club, drama club. (1+1)", "E"),
W("What did Kamal Parmar of Ahmedabad give to the poor children besides tuition?", 1, "A free dinner. (1)", "E"),
W("In which year did the Chennai floods, mentioned in the chapter, take place?", 1, "2015. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Give two differences between a joint family and a nuclear family.", 2, "A joint family has several generations and relatives such as grandparents, uncles, aunts and cousins living together; a nuclear family has only a couple and their children (or one parent with children). (2)", "M"),
W("Why do Indian languages have so many words for relatives while English has few?", 2, "In Indian families the relationships are close and each relative has a different role, so languages have separate terms such as chacha, tau, mausi and nana. English uses a few general words like uncle and aunt. (2)", "M"),
W("Shalini had expected a silk dress but got a cotton one. Why did she not mind?", 3, "Her uncle had lost his job and could not buy festival clothes (1). Her parents bought clothes for everyone, so she got a simpler dress (1). Her grandmother explained that families support and share with each other, so she was happy that everyone had new clothes (1).", "M", wp=True),
W("In Tenzing's family his father also does housework. What does this tell us about family roles?", 2, "Family work is shared. After the mother became busy in a handicraft cooperative, the father joined in cleaning, gardening and cooking help. So roles are flexible and not fixed. (2)", "M", wp=True),
W("Why do Tenzing's parents discuss special expenses together?", 2, "In a family all members who earn or manage the home share responsibility, so important decisions are made by discussion and cooperation. Saving for unexpected needs is also planned together. (2)", "M", wp=True),
W("Explain what the Bhil community did to face the water crisis near Jhabua.", 3, "Following the halma tradition, they came together (1), planted thousands of trees in hundreds of villages (1), and dug trenches and built water-harvesting structures to conserve rainwater, without payment (1).", "M"),
W("Who was honoured with the Padma Shri in 2019 for work with the Bhil communities? Which movement was he part of?", 2, "Shri Mahesh Sharma, of the Shivganga movement. (2)", "M"),
W("How did people help each other during the Chennai floods of 2015?", 2, "Roads turned into rivers and shops closed. Many private groups, especially spiritual and religious organisations, cooked large quantities of food and distributed it to people who needed it. (2)", "M"),
W("What did Kamal Parmar start in Ahmedabad and how many children came to attend?", 2, "He gave tuition from 5:30 to 9:30 pm every day, with a free dinner, to underprivileged children after his work hours. About 150 children attended. (2)", "M"),
W("A teacher said of Kamal Parmar's classes: 'These children don't get proper benches ... yet they pay all their attention.' What does this show about the children?", 2, "The children were eager to learn and did not mind the lack of facilities such as benches and quiet rooms. (2)", "M"),
W("What are Residents' Welfare Associations? Name two matters on which they make rules.", 3, "They are groups of residents in urban areas who form a community and make their own rules (1). Any two: waste management, cleanliness of common areas, care of pets (1+1).", "M"),
W("Show with one example how communities are interdependent.", 2, "A Residents' Welfare Association depends on the trading community for supplies and on municipal workers for waste. (2)", "M"),
W("Match the example with the type of community: (a) Mumbai's Parsi community (b) the village's farming community (c) our school's art community with (1) common work (2) common interest (3) common religion.", 3, "(a) with (3), (b) with (1), (c) with (2). (1 each)", "M"),
W("Why do communities keep rules about water, grazing lands and forest produce?", 2, "The rules give every family secure access to shared natural resources, and protect them for everyone's use. (2)", "M"),
W("Find the mistake: \"A community is only a group of people who live in the same village.\"", 2, "The chapter says community is a flexible idea. It can also be a group of a religion, jāti, work, interest, school club and so on, not only a village. (2)", "M"),
W("Meena helps her mother cook, her brother helps her with homework, and her grandfather takes her to the bus stop. Which words of the chapter describe this and why does it matter?", 3, "This shows cooperation, interdependence and shared roles (1). Each member helps others, as children grow up and take on more responsibilities (1). Through daily practice children learn to take part in the life of the household (1).", "M", wp=True),
W("Why is the family called a 'school' in the chapter?", 2, "Children learn values such as ahimsa, giving, service and sacrifice in the family and learn the traditions followed for generations. (2)", "M"),
W("Give an example from your village or town (or an imagined one) of neighbours helping each other, like the neighbours in Tenzing's story.", 3, "Sample: after a storm damaged a neighbour's house, Tenzing's grandfather collected money from the whole neighbourhood for repairs (1). In a village, people help in sowing, harvesting or at a wedding (1). Any sensible example showing community support (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Draw in words the family tree of Shalini's family of seven: write each member and say how they are related to Shalini.", 4, "Father and mother (parents), a younger brother (sibling), Acchamma (father's mother, grandmother), Chittappa (father's brother, paternal uncle), Chitti (uncle's wife, aunt) and Chinni (their daughter, Shalini's cousin) (1 mark each for correct relation groups: parents, brother, grandmother, uncle-aunt-cousin). Total with Shalini: seven members.", "H"),
W("Case study: Raju's father has lost his job. His mother wants to cancel the school trip. His uncle who lives with them says he will pay for it from savings. Which ideas from the chapter does this show? What would you do if you were Raju?", 4, "It shows family support, sharing and interdependence (1), like Shalini's family giving to the uncle in need (1). The uncle's act is a case of tyāga and sevā, giving up personal needs for family (1). Opinion: any reasoned answer, for example, I would thank the uncle and use the money carefully (1).", "H", wp=True),
W("Read: 'Through daily practice, children learn to participate in the life of the household.' Explain with two examples what responsibilities children can take up as they grow.", 3, "Children can help in cleaning, setting the table, looking after younger brothers and sisters, helping grandparents or running small errands (any two, 1 each). In this way they learn duty and cooperation (1).", "H", wp=True),
W("Why might a young couple choose to live in a nuclear family? Give two reasons and one disadvantage.", 3, "Reasons: jobs in another city or town, smaller houses or flats, wanting more independence (any two, 1 each). Disadvantage: fewer helping hands, such as grandparents, to care for children or the sick (1). (Any sensible points are accepted.)", "H", wp=True),
W("Give two advantages and two disadvantages of joint families.", 4, "Advantages (any two): more help in work and care, shared expenses, children learn values from elders, support in crisis (1 each). Disadvantages (any two): less space or privacy, many opinions, difficult to take decisions, expenses and chores need good sharing (1 each).", "H"),
W("The chapter says communities have 'rules' that are rarely written down. Why do people follow unwritten rules? What happens if some people break them?", 3, "People follow them because they have grown from long practice and because everyone gains secure use of shared resources (1). If some break them, the shared water, grazing land or forest may be misused (1) and the community will not function smoothly (1).", "H"),
W("Compare the work of Bhil villagers in Jhabua and of Kamal Parmar in Ahmedabad. Write one similarity and one difference.", 3, "Similarity: both worked for the benefit of the community without expecting payment or return (1.5). Difference: Bhils worked as a whole group in a rural area to conserve water and trees, whereas Kamal Parmar started alone in a city to teach children, and others then joined (1.5).", "H"),
W("What values are reflected in Kamal Parmar's initiative? Do you think society was fair to the children he taught? What should society do so that all children get education?", 4, "Values: compassion, service, generosity and commitment to education (1). The children had dropped out of school or never gone, so they did not get the chance that others get (1), which was unfair to them (1). Society should provide schools, teachers, free education and encourage volunteers (1).", "H"),
W("Chintu says, 'I do not depend on anyone, because my family does everything for me.' Use the idea of interdependence to answer him with three examples of people outside his family who help him.", 3, "Everyone depends on many people and communities (1). Examples: the teacher who teaches him, the shopkeeper who sells food and stationery, the bus driver, the doctor, the safai worker, the farmer who grows food (any two, 1 each).", "H", wp=True),
W("Why did the Bhils not accept payment for planting trees and digging trenches? Link your answer to the halma tradition.", 3, "In halma, the community comes together to support anyone in crisis (1). They treated the work as their duty towards the community and the environment (1), and their objective was to serve Mother Earth, so no payment was needed (1).", "H"),
W("Explain with reasons why 'community' is a 'flexible concept'. Give four examples.", 4, "It has several meanings depending on the context (1). Examples (1 each, any three): a jāti, a religion's group such as Chennai's Sikh community, a regional group, people with common work such as the village's farming community, people with common interest such as the school's art community, the science community.", "H"),
W("A new colony's residents decide to form a Residents' Welfare Association. Suggest three rules they could make and say why each matters.", 3, "(1 each) Rules such as: not littering and separating waste so the colony is clean; keeping common areas such as parks tidy for everyone; controlling noise and pets so that neighbours are not disturbed. Any three sensible rules with reasons.", "H", wp=True),
W("Tenzing's grandfather registers a complaint during a power failure and helps collect money for a neighbour's repairs. What kind of citizen is he and why is such a person valuable to a community?", 3, "He is a helpful, active and responsible citizen who thinks about others (1). By reporting problems and helping neighbours, he makes the community work smoothly (1). A community with such members is stronger and safer in times of difficulty (1).", "H", wp=True),
W("Choose the better statement and justify: (A) A family should always give up its own needs when relatives ask. (B) Families support each other and share what they have, as in Shalini's story. Which is closer to the chapter?", 3, "(B) is closer to the chapter (1). In Shalini's story the whole family shared according to need: the uncle had lost his job and got new clothes, while Shalini accepted a simple dress (1). The chapter speaks about giving up some wants for care of the family, not about giving up everything on every demand (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "9.4 Time Pointers in the Chapter"),
 ("table", ["When", "Event"], [
  ["Very old (ancient)", "Family is described as the most ancient unit of society; Tiruvalluvar's saying on love and dharma"],
  ["More than 20 years ago", "Kamal Parmar began free evening classes for poor children in Ahmedabad; 150 children soon attended"],
  ["Last 30–40 years", "New communities such as Residents' Welfare Associations appeared in urban areas"],
  ["2015", "Chennai floods: groups cooked and distributed food"],
  ["2019", "Mahesh Sharma of the Shivganga movement honoured with the Padma Shri for his work with the Bhil communities"]]),
 ("h2", "9.5 Key Terms and People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Family**", "The basic and most ancient unit of society; members live together and care for one another"],
  ["**Joint family**", "Several generations (grandparents, parents, uncles, aunts, cousins) living together"],
  ["**Nuclear family**", "A couple and their children, sometimes one parent with children"],
  ["**Cooperation**", "Working together"],
  ["**Interdependence**", "Depending on each other"],
  ["**Dharma**", "Doing one's duty"],
  ["**Ahimsa, dāna, sevā, tyāga**", "Non-violence, giving, service, sacrifice: values learnt in the family"],
  ["**Halma**", "Bhil tradition of coming together to help anyone in crisis; the aim is to serve Mother Earth"],
  ["**Community**", "A group of connected people who come together for common reasons (a flexible idea)"],
  ["**Jāti**", "A group by birth-based occupation or caste; its subdivision is often called a community"],
  ["**RWA**", "Residents' Welfare Association, an urban community that makes its own rules"],
  ["**Kamal Parmar**", "Ahmedabad workshop owner who taught poor children in the evenings"],
  ["**Mahesh Sharma**", "Shivganga movement; Padma Shri 2019"]]),
 ("h2", "9.6 Map Pointers"),
 ("ul", ["**Kerala** — Shalini's family (joint family, Onam).",
  "**Meghalaya** (north-east India) — Tenzing's village; handicraft cooperative, grocery store.",
  "**Jhabua, Madhya Pradesh** — Bhil halma; trees and water-harvesting structures.",
  "**Chennai, Tamil Nadu** — floods of 2015 and community food distribution.",
  "**Ahmedabad, Gujarat** — Kamal Parmar's free classes."]),
 ("h2", "9.7 Joint and Nuclear Families Compared"),
 ("table", ["Point", "Joint family", "Nuclear family"], [
  ["Members", "Grandparents, parents, uncles, aunts, cousins", "Couple and children"],
  ["Examples in chapter", "Shalini's family in Kerala; Tenzing's family (grandparents live with them)", "Couple with their children"],
  ["Strength", "More helping hands, shared care and support (ideas for discussion)", "Independence, smaller needs (ideas for discussion)"],
  ["Difficulty", "More members to adjust with", "Fewer people to help in crisis"]]),
 ("note", "REMEMBER", "The chapter asks you to **discuss** advantages and disadvantages of both kinds of family. Neither is 'better': give balanced points and use examples."),
 ("h2", "9.8 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Shalini's uncle lost his job", "Parents bought clothes for all, Shalini accepted a cotton dress"],
  ["Tenzing's mother got busy in a handicraft cooperative", "Father joined in housework and cooking"],
  ["Severe water crisis in Jhabua", "Bhils planted trees and built water-harvesting structures under halma"],
  ["Floods in Chennai in 2015", "Many groups cooked and distributed food"],
  ["Poor children out of school in Ahmedabad", "Kamal Parmar started evening tuition; 150 joined; volunteers helped"]]),
 ("h2", "9.9 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Explain how a family is a 'school' for values. (3 marks)", "In the family children learn ahimsa, dāna, sevā and tyāga. Members often give up their own needs for others, like Shalini accepting a simpler dress. Children also take up more duties as they grow and learn the traditions of the family. So the family teaches dharma through daily practice."),
  ("What is a community? Describe three kinds of community. (5 marks)", "A community is a group of connected people who come together for reasons such as festivals, weddings, farming help or shared interest. Kinds: (1) village or tribal communities that share water, grazing land and forest produce; (2) urban Residents' Welfare Associations that make rules for waste and common areas; (3) communities based on religion, region, work or interest such as Parsi community in Mumbai or the farming community. In school there are class, sports, NSS, NCC and science or drama clubs."),
  ("Describe the halma tradition with an example. (5 marks)", "Halma is a Bhil tradition of coming together to support any individual or family in crisis; its aim is to serve Mother Earth. Near Jhabua, Madhya Pradesh, acute water shortage was solved when Bhils planted thousands of trees in hundreds of villages and dug trenches and built water-harvesting structures. They were not paid and did it as their duty to the community and environment. Mahesh Sharma of the Shivganga movement got the Padma Shri in 2019."),
 ]),
]
CH["takeaways"] += ["**Family** is the foundation; **community** is the bigger circle; both rest on **cooperation and interdependence**.",
  "Examples to remember: Shalini (Kerala), Tenzing (Meghalaya), Bhil halma (Jhabua), Chennai floods 2015, Kamal Parmar (Ahmedabad)."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
