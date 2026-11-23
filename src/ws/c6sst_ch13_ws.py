"""Class 6 Social Science Ch 13 - The Value of Work: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch13"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c13", str(REPO / "src/rn_work/c6_sst/c13.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("An activity done in exchange for money or money's worth is called an:", 1, "(a) economic activity", "E", opts=["economic activity", "non-economic activity", "festival", "hobby only"]),
W("Which of these is a non-economic activity?", 1, "(c) A mother helping her children with schoolwork", "E", opts=["A lawyer arguing a case for a fee", "A truck driver carrying goods", "A mother helping her children with schoolwork", "Workers in a car factory"]),
W("A fixed regular payment, generally monthly, paid by an employer to an employee is a:", 1, "(b) salary", "E", opts=["fee", "salary", "wage", "prasād"]),
W("A payment made to a doctor or a lawyer for advice or service is called a:", 1, "(d) fee", "E", opts=["salary", "wage", "payment in kind", "fee"]),
W("The mangoes received by Sahil as a part of his payment are an example of:", 1, "(a) payment in kind", "E", opts=["payment in kind", "salary", "fee", "profit"]),
W("Selfless service is called:", 1, "(b) sevā", "E", opts=["vyapar", "sevā", "mela", "sabha"]),
W("The festival of forests, which promotes tree plantation, is:", 1, "(c) Van Mahotsav", "E", opts=["Swachh Bharat Abhiyan", "Navaratri", "Van Mahotsav", "Onam"]),
W("A place where goods and services are exchanged, generally for money, is a:", 1, "(d) market", "E", opts=["school", "temple", "park", "market"]),
W("Fill in the blank: Value addition means adding ______ at each stage of making a thing.", 1, "value. (1)", "E"),
W("Write True or False: A person can do both economic and non-economic activities.", 1, "True. Rohan earns a salary at his company and also volunteers at weekends. (1)", "E"),
W("Write True or False: Non-economic activities have no value in our lives.", 1, "False. They bring satisfaction, social welfare and better quality of life even if they bring no money. (1)", "E"),
W("What work does Geeta Aunty do in Anu and Kabir's story?", 1, "She is a pilot in the Indian Air Force. (1)", "E"),
W("Name any two economic activities mentioned in the chapter.", 2, "Any two: selling school bags, farmer selling produce, lawyer arguing a case, truck driving, working in a car factory. (1+1)", "E"),
W("Name any two non-economic activities mentioned in the chapter.", 2, "Any two: parents cooking for the family, helping children with schoolwork, youth caring for grandparents, family helping to renovate the house. (1+1)", "E"),
W("What is a langar?", 1, "A community kitchen, for example at gurudwaras, that serves free food to every visitor. (1)", "E"),
W("Which highway-related fact in Kavya's story shows the benefit of a new road?", 1, "It would reduce the travel time to the nearest town from five hours to two. (1)", "E"),
W("What is a wage?", 2, "A payment made by the employer to the worker for a specific period of time, for example a daily wage. (2)", "E"),
W("From which force had Kabir's grandfather retired?", 1, "The Border Security Force. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Differentiate between economic and non-economic activities with one example of each.", 3, "Economic activities involve money or are done for money or money's worth, for example a farmer selling produce (1.5). Non-economic activities do not earn income and are done from love, care, gratitude or respect, for example parents cooking for the family (1.5).", "M"),
W("Make the table: Rohan's two activities and say whether each is economic or non-economic.", 3, "Working in a software company for a salary: economic (1.5). Teaching computer skills free at the youth development programme: non-economic (1.5).", "M"),
W("Kabir's grandfather teaches Geography free to the neighbourhood kids. A school teacher teaches Geography for a salary. How are they different?", 3, "Grandfather: non-economic, no payment, done out of care (1.5). School teacher: economic, because she receives a salary (1.5).", "M", wp=True),
W("Classify the following as economic (E) or non-economic (N): (i) tailor stitching clothes for a customer (ii) a daughter taking care of a sick grandmother (iii) a baker selling bread (iv) children cleaning their street on Swachh Bharat day.", 3, "(i) E (ii) N (iii) E (iv) N. (¾ for each correct item)", "M", wp=True),
W("Name any three forms of payment for work, with one example of each.", 3, "Any three: salary (pilot); wage (farm labourer); fee (doctor or lawyer); payment in kind (mangoes for Sahil). (1 each)", "M"),
W("How was Sahil paid for his work? Why is this unusual compared with a salary?", 3, "He got a daily wage (1), partly in cash and partly in mangoes of equal value (1). Payment in kind is non-cash, whereas a salary is a fixed regular payment, usually monthly (1).", "M"),
W("Kavya's aunt works at the post office and teaches online in the evening. What payments does she receive and what are they called?", 3, "A monthly salary from the post office (1.5) and a weekly fee for the online classes (1.5).", "M", wp=True),
W("Explain value addition with the example of Rajesh the carpenter.", 3, "Rajesh buys wood for ₹600 and makes a chair that he sells for ₹1,000 (1). The extra ₹400 is the value of his skill, time and effort (1). He has added value to the wood by turning it into furniture (1).", "M", wp=True),
W("A baker buys flour and ingredients for ₹300 and bakes bread which she sells for ₹450. How much value has she added? What does this amount stand for?", 2, "₹450 - ₹300 = ₹150 (1). It is the value of her skill, time and effort (and oven and fuel costs, if any) (1).", "M", wp=True),
W("A tailor buys cloth for ₹800 and sells the stitched kurta for ₹1,500. Find the value added and say why we count the activities as economic.", 3, "₹1,500 - ₹800 = ₹700 value added (1). The tailor pays for cloth and is paid for the kurta (1), so both activities involve money and are economic activities (1).", "M", wp=True),
W("What is meant by 'sevā'? Give two examples from places of worship.", 3, "Sevā means selfless service (1). Examples: langar at a gurudwara (free community kitchen) (1) and prasād distributed to devotees in a temple (1).", "M"),
W("What is the Swachh Bharat Abhiyan and how does it show community participation?", 3, "It is a campaign based on collective effort of all citizens to keep surroundings clean (1). People keep their homes clean and also come together to clean streets, roads, parks and public places (1). Together this makes a clean neighbourhood, society and nation (1).", "M"),
W("What is Van Mahotsav and why is it celebrated?", 2, "Van Mahotsav is the festival of forests, with community tree plantation drives, to promote awareness about the value of trees and conservation of forests. (2)", "M"),
W("Find the mistake: \"Non-economic activities are those for which people are paid a salary.\"", 2, "Non-economic activities do not generate income. Activities for which a salary is paid are economic. (2)", "M"),
W("Why are festivals considered non-economic activities though people spend money on them?", 2, "During festivals people gather to decorate, cook and share food as a community, for togetherness and joy and not for earning. They hold value as they bring people together. (2)", "M"),
W("Anu's mother runs a uniform shop with her husband and also voluntarily teaches knitting. Which of her activities is economic and which non-economic?", 2, "Running the shop is economic (1). Teaching knitting to women in the community voluntarily is non-economic (1).", "M", wp=True),
W("List four people who work in your neighbourhood and the way each of them is paid.", 3, "Sample: shopkeeper (profit from sales), school teacher (salary), farm labourer (daily wage), doctor (fee). (1 each for three correct)", "M", wp=True),
W("Give two examples of non-economic activities that are important in your family and say why each is valuable.", 2, "Sample: caring for grandparents (gives them comfort and teaches respect) (1); helping with household chores (builds cooperation and saves effort of others) (1). Any two sensible examples.", "M", wp=True),
# ---------------- HARD ----------------
W("Case study: Ramesh drives a taxi in Jaipur and earns money from fares. In the evening, he drives an old neighbour to the hospital without taking any money. Identify the economic and the non-economic activity and explain what each gives to him and the society.", 4, "Driving the taxi is economic: he earns fares, which support his family and provide transport to others (2). Driving the neighbour free is non-economic: it is done from care and respect and brings satisfaction and trust in the community (2).", "H", wp=True),
W("Case study: Sunita grows vegetables in her field and sells them in the market. She also gives a basket of vegetables to a family whose house was damaged by rain. Show how the same produce can be used in both kinds of activities.", 3, "Sold in the market for money: economic (1.5). Given free as help: non-economic, done out of care (1.5). Thus the same person and the same produce may be used for economic or non-economic purposes depending on the aim.", "H", wp=True),
W("The chapter's table lists 'Farmers repairing their tractor' for you to judge. Explain when this activity would be economic and when non-economic.", 3, "If a mechanic repairs the tractor and is paid a fee, it is an economic activity because money is involved (1½). If the farmers repair their own tractor without paying anyone, no money changes hands, so it can be seen as non-economic, although the working tractor helps them to earn from farming (1½). (The chapter leaves this for discussion; accept a reasoned answer.)", "H", wp=True),
W("Read: 'Do it as worship, as the highest worship, and devote your whole life to it for the time being.' (Swami Vivekananda). What do these words teach about work, whatever kind it is?", 3, "Any work, economic or non-economic, deserves full attention and devotion (1). The attitude of worship means honesty and focus (1). It tells us that all useful work is respectable and has value (1).", "H"),
W("Do you think non-economic activities are as important as economic ones? Give your opinion with three reasons.", 4, "Yes (or reasoned). Without care at home, children and the old would not be looked after (1). Sevā and community efforts such as Swachh Bharat clean our surroundings (1). They produce gratitude and satisfaction that money cannot buy (1). Economic activities provide a living, so both are needed (1). (Any reasoned view accepted.)", "H"),
W("Explain how the economic activities in a village like Kamlapur depend on each other. Use at least four people from Kavya's story.", 4, "Uncle (bulldozer technician) builds the road for travel (1); aunt (post office and online classes) provides postal services and education (1); Sahil (farm labourer) helps the farmer grow mangoes (1); Rajesh the carpenter uses wood to make furniture sold to others (1). Each one's work helps the others, showing interdependence.", "H", wp=True),
W("The chapter says economic activities have value in terms of money. Using the carpenter example, explain how a price of a chair is made up of cost and value addition.", 3, "Price ₹1,000 = cost of wood ₹600 + value added ₹400 (1). The value added is skill, time and effort (1). Hence the selling price is higher than the cost, and the difference is reward for the worker's contribution (1).", "H", wp=True),
W("A farmer sells milk at ₹50 a litre. The same milk is made into paneer by a dairy and sold at a higher price per kilo of milk used. Explain with value addition why paneer costs more.", 3, "The dairy buys milk (cost) and adds work, skill, time and equipment to make paneer (1). The extra effort adds value (1). So the final product costs more than the raw milk (1).", "H", wp=True),
W("The chapter says Geeta Aunty 'serves the country and performs an economic activity too'. Explain how both can be true.", 3, "She is a pilot in the Indian Air Force, so she serves the nation (1). She receives a salary for her work, so it is an economic activity (1). Thus an activity can be a service and also a paid job (1).", "H"),
W("Make a list of ways the following people may be paid: (a) a bus driver (b) a farm labourer (c) a doctor (d) a shopkeeper. Name the payment forms.", 4, "(a) salary (b) wage, possibly with payment in kind (c) fee (d) income from sale or profit. (1 each)", "H", wp=True),
W("Explain why 'there is great value attached to people engaged in community service activities'.", 3, "They give time and effort without expecting anything in return (1). They help people in need and improve the neighbourhood, for example by cleaning or planting trees (1). They create gratitude and togetherness and make society a better place to live (1).", "H"),
W("Describe a community activity of your school or locality, what you observed and which values it showed.", 3, "Sample: a tree plantation drive in school for Van Mahotsav (1). Students, teachers and neighbours worked together (1). It showed care for environment, teamwork and sevā (1). (Any real example accepted.)", "H", wp=True),
W("Which is better for a young person: working only to earn, or working to earn and also doing voluntary work? Give two reasons, using Rohan as an example.", 3, "Doing both is better (1). Rohan earns a salary in a software company and teaches computer skills free (1). The salary supports his life, while volunteering brings satisfaction and helps others (1). (Reasoned alternative views accepted.)", "H", wp=True),
]

CH = _base()
def _fix(x):
    if isinstance(x, str):
        return x.replace("Yes, helps income (production) — repair is part of farming", "Open to discussion: economic if a mechanic is paid; non-economic if farmers repair it themselves without payment")
    if isinstance(x, (list, tuple)):
        return type(x)(_fix(i) for i in x)
    return x
CH["blocks"] = _fix(CH["blocks"])
CH["blocks"] += [
 ("h2", "13.6 Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["**Economic activity**", "Activity involving money or money's worth"],
  ["**Non-economic activity**", "Activity that does not generate income, done from gratitude, love, care and respect"],
  ["**Money's worth**", "The monetary value a person places on an object based on the benefit"],
  ["**Market**", "Place where goods and services are exchanged"],
  ["**Fee**", "Payment for professional advice or service"],
  ["**Salary**", "Fixed regular payment, usually monthly, by an employer"],
  ["**Wage**", "Payment by an employer to a worker for a specific period"],
  ["**Payment in kind**", "Non-cash payment"],
  ["**Value addition**", "Adding value at each stage of making something"],
  ["**Sevā**", "Selfless service"],
  ["**Langar**", "Community kitchen serving free food"],
  ["**Van Mahotsav**", "Festival of forests; tree plantation"],
  ["**Swachh Bharat Abhiyan**", "National cleanliness campaign by collective effort"]]),
 ("h2", "13.7 Characters of the Chapter at a Glance"),
 ("table", ["Character", "Economic activity", "Non-economic activity"], [
  ["Geeta Aunty", "Air Force pilot (salary)", "-"],
  ["Kabir's grandfather", "- (retired from the Border Security Force)", "Free Geography classes, garden, errands"],
  ["Anu's parents", "Run a shop of uniforms and garments", "Mother's voluntary knitting classes"],
  ["Rohan", "Software engineer (salary)", "Teaches computer skills on weekends"],
  ["Kavya's uncle", "Bulldozer technician (salary)", "-"],
  ["Kavya's aunt", "Post office (salary); online classes (weekly fee)", "-"],
  ["Sahil", "Farm labourer (wage + mangoes)", "-"],
  ["Rajesh", "Carpenter: chair sold for ₹1,000 (wood ₹600)", "-"]]),
 ("h2", "13.8 Worked Example: Value Addition"),
 ("steps", [("Example 1 — A potter", "A potter buys clay worth ₹200 and makes pots that he sells for ₹700. **Value added = 700 − 200 = ₹500.** This is the value of his skill, time and effort."),
  ("Example 2 — Tailor", "A tailor buys cloth for ₹800 and sells the stitched kurta for ₹1,500. **Value added = 1,500 − 800 = ₹700.**")]),
 ("h2", "13.9 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["People work for money or money's worth", "Economic activities: salaries, wages, fees, income from sale"],
  ["Care, love and gratitude", "Non-economic activities: caring for the family, sevā, community work"],
  ["Skill, time and effort added to raw material", "Value addition: the product sells for more than the raw material"],
  ["Collective efforts of citizens", "Clean neighbourhoods (Swachh Bharat), more trees (Van Mahotsav)"]]),
 ("note", "IMPORTANT", "Ask yourself two things to classify an activity: **Is it done for money or money's worth?** If yes, it is economic. If it is done from care, gratitude, love or respect with no income, it is non-economic. The same act (teaching) can be either."),
 ("h2", "13.10 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("How are economic activities different from non-economic activities? (3 marks)", "Economic activities involve money or money's worth, such as a lawyer earning a fee or a farmer selling produce. Non-economic activities do not generate income and are done from feelings like love, care and respect, such as parents cooking for the family. Both are important."),
  ("Describe the various ways in which people are paid for economic activities. (5 marks)", "A salary is a fixed monthly payment by an employer, as for a pilot or post-office employee. A wage is payment for a specific period, such as a daily wage of a farm labourer. A fee is paid for professional services such as a doctor, lawyer or online tutor. Payment in kind is non-cash, like mangoes given to Sahil. Traders and farmers earn from the sale of goods."),
  ("Explain value addition with an example. (3 marks)", "Value addition means adding value at each stage of changing something to another form. Rajesh buys wood for ₹600 and makes a chair that he sells for ₹1,000. The ₹400 extra is the value of his skill, time and effort."),
 ]),
]
CH["takeaways"] += ["The same person can do **both** kinds of activity.",
  "**Value added = selling price - cost of raw materials** (the worker's skill, time and effort)."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
