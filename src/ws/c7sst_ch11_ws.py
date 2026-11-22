"""Class 7 Social Science Ch 11 - From Barter to Money (NCERT Ch 11): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c7sst_ch11"

def _base():
    s = importlib.util.spec_from_file_location("c7sst_c11", str(REPO / "src/rn_work/c7_sst/c11.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("A system of exchanging goods and services without using money is called:", 1, "(b) the barter system", "E", opts=["a banking system", "the barter system", "a tax system", "digital banking"]),
W("The situation in which two people each have something the other wants is called:", 1, "(a) double coincidence of wants", "E", opts=["double coincidence of wants", "common denomination", "divisibility", "minting"]),
W("The ancient Indian metal coins were called:", 1, "(c) karshapanas or panas", "E", opts=["rupees", "annas", "karshapanas or panas", "tajaderos"]),
W("Giant discs of rock used as money on Yap Island were called:", 1, "(d) Rai stones", "E", opts=["Tajadero", "Tevau", "cowrie", "Rai stones"]),
W("Only which authority is legally allowed to issue currency notes in India today?", 1, "(b) Reserve Bank of India", "E", opts=["State Bank of India", "Reserve Bank of India", "Any commercial bank", "The Finance Ministry's shops"]),
W("The rupee symbol was designed by:", 1, "(a) Udaya Kumar of IIT Bombay", "E", opts=["Udaya Kumar of IIT Bombay", "Kautilya", "John Maynard Keynes", "Krishnappa"]),
W("The Junbeel Mela, where barter still takes place, is held in which state?", 1, "(c) Assam", "E", opts=["Kerala", "Rajasthan", "Assam", "Tamil Nadu"]),
W("Fill in the blank: Money is accepted by everybody as a ______ of exchange.", 1, "medium (1)", "E"),
W("Write True or False: Paper money was first used in China.", 1, "True. (1)", "E"),
W("Name any two commodities that people used as a medium of exchange in barter times.", 2, "Any two: cowrie shells, salt, tea, tobacco, cloth, cattle, seeds. (1+1)", "E"),
W("What is meant by 'common standard measure of value'?", 2, "An agreed-upon worth that helps determine the value of goods and services; barter lacked it, so it was hard to compare the value of goods. (2)", "E"),
W("What is a 'mint'?", 1, "A manufacturing facility that produces coins used as a nation's currency. (1)", "E"),
W("What is an alloy? Why were coins made from alloys?", 2, "An alloy is a metal made by combining two or more metallic elements (1); it makes the coin strong (1).", "E"),
W("Give two examples of digital forms of money.", 2, "Any two: UPI, debit cards, credit cards, net banking, QR code payments. (1+1)", "E"),
W("State the fraction of a rupee that 1 anna was equal to.", 1, "1/16 of a rupee. (1)", "E"),
W("What are 'denominations'? Give one example from India.", 2, "Units in which coins and notes are classified; e.g. 50 paisa, Rs 1, Rs 5, Rs 10 coins or notes of Rs 10, Rs 20, Rs 50 and Rs 100. (2)", "E"),
W("What does QR stand for?", 1, "Quick response. (1)", "E"),
W("Fill in the blank: The chapter says 'necessity is the mother of ______' while explaining why money came into existence.", 1, "invention (1)", "E"),
W("Name the places where any two of these were used as money: Rai stones, the Aztec Tajadero, the Tevau.", 2, "Rai stones: Yap Island (Micronesia, Pacific); Tajadero: Central Mexico and parts of Central America; Tevau: Solomon Islands. (1+1 for any two)", "E"),
# ---------------- MEDIUM ----------------
W("What is barter? Explain with the example of the pencil and eraser.", 3, "The barter system is a way of exchanging goods and services without money (1). You have an extra eraser and need a pencil, while your classmate has an extra pencil and needs an eraser (1). You exchange them directly, so both needs are met (1).", "M"),
W("Explain any three problems of the barter system with one line on each.", 3, "Any three: double coincidence of wants: both persons must want what the other has; lack of a common standard measure of value: hard to decide the proportion of exchange; divisibility: you cannot exchange part of an ox for a sweater; portability: carrying an ox or many bags everywhere; durability: wheat rots or is eaten by rats if stored. (1 each)", "M"),
W("A farmer has an ox and needs shoes, a sweater and medicines. Which problems of barter does he face?", 3, "He must find someone who needs an ox and offers what he needs: double coincidence of wants (1). Exchanging a whole ox for shoes is unfair and he cannot divide the ox: lack of a common measure and divisibility (1). Carrying the ox or the wheat everywhere is a portability problem and the wheat may rot: durability (1).", "M", wp=True),
W("How does money solve the problems of the farmer in the story?", 3, "He can sell the ox for money to anyone who wants it, so there is no need for double coincidence (1). Money is divisible, so he can pay the exact price for shoes, sweater and medicines, with the same measure of value (1). It is easy to carry and can be stored for a long time without rotting (1).", "M", wp=True),
W("Explain the three basic functions of money, with one example each.", 3, "Medium of exchange: buying vegetables with money (1). Store of value: the farmer keeps money to buy things later (1). Common denomination (measure of value) or standard of deferred payment: prices are compared in rupees; paying the rest of a Rs 100 book's cost later (1).", "M"),
W("What is 'standard of deferred payment'? Use the Rs 50 and Rs 100 book example.", 3, "It means money is accepted as a way of making payments later (1). If you have only Rs 50 for a book worth Rs 100, you may pay Rs 50 now and the rest later (1) and the shopkeeper accepts the promise in money terms (1).", "M", wp=True),
W("Describe the Junbeel Mela. Why is it a surviving example of barter?", 3, "A three-day annual fair at Junbeel in Morigaon district of Assam, beginning with Agni Puja (1). Tribal communities such as Tiwa, Karbi, Khasi and Jaintia gather; since the 15th century it has grown into a fair where people exchange produce (1). Hill products like roots, herbs, spices and handmade goods are exchanged for rice cakes and other foods from the plains, without money (1).", "M"),
W("Give two modern examples of barter in daily life from the chapter.", 2, "Exchange of old clothes for new utensils with a vendor; book exchange among friends (also pencil-eraser swaps). (1+1)", "M"),
W("Describe the main features of ancient Indian coins.", 3, "Made of precious metals like gold, silver, copper or alloys (1); called karshapanas or panas, with symbols punched on them called rupas (1); minting and issue controlled by the rulers; two sides (obverse and reverse) carried different symbols like animals, trees, kings or deities (1).", "M"),
W("Name the images on the coin of the Chalukyas of Kalyana and the Chola silver coin.", 2, "Chalukyas: Varaha (avatar of Vishnu) on one side and a decorated three-tiered parasol on the other (1). Cholas: a tiger emblem (1).", "M"),
W("Roman gold coins were found at Pudukkottai in Tamil Nadu. What conclusions can be drawn?", 3, "Southern India traded with the Roman world (1). Coinage helped boost India's maritime trade with the world (1). Since Roman coins were found in Kerala and Tamil Nadu, scholars conclude that the trade was in favour of India (1).", "M"),
W("Why did people shift from coins to paper money?", 3, "As coins were used for all exchanges, from vegetables to land, it became difficult to carry large numbers of coins (1.5), and storing them was also a problem; paper money was a more suitable alternative (1.5).", "M"),
W("Timeline. Arrange from the oldest to the newest according to the chapter: UPI, metal coinage (600 BCE), barter (6000 BCE), debit and credit cards (1980), official paper money (1861).", 3, "Barter (6000 BCE), metal coinage (600 BCE), official paper money (1861), debit and credit cards (1980), UPI (2016). (3 for all five in order; 2 for three correct)", "M"),
W("What are the roles of coins and paper currency in terms of denominations today?", 2, "Coins are used for smaller denominations (1), paper currency for higher denominations (1).", "M"),
W("Mark the mistake: 'Today any bank can print and issue notes in India.'", 2, "Wrong. It is illegal for anyone other than the Reserve Bank of India to issue currency (2).", "M"),
W("Source-based. 'The importance of money flows from it being a link between the present and the future.' (J.M. Keynes). Explain the quotation with an example.", 3, "Money can be saved today and used later, so it links the present with the future (1.5). For example, the farmer can keep money from selling an ox and buy shoes next month, which he could not do with wheat that rots (1.5).", "M"),
W("Give two features of the ₹ sign and who designed it.", 3, "Designed by Udaya Kumar of IIT Bombay (1). It mixes the Devanagari 'Ra' and the Roman 'R' (1) with two parallel horizontal stripes representing the national flag and the 'equal to' sign; adopted in 2010 (1).", "M"),
W("A shopkeeper in Kota takes an old shirt from a customer and gives a steel bowl in return. (i) Which system is it? (ii) Write one benefit to each side as the chapter explains.", 3, "(i) The barter system (1). (ii) The household gets rid of an item it no longer needs; the vendor collects material that can be resold, repurposed or recycled (2).", "M", wp=True),
# ---------------- HARD ----------------
W("Source-based. 'An annual salary of 60 panas could be substituted by an adhaka of grain per day, enough for four meals' (Arthashastra). One adhaka is about 3 kg. (i) How much grain would that be in 30 days? (ii) The fine for failing to help a neighbour was 100 panas. Compare with the annual salary and say what value is encouraged.", 4, "(i) 3 kg x 30 = 90 kg of grain a month (1). (ii) The fine of 100 panas is more than the annual salary of 60 panas (1; 100 - 60 = 40 panas more); so the fine is heavy (1), which encourages the human value of helping and caring for neighbours (1).", "H", wp=True),
W("Evaluate: 'The barter system is completely outdated.' Use two examples to agree or disagree.", 4, "Money has replaced barter in most places (1), but barter still exists: the Junbeel Mela in Assam (1.5), exchange of old clothes for utensils and book exchange clubs (1.5). So barter is rare but not completely gone, and it benefits both sides in these cases.", "H"),
W("Case study. Anita, a vendor in Jaipur, receives UPI payments through a QR code on her cart. (i) How does this help her? (ii) How is it different from a coin? (iii) Name two other methods like this.", 4, "(i) Customers scan the code and the payment goes directly into her bank account, so there is no need to carry cash (1). (ii) It is intangible, digital money in electronic form that cannot be touched or felt, while a coin is a physical object (1). (iii) Debit cards, credit cards, net banking (any two) (2).", "H", wp=True),
W("Explain with an example how a lack of a common standard measure of value makes barter difficult. How does money fix it?", 3, "If a person has an ox and another has a sweater, there is no agreed rule on how many sweaters equal an ox, so one side may feel the exchange is unfair and refuse (2). Money gives a common denomination so prices of all goods can be compared and fixed in rupees (1).", "H"),
W("Describe the 'journey of money' in India in five steps from the chapter, with one feature of each.", 5, "Barter (about 6000 BCE): exchange of goods and services; commodity money (cowrie shells, salt, cattle etc.); metal coins (from about 600 BCE): gold, silver, copper, issued by rulers; paper money (introduced in the late 18th century, official in 1861): easier to carry; digital money (debit and credit cards from about 1980, UPI in 2016): intangible. (1 each)", "H"),
W("Why did powerful rulers' coins get accepted in other kingdoms? What was the effect on trade?", 3, "The minting and issue of coins was controlled entirely by rulers, and over time coins of powerful rulers were accepted in various kingdoms and not only their own (2). This made exchange easier and facilitated trade across geographies (1).", "H"),
W("The Aztec Tajadero, the Rai stones and the Tevau were all used as money. What does this show about the idea of money, and which problem would the Rai stones have faced?", 4, "It shows that money is whatever a community commonly accepts as a medium of exchange; it need not be metal (2). Rai stones were giant discs of rock, so they would have had a portability problem (2).", "H"),
W("'Necessity is the mother of invention.' Explain how this applies to the invention of money, with reference to the chapter.", 4, "As the types and numbers of goods increased and trade distances became longer, barter became hard (2). A common medium of exchange was needed to make trade easier, so money came into existence and became the accepted method of payment (2).", "H"),
W("Mini project. A class collects old coins. List four details they should note, and say one thing each could tell them.", 4, "(1 each) What the coin is made of (metal or alloy); the year inscribed (when it was used); the obverse (head side) and the reverse designs (rulers, deities, animals, language); the denomination and language (the value and the region or ruler).", "H", wp=True),
W("Compare coins, paper money and digital money on form, portability and one risk or limit.", 4, "Coins: metallic, tangible; heavy to carry in bulk (storage problem). Paper money: light, tangible, issued by RBI; can be misused if forged, so security features are used. Digital money: intangible, in electronic form, easy to transfer from one bank account to another; needs a device and internet. (1 + 1 + 2)", "H"),
W("Do you think money makes society fairer than barter? Give two reasons from the chapter and one limit.", 4, "Yes: money gives a common standard measure of value so exchanges are fair (1.5); it removes the need for a double coincidence of wants and is divisible, portable and durable (1.5). Limit: it must be controlled by a trusted authority like the RBI, and digital payments need technology and awareness (1).", "H"),
W("Why does the chapter say that coinage is also a source of history? Give two examples from the chapter.", 3, "Coins show rulers' symbols, deities and trade links (1). Roman gold coins found at Pudukkottai show trade with Rome (1); Chola tiger coins and Chalukya Varaha coins show the emblems and beliefs of those dynasties (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "11.6 Timeline: The Journey of Money"),
 ("table", ["Period", "Form of money / event"], [
  ["About 6000 BCE", "Barter, with commodities as media of exchange (cowrie shells, salt, cattle, etc.)"],
  ["About 600 BCE", "Metal coinage of iron, silver, gold and copper; karshapanas / panas with punched rupas"],
  ["Ancient to medieval", "Rulers issue coins with symbols: Chola tiger, Chalukya Varaha and parasol"],
  ["Late 18th century", "Paper money introduced in India (Bank of Bengal, Bank of Bombay notes)"],
  ["1861", "Official paper money (as shown on the chapter's timeline)"],
  ["1942-1947", "Coins of anna denominations; in 1947 one anna could buy a dozen bananas"],
  ["1980", "Debit and credit cards"],
  ["2010", "The rupee symbol adopted by the Government of India"],
  ["2016", "UPI (Unified Payments Interface)"],
  ["2021", "Special coin to mark 75 years of independence"]]),
 ("note", "REMEMBER", "In the chapter's timeline (Fig. 11.10) the labels are barter, cowrie, metal coinage, official paper money, debit and credit cards and UPI. Learn the order of forms, and 600 BCE for coins, 1861 for official paper money, 2016 for UPI."),
 ("h2", "11.7 Key Terms"),
 ("table", ["Term", "Meaning"], [
  ["**Barter system**", "Exchange of goods and services without money"],
  ["**Commodity**", "A product or good that can be bought, sold or traded"],
  ["**Transaction**", "A piece of business, especially buying or selling"],
  ["**Double coincidence of wants**", "Two persons each have what the other wants"],
  ["**Common standard measure of value**", "Agreed worth that helps compare goods and services"],
  ["**Divisibility / portability / durability**", "Can be split / can be carried / lasts a long time"],
  ["**Medium of exchange**", "What everyone accepts as payment in trade"],
  ["**Store of value**", "Money can be kept and used later"],
  ["**Standard of deferred payment**", "Money accepted for making payment later"],
  ["**Common denomination**", "Money measures the value of goods and services so they can be compared"],
  ["**Minting / mint**", "Making coins / the place where they are made"],
  ["**Obverse and reverse**", "Head side and tail side of a coin"],
  ["**Currency and denomination**", "A country's money system / the units of coins and notes"],
  ["**RBI**", "The Reserve Bank of India, the only legal issuer of currency"],
  ["**QR code**", "Quick-response code with the receiver's bank account details, scanned to pay"]]),
 ("h2", "11.8 Map and Picture Pointers"),
 ("ul", ["Locate on a world map: **Yap Island (Micronesia, Pacific)** for Rai stones, **Central Mexico** for Aztec Tajadero, **Solomon Islands** for Tevau, **China** (first paper money).",
  "In India: **Junbeel (Morigaon district, Assam)**; **Pudukkottai (Tamil Nadu)** where Roman gold coins were found; Kerala and Tamil Nadu coast (Roman coins show trade).",
  "In the pictures of coins (Fig. 11.11 to 11.13) observe the obverse and reverse symbols, and look at the 50 and 100-rupee notes for heritage motifs and features that help visually impaired people."]),
 ("h2", "11.9 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Problems of barter: double coincidence, no common measure, divisibility, portability, durability", "Need for a common medium of exchange: money"],
  ["More goods and longer trading distances", "Money came into use"],
  ["Rulers controlled coin minting; powerful rulers' coins accepted widely", "Easier trade across kingdoms"],
  ["Large numbers of coins hard to carry and store", "Paper money"],
  ["Advance in technology", "Digital money: cards, UPI, QR codes"],
  ["Need to prevent forgery", "RBI introduces security features on notes"]]),
 ("h2", "11.10 Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("What were the limitations of the barter system? (5 marks)", "Double coincidence of wants: one must find someone who wants what he offers and offers what he wants. No common standard measure of value: it is hard to decide how much of one good equals another. Divisibility: a whole ox cannot be exchanged for part of a sweater. Portability: heavy items are hard to carry about. Durability: goods like wheat can rot or be eaten by rats."),
  ("Explain the functions of money. (3 marks)", "Money is a medium of exchange accepted by everyone. It is a store of value that can be kept and used later. It is a common denomination to measure and compare the values of goods and services and a standard of deferred payment."),
  ("How has money changed over time? (5 marks)", "Barter existed before money, using commodities like cowrie shells, salt and cattle. Metal coins of gold, silver, copper and alloys were issued by rulers (karshapanas). Paper money, first used in China, came to India in the late 18th century, and is issued only by the RBI. Today digital money (cards, net banking, UPI and QR codes) transfers money from one bank account to another."),
  ("Why are Indian coins important to historians? (3 marks)", "Coins show symbols, rulers and gods, and the finds of Roman coins in Kerala and Tamil Nadu show that India had trade with the world; they also show that the trade was in India's favour."),
 ]),
]
CH["takeaways"] += ["Link problem to solution: each **barter problem** (double coincidence, measure of value, divisibility, portability, durability) is solved by money.",
  "Names to recall: **karshapanas/panas, rupas, obverse/reverse, RBI, UPI, QR code, Rs sign by Udaya Kumar**."]

if __name__ == "__main__": run(__file__, BANK, 7, "Social_Science", WS, CH)
