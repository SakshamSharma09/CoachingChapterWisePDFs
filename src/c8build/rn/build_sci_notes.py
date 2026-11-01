import html
from playwright.sync_api import sync_playwright
CSS = """
@page{size:A4;margin:12mm 13mm 14mm 13mm}
*{box-sizing:border-box}
body{font-family:Arial,Helvetica,sans-serif;color:#1d1d1f;font-size:10.3pt;line-height:1.42;margin:0}
h1.cover{color:#13286b;font-size:26pt;margin:0 0 4px}
.sub{color:#c49a3c;letter-spacing:2px;font-weight:bold;font-size:10pt}
.ch{page-break-before:always}
.chtag{color:#c49a3c;font-weight:bold;letter-spacing:2px;font-size:9pt;margin-top:6px}
h2{color:#13286b;font-size:19pt;margin:2px 0 4px;border-bottom:2px solid #13286b;padding-bottom:3px}
h3{color:#13286b;font-size:12pt;margin:12px 0 4px}
h4{color:#13286b;font-size:10.5pt;margin:8px 0 2px}
p{margin:4px 0}
ul{margin:3px 0 4px 18px;padding:0}
li{margin:2px 0}
table{border-collapse:collapse;width:100%;margin:6px 0;font-size:9.6pt}
th{background:#13286b;color:#fff;text-align:left;padding:4px 6px}
td{border:1px solid #c9d2e6;padding:4px 6px;vertical-align:top}
tr:nth-child(even) td{background:#f4f7fc}
.def{background:#eaf1fb;border-left:4px solid #13286b;padding:6px 9px;margin:7px 0}
.def b.t{color:#13286b;letter-spacing:.5px;font-size:9pt}
.key{background:#fff7e0;border:1px solid #c49a3c;border-radius:5px;padding:7px 11px;margin:10px 0}
.key h5{margin:0 0 3px;color:#13286b;font-size:10.5pt}
.probe{background:#f2f5fb;border:1px solid #c9d2e6;padding:6px 9px;font-style:italic;margin:6px 0}
.foot{color:#7a85a3;font-size:8pt;text-align:center;margin-top:10px;border-top:1px solid #c9d2e6;padding-top:3px}
.lead{font-size:10.4pt;color:#33415f}
"""
def tbl(head, rows):
    return "<table><tr>"+"".join(f"<th>{h}</th>" for h in head)+"</tr>"+"".join("<tr>"+"".join(f"<td>{c}</td>" for c in r)+"</tr>" for r in rows)+"</table>"
def ul(items): return "<ul>"+"".join(f"<li>{i}</li>" for i in items)+"</ul>"
def dfn(t, x): return f"<div class='def'><b class='t'>{t}</b><br>{x}</div>"
def key(items): return "<div class='key'><h5>★ KEY TAKEAWAYS</h5>"+ul(items)+"</div>"
def chap(n, title, lead, body): 
    return f"<div class='ch'><div class='chtag'>CHAPTER {n:02d}</div><h2>{title}</h2><div class='chtag' style='font-weight:normal;color:#555;letter-spacing:0'>Grade 8 · Science</div><p class='lead'>{lead}</p>{body}<div class='foot'>The Mastermind Coaching Classes · Road No. 5, VKIA, Jaipur · 9887258679 · Grade 8 Science · Part 2</div></div>"
