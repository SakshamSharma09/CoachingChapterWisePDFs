"""Class 6 Social Science Ch 14 - Economic Activities Around Us: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6sst_ch14"

def _base():
    s = importlib.util.spec_from_file_location("c6sst_c14", str(REPO / "src/rn_work/c6_sst/c14.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Activities in which people depend directly on nature to produce goods belong to the:", 1, "(a) primary sector", "E", opts=["primary sector", "secondary sector", "tertiary sector", "non-economic sector"]),
W("Making flour from wheat in a mill is a:", 1, "(b) secondary sector activity", "E", opts=["primary sector activity", "secondary sector activity", "tertiary sector activity", "non-economic activity"]),
W("Which one of these belongs to the tertiary sector?", 1, "(d) banking", "E", opts=["fishing", "mining", "making furniture in a factory", "banking"]),
W("The tertiary sector is also called the:", 1, "(c) service sector", "E", opts=["raw material sector", "factory sector", "service sector", "farm sector"]),
W("AMUL was set up in which year?", 1, "(a) 1946", "E", opts=["1946", "1857", "1975", "1905"]),
W("Who advised the farmers of Anand to form a cooperative?", 1, "(b) Sardar Vallabhbhai Patel", "E", opts=["Mahatma Gandhi", "Sardar Vallabhbhai Patel", "Jawaharlal Nehru", "Kauṭilya"]),
W("People who buy goods from producers and sell them to consumers for a fee are called:", 1, "(d) middlemen", "E", opts=["cooperatives", "technicians", "farmers", "middlemen"]),
W("Heating milk to a specific temperature to kill harmful bacteria is called:", 1, "(a) pasteurisation", "E", opts=["pasteurisation", "recycling", "retail", "export"]),
W("Fill in the blank: Extraction of coal from mines is a ______ sector activity.", 1, "primary. (1)", "E"),
W("Write True or False: The secondary sector depends on the outputs of the primary sector.", 1, "True. It processes raw materials from the primary sector into other products. (1)", "E"),
W("Write True or False: Selling milk by a farmer who milks his own cow is a secondary sector activity.", 1, "False. Milk is obtained directly from a natural source (livestock), so it is a primary activity. (1)", "E"),
W("Name three primary sector activities.", 2, "Any three: agriculture, mining, fishing, raising livestock, forestry (poultry farming, greenhouse farming). (2)", "E"),
W("Name two products which AMUL makes from milk.", 2, "Any two: butter, milk powder, ghee, cheese. (1+1)", "E"),
W("What is a cooperative?", 2, "A group of people who voluntarily come together to meet their economic and social needs in a formal way. They own it and decide together. (2)", "E"),
W("Name two milk cooperatives of India other than AMUL.", 2, "Any two: Nandini (Karnataka), Mother Dairy (Delhi-NCR), Aavin (Tamil Nadu), Vijaya (Andhra Pradesh), Kevi (Nagaland), Sudha (Bihar), Verka (Punjab). (1+1)", "E"),
W("What does the word 'export' mean?", 1, "Goods and services produced in one country and sold to buyers or consumers in another country. (1)", "E"),
W("Name the two persons who led the setting up of AMUL.", 2, "Tribhuvandas Patel (lawyer and freedom fighter) and Dr Varghese Kurien (engineer). (1+1)", "E"),
W("In which district of which State did the AMUL story begin?", 1, "Anand district, Gujarat. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Make a three-column table with sector, nature and two examples for the primary, secondary and tertiary sectors.", 3, "Primary: depends directly on nature; farming, mining. Secondary: processes primary products; flour mill, furniture factory. Tertiary: provides services; banking, transport. (1 each row)", "M"),
W("Classify as primary (P), secondary (S) or tertiary (T): (i) fish farming (ii) making clothes from cotton (iii) a truck driver carrying grain (iv) extracting oil from groundnut (v) a nurse in a hospital (vi) collecting wood from a forest.", 3, "(i) P (ii) S (iii) T (iv) S (v) T (vi) P. (Two correct = 1 mark; all correct = 3)", "M", wp=True),
W("How are wheat, flour mill, truck and bakery connected? Name the sector of each.", 3, "Wheat grown on a farm: primary (1). Flour made in a mill: secondary (1). Truck carrying wheat or flour: tertiary; the bakery sells bread to customers: secondary or tertiary depending on baking or selling (1).", "M", wp=True),
W("Why did the milk farmers of Anand depend on middlemen in the 1940s?", 3, "Milk spoils or curdles quickly in hot weather, so farmers had to sell it quickly (1). Travelling to nearby villages on foot or cycle was a lot of effort for a little money (1). Middlemen bought milk in bulk, though at meagre prices (1).", "M"),
W("Why did the farmers feel cheated and harassed by the middlemen?", 2, "Middlemen paid them very low prices for their milk and the farmers had little choice. (2)", "M"),
W("How did forming a cooperative help the farmers of Anand? Give three points.", 3, "They became independent of middlemen (1). They collectively decided on production, pasteurisation and sale and shared the tasks (1). Their income gradually rose, and women could also take part (1).", "M"),
W("Explain how AMUL's story uses all three sectors, giving one activity of each.", 3, "Primary: farmers milk cows and sell milk (1). Secondary: factories make butter, milk powder, ghee and cheese (1). Tertiary: transport by trucks, rail, air and ship, trading and retail shops (1).", "M"),
W("How do the tertiary sector activities support the farmer who grows vegetables?", 3, "Truck drivers carry vegetables to the market (1). Vendors sell them to households (1). Banks give loans and mechanics repair the tractor (1).", "M", wp=True),
W("Explain how a book reaches you, mentioning the three sectors.", 3, "Primary: trees are cut to get wood pulp (1). Secondary: pulp is made into paper and printed and bound into books (1). Tertiary: transport, distribution and sale of books, and services like designing and publishing (1).", "M"),
W("What are the facts about recycling paper given in the chapter?", 3, "Recycling one tonne of paper saves 17 trees (1) and 2.5 cubic metres of landfill space (1). It takes 70 per cent less energy and water than making new paper from wood pulp (1).", "M"),
W("Find the mistake: \"Construction of roads and supplying electricity are primary sector activities because they are done on the ground.\"", 2, "They belong to the secondary sector, which includes construction and utilities like water, electricity and gas. (2)", "M"),
W("Look at the automobile table (2022): which type was produced in the largest number and which in the smallest, and how many of each?", 3, "Two wheelers were largest at 2 crore units (1.5). Three wheelers were smallest at 8.6 lakh units (1.5).", "M"),
W("Find the total number of passenger vehicles and commercial vehicles produced in India in 2022 from the chapter's table.", 2, "45 lakh + 10.3 lakh = 55.3 lakh. (2)", "M", wp=True),
W("Why has the number of economic activities increased over the decades? Give two examples of new activities.", 3, "As societies progressed, more kinds of work arose to earn livelihoods (1). Earlier it was farming, livestock, tools, pottery and weaving (1). Today there are computers, mobile phones, drones, software and repair of fridges (1). (Any two new examples.)", "M"),
W("Define 'retail' and 'warehouse'.", 2, "Retail is the sale of goods in small quantities to the final consumer. A warehouse is a large building for storing products before they are sold or sent to shops. (1+1)", "M"),
W("Match: (a) Kevi (b) Verka (c) Sudha with (1) Punjab (2) Nagaland (3) Bihar.", 3, "(a) with (2), (b) with (1), (c) with (3). (1 each)", "M"),
W("What does Kauṭilya's Arthaśhāstra say about economic activity?", 2, "The root of prosperity is economic activity; lack of it brings material distress, and its absence harms current prosperity and future growth. (2)", "M"),
W("Give two examples each of secondary sector activities involving (a) construction and utilities (b) manufacturing from primary products.", 3, "(a) Construction of roads and buildings; supply of water, electricity or gas (1). (b) Wood into furniture and paper; cotton into clothes; iron ore steel into cars (any two with the above) (2).", "M"),
# ---------------- HARD ----------------
W("Case study: A farmer in Rajasthan grows bajra. A mill grinds it into flour. A trader sends the flour by truck to a city and a bakery sells rotis. Draw a flow chart with the sector of each stage.", 4, "Farm (primary) -> mill (secondary) -> trader and truck (tertiary) -> roti shop selling to customers (tertiary; the cooking is secondary). (1 mark for each correct stage with the sector, 4 in all)", "H", wp=True),
W("Case study: Mohan, a farmer near Jodhpur, sells milk to a middleman at a low price. His neighbours suggest forming a cooperative like AMUL. Write three reasons for and one difficulty.", 4, "Reasons: no middlemen so better price (1); collective decisions and shared tasks (1); a chance to start processing, such as ghee, giving higher income (1). Difficulty: needs trust, money and cooperation of all members (1).", "H", wp=True),
W("Explain with three examples why the three sectors are interdependent.", 3, "Without the primary sector there would be no raw materials for factories (1). Without the secondary sector, raw materials like wood or cotton could not become furniture or clothes (1). Without tertiary services like transport and banking neither sector could reach customers (1).", "H"),
W("What would happen if the tertiary sector stopped working for a week in your town? Write four effects.", 4, "No transport so vegetables and milk would not reach markets (1). Shops and banks would be closed (1). Hospitals and schools would not work (1). Factories could not send out goods, and farm produce would be wasted (1). Any four sensible effects.", "H", wp=True),
W("The chapter says AMUL uses 'lorries and trucks, railways, air and shipping'. Why does a milk product need so many types of transport?", 3, "Milk and its products have to reach towns, cities and villages all over the country and also other countries (1). Different distances and conditions need road, rail, air or ship transport (1). Fast transport avoids spoilage and delays (1).", "H"),
W("Draw up a table of ten activities from your neighbourhood and classify each as primary, secondary or tertiary. Draw arrows to show connections for two chains.", 4, "Sample: farming (P), dairy (P), flour mill (S), tailor making clothes (S), bakery (S), shop (T), bus driver (T), doctor (T), teacher (T), electrician (T). Chains: farm -> flour mill -> shop; cotton farm -> cloth mill -> tailor -> shop. (2 for the classification and 2 for two correct chains)", "H", wp=True),
W("Why is the story of AMUL an example of the 'power of working together'? Use the words cooperative, middlemen and income.", 3, "Farmers formed a cooperative (1) and removed the middlemen who paid them low prices (1), so their income rose gradually and they became independent, like one big family (1).", "H"),
W("Compare the primary and the secondary sector: give one similarity and two differences.", 3, "Similarity: both produce goods and create monetary value (1). Differences: the primary sector takes raw materials from nature while the secondary sector transforms them into other products (1); the primary uses farms, mines, forests while the secondary uses factories and production units (1).", "H"),
W("Why is the production of cars classified as secondary, but its transport to showrooms as tertiary? Explain.", 3, "Making cars processes materials like steel from iron ore in factories, which is manufacturing (secondary) (1.5). Moving cars from the factory to showrooms is a service that helps the sale of goods (tertiary) (1.5).", "H", wp=True),
W("List four ways to use paper wisely in your school. Explain how this links to the primary sector.", 3, "Use both sides of paper, reuse old sheets for rough work, avoid wasteful printing, recycle used paper (any three, 0.5 each). Paper comes from wood pulp from trees, a primary activity; saving paper saves 17 trees per tonne recycled (1.5).", "H", wp=True),
W("Explain how the farmers of Anand gradually moved from the primary to the secondary sector. Why did they do it?", 3, "At first they only milked cows and sold milk (primary) (1). As more milk was collected than was needed, they set up a factory in Anand for butter and milk powder (secondary) (1). It made use of the huge quantity of milk and raised their income (1).", "H"),
W("Why is the tertiary sector called the 'service sector'? Give three examples that we cannot always see but which matter.", 3, "It provides services and not goods (1). Examples: communication through mobile and internet, banking and software development, warehouses and repair services (2).", "H"),
W("In which sector would you place a person who repairs a tractor in a village? Which other sectors does he support? Give reasons.", 3, "He is in the tertiary sector, as a mechanic offering a repair service (1). He supports the primary sector, since the farmer needs the tractor to cultivate land (1) and indirectly the secondary sector which processes farm outputs (1).", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "14.4 Timeline of the AMUL Story"),
 ("table", ["When", "What happened"], [
  ["Early 1940s", "Farmers in Anand district sold milk to nearby villages or to middlemen at low prices"],
  ["Before 1946", "Farmers approach Sardar Vallabhbhai Patel, who advises forming a cooperative"],
  ["1946", "Anand Milk Union Limited (AMUL) set up under Tribhuvandas Patel and Dr Varghese Kurien"],
  ["Later", "Factory in Anand for butter and milk powder; many plants across India; products sold in retail shops and exported"],
  ["2022", "Automobile figures: about 2 crore two wheelers, 45 lakh passenger vehicles, 10.3 lakh commercial vehicles, 8.6 lakh three wheelers (SIAM)"]]),
 ("h2", "14.5 Key Terms and People"),
 ("table", ["Term / person", "Meaning"], [
  ["**Monetary value**", "Value of something measured in money"],
  ["**Economic sector**", "Broad group of activities that help a nation's prosperity"],
  ["**Primary sector**", "Extraction of raw materials directly from nature"],
  ["**Secondary sector**", "Processing primary products; construction; utilities"],
  ["**Tertiary sector**", "Services that support the other two sectors"],
  ["**Cooperative**", "Group of people who voluntarily work together to meet economic and social needs and own it together"],
  ["**Middlemen**", "People who buy from producers and sell to consumers for a fee"],
  ["**Pasteurisation**", "Heating milk to kill harmful bacteria"],
  ["**Retail**", "Selling goods in small quantities to the final consumer"],
  ["**Export**", "Selling goods to another country"],
  ["**Warehouse**", "Large building for storing products"],
  ["**Tribhuvandas Patel**", "Lawyer and freedom fighter who led AMUL"],
  ["**Dr Varghese Kurien**", "Engineer who worked at a dairy factory in Mumbai and helped set up AMUL"],
  ["**Sardar Vallabhbhai Patel**", "National leader who advised the farmers to form a cooperative"]]),
 ("h2", "14.6 Map and Picture Pointers"),
 ("ul", ["Locate **Anand district in Gujarat** on the political map of India; mark Gujarat as the home of AMUL.",
  "Mark the States with milk cooperatives in the chapter: **Karnataka (Nandini), Delhi-NCR (Mother Dairy), Tamil Nadu (Aavin), Andhra Pradesh (Vijaya), Nagaland (Kevi), Bihar (Sudha), Punjab (Verka)**.",
  "In the sector chart: primary (agriculture, mining, fishing, livestock, forestry), secondary (construction, manufacturing, water supply, solar power, electricity), tertiary (healthcare, trade and logistics, communication, banking, transportation)."]),
 ("h2", "14.7 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Societies progressed", "Many more economic activities and sectors"],
  ["Milk spoils quickly and farmers depended on middlemen", "Low prices and unhappy farmers"],
  ["Cooperative formed in 1946", "Farmers controlled production and sale; income rose"],
  ["Large quantity of milk collected", "Factories for butter and milk powder; many products"],
  ["Paper is recycled", "Trees, landfill space, energy and water are saved"]]),
 ("note", "IMPORTANT", "Quick test: **Taken from nature? Primary. Changed into another product (or built / utilities)? Secondary. Service that helps others? Tertiary.**"),
 ("h2", "14.8 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("What is the primary sector? How is it different from the secondary sector? Give two examples of each. (5 marks)", "The primary sector extracts raw materials directly from nature, for example farming and fishing. The secondary sector depends on primary outputs and transforms them into products, for example making flour in a mill and furniture from wood. The primary sector gets the raw material; the secondary sector changes its form."),
  ("How does the secondary sector depend on the tertiary sector? (3 marks)", "Factories need transport to bring raw materials and send out goods, banks for money, electricians and mechanics for machines, and shops to sell the products. All these are tertiary services."),
  ("Describe the AMUL story and show the three sectors in it. (5 marks)", "In the 1940s Anand's farmers depended on middlemen who paid low prices. On Sardar Patel's advice they formed a cooperative, AMUL, in 1946 under Tribhuvandas Patel and Dr Varghese Kurien. Milking cows is primary. Making butter, milk powder, ghee and cheese in factories is secondary. Transport by trucks, rail, air and ship, trading and retail shops are tertiary."),
 ]),
]
CH["takeaways"] += ["Sector test: **nature -> primary; processing -> secondary; services -> tertiary.**",
  "AMUL (1946, Anand, Gujarat) shows farmers' **cooperation** and the three sectors together.",
  "Recycling one tonne of paper saves **17 trees**."]

if __name__ == "__main__": run(__file__, BANK, 6, "Social_Science", WS, CH)
