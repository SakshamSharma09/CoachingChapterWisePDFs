"""Class 8 Science Ch 2 Invisible Living World - extras."""
from common import AR4, Q

AR = [
 AR4("Robert Hooke used the name 'cells' for the box-like compartments he saw in a thin slice of cork.", "Cork is made of dead cells whose walls remain as empty compartments.", "a", "The compartments he saw were the walls of dead plant cells, which is why they looked like small rooms."),
 AR4("Plant cells have a definite shape.", "Plant cells have a rigid cell wall outside the cell membrane.", "a", "The cell wall gives the plant cell its fixed shape."),
 AR4("Animal cells have chloroplasts.", "Chloroplasts contain chlorophyll and carry out photosynthesis.", "d", "Animal cells do not have chloroplasts, so A is false; R is true."),
 AR4("An onion peel is stained before observing it under a microscope.", "A stain makes the transparent parts of the cell easier to see.", "a", "Most cell parts are nearly colourless; the stain provides contrast."),
 AR4("Bacteria are prokaryotic organisms.", "Bacteria are single-celled organisms.", "b", "Both true, but being single-celled does not make them prokaryotic; the lack of a membrane-bound nucleus does."),
 AR4("The nucleus of a cell controls its activities.", "The nucleus is present in every living cell without exception.", "c", "A is true; R is false because bacterial cells have no true nucleus."),
]

CASE = [
 Q("<b>Case study.</b> In the school laboratory, Kavya peels a thin layer from an onion, places it on a slide, adds a drop of safranin stain and a cover slip, and observes it under a compound microscope. She sees rectangular cells arranged closely, each with a dark round spot near the edge. "
   "(i) Why is the peel kept thin? (ii) Name the dark round structure. (iii) Name the outer rigid layer that gives the rectangular shape. (iv) She then scrapes cells from the inside of her cheek. Name two differences she would see compared with onion cells.",
   "(i) A thin peel lets light pass through so one layer of cells can be seen (1). (ii) Nucleus (1). (iii) Cell wall (1). (iv) Cheek cells have no cell wall and are irregular/rounded in shape, and have no large central vacuole (any two) (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A teacher compares three living things: an amoeba in pond water, a human and a mango tree. She explains that an amoeba is a single cell that eats, moves and reproduces on its own, whereas a human is made of trillions of cells that work together. "
   "(i) What is the basic structural and functional unit of life? (ii) Give the term for an organism made of one cell. (iii) Give the term for an organism made of many cells. (iv) Why do multicellular organisms need cells of different kinds?",
   "(i) The cell (1). (ii) Unicellular (1). (iii) Multicellular (1). (iv) Different cells are specialised for different jobs (e.g. nerve cells, muscle cells), so division of work makes the organism function efficiently (2).", "1+1+1+2"),
 Q("<b>Case study.</b> A microscope has an eyepiece lens of magnification 10x and an objective lens of 40x. Arjun views a red blood cell of diameter about 7 micrometres, a bacterium of about 2 micrometres, and tries to see a virus of about 0.1 micrometre. He can see the first two but the virus cannot be seen clearly. "
   "(i) Find the total magnification of the microscope. (ii) Which is the largest of the three? (iii) Name a part of a plant cell that stores water and dissolved substances. (iv) Why can the virus not be seen clearly with this microscope?",
   "(i) 10 x 40 = 400 times (1). (ii) The red blood cell (1). (iii) Vacuole (1). (iv) A virus is far smaller than a bacterium and is below the limit of a light microscope; a much more powerful electron microscope is needed (2).", "1+1+1+2"),
]

FORMULAS = [
 ("Cell basics", ["The cell is the basic structural and functional unit of living organisms.", "Robert Hooke (1665) named cells in cork; Leeuwenhoek observed living microorganisms.",
   "Unicellular: one cell (amoeba, bacteria). Multicellular: many cells (humans, trees)."]),
 ("Parts of a cell and functions", ["Cell membrane: selectively permeable, controls entry and exit.", "Cytoplasm: jelly-like fluid where cell activities take place.",
   "Nucleus: controls cell activities; holds genetic material.", "Cell wall (plants, fungi, bacteria): rigid, gives shape and protection.",
   "Chloroplast (plants): contains chlorophyll, site of photosynthesis.", "Vacuole: stores water and dissolved substances (large and central in plants)."]),
 ("Plant cell vs animal cell", ["Plant: cell wall, chloroplasts, large central vacuole, fixed shape.", "Animal: no cell wall or chloroplasts, small vacuoles, irregular shape."]),
 ("Microscope and sizes", [r"Total magnification $=$ magnification of eyepiece $\times$ magnification of objective.", r"1 millimetre $=1000$ micrometres.",
   "Prokaryotes (bacteria): no true nucleus; eukaryotes: true nucleus.", "Slide preparation: thin peel, stain (iodine/safranin), cover slip."]),
]

MISTAKES = [
 "Saying that animal cells also have a cell wall or chloroplasts.",
 "Confusing the <b>cell wall</b> (outer, rigid, plants) with the <b>cell membrane</b> (inside the wall, in all cells).",
 "Believing cork contains living cells, when Hooke saw the walls of dead cells.",
 "Calculating total magnification by adding the lens powers instead of multiplying.",
 "Writing that all cells have a nucleus; bacteria have no true nucleus.",
 "Forgetting the stain, thin peel and cover slip when describing slide preparation.",
]
