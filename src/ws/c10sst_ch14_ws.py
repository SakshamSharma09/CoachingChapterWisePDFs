"""Class 10 Social Science Ch 14 - Federalism (Political Science Ch 2): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch14"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)
AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def ar(a, r, i, why, lvl="E"):
    return W(f"Assertion (A): {a}  Reason (R): {r}  Choose the correct option.", 1, f"({'abcd'[i]}) {AR[i]}. {why}", lvl, opts=AR)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("Which of these is a 'coming together' federation?", ["India", "Spain", "United States of America", "Belgium"], 2, "Independent states came together to form a bigger unit."),
mc("Subjects such as defence, foreign affairs, banking and currency are in the:", ["State List", "Union List", "Concurrent List", "Residuary List"], 1),
mc("Subjects such as police, trade, commerce, agriculture and irrigation are in the:", ["Union List", "State List", "Concurrent List", "Residuary List"], 1),
mc("In case of a conflict between a Union law and a State law on a Concurrent subject, which law prevails?", ["State law", "Union law", "The law passed earlier", "The Supreme Court decides each time with no rule"], 1),
mc("Who has the power to legislate on residuary subjects such as computer software?", ["The State governments", "The Union Government", "Panchayats", "The Election Commission"], 1),
mc("The institution that conducts panchayat and municipal elections in a state is the:", ["Election Commission of India", "State Election Commission", "Supreme Court", "Gram Sabha"], 1),
mc("The body of all the voters in a village is called the:", ["Gram Panchayat", "Gram Sabha", "Panchayat Samiti", "Zilla Parishad"], 1),
mc("In India, which language is the official language of the Union, with English also used?", ["Sanskrit", "Hindi", "Tamil", "Urdu"], 1, "Hindi is the mother tongue of only about 40 per cent of Indians."),
W("Define federalism.", 2,
  "Federalism is a system of government in which power is divided between a central authority and various constituent units of the country (2).", "E"),
W("Name the three lists in the distribution of legislative powers between the Union and the States.", 1, "Union List, State List and Concurrent List. (1)", "E"),
W("How many countries of the world have a federal system and what share of the world's population lives in them?", 2,
  "25 of the world's 193 countries have federal political systems (1). Their citizens make up about 40 per cent of the world's population (1).", "E"),
W("Name any two Union Territories of India.", 1, "Any two of Chandigarh, Lakshadweep, Delhi (the capital city) (also Puducherry etc.). (1)", "E"),
W("True or false (with a reason): 'The Constitution of India gave the status of national language to Hindi.'", 2,
  "False (1). The Constitution did not give the status of national language to any one language; Hindi was identified as the official language, and there are 21 other Scheduled Languages (1).", "E"),
W("Match: (i) Panchayat Samiti (ii) Municipal Corporation (iii) Gram Panchayat (iv) Zilla Parishad.  A. Headed by a Mayor  B. Sarpanch  C. Block or mandal  D. District level.", 2,
  "(i)-C, (ii)-A, (iii)-B, (iv)-D. (all four = 2; two or three correct = 1)", "E"),
W("Which Amendment in 1992 made local government more powerful? State two of its provisions.", 2,
  "The 1992 amendment (73rd and 74th) made the third tier of democracy more powerful (0.5). Any two: regular elections are mandatory; seats reserved for SC, ST and OBC; at least one-third positions reserved for women; State Election Commission; sharing of powers and revenue by the state (1.5).", "E"),
W("What does the Constitution say about a change in the power-sharing arrangement between the Union and the States?", 2,
  "Any change must first be passed by both Houses of Parliament with at least two-thirds majority (1) and then ratified by the legislatures of at least half of the total States (1).", "E"),
W("Name any two states created on the basis of culture, ethnicity or geography rather than language.", 1, "Any two of Nagaland, Uttarakhand, Jharkhand. (1)", "E"),
# ------------------------------------------------------------------ MEDIUM (20)
ar("The Constitution of India provides for a federal system.", "The powers of the Union and the State governments are specified in the Constitution and the courts can settle disputes between them.", 0, "Clear division of powers and an umpire are features of federalism.", "M"),
ar("Linguistic states have made India more united.", "People speaking the same language live within one state, making administration easier.", 0, "Experience showed that fears of splitting the country were not borne out.", "M"),
W("Write any three key features of federalism.", 3,
  "Two or more levels of government (1). Each level has its own jurisdiction in legislation, taxation and administration, specified in the Constitution (1). Fundamental provisions cannot be changed by one level alone and courts interpret the Constitution and act as umpire (1). Sources of revenue for each level are clearly specified, ensuring financial autonomy; dual objective of unity and regional diversity (1). (any three)", "M"),
W("Differentiate between 'coming together' and 'holding together' federations with an example each.", 3,
  "Coming together: independent States come together on their own to form a bigger unit and retain identity; States have equal powers and are strong; e.g. USA, Switzerland, Australia (1.5). Holding together: a large country divides its power between the national government and States; the Centre is more powerful and units may have unequal powers; e.g. India, Spain, Belgium (1.5).", "M"),
W("Distinguish between a unitary and a federal system.", 3,
  "Unitary: one level of government, or sub-units subordinate to the centre; the central government can pass orders to provincial governments; example: Sri Lanka in practice (1.5). Federal: two or more levels, each with its own powers; the central government cannot order the state governments; example: India, USA (1.5).", "M"),
W("Explain the three lists with two examples of each.", 3,
  "Union List: defence, foreign affairs, banking, communications, currency; only the Union can legislate (1). State List: police, trade, commerce, agriculture, irrigation; only States legislate (1). Concurrent List: education, forest, trade unions, marriage, adoption and succession; both legislate, and the Union law prevails in case of conflict (1).", "M"),
W("Why is the Union Government empowered to legislate on residuary subjects? Give an example.", 2,
  "Subjects that do not fall in any of the three lists, or which came up after the Constitution was made, need a clear authority to legislate (1). Union has this power; example: computer software (1).", "M"),
W("'All States in the Indian Union do not have identical powers.' Explain with examples.", 3,
  "India is a holding together federation, in which the Centre tends to be more powerful and units may have unequal powers (1). Some States such as Assam, Nagaland, Arunachal Pradesh and Mizoram enjoy special powers under certain provisions (Article 371) due to peculiar social and historical circumstances (1). Union Territories like Delhi, Chandigarh and Lakshadweep do not have the powers of a State and the Centre runs them with special powers (1).", "M"),
W("Describe how the creation of linguistic states strengthened Indian federalism.", 3,
  "After 1947 several old state boundaries were changed so that people speaking the same language lived in the same state (1). Some leaders feared the country would split, but experience showed that linguistic states made the country more united and administration easier (1). Later states were also formed on the basis of culture, ethnicity or geography, such as Nagaland, Uttarakhand and Jharkhand (1).", "M"),
W("Explain India's language policy in three points.", 3,
  "The Constitution did not give the status of national language to any one language (1). Hindi was identified as the official language, though it is the mother tongue of only about 40 per cent of Indians; 21 other languages are recognised as Scheduled Languages (1). English continues to be used along with Hindi for official purposes; central leaders were careful not to impose Hindi (1).", "M"),
W("What happened in Tamil Nadu on the language issue? How did the Union Government respond?", 2,
  "The use of English for official purposes was to stop in 1965, but many non-Hindi States demanded that it continue; in Tamil Nadu the movement took a violent form (1). The Central Government agreed to continue the use of English along with Hindi (1).", "M"),
W("How did coalition governments after 1990 make Indian federalism more effective?", 3,
  "Earlier, the same party ruling the Centre and most States undermined State autonomy and often misused the Constitution to dismiss rival governments (1). After 1990 regional parties rose and no single party won a clear majority in the Lok Sabha, so national parties had to form alliances with regional parties (1). A major Supreme Court judgement also made arbitrary dismissal of State governments difficult, so power sharing became real (1).", "M"),
W("What is decentralisation? Why is it needed in a country like India? Give two reasons.", 3,
  "Taking power from Central and State governments and giving it to local government is decentralisation (1). Many problems are best settled at the local level and people have better knowledge of local issues (1). States are as large as European countries and are internally diverse, so a third tier is needed to share power below the State (1).", "M"),
W("Describe the structure of rural local government.", 3,
  "Each village or group of villages has a Gram Panchayat consisting of ward members (panch) and a president (sarpanch), elected by adult voters, working under the Gram Sabha, which is the body of all voters (1). A few gram panchayats form a Panchayat Samiti (block or mandal) (1). All the Panchayat Samitis in a district together form the Zilla Parishad, whose chairperson is the political head (1).", "M"),
W("Describe urban local government and name its heads.", 2,
  "Municipalities are set up in towns and Municipal Corporations in big cities, controlled by elected bodies of people's representatives (1). The political head of a municipality is the municipal chairperson and of a municipal corporation the Mayor (1).", "M"),
W("Give two benefits and one limitation of local government in India.", 3,
  "Benefits: people can directly participate and decisions are made nearer to them; people have better knowledge of local problems (2). Limitation: many State governments have not transferred sufficient powers and revenue to local bodies (1).", "M"),
W("Map-based. Name three states carved out of bigger states and the state they were carved out of, if known.", 3,
  "Examples (any three): Uttarakhand (from Uttar Pradesh), Jharkhand (from Bihar), Chhattisgarh (from Madhya Pradesh), Telangana (from Andhra Pradesh), Gujarat (from Bombay State) (3, 1 each).", "M"),
W("A village panchayat in Rajasthan has 15 seats of which one-third must go to women. (i) How many seats are reserved for women? (ii) How many remain open to all?", 2,
  "(i) One-third of 15 = 5 seats for women (1). (ii) 15 - 5 = 10 seats remain open (1).", "M", wp=True),
W("Error analysis. A student writes: 'In a federal country the central government can order the state governments to do anything because it is stronger.' Correct the statement.", 2,
  "In a federal system the central government cannot order the state governments to do something; the states have powers of their own (1). Both are independent in their own sphere and both derive their power from the Constitution (1).", "M"),
W("Why does the Constitution not allow changes to the power-sharing arrangement by Parliament alone?", 2,
  "The fundamental provisions cannot be unilaterally changed by one level of government (1). A change needs two-thirds majority in both Houses and ratification by at least half of the State legislatures, so that the States also have a say (1).", "M"),
W("Study the table. Subject: Education - Concurrent; Police - State; Currency - Union; Marriage - Concurrent. Suppose the Union passes a law on marriage that differs from a State's law. Which law applies and why? Could the State ignore the Union law on currency?", 3,
  "Marriage is on the Concurrent List, so both can legislate, but in case of conflict the Union law prevails (1.5). Currency is a Union subject only, so States cannot make their own law, and cannot ignore the Union law (1.5).", "M", wp=True),
# ------------------------------------------------------------------ HARD (13)
W("Compare federal power sharing in Belgium and India under four heads: type of federation, status of units, regional governments, special arrangement.", 4,
  "Both are holding together federations in which a large unit divides power (1). In India, the Centre is more powerful and States have unequal powers; in Belgium the central government gave a large part of its power to regional governments, and State governments are not subordinate to the centre (1.5). Belgium has a community government and Brussels has a separate government; India has a third tier of panchayats and municipalities and special provisions for some States (1.5).", "H"),
W("Read the extract and answer. 'The Constitution did not give the status of national language to any one language. Hindi was identified as the official language. But Hindi is the mother tongue of only about 40 per cent of Indians. Therefore, there were many safeguards to protect other languages.'  (i) What is the difference between national and official language? (ii) What safeguards exist? (iii) Why was this wise? (iv) Contrast with Sri Lanka.", 5,
  "(i) A national language is a symbol of the nation, but India gave that status to none; an official language is the language used for government work (1). (ii) 21 other Scheduled Languages, examination in any of them for central jobs, state official languages, English also used (1.5). (iii) Imposing Hindi on non-Hindi States could cause conflict, as in Tamil Nadu; accommodation promotes unity (1.25). (iv) Sri Lanka made Sinhala the only official language disregarding Tamil, leading to conflict (1.25).", "H"),
W("'Federalism is practised in India through democratic politics.' Explain with reference to linguistic states, language policy and centre-state relations.", 5,
  "Linguistic states: boundaries redrawn after 1947 on language; made the country more united and administration easier (1.5). Language policy: no national language; Hindi official; 21 other Scheduled Languages; English retained after Tamil Nadu protest (1.5). Centre-state relations: early dominance of one party; after 1990 regional parties and coalitions required power sharing and respect for State autonomy; Supreme Court judgement protected states from arbitrary dismissal (2).", "H"),
W("Case study. Two villages in a district each have Rs 5 lakh from the state government for a project. Village A's gram sabha meets, votes to use it for a well and a school wall; Village B's sarpanch decides alone and builds a shop for his relative. (i) Which institution has failed in B? (ii) Which constitutional features should ensure accountability? (iii) What can villagers do?", 5,
  "(i) The Gram Sabha, which should decide and supervise the work of the panchayat, did not function in B (1.5). (ii) Regular elections, the State Election Commission, powers and revenue shared with local bodies, and reservation making local government representative (1.5). (iii) Demand a Gram Sabha meeting, ask for accounts and vote the sarpanch out at the next election; use right to information and complain to higher authorities (2).", "H", wp=True),
W("Assertion (A): States in India have unequal powers although India is a federation.  Reason (R): India is a 'holding together' federation, where the Centre tends to be more powerful.  Examine whether A and R are true and R explains A, and give two examples of the inequality.", 4,
  "Both are true and R explains A (1.5). Some States such as Assam, Nagaland, Arunachal Pradesh and Mizoram enjoy special powers under Article 371 for their peculiar historical and social circumstances (1.25). Union Territories like Delhi and Chandigarh lack the powers of a State (1.25).", "H"),
W("'India's system of local government is a step to deepen democracy.' Examine the 1992 changes and the problems that remain. Give about four points in all.", 5,
  "Changes: regular elections constitutionally mandatory; seats reserved for SC, ST and OBC in elected bodies and executive heads; at least one-third of positions reserved for women; State Election Commission created in each State; States required to share some powers and revenue (2.5). Problems: the nature of sharing varies from State to State; many State governments have not transferred enough powers and funds to local bodies (2.5).", "H"),
W("Distinguish between the Gram Panchayat, Panchayat Samiti and Zilla Parishad in terms of members, how chosen and level. Which is the decision-making body for the village?", 4,
  "Gram Panchayat: ward members (panch) and sarpanch directly elected by adults of the ward or village; village level; it is the decision-making body for the village under the Gram Sabha (1.5). Panchayat Samiti: representative body of a block/mandal; members elected by all panchayat members in the area (1.25). Zilla Parishad: district level; most members elected, with Members of Parliament and MLAs of the district and some officials as members; chairperson is the political head (1.25).", "H"),
W("Why is it important that courts, especially the Supreme Court, act as umpire in a federation? Illustrate with two possible disputes.", 4,
  "In a federation levels of government may dispute their powers; an independent court interprets the Constitution and decides who is right, so neither level dominates (1.5). Example 1: a dispute over whether a subject belongs to the State List or the Union List (1). Example 2: a dispute where a Union law conflicts with a State law on a Concurrent subject or dismissal of a State government by the Centre (1.5).", "H"),
W("State the effect of the dual objective of federalism on India. Show how both unity and diversity have been protected, with two examples each.", 4,
  "Dual objective: safeguard and promote unity and accommodate regional diversity (1). Unity: a strong Union, common Constitution, residuary powers with the Union, power of Union on defence and currency (1.5). Diversity: linguistic states, many Scheduled Languages, special provisions for some States, local governments (1.5).", "H"),
W("Compare the effects of 'holding together' federal arrangements in India and the USA on (i) status of States (ii) strength of the centre. Why was the Indian Constitution framed this way?", 4,
  "USA is a coming together federation: States came together to form a bigger unit, are equal and strong compared with the federal government (1.5). India is a holding together federation: the Centre is more powerful and States can be unequal (1.5). India's makers framed it so because the country was diverse and needed unity after Partition, and wanted to hold the country together by sharing power (1).", "H"),
W("Suppose a State government wants to make Hindi compulsory in all schools and the Union Government wants English as an additional compulsory language. Which list does 'education' belong to? What process should be followed? Why is accommodation needed?", 4,
  "Education is on the Concurrent List, so both can legislate; in a conflict the Union law prevails (1.5). The process: consultation with the State, debates and agreement through Parliament; a change in the division of power itself would need two-thirds in both Houses plus half the States (1). Accommodation is needed because language is a sensitive issue; imposing a language caused violent protest in Tamil Nadu; trust between levels keeps unity (1.5).", "H"),
W("Why can federalism be called a method of managing diversity? Give four points and an example showing it has not always worked smoothly.", 4,
  "Different regions, languages and cultures are accommodated in a single country (1). Powers are divided so that regional issues are handled by regional governments (1). Linguistic states, language policy, special provisions for some States and local governments give every community a voice (1). Example of difficulty: Tamil Nadu's violent movement against Hindi and the tension over the Centre dismissing State governments (1).", "H"),
]

def _sub(x, pairs):
    if isinstance(x, str):
        for a, b in pairs: x = x.replace(a, b)
        return x
    if isinstance(x, (list, tuple)): return type(x)(_sub(i, pairs) for i in x)
    return x
_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c14.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
_PAIRS = [(" India now has **28 states and 8 Union Territories** (as of the changes of 2019-2020).", ""),
          (" (for example Andhra Pradesh and Karnataka, with **Maharashtra and Gujarat** formed in 1960)", ""),
          ("such as **Nagaland** (1963), **Uttarakhand** and **Jharkhand** (both 2000)", "such as **Nagaland, Uttarakhand and Jharkhand**"),
          ("; there are **22 Scheduled Languages**;", "; there are **21 other Scheduled Languages** besides Hindi;"),
          ("the Supreme Court's **S. R. Bommai judgement (1994)** made it difficult", "a major judgement of the **Supreme Court** made it difficult"),
          (" Jammu and Kashmir and Ladakh became Union Territories in 2019.", " Some States such as **Assam, Nagaland, Arunachal Pradesh and Mizoram** enjoy special powers under Article 371."),
          ("some units, such as **Delhi** and **Chandigarh**, are Union Territories", "some units, such as **Delhi, Chandigarh and Lakshadweep**, are Union Territories"),
          ("'Hindi is official language; there are 22 scheduled languages; English is also used.'", "'Hindi is official language; 21 other scheduled languages; English is also used.'")]
_core = _sub(_old["blocks"][:_i], _PAIRS)
_extra = [
 ("h2", "Key Terms at a Glance"),
 ("table", ["Term", "Meaning"], [
  ["Federalism", "Division of power between a central authority and constituent units"],
  ["Union List / State List / Concurrent List", "Subjects for the Union alone / the States alone / both (Union law prevails in a conflict)"],
  ["Residuary subjects", "Subjects not in any list or arising after the Constitution; the Union legislates"],
  ["Holding together federation", "Large country divides power between Centre and States (India, Spain, Belgium)"],
  ["Coming together federation", "Independent States join to form a unit (USA, Switzerland, Australia)"],
  ["Decentralisation", "Giving power from Union and State governments to local governments"],
  ["Gram Sabha", "All the voters of a village; supervises the Gram Panchayat"],
  ["Coalition government", "Government formed by an alliance of parties"],
  ["Union Territory", "Area not a State and not merged with one; run by the Centre (Chandigarh, Lakshadweep, Delhi)"]]),
 ("h2", "Local Government Structure"),
 ("table", ["Level", "Rural", "Urban"], [
  ["Village / ward", "Gram Panchayat (sarpanch and panch); Gram Sabha of all voters", "Municipal ward"],
  ["Block", "Panchayat Samiti (block or mandal)", "-"],
  ["Town / city", "-", "Municipality (chairperson) / Municipal Corporation (Mayor)"],
  ["District", "Zilla Parishad (chairperson is the political head)", "-"]]),
 ("h2", "Timeline and Facts to Remember"),
 ("table", ["Item", "Fact"], [
  ["World", "25 of 193 countries are federations; 40 per cent of the world's population"],
  ["1947 onwards", "Linguistic states, redrawing of boundaries"],
  ["1965", "English was to end as official language; protests in Tamil Nadu led to its continuation"],
  ["1990 onwards", "Regional parties, coalition governments, more State autonomy"],
  ["1992", "73rd and 74th Amendments: third tier made stronger"],
  ["Constitution change", "Two-thirds of Parliament plus ratification by half of the State legislatures"]]),
 ("h2", "Map Pointers"),
 ("ul", ["On a world map identify **federal countries**: USA, Canada, Mexico, Brazil, Argentina, Nigeria, Russia, India, Australia, Germany, Switzerland and Belgium.",
  "On a map of India locate the **Union Territories** Delhi, Chandigarh, Lakshadweep and the states carved out in 2000: **Uttarakhand, Jharkhand, Chhattisgarh**.",
  "Mark **Nagaland, Assam, Arunachal Pradesh and Mizoram** (special provisions under Article 371)."]),
 ("h2", "Sources and Case Notes"),
 ("ul", ["**Case: Belgium.** Reduced the power of the Central Government and gave it to regional governments, which cannot be withdrawn by the Centre; this strengthened federalism.",
  "**Case: Language movement in Tamil Nadu.** Violent protest when English was to be withdrawn in 1965; the Centre agreed to continue English with Hindi.",
  "**Source: Constitution.** Specifies the three lists, Article 371 for special States, and amendment rules for the power-sharing arrangement."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Linguistic reorganisation of states", "More unity and easier administration"],
  ["Rise of regional parties and coalitions after 1990", "Greater respect for State autonomy"],
  ["States as big as European countries", "Need for a third tier: local government"],
  ["1992 amendments", "Regular local elections, one-third seats for women, State Election Commission"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "Do not call Hindi the **national language**: it is the **official language**. There are **21 other Scheduled Languages**. Education and forests are on the **Concurrent List**, police and agriculture on the **State List**."),
 ("note", "REMEMBER", "The Union has power on **residuary** subjects, but the **Concurrent List** is shared; in a conflict the Union law prevails. Panchayats and municipalities form the **third tier**, added by the 1992 amendment."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("What are the key features of federalism? (5)", "Two or more levels; separate jurisdictions; powers in the Constitution; changes need consent of both levels; courts as umpire; independent revenue sources; dual objective of unity and diversity."),
  ("How is federalism practised in India? (5)", "Linguistic states, language policy with Hindi as official language and 21 other Scheduled Languages, centre-state relations improved after coalition governments, decentralisation through panchayats and municipalities."),
  ("Explain the three-fold distribution of legislative powers. (3)", "Union List, State List, Concurrent List with examples; residuary subjects with the Union; Union law prevails for conflicts in Concurrent List."),
  ("Why is local government needed? (3)", "Local problems are best solved locally; people know them better; participation and accountability improve; States are large and diverse."),
  ("State the 1992 provisions for local government. (3)", "Regular elections; reservation for SC, ST, OBC and one-third for women; State Election Commission; sharing of powers and revenue."),
 ]),
]
CH = dict(num=14, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_old["takeaways"] + ["Only 25 of the world's 193 countries are federations, but they hold about 40 per cent of the world's people.", "A change in the Union-State power sharing needs two-thirds of both Houses and ratification by half of the State legislatures."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