CH = []
# ---------- Chapter 8
CH.append(chap(8, "Nature of Matter: Elements, Compounds and Mixtures",
 "This chapter classifies matter around us. Matter is either a mixture (components keep their properties) or a pure substance (elements and compounds). Minerals link the chapter to the Earth.",
 "<div class='probe'>Probe &amp; Ponder: Is air a pure substance? Why does water behave differently from hydrogen and oxygen?</div>"
 "<h3>8.1 What Are Mixtures?</h3>"
 + dfn("DEFINITION", "A <b>mixture</b> is formed when two or more substances are mixed and <b>each substance retains its properties</b>. The substances in a mixture are its <b>components</b>. The components do not react chemically and are not in a fixed ratio.")
 + ul(["<b>Air is a mixture</b> of nitrogen, oxygen, argon, carbon dioxide and other gases.", "A mixture can be separated by <b>physical methods</b> (magnet, filtration, evaporation, sieving).", "Composition is <b>variable</b>: sugar solution can be sweeter or weaker."])
 + "<h4>Types of mixtures</h4>"
 + tbl(["Basis", "Type", "Examples"], [["Distribution", "Uniform (homogeneous) – same composition throughout", "Sea water, sugar solution, air, brass"], ["Distribution", "Non-uniform (heterogeneous) – components visible or settle", "Muddy water, sand and iron filings, soil"], ["State of components", "Solid–solid", "Baking powder (baking soda + tartaric acid), alloys"], ["State of components", "Solid–liquid / liquid–liquid / gas–gas", "Salt in water / alcohol in water / air"]])
 + dfn("ALLOYS", "Solid mixtures of a metal with other metals or non-metals. <b>Brass</b> = copper + zinc; <b>bronze</b> = copper + tin; <b>stainless steel</b> is stronger and more durable than pure iron. Our scientific heritage: <b>Mishraloha</b> was the name for a mixture of two or more metals with properties distinct from its metals; <b>Kamsya</b> (bronze) = Tamra (copper) 4 parts + Vanga (tin) 1 part.")
 + "<h3>8.2 What Are Pure Substances?</h3>"
 + ul(["A <b>pure substance</b> consists of the same type of particles; all its particles behave identically.", "Examples: sugar, baking soda, distilled water, oxygen, gold.", "Milk, packed fruit juice, soil and sea water are <b>mixtures</b>, not pure substances."])
 + "<h3>8.3 Types of Pure Substances</h3>"
 + tbl(["", "Element", "Compound"], [["Meaning", "Simplest substance that cannot be broken down further", "Two or more elements combined chemically in a <b>fixed ratio</b>"], ["Properties", "Own properties", "Different from the constituent elements"], ["Separation", "Cannot be broken down by chemical reactions", "Can be broken into elements only by chemical methods (e.g. electrolysis)"], ["Examples", "Hydrogen, oxygen, iron, sulfur, gold, aluminium", "Water, carbon dioxide, sodium chloride (Na : Cl = 1 : 1), glucose, rust"]])
 + ul(["<b>Water</b> splits into hydrogen and oxygen on passing electricity – so water is a compound, hydrogen and oxygen are elements.", "<b>Metalloids</b> (silicon, boron) have properties between metals and non-metals."])
 + "<h4>Activity: iron filings and sulfur</h4>"
 + tbl(["Sample", "Observation", "Conclusion"], [["A – mixture (no heating)", "Magnet pulls out iron; sulfur remains", "Mixture – components keep properties"], ["B – heated strongly", "Black mass <b>iron sulfide</b>; magnet has no effect", "New compound with new properties"]])
 + "<p><b>Word equations:</b> Iron + Sulfur → Iron sulfide. &nbsp; Iron sulfide + dilute hydrochloric acid → Iron chloride + Hydrogen sulfide gas. &nbsp; Iron + dilute hydrochloric acid → Iron chloride + Hydrogen. &nbsp; Magnesium + Oxygen → Magnesium oxide.</p>"
 + "<h3>8.5 What Are Minerals?</h3>"
 + ul(["<b>Minerals</b> are natural, solid substances found on the Earth with a fixed chemical composition.", "Most are compounds; rarely pure elements – called <b>native minerals</b> (e.g. gold).", "Most rocks are mixtures of minerals."])
 + key(["Mixture: components retain properties, variable composition, separated physically.", "Pure substance = element or compound.", "Element cannot be broken down; compound has elements combined chemically in fixed ratio with new properties.", "Alloys are mixtures (brass, bronze, steel).", "Minerals: natural solids with fixed composition; native minerals are elements."])))
