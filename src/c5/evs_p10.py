from evs_common6 import *

q = []
q.append(mcq("Look at the picture. It is related to:", ["a heritage monument (fort)", "a dam", "a market", "a hospital"], 0, fig=pic("🏰 🚩 🐪")))
q.append(mcq("The State Flower of Rajasthan is:", ["Lotus", "Rohida", "Rose", "Marigold"], 1))
q.append(Q("Name one use of each tree.", 3, "", parts=[
    P("(i)", "Khejri", 1, "Its pods (sangri) are eaten as a vegetable; leaves are fodder for goats and camels."),
    P("(ii)", "Neem", 1, "Medicine / shade / twigs for cleaning teeth."),
    P("(iii)", "Ber", 1, "Gives sweet-sour fruits (ber).")]))
q.append(cities_q([dq("(a)", "Kota", "Udaipur", 2, "west"), dq("(b)", "Bharatpur", "Kota", 2, "south-west"),
                   P("(c)", "Which city shown in the figure lies farthest to the south?", 1, "Banswara."),
                   P("(d)", "Name the state that lies to the south-west of Rajasthan.", 1, "Gujarat.")]))
q.append(mcq("The Keoladeo National Park at Bharatpur is famous for its:", ["birds", "lions", "elephants", "whales"], 0))
q.append(Q("Write any three features that help a camel to live in the desert.", 3,
           "Broad padded feet do not sink in sand; long eyelashes and closable nostrils keep out sand; the hump stores fat for food; it can go for a long time without water."))
q.append(Q("", 8, "", parts=[
    P("(i)", "Write <b>four</b> slogans or rules for a tree-plantation campaign <i>'Save Trees, Save Earth'</i>.", 4,
      "Any four: Plant a tree on your birthday; Trees give life; Do not cut green trees; Water the sapling daily; One child, one tree."),
    P("(ii)", "Look at the picture: " + pic("🛍️🧴🥤 🐄 🌳") + "Plastic bags and bottles are lying in a park and a cow is eating a bag. (a) What problem is shown? (b) What can you do?", 4,
      "(a) Litter and plastic waste harm animals and spoil the park (2). (b) Use cloth bags, put waste in dustbins, do not throw plastic (2).")]))
q.append(mcq("Bajra belongs to the group of:", ["cereals", "pulses", "oilseeds", "spices"], 0))
q.append(mcq("Ker and sangri are used as:", ["vegetables", "medicines only", "fodder only", "fuel"], 0))
q.append(Q("Write any three differences between <b>wild</b> animals and <b>domestic</b> animals.", 3,
           "Wild animals live in forests; domestic animals live with people. Wild animals find their own food; domestic animals are fed by humans. Examples: tiger, deer vs cow, goat."))
q.append(Q("Instead of a gift, a school suggests that every child plants a sapling on his birthday. Do you agree?", 3, "", parts=[
    P("(i)", "Give two reasons.", 2, "Yes. Trees clean the air and give shade, fruit and homes to birds; a living gift grows for years."),
    P("(ii)", "Name a tree you would plant and why.", 1, "e.g. Neem for shade and medicine.")]))
q.append(Q("Your class is visiting a fort in Rajasthan.", 3, "", parts=[
    P("(i)", "Write two questions you would ask the guide.", 2, "e.g. Who built this fort and when? How did people get water in the fort?"),
    P("(ii)", "Write one rule to follow at monuments.", 1, "Do not write on walls or litter.")]))
q.append(Q("Why should we not throw plastic bags in the open? Give three reasons.", 3,
           "Animals eat them and fall ill; they block drains; plastic does not rot, so it pollutes the soil."))
