from fractions import Fraction as F
from lib import mcq, Q, OR
from mk9 import M4, build
def fm(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f"{float(x):.2f}".rstrip("0").rstrip(".")
A = []
# energy received (insolation 1 kW/m2) (4)
for a, h in [(1, 1), (2, 3), (5, 2), (10, 4)]:
    e = a * h
    ws = [x for x in dict.fromkeys([e * 2, a + h, e + 3, F(e, 2) if e > 1 else e + 7, e * 10]) if F(x) != e][:3]
    A.append(M4(f"If the insolation is 1 kW m⁻², the solar energy received by {a} m² in {h} h is:", f"{fm(e)} kWh", [f"{fm(x)} kWh" for x in ws], "energy = power × area × time"))
# solar constant energy per second (2)
for a in [2, 5]:
    e = 1400 * a
    A.append(M4(f"The solar constant is about 1400 J s⁻¹ m⁻². The energy arriving on {a} m² (perpendicular to the Sun's rays) in 1 s is:", f"{e} J", [f"{x} J" for x in (e // 2, e * 2, e + 1000)], "1400 × area"))
# speed of light: time (2)
for t, d in [(1, 3), (2, 6)]:
    A.append(M4(f"Light travels at 3 × 10⁸ m s⁻¹. In {t} s it travels:", f"{d} × 10⁸ m", [f"{x} × 10⁸ m" for x in (d * 2, d + 1, F(d, 2) if d > 2 else 9)], "distance = speed × time"))
# wavelength to nm (2)
for l in [100, 400]:
    A.append(M4(f"A wavelength of {l} nm in metres is:", f"{l} × 10⁻⁹ m", [f"{l} × 10⁻⁶ m", f"{l} × 10⁻³ m", f"{l} × 10⁻¹² m"], "1 nm = 10⁻⁹ m"))
A += [
 M4("The four spheres of the Earth are geosphere, hydrosphere, atmosphere and:", "biosphere", ["lithosphere", "cryosphere only", "stratosphere"], "life"),
 M4("The part of the Earth system made of ice and snow is the:", "cryosphere", ["hydrosphere", "atmosphere", "geosphere"], "glaciers and polar ice"),
 M4("The main source of energy for the Earth is:", "solar radiation", ["geothermal energy", "tidal energy", "fossil fuels"], "the Sun"),
 M4("Electromagnetic waves:", "can travel through vacuum", ["need a medium", "are longitudinal only", "are slower than sound"], "unlike sound waves"),
 M4("The speed of light in vacuum is:", "3 × 10⁸ m s⁻¹", ["3 × 10⁶ m s⁻¹", "340 m s⁻¹", "3 × 10¹⁰ m s⁻¹"], "c"),
 M4("The ozone layer absorbs mainly:", "ultraviolet radiation", ["infrared radiation", "visible light", "radio waves"], "stratosphere"),
 M4("Radiation that warms the Earth's surface and is re-radiated is mainly:", "infrared", ["gamma", "X-rays", "radio"], "heat"),
 M4("The amount of solar radiation reaching the Earth's surface is called:", "insolation", ["solar constant", "albedo", "transpiration"], "incoming solar radiation"),
 M4("The solar constant is approximately:", "1.4 kW m⁻²", ["14 kW m⁻²", "0.14 kW m⁻²", "140 kW m⁻²"], "at the top of the atmosphere"),
 M4("The maximum insolation at the surface under a clear sky is about:", "1 kW m⁻²", ["1.4 kW m⁻²", "10 kW m⁻²", "0.1 kW m⁻²"], "less than the solar constant"),
 M4("The polar regions are colder than the equator mainly because:", "the Sun's rays are spread over a larger area", ["they are closer to the Sun", "they have more oceans", "they have no atmosphere"], "slanting rays"),
 M4("Which gas is the most abundant in the Earth's atmosphere?", "nitrogen", ["oxygen", "carbon dioxide", "argon"], "78%"),
 M4("The layer of the atmosphere where weather occurs is the:", "troposphere", ["stratosphere", "mesosphere", "exosphere"], "lowest layer"),
 M4("The ozone layer is present in the:", "stratosphere", ["troposphere", "thermosphere", "mesosphere"], "12–50 km"),
 M4("Greenhouse gases include:", "carbon dioxide, methane and water vapour", ["nitrogen and oxygen", "argon and helium", "neon and hydrogen"], "trap heat"),
 M4("The greenhouse effect:", "keeps the Earth warm enough for life", ["makes the Earth colder", "is entirely harmful", "occurs only in greenhouses"], "natural but enhanced by humans"),
 M4("Global warming is caused mainly by an increase in:", "greenhouse gases", ["nitrogen", "oxygen", "ozone in the stratosphere"], "fossil fuels, deforestation"),
 M4("Chemicals that caused the ozone hole are:", "CFCs", ["CO₂", "methane", "nitrogen oxides only"], "refrigerators, aerosols"),
 M4("The agreement that reduced the use of CFCs is the:", "Montreal Protocol", ["Kyoto Protocol", "Paris Agreement", "Rio Declaration"], "ozone recovery"),
 M4("Winds are caused by:", "uneven heating of the Earth's surface", ["rotation of the Moon", "tides only", "volcanic eruptions"], "pressure differences"),
 M4("Air moves from:", "high pressure to low pressure", ["low pressure to high pressure", "cold to cold", "sea to sea"], "wind"),
 M4("Surface ocean currents are driven mainly by:", "winds", ["volcanoes", "ice melting", "gravity of the Sun only"], "friction with the water"),
 M4("The surface that reflects most solar radiation is:", "fresh snow", ["forest", "dark soil", "ocean"], "high albedo"),
 M4("Albedo is the:", "fraction of incoming solar radiation reflected by a surface", ["energy absorbed by plants", "temperature of the air", "pressure of the atmosphere"], "reflectivity"),
 M4("The cycling of nutrients between living and non-living parts is the:", "biogeochemical cycle", ["rock cycle only", "food chain", "life cycle"], "matter cycles"),
 M4("Water enters the atmosphere from plants through:", "transpiration", ["infiltration", "precipitation", "condensation"], "stomata"),
 M4("Conversion of water vapour into droplets is:", "condensation", ["evaporation", "infiltration", "transpiration"], "cloud formation"),
 M4("The largest reservoir of carbon on Earth is the:", "oceans", ["atmosphere", "living organisms", "soil only"], "~71%"),
 M4("Carbon is removed from the atmosphere by plants during:", "photosynthesis", ["respiration", "combustion", "decomposition"], "CO₂ fixed into sugars"),
 M4("The largest reservoir of nitrogen is the:", "atmosphere", ["oceans", "soil", "plants"], "N₂ gas is 78%"),
 M4("Bacteria that convert atmospheric nitrogen into usable forms are found in:", "root nodules of legumes", ["plant leaves", "animal blood", "rocks"], "Rhizobium"),
 M4("The artificial fixation of nitrogen to make fertilisers is called the:", "Haber–Bosch process", ["Bessemer process", "Contact process", "Solvay process"], "‘bread from air’"),
 M4("The India-led initiative encouraging mindful and eco-friendly lifestyles is:", "Mission LiFE", ["Swachh Bharat", "Digital India", "Make in India"], "Lifestyle for Environment"),
]
A = A[:40]
assert len(A) == 40, len(A)
B = [
 Q("Name the four spheres of the Earth system.", "Geosphere, hydrosphere, atmosphere and biosphere (cryosphere may be mentioned) (2).", "2"),
 Q("Give an example of how a change in one sphere affects another.", "Warmer sea water increases evaporation and changes monsoon rainfall (2).", "2"),
 Q("What is solar radiation? Why is it important?", "Energy from the Sun in the form of electromagnetic waves (1); drives winds, the water cycle and photosynthesis (1).", "1+1"),
 Q("Differentiate between the solar constant and insolation.", "Solar constant: energy at the top of the atmosphere (about 1.4 kW m⁻²); insolation: radiation reaching the surface (1+1).", "1+1"),
 Q("How much solar energy falls on 1 m² in one hour at an insolation of 1 kW m⁻²?", "1 kW × 1 h = 1 kWh = 3.6 × 10⁶ J (2).", "2"),
 Q("Why do polar regions receive less heat than the equator?", "The Sun's rays slant and spread over a larger area (2).", "2"),
 Q("What is the greenhouse effect?", "Greenhouse gases trap heat re-radiated from the Earth, keeping it warm (2).", "2"),
 Q("Name two greenhouse gases and a human source for each.", "CO₂ from burning fossil fuels; methane from livestock or paddy fields (1+1).", "1+1"),
 Q("What is the ozone layer? Why is it important?", "A layer of ozone in the stratosphere (1); it absorbs harmful UV radiation (1).", "1+1"),
 Q("What are CFCs? What did the Montreal Protocol do?", "Chemicals from refrigerators and aerosols that destroy ozone (1); reduced their use so the layer is recovering (1).", "1+1"),
 Q("Why does wind blow?", "Uneven heating creates pressure differences; air moves from high to low pressure (2).", "2"),
 Q("Define albedo. Give one high-albedo and one low-albedo surface.", "Fraction of radiation reflected (1); snow high, dark forest or ocean low (1).", "1+1"),
 Q("What is a biogeochemical cycle?", "The cycling of matter between living and non-living parts of the Earth (2).", "2"),
 Q("Name the processes of the water cycle.", "Evaporation, transpiration, condensation, precipitation, infiltration (2).", "2"),
 Q("How does the nitrogen in the atmosphere become useful to plants?", "Rhizobium bacteria and lightning fix N₂ into nitrogen compounds absorbed by plants (2).", "2"),
 Q("Name two ways in which an individual can reduce greenhouse gas emissions.", "Save energy, use public transport, plant trees, use renewable energy (1+1).", "1+1"),
]
C = [
 Q("Explain how a change in the cryosphere can affect the other spheres.", "Warming melts glaciers (1); sea level rises, flooding coasts (hydrosphere) (1); affects ecosystems in the biosphere (1).", "1+1+1"),
 Q("Describe the electromagnetic spectrum from long to short wavelengths.", "Radio, microwave, infrared, visible, ultraviolet, X-rays, gamma rays (2); all travel at 3 × 10⁸ m s⁻¹ in vacuum (1).", "2+1"),
 Q("Why is UV radiation harmful and useful?", "Harmful: damages eyes and skin, may cause cancer (1.5); useful: kills germs in water purifiers (1.5).", "1½+1½"),
 Q("Calculate the energy received by a 5 m² solar panel in 2 hours at 1 kW m⁻² insolation.", "Power = 5 kW (1); energy = 5 × 2 = 10 kWh (1) = 3.6 × 10⁷ J (1).", "1+1+1"),
 Q("Why is insolation at the surface less than the solar constant?", "The atmosphere absorbs, scatters and reflects part of the radiation (3).", "3"),
 Q("Why is India suitable for solar energy?", "It lies in the tropical and sub-tropical regions and gets abundant sunshine all year (3).", "3"),
 Q("Explain how the Earth's tilt and shape cause seasons and uneven heating.", "The spherical shape gives different angles of rays (1.5); the tilt changes the angle and length of days during the year (1.5).", "1½+1½"),
 Q("Describe the layers of the atmosphere with one feature each.", "Troposphere: weather; stratosphere: ozone; mesosphere: meteors burn; thermosphere/exosphere: thin (3).", "3"),
 Q("State two roles of the atmosphere in supporting life.", "Absorbs harmful UV; keeps the Earth warm by the greenhouse effect (1.5+1.5).", "1½+1½"),
 Q("Why is Venus hotter than Mercury although Mercury is nearer to the Sun?", "Venus has a thick atmosphere of CO₂ with a strong greenhouse effect (3).", "3"),
 Q("Explain how the ozone hole formed and how it is recovering.", "CFCs release chlorine that destroys ozone (1.5); the Montreal Protocol banned CFCs, so the layer is slowly recovering (1.5).", "1½+1½"),
 Q("Explain land and sea breezes.", "Day: land heats faster so air rises and cool sea air moves in (1.5); night: reverse (1.5).", "1½+1½"),
 Q("How do planetary winds and pressure belts form?", "Uneven heating of the equator and poles produces low and high pressure belts (1.5); air flows from high to low pressure belts (1.5).", "1½+1½"),
 Q("Name three factors that drive ocean currents.", "Winds, differences in temperature and salinity, Earth's rotation (1+1+1).", "1+1+1"),
 Q("Describe the water cycle and its link with all four spheres.", "Evaporation from oceans, condensation, precipitation (1.5); runoff and infiltration link the hydrosphere, atmosphere, geosphere and biosphere (1.5).", "1½+1½"),
 Q("Explain how deforestation affects the water cycle.", "Less transpiration and less infiltration, more runoff and erosion (1.5); less rainfall and soil loss (1.5).", "1½+1½"),
 Q("Describe the carbon cycle in brief.", "Plants fix CO₂ by photosynthesis (1); carbon passes through food chains and returns by respiration and decay (1); oceans store carbon (1).", "1+1+1"),
 Q("Why is the rise in atmospheric CO₂ a concern? Mention two effects.", "Enhanced greenhouse effect (1); global warming, glacier melting, sea-level rise, extreme weather (any two) (2).", "1+2"),
 Q("Explain the nitrogen cycle in short.", "Nitrogen fixation by bacteria and lightning (1); plants absorb and animals eat plants (1); decomposers return ammonia and denitrifying bacteria return N₂ (1).", "1+1+1"),
 Q("What is the Haber–Bosch process and its impact?", "Artificial fixation of nitrogen to make ammonia fertilisers (1.5); boosted food production but is energy intensive and causes pollution (1.5).", "1½+1½"),
 Q("How does the oceanic reservoir regulate carbon in the atmosphere?", "Oceans hold about 71% of the carbon and dissolve CO₂ (1.5); excess CO₂ acidifies oceans and harms marine life (1.5).", "1½+1½"),
 Q("Suggest three actions to restore balance among the Earth's spheres.", "Save energy, plant trees, use renewable energy, conserve water, sustainable farming (1+1+1).", "1+1+1"),
 Q("What is Mission LiFE?", "India-led initiative encouraging mindful, eco-friendly lifestyle choices by individuals and communities (3).", "3"),
 Q("If photosynthesis stopped on Earth, what would happen?", "No food or oxygen production; the CO₂ would rise and food chains would collapse (3).", "3"),
]
D = [
 Q("(i) Name and describe the four spheres of the Earth. (ii) Explain with an example how they are interlinked. (iii) What is the role of the cryosphere?", "(i) Geosphere, hydrosphere, atmosphere, biosphere (2). (ii) Warmer Arabian Sea alters the monsoon, affecting rivers and crops (2). (iii) Stores freshwater and regulates sea level (1).", "2+2+1"),
 Q("<b>Case study:</b> Less snowfall in winter leads to less water in a lake in summer and less grass. (i) Which spheres are involved? (ii) Trace the chain of effects. (iii) How might this affect animals? (iv) Suggest one measure.", "(i) Cryosphere/hydrosphere, biosphere (1). (ii) Less snow → less melt water → shrinking lake → less grass (2). (iii) Less food for grazers (1). (iv) Water conservation and afforestation (1).", "1+2+1+1"),
 Q("(i) What is solar radiation? (ii) Describe the electromagnetic spectrum. (iii) What are the roles of UV, visible and infrared radiation?", "(i) EM energy from the Sun (1). (ii) Gamma to radio; same speed in vacuum (2). (iii) UV absorbed by ozone; visible gives light for photosynthesis; infrared warms the Earth (2).", "1+2+2"),
 Q("<b>Case study:</b> A solar panel of 4 m² receives 1 kW m⁻² sunlight for 5 hours. (i) Find the power. (ii) Find the energy in kWh. (iii) Express it in joules. (iv) What is the difference between the solar constant and this value?", "(i) 4 kW (1). (ii) 20 kWh (1). (iii) 20 × 3.6 × 10⁶ = 7.2 × 10⁷ J (2). (iv) The solar constant (1.4) is at the top of the atmosphere, 1 kW m⁻² at the surface (1).", "1+1+2+1"),
 Q("(i) Why is the heating of the Earth uneven? (ii) How does it drive winds? (iii) Explain land and sea breezes.", "(i) Shape, tilt, latitude and surface type (2). (ii) Pressure differences make air flow from high to low (1). (iii) Day: sea breeze; night: land breeze (2).", "2+1+2"),
 Q("(i) Describe the structure of the atmosphere. (ii) What is its composition? (iii) How does it protect life?", "(i) Troposphere, stratosphere, mesosphere, thermosphere, exosphere (2). (ii) Nitrogen 78%, oxygen 21%, others (1). (iii) Absorbs UV and traps heat (2).", "2+1+2"),
 Q("<b>Case study:</b> The ozone layer thinned over Antarctica in the late 20th century. (i) What caused it? (ii) What harm does extra UV cause? (iii) What international action was taken? (iv) What is the current status?", "(i) CFCs from refrigerators and aerosols (1). (ii) Skin cancer, eye damage, harm to ecosystems (2). (iii) The Montreal Protocol (1). (iv) The layer is slowly recovering (1).", "1+2+1+1"),
 Q("(i) Explain the greenhouse effect. (ii) What is global warming? (iii) State four consequences.", "(i) GHGs trap re-radiated heat (2). (ii) Rise in average temperature due to excess GHGs (1). (iii) Melting of glaciers, sea-level rise, extreme weather, monsoon changes (2).", "2+1+2"),
 Q("<b>Case study:</b> The CO₂ level has risen from about 280 ppm to about 420 ppm. (i) What are the causes? (ii) Where is most carbon stored? (iii) How do oceans and plants respond? (iv) Suggest two ways to cut emissions.", "(i) Fossil fuels and deforestation (1). (ii) Oceans (about 71%) (1). (iii) Both absorb CO₂, but ocean acidification and saturated sinks result (1). (iv) Renewable energy, trees, saving energy (2).", "1+1+1+2"),
 Q("(i) Draw and explain the water cycle. (ii) How do human activities affect it? (iii) Give the role of transpiration.", "(i) Evaporation → condensation → precipitation → runoff/infiltration (2). (ii) Deforestation, pollution, groundwater overuse, climate change (2). (iii) Returns water vapour to the atmosphere and creates a pull in xylem (1).", "2+2+1"),
 Q("(i) Explain the carbon cycle with the help of a flow description. (ii) How do humans disturb it? (iii) Why is the ocean important?", "(i) Photosynthesis, food chain, respiration, decay, combustion, ocean exchange (3). (ii) Burning fossil fuels and deforestation (1). (iii) Large reservoir that absorbs CO₂ (1).", "3+1+1"),
 Q("<b>Case study:</b> A farmer applies urea fertiliser and also grows pulses in rotation. (i) Name the cycle involved. (ii) How do pulses help the soil? (iii) What is the Haber–Bosch process? (iv) State one harm of overusing fertiliser.", "(i) Nitrogen cycle (1). (ii) Root nodule bacteria fix nitrogen (1). (iii) Artificial fixation of nitrogen to ammonia (1). (iv) Water pollution and eutrophication (2).", "1+1+1+2"),
 Q("(i) Explain the nitrogen cycle with a flow diagram. (ii) Name the types of nitrogen fixation. (iii) Why can plants not use N₂ directly?", "(i) Atmosphere → fixation → plants → animals → decomposers → atmosphere/soil (3). (ii) Biological, lightning, industrial (1). (iii) N₂ is non-reactive (1).", "3+1+1"),
 Q("(i) How is solar energy harnessed in India? (ii) Define albedo and explain its effect on temperature. (iii) Give two high-albedo and two low-albedo surfaces.", "(i) Solar panels and heaters for electricity and heat (1). (ii) Reflectivity; high albedo leads to cooler surfaces (2). (iii) Snow, ice; forest, ocean (2).", "1+2+2"),
 Q("(i) How do human activities affect the Earth's spheres? (ii) List five practices from Mission LiFE or individual actions to reduce the impact. (iii) What is the role of international cooperation?", "(i) Emissions, deforestation, pollution disturb all spheres (2). (ii) Saving energy and water, planting trees, recycling, renewable energy, sustainable farming (2). (iii) Treaties such as the Montreal Protocol show that collective action works (1).", "2+2+1"),
 Q("(i) Why do the equator and poles differ in temperature? (ii) How does this difference drive ocean currents and winds? (iii) Give a local example of the effect of uneven heating.", "(i) Rays are concentrated at the equator and spread out over a larger area at the poles (2). (ii) Pressure and density differences set air and water in motion (2). (iii) Land and sea breezes (1).", "2+2+1"),
]
assert len(B) == 16 and len(C) == 24 and len(D) == 16, (len(A), len(B), len(C), len(D))
SETS, POOL = build(A, B, C, D)