# ---------- Chapter 9
CH.append(chap(9, "The Amazing World of Solutes, Solvents and Solutions",
 "Everyday liquids such as sea water, soft drinks and syrups are solutions. This chapter studies how substances dissolve, how much can dissolve, and how density explains floating and sinking.",
 "<h3>9.1 Solute, Solvent and Solution</h3>"
 + dfn("DEFINITIONS", "<b>Solution</b>: a uniform mixture of two or more substances. <b>Solute</b>: the substance that dissolves (smaller amount in liquid–liquid solutions). <b>Solvent</b>: the substance in which the solute dissolves (larger amount). A solid dissolved in a liquid: solid = solute, liquid = solvent.")
 + tbl(["Type", "Example"], [["Solid in liquid", "Salt or sugar in water"], ["Liquid in liquid", "Alcohol or vinegar in water"], ["Gas in liquid", "Carbon dioxide in soda water; oxygen in water"], ["Solid in solid", "Brass (zinc in copper)"]])
 + "<h3>9.2 Saturated and Unsaturated Solutions</h3>"
 + tbl(["Term", "Meaning"], [["Unsaturated solution", "More solute can still dissolve at that temperature"], ["Saturated solution", "Maximum solute dissolved; extra solute settles at the bottom"], ["Solubility", "Maximum amount of solute that dissolves in a fixed quantity (100 mL) of solvent at a particular temperature"]])
 + "<h4>Effect of temperature</h4>"
 + ul(["Solubility of most <b>solids</b> in liquids <b>increases</b> with temperature (more sugar dissolves in warm water).", "Solubility of <b>gases</b> in liquids <b>decreases</b> with temperature – warm soda loses fizz; warm water holds less oxygen for fish.", "A saturated solution on cooling lets excess solute separate as crystals.", "Stirring speeds up dissolving but does not change solubility."])
 + "<h3>9.3 Mass, Volume and Density</h3>"
 + tbl(["Quantity", "Meaning", "Instrument / unit"], [["Mass", "Amount of matter in an object", "Weighing balance; kg, g"], ["Volume", "Space occupied by an object or substance", "Measuring cylinder; mL, cm³, m³"], ["Density", "Mass per unit volume", "Density = Mass ÷ Volume; kg/m³ or g/cm³"]])
 + ul(["Read the volume at the bottom of the <b>meniscus</b> (curved liquid surface) with eye at the same level.", "Water has density about <b>1 g/cm³</b> (1000 kg/m³).", "<b>Example:</b> mass 200 g, volume 50 cm³ → density = 200 ÷ 50 = 4 g/cm³."])
 + dfn("FLOATING AND SINKING", "An object floats if its density is <b>less</b> than that of the liquid; it sinks if its density is <b>more</b>. A raw egg sinks in tap water but floats in salt water because salt water is denser.")
 + "<h4>Effect of temperature and pressure on density</h4>"
 + ul(["Density generally <b>decreases</b> with a rise in temperature (substances expand).", "Pressure strongly affects the density of <b>gases</b>; little effect on solids and liquids."])
 + dfn("WHY ICE FLOATS", "On freezing, water particles arrange themselves so that they take up <b>more space</b> (expansion), reducing density. Ice floats and forms an insulating layer, keeping water below warm enough for aquatic life in cold weather.")
 + key(["Solution = uniform mixture; solute dissolves in solvent.", "Saturated: no more solute dissolves; unsaturated: more can dissolve.", "Solubility of solids rises, of gases falls, with temperature.", "Density = mass ÷ volume; water ≈ 1 g/cm³.", "Float if density < liquid’s density; ice floats because it is less dense than water."])))
