"""Class 7 Social Science Ch 12 - Understanding Markets (NCERT Ch 12): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c7sst_ch12"

def _base():
    s = importlib.util.spec_from_file_location("c7sst_c12", str(REPO / "src/rn_work/c7_sst/c12.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("A market where goods and services are bought and sold within the boundaries of a country is called a:", 1, "(c) domestic market", "E", opts=["wholesale market", "international market", "domestic market", "stock market"]),
W("Those who buy goods in large quantities from producers and store them in godowns are the:", 1, "(a) wholesalers", "E", opts=["wholesalers", "retailers", "consumers", "aggregators"]),
W("The mark that shows food has been tested and is safe is:", 1, "(b) FSSAI", "E", opts=["ISI", "FSSAI", "AGMARK", "BEE star"]),
W("AGMARK is the certification mark for:", 1, "(d) agricultural products", "E", opts=["electrical appliances", "medicines", "electronic goods", "agricultural products"]),
W("A higher BEE star rating on an appliance indicates that it:", 1, "(a) uses less electricity", "E", opts=["uses less electricity", "costs more", "is made abroad", "is heavier"]),
W("Which Portuguese traveller called Hampi 'the best-provided city in the world'?", 1, "(c) Domingos Paes", "E", opts=["Fernao Nuniz", "Adam Smith", "Domingos Paes", "Kautilya"]),
W("The market run entirely by about 3000 women in Imphal, Manipur, is:", 1, "(b) Ima Keithal", "E", opts=["Johari Bazaar", "Ima Keithal", "Khari Baoli", "Hampi Bazaar"]),
W("Fill in the blank: Selling goods produced in one country to buyers in another is called ______.", 1, "export (1)", "E"),
W("Write True or False: A retailer sells goods in large quantities for resale.", 1, "False. A retailer sells in smaller quantities to final consumers; wholesalers sell in bulk. (1)", "E"),
W("What is a market? Name two other names for it.", 2, "A place where people buy and sell goods (and services); bazaar and haat (also marukatte in Kannada). (1+1)", "E"),
W("Define 'price' as used in the chapter.", 2, "Price is the amount at which a buyer is willing to buy and a seller is willing to sell particular goods or services. (2)", "E"),
W("Differentiate between a need and a want with one example each.", 2, "A need is something required to survive, e.g. food; a want is something desired but not essential, e.g. a mobile phone. (1+1)", "E"),
W("What is an aggregator?", 2, "A website or mobile application that organises and combines offers from multiple sellers and sells them to consumers at one place. (2)", "E"),
W("Which city is known as a famous textile hub in Gujarat, and for which other industry is it known?", 2, "Surat; it also has the world's largest diamond industry. (1+1)", "E"),
W("Name two goods for which the government sets a price limit, according to the chapter.", 2, "Lifesaving drugs (maximum price) and essential farm products like wheat, paddy, maize (minimum price). (1+1)", "E"),
W("Give two examples of public goods mentioned in the chapter.", 2, "Public parks, roads, policing. (any two, 1+1)", "E"),
W("What is a distributor?", 1, "A person or business who supplies goods from manufacturers and wholesalers to retailers. (1)", "E"),
W("What does the BEE star rating tell a buyer, and on what kind of goods is it found?", 2, "It shows how energy-efficient an appliance is; more stars mean it uses less electricity (1). It is found on electronic items like TVs, laptops and air conditioners (1).", "E"),
# ---------------- MEDIUM ----------------
W("Explain the three guava-selling scenarios (₹80, ₹20, ₹40 per kg). What price finally works and why?", 3, "At ₹80 buyers find the price very high and may not buy (1). At ₹20 the seller finds it unprofitable and may not sell (1). At ₹40 it is just right: not too high for the buyer and not too low for the seller, so the transaction takes place (1).", "M", wp=True),
W("How do the amount of goods offered by sellers and the amount needed by buyers help determine the price?", 3, "Over time sellers learn the quantity needed by buyers and bring that quantity (1). When the supply offered and the demand wanted come together, the price settles at a level high enough for the seller and low enough for the buyer (2).", "M"),
W("Why are vegetables sold cheaper late at night in a weekly market? Why do garment shops give heavy discounts on woollens at the end of winter?", 3, "Vegetables are perishable, so sellers cut prices to sell them before they spoil (1.5). Woollens are not needed after winter, so demand falls and the shop cuts prices to clear stock (1.5).", "M", wp=True),
W("Differentiate between physical and online markets with one example of each.", 3, "A physical market is where buyers meet sellers in person, e.g. weekly market, haat, mall (1.5). In an online market buyers and sellers transact through websites or apps from far apart and goods are delivered to the doorstep (1.5).", "M"),
W("Differentiate between domestic and international markets. Give one example of an import and one export from the chapter.", 3, "A domestic market is within the country's borders, an international market is across borders (1). Imports: for example vegetable oils from Southeast Asia or crude petroleum from West Asia (1). Exports: for example refined petroleum to West Asia or pharmaceuticals to Africa (1).", "M"),
W("Describe in words the flow of goods in a physical market from the producer to the consumer. What is the role of each participant?", 3, "Producer, then wholesaler (buys in bulk and stores in godowns or cold storage), then distributor (reaches retailers far away), then retailer (sells small quantities to final consumers), then consumer (1+1+1 for correct order and roles).", "M"),
W("How is the distribution chain in an online market different?", 3, "Manufacturers send bulk quantities to the warehouse of a business that sells through an app or website (1). Consumers order online (1). The aggregator packs and delivers the product to the buyer, with no wholesaler or retailer shop in between (1).", "M"),
W("Match: (a) Mandi (b) Godown (c) Cold storage (d) Retailer with (1) stores perishables (2) wholesale market for grains and vegetables (3) large warehouse (4) shop near households.", 3, "(a) with (2), (b) with (3), (c) with (1), (d) with (4). (3 marks for all correct, 2 for three correct)", "M"),
W("Source-based. Fernao Nuniz wrote about Hampi's bazaar: 'There were craftsmen, also, working in their streets... all kinds of rubies and diamonds and pearls...'. (i) What does this show? (ii) Which empire and temple are linked?", 3, "(i) The bazaar was prosperous and full of a wide variety of goods, from jewels to cloth, with craftsmen working in the streets (1.5). (ii) The Vijayanagara Empire; the bazaar was opposite the Virupaksha temple (1.5).", "M"),
W("List four products Domingos Paes noticed in Hampi's market.", 2, "Any four: grains, seeds, milk, oil, silk, cows, rabbits, horses, quails and partridges. (2)", "M"),
W("What are the non-economic roles of a market? Explain with the examples of Ima Keithal and the haldi-kumkum tradition.", 3, "Markets build relationships (e.g. families trust their tailor, jeweller or grocer over decades) and bring people together to exchange ideas and traditions (1). Ima Keithal gives employment to thousands of families and is a melting pot of cultures (1). In south India sellers give a little haldi and kumkum free as a mark of auspiciousness (1).", "M"),
W("How do consumer choices influence production? Use the energy-saving refrigerator example.", 3, "When many consumers ask for refrigerators that use less electricity, this sends a signal along the chain to producers (1.5). Producers make energy-efficient refrigerators, which benefits society (1.5).", "M"),
W("Why can an artist like Aakriti find it difficult to sell her paintings in a local market?", 2, "There are fewer local buyers and sellers of art, so it is hard to find buyers and fix a price (1). Artists can look for buyers through online platforms, exhibitions and fairs. (1)", "M", wp=True),
W("Why does the government set maximum and minimum prices? Give one example of each.", 3, "To protect buyers and sellers (1). Maximum price: lifesaving drugs (1). Minimum price: essential farm products like wheat, paddy and maize, so that farmers do not make losses (also minimum wages) (1).", "M"),
W("What are the risks if price limits are not set carefully?", 2, "If the price is too low, producers have no motivation to produce; if the price is too high, consumers are disadvantaged. (2)", "M"),
W("Explain the government's role in ensuring quality and safety, with the example of medicines.", 3, "The government protects consumers from unfair practices by making manufacturers follow quality and safety standards (1). For medicines it sets procedures for approval (1) and conducts sample testing to check that drugs meet quality standards so that health is not at risk (1).", "M"),
W("What is the use of the FSSAI, ISI, AGMARK and BEE marks? Match each with a product: gram flour, TV, honey, an electric iron.", 3, "FSSAI: food, e.g. gram flour; AGMARK: agricultural products such as honey; BEE star: electronic items such as TV, shows energy efficiency; ISI (BIS): electrical appliances such as an electric iron, shows quality and safety. (Any three correct matches with uses, 1 each)", "M"),
W("Case study. During a festival the supply of onions in Jodhpur's mandi falls sharply. (i) What happens to the price? (ii) Why? (iii) What can the government do?", 3, "(i) The price goes up (1). (ii) When fewer goods are supplied against the same demand, buyers compete and sellers can ask a higher price (1). (iii) It can supply stocks, bring goods from other regions, import, or set price limits carefully (1).", "M", wp=True),
# ---------------- HARD ----------------
W("Case study. Dev, a farmer near Kota, has a bumper tomato crop but the price falls so low that he throws tomatoes away. (i) Why does this happen? (ii) What role can wholesalers play? (iii) Suggest two ways to avoid wastage.", 5, "(i) Too much supply compared with demand pushes the price very low, so selling costs more than it earns (1.5). (ii) Wholesalers can buy in bulk and store the produce in cold storage, sending it to other markets (1.5). (iii) Any two: cold storage, sending to distant mandis, processing into puree or sauce, planning crops by demand, online selling (2).", "H", wp=True),
W("Case study. A family buys beans at ₹30 per kg from a cart seller after a bargain failed at ₹25, and later buys beans at ₹40 per kg from a super bazaar. Why? List two non-price reasons for buying and selling choices.", 4, "The cart seller would make a loss at ₹25 so no sale (1). Family prefers a neat, packed, clean, convenient shop with trust in quality, even at a higher price (1). Non-price factors: quality, convenience, packaging, trust and relationship, reputation, hygiene, location (any two, 2).", "H", wp=True),
W("Why does the chapter say 'markets connect people, traditions and ideas'? Give three examples.", 4, "Markets bring together buyers and sellers from different places and communities (1). Examples: Hampi Bazaar attracted foreign travellers and traders (1); Ima Keithal brings women of different communities together (1); haldi-kumkum custom shows how traditions are shared; online markets link people thousands of km apart (1).", "H"),
W("Read the quotation: 'Prosperity emanates from the market that develops when people need goods and services that they can't create themselves.' (Adam Smith). Explain it with an example from the chapter.", 4, "People cannot produce everything they need, so they depend on others (1). Markets let them exchange (1). Example: Surat's textile makers need cotton which comes from farms in Maharashtra and Gujarat through mandis, and sell their cloth through wholesalers and retailers; all gain income and goods, creating prosperity (2).", "H"),
W("Trace the supply chain of the Surat textile market for cotton cloth. Name three stages and the markets between them.", 4, "Raw cotton reaches Surat through cotton mandis from Maharashtra and Gujarat (1). It is woven on power looms into fabric, dyed in processing units and made into finished goods like sarees and ready-made garments (1). Each stage's product moves through markets: for woven fabric, dyed fabric and finished products (1). Finished goods are traded in the wholesale market and go to small shops and big retail stores across the country and abroad (1).", "H"),
W("Why did Surat become a trading hub? Give four reasons from the chapter.", 4, "West-coast location led to ports and road networks (1); railway and highway links (1); centuries-old communities of expert artisans passing skills over generations (1); trade flourishing from the 16th century and a large supply of raw cotton from nearby areas (1).", "H"),
W("Discuss two merits and two limits of government control over prices.", 4, "Merits: protects consumers from very high prices of essentials like lifesaving drugs; protects farmers with minimum prices; fair wages through minimum wages (any two, 2). Limits: price too low discourages production; too high disadvantages buyers; too many rules can make markets work badly (any two, 2).", "H"),
W("How does the government reduce the 'external effects' of markets? Use single-use plastics and weights and measures as examples, and mention the old Indian rule from Kautilya's Arthashastra.", 4, "Factories can pollute the environment and some goods like single-use plastics cause health risks, so the government makes strict regulations to reduce negative effects (2). It also monitors weights and measures of packaged goods to check the net quantity (1). Kautilya's Arthashastra gave a rule about ghee, adding 1/50th more as manasrava for the quantity lost sticking to the measuring can, showing the idea is old (1).", "H"),
W("Why does the government provide public goods like roads and parks? Why do private producers not provide them?", 3, "Producers sell to make a profit but do not expect profit on goods like parks, roads and policing (1.5). These are used by all members of society and one person's use does not reduce availability for others, so the government provides them for the welfare of citizens (1.5).", "H"),
W("Case study. A packet of gram flour shows net quantity, MRP, date of manufacture, best before date, batch number, FSSAI mark, ingredients, nutrition and allergen declaration. Explain how each of any five helps a consumer judge quality.", 5, "(1 each for any five) Net quantity shows the weight you get; MRP the maximum price; date of manufacture and best before date show freshness; batch number helps trace faults; FSSAI mark shows testing by the government and safety; ingredients and allergen declaration show what the food contains, important for health; nutrition panel shows food value.", "H", wp=True),
W("How can consumers assess quality besides government marks? Evaluate one advantage and one risk of online reviews.", 4, "Reputation by word of mouth from family and friends (1), and online reviews and feedback from other consumers (1). Advantage: gives many experiences, helping decide before buying (1). Risk: reviews may be false or biased, so should be checked with other sources (1).", "H"),
W("Compare the retail market and the wholesale market on seller, buyer, quantity and purpose. Give one example of each.", 4, "Wholesale: sellers are producers or wholesalers; buyers are retailers; bulk quantities; goods are for resale; example mandi or Khari Baoli spice market (2). Retail: sellers are shopkeepers; buyers are final consumers; small quantities; goods for consumption; example grocery store, salon, garment shop (2).", "H"),
]

WS += [
W("Your class sets up a school fair stall. List four steps for a fair buying and selling, using ideas of price, negotiation, quality and honesty from the chapter.", 4, "(1 each) Decide a price with the cost in mind (not too high, not too low); allow polite negotiation; show quantity and quality clearly like a label with date and net quantity; give correct weights and keep the buyer's trust.", "H", wp=True),
W("Online and physical markets: one buyer and one seller viewpoint each. Give one advantage and one disadvantage for the buyer and for the seller of online selling.", 4, "Buyer advantage: wide choice and doorstep delivery from anywhere; buyer disadvantage: cannot touch or check the item, services needing contact like tailoring cannot be provided online (2). Seller advantage: reaches far-away buyers; seller disadvantage: depends on apps, competition from many sellers and delivery needs (2).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "12.9 Timeline and Fact Box"),
 ("table", ["Period / year", "Fact"], [
  ["16th century", "Hampi Bazaar of the Vijayanagara Empire described by the Portuguese Domingos Paes and Fernao Nuniz; Surat's trade also flourished from the 16th century"],
  ["18th century", "Adam Smith, economist quoted at the start of the chapter"],
  ["Ancient India (Arthashastra)", "Rule that buyers of ghee get 1/50 more (manasrava) to make up for loss in measuring"],
  ["2024", "India the world's largest importer of vegetable oils (palm oil mostly from Malaysia, Indonesia and Thailand)"]]),
 ("note", "REMEMBER", "The three scenarios for guavas: ₹80 per kg (too high, no sale), ₹20 per kg (too low, seller will not sell) and ₹40 per kg (just right, sale takes place). The same logic applies to all goods."),
 ("h2", "12.10 Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["**Market**", "A place (physical or online) where people buy and sell goods and services"],
  ["**Needs / wants**", "What is required to survive / what is desired but not essential"],
  ["**Price**", "Amount at which a buyer is willing to buy and a seller to sell"],
  ["**Demand / supply**", "Quantity consumers are willing to buy / quantity sellers are willing to sell at a price"],
  ["**Wholesaler / retailer**", "Buys and sells in bulk / sells small quantities to final consumers"],
  ["**Distributor**", "Supplies goods from manufacturers and wholesalers to retailers"],
  ["**Aggregator**", "App or website combining offers from many sellers"],
  ["**Mandi**", "Wholesale market, e.g. for grains and vegetables"],
  ["**Cold storage**", "Warehouse that keeps perishable goods at low temperature"],
  ["**Import / export**", "Buying from / selling to other countries"],
  ["**Public goods**", "Goods and services available to all, whose use does not reduce availability for others"],
  ["**Inputs for production**", "Materials or resources used to make goods"],
  ["**FSSAI / ISI (BIS) / AGMARK / BEE**", "Marks for food safety / quality of appliances and materials / farm products / energy efficiency"]]),
 ("h2", "12.11 Map and Picture Pointers"),
 ("ul", ["Locate: **Hampi (Karnataka)**, **Surat (Gujarat)** and the cotton areas around it (Surendranagar, Jamnagar, Bhavnagar, Amreli in Gujarat; Amravati, Akola, Nagpur, Wardha, Yavatmal in Maharashtra; Adilabad in Telangana), **Imphal (Manipur)**, **Khari Baoli (Old Delhi)**, **Johari Bazaar (Jaipur)**, **Bengaluru** flower market.",
  "On the world trade map (Fig. 12.10) note India's exports and imports by region: exports of software services to North America, pharmaceuticals to Africa, engineering goods to Europe, refined petroleum to West Asia, chemical products to South America; imports of aircraft and components from North America, diamonds from Africa, electrical equipment from Europe, crude petroleum and fertilizers from West Asia, vegetable oils from Southeast Asia, copper ores from South America.",
  "In the supply flow diagram (Fig. 12.11), follow the arrows: inputs and producer, wholesaler, retailer, consumer."]),
 ("h2", "12.12 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Too high a price", "Buyers do not buy; no transaction"],
  ["Too low a price", "Seller refuses to sell; producers lose motivation"],
  ["Many consumers ask for energy-efficient refrigerators", "Producers make them; society benefits"],
  ["Bumper harvest with low prices", "Farmers may throw away produce; wholesalers and cold storage help"],
  ["Factories and single-use plastics pollute", "Government regulates"],
  ["Consumers need to judge quality", "Certification marks, reviews and word of mouth"]]),
 ("h2", "12.13 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Describe the role of the government in markets. (5 marks)", "The government controls the prices of certain goods: maximum prices for lifesaving drugs and minimum prices for wheat, paddy and maize, and sets minimum wages. It ensures quality and safety standards, for example approval and testing of medicines. It reduces harmful external effects, such as pollution from factories and single-use plastics, and checks weights and measures. It provides public goods like roads, parks and policing. Too many rules can make markets work badly."),
  ("Explain the chain of supply in physical and online markets. (5 marks)", "In physical markets the producer sells to a wholesaler who stores goods in godowns or cold storage and sells in mandis; distributors bring goods to retailers; retailers sell to consumers in small quantities. In online markets manufacturers send bulk goods to the warehouse of an aggregator, who packs and delivers them to the buyer who orders by app or website."),
  ("How can consumers assess quality? (3 marks)", "Look at the label: net quantity, MRP, dates, ingredients; check marks like FSSAI, ISI, AGMARK and BEE stars. Reputation from word of mouth and online reviews also help."),
  ("Why are markets more than a place of buying and selling? (3 marks)", "Markets build long relationships between buyers and sellers over generations, give employment as in Ima Keithal, and bring different communities and traditions together; sellers of haldi-kumkum even give a small free gift as good wishes."),
 ]),
]
CH["takeaways"] += ["Remember the three guava prices (**₹80, ₹20, ₹40**) to explain how price is settled by buyers and sellers.",
  "Quote examples: **Hampi, Surat, Ima Keithal, Khari Baoli, Johari Bazaar, FSSAI, ISI, AGMARK, BEE stars**."]

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
