"""Class 9 Science Ch 9 Cell: The Building Block of Life - extras."""
from common import AR4, Q

AR = [
 AR4("Mitochondria are called the powerhouses of the cell.", "They release energy from food through cellular respiration and store it in the form of ATP.", "a",
     "ATP is the energy currency of the cell, which is why mitochondria are called powerhouses."),
 AR4("Plant cells have a cell wall, but animal cells do not.", "The plant cell wall is made mainly of cellulose.", "b",
     "Both are true, but the composition of the wall does not explain why animal cells lack it."),
 AR4("Ribosomes are the sites of protein synthesis.", "Ribosomes are enclosed by a double membrane.", "c",
     "Ribosomes are non-membrane-bound particles, so R is false."),
 AR4("A bacterial cell has a well-defined nucleus surrounded by a nuclear membrane.", "Bacteria are prokaryotes.", "d",
     "Prokaryotic cells have no nuclear membrane; their DNA lies free in the cytoplasm, so A is false."),
 AR4("A plant cell placed in a hypotonic solution swells but does not burst.", "The rigid cell wall resists the expansion of the cell.", "a",
     "Water enters by osmosis, and the wall prevents bursting."),
 AR4("Chloroplasts carry out photosynthesis in green plant cells.", "Lysosomes contain digestive enzymes and are called the suicide bags of the cell.", "b",
     "Both are true, but they describe different organelles."),
]

CASE = [
 Q("<b>Case study.</b> Anil keeps dried raisins in plain water overnight and finds them swollen next morning. He also weighs two equal potato strips of 100 g each: one kept in a 10 per cent salt solution weighs 90 g after an hour, and the other kept in distilled water weighs 112 g. "
   "(i) Define osmosis. (ii) Why do the raisins swell? (iii) Which strip is in the hypertonic solution? (iv) Find the percentage change in mass of each strip and explain the result.",
   r"(i) Osmosis is the movement of water molecules through a selectively permeable membrane from a region of higher water concentration to a region of lower water concentration (1). (ii) Water enters the raisin cells by osmosis because the surrounding water is hypotonic to the cell contents (1). (iii) The strip in the salt solution (1). (iv) Salt solution: $-10\%$ (loses water); distilled water: $+12\%$ (gains water) (1); the cell loses water in a hypertonic medium and gains water in a hypotonic medium (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Aarti studies cells from the pancreas, which secrete large amounts of digestive enzymes, and from a green leaf, using a microscope. She notes the following organelles: nucleus, mitochondria, rough endoplasmic reticulum, Golgi apparatus, chloroplast and a large central vacuole. "
   "(i) Which organelle controls the activities of the cell? (ii) Which organelle is the site of ATP production? (iii) Which two of the listed structures are present in the leaf cell but not in the pancreatic cell? (iv) Which organelles would be especially well developed in an enzyme-secreting cell, and why?",
   "(i) Nucleus (1). (ii) Mitochondria (1). (iii) Chloroplast and the large central vacuole (and cell wall) (1). (iv) Rough endoplasmic reticulum (has ribosomes that make proteins) and the Golgi apparatus (1) which modify, package and dispatch them (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A student examines two slides. Slide P shows a cell with a cell wall, ribosomes and DNA lying free in the cytoplasm, with no nuclear membrane. Slide Q shows a cell with a nuclear membrane, mitochondria and an endoplasmic reticulum. "
   "(i) Which slide shows a prokaryotic cell? (ii) Which slide shows a eukaryotic cell? (iii) Give one example of each type of organism. (iv) State two differences between the two types of cells.",
   "(i) Slide P (1). (ii) Slide Q (1). (iii) Prokaryote: bacterium (e.g. <i>E. coli</i>); eukaryote: onion plant, human, yeast, Amoeba (1). (iv) Any two: prokaryotes have no nuclear membrane, eukaryotes have; prokaryotes have no membrane-bound organelles, eukaryotes do; prokaryotes are generally much smaller (1+1).", "1+1+1+2"),
]

FORMULAS = [
 ("Cell theory", ["Schleiden and Schwann: all plants and animals are made of cells; the cell is the basic unit of life. Virchow: new cells arise from pre-existing cells.",
   "Robert Hooke observed and named cells in cork (1665). Unicellular organisms: <i>Amoeba</i>, <i>Paramecium</i>, bacteria. Multicellular organisms: plants, animals."]),
 ("Prokaryotic and eukaryotic cells", ["Prokaryotic: no true nucleus (no nuclear membrane), DNA free in the cytoplasm, no membrane-bound organelles (bacteria).",
   "Eukaryotic: true nucleus with nuclear membrane, membrane-bound organelles (plants, animals, fungi, protists).",
   "Sizes: $1\\text{ }\\mu\\text{m}=10^{-6}\\text{ m}$; bacteria about 1 to 10 $\\mu$m; the human egg cell is about 100 $\\mu$m."]),
 ("Cell structures and functions", ["Cell membrane: selectively permeable, controls entry and exit. Cell wall (plants, fungi, bacteria): rigid, protective; cellulose in plants.",
   "Nucleus: control centre, holds DNA (chromosomes). Cytoplasm: jelly-like medium. Ribosomes: protein synthesis.",
   "Rough ER: protein synthesis and transport; smooth ER: lipid synthesis and detoxification. Golgi apparatus: modifies, packs and dispatches materials.",
   "Mitochondria: respiration, ATP production. Chloroplasts (plastids): photosynthesis, contain chlorophyll. Lysosomes: digestion, 'suicide bags'. Vacuoles: storage, turgidity."]),
 ("Transport across the membrane", ["Diffusion: movement of molecules from higher to lower concentration. Osmosis: diffusion of water through a selectively permeable membrane.",
   "Hypotonic medium: cell gains water and swells. Hypertonic medium: cell loses water and shrinks (plasmolysis). Isotonic: no net movement of water."]),
 ("Plant cell vs animal cell", ["Plant cell: cell wall, chloroplasts, large central vacuole. Animal cell: no cell wall or chloroplast, small vacuoles, centrioles.",
   "Mass change in osmosis (per cent) $=\\dfrac{\\text{final mass}-\\text{initial mass}}{\\text{initial mass}}\\times100$."]),
]

MISTAKES = [
 "Saying that bacteria have a nucleus, or that prokaryotes have no genetic material; the DNA is present but is not enclosed in a nuclear membrane.",
 "Mixing up hypotonic and hypertonic: in a <i>hypotonic</i> outside solution the cell swells, in a <i>hypertonic</i> one it shrinks.",
 "Calling osmosis the movement of any solute; osmosis is the movement of <i>water</i> through a selectively permeable membrane.",
 "Confusing the functions of rough ER (protein synthesis, studded with ribosomes) and smooth ER (lipids, detoxification), or saying that mitochondria 'make' energy; they release energy from food as ATP.",
 "Saying that the cell wall and cell membrane are the same; the membrane is selectively permeable and present in all cells, the wall is rigid and fully permeable.",
 "Forgetting that plant cells do not burst in water because of the cell wall, whereas an animal cell like RBC can swell and burst.",
]
