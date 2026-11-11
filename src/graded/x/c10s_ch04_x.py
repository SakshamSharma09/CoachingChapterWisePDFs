"""Class 10 Science Ch 4 Carbon and its Compounds - extras."""
from common import AR4, Q

AR = [
 AR4(r"Carbon forms a very large number of compounds.", r"Carbon is tetravalent and shows the property of catenation.", "a",
     r"Self-linking into long chains, branches and rings (catenation) together with four bonds per atom gives a huge number of compounds."),
 AR4(r"Ethanol is oxidised to ethanoic acid by alkaline potassium permanganate.", r"Acidified potassium dichromate is also an oxidising agent that converts ethanol to ethanoic acid.", "b",
     r"Both are true, but R is an additional fact about another oxidising agent and does not explain A."),
 AR4(r"Vegetable oils are hydrogenated using nickel catalyst to obtain saturated fats.", r"Hydrogenation converts the single bonds of unsaturated oils into double bonds.", "c",
     r"Hydrogen adds across the double bonds, converting them into single bonds; so R is false."),
 AR4(r"Diamond is a good conductor of electricity.", r"In diamond each carbon atom uses all four of its valence electrons to form bonds with four other carbon atoms.", "d",
     r"No free electrons are available in diamond, so it does not conduct; A is false, R is true."),
 AR4(r"Covalent compounds generally have low melting and boiling points.", r"The intermolecular forces in covalent compounds are weak.", "a",
     r"Little energy is needed to overcome weak intermolecular forces."),
 AR4(r"Esters have a sweet, fruity smell.", r"Esterification is the reaction of a carboxylic acid with an alcohol in the presence of an acid catalyst.", "b",
     r"Both true; R describes how esters are formed, not why they smell sweet."),
]

CASE = [
 Q(r"<b>Case study.</b> Alkanes form a homologous series with the general formula $\mathrm{C_nH_{2n+2}}$. The first member is methane, the second is ethane and the third is propane. The fourth member is butane and the fifth is pentane. "
   r"(i) Write the molecular formula of the alkane with five carbon atoms. (ii) Name the first member of the alkyne series. (iii) What is the difference in molecular mass between two consecutive members of a homologous series? (iv) Find the number of covalent bonds in propane and explain why propane is called a saturated compound.",
   r"(i) $\mathrm{C_5H_{12}}$ (pentane) (1). (ii) Ethyne, $\mathrm{C_2H_2}$ (1). (iii) 14 u (a $\mathrm{CH_2}$ unit) (1). (iv) Propane $\mathrm{C_3H_8}$ has $3n+1=10$ covalent bonds (1); all carbon-carbon bonds are single bonds, so each carbon holds the maximum number of hydrogen atoms (saturated) (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> In the school laboratory, Priya added a pinch of sodium hydrogencarbonate to a test tube containing ethanoic acid (vinegar-type acid) and observed brisk effervescence. In another test tube, her teacher warmed ethanoic acid with ethanol and a few drops of concentrated sulphuric acid and then poured the mixture into water; a sweet fruity smell was noticed. "
   r"(i) Name the gas evolved in the first test tube. (ii) How can the gas be tested? (iii) Name the organic product formed in the second test tube. (iv) Write the chemical equation for the second reaction and name the reaction.",
   r"(i) Carbon dioxide (1). (ii) It turns lime water milky (1). (iii) Ethyl ethanoate (an ester) (1). (iv) $\ce{CH3COOH + C2H5OH ->[conc. H2SO4] CH3COOC2H5 + H2O}$ (1); esterification (1).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Rohan washed a white shirt with bar soap in hard water and noticed a sticky white scum on the shirt. His mother then washed it with a detergent and it was cleaned without any scum. The teacher explained that soap molecules form spherical clusters in water that trap dirt. "
   r"(i) What is the white scum? (ii) Which part of a soap molecule is hydrophobic? (iii) Name the clusters formed by soap molecules in water. (iv) Why do detergents work in hard water while soaps do not?",
   r"(i) Calcium and magnesium salts of the fatty acids (insoluble) (1). (ii) The long hydrocarbon chain (tail) (1). (iii) Micelles (1). (iv) Calcium and magnesium salts of detergents (sodium salts of sulphonic acids or ammonium salts) are soluble in water (1), so no insoluble scum forms and the cleansing action is not reduced (1).", "1+1+1+2"),
]

