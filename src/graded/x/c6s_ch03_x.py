"""Class 6 Science Ch 3 Mindful Eating - extras."""
from common import AR4, Q

AR = [
 AR4("Proteins are called body-building nutrients.", "Proteins help in growth and repair of the body.", "a",
     "Growth and repair of tissues is why proteins are called body-building nutrients."),
 AR4("Lack of vitamin C causes scurvy.", "Citrus fruits like lemon and amla are rich in vitamin C.", "b",
     "Both are true, but the food source does not explain the disease."),
 AR4("Iodine solution turns blue-black when it is added to a food containing starch.", "Iodine solution turns blue-black with proteins also.", "c",
     "A is true (starch test); R is false, the blue-black colour is the test for starch only."),
 AR4("Dietary fibre gives a lot of energy to the body.", "Fibre helps in the passing out of undigested food and prevents constipation.", "d",
     "A is false: fibre gives no energy. R is true."),
 AR4("A balanced diet contains all nutrients in the right amounts.", "Eating only one kind of food will keep the body healthy.", "c",
     "A is true; R is false because a single food cannot give all nutrients."),
 AR4("Lack of iron in food can cause anaemia.", "Iron is needed to make haemoglobin in the blood.", "a",
     "Without enough iron the blood cannot make enough haemoglobin, so R explains A."),
]

CASE = [
 Q("<b>Case study.</b> Aarav's tiffin usually has only chips and biscuits. His teacher in Chennai explained that such packaged junk food has a lot of fat, sugar and salt but little else. She asked the class to read food labels and to eat a variety of foods such as dal, vegetables, fruits, rotis and milk. "
   "(i) Which nutrient in dal helps growth? (ii) Name a nutrient in fruits and vegetables that protects the body from disease. (iii) What can we learn by reading a food label? (iv) Why is a mix of foods better than only chips and biscuits?",
   "(i) Protein (1). (ii) Vitamins (and minerals) (1). (iii) The ingredients and nutrients in the food (and its date of expiry) (1). (iv) No single food gives all the nutrients (1); a mix gives carbohydrates, proteins, vitamins and minerals in balance, while junk food has too much fat, sugar and salt (1).", "1+1+1+2"),
 Q("<b>Case study.</b> In a school activity, Simran put a few drops of iodine solution on a slice of boiled potato and on a piece of paneer. The potato turned blue-black but the paneer did not change colour. She then rubbed a small piece of groundnut on brown paper and saw an oily patch. "
   "(i) Which nutrient does the iodine test show? (ii) Which of the two foods contains it? (iii) Which nutrient did the oily patch show? (iv) Why does the body need the nutrient found in the potato? Name one other food rich in it.",
   "(i) Starch (a carbohydrate) (1). (ii) Potato (1). (iii) Fat (1). (iv) Carbohydrates give energy (1); rice (or wheat, bread) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Kabir's gums bleed often and he feels weak. A doctor in Kolkata finds that his diet has almost no fresh fruit. Another child in his class, Tanvi, cannot see well in dim light, and a third child, Joy, has weak bones and bent legs. The doctor says all three need to improve their diet. "
   "(i) Kabir is likely to lack which vitamin? (ii) Which disease is caused by lack of vitamin A? (iii) Lack of which vitamin gives weak bones? (iv) Suggest one food each for Tanvi and Joy.",
   "(i) Vitamin C (1). (ii) Night blindness (1). (iii) Vitamin D (rickets) (1). (iv) Tanvi: carrot or papaya (vitamin A) (1); Joy: milk or eggs, with morning sunlight (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Nutrients and their use", ["Carbohydrates: energy (rice, potato).", "Proteins: growth and repair (dal, paneer, eggs).", "Fats: stored energy, warmth (ghee, oil).",
   "Vitamins and minerals: protect the body and keep it working.", "Water and fibre: water helps digestion; fibre helps remove waste."]),
 ("Vitamins and deficiency", ["Vitamin A: night blindness.", "Vitamin C: scurvy (bleeding gums).", "Vitamin D: rickets (weak bones); sunlight helps make it.",
   "Iron: anaemia.   Iodine: goitre.   Calcium: weak bones and teeth."]),
 ("Food tests", ["Starch: iodine solution turns blue-black.", "Fat: food rubbed on paper leaves an oily patch."]),
 ("Healthy eating", ["Balanced diet: all nutrients in the right amount.", "Eat a variety, wash food, eat slowly, do not waste food.", "Junk food: high fat, sugar and salt; eat rarely.", "Read the food label before buying packaged food."]),
]

MISTAKES = [
 "Saying iodine solution tests for proteins or fats; it tests only for <b>starch</b>.",
 "Writing that fibre gives energy; it helps the body remove waste but gives no energy.",
 "Mixing deficiency diseases: scurvy (C), rickets (D), night blindness (A), anaemia (iron), goitre (iodine).",
 "Writing 'balanced diet means eating a lot'; it means <b>all nutrients in the right amounts</b>.",
 "Thinking water is not a nutrient or that proteins are the main energy source (carbohydrates are).",
 "Believing all packaged food is healthy; check the label for fat, sugar and salt.",
]
