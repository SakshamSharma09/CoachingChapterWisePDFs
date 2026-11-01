from sst_h import *
META = meta(5)
hm, gm = map_pair([('A','Chennai',"The city (then Madras) where the Justice Party, a non-Brahmin party, was founded and which was a centre of the Self-Respect movement."),('B','Nagpur',"The place where the Indian National Congress session of 1920 adopted the Non-Cooperation programme.")],
  [("The nuclear power plant in Maharashtra.", 'Tarapur'), ("The nuclear power plant in Uttar Pradesh.", 'Narora'), ("The nuclear power plant in Tamil Nadu.", 'Kalpakkam'), ("The nuclear power plant in Karnataka.", 'Kaiga')])
HIS = sec("SECTION A — HISTORY", "20 marks", [
 ar("The Zollverein was a customs union formed in 1834 at the initiative of Prussia.", "It abolished tariff barriers and reduced the number of currencies from over thirty to two.", 'a', "Both true; R explains A."),
 stmt("Read the statements.", "The Non-Cooperation Movement began in January 1921.", "Foreign goods were boycotted and liquor shops picketed.", 'a', "Both correct."),
 match("Match the following.", [("1. Zollverein","a. Customs union"),("2. Swaraj Party","b. Formed by C.R. Das and Motilal Nehru"),("3. Khilafat Movement","c. Led by Muhammad Ali and Shaukat Ali")], ["(a) 1-a, 2-b, 3-c","(b) 1-b, 2-a, 3-c","(c) 1-c, 2-b, 3-a","(d) 1-a, 2-c, 3-b"], 'a', "Correct matches."),
 mcq("Which statement about the Indian trade during the colonial period is INCORRECT?", ["Indian indigo was exported to Britain.", "India exported raw cotton and imported finished goods.", "Opium was exported to China.", "India's export surplus helped India to repay its debts."], 'd', "India's export surplus was used to pay Britain's 'home charges', not to benefit India."),
 sa("Why did the Indian workers' participation in the Civil Disobedience Movement remain limited? Give two reasons.", 2, "(1) Industrial workers of Nagpur joined but others stayed away as Congress was reluctant to include workers' demands. (1) Industrialists feared socialism among workers."),
 sa("Explain any three problems that artisans and weavers faced under colonial rule.", 3, "(1) Cotton goods exports declined. (1) Raw cotton supply was restricted due to export. (1) Manchester goods flooded the Indian market; gomasthas controlled weavers."),
 OR(sa("Describe the role of Napoleon in the French Revolution aftermath and its effects on Europe.", 5, "(1) Napoleonic Code 1804 – abolished privileges, equality before law. (1) Simplified administrative divisions. (1) Abolished feudal system. (1) Guild restrictions removed. (1) Some opposition – increased taxation, censorship, forced conscription."),
    sa("Describe the role of newspapers and novels in nationalism in nineteenth century India.", 5, "(1) Vernacular press. (1) Reformers used print to spread ideas. (1) Novels created a sense of identity. (1) Caricatures. (1) Government introduced Vernacular Press Act, 1878.")),
 case_n("Read the source and answer.<br><i>The Government of India Act of 1935 provided for provincial autonomy. Elections of 1937 saw the Congress form governments in 8 of 11 provinces. The Muslim League did not do well.</i>",
  [sub("What did the 1935 Act provide?", 1, "Provincial autonomy."), sub("How many provinces did the Congress rule after 1937?", 1, "Eight of eleven."), sub("Explain how the 1937 election result influenced Muslim League politics.", 2, "(1) The League's poor showing made it seek a separate political identity. (1) It raised the demand for separate electorates and later Pakistan.")]),
 hm])
GEO = sec("SECTION B — GEOGRAPHY", "20 marks", [
 ar("Forests are called the 'lungs of the earth'.", "They absorb carbon dioxide and release oxygen.", 'a', "Both true; R explains A."),
 stmt("Read the statements.", "Project Tiger was launched in 1973.", "Biosphere reserves protect the entire ecosystem.", 'a', "Both correct."),
 match("Match the following.", [("1. Bhakra Nangal","a. Satluj"),("2. Hirakud","b. Mahanadi"),("3. Tehri","c. Bhagirathi")], ["(a) 1-a, 2-b, 3-c","(b) 1-b, 2-a, 3-c","(c) 1-c, 2-b, 3-a","(d) 1-a, 2-c, 3-b"], 'a', "Correct matches."),
 mcq("Which statement about water resources is INCORRECT?", ["Three-fourths of the earth's surface is covered with water.", "Freshwater constitutes about 2.5 per cent.", "India has 4% of world's water resources and 16% of its population.", "India has abundant water in every region."], 'd', "India faces scarcity in many regions."),
 mcq("Which of the following is a cash crop?", ["Wheat", "Sugarcane", "Gram", "Barley"], 'b', "Sugarcane."),
 mcq("Which one is the oldest artificial port of India on the east coast?", ["Chennai", "Kandla", "Mumbai", "Kochi"], 'a', "Chennai is the oldest artificial port of India."),
 mcq("Which of these is a non-conventional source of energy?", ["Coal", "Petroleum", "Solar", "Natural gas"], 'c', "Solar."),
 OR(sa("Why are water resources becoming scarce? Give two reasons.", 2, "(1) Rising population and unequal access. (1) Over-exploitation, pollution and urbanisation."),
    sa("What is rainwater harvesting? Name one method used in Rajasthan.", 2, "(1) Collecting and storing rainwater for future use. (1) Tankas in Bikaner/Phalodi.")),
 sa("Explain any three roles of tertiary and air transport in India.", 3, "(1) Quick, fast, covers difficult terrain. (1) Connects remote areas (North-East). (1) Pawan Hans helicopters; tourism and trade."),
 OR(sa("Describe the importance of forests and wildlife and any four conservation measures.", 5, "(2) Ecological balance, resources, medicine. (3) Project Tiger, Wildlife Protection Act 1972, community participation, biosphere reserves, joint forest management."),
    sa("Describe the pattern of distribution of iron ore in India and its uses.", 5, "(2) Odisha–Jharkhand belt, Durg–Bastar–Chandrapur belt, Ballari–Chitradurga–Chikkamagaluru–Tumakuru belt, Maharashtra–Goa belt. (2) Uses in iron and steel; (1) hematite and magnetite types.")),
 gm])