# ---------- Chapter 10
CH.append(chap(10, "Light: Mirrors and Lenses",
 "Light helps us see. This chapter studies reflection from plane and curved mirrors, the laws of reflection, and refraction through lenses.",
 "<h3>10.1 Reflection and the Laws of Reflection</h3>"
 + dfn("LAWS OF REFLECTION", "(1) The <b>angle of incidence equals the angle of reflection</b>. (2) The incident ray, the <b>normal</b> to the mirror at the point of incidence and the reflected ray all lie in the <b>same plane</b>. These laws hold for plane, concave and convex mirrors.")
 + ul(["Angles are measured from the <b>normal</b> (perpendicular to the surface).", "A ray along the normal has angle of incidence 0° and reflects back along the same path.", "<b>Example:</b> i = 40° → r = 40°; angle between ray and mirror = 90° − 40° = 50°; angle between incident and reflected ray = 80°.", "Smooth surfaces give <b>regular</b> reflection; rough surfaces give <b>diffuse</b> reflection. We see the Moon because it reflects sunlight."])
 + "<h3>10.2 Spherical Mirrors and Images</h3>"
 + tbl(["", "Plane mirror", "Concave mirror", "Convex mirror"], [["Surface", "Flat", "Curves inward", "Bulges outward"], ["Effect on light", "Reflects", "<b>Converges</b> light", "<b>Diverges</b> light"], ["Image", "Erect, same size, virtual", "Enlarged, diminished or same size; erect or inverted, depending on object distance", "<b>Always erect and diminished</b>"], ["Uses", "Dressing mirror", "Dentist and ENT mirrors, shaving mirror, solar cookers", "Rear-view mirrors, shop security (wide field of view)"]])
 + ul(["<b>Lateral inversion</b> (left appears right) occurs in all three types of mirrors.", "Concave mirror: when the object is <b>close</b>, the image is erect and magnified; when far, the image is inverted."])
 + "<h3>10.4 Lenses and Refraction</h3>"
 + dfn("REFRACTION", "The bending of light when it passes from one transparent medium to another (e.g. air to water). A pencil in a glass of water appears bent because of refraction.")
 + tbl(["", "Convex lens", "Concave lens"], [["Shape", "Thicker at centre", "Thinner at centre"], ["Effect on light", "<b>Converges</b>", "<b>Diverges</b>"], ["Image", "Enlarged, diminished or same size; erect or inverted, by object distance", "<b>Always erect and diminished</b>"], ["Uses", "Magnifying glass, cameras, microscopes, spectacles for long-sightedness", "Spectacles for short-sightedness"]])
 + key(["Angle of incidence = angle of reflection; all rays and normal lie in one plane.", "Concave mirror converges; convex mirror diverges and always gives erect diminished image.", "Convex lens converges; concave lens diverges and always gives erect diminished image.", "Refraction is bending of light between media.", "Convex mirrors for traffic, concave mirrors for dentists and solar cookers."])))
