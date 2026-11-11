"""Class 10 Science Ch 5 Life Processes - extras."""
from common import AR4, Q

AR = [
 AR4(r"Guard cells control the opening and closing of stomata.", r"Guard cells swell when water flows into them, causing the stomatal pore to open.", "a",
     r"Turgid guard cells bulge apart and open the pore; shrunken ones close it."),
 AR4(r"Arteries have thick, elastic walls.", r"Veins have valves that prevent backflow of blood.", "b",
     r"Both true; arteries carry blood under high pressure (hence thick walls) while valves are a separate feature of veins."),
 AR4(r"In yeast, pyruvate is converted into ethanol and carbon dioxide in the absence of oxygen.", r"Anaerobic respiration releases more energy than aerobic respiration.", "c",
     r"Anaerobic breakdown is incomplete and releases much less energy than aerobic respiration; R is false."),
 AR4(r"Xylem carries the food prepared in the leaves to the other parts of the plant.", r"Translocation of food takes place through the phloem using energy.", "d",
     r"Xylem carries water and minerals; food is carried by phloem, so A is false and R is true."),
 AR4(r"The small intestine has a large surface area for absorption.", r"The inner lining of the small intestine has numerous finger-like projections called villi.", "a",
     r"Villi (rich in blood vessels) greatly increase the absorbing surface."),
 AR4(r"Filtration of blood in the kidney takes place in the glomerulus.", r"The ureter carries urine from the kidney to the urinary bladder.", "b",
     r"Both true but the second statement describes a different part of the excretory system."),
]

CASE = [
 Q(r"<b>Case study.</b> Meera had a lunch of chapatti, dal and a glass of milk. The food first entered her mouth, where it was mixed with saliva, and then passed through the oesophagus into the stomach and later into the small intestine. "
   r"(i) Name the enzyme in saliva that acts on chapatti. (ii) Name the acid secreted in the stomach. (iii) Where does the complete digestion of food take place? (iv) State the role of bile juice in the digestion of fat in milk and explain why the medium in the small intestine must be alkaline.",
   r"(i) Salivary amylase (1). (ii) Hydrochloric acid (1). (iii) Small intestine (1). (iv) Bile emulsifies fats, breaking large globules into smaller ones for the action of lipase (1); the pancreatic enzymes act only in an alkaline medium, so the acidic food from the stomach is made alkaline by bile (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> During a health check-up, a doctor measured the blood pressure of Mr Rao's grandson Arjun and recorded 120/80 mm of Hg. She explained that the human heart has four chambers and that oxygen-rich blood and oxygen-poor blood do not mix. "
   r"(i) How many chambers are there in the human heart? (ii) Name the vessel that brings oxygenated blood from the lungs to the heart. (iii) Name the instrument used to measure blood pressure. (iv) Why is it necessary to separate oxygenated and deoxygenated blood in birds and mammals?",
   r"(i) Four (1). (ii) Pulmonary vein (1). (iii) Sphygmomanometer (1). (iv) Birds and mammals need a high supply of oxygen as they have high energy needs and maintain constant body temperature (1); separation allows a highly efficient supply of oxygen to the body (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Mr Singh's kidneys stopped working properly, so he visits a hospital every week for haemodialysis. The machine contains a tube lined with a semi-permeable membrane and surrounded by a dialysing fluid. The fluid has the same osmotic pressure as blood but contains no nitrogenous waste. "
   r"(i) Name the structural and functional unit of the kidney. (ii) Name the tube that carries urine from the kidney to the urinary bladder. (iii) Name the nitrogenous waste mainly removed from the blood. (iv) Why does the dialysing fluid contain no nitrogenous waste and why is its osmotic pressure the same as blood?",
   r"(i) Nephron (1). (ii) Ureter (1). (iii) Urea (1). (iv) So that nitrogenous waste diffuses from the blood into the fluid along the concentration gradient (1); equal osmotic pressure prevents gain or loss of water by the blood (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Nutrition in plants", [r"Photosynthesis: $\ce{6CO2 + 6H2O ->[chlorophyll, sunlight] C6H12O6 + 6O2}$.",
   r"Steps: absorption of light by chlorophyll; conversion of light energy to chemical energy and splitting of water into $\ce{H2}$ and $\ce{O2}$; reduction of $\ce{CO2}$ to carbohydrates.",
   r"Gases enter/leave through stomata; guard cells open the pore when water flows in. Starch is tested with iodine (blue-black)."]),
 ("Human digestion", [r"Mouth: salivary amylase (starch $\rightarrow$ sugar). Stomach: HCl, pepsin (protein), mucus protects wall.",
   r"Liver: bile (emulsifies fats; alkaline). Pancreas: amylase, trypsin, lipase. Small intestine: complete digestion; villi absorb.",
   r"Heterotrophic modes: holozoic (humans, Amoeba), saprophytic (fungi), parasitic."]),
 ("Respiration", [r"Glucose $\xrightarrow{\text{cytoplasm}}$ pyruvate (3C) $\rightarrow$ (with $\ce{O2}$, mitochondria) $\ce{CO2 + H2O}$ + energy; ATP is the energy currency.",
   r"Anaerobic: yeast gives ethanol + $\ce{CO2}$ + energy; muscles give lactic acid (cramps) + energy.",
   r"Human lungs: nostril $\rightarrow$ pharynx $\rightarrow$ trachea $\rightarrow$ bronchi $\rightarrow$ alveoli (gas exchange); haemoglobin carries $\ce{O2}$; $\ce{CO2}$ is carried in dissolved form."]),
 ("Transportation", [r"Heart: 4 chambers (2 atria, 2 ventricles); double circulation; BP about 120/80 mm Hg (systolic/diastolic).",
   r"Arteries: thick walls, carry blood from heart; veins: thinner, valves, carry blood to heart; capillaries: exchange. Blood: plasma, RBC, WBC, platelets.",
   r"Plants: xylem (water, minerals; transpiration pull); phloem (food; translocation uses ATP)."]),
 ("Excretion", [r"Kidney: nephron = glomerulus + Bowman's capsule + tubule. Filtration $\rightarrow$ selective reabsorption $\rightarrow$ urine collected in pelvis $\rightarrow$ ureter $\rightarrow$ bladder $\rightarrow$ urethra.",
   r"Haemodialysis (artificial kidney) removes urea. Plants: excretion by fallen leaves, bark, gums, resins, transpiration."]),
]

MISTAKES = [
 r"Writing that plants respire only at night and photosynthesise only by day; plants respire all the time and photosynthesise in the presence of light.",
 r"Mixing up xylem and phloem: xylem carries water and minerals (one-way, upwards); phloem carries food (both directions).",
 r"Saying pulmonary artery carries oxygenated blood; the pulmonary <b>artery</b> carries deoxygenated blood to the lungs and the pulmonary <b>vein</b> carries oxygenated blood back.",
 r"Confusing breathing with respiration; breathing is gas exchange, respiration is the breakdown of glucose in cells to release energy.",
 r"Stating that pyruvate is formed in the mitochondria; glucose is broken down to pyruvate in the cytoplasm.",
 r"Believing the kidney makes urine only by filtration; selective reabsorption and the amount of water excreted are equally important steps.",
]
