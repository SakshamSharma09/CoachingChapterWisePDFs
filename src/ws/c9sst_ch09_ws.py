"""Class 9 Social Science Ch 9 - Oceans and Life (Geography, Part 2): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch09"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c09", str(REPO / "src/rn_work/c9_sst2/c09.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("The deepest place on Earth is located in the:", 1, "(b) Mariana Trench, in the Pacific Ocean", "E", opts=["Mid-Ocean Ridge", "Mariana Trench, in the Pacific Ocean", "Abyssal plain", "Continental slope"]),
W("Spring tides occur on:", 1, "(c) full moon and new moon days", "E", opts=["first-quarter Moon days only", "third-quarter Moon days only", "full moon and new moon days", "days without any Sun or Moon influence"]),
W("The territorial waters of a coastal country extend up to:", 1, "(a) 12 nautical miles", "E", opts=["12 nautical miles", "24 nautical miles", "200 nautical miles", "64 nautical miles"]),
W("The warm current that keeps the coastal waters of Norway relatively ice-free is the:", 1, "(d) Gulf Stream", "E", opts=["Labrador Current", "Antarctic Current", "Mid-Ocean Current", "Gulf Stream"]),
W("One nautical mile is equal to:", 1, "(b) 1,852 metres", "E", opts=["1,000 metres", "1,852 metres", "1,609 metres", "2,000 metres"]),
W("The instruments on the sea floor that confirm the passage of tsunami waves are called:", 1, "(c) Ocean Bottom Pressure Recorders", "E", opts=["tide gauges", "seismic stations", "Ocean Bottom Pressure Recorders", "weather balloons"]),
W("Because of the Coriolis force, moving ocean water in the Northern Hemisphere is deflected to the:", 1, "(a) right", "E", opts=["right", "left", "north", "south"]),
W("A flat-topped underwater volcanic mountain is called a:", 1, "(d) guyot", "E", opts=["trench", "abyssal hill", "continental rise", "guyot"]),
W("Define a wave. What mainly causes ordinary ocean waves?", 2, "A wave is the alternate rise and fall of the ocean surface (1). Waves are mainly caused by winds (1).", "E"),
W("Name the four maritime zones as you move from the coast towards the open sea.", 2, "Territorial waters, contiguous zone, Exclusive Economic Zone (EEZ) and the high seas. (0.5 each)", "E"),
W("State True or False, with a reason: The Exclusive Economic Zone gives a country complete ownership of the sea up to 200 nautical miles.", 2, "False (1). It gives special rights over fish, oil, gas and other resources, but not full ownership; other ships may pass peacefully (1).", "E"),
W("What is a tsunami? What usually causes it?", 2, "A tsunami is a series of giant sea waves (1) caused mainly by underwater earthquakes (1).", "E"),
W("Fill in the blank: The Gulf of ______ has one of the highest tidal ranges in India, about 12 metres.", 1, "Khambhat (1)", "E"),
W("Expand ITEWC and say what it does.", 2, "Indian Tsunami Early Warning Centre (1). It runs a real-time network of detection buoys and sensors and sends alerts to the Government (1).", "E"),
W("Name the landforms formed in sequence on a headland by wave erosion.", 2, "Crack, cave, arch, stack and finally a stump. (2)", "E"),
W("What is meant by 'run-up height' of a tsunami?", 1, "The maximum vertical height above sea level reached by the tsunami waves on reaching the coast. (1)", "E"),
W("What does UNCLOS stand for?", 1, "United Nations Convention on the Law of the Sea. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Why is the continental shelf economically important to a coastal country? Give three reasons.", 3, "It is shallow, so sunlight reaches and it is rich in fish; it is the main fishing zone (1). It holds oil and natural gas (1). Being shallow and near the coast, its resources are easier to reach and use (1).", "M"),
W("Two crests of a wave are 8 m apart and the vertical distance from trough to crest is 1.5 m. Name and give the value of (i) wavelength and (ii) wave height.", 3, "(i) Wavelength is the horizontal distance between two consecutive crests = 8 m (1.5). (ii) Wave height is the vertical distance between trough and crest = 1.5 m (1.5).", "M", wp=True),
W("Explain how a sea stack is formed from a headland.", 3, "Waves attack the headland by hydraulic action and abrasion, widening cracks into caves (1). Caves cut through the headland to form an arch (1). When the roof of the arch collapses, a standing rock, the sea stack, is left (1).", "M"),
W("Differentiate between spring tides and neap tides on the basis of the position of the Sun and Moon, the day, and the tidal range.", 3, "Spring tides: Sun, Earth and Moon in a straight line, on full-moon and new-moon days, with very high high tides and very low low tides (large range). Neap tides: Sun and Moon pull in different directions at the first- and third-quarter Moon, with a smaller difference between high and low tide. (1 each for position, day, range)", "M"),
W("A very large crude carrier has to pass a shallow channel such as the Singapore Strait. How do tides help it, and why must the captain check both depth and tidal range?", 3, "The ship waits for high tide, when the water is deeper, to pass safely (1.5). The captain checks depth and tidal range to know how much water will be under the ship at each time, so that it does not run aground (1.5).", "M", wp=True),
W("Why do regions where warm and cold currents meet become good fishing grounds?", 3, "Mixing of warm and cold water brings nutrients to the surface (1.5), which feed plankton and so support large populations of fish; hence these are major fishing grounds (1.5).", "M"),
W("Compare the Gulf Stream and the Labrador Current on origin, temperature and effect.", 3, "Gulf Stream: warm, flows from the Gulf of Mexico, keeps Norway's coastal waters relatively ice-free at 60-70 degrees N (1.5). Labrador Current: cold, off the east coast of Canada, carries freezing water, so sea ice and icebergs form even at lower latitudes (1.5).", "M"),
W("Match the stage of a tsunami early warning system with the tool used: (a) detection (b) confirmation (c) tracking (d) warning, with (1) tide gauges and radars (2) satellite, SMS and other channels (3) seismic stations (4) ocean bottom pressure recorders.", 3, "(a)-(3); (b)-(4); (c)-(1); (d)-(2). (3 for all four, 2 for three)", "M"),
W("Why was the island of Simeulue largely spared in the 26 December 2004 tsunami? What lesson does this give?", 3, "Local folklore taught people to recognise the warning signs of the sea and move to safety (1.5). Traditional knowledge and public awareness can save lives even without modern technology (1.5).", "M"),
W("Timeline. Arrange in order: (i) Cyclone Remal (ii) Cyclone Biparjoy (iii) the Indian Ocean tsunami that killed about 2,30,000 people. Give the years.", 3, "(iii) 26 December 2004; (ii) Biparjoy, 2023; (i) Remal, 2024. (3 for correct order with years, 2 for order only)", "M"),
W("A country's territorial waters extend 12 nautical miles and its EEZ 200 nautical miles from the baseline. Taking 1 nautical mile = 1.852 km, convert both distances to kilometres.", 3, "Territorial waters: 12 × 1.852 = 22.224 km (1.5). EEZ: 200 × 1.852 = 370.4 km (1.5).", "M", wp=True),
W("Match the zone with the rights of the coastal country: (a) territorial waters (b) contiguous zone (c) EEZ (d) high seas, with (1) global commons with equal rights of navigation and fishing (2) near-complete control with innocent passage for foreign ships (3) special rights over fish, oil and gas (4) limited control over customs, immigration and pollution.", 3, "(a)-(2); (b)-(4); (c)-(3); (d)-(1). (3 for all four, 2 for three)", "M"),
W("What is 'innocent passage'? Would a foreign vessel stopping to fish in territorial waters be covered by it?", 2, "Innocent passage is the right of foreign ships to pass continuously and peacefully through territorial waters without threatening the peace or security of the coastal state (1). Fishing is not allowed, so a vessel stopping to fish would not be covered (1).", "M"),
W("Classify as living or non-living marine resources: fish, oil, coral reefs, sand and gravel, aquatic vegetation, offshore wind, natural gas, gas hydrates.", 3, "Living: fish, coral reefs, aquatic vegetation (1.5). Non-living: oil, sand and gravel, offshore wind, natural gas, gas hydrates (1.5).", "M"),
W("Define the 'Blue Economy'. Which Sustainable Development Goal is linked to it?", 3, "The Blue Economy is the sustainable use of ocean resources for economic growth, better livelihoods and jobs while keeping the marine ecosystem healthy (2). It is linked to SDG 14, Life Below Water (1).", "M"),
W("Find the mistake and correct it: 'The high seas belong to the country with the strongest navy.'", 2, "Wrong (1). The high seas lie beyond all EEZs (about 64 per cent of the oceans) and belong to no one: they are global commons with equal rights of navigation, fishing and overflight for all countries (1).", "M"),
W("The Bhadkeshwar Mahadev Temple near Dwarka can be reached only at certain times of the day. Explain why.", 2, "It can be reached on foot only at low tide, when the sea level falls and the path is uncovered (1), while at high tide the water rises and covers it (1).", "M"),
W("Map pointers. Describe the location of the Gulf of Kutch, the Gulf of Khambhat and the Sundarbans on India's coastline and say why they are noted in the chapter.", 3, "The Gulf of Kutch and the Gulf of Khambhat lie on the west coast of India in Gujarat, and the Sundarbans lie on the east coast at the delta in West Bengal (2). They are sites identified as suitable for tidal energy, the Gulf of Khambhat having a tidal range of about 12 m (1).", "M"),
W("Source-based. 'GEMINI is a GAGAN-enabled handheld device for fishermen that sends alerts through Bluetooth to a mobile app in nine languages.' (i) Who is it meant for? (ii) Why is the language feature important?", 3, "(i) Fishermen at sea (1). (ii) Fishermen speak many regional languages, so alerts in nine languages let them understand warnings quickly and act on them (2).", "M"),
# ---------------- HARD ----------------
W("Case study. The tidal range at a port is 4-5 m. At low tide the water in the channel is 9 m deep. A cargo ship has a draught (depth below the water line) of 12 m and needs at least 0.5 m of clearance. Assuming a tidal range of 4 m, can it enter at low tide or at high tide? Explain.", 4, "Low tide depth 9 m is less than the 12 m draught, so it cannot enter (1.5). High tide depth = 9 + 4 = 13 m; the ship needs 12.5 m, so it can enter with 0.5 m to spare (2). Hence the captain must time arrival with the tide (0.5).", "H", wp=True),
W("Case study. Rajesh, a fisherman from Veraval in Gujarat, is given a GEMINI device. Describe three ways in which it can protect his life and livelihood, and mention the scheme that supports it.", 4, "It gives cyclone and sea-state alerts on a phone app by Bluetooth even in the sea (1); alerts in a language he understands (1); its range lets him know of danger before it reaches his boat so he can return to shore, saving lives and boats and reducing losses (1). It is supported under the PMMSY (1).", "H", wp=True),
W("Explain how the Coriolis force and winds together affect ocean currents. In which direction is the water deflected in each hemisphere?", 4, "Winds push surface water and set currents in motion (1). The Coriolis force, caused by Earth's rotation, deflects moving water to the right in the Northern Hemisphere (1.5) and to the left in the Southern Hemisphere (1.5). Temperature, salinity and the shape of continents further guide the currents.", "H"),
W("Case study. A coastal village in Odisha is asked to prepare for cyclones and tsunamis. Using the chapter, list four measures covering technology, public awareness and infrastructure.", 4, "Any four, 1 each: receive alerts from ITEWC / INCOIS / IMD by SMS; sirens and radio announcements; cyclone shelters and Decision Support System under NCRMP; evacuation drills; teach warning signs from folklore and traditional knowledge, as at Simeulue; cyclone-ready boats and devices such as GEMINI.", "H", wp=True),
W("Compare the Exclusive Economic Zone and the high seas on extent, rights of the coastal country, and who may use them.", 4, "EEZ: up to 200 nautical miles from the baseline (1); the coastal country has special rights over fish, oil and gas under UNCLOS but not ownership, while others may pass peacefully (1.5). High seas: beyond all EEZs, about 64 per cent of the oceans (1); global commons, belong to no country, with equal rights of navigation, fishing, overflight and laying cables for all, and the laws of the flag state apply on ships (1.5).", "H"),
W("Three ships are at 8, 20 and 150 nautical miles from the baseline of a country. Name the zone in which each is located and state one right of the coastal state in each case.", 4, "8 NM: territorial waters; near-complete control and the right to allow only innocent passage (1.5). 20 NM: contiguous zone; limited control for customs, immigration and pollution (1.5). 150 NM: EEZ; special rights over fish, oil and gas (1).", "H", wp=True),
W("Case study. A village in a coastal state wants to start fish farming, a small tourism business and a solar-powered ice plant while protecting its reef. Suggest how it can follow the Blue Economy and SDG 14, with four points.", 4, "Four points, 1 each: use fishing and farming methods that do not exhaust fish stocks (regulated fishing); keep the reef and mangroves protected; control plastic and waste pollution; use renewable energy; give jobs to the local people; protect marine areas; use sustainable tourism.", "H", wp=True),
W("HOTS. Why was the loss of life in the 2004 tsunami so large in some regions but low in others, even though the same waves struck? Give three reasons from the chapter.", 3, "Most deaths occurred in Indonesia, where people near the coast had little time (1). Where early warning, timely evacuation or awareness existed, as at Simeulue where folklore taught people to recognise the signs, lives were saved (1). It shows that warning systems, public education and preparedness decide the loss of life (1).", "H"),
W("A photograph shows a headland with a sea cave and, a little further, a sea arch. (i) Which processes made them? (ii) Predict, with reasons, what will form next and finally.", 3, "(i) Hydraulic action and abrasion widen cracks into caves, and caves cut through to arches (1). (ii) With time the roof of the arch will collapse, leaving a sea stack (1), which waves will wear down to a stump (1).", "H"),
W("Explain how the alignment of the Sun, Earth and Moon creates spring tides and neap tides. Which would be more useful for generating tidal energy and why?", 4, "When the three are in a straight line, on full and new moon days, their gravitational pulls add up and give spring tides with very high and very low waters (1.5). At the quarter moons the Sun and Moon pull in different directions, giving smaller range neap tides (1.5). Spring tides give the larger range and stronger flow, which gives more energy for tidal power (1).", "H"),
W("Oceans carry about 90 per cent of global trade by volume. Explain why international rules such as UNCLOS, COLREGs and MARPOL are necessary for safe and sustainable shipping.", 4, "With so much traffic, ships from many countries share the same waters, so common rules prevent disputes, accidents and piracy (1). UNCLOS defines maritime zones and rights and helps settle disputes (1). COLREGs are the rules of the road at sea, like lookout, safe speed and give-way duties, to prevent collisions (1). MARPOL prevents pollution of the sea by ships, protecting marine life (1).", "H"),
W("Describe the cultural importance of the ocean in Indian tradition, mentioning Samudra, the conch and the cowrie.", 3, "In Indian culture the ocean, Samudra, is considered powerful and sacred and appears in stories and rituals (1). The conch (shankha) and the cowrie (kapardika), once used as currency, are linked to the Samudra Manthana, and show that the ocean's products were valued in culture and trade (2).", "H"),
W("Essay. 'Oceans shape life on Earth.' Discuss with reference to ocean relief, waves, tides and currents, marine resources and the need for early warning and rules.", 5, "Ocean relief (shelf, slope, ridges, trenches) gives fishing grounds, oil, gas and a hidden landscape (1). Waves shape coasts; tides help navigation, fishing and energy; currents such as the Gulf Stream moderate climate and create fishing grounds (2). Marine resources, living and non-living, support food, energy, trade and jobs under the Blue Economy and SDG 14 (1). Early warning systems and rules like UNCLOS protect people and the seas (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "9.9 Timeline and Numbers to Remember"),
 ("table", ["Date / figure", "What it is"], [
  ["26 December 2004", "Indian Ocean tsunami; about 2,30,000 deaths; Simeulue largely spared by folklore"],
  ["2023", "Cyclone Biparjoy (name from the North Indian Ocean list)"],
  ["2024", "Cyclone Remal"],
  ["169 names, 13 countries", "List used to name cyclones in the North Indian Ocean"],
  ["12 / 24 / 200 nautical miles", "Territorial waters / contiguous zone / EEZ"],
  ["about 64 per cent", "Share of the world's oceans that are high seas"],
  ["about 90 per cent", "Share of global trade by volume carried by sea"],
  ["1,852 m", "One nautical mile"],
  ["11,098.81 km", "Length of India's coastline"],
  ["about 12 m", "Tidal range in the Gulf of Khambhat"],
  ["5-6 knots (9-11 km/h)", "Speed of tidal currents"]]),
 ("h2", "9.10 Key Terms and Key Places"),
 ("table", ["Term / place", "Meaning or significance"], [
  ["**Submarine relief**", "Landforms of the ocean floor"],
  ["**Seamount / guyot**", "Underwater volcanic mountain / flat-topped seamount"],
  ["**Hydraulic action, abrasion**", "Wave processes that erode the coast"],
  ["**Run-up height**", "Maximum height reached by a tsunami on the coast"],
  ["**Tidal range**", "Difference between high-tide and low-tide levels"],
  ["**Coriolis force**", "Deflection due to Earth's rotation: right in the north, left in the south"],
  ["**Baseline**", "The line from which maritime zones are measured"],
  ["**Flag state**", "The country whose flag a ship flies; its laws apply on the ship on the high seas"],
  ["**Mariana Trench**", "Deepest place on Earth (Pacific Ocean)"],
  ["**Mid-Ocean Ridge**", "Longest mountain range, underwater"],
  ["**Gulf of Khambhat, Gulf of Kutch, Sundarbans**", "Sites suited to tidal energy"],
  ["**Singapore Strait**", "Shallow channel where large crude carriers wait for high tide"]]),
 ("h2", "9.11 Map and Diagram Pointers"),
 ("ul", ["On a world map locate the **Pacific Ocean (Mariana Trench)**, the **Gulf Stream** (warm, from the Gulf of Mexico towards north-western Europe, Norway) and the **Labrador Current** (cold, off eastern Canada).",
  "On a map of India locate the **Gulf of Kutch** and **Gulf of Khambhat** (west coast, Gujarat), and the **Sundarbans** (east coast, West Bengal).",
  "Draw and label the cross-section of submarine relief: continent → shelf → slope → rise → abyssal plain, with the mid-ocean ridge, rift valley, trench, seamount and submarine canyon.",
  "Draw a wave and label crest, trough, wavelength and wave height."]),
 ("h2", "9.12 Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Wind blowing over water", "Waves"],
  ["Underwater earthquake", "Tsunami with large run-up height"],
  ["Gravitational pull of Moon and Sun", "Tides; spring tides when aligned, neap at quarter moons"],
  ["Earth's rotation, winds, temperature and salinity differences", "Ocean currents deflected by the Coriolis force"],
  ["Warm Gulf Stream towards Norway", "Ice-free coastal waters at 60-70 degrees N"],
  ["Meeting of warm and cold currents", "Nutrient-rich water; major fishing grounds"],
  ["Seismic detection, OBPRs, tide gauges, alerts", "Timely evacuation and fewer deaths"],
  ["UNCLOS maritime zones", "Clear rights and fewer disputes over resources"]]),
 ("h2", "9.13 Worked Examples"),
 ("steps", [
  ("Example 1 — Nautical miles to kilometres", "EEZ = 200 nautical miles. 200 × 1.852 = 370.4 km. Territorial waters = 12 × 1.852 = 22.224 km."),
  ("Example 2 — Which zone?", "A ship is 30 nautical miles from the baseline. It is beyond 24 NM (contiguous zone) and within 200 NM, so it is in the EEZ; the coastal state has rights over fish, oil and gas, but the ship may pass peacefully."),
  ("Example 3 — Can the ship enter?", "Channel depth at low tide 9 m; tidal range 4 m; ship needs 12.5 m. At high tide depth = 9 + 4 = 13 m, so the ship can enter only at high tide.")]),
 ("h2", "9.14 Comparison Tables"),
 ("table", ["Feature", "Waves", "Tides", "Currents"], [
  ["Cause", "Wind", "Gravitational pull of Moon and Sun", "Wind, Coriolis force, temperature, salinity, shape of ocean basins"],
  ["Nature", "Alternate rise and fall of surface; carry energy", "Regular rise and fall twice a day", "Continuous streams flowing in definite directions"],
  ["Importance", "Shape coasts (caves, arches, stacks, beaches)", "Navigation, fishing, tidal energy", "Climate, fishing grounds, travel"]]),
 ("table", ["Zone", "Distance", "Control", "Example of use"], [
  ["Territorial waters", "12 NM", "Almost full; innocent passage", "Coastal patrol, ports"],
  ["Contiguous zone", "24 NM", "Limited: customs, immigration, pollution", "Checking smuggling"],
  ["EEZ", "200 NM", "Special rights over resources", "Fishing, offshore oil and gas"],
  ["High seas", "Beyond EEZ", "None; shared", "Free navigation, fishing, cables"]]),
 ("h2", "9.15 More Likely Questions"),
 ("qa", [
  ("Explain the importance of ocean relief. (3 marks)", "The continental shelf is a rich fishing zone with oil and gas; seamounts support marine life; the mid-ocean ridge shows where new crust forms; trenches are the deepest parts; the ocean floor is a hidden landscape, as varied as land."),
  ("How does ocean water movement affect life and the environment? (5 marks)", "Waves shape coasts by erosion and deposition; tides help ships enter ports, improve fishing and can give tidal energy; currents such as the Gulf Stream moderate the climate and meeting warm and cold currents form fishing grounds; tsunamis and cyclones can cause disasters, so early warning is vital."),
  ("Why are maritime zones important for a country? (3 marks)", "They define which part of the sea a country controls and where it has rights over resources; this avoids disputes, protects security, customs and the environment, and keeps the high seas open for all."),
  ("How can ocean resources be used sustainably? (3 marks)", "By following the Blue Economy and SDG 14: regulating fishing, reducing pollution, protecting marine ecosystems and conserving marine areas while using resources for jobs and growth."),
  ("How do early warning systems protect people? (3 marks)", "Seismic stations detect earthquakes, OBPRs confirm waves, tide gauges and radars track them and alerts reach officials and the public by satellite and SMS, giving time to evacuate. Public awareness and traditional knowledge add to this."),
 ]),
]
CH["takeaways"] += ["Numbers: **12 / 24 / 200** nautical miles; **1 NM = 1,852 m**; high seas about **64 per cent** of the oceans; about **90 per cent** of trade by sea.",
  "Tsunami warning in order: **detect (seismic), confirm (OBPR), track (tide gauges, radars), warn (satellite, SMS)**; 26 December 2004 is the key date."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