FORMULAS = [
 ("Bonding in carbon", [r"Carbon: atomic number 6 (2, 4), tetravalent; forms covalent bonds by sharing electrons (does not form $\ce{C^{4+}}$ or $\ce{C^{4-}}$).",
   r"Covalent compounds: low melting/boiling points, poor conductors. Catenation: self-linking into chains, branches, rings.",
   r"Allotropes: diamond (hard, non-conductor), graphite (soft, conducts), fullerene $\ce{C60}$ (football-shaped)."]),
 ("Hydrocarbons and homologous series", [r"Alkanes $\mathrm{C_nH_{2n+2}}$ (single bonds): methane, ethane, propane, butane, pentane.",
   r"Alkenes $\mathrm{C_nH_{2n}}$ (double bond): ethene $\mathrm{C_2H_4}$; alkynes $\mathrm{C_nH_{2n-2}}$ (triple bond): ethyne $\mathrm{C_2H_2}$.",
   r"Covalent bonds in an alkane $= 3n+1$. Consecutive homologues differ by $\mathrm{CH_2}$ (14 u).",
   r"Functional groups: halo ($-$Cl, $-$Br), alcohol ($-$OH, -ol), aldehyde ($-$CHO, -al), ketone ($>$C=O, -one), carboxylic acid ($-$COOH, -oic acid)."]),
 ("Chemical properties", [r"Combustion: $\ce{CH4 + 2O2 -> CO2 + 2H2O}$ + heat and light; saturated burn with clean blue flame, unsaturated with yellow sooty flame.",
   r"Oxidation: alcohol $\xrightarrow{\text{alk. KMnO}_4 \text{ or acidified K}_2\text{Cr}_2\text{O}_7}$ carboxylic acid.",
   r"Addition (unsaturated, Ni catalyst): $\ce{CH2=CH2 + H2 -> CH3-CH3}$. Substitution (saturated, sunlight): $\ce{CH4 + Cl2 -> CH3Cl + HCl}$."]),
 ("Ethanol and ethanoic acid", [r"$\ce{2Na + 2C2H5OH -> 2C2H5ONa + H2}$; dehydration: $\ce{CH3CH2OH ->[conc. H2SO4, 443 K] CH2=CH2 + H2O}$.",
   r"$\ce{CH3COOH + NaOH -> CH3COONa + H2O}$; $\ce{2CH3COOH + Na2CO3 -> 2CH3COONa + H2O + CO2}$.",
   r"Esterification: acid + alcohol $\xrightarrow{\text{conc. H}_2\text{SO}_4}$ ester + water. Saponification: ester + NaOH $\rightarrow$ alcohol + sodium salt of acid (soap).",
   r"Vinegar: 5-8% ethanoic acid; pure ethanoic acid freezes at 290 K (glacial acetic acid)."]),
 ("Soaps and detergents", [r"Soap: sodium/potassium salt of long-chain fatty acid; ionic head (hydrophilic) + hydrocarbon tail (hydrophobic) $\rightarrow$ micelles trap oily dirt.",
   r"Hard water ($\ce{Ca^{2+}}$, $\ce{Mg^{2+}}$) + soap $\rightarrow$ insoluble scum; detergents (sulphonate / ammonium salts) do not form scum."]),
]

MISTAKES = [
 r"Counting covalent bonds wrongly: an alkane $\mathrm{C_nH_{2n+2}}$ has $3n+1$ bonds (include all C-H and C-C bonds).",
 r"Confusing ethanol and ethanoic acid: ethanol ($\ce{C2H5OH}$) is an alcohol, ethanoic acid ($\ce{CH3COOH}$) releases $\ce{CO2}$ with carbonates; ethanol does not.",
 r"Naming the chain from the wrong carbon count, e.g. calling $\ce{CH3CH2CHO}$ 'propanol' instead of propanal; the suffix comes from the functional group (-ol, -al, -one, -oic acid).",
 r"Writing an addition reaction for a saturated hydrocarbon; saturated compounds undergo substitution, unsaturated ones undergo addition.",
 r"Saying that detergents form micelles but soaps do not, or that soap works well in hard water; soaps give scum in hard water.",
 r"Stating that diamond and graphite conduct electricity; only graphite does (it has free electrons).",
]