q.append(Q("", 6, "", parts=[
    P("(a)", "Name two Indian states on the coast of the Arabian Sea and one on the Bay of Bengal.", 3,
      "Arabian Sea: Gujarat, Maharashtra, Goa, Karnataka, Kerala (any two). Bay of Bengal: Odisha, West Bengal, Andhra Pradesh, Tamil Nadu (any one)."),
    P("(b)", "Match the person with the work." + match(["Amrita Devi", "Maharshi Dayanand Saraswati", "Maharaja Ganga Singh"],
        ["Brought canal water to Bikaner", "Gave her life to save Khejri trees (Khejarli)", "Founded the Arya Samaj"]), 3, "1-b, 2-c, 3-a.")]))
q.append(Q("", 8, "", parts=[
    P("(i)", "Sort these into things that rot (biodegradable) and those that do not: fruit peel, plastic bag, dry leaves, glass bottle, vegetable waste, tin can, paper, polythene.", 4,
      "Rot: fruit peel, dry leaves, vegetable waste, paper. Do not rot: plastic bag, glass bottle, tin can, polythene."),
    P("(ii)", "People of a village threw garbage into their pond and its fish died. After a cleaning drive the fish came back. (a) Why did the fish die? (b) What should the villagers do in future?", 4,
      "(a) Garbage made the water dirty and the fish could not get clean water (2). (b) Never dump garbage in the pond; use a dustbin / compost pit (2).")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "The water of a river turned dark near a factory. (i) What is the likely cause? (ii) How does it affect fish? (iii) What can be done?", 3,
      "(i) Dirty waste of the factory flowing in. (ii) Fish fall ill and die. (iii) Treat the waste before releasing it; stop dumping."),
    P("(b)", "Compare a cloth bag and a plastic bag in three points.", 3,
      "Cloth bag can be used again and again; plastic bag is thrown away; cloth bag does not harm animals; plastic does not rot.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "In recent years summers have become hotter and rain uneven. Give one cause, one effect on farmers and one thing we can do.", 3,
      "Cause: burning fuels / cutting forests. Effect: crops fail due to too little or too much rain. We can plant trees and save energy."),
    P("(b)", "Many houses in Rajasthan have solar panels on the roof. Write three benefits.", 3,
      "Free energy from the sun; no smoke; saves electricity bill.")]))
q.append(mcq("On a road with no footpath, a person walking should walk:", ["in the middle", "on the right side facing the traffic", "on the left side with the traffic", "anywhere"], 1))
q.append(Q("In Holi it is better to use natural colours.", 3, "", parts=[
    P("(i)", "Why should chemical colours be avoided?", 1, "They can harm skin and eyes."),
    P("(ii)", "Name one natural source of colour.", 1, "Turmeric (yellow) / palash flowers (orange) / beetroot (pink)."),
    P("(iii)", "What should you do if colour goes into your eyes?", 1, "Wash with clean water at once and tell an elder.")]))
q.append(Q("", 6, "", parts=[
    P("(a)", "Match the monument with its city." + match(["Mehrangarh Fort", "Lake Pichola", "Gadisar Lake"], ["Jaisalmer", "Jodhpur", "Udaipur"]), 3, "1-b, 2-c, 3-a."),
    P("(b)", "Fill in the blanks: (i) Using public transport reduces ___. (ii) A ___ does not need fuel. (iii) ___ vehicles give out no smoke.", 3,
      "(i) pollution (ii) bicycle (iii) Electric.")]))
q.append(mcq("AIR stands for:", ["All India Radio", "Air India Runway", "All Indian Roads", "Area India Report"], 0))
q.append(Q("", 6, "", parts=[
    P("(a)", "Whom would you inform if: (i) someone cuts trees in a forest (ii) garbage is not collected for days (iii) you see an accident?", 3,
      "(i) Forest department (ii) Municipality / Panchayat (iii) Police (call 112) / ambulance."),
    P("(b)", "Write the use: (i) Amla (ii) Ajwain (iii) Pudina (mint).", 3,
      "(i) Rich in vitamin C. (ii) Helps in stomach ache / gas. (iii) Cooling; helps digestion.")]))
run(10, q)
