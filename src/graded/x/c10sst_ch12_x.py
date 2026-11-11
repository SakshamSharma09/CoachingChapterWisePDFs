"""Class 10 SST Ch 12 Lifelines of National Economy - extras."""
from common import AR4, Q

AR = [
 AR4(r"The Golden Quadrilateral Super Highways are being implemented by the National Highways Authority of India.", r"The Border Roads Organisation was established in 1960 to develop roads in the northern and north-eastern border areas.", "b",
     r"Both statements are true, but the BRO's work on border roads does not explain who builds the Golden Quadrilateral."),
 AR4(r"Pipelines are an economical mode of transporting crude oil and natural gas over long distances.", r"After laying, their running cost is low and they avoid trans-shipment losses and delays.", "a",
     r"The initial cost is high but later costs are small and there is no trans-shipment, which explains why pipelines are economical."),
 AR4(r"Kandla in Gujarat is a tidal port.", r"Kandla is located on the eastern coast of India.", "c",
     r"A is true: Kandla was developed to ease the pressure on Mumbai port. R is false: it lies on the western coast."),
 AR4(r"Roadways have completely replaced railways in India.", r"Railways remain the principal mode of transport for both freight and passengers in India.", "d",
     r"A is false, since both modes work together and roads cannot replace railways for bulk long-distance carriage. R is true."),
 AR4(r"Railways are the principal mode of transportation for freight and passengers in India.", r"Railways conduct multifarious activities such as business, sightseeing and pilgrimage besides carrying goods over long distances.", "a",
     r"Carrying people and goods over long distances for so many purposes is why they are the principal mode; R explains A."),
 AR4(r"Mormugao port in Goa handles a large share of India's iron ore exports.", r"Kolkata is an inland riverine port.", "b",
     r"Both are true but unrelated, so R does not explain A."),
]

CASE = [
 Q(r"<b>Case study.</b> Dinesh, a truck driver from Jaipur, carries goods to Chennai. He uses a six-lane highway that is part of the project linking Delhi, Mumbai, Chennai and Kolkata. For small villages off the highway he delivers the goods on narrower roads. His friend says that the road network of India is among the largest in the world. "
   r"(i) Name the project that links Delhi, Mumbai, Chennai and Kolkata. (ii) Which authority is responsible for national highways? (iii) The North-South corridor links which two places? (iv) Why are roadways preferred to railways for short distances and for reaching villages?",
   r"(i) The Golden Quadrilateral Super Highways (1). (ii) National Highways Authority of India (NHAI) (1). (iii) Srinagar and Kanyakumari (1). (iv) Roads provide door-to-door service, have lower construction cost, can climb gradients and pass through rough terrain, and can reach villages where rail lines cannot (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Ashok runs a firm in Goa that exports iron ore to Japan. His goods leave from a port that is among the leading iron ore exporters of the country. Another friend ships goods through the port at Navi Mumbai, which was planned to relieve the pressure on Mumbai port. A third trader uses Kandla in Gujarat, a tidal port. "
   r"(i) Name the port Ashok uses. (ii) Name the port at Navi Mumbai. (iii) What kind of port is Kandla? (iv) Why are ports called the gateways of international trade?",
   r"(i) Mormugao port (1). (ii) Jawaharlal Nehru Port (Nhava Sheva) (1). (iii) A tidal port (1). (iv) Goods for foreign countries are loaded and imported goods are unloaded at ports, so they link the country to the world by sea, and sea transport carries most of the bulk cargo of international trade cheaply (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In a year, a country exports goods worth Rs 80 crore and imports goods worth Rs 100 crore. A student of economics notes that the advancement of international trade of a country is an index of its economic prosperity, and that the gap between exports and imports must be watched. "
   r"(i) What is meant by balance of trade? (ii) Is the country's balance of trade favourable or unfavourable? (iii) What is the amount of the deficit? (iv) Why is international trade considered an index of the economic prosperity of a country?",
   r"(i) The difference between the value of exports and the value of imports (1). (ii) Unfavourable (adverse), because imports exceed exports (1). (iii) Rs 20 crore (1). (iv) No country can produce all it needs, so trade lets it exchange surplus goods for what it lacks; a country with a flourishing trade has strong production and demand, so trade reflects its economic health (2).", "1+1+1+2"),
]

MISTAKES = [
 r"Writing that Mumbai is an <b>artificial</b> harbour: it is the <b>biggest natural harbour</b>, while Chennai is an artificial port and Kandla a <b>tidal</b> port.",
 r"Mixing up the Golden Quadrilateral (<b>Delhi-Kolkata-Chennai-Mumbai</b>) with the North-South (<b>Srinagar-Kanyakumari</b>) and East-West (<b>Silchar-Porbandar</b>) corridors.",
 r"Saying that the <b>NHAI</b> builds state highways; state highways and district roads are built and maintained by the State Public Works Department, and the BRO builds roads in border areas.",
 r"Confusing <b>balance of trade</b> (goods only, exports minus imports) with 'balance of payments', or calling a deficit 'favourable'.",
 r"Forgetting that the first railway ran from <b>Mumbai to Thane</b> in 1853, and treating railways as unimportant now; they are still the principal mode for bulk freight.",
 r"Treating communication as only the telephone: it includes <b>personal communication</b> (post, telephone, internet) and <b>mass communication</b> (radio, TV, newspapers, cinema).",
]