# ---------- Chapter 11
CH.append(chap(11, "Keeping Time with the Skies",
 "People kept time by watching the Sun, the Moon and the stars. This chapter explains the phases of the Moon, the logic of lunar, solar and luni-solar calendars, and introduces artificial satellites.",
 "<h3>11.1 Phases of the Moon</h3>"
 + ul(["The Moon reflects sunlight; half of it is always lit. As it orbits the Earth we see different portions of the lit half – the <b>phases</b>.", "The <b>shape of the Moon itself does not change</b>; only the part visible to us changes.", "A full cycle of phases takes about <b>29.5 days</b> (nearly a month): new moon → waxing crescent → full moon → waning → new moon.", "The Moon rises about 50 minutes later each day."])
 + "<h3>11.2 Calendars</h3>"
 + tbl(["Cycle", "Defined by", "Length"], [["Day", "Earth’s rotation", "About 24 hours"], ["Month", "Moon’s revolution – cycle of phases", "About 29.5 days"], ["Year", "Earth’s revolution round the Sun – seasons", "About 365¼ days"]])
 + tbl(["Calendar", "Based on", "Features"], [["Lunar", "Moon’s phases", "Month ≈ 29.5 days; lunar year = 12 months = 354 days – about 11 days shorter than the solar year; festivals such as Eid-ul-fitr shift through the seasons"], ["Solar", "Seasons (Earth’s revolution)", "Gregorian calendar; 365 days; <b>leap year</b> adds 29 February in years divisible by 4"], ["Luni-solar", "Moon’s phases and seasons", "An extra month (<b>Adhika Maasa</b>) is added every few years to match the seasons"]])
 + ul(["Century years are leap years only if divisible by 400 (1700, 1800, 1900 not; 1600, 2000 are).", "<b>Tropical year</b>: time between successive spring equinoxes (basis of the Gregorian calendar). <b>Sidereal year</b>: same stars rise again at sunset; longer by about 20 minutes.", "On <b>equinoxes</b> the Sun rises exactly in the east; on <b>solstices</b> (about 21 June and 21 December) it reaches extreme positions. The Surya Siddhanta records star patterns (e.g. Makar) at the winter solstice.", "Festivals such as Makar Sankranti, Pongal, Bihu, Vaisakhi follow a <b>solar sidereal calendar</b> and fall on almost the same Gregorian date each year."])
 + dfn("INDIAN NATIONAL CALENDAR", "Adopted from 21 March 1956 (1 Chaitra 1878 Saka). Year begins on <b>22 March</b> (the day after the spring equinox; 21 March in leap years) with Chaitra; months have 30 or 31 days; follows the Surya Siddhanta principles.")
 + "<h3>11.3 Artificial Satellites</h3>"
 + ul(["Human-made objects launched from Earth; give information for well-being and space science (weather, mapping, communication, astronomy).", "Indian examples: Cartosat, AstroSat, AzaadiSat, InspireSat-1, Jugnu.", "<b>Space debris</b>: old satellites and rocket parts that crowd space and may collide with working satellites.", "<b>Vikram Sarabhai</b> (1919–1971): Father of the Indian Space programme; VSSC, Thiruvananthapuram, is named after him."])
 + key(["Phases arise from the changing view of the Moon’s lit half; cycle ≈ 29.5 days.", "Lunar year 354 days vs solar year ≈ 365¼ days; Adhika Maasa fixes the gap.", "Leap year rule: divisible by 4, century years need 400.", "Indian National Calendar starts 22 March (Chaitra).", "Satellites help weather, mapping and communication; debris is a threat."])))
