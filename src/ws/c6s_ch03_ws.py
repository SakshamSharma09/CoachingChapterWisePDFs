"""Class 6 Science Ch 3 - Mindful Eating: A Path to a Healthy Body: worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c6s_ch03"

def _base():
    s = importlib.util.spec_from_file_location("c6sci_ch03", str(REPO / "src/rn_work/c6_sci/ch03.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Which nutrient is the primary source of energy for our body?", 1, "(a) carbohydrates", "E", opts=["carbohydrates", "roughage", "vitamin D", "iodine"]),
W("Lack of Vitamin C causes the disease:", 1, "(c) scurvy", "E", opts=["rickets", "goitre", "scurvy", "anaemia"]),
W("A blue-black colour on adding iodine solution shows the presence of:", 1, "(b) starch", "E", opts=["protein", "starch", "fat", "water"]),
W("Which of these is a protein-rich food?", 1, "(d) moong dal", "E", opts=["sugar", "salt", "cucumber", "moong dal"]),
W("Goitre is caused by the lack of:", 1, "(b) iodine", "E", opts=["iron", "iodine", "calcium", "vitamin A"]),
W("Which of these is a nutri-cereal (millet)?", 1, "(c) ragi", "E", opts=["maida", "polished rice", "ragi", "sugar"]),
W("Fill in the blank: Roughage helps in removing ______ food from the body.", 1, "undigested.", "E"),
W("Fill in the blank: The distance travelled by food from producer to consumer is called ______.", 1, "food miles.", "E"),
W("Write True or False: Vitamins and minerals are needed in large amounts.", 1, "False. They are needed in small amounts, but they protect us from disease. (1)", "E"),
W("Name the vitamin that our body makes in sunlight.", 1, "Vitamin D. (1)", "E"),
W("Name the nutrient that builds muscles and helps in growth and repair.", 1, "Proteins. (1)", "E"),
W("Name two foods rich in fats.", 2, "Any two: ghee, butter, oil, groundnut, coconut, almonds. (1+1)", "E"),
W("What deficiency disease is caused by lack of iron? State one symptom.", 2, "Anaemia (1). Weakness or shortness of breath (1).", "E"),
W("Why does a marathon runner drink glucose water?", 1, "Glucose is a carbohydrate and gives instant energy. (1)", "E"),
W("What does FSSAI stand for?", 1, "Food Safety and Standards Authority of India. (1)", "E"),
W("Name the traditional stove and grinding stone used earlier in Indian kitchens.", 2, "Chulha (stove) and sil-batta (grinding stone). (1+1)", "E"),
W("Write one use of water in our body.", 1, "It helps absorb nutrients and removes waste through sweat and urine. (1)", "E"),
# ---------------- MEDIUM ----------------
W("Complete the table: Test for starch - ______; test for fat - ______; test for protein - ______ (name the positive result).", 3, "Starch: iodine solution turns blue-black. Fat: oily patch on paper. Protein: copper sulfate and caustic soda give violet colour. (1 each)", "M"),
W("Write the steps of the paper test for fat.", 3, "Rub or press a small piece of food on a piece of paper (1). Let the paper dry (1). Hold it against the light; an oily patch that lets light through shows fat (1).", "M"),
W("Rohit put a drop of iodine on a boiled potato and on a cucumber slice. The potato turned blue-black and the cucumber did not. What do you conclude?", 2, "Potato contains starch, and the cucumber has little or none. (2)", "M", wp=True),
W("Why do we eat more ghee and nuts in winter?", 2, "Fats give stored energy and help to keep the body warm. (2)", "M", wp=True),
W("Mohan's grandmother has bleeding gums. Which vitamin may she lack? Suggest two foods.", 3, "Vitamin C (1). Foods: amla and guava (also orange, lemon, green chilli). (1+1)", "M", wp=True),
W("In 1746 James Lind observed sailors with swollen, bleeding gums. What did he find?", 2, "Sailors who ate lemons and oranges recovered. Scurvy is caused by lack of vitamin C. (2)", "M"),
W("Why was iodised salt introduced? Name the disease it prevents.", 2, "Soil, food and water in some regions lacked iodine (1). Iodised salt prevents goitre, a swelling at the front of the neck (1).", "M"),
W("Pooja eats only rice and bread and no vegetables or fruit. Name two nutrients she may lack and a disease linked to one.", 3, "Vitamins and minerals (and roughage) (1+1). Lack of vitamin C may cause scurvy or lack of iron may cause anaemia (1).", "M", wp=True),
W("Why should we eat locally grown food? Give two reasons.", 2, "It is fresher, cheaper and has fewer food miles; it supports local farmers and reduces pollution. (Any two, 1 each)", "M"),
W("Table of per 100 g: Potato wafers - fat 35.0 g, protein 7.0 g, fibre 4.8 g; roasted chana - fat 6.26 g, protein 18.64 g, fibre 16.8 g. Which is the healthier choice and why?", 3, "Roasted chana (1). It has more protein (1) and fibre and much less fat (1).", "M", wp=True),
W("What is a balanced diet? Why do different people need different diets?", 3, "A diet containing all nutrients, roughage and water in the right amounts (1). Needs depend on age, gender, physical activity, health and lifestyle (2).", "M"),
W("Name four millets and say why they are called nutri-cereals.", 3, "Jowar, bajra, ragi, sanwa (1.5). They are rich in vitamins, minerals such as iron and calcium, and fibre (1.5).", "M"),
W("Why should fruits and vegetables be washed before cutting, and why should they not be overcooked?", 2, "Washing removes dirt and germs; overcooking at high heat destroys some vitamins such as vitamin C. (1+1)", "M", wp=True),
W("Why have cooking practices in India changed over time? Give two reasons.", 2, "Technological development and better transport and communication. (1+1)", "M"),
W("Write the sources and one function of vitamin D.", 2, "Sources: sunlight, milk, butter, eggs, fish (1). It helps the body absorb calcium for strong bones and teeth (1).", "M"),
W("A child has soft and bent bones. Name the disease and the nutrients involved.", 2, "Rickets, caused by lack of vitamin D (and calcium). (2)", "M", wp=True),
W("Why is roughage called a non-nutrient but still necessary?", 2, "It gives no nutrients but removes undigested food and prevents constipation. (2)", "M"),
W("Find the mistake: \"Peanuts contain only fat, so they are not a good protein source.\"", 2, "Peanuts contain both protein and fat; one food can have several nutrients. (2)", "M"),
W("Why do traditional foods of Punjab, Karnataka and Manipur differ?", 3, "They depend on locally grown crops, which depend on soil and climate (1.5), and on taste, culture and traditions (1.5).", "M"),
# ---------------- HARD ----------------
W("Asha tests four foods. Boiled rice and bread turn blue-black with iodine, butter makes an oily patch on paper, and boiled gram gives violet colour with copper sulfate and caustic soda. Write what each shows.", 4, "Rice and bread contain starch (1). Butter contains fat (1). Boiled gram contains protein (1). Foods can contain more than one nutrient, so more tests could give more results (1).", "H", wp=True),
W("A school canteen sells only samosas, chips and cold drinks. Write a note of 4 points to the principal on why this is unhealthy and what to add.", 4, "These are junk foods high in sugar and fat and low in protein, vitamins, minerals and fibre (1). They may cause obesity and tiredness (1). Add fruits, sprouts, roasted chana and milk (1) and a watch on food by FSSAI rules and cleanliness (1).", "H", wp=True),
W("Anita says, \"Salt is a nutrient we get only from plants and animals.\" Is she right? Explain.", 3, "No (1). Salt comes from rocks or sea water (1). Vitamin D is another example made by the body in sunlight, so not all nutrients come only from plants and animals (1).", "H", wp=True),
W("Explain, using the work of Coluthur Gopalan, how science helped a government programme for school children.", 3, "He started nutrition research in India and analysed over 500 Indian foods (1). His surveys showed deficiencies of protein and energy (1). This led to the Mid Day Meal Programme, now PM POSHAN, giving balanced food in schools (1).", "H"),
W("The Agariyas of the Little Rann of Kutch farm salt. Why is the salt they produce important for our health after processing?", 3, "Salt is a mineral we need in small amounts (1). Iodised salt prevents goitre (1), so salt farming helps in good health (1).", "H", wp=True),
W("A wheat farmer in Madhya Pradesh grows wheat for a shop in Chennai. Explain the food miles and one way to reduce them.", 3, "Food miles are the distance wheat travels from farm to consumer, here a long distance (1). Long distances increase cost, pollution and time (1). Buying locally grown grains and other local food reduces food miles (1).", "H", wp=True),
W("Why is it better for a growing child to eat a mix of dal, vegetables, roti, milk and fruit than only potato chips? Explain nutrient by nutrient.", 4, "Roti gives carbohydrates for energy (1), dal gives proteins for growth (1), milk, vegetables and fruit give vitamins, minerals and fibre for protection (1). Chips mainly give fat and sugar and few other nutrients (1).", "H", wp=True),
W("Why are packaged foods required to list their nutrients? Name an organisation involved in food safety.", 3, "Nutrient lists help us choose healthy food and compare products (2). FSSAI regulates food quality in India (1).", "H"),
W("Can a person who eats a lot of food still lack nutrients? Explain with an example.", 3, "Yes (1). If the food is mostly junk or has only one kind of nutrient, other nutrients are missing (1). E.g. someone eating only rice may lack vitamins and proteins and show deficiency symptoms (1).", "H"),
W("Explain how to test a food item for protein safely and mention two safety rules.", 4, "Make a paste of the food in a test tube with 2-3 tsp of water (1). Add 2 drops of copper sulfate and 10 drops of caustic soda, shake and wait; violet colour shows protein (1). Safety: do the test only under the teacher's guidance, and never taste or smell chemicals and wash spills with water (2).", "H"),
W("Arun says, \"If I drink more water I do not need food.\" Correct his idea and give reasons.", 3, "Water is necessary but gives no energy or nutrients (1). It helps in absorbing nutrients and removing waste (1). A balanced diet with all nutrients is also needed for growth and health (1).", "H", wp=True),
W("Why do polar bears store fat under the skin? Connect it with the idea that fat is stored energy.", 3, "Polar bears hibernate and do not eat for months (1). Stored fat gives them energy during that time (1) and also helps keep them warm (1).", "H"),
W("List four nutrients, one source of each, and one deficiency disease or role for each.", 4, "Carbohydrates - rice - energy (1). Proteins - dal - growth (1). Vitamin A - carrot - healthy eyes, prevents night blindness (1). Iron - green leafy vegetables - anaemia (1).", "H"),
W("Why should we not waste food? Give three reasons, one from the farmer's view.", 3, "Farmers work hard to grow food and wasting it disrespects their effort (1). Wasted food uses up resources like water and transport (1). Many people lack food, so we should take only what we can eat (1).", "H", wp=True),
]

CH = _base()
CH["blocks"] += [
 ("h2", "3.8 Worked Examples: Reading Food Tests and Diets"),
 ("steps", [("Example 1 — Interpreting a test table", "Food A turns blue-black with iodine; Food B leaves an oily patch on paper; Food C gives violet colour with copper sulfate and caustic soda; Food D does all three. **Result:** A has starch, B has fat, C has protein and D has starch, fat and protein."),
  ("Example 2 — Choosing between two snacks", "Per 100 g potato wafers have 536 kcal and 35.0 g fat but only 7.0 g protein. Roasted chana has 355 kcal, 6.26 g fat, 18.64 g protein and 16.8 g fibre. Chana gives more protein and fibre with less fat, so it is the healthier choice."),
  ("Example 3 — Matching symptom to nutrient", "Bleeding gums → vitamin C (scurvy). Soft, bent bones → vitamin D (rickets). Swelling in the front of the neck → iodine (goitre). Weakness and shortness of breath → iron (anaemia). Night blindness → vitamin A.")]),
 ("h2", "3.9 Nutrients at a Glance"),
 ("table", ["Group", "Nutrients", "Main job", "Memory hook"],
  [["Energy-giving", "Carbohydrates, fats", "Give energy for work and warmth", "Roti, rice, ghee, oil"],
   ["Body-building", "Proteins", "Growth, repair of body", "Dal, milk, egg, paneer"],
   ["Protective", "Vitamins, minerals", "Fight disease, keep body working", "Fruits, vegetables"],
   ["Other needs", "Roughage, water", "Remove waste, help digestion and absorption", "Salad, whole grains, water"]]),
 ("h2", "3.10 Common Mistakes"),
 ("ul", ["Iodine solution tests only for **starch**; it does not show fat or protein.",
  "The colour for protein is **violet** (not blue-black); for starch it is **blue-black**.",
  "Roughage is not a nutrient, but a balanced diet needs it.",
  "Sugar is a carbohydrate, so it also gives energy; but too much sugar and junk food is harmful.",
  "Deficiency diseases come from **long-term** lack of a nutrient, not from missing one meal.",
  "Do not confuse **fortification** (adding nutrients in processing, e.g. iodised salt) with junk food."]),
 ("h2", "3.11 Healthy Habits Checklist"),
 ("ul", ["Eat at regular times; do not skip breakfast.",
  "Include one food from each group at every main meal.",
  "Choose fruit, sprouts, roasted chana and buttermilk over chips and cold drinks.",
  "Wash hands, fruits and vegetables before eating.",
  "Drink enough water through the day.",
  "Read the nutrient label on packets and look for the FSSAI mark.",
  "Take only what you can finish; avoid wasting food."]),
 ("h2", "3.12 Higher Order Questions"),
 ("qa", [("Why is it said that a food can contain more than one nutrient?", "Peanuts have both protein and fat; milk has proteins, fats, carbohydrates, vitamins and minerals."),
  ("Why do vitamin C rich foods lose some of their value when overcooked?", "High heat destroys some vitamins such as vitamin C, so fresh fruit and uncooked vegetables are valuable."),
  ("Why is a mid-day meal important for school children?", "It gives balanced food to every child, improving health and learning."),
  ("Why are millets good for the planet and for health?", "They grow easily in different climates, are nutrient-rich and are local plant-based food.")]),
]
CH["takeaways"] += ["Eat **fresh, local, balanced** food; avoid junk food and waste.", "One food can contain **more than one** nutrient."]

if __name__ == "__main__": run(__file__, BANK, 6, "Science", WS, CH)
