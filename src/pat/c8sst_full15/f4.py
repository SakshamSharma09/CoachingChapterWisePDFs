from h8 import *
META = meta(4, "Set 04")
A = [
 m("Which map projection is described as a compromise that balances distortions of size and shape?", "Robinson projection", ["Mercator projection", "A globe", "A satellite image"], "Mercator preserves shape and direction but distorts size near the poles."),
 m("The first Chief Election Commissioner of India was —", "Sukumar Sen", ["T.N. Seshan", "K.V.K. Sundaram", "B.R. Ambedkar"], "He conducted the first general elections of 1951–52."),
 m("The Ghadar Party, which tried to start a mutiny in the army in 1914–15, was formed by Indians living in —", "North America", ["South Africa", "Australia", "Japan"], "Lala Hardayal was among its founders."),
 m("The charbagh garden design adopted by the Mughals for tombs, forts and mosques came from —", "Persia", ["Portugal", "Rajasthan", "Gujarat"], "A four-part garden with waterways and terraces."),
 m("The National Green Tribunal (NGT) is a specialised body that decides disputes related to the —", "environment", ["taxes", "armed forces", "elections"], "Tribunals handle specific kinds of disputes."),
 st("Fundamental Duties can be enforced by courts in the same way as Fundamental Rights.", "Fundamental Duties were added to the Constitution by the 42nd Amendment in 1976.", False, True, "Duties are mainly moral and social; they were added in 1976 as Article 51A."),
 m("Japan has a median age of about 50 years, compared with India's 28 years. This shows that Japan has —", "an ageing population", ["a youth bulge", "a very high birth rate", "a large number of children"], "A high median age signals an older population."),
 ar("Slums usually come up near railway tracks and the edges of a city.", "Poor migrants cannot afford housing in planned areas and settle on vacant land.", 'exp', "R explains A: lack of affordable housing pushes the poor to unused land."),
 m("Wood, marble and gold are classed as resources for —", "materials", ["life", "energy", "culture"], "They are converted into objects."),
 ar("Akbar is remembered for his policy of religious tolerance.", "He followed the policy of sulh-i-kul, or peace with all.", 'exp', "R explains A: sulh-i-kul meant respect for all faiths."),
 m("The Third Battle of Panipat in 1761 was fought between the Marathas and —", "Ahmad Shah Abdali", ["Aurangzeb", "Babur", "Robert Clive"], "The Marathas suffered a heavy defeat."),
 m("Mangal Pandey's act of defiance in 1857 took place at —", "Barrackpore", ["Meerut", "Jhansi", "Lucknow"], "It was an early spark of the Revolt."),
 m("In India's parliamentary system, the real executive power is exercised by the —", "Prime Minister and the Council of Ministers", ["Chief Justice of India", "Speaker", "Election Commission"], "The President is the formal head of state."),
 m("Profit is the reward for —", "entrepreneurship", ["land", "labour", "capital"], "The entrepreneur bears the risk of the business."),
 chrono([("Founding of Vijayanagara", 1336), ("Destruction of Nālandā", 1193), ("Akbar becomes emperor", 1556), ("Razia Sultan rules at Delhi", 1236)]),
]
B = [
 OR(vsa("Explain the term 'ecosystem services' with one example.", "Benefits that people receive from the natural working of ecosystems — 1 mark", "Example: forests clean water and air, bees pollinate crops, wetlands reduce floods — 1 mark", head="Marking points (1 + 1):"),
    vsa("How did traditional communities protect fish populations?", "They avoided fishing during the spawning (breeding) season — 1 mark", "This let fish multiply, so the resource regenerated and was available for the future — 1 mark", head="Marking points (1 + 1):")),
 vsa("What is a stupa? Name one famous stupa.", "A dome-shaped Buddhist monument that holds relics or marks a sacred place — 1 mark", "Sanchi Stupa (Madhya Pradesh) — with ornamental gateways (toranas) — 1 mark", head="Marking points (1 + 1):"),
 OR(vsa("What is migration? State one push factor and one pull factor.", "Movement of people from one place to another to settle temporarily or permanently — 1 mark", "Push: poverty or disaster; Pull: jobs or education (any one each, ½ mark each) — 1 mark", head="Marking points (1 + 1):"),
    vsa("What is a slum? Why do slums come up in cities?", "An overcrowded settlement with poor housing and few services — 1 mark", "Migrants cannot afford housing in planned areas — 1 mark", head="Marking points (1 + 1):")),
 vsa("Name any two leaders of the Revolt of 1857 and the places they are associated with.", "Rani Lakshmibai — Jhansi", "Nana Saheb / Tantia Tope — Kanpur", "Bahadur Shah Zafar — Delhi", "Begum Hazrat Mahal — Lucknow (any two, 1 mark each)"),
]
C = [
 OR(sa("State any three differences between the Supreme Court and a High Court.", 3, sol("Marking points (any three, 1 mark each):", "Supreme Court is the highest court of India, seated in New Delhi; a High Court is the highest court of a state", "Supreme Court judges retire at 65; High Court judges at 62", "Supreme Court's law binds all courts in India; a High Court's binds courts in its state", "Supreme Court has advisory jurisdiction; High Courts have supervisory control over subordinate courts")),
    sa("Describe any three problems faced by Indian cities because of rapid growth.", 3, sol("Marking points (any three, 1 mark each):", "Traffic congestion and air pollution", "Shortage of housing, leading to slums", "Pressure on water, sanitation and waste management", "Heat islands and loss of green space"))),
 OR(sa("Describe any three features of Akbar's religious and administrative policy.", 3, sol("Marking points (any three, 1 mark each):", "Sulh-i-kul — peace and tolerance for all faiths", "Abolished the jizya tax on non-Muslims (and pilgrim tax)", "Employed Rajputs and people of all communities in high posts", "Mansabdari system — officers graded by rank")),
    sa("Describe any three features of Hampi, the capital of the Vijayanagara Empire.", 3, sol("Marking points (any three, 1 mark each):", "Situated on the banks of the Tungabhadra river with rocky hills as natural defence", "Grand temples, palaces and royal enclosures built by the rulers", "Busy bazaars where traders from many places bought and sold goods", "Tanks, canals and water works to supply water; later a UNESCO World Heritage Site"))),
]
D = [
 OR(sa("How did the bhakti and Sufi movements promote harmony? Name some saints and the main ideas they taught.", 5, sol("Marking points (any five, 1 mark each):", "Bhakti — the path of devotion; Kabir, Ravidas, Guru Nanak, Chaitanya Mahaprabhu, Tukaram, Mirabai (any three names)", "Kabir criticised rituals of both Hinduism and Islam and spoke of one god", "Ravidas promoted equality and oneness of all", "Sufism stressed devotion and an inner, personal search for god", "Qawwālīs of Sufi saints blended local and Persian music", "Saints used common regional languages so that ordinary people understood them")),
    sa("Describe the role of women in India's freedom struggle with the help of examples.", 5, sol("Marking points (any five, 1 mark each):", "Women took part in the Salt March and boycott of foreign cloth", "Sarojini Naidu led the Salt Satyagraha at Dharasana", "Annie Besant led the Home Rule Movement", "Aruna Asaf Ali hoisted the flag at the start of Quit India", "Kanaklata Barua became a martyr in 1942", "Bina Das and other revolutionaries joined armed resistance; Rani Lakshmibai led in 1857"))),
 sa("Explain the four factors of production, their rewards and the importance of entrepreneurship.", 5, sol("Marking points (any five, 1 mark each):", "Land — all natural resources used in production; reward: rent", "Labour — human effort, physical or mental; reward: wages", "Capital — machines, tools, buildings and money used to produce goods; reward: interest", "Entrepreneurship — organising the other factors and taking risks; reward: profit", "The factors must work together; without the entrepreneur's decisions production may not start", "Any one example showing all four factors working in a business")),
]
E = [
 src("Anandibai Joshi was married at the age of nine. When her baby died soon after birth for want of proper medical care, she resolved to become a doctor. At a time when few Indian women received any education, she travelled across the seas to the United States and studied medicine in Pennsylvania. Despite poor health and social criticism, she completed her degree.",
     [s("What event made Anandibai decide to study medicine?", 1, "The death of her baby for want of proper medical care."),
      s("Where did she study medicine?", 1, "In Pennsylvania, United States of America."),
      s("What does her story teach us about discrimination and determination? Give two points.", 2, "(1) Women faced discrimination in education and professions; (1) determination and courage can overcome obstacles and open doors for others.")]),
 src("Under the Permanent Settlement introduced by Lord Cornwallis in 1793, the zamindars of Bengal had to pay a fixed amount of land revenue to the Company every year. Zamindars collected rent from the peasants, and if they failed to pay the fixed sum on time, their estate could be auctioned. Many zamindars raised rents on peasants to meet the demand, even when the harvest was poor.",
     [s("Who introduced the Permanent Settlement?", 1, "Lord Cornwallis."),
      s("What was 'fixed' under this arrangement?", 1, "The amount of land revenue payable by the zamindars to the Company."),
      s("Explain two effects of this system on peasants.", 2, "(1) Peasants had to pay high rents even in poor harvests; (1) they fell into debt and many lost their land when zamindars were pressed by the fixed demand.")]),
 src("Jaipur, founded in 1727 by Sawai Jai Singh II, is one of India's best-planned old cities. The streets run in a grid pattern, forming rectangular blocks called chowkris. Wide main roads, separate markets for different trades and sandstone buildings gave the city an orderly look. Its architect, Vidyadhar Bhattacharya, helped design the plan.",
     [s("Who founded the city of Jaipur and in which year?", 1, "Sawai Jai Singh II, in 1727."),
      s("What are chowkris?", 1, "Rectangular blocks formed by the grid of streets."),
      s("State two advantages of such a planned city layout.", 2, "Any two (1 mark each): easy movement and orderly traffic; planned markets and services; room for open spaces; easier to expand and maintain.")]),
 src("The Atacama Desert in Chile is one of the driest places on Earth and is famous for stargazing. In recent years it has also become a dumping ground for discarded clothes, a result of 'fast fashion' — cheap, trendy clothing that is made quickly and thrown away when styles change. The United Nations has called this problem 'an environmental and social emergency'.",
     [s("In which country is the Atacama Desert located?", 1, "Chile."),
      s("What is meant by 'fast fashion'?", 1, "Cheap, trendy clothing made quickly and discarded when fashion changes."),
      s("Suggest two ways in which individuals can reduce this problem.", 2, "Any two (1 mark each): buy fewer clothes; repair and reuse; donate or exchange; choose durable clothing.")]),
]
F = mapq([("Wardha (Sevagram)", 78.6, 20.75, "Maharashtra"), ("Gwalior", 78.18, 26.22, "Madhya Pradesh"), ("Srirangam (Tiruchirappalli)", 78.69, 10.86, "Tamil Nadu"), ("Varanasi", 83.0, 25.32, "Uttar Pradesh"), ("Kolkata", 88.36, 22.57, "West Bengal"), ("Bengaluru", 77.59, 12.97, "Karnataka")])
SECTIONS = assemble(A, B, C, D, E, F)
