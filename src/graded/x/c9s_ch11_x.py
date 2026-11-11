"""Class 9 Science Ch 11 Patterns in Life: Diversity and Classification - extras."""
from common import AR4, Q

AR = [
 AR4("The species is the basic unit of classification.", "Members of a species can interbreed to produce fertile offspring.", "a",
     "Interbreeding with fertile offspring is the defining feature of a species."),
 AR4("The scientific name of the human being is <i>Homo sapiens</i>.", "In binomial nomenclature the first word is the genus (beginning with a capital letter) and the second word is the species (beginning with a small letter).", "b",
     "Both are true; R states the rule of writing but does not explain why the human name is <i>Homo sapiens</i>."),
 AR4("Birds and mammals are warm-blooded animals.", "All vertebrates are warm-blooded.", "c",
     "Fish, amphibians and reptiles are vertebrates but are cold-blooded, so R is false."),
 AR4("Fungi are autotrophs.", "The cell wall of fungi is made of chitin.", "d",
     "Fungi lack chlorophyll and are heterotrophs, so A is false; R is true."),
 AR4("Mushrooms are not classified as plants.", "Fungi lack chlorophyll and feed on dead organic matter (saprotrophic nutrition).", "a",
     "Plants are autotrophs with cellulose walls; fungi differ in nutrition and cell wall, so they form a separate kingdom."),
 AR4("Fish have a two-chambered heart.", "Fish are cold-blooded animals.", "b",
     "Both are true but one does not explain the other."),
]

CASE = [
 Q("<b>Case study.</b> A botany teacher in Lucknow writes the scientific names of three organisms on the board: mango, <i>Mangifera indica</i>; neem, <i>Azadirachta indica</i>; and tiger, <i>Panthera tigris</i>. "
   "(i) Name the genus of the mango. (ii) Name the species of the tiger. (iii) Mango and neem both have the species name <i>indica</i>. Are they the same species? (iv) Write the name of the tiger correctly according to the rules and give one reason why scientific names are preferred to common names.",
   "(i) <i>Mangifera</i> (1). (ii) <i>tigris</i> (1). (iii) No; the species name alone is not enough, they belong to different genera (1). (iv) <i>Panthera tigris</i>: genus begins with a capital letter, species with a small letter, and the name is in italics or underlined separately (1); scientific names are the same worldwide and avoid confusion caused by many local names (1).", "1+1+1+2"),
 Q("<b>Case study.</b> A student notes the features of three animals. Animal P has a backbone, a four-chambered heart, hair on the body and mammary glands. Animal Q has feathers, forelimbs modified into wings and lays eggs with hard shells. Animal R has moist skin without scales, lays eggs in water and its young stage breathes through gills. "
   "(i) Identify the class of P. (ii) Identify the class of Q. (iii) Identify the class of R. (iv) A bat flies like a bird but is classed with P. Give two reasons.",
   "(i) Mammalia (mammal) (1). (ii) Aves (bird) (1). (iii) Amphibia (amphibian) (1). (iv) A bat has hair or fur on the body (1) and has mammary glands and gives birth to young ones (any two points) (1).", "1+1+1+2"),
 Q("<b>Case study.</b> During a nature walk in the Western Ghats, Divya collects a moss, a fern, a pine cone, a rose flower and a mushroom. She is asked to classify them. "
   "(i) Name the group to which the moss belongs. (ii) Which specimen bears seeds that are not enclosed in a fruit? (iii) Which specimen is an angiosperm? (iv) Why is the mushroom not placed with the plants?",
   "(i) Bryophytes (1). (ii) Pine (a gymnosperm) (1). (iii) Rose (1). (iv) The mushroom is a fungus: it has no chlorophyll and cannot make its own food (1), it feeds on dead matter and its cell wall is made of chitin, not cellulose (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Classification and nomenclature", ["Taxonomic hierarchy (highest to lowest): Kingdom $\\rightarrow$ Phylum (Division in plants) $\\rightarrow$ Class $\\rightarrow$ Order $\\rightarrow$ Family $\\rightarrow$ Genus $\\rightarrow$ Species.",
   "Species: group of organisms that can interbreed and produce fertile offspring. Biodiversity: variety of living organisms.",
   "Binomial nomenclature (Linnaeus): genus (capital first letter) + species (small letter), italics or underlined separately, e.g. <i>Homo sapiens</i>, <i>Mangifera indica</i>."]),
 ("Five kingdoms", ["Monera: bacteria; unicellular, prokaryotic. Protista: unicellular eukaryotes (<i>Amoeba</i>, <i>Paramecium</i>).",
   "Fungi: heterotrophic, chitin cell wall, saprotrophic (mushroom, yeast, bread mould); lichens: association of an alga and a fungus.",
   "Plantae: multicellular autotrophs with cellulose walls. Animalia: multicellular heterotrophs without cell walls."]),
 ("Plant groups", ["Thallophytes (algae): no differentiated body. Bryophytes: mosses, need water for fertilisation. Pteridophytes: ferns, vascular, no seeds.",
   "Gymnosperms: naked seeds (pine, cycas). Angiosperms: flowering plants, seeds in fruits; monocots (one cotyledon) and dicots (two cotyledons)."]),
 ("Animal phyla", ["Porifera (sponges, pores), Cnidaria (<i>Hydra</i>, stinging cells), Platyhelminthes (flatworms, tapeworm), Nematoda (roundworms).",
   "Annelida (earthworm, segmented), Arthropoda (jointed legs, insects, spiders, crabs; the largest phylum), Mollusca (snail, octopus), Echinodermata (starfish, spiny skin).",
   "Chordata: notochord and backbone."]),
 ("Vertebrate classes", ["Pisces: gills, two-chambered heart, cold-blooded. Amphibia: moist skin, three-chambered heart. Reptilia: scales, lay eggs on land, three-chambered heart (crocodile has four).",
   "Aves: feathers, wings, warm-blooded, four-chambered heart. Mammalia: hair, mammary glands, mostly give birth to young, four-chambered heart, warm-blooded."]),
]

MISTAKES = [
 "Writing scientific names wrongly: <i>homo Sapiens</i> or <i>Homo Sapiens</i>; the genus has a capital letter, the species a small letter, and both are italicised or underlined separately.",
 "Treating the kingdom as the smallest group and the species as the largest; the hierarchy runs from kingdom (largest) to species (smallest).",
 "Putting fungi (mushroom, yeast) in the plant kingdom; they lack chlorophyll and have chitin in their cell wall.",
 "Mixing up gymnosperms (naked seeds) and angiosperms (seeds enclosed in fruits), or monocots and dicots (one or two cotyledons).",
 "Saying that all vertebrates are warm-blooded, or that bats (mammals) are birds because they fly.",
 "Mixing up the phyla: spiders and insects are arthropods, earthworms are annelids, and roundworms are nematodes; also confusing 'Annelida' (segmented) with 'Nematoda' (unsegmented).",
]
