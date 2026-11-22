"""Class 9 Social Science Ch 10 - Life on Earth (Geography, Part 2): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch10"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c10", str(REPO / "src/rn_work/c9_sst2/c10.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The largest tropical rainforest of the world is located in the:", 1, "(c) Amazon Basin", "E", opts=["Congo Basin", "Gobi region", "Amazon Basin", "Himalayan foothills"]),
W("Which biome is called a 'gene bank' because of its huge variety of species?", 1, "(a) Tropical rainforest", "E", opts=["Tropical rainforest", "Tundra", "Desert", "Temperate grassland"]),
W("Permafrost, soil frozen almost throughout the year, is a feature of the:", 1, "(d) tundra biome", "E", opts=["desert biome", "savanna biome", "tropical rainforest biome", "tundra biome"]),
W("The Rann of Kutch in Gujarat is an example of a:", 1, "(b) salt desert", "E", opts=["tropical rainforest", "salt desert", "coniferous forest", "coral reef"]),
W("The first village in India to gain rights over its forest under the Forest Rights Act was:", 1, "(a) Mendha Lekha", "E", opts=["Mendha Lekha", "Thenmala", "Channapatna", "Kandhamal"]),
W("India's first planned ecotourism destination, developed in Kollam (Keralam), is:", 1, "(c) Thenmala", "E", opts=["Sundarbans", "Mendha Lekha", "Thenmala", "Tezpur"]),
W("Tezpur Litchi, a GI-tagged product, comes from:", 1, "(b) Assam", "E", opts=["Odisha", "Assam", "Karnataka", "Meghalaya"]),
W("Aquatic biomes cover about what part of the Earth's surface?", 1, "(d) three-fourths", "E", opts=["one-tenth", "one-fourth", "half", "three-fourths"]),
W("Define a biome. Give one example of a terrestrial biome.", 2, "A biome is a large natural region where certain types of plants and animals live under similar climatic conditions (1). Example: tropical rainforest, grassland, desert or tundra (1).", "E"),
W("Name the four layers of a tropical rainforest from top to bottom.", 2, "Emergent layer, upper canopy, understory (lower canopy) and forest floor. (0.5 each)", "E"),
W("State True or False, with a reason: In a biome pyramid, energy increases as we go up from producers to top consumers.", 2, "False (1). Energy is lost as heat at each level, so energy, numbers and biomass decrease upwards (1).", "E"),
W("What are non-timber forest products? Give two examples.", 2, "Non-timber forest products are items other than timber that forests provide, which people collect for use and income (1). Examples: honey, fruits, nuts, resins, tendu leaves, mahua flowers, lac, medicinal plants (any two, 1).", "E"),
W("Fill in the blank: GI tag stands for ______ Indication tag.", 1, "Geographical (1)", "E"),
W("Name two terrestrial and two aquatic biomes.", 2, "Terrestrial: any two of forest, grassland, desert, tundra. Aquatic: freshwater and marine. (1+1)", "E"),
W("Which movement of Rajasthan inspired the Chipko Movement of Uttarakhand?", 1, "The Bishnoi Movement (Amrita Devi). (1)", "E"),
W("Name any two biodiversity hotspots of India mentioned in the chapter.", 2, "Any two: the Himalaya, the Western Ghats, North-East India, Andaman and Nicobar Islands. (1+1)", "E"),
W("What does FRA stand for? In which year was it passed?", 1, "Forest Rights Act (Scheduled Tribes and Other Traditional Forest Dwellers (Recognition of Forest Rights) Act), 2006. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Distinguish between a biome and an ecosystem with an example.", 3, "A biome is a large natural region with similar climate, plants and animals, such as the tundra or tropical rainforest (1.5). An ecosystem is like a neighbourhood within the biome where living and non-living things closely interact, such as a pond or a patch of forest (1.5).", "M"),
W("Why are tropical rainforests called a 'gene bank'? Give two other reasons why they are important.", 3, "They have a huge variety of plant and animal species and genes (1). They help maintain the oxygen supply and balance the climate (1), and give forest products and shelter to local people (1).", "M"),
W("Match the terms: (a) savanna (b) prairie (c) taiga (d) tundra with (1) temperate grassland of North America (2) tropical grassland of Africa (3) coniferous forest of cold sub-polar regions (4) coldest biome with mosses and lichens.", 3, "(a)-(2); (b)-(1); (c)-(3); (d)-(4). (3 for all, 2 for three)", "M"),
W("Arrange the following in a biome pyramid from base to top and explain why numbers and energy decrease upwards: carnivores, producers, herbivores, top consumers.", 3, "Producers (plants, algae) → herbivores (primary consumers) → carnivores (secondary consumers) → top consumers (2). Energy is lost as heat in metabolism at each level, so less is available upwards and fewer organisms can survive (1).", "M"),
W("The Sahara and the Gobi are both deserts. How are they different, and how do desert animals and plants survive?", 3, "The Sahara in Africa is a hot desert, while the Gobi in Asia is a cold desert (1.5). Plants like cacti and animals such as camels store water and withstand heat and scarce water; lizards and snakes are also adapted (1.5).", "M"),
W("Why is the tundra called a fragile ecosystem? Name two of its plants and two animals.", 3, "Even small changes in temperature can disturb it (1). Plants: mosses, lichens, shrubs; animals: reindeer, arctic fox, polar bear (any two each, 2).", "M"),
W("How is ecotourism different from mass tourism? Explain with the example of Thenmala.", 3, "Ecotourism is responsible travel to nature-friendly places with minimal environmental impact, respect for local communities and learning about ecosystems; mass tourism may harm the place (1.5). At Thenmala, the first planned ecotourism destination in Keralam, locals work as guides, eco-guards and service providers, so the community benefits and the forest is conserved (1.5).", "M"),
W("What are sacred groves? Why are they important for biodiversity and water?", 3, "Sacred groves are small forest patches protected by local communities for religious and cultural reasons (1). They preserve rare plants, medicinal species and wildlife that may not survive elsewhere (1) and some are linked to water sources, helping maintain streams and groundwater (1).", "M"),
W("Cause and effect. Explain how the Bishnoi Movement and Chipko Movement show the role of local people, especially women, in protecting forests.", 3, "In the Bishnoi Movement of Rajasthan, led by Amrita Devi, people stood up to protect trees (1). It inspired the Chipko Movement in Uttarakhand where village women hugged trees to stop deforestation (1). Both show that communities, and women in particular, can play a key role in forest management and eco-restoration (1).", "M"),
W("What is a GI tag? State any two benefits.", 3, "A Geographical Indication tag is an intellectual property right which identifies a product as originating from a specific place, whose quality or reputation is linked to that origin (1). Benefits: protects regional products, promotes cultural heritage, gives local people income through exclusive market recognition (any two, 2).", "M"),
W("Match each GI-tagged product with its state: (a) Tezpur Litchi (b) Erode Turmeric (c) Channapatna Toys (d) Kandhamal Haldi with (1) Karnataka (2) Odisha (3) Assam (4) Tamil Nadu.", 3, "(a)-(3); (b)-(4); (c)-(1); (d)-(2). (3 for all, 2 for three)", "M"),
W("State any three challenges faced by forest-dwelling communities.", 3, "Any three: poor healthcare, education and clean water; fuelwood fumes harming women's health; restrictions on forest use; floods, landslides and forest fires; crop damage by elephants, monkeys and wild boar; low prices for forest produce; lack of awareness of their rights. (1 each)", "M"),
W("What does the Forest Rights Act, 2006 provide to eligible forest communities? State two provisions.", 3, "It recognises the rights of eligible communities over forest land and resources (1). It allows collection of minor forest produce (1) and grants ownership of small patches of land cultivated by them (1).", "M"),
W("Find the mistake and correct it: 'Biodiversity means only the number of animal species in an area.'", 2, "Wrong (1). Biodiversity is the variety of all life: plants, animals, microorganisms, the genetic differences within species and the ecosystems and habitats they live in (1).", "M"),
W("Map pointers. Name two regions where tropical rainforests occur in the world, and two in India.", 3, "World: the Amazon Basin in South America, the Congo Basin in Africa, and parts of South-East Asia such as Indonesia (any two, 1.5). India: Andaman and Nicobar Islands, North-East India (1.5).", "M"),
W("What are ecological commons? Give two examples from the chapter.", 3, "Natural resources such as forests, rivers, lakes, grazing lands, air and biodiversity that a community shares and uses collectively, often under traditional rules (1.5). Examples: commons-based fisheries in Bihar and traditional water tanks (1.5).", "M"),
W("Explain how the Bihar Fish Jalkar Management Act, 2006 helped fishers.", 3, "Earlier large landowners controlled the water bodies and marginalised the fishers (1). The Act promotes community-led management of fisheries and public access to water bodies (1) and fish production has grown (1).", "M"),
W("Match the conservation strategy with the setting: (a) mangrove protection (b) afforestation (c) terrace farming (d) wildlife corridors with (1) hills (2) coasts (3) mountains with loss of forest (4) to link fragmented habitats.", 3, "(a)-(2); (b)-(3); (c)-(1); (d)-(4). (3 for all, 2 for three)", "M"),
W("Source-based. Mendha Lekha follows the slogan 'Mawa Nate Mawa Raj' (our village, our rule). (i) What does it mean? (ii) Name two ways its Gram Sabha manages the forest.", 3, "(i) The village community itself governs its resources, taking its own decisions (1). (ii) Any two: regulates tree cutting, prevents fires, promotes bamboo harvesting, uses revenue for education and infrastructure; it manages about 1,800 hectares (2).", "M"),
# ---------------- HARD ----------------
W("Case study. In a forest village the women cook on firewood, and the village has few clinics. Many children fall ill with cough. Some of the forest is also prone to fire. (i) Name the problems. (ii) Which scheme in the chapter helps with the fumes? (iii) Suggest two measures against forest fires and for health.", 4, "(i) Smoke from fuelwood harms health, poor healthcare, forest fires (1.5). (ii) PM Ujjwala Yojana (1). (iii) Any two: awareness, fire lines and community watch, JFM, health and skill programmes of the Government (1.5).", "H", wp=True),
W("Case study. Mendha Lekha, a Gond village in Gadchiroli, Maharashtra, got community forest rights. Explain how the Gram Sabha's decisions help the forest and the people, and why the case is a model.", 4, "It manages about 1,800 hectares by its own rules under 'Mawa Nate Mawa Raj' (1). It regulates tree cutting and prevents fires, protecting biodiversity (1), promotes bamboo harvesting, and uses revenue for education and infrastructure, supporting livelihoods (1). It shows that rights under the FRA and community self-governance can combine conservation with development (1).", "H", wp=True),
W("Case study. A village near a forest wants to start ecotourism. Prepare a short code of conduct with four points for visitors and four benefits for the village, based on the chapter.", 4, "Visitors (any four examples, 0.5 each): no littering or noise, stay on trails, do not disturb wildlife, respect local customs, avoid plastic, learn about the ecosystem. Benefits (0.5 each): jobs as guides, eco-guards and service providers, income for the community, conservation of the forest, learning for visitors and pride in local culture.", "H", wp=True),
W("Case study. In a grassland the numbers are: grass 10,000; grasshoppers 1,000; frogs 100; snakes 10; eagle 1. (i) Name the producers and top consumer. (ii) Which shape does the pyramid have? (iii) Give two reasons for the fall in numbers.", 4, "(i) Producers: grass; top consumer: eagle (1). (ii) A pyramid, broad at the base and narrow at the top (1). (iii) Energy is lost as heat at every level through metabolism (1) so a larger number of organisms is needed at the lower level to support those above (1).", "H", wp=True),
W("Explain with reasons how rivers, mountains and valleys act as barriers to animal movement, and how wildlife corridors and protected areas help.", 4, "Rivers, mountains and valleys can stop animals from moving, so populations become separated and habitats fragmented (1.5). Wildlife corridors link the habitats and allow gene flow (1.5). Protected areas such as national parks, sanctuaries and biosphere reserves prevent fragmentation and safeguard species (1).", "H"),
W("Compare the tropical rainforest and the tundra on location, climate, plants and animals, and human importance.", 4, "Rainforest: 23.5° N to 23.5° S, hot and wet all year, dense layered forest with a huge variety of species, gene bank and climate balance (2). Tundra: near the polar regions, coldest with long winters, mosses, lichens, shrubs, reindeer, arctic fox and polar bear, fragile with permafrost (2).", "H"),
W("HOTS. Some argue that forest dwellers should not be allowed to collect forest produce because it harms conservation. Give an argument against this, using the chapter, and suggest a balanced approach.", 4, "Forest dwellers depend on NTFPs for income and household needs and have traditional knowledge and protect forests through rituals, sacred groves and movements (2). The FRA recognises their rights, JFM involves them as partners (1). Balanced approach: sustainable collection, regulated cutting, community rules like those of Mendha Lekha (1).", "H"),
W("The Chandella and Bundela kings built about 8,000 water tanks in Bundelkhand (800-1200 CE). (i) Why are such tanks examples of ecological commons? (ii) Name two regional names for tanks. (iii) Why do they need protection today?", 4, "(i) They were shared by the whole community and managed collectively (1). (ii) Any two: keres (Karnataka), eri (Tamil Nadu), chevuru (Andhra Pradesh, Odisha), ahar pynes (Bihar), katas (Gond kings) (1). (iii) Population growth, industry and privatisation are shrinking the commons; community management is needed to keep the over 15 lakh functional tanks working (2).", "H"),
W("Case study. Kamla collects mahua flowers and honey from a forest in Rajasthan but gets very low prices from traders. Suggest three ways to improve her income, referring to the chapter.", 4, "Three, with reasons: give facilities for processing and marketing NTFPs to add value (1.5); obtain a GI tag for region-specific products, like the Ramban Sulai Honey or Kandhamal Haldi, for exclusive recognition (1.5); help her access government schemes and form a community group or use the rights under the FRA (1).", "H", wp=True),
W("A sacred grove with a spring is in the way of a road project. Using the chapter, argue why it should be protected and suggest an alternative.", 4, "Sacred groves protect rare plants, medicinal species and wildlife, and link to water sources, helping maintain streams and groundwater (2). Their cultural value protected by communities for generations (1). Alternative: realign the road around the grove or use a forest bridge to avoid harming wildlife (1).", "H", wp=True),
W("Why is it important to protect aquatic biomes? Explain with reference to freshwater and marine biomes.", 3, "They cover about three-fourths of the Earth's surface (1). Freshwater biomes (rivers, lakes, ponds, wetlands) supply drinking water, farming and fish, frogs and insects (1). Marine biomes (oceans, seas, coral reefs) store and distribute heat, influence climate, host whales, dolphins, fish and plankton and give food and jobs to millions (1).", "H"),
W("Explain how living beings and biomes depend on each other. Give three examples of interdependence between living things, and one of human impact.", 3, "Animals pollinate plants and disperse seeds (1); microorganisms recycle nutrients (1); plants give food and oxygen to animals (0.5). Humans modify landscapes for farming and cities, which can change biomes (0.5).", "H"),
W("Essay. 'Humans and forests are interconnected.' Discuss with reference to livelihoods, culture, ecotourism, challenges and government support.", 5, "Forests give food, fuel, fodder, medicine, shelter and NTFPs (1). Culture: rituals of Gonds and Bhils, sacred groves, Bishnoi and Chipko (1). Ecotourism such as Thenmala gives jobs while conserving (1). Challenges: poor services, restrictions, fires, wildlife attacks, low prices (1). Support: FRA 2006, JFM, PESA, PM JANMAN, schemes and the Mendha Lekha model (1).", "H"),
W("Describe the lessons that the Bishnoi Movement, Chipko and Mendha Lekha offer us for conserving forests today.", 3, "Bishnoi and Chipko show that local people, especially women, can lead the protection of trees (1). Mendha Lekha shows that when communities have legal rights and manage forests collectively, they conserve and also earn (1). Together they stress community participation, traditional values and rights-based forest governance (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "10.6 Timeline and Key Figures"),
 ("table", ["Date / figure", "What it refers to"], [
  ["800-1200 CE", "Chandella and Bundela kings build about 8,000 tanks in Bundelkhand"],
  ["Bishnoi, then Chipko", "Bishnoi Movement (Rajasthan, Amrita Devi) inspires Chipko (Uttarakhand); women hug trees"],
  ["2006", "Forest Rights Act; Bihar Fish Jalkar Management Act"],
  ["Over 1,00,000", "Sacred groves in India"],
  ["about 1,800 hectares", "Forest managed by the Gram Sabha of Mendha Lekha"],
  ["Over 15 lakh", "Functional traditional water tanks in India today"],
  ["about three-fourths", "Share of the Earth's surface covered by aquatic biomes"]]),
 ("h2", "10.7 Key Terms and Places"),
 ("table", ["Term / place", "Meaning"], [
  ["**Biome**", "Large natural region with similar climate, plants and animals"],
  ["**Ecosystem**", "A community of living and non-living things interacting closely within a biome"],
  ["**Biodiversity**", "Variety of life: species, genes and ecosystems"],
  ["**Hotspot**", "Region rich in unique species, e.g. Western Ghats"],
  ["**Permafrost**", "Permanently frozen soil of the tundra"],
  ["**NTFP**", "Non-timber forest product, e.g. honey, lac, tendu leaves"],
  ["**Sacred grove**", "Forest patch protected for religious reasons"],
  ["**Ecotourism**", "Responsible nature tourism with minimal impact that benefits locals"],
  ["**GI tag**", "Intellectual property right linking a product to its place of origin"],
  ["**FRA, JFM, PESA, PM JANMAN**", "Forest Rights Act; Joint Forest Management; Panchayats (Extension to Scheduled Areas); scheme for Particularly Vulnerable Tribal Groups"],
  ["**Ecological commons**", "Shared natural resources used collectively by a community"],
  ["**Rann of Kutch, Sahara, Gobi, Amazon, Congo**", "Salt desert (Gujarat), hot desert (Africa), cold desert (Asia), the largest rainforest basins"]]),
 ("h2", "10.8 Map Pointers"),
 ("ul", ["On a world map mark the **Amazon Basin**, **Congo Basin** and **Indonesia / South-East Asia** (rainforest), the **Sahara** and the **Gobi** (deserts), and the polar belts (tundra).",
  "On the map of India locate the **Himalaya, Western Ghats, North-East India, Andaman and Nicobar Islands** (hotspots), the **Rann of Kutch** and **Gadchiroli district (Maharashtra)** for Mendha Lekha, and **Thenmala (Kollam, Keralam)**.",
  "Mark GI products on a map of India: Tezpur (Assam), Kandhamal (Odisha), Erode (Tamil Nadu), Channapatna (Karnataka), Ramban (Jammu and Kashmir), Khasi Mandarin (Meghalaya), Tripura Queen Pineapple (Tripura), Nilgiri Tea (Tamil Nadu, Keralam, Karnataka)."]),
 ("h2", "10.9 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Temperature, rainfall, dominant vegetation", "Different biomes across the world"],
  ["Energy lost as heat in metabolism", "Pyramid narrows upwards"],
  ["Rivers, mountains, valleys fragment habitats", "Need for corridors and protected areas"],
  ["Forest produce sold at low prices; no processing", "Poverty; need for GI tags, processing and marketing"],
  ["Rights over forest recognised (FRA)", "Communities such as Mendha Lekha manage and conserve forests"],
  ["Population growth, industry, privatisation", "Commons such as tanks and fisheries shrink"]]),
 ("h2", "10.10 Comparison of Land Biomes"),
 ("table", ["Biome", "Climate", "Typical life", "Importance"], [
  ["Tropical rainforest", "Hot and wet", "Dense layered forest; huge variety of species", "Gene bank; oxygen and climate balance"],
  ["Savanna (tropical grassland)", "Warm with moderate rain", "Grass, few trees; lions, elephants, giraffes", "Wildlife and grazing"],
  ["Temperate grassland (prairies, steppes)", "Moderate rainfall", "Grass; grazing animals", "Fertile soil for farming"],
  ["Desert", "Very dry; hot or cold", "Cacti, camels, lizards, snakes", "Minerals, oil, salt"],
  ["Taiga", "Cold, sub-polar", "Pines, spruces, larches", "Timber, boreal forest"],
  ["Tundra", "Coldest, long winters", "Mosses, lichens, reindeer, polar bear", "Fragile; permafrost"]]),
 ("h2", "10.11 More Likely Questions"),
 ("qa", [
  ("How do physiography and climate shape life on Earth? (5 marks)", "Temperature, precipitation and the dominant vegetation decide the biome: hot and wet near the equator gives rainforests; moderate rain gives grasslands; very little rain gives deserts; the cold near the poles gives tundra. Mountains, rivers and valleys act as barriers or corridors, and landforms and water shape habitats."),
  ("Why should we conserve biodiversity? (3 marks)", "All living things are interdependent: plants give food and oxygen, animals pollinate and spread seeds, microorganisms recycle nutrients. Loss of species disturbs ecosystems and humans depend on them for food, medicine, livelihood and culture."),
  ("What are the ways in which the government supports forest communities? (3 marks)", "The Forest Rights Act 2006 recognises their rights; Joint Forest Management, PESA, PM JANMAN, PM Ujjwala Yojana and programmes for scholarships, healthcare and skills help them."),
  ("How do GI tags help forest communities? (3 marks)", "A GI tag gives exclusive recognition and a better price to region-specific products such as Ramban Sulai Honey or Kandhamal Haldi, preserves heritage and gives income to local producers."),
 ]),
]
CH["takeaways"] += ["Know the biomes by climate: **hot-wet (rainforest), moderate (grassland, deciduous), dry (desert), cold (taiga, tundra)**.",
  "Community case studies to cite: **Bishnoi and Chipko, Mendha Lekha, Thenmala, Bihar fisheries, Bundelkhand tanks**; law: **FRA 2006**."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
