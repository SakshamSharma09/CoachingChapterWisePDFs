"""Class 6 SST Ch 3 Landforms and Life - Hard-tier extras (assertion-reason, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The Himalayas have tall, sharp, snow-covered peaks.", "The Himalayas are young fold mountains that have not been worn down much by erosion.", "a",
     "Young mountains are still sharp and high; R explains A."),
 AR4("The Aravalli Range is an old mountain range with rounded tops.", "The Aravalli Range is higher than the Himalayas.", "c",
     "A is true because long erosion has rounded the Aravallis; R is false, as the Himalayas are far higher."),
 AR4("A plateau has a gently sloping surface with no steep sides.", "Plateaus are often rich in minerals.", "d",
     "A plateau is a raised flat-topped land with steep sides, so A is false; R is true."),
 AR4("Terrace farming is practised on mountain slopes.", "Tourism is an important source of income in mountain regions.", "b",
     "Both statements are true, but tourism does not explain why steps are cut for farming."),
 AR4("Plains are densely populated.", "Plains have fertile soil and it is easy to build roads and railways there.", "a",
     "Good farming and easy transport attract people, which explains the dense population."),
 AR4("The Deccan Plateau has black soil that is good for growing cotton.", "The Deccan Plateau was formed by lava flows from volcanic activity.", "a",
     "Cooled lava breaks down into black soil, so R explains A."),
]

CASE = [
 Q("<b>Case study.</b> Pooja visits a village in the Himalayan foothills. She sees steps cut into the slopes where people grow crops. Many families run guest houses for visitors who come to see the snow peaks. The local people tell her that heavy rain sometimes causes sudden falls of earth and rock, and in winter snow slides down the slopes. "
   "(i) What is the farming on steps called? (ii) Name one source of income here other than farming. (iii) What is the fall of earth and rock called? (iv) Why is it difficult to build roads and railways in mountain regions?",
   "(i) Terrace farming (1). (ii) Tourism (1). (iii) A landslide (1). (iv) Mountains are high, steep and rocky with cold weather and risk of landslides and avalanches (1), so construction is costly and difficult (1).", "1+1+1+2"),
 Q("<b>Case study.</b> The Chhota Nagpur Plateau is a raised, flat-topped region with steep sides. It is rich in iron ore, coal and manganese, and many mines and factories are located there. The Deccan Plateau, formed by volcanic lava, has fertile black soil. Rivers flowing off plateaus often form waterfalls, such as Jog Falls in Karnataka. "
   "(i) Define a plateau. (ii) Name two minerals found in the Chhota Nagpur Plateau. (iii) Which soil is found in the Deccan Plateau? (iv) Why are plateaus called storehouses of minerals, and how do waterfalls help people?",
   "(i) A raised, flat-topped land with steep sides (1). (ii) Any two of iron ore, coal, manganese (1). (iii) Black soil (1). (iv) They contain many valuable minerals such as coal and iron (1); waterfalls can be used to generate hydroelectricity and attract tourists (1).", "1+1+1+2"),
 Q("<b>Case study.</b> The Ganga plain is a large, almost flat landform formed by the deposits of rivers. Its soil is very fertile and crops like wheat and rice grow well. Roads, railways and canals are easy to build, and many large cities are located here. The plain is one of the most densely populated regions of the world. "
   "(i) What is a plain? (ii) Which crops grow well on the Ganga plain? (iii) Name one facility that is easy to build here. (iv) Explain two reasons why plains attract a large population.",
   "(i) A large flat or gently rolling area of low-lying land (1). (ii) Wheat and rice (1). (iii) Roads, railways or canals (any one) (1). (iv) Fertile soil gives good harvests (1); easy transport and building of towns and industries (1).", "1+1+1+2"),
]

MISTAKES = [
 "Mixing up a <b>hill</b> and a <b>mountain</b>: a mountain is much higher with a narrow summit; a hill is lower with a rounded top and gentler slope.",
 "Calling the Aravallis young. The Himalayas are young fold mountains with sharp peaks; the Aravallis are old, worn-down and rounded.",
 "Describing a plateau as having no steep sides. A plateau is a raised, flat-topped land <i>with</i> steep sides, often rich in minerals.",
 "Confusing an <b>avalanche</b> (snow sliding down a slope) with a <b>landslide</b> (earth and rock falling).",
 "Giving the wrong peak for the continent: Everest (Asia), Aconcagua (South America), Mont Blanc (Europe), Kilimanjaro (Africa).",
 "Writing that plains are less useful. Plains are the main areas of farming, transport and dense population.",
]