# ---------- Chapter 12
CH.append(chap(12, "How Nature Works in Harmony",
 "Living things depend on each other and on non-living surroundings. This chapter studies habitats, ecosystems, food chains, relationships between organisms, benefits of ecosystems and their conservation.",
 "<h3>12.1 Habitat and Ecosystem</h3>"
 + dfn("DEFINITIONS", "<b>Habitat</b>: a place that provides the right conditions for an organism to live and grow. <b>Ecosystem</b>: the interaction of <b>biotic</b> (plants, animals, microbes) and <b>abiotic</b> (air, water, soil, sunlight, temperature) components of an area. Ecosystems are <b>terrestrial</b> (forest, grassland, desert) or <b>aquatic</b> (pond, lake, sea).")
 + "<h3>12.2 Who Eats Whom?</h3>"
 + tbl(["Group", "Role", "Examples"], [["Producers", "Make their own food using sunlight", "Green plants, algae"], ["Consumers", "Eat plants or animals – herbivores, carnivores, omnivores", "Deer, tiger, humans"], ["Decomposers (saprotrophs)", "Break down dead matter and recycle nutrients", "Bacteria, fungi (mushrooms)"]])
 + ul(["<b>Food chain</b>: who eats whom, e.g. millet → mouse → snake → eagle; arrows point from eaten to eater.", "<b>Food web</b>: interconnected food chains.", "<b>Trophic levels</b>: positions in a food chain – producers (level 1), primary consumers, secondary consumers, tertiary consumers. Number of organisms and energy decrease at higher levels (a pyramid)."])
 + "<h3>12.3 Relationships between organisms</h3>"
 + tbl(["Relationship", "Effect", "Example"], [["Mutualism", "Both benefit", "Bee and flower (nectar and pollination)"], ["Commensalism", "One benefits, other unaffected", "Orchid growing on a tree branch"], ["Parasitism", "One benefits, other is harmed", "Tapeworm in the human gut"]])
 + "<h3>12.4 Benefits of Ecosystems</h3>"
 + ul(["<b>Ecosystem services</b>: clean air and water, food, medicine, climate regulation, soil fertility, pollination.", "<b>Human-made ecosystems</b>: farms, fish ponds, gardens.", "Healthy ecosystems help farms through pollinators, natural pest control and decomposer-made nutrients. <b>Monoculture</b> and excess pesticides reduce biodiversity and create resistant pests.", "<b>Vrikshayurveda</b> advocates continual nourishment of soil with organic manure such as <b>Kunapa Jala</b> (a fermented liquid fertiliser from animal and plant waste)."])
 + "<h3>12.5 Threats and Conservation</h3>"
 + ul(["Threats: pollution, deforestation, habitat loss, climate change, invasive species, overexploitation.", "<b>Sundarbans</b>: world’s largest mangrove forest at the Ganga–Brahmaputra delta; slows winds and waves in storms; UNESCO World Heritage Site (1987); threatened by pollution and rising seas.", "Protection: national parks (e.g. Bandipur, Manas), wildlife sanctuaries, biosphere reserves (Nilgiri), community conserved areas, marine national parks."])
 + key(["Ecosystem = biotic + abiotic components interacting.", "Producers, consumers, decomposers; food chains form food webs; trophic levels.", "Mutualism (both gain), commensalism (one gains), parasitism (one harmed).", "Ecosystem services support human life; monoculture and pesticides harm it.", "Conserve through protected areas and sustainable practices."])))
# ---------- Chapter 13
CH.append(chap(13, "Our Home Earth, a Unique Life-Sustaining Planet",
 "Of billions of planets, Earth is special: it is the only known one that supports life. This chapter explains the conditions that make Earth habitable, how its spheres interact, how life continues through reproduction, and the threats it faces.",
 "<h3>13.1 What Makes Earth Suitable for Life?</h3>"
 + tbl(["Factor", "Why it matters"], [["Position", "Earth is in the <b>habitable (Goldilocks) zone</b> where water stays liquid; neither too hot nor too cold"], ["Nearly circular orbit", "Temperature does not vary too extremely through the year"], ["Size and gravity", "Strong enough to hold the atmosphere, not so strong as to crush creatures"], ["Ozone layer", "A three-atom form of oxygen that absorbs harmful <b>ultraviolet</b> rays"], ["Magnetic field", "Shields Earth from high-energy particles from space"], ["Greenhouse effect", "Atmospheric gases trap some heat and keep Earth warm (Venus is hotter than Mercury because of a strong greenhouse effect)"]])
 + "<h3>13.2 What Sustains Life?</h3>"
 + tbl(["Sphere", "Made of", "Role"], [["Atmosphere", "Air", "Oxygen, ozone shield, climate"], ["Hydrosphere", "Water", "Drinking water, habitats, water cycle"], ["Geosphere", "Solid Earth – soil, rocks, minerals", "Nutrients and materials"], ["Biosphere", "Life", "Plants, animals, microbes keep cycles going"]])
 + ul(["The four spheres <b>interact</b> and together sustain life; balance in oxygen level, temperature and ozone is delicate."])
 + "<h3>13.3 Reproduction – What Keeps Life from Disappearing?</h3>"
 + tbl(["", "Asexual reproduction", "Sexual reproduction"], [["Parents", "One", "Two (male and female)"], ["Offspring", "Exact copies of the parent", "New features appear (variation)"], ["Examples", "Parts of plants (stem, leaf) growing into new plants – sugarcane, rose; regeneration in small animals", "Flowering plants; fish, frogs, birds, mammals"]])
 + ul(["<b>Plants:</b> pollination (pollen to stigma by wind, insects, birds) → fertilisation (male and female gametes fuse) → <b>zygote</b> → seed; fruits help in <b>seed dispersal</b>.", "<b>Animals:</b> fish and frogs – fertilisation and embryo development in water; birds – fertilised egg (zygote) is laid, embryo develops after laying; most mammals – development inside the female’s body."])
 + "<h3>13.4 Threats – the Triple Planetary Crisis</h3>"
 + ul(["<b>Climate change</b> (burning fossil fuels releases carbon dioxide and methane), <b>pollution</b> and <b>biodiversity loss</b>.", "Solutions: clean energy, saving energy and water, reuse–repair–recycle, protecting biodiversity, sustainable use of resources by local communities, awareness."])
 + key(["Earth’s distance, orbit, gravity, ozone and magnetic field make it habitable.", "Atmosphere, hydrosphere, geosphere and biosphere interact to sustain life.", "Reproduction: asexual – one parent, identical; sexual – two parents, variation.", "Fertilisation forms the zygote; seeds form in plants.", "Triple planetary crisis: climate change, pollution, biodiversity loss."])))
