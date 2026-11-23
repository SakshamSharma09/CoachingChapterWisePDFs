"""Class 10 Social Science Ch 9 - Agriculture (Geography Ch 4): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch09"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)
AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def ar(a, r, i, why, lvl="E"):
    return W(f"Assertion (A): {a}  Reason (R): {r}  Choose the correct option.", 1, f"({'abcd'[i]}) {AR[i]}. {why}", lvl, opts=AR)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("Slash and burn agriculture is called 'jhumming' in:", ["Punjab and Haryana", "the north-eastern states such as Assam, Meghalaya, Mizoram and Nagaland", "Kerala and Tamil Nadu", "Gujarat and Rajasthan"], 1, "In Mexico and Central America the same system is called milpa."),
mc("Farming in which a single crop is grown on a large area with capital-intensive inputs and migrant labour is:", ["intensive subsistence farming", "primitive subsistence farming", "plantation farming", "shifting cultivation"], 2, "Tea, coffee, rubber and banana are examples."),
mc("Which one of these is a rabi crop?", ["Paddy", "Gram", "Cotton", "Bajra"], 1, "Wheat, barley, peas, gram and mustard are the main rabi crops."),
mc("Which crop is known as the 'golden fibre'?", ["Cotton", "Hemp", "Jute", "Silk"], 2),
mc("Being leguminous, pulses help in restoring soil fertility by:", ["adding potash", "fixing nitrogen from the air", "absorbing salts", "stopping evaporation"], 1, "That is why they are grown in rotation with other crops."),
mc("The Arabica variety of coffee, grown in India, was initially brought from:", ["Brazil", "Yemen", "Kenya", "Sri Lanka"], 1, "Its cultivation was first introduced on the Baba Budan Hills."),
mc("The Bhoodan movement was started by:", ["Mahatma Gandhi", "Vinoba Bhave", "Jawaharlal Nehru", "Sardar Patel"], 1, "It is also called the Blood-less Revolution."),
mc("Which crop needs more than 200 cm of rainfall and a temperature above 25 degrees C?", ["Wheat", "Rubber", "Bajra", "Gram"], 1),
W("Name the three cropping seasons of India.", 1, "Rabi, kharif and zaid. (1)", "E"),
W("Fill in the blanks: Rabi crops are sown from ______ to ______ and harvested from April to June.", 1, "October; December. (1)", "E"),
W("Define (i) plantation farming (ii) horticulture.", 2,
  "(i) Commercial farming in which a single crop is grown on a large area using capital-intensive inputs and migrant labour, the produce going to an industry as raw material (1). (ii) Growing of fruits and vegetables (1).", "E"),
W("Name any two crops grown in the 'zaid' season.", 1, "Any two of watermelon, muskmelon, cucumber, vegetables, fodder crops. (1)", "E"),
W("Match: (i) Wheat (ii) Jute (iii) Rubber (iv) Millets.  A. Equatorial crop  B. Coarse grain  C. Rabi crop  D. Fibre crop.", 2,
  "(i)-C, (ii)-D, (iii)-A, (iv)-B. (all four = 2 marks; two or three correct = 1 mark)", "E"),
W("True or false (with a reason): 'Rice is a commercial crop in all parts of India.'", 2,
  "False (1). It is a commercial crop in Punjab and Haryana but a subsistence crop in Odisha, so the degree of commercialisation differs from region to region (1).", "E"),
W("Name two states each that lead in the production of (i) tea (ii) jute.", 2,
  "(i) Assam and West Bengal (Darjeeling and Jalpaiguri), also Tamil Nadu and Kerala (1). (ii) West Bengal and Bihar, also Assam, Odisha and Meghalaya (1). (any two for each)", "E"),
W("Expand the abbreviations (i) KCC (ii) PAIS and say what each gives to a farmer.", 2,
  "(i) Kisan Credit Card: credit (loans) at low interest (1). (ii) Personal Accident Insurance Scheme: insurance cover against accidents (1).", "E"),
W("Name any two items that are made from sugarcane.", 1, "Sugar, gur (jaggery), khandsari and molasses (any two). (1)", "E"),
# ------------------------------------------------------------------ MEDIUM (20)
ar("Pulses are mostly grown in rotation with other crops.", "Being leguminous crops, pulses fix nitrogen in the soil.", 0, "Fixing nitrogen restores fertility, so a rotation with cereals benefits the next crop.", "M"),
ar("In India three crops of paddy are grown in a year in Assam, West Bengal and Odisha.", "Rice is the staple food crop of a majority of the people in India.", 1, "Both statements are true (the three crops are Aus, Aman and Boro), but the staple status of rice does not explain why three crops can be grown there.", "M"),
W("Differentiate between primitive subsistence farming and commercial farming on four points: tools, purpose, inputs and productivity.", 3,
  "Primitive: hoe, dao and digging stick; to feed the family; no fertilisers or modern inputs; low productivity (1.5, any two points matched). Commercial: machines and modern tools; produce for sale in the market; HYV seeds, chemical fertilisers, pesticides and irrigation; higher productivity (1.5, any two points matched).", "M"),
W("Why is primitive subsistence farming called 'slash and burn' agriculture? Why do farmers move to a fresh patch?", 3,
  "The farmer clears a patch of land by cutting and burning the vegetation and grows cereals and other food crops for the family (1). Because no fertilisers are used, soil fertility falls after some time (1). The farmer then shifts to a fresh patch, allowing nature to restore fertility through natural processes (1).", "M"),
W("Why is intensive subsistence farming practised in areas of high population pressure? Mention two features.", 2,
  "Land is scarce and many people depend on it, so farmers must take the maximum output from a small plot (1). It is labour-intensive, with high doses of biochemical inputs and irrigation; holdings are small because the right of inheritance has divided them among generations (1).", "M"),
W("Ritu's family in Anand grows wheat in winter and paddy after the monsoon on the same farm. (i) Classify each crop by season. (ii) When will she sow and harvest the wheat? (iii) Name one zaid crop she could add in summer.", 3,
  "(i) Wheat is a rabi crop and paddy is a kharif crop (1). (ii) Wheat is sown from October to December and harvested from April to June (1). (iii) Any one of watermelon, muskmelon, cucumber, vegetables or fodder (1).", "M", wp=True),
W("Group the following crops by season (rabi, kharif, zaid): mustard, cotton, cucumber, soyabean, barley, watermelon.", 3,
  "Rabi: mustard, barley (1). Kharif: cotton, soyabean (1). Zaid: cucumber, watermelon (1).", "M"),
W("Why does wheat grow well in the Ganga-Satluj plains? Give three conditions required for wheat.", 3,
  "Wheat needs a cool growing season and bright sunshine at the time of ripening (1), and 50 to 75 cm of annual rainfall evenly distributed over the growing season (1). The Ganga-Satluj plains in the north-west and the black soil region of the Deccan are the two important wheat-growing zones; winter showers from western temperate cyclones and irrigation further help (1).", "M"),
W("Millets are called coarse grains but have high nutritional value. Support this with the example of ragi, and name one major producing state each of jowar, bajra and ragi.", 3,
  "Ragi is very rich in iron, calcium, other micro-nutrients and roughage (1). Jowar: Maharashtra (or Karnataka, Andhra Pradesh, Madhya Pradesh) (1). Bajra: Rajasthan (or Uttar Pradesh, Gujarat, Haryana); ragi: Karnataka (or Tamil Nadu) (1).", "M"),
W("A farmer in Barmer (Rajasthan) with sandy soil and scanty rainfall asks which cereal is best for his field. Suggest one crop with two reasons.", 2,
  "Bajra (1). It grows well on sandy and shallow black soils and does not need much water, and Rajasthan is a major bajra-producing state (1).", "M", wp=True),
W("Describe the geographical conditions required for the growth of tea and name the major tea-producing states.", 3,
  "Tropical and sub-tropical climate with deep, fertile, well-drained soil rich in humus and organic matter (1). Warm, moist, frost-free climate with frequent showers evenly distributed through the year, and abundant cheap skilled labour (1). Assam, hills of Darjeeling and Jalpaiguri (West Bengal), Tamil Nadu and Kerala (1).", "M"),
W("Why is a well-developed network of transport and communication essential for plantations?", 2,
  "The produce is meant for the market and for processing industries, not for the family (1). Roads, railways and communication must connect the plantation areas, processing industries and markets so that the produce reaches them quickly (1).", "M"),
W("Map-based. On an outline map of India you are asked to shade the wheat-producing areas. Which regions and states will you shade, and why do they get ample wheat?", 3,
  "Shade the Ganga-Satluj plains in the north-west (Punjab, Haryana, Uttar Pradesh) and the Deccan black soil region (Madhya Pradesh), with Rajasthan and Bihar as other major states (2). These have cool winters, bright sunshine at ripening and irrigation (1).", "M"),
W("Locate on a map: (i) Nilgiri and Baba Budan Hills (ii) Garo Hills (iii) Nagpur. Say which crop is linked with each.", 3,
  "(i) Nilgiri region of Karnataka-Kerala-Tamil Nadu and Baba Budan Hills in Karnataka: Arabica coffee (1). (ii) Garo Hills in Meghalaya: rubber (1). (iii) Nagpur in Maharashtra: oranges (1).", "M"),
W("Explain two institutional reforms introduced after independence and why they were needed.", 3,
  "Collectivisation, consolidation of holdings, cooperation and abolition of zamindari were given priority (1). Land reform was the focus of the First Five Year Plan because the right of inheritance had fragmented holdings (1). Laws were made, but implementation was lacking or lukewarm (1).", "M"),
W("State two measures meant to protect farmers from exploitation by middlemen and speculators.", 2,
  "Minimum support price, remunerative prices and procurement prices for important crops (1). Crop insurance, KCC, PAIS and loans from Grameen banks and cooperative societies at lower interest also help (1).", "M"),
W("Error analysis. A student wrote: 'Kharif crops such as wheat, gram and mustard are sown in June-July.' Find and correct the mistake.", 2,
  "Wheat, gram and mustard are rabi crops, not kharif (1). Rabi crops are sown in winter (October-December); kharif crops such as paddy, maize, cotton and bajra are sown at the onset of monsoon in June-July (1).", "M"),
W("Why do cotton farmers prefer the black soil of the Deccan? Write three requirements of cotton.", 3,
  "India is believed to be the original home of the cotton plant and cotton grows well in the drier parts of the black cotton soil of the Deccan plateau (1). Cotton needs high temperature, light rainfall or irrigation, 210 frost-free days and bright sunshine (1); it is a kharif crop that takes six to eight months to mature (1).", "M"),
W("Sugarcane is a tropical as well as sub-tropical crop. State its temperature and rainfall needs, and name two products and two leading states.", 3,
  "Hot and humid climate with temperature 21 to 27 degrees C and annual rainfall of 75 to 100 cm; irrigation where rain is low (1). Products: sugar, gur (jaggery), khandsari, molasses (any two) (1). Leading states: Uttar Pradesh, Maharashtra, Karnataka, Tamil Nadu (any two); India is second to Brazil in output (1).", "M"),
W("Table-based. Crop / Season: Rice - Kharif (harvest Sept-Oct); Wheat - Rabi (sown Oct-Dec); Sugarcane - about 12 months; Groundnut - Kharif. A farmer has one field and wants two crops in the same year. Which two crops from the table can he combine, and why can sugarcane not be one of them?", 2,
  "Wheat after rice, or wheat after groundnut (1). Rice and groundnut are harvested by September-October, in time for wheat sowing in October-December; sugarcane takes almost a full year and blocks the field (1).", "M", wp=True),
# ------------------------------------------------------------------ HARD (13)
W("Assertion (A): The Green Revolution raised food production but widened regional disparities.  Reason (R): The package technology (HYV seeds, fertilisers, irrigation) was concentrated in a few selected areas.  State whether A and R are true and whether R explains A, with reasons.", 3,
  "Both are true (1) and R explains A (1). The Green Revolution of the 1960s-70s benefited Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan, where irrigation was available, while other regions were left behind (1).", "H"),
W("'Agriculture in India is a way of life, not only an economic activity.' Support this statement using farming systems and cropping seasons.", 4,
  "Cultivation methods have changed with physical environment, technology and socio-cultural practices; farming ranges from subsistence to commercial (1). Shifting cultivation has local names such as jhumming, Bewar, Podu and Kumari, which show that communities adapted the method to their areas (1). Rabi, kharif and zaid are linked with winter, monsoon and summer, so the family calendar follows them (1). Two-thirds of the people are engaged in farming, and tea, coffee and spices are also exported (1).", "H"),
W("Read the extract and answer. 'Suddenly Shri Ram Chandra Reddy stood up and offered 80 acres of land to be distributed among 80 landless villagers. This act was known as Bhoodan. ... Some zamindars offered to distribute some villages among the landless. It was known as Gramdan. However, many landowners chose to give some of their land due to the fear of the land ceiling act.'  (i) Where did this happen? (ii) Differentiate Bhoodan from Gramdan. (iii) Why did many landowners donate land? (iv) Why is the movement called the 'Blood-less Revolution'?", 4,
  "(i) At Pochampally (Telangana) when Vinoba Bhave was addressing villagers (1). (ii) Bhoodan: donation of land; Gramdan: zamindars offering whole villages (1). (iii) Fear of the land ceiling act (1). (iv) It redistributed land to the landless peacefully through persuasion, without violence (1).", "H"),
W("Compare rice and wheat on (i) season (ii) climate (iii) rainfall (iv) main growing regions.", 4,
  "Rice: kharif; high temperature above 25 degrees C and high humidity; annual rainfall above 100 cm (or irrigation); plains of north and north-east, coastal areas and deltas (West Bengal, Odisha, Andhra Pradesh; Punjab with irrigation) (2). Wheat: rabi; cool growing season and bright sunshine at ripening; 50-75 cm evenly distributed; Ganga-Satluj plains and the Deccan black soil (Punjab, Haryana, Uttar Pradesh, Madhya Pradesh) (2).", "H"),
W("Cause-effect. Canal irrigation and tubewells reached Punjab and Haryana. (i) What change did this bring in rice cultivation? (ii) How did the Green Revolution add to it? (iii) What problem for the environment can follow? Give a reason.", 4,
  "(i) Rice, a high-rainfall crop, could be grown in areas of low rainfall such as Punjab, Haryana, western Uttar Pradesh and parts of Rajasthan (1.5). (ii) HYV seeds, fertilisers and assured water raised wheat and rice yields, and paddy became an important crop of Punjab and Haryana (1.5). (iii) Heavy use of water and chemicals can lower the groundwater table and reduce soil fertility (1). (any reasoned answer)", "H"),
W("Why are Indian farmers often described as vulnerable despite higher production? Give four reasons.", 4,
  "Land holdings are small and fragmented after generations of inheritance (1). Many depend on the monsoon and natural fertility because irrigation is not available everywhere (1). Speculators and middlemen exploit farmers, so MSP and procurement prices were announced (1). Disasters (drought, flood, cyclone, fire, disease) can destroy crops, hence the need for crop insurance and low-interest credit (1).", "H"),
W("Case study. Meena lives in a village near Diphu in Assam. Her family clears a patch of forest, burns it, and sows food crops with a hoe. After a few seasons they move to a fresh patch. (i) Name the type of farming. (ii) Give its local names in the north-east. (iii) Give two disadvantages. (iv) Suggest one way to improve the family's farming.", 5,
  "(i) Primitive subsistence (slash and burn) farming (1). (ii) Jhumming in Assam, Meghalaya, Mizoram and Nagaland; Pamlou in Manipur; Dipa in Bastar and the Andaman and Nicobar Islands (1). (iii) Clearing and burning removes forest cover; productivity is low because there are no fertilisers or modern inputs, so the family barely has a surplus (2, any two reasoned points). (iv) Longer fallow, terracing, agro-forestry, or training and subsidised inputs through government schemes (1).", "H", wp=True),
W("Evaluate the statement: 'India needs both technological and institutional reforms in agriculture.' Give two examples of each and one limit of each.", 5,
  "Institutional: land reforms (consolidation of holdings, abolition of zamindari), cooperatives, Grameen banks, crop insurance (1.5). Technological: Green Revolution package (HYV seeds, fertiliser, irrigation), White Revolution (Operation Flood), weather bulletins on radio and TV (1.5). Limits: land reform laws were poorly implemented; Green Revolution led to concentration of development in a few areas, which is why a comprehensive land development programme combining institutional and technical reforms was started in the 1980s and 1990s (2).", "H"),
W("Explain with an example how the same crop may be commercial in one region and subsistence in another. What does this show about the 'degree of commercialisation'?", 3,
  "Rice is a commercial crop in Haryana and Punjab, where it is grown with modern inputs for the market, but a subsistence crop in Odisha, where it feeds the producing family (2). It shows that commercialisation varies from one region to another depending on inputs, market access and the farmer's aim (1).", "H"),
W("Passage-based. 'Pulses need less moisture and survive even in dry conditions. Being leguminous crops, all these crops except arhar help in restoring soil fertility by fixing nitrogen from the air.'  (i) Name two pulses and their seasons. (ii) Why would a farmer short of fertiliser money still gain by planting pulses before or after a cereal? (iii) Name two major pulse-producing states and India's world position.", 4,
  "(i) Tur (arhar), urad, moong are kharif; gram, masur and peas are rabi (1). (ii) Pulses add nitrogen to the soil, so the next cereal crop needs less chemical fertiliser and costs fall (1.5). (iii) Madhya Pradesh and Rajasthan (or Maharashtra, Uttar Pradesh, Karnataka); India is the largest producer and consumer of pulses in the world (1.5).", "H", wp=True),
W("A magazine states, 'Fruits and vegetables show the diversity of Indian climates.' Justify with five examples of crops and regions.", 4,
  "India produces tropical as well as temperate fruits (1). Examples (any five, 0.6 each): mangoes of Maharashtra, Andhra Pradesh, Telangana, Uttar Pradesh, West Bengal; oranges of Nagpur and Cherrapunjee; bananas of Kerala, Mizoram, Maharashtra, Tamil Nadu; litchi and guava of Uttar Pradesh and Bihar; pineapples of Meghalaya; grapes of Andhra Pradesh, Telangana, Maharashtra; apples, pears, apricots and walnuts of Jammu and Kashmir and Himachal Pradesh (3).", "H"),
W("Source-based. 'Though the right of inheritance, leading to the division of land among successive generations, has rendered land-holding size uneconomical, the farmers continue to take maximum output from the limited land in the absence of an alternative source of livelihood.'  (i) Which type of farming is described? (ii) Why is holding size uneconomical? (iii) Why do farmers still continue? (iv) Suggest one government measure that can help such farmers.", 4,
  "(i) Intensive subsistence farming (1). (ii) Each generation divides the land among heirs, so plots become smaller (1). (iii) They have no other source of livelihood, so they use more labour, biochemical inputs and irrigation on the limited land (1). (iv) Consolidation of holdings, cooperative farming, cheap credit or crop insurance (1).", "H"),
W("Why should a country with a large population and shrinking land shift towards sustainable and diversified farming? Give four points and name one crop group that suits dry regions.", 4,
  "Land is limited and fragmented and cannot be extended, so productivity has to rise without ruining the soil (1). Overuse of chemicals and water reduces fertility and groundwater (1). Diversification (pulses, millets, oilseeds, horticulture) reduces the risk of crop failure and improves nutrition and income (1). Organic methods lower input costs (0.5). Millets such as bajra and ragi need little water and suit dry regions (0.5).", "H"),
]

_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c09.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_core = _old["blocks"][:_i]
def _fix(x, a, b):
    if isinstance(x, str): return x.replace(a, b)
    if isinstance(x, (list, tuple)): return type(x)(_fix(y, a, b) for y in x)
    return x
for _a, _b2 in [
    (" The land ceiling act and other measures were not fully implemented because of the vested interests of political leaders.", " The laws of land reform were enacted but implementation was lacking or lukewarm."),
    ("and employs nearly half of India's workers; its share in GDP has fallen as other sectors have grown.", "and about two-thirds of India's population is engaged in agricultural activities (it provides livelihood for more than 60 per cent of the people)."),
    ("small and fragmented holdings, dependence on monsoon, lack of irrigation, soil degradation, falling groundwater, rising input costs, competition from imports and farmers' debt.", "small and fragmented holdings because of the right of inheritance, dependence of most farmers on the monsoon and natural fertility despite irrigation, and uneven benefits of the Green Revolution, which concentrated development in a few areas."),
    ("better irrigation, organic and sustainable farming, crop diversification, **millets and pulses**, food processing and fair prices.", "serious technical and institutional reforms: consolidation of holdings, cooperation, crop insurance, cheap credit, minimum support prices and information through radio, TV and the Farmers' Portal."),
    ("Punjab, Haryana, Himachal, Uttarakhand, Uttar Pradesh, Bihar, Rajasthan", "Punjab, Haryana, Himachal Pradesh, Jammu and Kashmir, Uttarakhand and Uttar Pradesh"),
]:
    _core = _fix(_core, _a, _b2)
_extra = [
 ("h2", "Crops at a Glance: Classification"),
 ("table", ["Group", "Crops", "Note"], [
  ["Cereals", "Rice, wheat, jowar, bajra, ragi, maize", "Rice and wheat are the two staple food crops; millets are coarse grains with high nutrition"],
  ["Pulses", "Tur (arhar), urad, moong, masur, peas, gram", "Leguminous (all except arhar restore soil fertility); India is the largest producer and consumer"],
  ["Oilseeds", "Groundnut, mustard, coconut, sesamum, soyabean, castor, cotton seed, linseed, sunflower", "Cover about 12 per cent of the cropped area; groundnut is about half of the major oilseeds"],
  ["Food crop other than grain", "Sugarcane", "Tropical and sub-tropical; 21-27 degrees C and 75-100 cm rain; needs about a year"],
  ["Beverage crops", "Tea, coffee", "Tea: plantation crop of Assam and North Bengal; coffee: Karnataka, Kerala, Tamil Nadu"],
  ["Horticulture", "Mango, orange, banana, litchi, guava, apple, grapes; peas, cauliflower, onion, tomato, potato", "India is the second largest producer of fruits and vegetables after China"],
  ["Fibre crops", "Cotton, jute, hemp, natural silk", "Silk is obtained from cocoons; rearing of silkworms is **sericulture**"],
  ["Industrial / non-food", "Rubber", "Equatorial; needs above 200 cm rain and above 25 degrees C"]]),
 ("h2", "India's Ranks in the World (NCERT)"),
 ("table", ["Crop", "Position of India", "Leader"], [
  ["Rice", "Second", "China"],
  ["Sugarcane", "Second", "Brazil"],
  ["Tea (2020)", "Second", "China"],
  ["Cotton", "Second", "China"],
  ["Groundnut (2020)", "Second", "China"],
  ["Fruits and vegetables (2020)", "Second", "China"],
  ["Pulses", "First (largest producer and consumer)", "-"]]),
 ("h2", "Timeline of Agricultural Reforms"),
 ("table", ["Period", "Step", "Result"], [
  ["After 1947", "Land reform, consolidation of holdings, abolition of zamindari, cooperation", "Main focus of the First Five Year Plan; weak implementation"],
  ["1951", "Bhoodan (Pochampally, Telangana) and Gramdan of Vinoba Bhave", "Voluntary land gifts to the landless; the 'Blood-less Revolution'"],
  ["1960s-1970s", "Green Revolution (package technology) and White Revolution (Operation Flood)", "Higher wheat, rice and milk output; development concentrated in a few areas"],
  ["1980s-1990s", "Comprehensive land development programme", "Combined institutional and technical reforms: crop insurance, Grameen banks, cooperatives, KCC, PAIS, weather bulletins, MSP"]]),
 ("h2", "Map Pointers"),
 ("ul", ["**Rice:** plains of north and north-east, coastal areas and deltas (West Bengal, Odisha, Andhra Pradesh, Telangana, Tamil Nadu, Kerala, the Konkan coast); Punjab and Haryana through irrigation.",
  "**Wheat:** the Ganga-Satluj plains (Punjab, Haryana, Uttar Pradesh) and the black soil of the Deccan (Madhya Pradesh), plus Rajasthan and Bihar.",
  "**Tea:** Assam, Darjeeling and Jalpaiguri hills, Tamil Nadu and Kerala; **coffee:** Baba Budan Hills and the Nilgiri region; **rubber:** Kerala, Tamil Nadu, Garo Hills.",
  "**Cotton:** Deccan black soil (Maharashtra, Gujarat, Madhya Pradesh, Karnataka); **jute:** flood plains of West Bengal, Bihar and Assam; **sugarcane:** Uttar Pradesh, Maharashtra, Karnataka, Tamil Nadu."]),
 ("h2", "Sources and Case Notes"),
 ("ul", ["**Case: Rinjha of Diphu (Assam).** Her family clears, slashes and burns a patch for cultivation and irrigates with a bamboo canal; unaware of declining fertility, they will shift next season. Use it for answers on shifting cultivation.",
  "**Case: Pochampally.** Landless villagers asked Vinoba Bhave for land; Ram Chandra Reddy offered 80 acres for 80 families; this started Bhoodan and later Gramdan, partly because landowners feared the land ceiling act.",
  "**Source: Farmers' Portal** (farmer.gov.in) gives information on crops, schemes and horticulture."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Right of inheritance and population pressure", "Land divided into small, uneconomical plots; intensive farming with heavy inputs"],
  ["Soil fertility falls in slash and burn farming", "Farmers shift to a fresh patch; low productivity and loss of forest"],
  ["Canals, tubewells and HYV seeds", "Rice and wheat grown even in low-rainfall Punjab, Haryana, western Uttar Pradesh"],
  ["Speculators and middlemen", "Government announces MSP, remunerative and procurement prices"],
  ["Pulses fix nitrogen", "Grown in rotation; soil fertility is restored"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "**Kharif** = monsoon sowing (June-July) and harvest in September-October. **Rabi** = winter sowing (October-December) and harvest in April-June. Do not interchange them, and do not call sugarcane a zaid crop: it takes almost a year."),
 ("note", "REMEMBER", "Tea, coffee and rubber are **plantation crops**, but cotton and jute are **fibre crops**; jute is the golden fibre, and silk comes from silkworm cocoons (sericulture). Maize is mainly kharif but is also grown in rabi in Bihar."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("Describe the geographical conditions required for the growth of rice. (3)", "Kharif crop; high temperature above 25 degrees C, high humidity and annual rainfall above 100 cm; irrigation where rain is less. Grown in the plains of north and north-east, coastal areas and deltas; canals and tubewells let it grow in Punjab, Haryana and western Uttar Pradesh."),
  ("What initiatives has the government taken to raise agricultural production? (5)", "Land reform, consolidation of holdings, abolition of zamindari; Green Revolution and White Revolution; crop insurance; Grameen banks and cooperative societies for cheap credit; Kisan Credit Card and PAIS; weather bulletins and farm programmes on radio and TV; minimum support, remunerative and procurement prices."),
  ("List the institutional reform programmes introduced for farmers. (3)", "Collectivisation, consolidation of holdings, cooperation, abolition of zamindari, crop insurance, Grameen banks and cooperative societies, KCC, PAIS and MSP."),
  ("Differentiate between kharif and rabi crops. (3)", "Kharif: sown with the onset of monsoon, harvested in September-October; paddy, maize, jowar, bajra, cotton, jute, groundnut. Rabi: sown in winter from October to December, harvested from April to June; wheat, barley, peas, gram, mustard, helped by western temperate cyclones."),
  ("What is meant by plantation agriculture? Give its features. (3)", "Single crop on a large area; capital-intensive; migrant labour; produce used as raw material in industries; needs transport and communication; tea, coffee, rubber, banana, sugarcane."),
 ]),
]
CH = dict(num=9, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_old["takeaways"] + ["India is second in the world in rice, sugarcane, tea, cotton, groundnut and fruits and vegetables, and first in pulses.", "**Bhoodan-Gramdan** (Vinoba Bhave, Pochampally) gave land to the landless without violence; the **Green Revolution** raised output but concentrated gains in a few regions."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