POL = sec("SECTION C — POLITICAL SCIENCE", "20 marks", [
 ar("Federalism is a system in which power is divided between a central authority and its constituent units.", "India follows a federal system with a strong centre.", 'b', "Both true but R is not the explanation of the definition."),
 stmt("Read the statements.", "In India, caste has completely disappeared from politics.", "Politics gives space to demands of various disadvantaged communities.", 'd', "I is false; II is true."),
 mcq("Which is INCORRECT about the Election Commission?", ["It is an independent body.", "It conducts elections.", "It controls government budgets.", "It supervises electoral rolls."], 'c', "It does not control budgets."),
 mcq("Which of these is a feature of communal politics?", ["Religion is the basis of nation", "Equal treatment of all", "Secular approach", "Rule of law"], 'a', "Communalism treats religion as the basis of nation."),
 mcq("Which of these is NOT a demand of women's movements?", ["Equal wages", "Political representation", "Reservation in local bodies", "Restriction on women's education"], 'd', "Opposite of their demands."),
 mcq("Which statement on democracy is INCORRECT?", ["It improves quality of decision making.", "It provides a method to resolve conflict.", "It enhances dignity.", "It eliminates all inequalities in income."], 'd', "Democracy does not automatically remove economic inequality."),
 sa("What is meant by a 'party system'? Name two types.", 2, "(1) The pattern of competition among parties. (1) One-party, two-party, multi-party."),
 OR(sa("Explain any three measures to reform political parties.", 3, "(1) Anti-defection law. (1) Mandatory disclosure of assets and criminal cases. (1) Compulsory organisational elections and tickets for women."),
    sa("Explain three features of the Indian federal system.", 3, "(1) Three lists. (1) Single judiciary. (1) Union can override in emergencies.")),
 OR(sa("Explain how the reservation of seats for women in local bodies has changed political participation.", 5, "(1) One-third seats reserved. (1) Participation rose. (1) Leadership roles. (1) Questions about proxies ('sarpanch pati'). (1) Demand for similar reservation in Parliament."),
    sa("Explain the different ways in which power is shared in modern democracies.", 5, "(1) Horizontal – legislature, executive, judiciary. (1) Vertical – different levels. (1) Among social groups – reserved constituencies. (1) Among parties – coalition. (1) Through pressure groups and movements.")),
 case_n("Read the source and answer.<br><i>A study showed that in India women's participation in public life is low. Only about 14% of Lok Sabha members are women. Women get lower wages than men for the same work.</i>",
  [sub("What is the percentage of women in the Lok Sabha according to the passage?", 1, "About 14%."), sub("Name one law that ensures equal wages.", 1, "Equal Remuneration Act, 1976."), sub("Suggest two measures to improve women's representation.", 2, "(1) Reservation in Parliament and Assemblies. (1) Education, awareness and party tickets for women.")])])
ECO = sec("SECTION D — ECONOMICS", "20 marks", [
 ar("Money solves the problem of double coincidence of wants.", "Money must be accepted as a medium of exchange.", 'a', "Both true; R explains A."),
 stmt("Read the statements.", "GDP is the value of all final goods and services produced within a country in a year.", "Intermediate goods are also counted in GDP.", 'c', "I true; II false – to avoid double counting."),
 mcq("Which is NOT a developmental goal of people?", ["Regular work", "Security", "Higher prices", "Better wages"], 'c', "Higher prices are not a goal."),
 sa("What is meant by 'Consumer Protection Act'? Why was it needed?", 2, "(1) A law of 1986 (COPRA) to protect consumers. (1) Consumers were exploited by malpractice."),
 OR(sa("Explain three ways through which the government tries to ensure fairness in globalisation.", 3, "(1) Fair rules at WTO. (1) Protect small producers. (1) Labour laws and support for farmers."),
    sa("Explain three features of unorganised sector employment.", 3, "(1) Low pay. (1) No job security. (1) No benefits.")),
 sa("Why do people prefer to deposit money in banks? Give three reasons.", 3, "(1) Safe. (1) Interest. (1) Easy withdrawal via cheques/ATM."),
 OR(sa("Explain the role of the RBI in the Indian economy.", 5, "(1) Issues currency. (1) Supervises banks. (1) Monetary policy. (1) Banker to banks. (1) Maintains reserves."),
    sa("Describe how the government regulates the economy through the public sector and why it is needed.", 5, "(2) Provides infrastructure, jobs. (2) Supports welfare (ration shops, health). (1) Protects weaker groups.")),
 case_n("Read the source and answer.<br><i>Ramesh bought a packet of biscuits whose expiry date was already over. The shopkeeper refused to take it back.</i>",
  [sub("Which consumer right was violated?", 1, "Right to safety / information."), sub("Where can Ramesh complain?", 1, "District Consumer Forum."), sub("Explain two steps he should take.", 2, "(1) Keep the bill and packet as evidence. (1) File a complaint in the consumer court.")])])
SECTIONS = [HIS, GEO, POL, ECO]