cover = ("<div style='text-align:center;margin-top:60px'><div class='sub'>THE MASTERMIND COACHING CLASSES</div><h1 class='cover' style='margin-top:30px'>Mastermind Revision Notes</h1>"
 "<div class='sub'>GRADE 8 · SCIENCE</div><p class='lead' style='margin-top:20px'>Fast, high-retention revision notes built on the NCERT Grade 8 Science textbook <i>Curiosity</i>.</p>"
 "<h2 style='border:none;margin-top:20px'>PART 2 — CHAPTERS 8 to 13</h2></div>"
 "<div class='def' style='margin-top:30px'><b class='t'>HOW TO USE THESE NOTES</b><br>This Part 2 continues the supplied Part 1 (Chapters 1–7) in the same format. Each chapter follows the textbook’s section order. Bold words are keywords; tables compare and classify; blue boxes hold definitions; the gold Key Takeaways box is your last-two-minutes revision.</div>"
 + tbl(["Ch.", "Chapter", "Core theme"], [["8", "Nature of Matter: Elements, Compounds and Mixtures", "Classification of matter"], ["9", "Solutes, Solvents and Solutions", "Solubility and density"], ["10", "Light: Mirrors and Lenses", "Reflection and refraction"], ["11", "Keeping Time with the Skies", "Moon, calendars, satellites"], ["12", "How Nature Works in Harmony", "Ecosystems"], ["13", "Our Home Earth", "Habitability, reproduction, threats"]])
 + "<div class='foot'>The Mastermind Coaching Classes · Road No. 5, VKIA, Jaipur · 9887258679</div>")
doc = f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{cover}{''.join(CH)}</body></html>"
open("/tmp/sci_notes_p2.html","w").write(doc)
with sync_playwright() as p:
    b = p.chromium.launch(executable_path="/opt/pw-browsers/chromium" if False else None)
    pg = b.new_page(); pg.goto("file:///tmp/sci_notes_p2.html")
    import os
    os.makedirs("/home/claude/out8/Revision_Notes", exist_ok=True)
    pg.pdf(path="/home/claude/out8/Revision_Notes/Class8_Science_Revision_Notes_Part2_Ch08-13.pdf", format="A4", print_background=True, display_header_footer=True,
      header_template="<span></span>", footer_template="<div style='width:100%;font-family:Arial;font-size:7px;text-align:right;margin:0 13mm;color:#13286b'>Mastermind Revision Notes — Grade 8 Science (Part 2) · Page <span class='pageNumber'></span> of <span class='totalPages'></span></div>",
      margin=dict(top="12mm", bottom="14mm", left="13mm", right="13mm"))
    b.close()
