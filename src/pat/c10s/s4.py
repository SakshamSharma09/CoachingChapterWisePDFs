from common import *
bio = dict(
 mcq=[
  mcq("Haemoglobin in red blood cells has a very high affinity for oxygen. In which organ do the red blood cells pick up the maximum amount of oxygen?", ["Kidney", "Lungs", "Liver", "Heart"], 'b', "Gas exchange in the alveoli of the lungs loads haemoglobin with oxygen."),
  mcq("Which of the following statements about guard cells is correct?", ["Water entering guard cells makes them swell and the stomatal pore opens", "Water leaving guard cells makes the stomatal pore open", "Guard cells are present only in roots", "Guard cells have no chloroplasts"], 'a', "Turgid guard cells bend apart and open the pore; flaccid ones close it."),
  mcq("Taste and smell are detected by gustatory and olfactory receptors. The impulses from these receptors are interpreted in the:", ["spinal cord", "cerebellum", "forebrain (cerebrum)", "medulla"], 'c', "Sensory information is analysed in the forebrain."),
  mcq("After a meal the blood sugar level of a healthy person rises. In response, the body releases the hormone:", ["glucagon from the liver", "insulin from the pancreas", "adrenaline from the adrenal gland", "thyroxine from the thyroid"], 'b', "Insulin lowers blood glucose by promoting its storage as glycogen."),
  mcq("In a mango flower, after fertilisation the part that develops into the seed is the:", ["ovary", "ovule", "style", "stigma"], 'b', "Ovule → seed, ovary → fruit."),
  mcq("Round yellow pea plants (RRYY) are crossed with wrinkled green plants (rryy) and the F₁ is self-pollinated. Out of 160 F₂ plants, the expected number of wrinkled yellow plants is:", ["10", "30", "90", "50"], 'b', "Wrinkled yellow (rrY_) form 3/16 of F₂: 3/16 × 160 = 30."),
  mcq("Which of the following represents a correct food chain of a pond ecosystem?", ["Algae → water flea → fish → heron", "Heron → fish → water flea → algae", "Fish → algae → heron → water flea", "Water flea → heron → algae → fish"], 'a', "A food chain starts with the producer and ends with the top consumer."),
 ],
 ar=[
  ar("Blood flows in only one direction through the human heart.", "Valves in the heart prevent the backward flow of blood.", 'a', "R explains the unidirectional flow."),
  ar("Thyroxine regulates the metabolism of carbohydrates, proteins and fats.", "Iodine is necessary for the synthesis of thyroxine.", 'b', "Both are true, but the need for iodine does not explain why thyroxine regulates metabolism."),
 ],
 s2=[
  sa("Distinguish between aerobic and anaerobic respiration on the basis of (i) the amount of energy released and (ii) the end products.", 2, "Aerobic: more energy (about 38 ATP per glucose); products CO₂ and water. Anaerobic: less energy (2 ATP); products ethanol + CO₂ (yeast) or lactic acid (muscles) (1 + 1)."),
  OR(sa("Name the hormones responsible for (i) controlling blood sugar and (ii) the changes seen in boys at puberty. State the glands that secrete them.", 2, "(i) Insulin – pancreas (1); (ii) testosterone – testes (1)."),
     sa("What is a feedback mechanism in hormone regulation? Explain with one example.", 2, "The timing and amount of hormone released is regulated by feedback; e.g. when blood sugar rises, insulin is released and when the sugar falls insulin secretion decreases (2).")),
  sa("State the 10% law. If the producers in an ecosystem receive 5000 J of energy, how much energy will be available to the secondary consumers?", 2, "Only 10% of the energy of one trophic level passes to the next (1). 5000 → 500 J (primary) → 50 J (secondary consumer) (1)."),
 ],
 s3=[
  sa("What are contraceptives? Explain any two different types of contraceptive methods and state one advantage of each.", 3, "Devices/methods to prevent pregnancy (1). e.g. mechanical barrier – condom (protects against STDs) (1); chemical – oral pills (high efficiency); surgical – vasectomy/tubectomy (permanent) (any two, 1)."),
  sa("How is the sex of a child determined in human beings? Explain with the help of a flow chart.", 3, "Male XY, female XX (½). Female gametes: all X; male gametes: X or Y (½). Flow chart: X + X → girl (XX); X + Y → boy (XY) (1½). The father’s sperm decides the sex (½)."),
 ],
 case=[case("In a school garden, students observe that the leaves of a ‘touch-me-not’ plant droop when touched, that the tendrils of a pea plant coil around a stick, and that the roots of a germinating seed grow downwards while the shoot grows upwards.",
   [sub("Name the type of movement shown by the tendrils of the pea plant.", 1, "Thigmotropism (growth movement in response to touch) (1)."),
    sub("Which of the movements observed is not dependent on growth?", 1, "Drooping of the touch-me-not leaves (1)."),
    OR(sub("Explain how a plant hormone causes the tendril to coil.", 2, "Auxin shifts to the side of the tendril away from the contact; cells on that side grow faster and the tendril coils around the support (2)."),
       sub("Name the tropic movement shown by roots and shoots and the hormone involved in the phototropic response.", 2, "Roots – positive geotropism, shoots – negative geotropism (1); auxin (1)."))])],
 d=[OR(sa("(i) Draw a labelled diagram of the human heart and trace the path of blood from the right atrium back to the right atrium. (ii) Why is the human heart four-chambered?", 5,
          "(i) Labelled diagram (2). Path: right atrium → right ventricle → pulmonary artery → lungs → pulmonary vein → left atrium → left ventricle → aorta → body → vena cava → right atrium (2). (ii) Separates oxygenated and deoxygenated blood, giving efficient supply for high energy needs (1)."),
       sa("(i) What is an ecosystem? Name its two components. (ii) How is ozone formed in the upper atmosphere? (iii) How do CFCs damage the ozone layer and why is this a concern?", 5,
          "(i) A self-sustaining unit of interacting living organisms (biotic) and the physical environment (abiotic) (1½). (ii) UV radiation splits O₂ into atoms; O + O₂ → O₃ (1½). (iii) CFCs release chlorine atoms which break down ozone; more UV reaches the earth, causing skin cancer and cataract (2)."))],
)
chem = dict(
 mcq=[
  mcq("Fat and oil containing foods become rancid on keeping for long. Which of the following can be added to prevent this?", ["a catalyst", "an antioxidant", "an acid", "a base"], 'b', "Antioxidants such as BHA/BHT prevent oxidation of fats."),
  mcq("The balanced form of the chemical equation Al + O₂ → Al₂O₃ is:", ["2Al + 3O₂ → Al₂O₃", "4Al + 3O₂ → 2Al₂O₃", "Al + O₂ → 2Al₂O₃", "2Al + O₂ → Al₂O₃"], 'b', "4Al + 3O₂ → 2Al₂O₃ has 4 Al and 6 O on each side."),
  mcq("A solution turns red litmus blue and has a pH of nearly:", ["2", "5", "7", "10"], 'd', "Basic solutions have pH > 7 and turn red litmus blue."),
  mcq("A student drops pieces of Mg, Zn, Fe and Cu in dilute HCl taken in four different test tubes. In which test tube would no bubbles be seen?", ["Mg", "Zn", "Fe", "Cu"], 'd', "Copper lies below hydrogen in the reactivity series."),
  mcq("The functional group present in ethanal (CH₃CHO) is:", ["alcohol (–OH)", "aldehyde (–CHO)", "ketone (>C=O)", "carboxylic acid (–COOH)"], 'b', "The –CHO group at the end of the chain is the aldehyde group."),
 ],
 ar=[ar("The blue colour of copper sulphate solution fades when an iron nail is dipped in it.", "Iron is more reactive than copper and displaces it from its salt solution.", 'a', "Fe + CuSO₄ → FeSO₄ + Cu.")],
 s2=[
  sa("What is observed when aqueous solutions of lead nitrate and potassium iodide are mixed? Write the balanced chemical equation and name the type of reaction.", 2, "A yellow precipitate of lead iodide forms (½). Pb(NO₃)₂ + 2KI → PbI₂↓ + 2KNO₃ (1); double displacement/precipitation reaction (½)."),
  sa("What happens when gypsum is heated at 373 K? Why should Plaster of Paris be stored in a moisture-proof container?", 2, "Gypsum loses water to form Plaster of Paris, CaSO₄·½H₂O (1). Moisture would convert it back to gypsum (CaSO₄·2H₂O) and it would set into a hard mass (1)."),
 ],
 s3=[
  OR(sa("What is an alloy? Name the alloys made of (i) copper and zinc, (ii) lead and tin. State one reason for making alloys.", 3, "A homogeneous mixture of two or more metals (or a metal and a non-metal) (1). Brass; solder (1). Alloys have improved properties such as strength, hardness, lower melting point or resistance to corrosion (1)."),
     sa("Write balanced chemical equations for the reactions of (i) iron with steam, (ii) calcium with cold water and (iii) magnesium with dilute HCl.", 3, "(i) 3Fe + 4H₂O → Fe₃O₄ + 4H₂ (1). (ii) Ca + 2H₂O → Ca(OH)₂ + H₂ (1). (iii) Mg + 2HCl → MgCl₂ + H₂ (1).")),
  sa("Write the name and formula of the main product formed when: (a) ethanol is heated with excess concentrated H₂SO₄ at 443 K, (b) ethanoic acid reacts with sodium hydroxide, (c) ethene reacts with hydrogen in the presence of nickel.", 3, "(a) Ethene, CH₂=CH₂ (1). (b) Sodium ethanoate, CH₃COONa (and water) (1). (c) Ethane, C₂H₆ (1)."),
 ],
 case=[case("Anil often feels a burning sensation in the stomach after a heavy meal. The doctor explains that the stomach produces hydrochloric acid of pH about 1.5 to 3.0, which helps in digestion, but excess acid causes acidity. He suggests a tablet containing magnesium hydroxide (milk of magnesia) as an antacid.",
   [sub("In what pH range is the acid present in the stomach? Is it strongly acidic or weakly acidic?", 1, "pH 1.5–3.0; strongly acidic (½ + ½)."),
    sub("Name the type of reaction between the antacid and the stomach acid.", 1, "Neutralisation (1)."),
    OR(sub("Write the balanced chemical equation for the reaction between magnesium hydroxide and hydrochloric acid.", 2, "Mg(OH)₂ + 2HCl → MgCl₂ + 2H₂O (2)."),
       sub("Why should an antacid not be a strong base such as sodium hydroxide? Name one other common antacid.", 2, "A strong base is corrosive and would damage the stomach lining (1); sodium hydrogencarbonate/aluminium hydroxide (1)."))])],
 d=[OR(sa("Describe the extraction of copper from copper glance (Cu₂S): write the chemical equations for roasting and for the reduction step, and describe the electrolytic refining of copper (anode, cathode and electrolyte).", 5,
          "Roasting: 2Cu₂S + 3O₂ → 2Cu₂O + 2SO₂ (1½). Reduction: 2Cu₂O + Cu₂S → 6Cu + SO₂ (1½). Refining: impure copper as anode, pure copper strip as cathode, acidified CuSO₄ as electrolyte; copper dissolves from the anode and is deposited at the cathode; impurities settle as anode mud (2)."),
       sa("(a) Draw the structures of the three isomers of pentane (C₅H₁₂) and name them. (b) Write the balanced equation for the combustion of methane. (c) What is a substitution reaction? Give the equation for the reaction of methane with chlorine in sunlight (first step).", 5,
          "(a) n-pentane, 2-methylbutane, 2,2-dimethylpropane with correct structures (3). (b) CH₄ + 2O₂ → CO₂ + 2H₂O + heat/light (½). (c) Replacement of an atom (H) by another atom (Cl) (½); CH₄ + Cl₂ → CH₃Cl + HCl (1)."))],
)
phy = dict(
 mcq=[
  mcq("A ray of light travelling in air is incident on the surface of a glass slab. At which angle of incidence will the ray pass into glass without any deviation?", ["0°", "30°", "45°", "90°"], 'a', "A ray along the normal (i = 0°) goes undeviated."),
  mcq("A concave mirror of focal length 10 cm forms an image of an object placed 15 cm from it, as shown. The image is:", ["real, inverted and magnified, at 30 cm from the mirror", "virtual, erect and magnified, behind the mirror", "real, inverted and diminished, at 7.5 cm", "real, inverted and of the same size, at 20 cm"], 'a', "1/v = −1/10 + 1/15 = −1/30 → v = −30 cm; m = −2.", fig=ray_mirror(15, 10)),
  mcq("When we move from bright sunlight into a dimly lit room we cannot see anything clearly at first, but after some time we start seeing. This is because:", ["the pupil dilates and allows more light to enter the eye", "the pupil contracts and allows less light to enter", "the eye lens becomes thinner", "the retina moves closer to the lens"], 'a', "The iris relaxes and widens the pupil in dim light."),
  mcq("Three resistors of 6 Ω, 3 Ω and 2 Ω are connected in parallel to a 6 V battery as shown. The total current drawn from the battery is:", ["1 A", "3 A", "6 A", "11 A"], 'c', "1/R = 1/6 + 1/3 + 1/2 = 1 → R = 1 Ω; I = 6/1 = 6 A.", fig=circuit('par3', ['R₁ = 6 Ω', 'R₂ = 3 Ω', 'R₃ = 2 Ω'], '6 V')),
 ],
 ar=[ar("Tungsten is used for making the filament of an electric bulb.", "Tungsten has a very high melting point.", 'a', "The filament gets white hot and must not melt.")],
 s2=[OR(sa("A lens has a focal length of −50 cm. Find its power and state its nature.", 2, "P = 1/f = 1/(−0.5 m) = −2 D (1); concave (diverging) lens (1)."),
        sa("Why is copper used for connecting wires, while an alloy like nichrome is used in heating devices?", 2, "Copper has very low resistivity, so little heat is produced in the wires (1). Nichrome has high resistivity and a high melting point and does not oxidise easily when red hot (1)."))],
 s3=[
  sa("Explain how a rainbow is formed in the sky. Under what conditions is it seen?", 3, "Tiny water droplets in the atmosphere act as small prisms: sunlight is refracted and dispersed on entering the droplet, internally reflected and refracted again as it leaves, giving a spectrum (2). Seen when the Sun is behind the observer and it is raining/water droplets are in front (1)."),
  sa("An electric iron of power 1.1 kW is operated on a 220 V supply for 2 hours every day. Calculate (a) the current drawn, (b) the energy consumed in 30 days and (c) the monthly bill at ₹6 per unit.", 3, "(a) I = P/V = 1100/220 = 5 A (1). (b) E = 1.1 × 2 × 30 = 66 kWh (1). (c) Bill = 66 × 6 = ₹396 (1)."),
  sa("What is meant by the magnetic field? State three properties of magnetic field lines.", 3, "The region around a magnet in which its influence can be detected (1). Properties: emerge from N and merge at S outside the magnet; closed curves; never intersect; closeness shows strength (any two, 1 each)."),
 ],
 case=[case("A dynamo fixed on the wheel of Gurpreet’s bicycle lights the lamp when the cycle moves. Inside the dynamo a small permanent magnet rotates near a coil of wire. He notices that the lamp glows brighter when he cycles faster and stops glowing when he stops.",
   [sub("Name the principle on which the dynamo works.", 1, "Electromagnetic induction (1)."),
    sub("What is the nature of the current produced by this dynamo, AC or DC? Justify.", 1, "AC; the polarity of the induced emf changes every half rotation as the magnet’s poles pass the coil (1)."),
    OR(sub("Why does the lamp glow brighter when the cycle moves faster?", 2, "The rate of change of the magnetic field through the coil increases, so the induced emf/current increases (2)."),
       sub("State Fleming’s right-hand rule and name the three fingers used.", 2, "Thumb, forefinger and middle finger mutually perpendicular: thumb – motion of the conductor, forefinger – magnetic field, middle finger – induced current (2)."))])],
 d=[OR(sa("A convex lens of focal length 12 cm forms an image of a 4 cm tall object placed 8 cm from the lens. Find the position, size and nature of the image and draw the ray diagram. Name one use of a lens in such a situation.", 5,
          "u = −8, f = +12: 1/v = 1/12 − 1/8 = −1/24 → v = −24 cm (1½). m = v/u = +3 (1); h′ = 12 cm (½). Virtual, erect, magnified, on the same side as the object (1). Ray diagram (½); use: magnifying glass/reading lens (½)."),
       sa("(a) Describe Faraday’s experiment that demonstrates electromagnetic induction using a coil and a bar magnet. (b) State the rule used to find the direction of the induced current. (c) Write two differences between AC and DC.", 5,
          "(a) When a bar magnet is pushed into/pulled out of a coil connected to a galvanometer, the needle deflects in opposite directions; no deflection if the magnet is at rest (2). (b) Fleming’s right-hand rule (1). (c) AC reverses direction periodically (50 Hz in India) and can be transmitted over long distances with less loss; DC flows in one direction (e.g. cells) (any two, 2)."))],
)
if __name__ == '__main__': go(4, bio, chem, phy); print('built 4')
