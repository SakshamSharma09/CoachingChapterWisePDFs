"""Class 10 Social Science Ch 15 - Gender, Religion and Caste (Political Science Ch 3): worksheet (50 graded questions) + detailed chapter notes."""
from libws import *          # W, run
import runpy
BANK = "c10sst_ch15"

def mc(q, opts, i, why=""):
    return W(q, 1, f"({'abcd'[i]}) {opts[i]}." + (" " + why if why else ""), "E", opts=opts)
AR = ["Both A and R are true and R is the correct explanation of A", "Both A and R are true but R is not the correct explanation of A", "A is true but R is false", "A is false but R is true"]
def ar(a, r, i, why, lvl="E"):
    return W(f"Assertion (A): {a}  Reason (R): {r}  Choose the correct option.", 1, f"({'abcd'[i]}) {AR[i]}. {why}", lvl, opts=AR)

WS = [
# ------------------------------------------------------------------ EASY (17)
mc("The sexual division of labour means that:", ["women and men do the same work", "women do most work inside the home while men do work outside", "men do all household work", "all work is paid"], 1, "It confines women to the private sphere."),
mc("A system that values men more and gives them power over women is called:", ["patriarchy", "secularism", "communalism", "federalism"], 0, "Literally, rule by the father."),
mc("According to NCERT, the child sex ratio in India fell to about:", ["1000", "950", "919", "850"], 2, "Girls per thousand boys; sex-selective abortion is a cause."),
mc("The Equal Remuneration Act was passed in:", ["1950", "1976", "1992", "2005"], 1, "It provides that equal wages should be paid for equal work."),
mc("What share of seats in panchayats and municipalities is reserved for women?", ["10 per cent", "One-fourth", "One-third", "One-half"], 2),
mc("Communalism is the belief that:", ["all religions are equal", "religion is the principal basis of social community", "the state should have no relation with citizens", "the majority should not rule"], 1),
mc("A secular state is one that:", ["has an official religion", "gives special status to one religion", "has no official religion and treats all religions equally", "bans all religions"], 2),
mc("Which of these reformers worked to end caste inequalities?", ["Periyar Ramaswami Naicker", "Lord Dalhousie", "Mahmud Ghazni", "Mohammad Ali Jinnah"], 0, "Jotiba Phule, Gandhiji and Dr Ambedkar also worked for this."),
W("Define patriarchy and feminist.", 2,
  "Patriarchy: literally rule by the father; a system that values men more and gives them power over women (1). Feminist: a woman or a man who believes in equal rights and opportunities for women and men (1).", "E"),
W("What percentage of the Lok Sabha did women's elected share touch in 2019 for the first time, and what is their share in State Assemblies?", 2,
  "14.36 per cent in the Lok Sabha (1) and less than 5 per cent in State Assemblies (1).", "E"),
W("Fill in the blanks: According to the 1998-99 Time Use Survey, an average Indian woman works about ______ hour(s) more than an average man every day, and the Act that requires equal wages for equal work is the ______ Act, 1976.", 2,
  "One; Equal Remuneration. (1 + 1)", "E"),
W("Name two Scandinavian countries where women's participation in public life is high.", 1, "Any two of Sweden, Norway, Finland. (1)", "E"),
W("True or false (with a reason): 'Religious differences are always the same as communalism.'", 2,
  "False (1). Religion can be part of politics when values and ethics drawn from it are used, as Gandhiji said; communalism is when religion is made the basis of nation and politics, pitting one religion against another (1).", "E"),
W("Match: (i) Gandhiji (ii) B. R. Ambedkar (iii) Periyar (iv) Jotiba Phule.  A. Said that religion cannot be separated from politics, meaning moral values  B. Worked for caste equality in Tamil Nadu  C. Social reformer who opposed caste hierarchy and untouchability  D. Leader of Dalits and architect of the Constitution.", 2,
  "(i)-A, (ii)-D, (iii)-B, (iv)-C. (all four = 2; two or three correct = 1)", "E"),
W("State any two factors that have weakened caste hierarchy in modern India.", 2,
  "Urbanisation, growth of literacy and education, occupational mobility and weakening of the position of landlords (any two) (1), and the efforts of social reformers and the Constitution's prohibition of caste discrimination (1).", "E"),
W("What does the Constitution say about religion in India? Mention two features.", 2,
  "There is no official religion; the state does not give special status to any religion (1). Citizens are free to follow, practise and propagate any religion or none, and the Constitution prohibits discrimination on grounds of religion (1).", "E"),
W("What is meant by 'communal politics'? Give one form.", 2,
  "Communal politics is the use of religion in politics in exclusive and partisan terms, pitting one religion against another and seeking domination by one group (1). Forms: political mobilisation on religious lines, using sacred symbols, or communal violence and riots (1).", "E"),
# ------------------------------------------------------------------ MEDIUM (20)
ar("Women's representation in India's legislatures is low.", "The share of elected women in the Lok Sabha touched only 14.36 per cent in 2019.", 0, "The low share of women is an example of limited political representation.", "M"),
ar("India's Constitution prohibits discrimination on grounds of religion.", "India has chosen a secular model.", 0, "Secularism means equal treatment of all religions with no official religion.", "M"),
W("Explain the 'sexual division of labour' with examples and say why women's outdoor work is not valued.", 3,
  "In most families women do all the work inside the home, such as cooking, cleaning, washing, tailoring and looking after children, while men do the work outside (1). Women also work outside the home: fetching water, collecting fuel, working in fields, as domestic helpers or in offices (1). Their work is not valued and not recognised, as it is often unpaid and paid less than men's even for the same work (1).", "M"),
W("Table-based. Time use survey (1998-99, hours:minutes per day): Income-generating work - men 6:00, women 2:40; Household and related work - men 0:30, women 5:00. (i) Find total work of men and of women. (ii) Who works longer and by how much? (iii) Which work is more recognised as 'work' in public life?", 3,
  "(i) Men: 6:00 + 0:30 = 6:30 hours; women: 2:40 + 5:00 = 7:40 hours (1.5). (ii) Women work 1 hour 10 minutes longer (1). (iii) Income-generating work done mostly by men is visible and valued; household work is unpaid and often unrecognised (0.5).", "M", wp=True),
W("Give three reasons why the literacy and education of girls lag behind that of boys.", 3,
  "The literacy rate among women is only 54 per cent compared with 76 per cent among men (1). Girls drop out of school because parents spend more on boys' education and prefer sons (1). A smaller proportion of girls go for higher studies because of the social expectation that they should look after homes (1).", "M"),
W("What is the child sex ratio? State its value and two causes of its fall.", 3,
  "Number of girl children per thousand boys (1). It has fallen to merely 919 (0.5). Causes: preference for sons and sex-selective abortion; parents finding ways to prevent the birth of girls (1.5).", "M"),
W("Why do women's movements demand reservation of seats in legislatures? What has been done at the local level?", 3,
  "Women are very poorly represented in the Lok Sabha and State Assemblies, and need seats so that their issues are raised and decided (1.5). One-third of seats in panchayats and municipalities are reserved for women; there are now more than 10 lakh elected women representatives (1.5).", "M"),
W("What does the Nari Shakti Vandan Adhiniyam (2023) provide? Why was a bill needed for so many years?", 2,
  "It provides 33 per cent reservation of seats for women in the Lok Sabha, State Legislative Assemblies and the Delhi Assembly (1). A bill on this had been pending before Parliament for many decades because of lack of agreement among parties (1).", "M"),
W("Explain how Gandhiji viewed religion and politics. Is this the same as communalism?", 3,
  "Gandhiji said that religion can never be separated from politics, by which he meant the moral values drawn from all religions that should guide politics (1.5). This is not communalism, since he did not favour any one community; communalism makes religion the principal basis of social community and politics (1.5).", "M"),
W("Describe three forms of communalism with an example.", 3,
  "In everyday beliefs: religious prejudices, stereotypes and belief in the superiority of one's religion (1). In politics: seeking dominance of one's community; mobilising on religious lines, using sacred symbols and religious leaders (1). In violence: communal riots and massacre, as at the time of Partition (1).", "M"),
W("Why is a secular state needed in a diverse country like India? Give three points.", 3,
  "India has followers of many religions; secularism ensures that no religion is official and none is favoured (1). It protects the freedom of every citizen to practise and propagate any religion and bans discrimination (1). The Constitution allows the state to intervene to ensure equality within religious communities, e.g. banning untouchability; communalism threatens the very idea of India (1).", "M"),
W("Which feature of caste distinguishes it from other social divisions? Describe the caste system in three points.", 3,
  "Caste is hereditary and sanctioned by rituals; occupation is hereditary and the division of labour is rigid (1). Members of the same caste practise the same or similar occupation, marry within the caste and exclude other castes from eating with them (1). 'Outcaste' groups were subjected to discrimination and untouchability (1).", "M"),
W("Describe three ways in which caste influences politics.", 3,
  "Parties take into account the caste composition of the electorate when choosing candidates (1). Governments are formed with a mix of castes and parties and candidates appeal to caste sentiment (1). Universal adult franchise and one person one vote force leaders to seek support of many caste groups (1).", "M"),
W("Why do caste-based parties not win elections just by caste appeals? Give two reasons.", 2,
  "No parliamentary constituency has a clear majority of one caste, so a party needs support across castes (1). Voters have other considerations too, such as the party, the performance of the government and the candidate (1).", "M"),
W("In what two ways has caste politics helped marginalised communities?", 2,
  "It has brought under-privileged communities, including Dalits and OBCs, into the political arena (1), giving them greater voice and power and opening the way for them to claim their share (1).", "M"),
W("An unconventional wedding: a boy from one caste and a girl from another marry in a village in Rajasthan, and some villagers object. (i) What does this show about caste? (ii) What does the Constitution say? (iii) Who could help?", 3,
  "(i) Caste is still in the way people marry and the practice of marrying within the caste continues; untouchability and prejudice have not ended completely (1). (ii) Caste-based discrimination is prohibited and every adult has the right to choose (1). (iii) Local administration and police, panchayat committees, social organisations and courts can help (1).", "M", wp=True),
W("Error analysis. A student writes: 'Gender division in politics is based on biological differences between women and men.' Correct this.", 2,
  "The gender division is mostly based not on biology but on social expectations and stereotypes (1). Boys and girls are brought up to believe that women's main role is housework and bringing up children (1).", "M"),
W("List two ways in which religion can be used in politics without being communal.", 2,
  "Raising demands for equality and justice for a religious community (e.g. protection of minorities) and values or ethics drawn from religions that guide politics (1). Human rights groups demanding protection of minorities and women's movements demanding equal family laws (1).", "M"),
W("What is the significance of 'one person one vote' for caste politics?", 2,
  "Each citizen has an equal vote regardless of caste or religion (1). Leaders must therefore seek the support of many groups, which has forced political leaders to take up the concerns of different castes (1).", "M"),
W("Table-based. In a panchayat election, a constituency has 45 per cent voters from caste P, 35 per cent from caste Q, 20 per cent from others. Candidate A gets all of P's votes but nothing else. Can A win for sure? What does this show?", 2,
  "Not for sure: A would get 45 per cent; if Q and the others all vote for a rival, the rival gets 55 per cent (1). It shows that no caste has a clear majority and that candidates must win support across castes (1).", "M", wp=True),
# ------------------------------------------------------------------ HARD (13)
W("'Gender division is an example that some form of social division needs to be expressed in politics.' Explain with four points.", 4,
  "Women are half of humanity but their role in public life, especially politics, is minimal in most societies (1). Political expression of the demand lets women's movements demand equal rights in personal and family life, education and the workplace (1). Reservation in local bodies and the 2023 Act show that representation can be improved through politics (1). Countries such as Sweden, Norway and Finland show that women's participation in public life can be high (1).", "H"),
W("Read the extract and answer. 'Communalism involves thinking along the following lines. The followers of a particular religion must belong to one community. Their fundamental interests are the same. Any difference that they may have is irrelevant or trivial for community life. It also follows that people who follow different religions cannot belong to the same social community.'  (i) What belief is described? (ii) Why is it harmful in a diverse country? (iii) How does it express itself in politics? (iv) What does the Constitution do against it?", 5,
  "(i) Communalism: religion is the principal basis of social community (1). (ii) It ignores differences within a community and overlooks common interests of people of different religions, leading to conflict and violence, as in Partition (1.5). (iii) Political mobilisation on religious lines, use of sacred symbols and religious leaders, communal violence and riots (1.5). (iv) Chooses a secular state with no official religion, prohibits discrimination and allows the state to intervene to ensure equality (1).", "H"),
W("Examine the statement: 'Caste has become a vote bank, but it does not decide elections alone.' Give three arguments for and three against.", 5,
  "For: parties choose candidates on caste composition; governments represent a mix of castes; leaders appeal to caste sentiment (2.5). Against: no constituency has a clear majority of one caste; voters consider the party, government performance and candidate; many candidates win with support from several castes (2.5).", "H"),
W("Case study. In a village near Jaisalmer a girl, Pooja, tops the Class 10 board exam but her family wants her to stop studying after Class 10 to help at home and arrange marriage. (i) Which social attitudes are at work? (ii) Name two facts about gender gaps from the chapter. (iii) How can the family, school and government help?", 5,
  "(i) Gender stereotypes and the sexual division of labour that expect women to do housework, and son preference with more spending on boys' education (1.5). (ii) Literacy rate 54 per cent for women compared with 76 per cent for men; women work one hour more than men every day, with unpaid work; child sex ratio of 919 (1.5, any two). (iii) Family: encourage and invest in her education; School: counselling, scholarships and role models; Government: scholarships, reservation in local bodies and laws such as equal pay and others for girls' education (2).", "H", wp=True),
W("Compare how gender, religion and caste interact with politics: give one positive effect and one risk for each.", 5,
  "Gender: positive, women's movements and reservation of one-third seats in local bodies and 33 per cent in legislatures raise participation; risk: patriarchy and low representation continue (2). Religion: positive, ethics and values from religion can inspire fairness and human rights groups protect minorities; risk: communalism, riots and majority-minority conflict (2). Caste: positive, gives voice to Dalits and OBCs and encourages social reform; risk: caste divisiveness, tension and violence, diverting attention from poverty, development and corruption (1).", "H"),
W("Why is communalism called a threat to the 'very idea of India'? Support with two historical and two constitutional points.", 4,
  "Historical: India and Pakistan suffered some of the worst communal riots at the time of Partition (1); large-scale communal violence has occurred in the post-Independence period (1). Constitutional: India chose a secular state with no official religion (1) and the Constitution prohibits discrimination on religious grounds, treating every citizen equally (1).", "H"),
W("Why have women's work and contribution been 'undercounted' in India? Use data on time use, wages and unpaid work.", 4,
  "The Time Use Survey shows that women work a little over 7 and a half hours daily while men work 6 and a half hours (1). Much of women's household work, including fetching water, collecting fuel and farm tasks, is unpaid and not recognised (1.5). Even when paid, women are paid less than men for the same work despite the Equal Remuneration Act, 1976 (1.5).", "H"),
W("Hard HOTS. 'Reservation is the only way to increase women's participation.' Argue for and against this statement with two points each.", 4,
  "For: reservation in local bodies has put more than 10 lakh women in elected roles; without it women are very poorly represented at 14.36 per cent in the Lok Sabha (2). Against or limits: social attitudes, safety, education and equal wages also matter; family responsibilities and patriarchy keep women away, so reservation alone is not enough (2).", "H"),
W("Assertion (A): Caste inequality has completely disappeared in India.  Reason (R): The Constitution prohibits caste-based discrimination.  Evaluate A and R with reasons.", 3,
  "A is false and R is true (1). Although caste notions are breaking down because of urbanisation, literacy, occupational mobility and the efforts of reformers (Phule, Gandhi, Ambedkar, Periyar), caste still shapes marriage and untouchability has not ended completely (1). The Constitution prohibits discrimination and lays the foundation for policies to reverse injustice, but a law alone does not remove prejudice (1).", "H"),
W("A political party in a state promises 'special benefits to our community only'. Evaluate this promise in the light of secularism, equality and the chapter's lessons in about five points.", 5,
  "It uses religion or caste as the main basis of politics, which is communal or casteist politics (1). It conflicts with the Constitution's ban on discrimination and the secular idea of equal treatment (1.5). It divides society and diverts attention from poverty, development and corruption (1.5). Voters need not support it because no group is a majority in most constituencies; policies for under-privileged groups are legitimate when based on constitutional equality and not on exclusion (1).", "H"),
W("Women's movement point. Name three demands raised by feminist movements and two achievements.", 4,
  "Demands: equal rights in personal and family life; equal opportunities in education; equal pay and treatment in the workplace; political representation (2). Achievements: reservation of one-third seats in panchayats and municipalities; equal remuneration law; the 2023 Act for 33 per cent reservation in legislatures (2).", "H"),
W("Passage-based. 'Politics works to bring under-privileged communities into the political arena. It has also made them aware that they too can claim a share of power. However, politicisation of caste can lead to tensions, violence and divisiveness, and it diverts attention from vital issues like poverty, development and corruption.'  (i) Give one benefit of this process. (ii) Give two dangers. (iii) Is caste-based politics good for democracy? Give a reasoned verdict.", 4,
  "(i) Marginalised groups such as Dalits and OBCs gain greater voice and share of power (1). (ii) Tension, violence and divisiveness; diversion from poverty, development and corruption (1.5). (iii) It is not good for democracy if it divides people and excludes issues of common concern; inclusion through equality is positive but caste-exclusive politics is harmful (1.5).", "H"),
]

_old = runpy.run_path(str(REPO / "src/rn_work/c10_sst/c15.py"))["CH"]
_i = max(k for k, b in enumerate(_old["blocks"]) if b[0] == "h2")
def _sub(x, pairs):
    if isinstance(x, str):
        for a, b in pairs: x = x.replace(a, b)
        return x
    if isinstance(x, (list, tuple)): return type(x)(_sub(i, pairs) for i in x)
    return x
_PAIRS = [("(figures given in the NCERT text)", "(NCERT text)"), ("‘", "'"), ("’", "'")]
_core = _sub(_old["blocks"][:_i], _PAIRS)
_extra = [
 ("h2", "Key Terms at a Glance"),
 ("table", ["Term", "Meaning"], [
  ["Gender division", "Hierarchical social division based on social expectations about women and men, not biology"],
  ["Sexual division of labour", "Women do the work inside the home, men do the work outside"],
  ["Patriarchy", "Literally rule by the father; system valuing men more and giving them power over women"],
  ["Feminist", "A woman or man who believes in equal rights and opportunities for women and men"],
  ["Communalism", "Belief that religion is the principal basis of social community"],
  ["Secular state", "No official religion; equal treatment and freedom of religion for all"],
  ["Casteism", "Belief that caste is the main basis of social community and politics"],
  ["Communal politics", "Using religion in politics in an exclusive and partisan way to dominate others"]]),
 ("h2", "Facts and Figures to Remember"),
 ("table", ["Fact", "Figure"], [
  ["Women's literacy compared with men's", "54 per cent compared with 76 per cent"],
  ["Child sex ratio", "919 girls per 1000 boys"],
  ["Women in Lok Sabha (2019)", "14.36 per cent; less than 5 per cent in State Assemblies"],
  ["Reservation in local bodies", "One-third of seats; more than 10 lakh elected women representatives"],
  ["Equal Remuneration Act", "1976: equal wages for equal work"],
  ["Time Use Survey (1998-99)", "Women work a little over 7 and a half hours daily; men about 6 and a half hours"],
  ["Nari Shakti Vandan Adhiniyam", "2023: 33 per cent reservation in Lok Sabha, State Assemblies and the Delhi Assembly"]]),
 ("h2", "Sources and Case Notes"),
 ("ul", ["**Source: Time Use Survey.** Income-generating work: men 6:00, women 2:40 hours; household and related work: men 0:30, women 5:00 hours; the visible work of men is better valued.",
  "**Case: Scandinavian countries.** Participation of women in public life is high in Sweden, Norway and Finland.",
  "**Case: Northern Ireland.** Shows the danger of basing nationhood on religion.",
  "**Gandhiji's view.** Religion cannot be separated from politics, meaning moral values drawn from all religions."]),
 ("h2", "Cause and Effect Chains"),
 ("table", ["Cause", "Effect"], [
  ["Sexual division of labour and stereotypes", "Women's work undervalued; low presence in public life"],
  ["Preference for sons and sex-selective abortion", "Child sex ratio falls to 919"],
  ["Use of religion in exclusive terms in politics", "Communal violence, riots and mistrust"],
  ["Urbanisation, education, occupational mobility and reform", "Caste hierarchy weakens, though not fully"],
  ["No constituency with a clear majority of one caste", "Parties need support across castes"]]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "**Secular does not mean anti-religion.** The state has no official religion and treats all religions equally; it can intervene to ensure equality, such as banning untouchability."),
 ("note", "REMEMBER", "The **Equal Remuneration Act is 1976**, the **local body reservation is one-third** and the **2023 Act provides 33 per cent** for Lok Sabha, State Assemblies and the Delhi Assembly. Do not say 50 per cent."),
 ("h2", "Likely 3 and 5 Mark Answers"),
 ("qa", [
  ("How does the sexual division of labour affect women's role in public life? (3)", "Women do most of the unpaid household work, which is not valued; though they work longer hours, their role in public life, especially politics, is minimal."),
  ("Explain the different forms of communalism. (5)", "Everyday prejudices and stereotypes; political mobilisation on religious lines using sacred symbols and leaders; communal violence, riots and massacre; quest for dominance by the majority or separate political unit by a minority."),
  ("How is caste related to politics? (5)", "Parties consider caste while choosing candidates; governments reflect a mix of castes; appeals to caste sentiment; politics brings under-privileged communities into the political arena; no constituency has a single-caste majority; voters have other interests."),
  ("Why is caste politics harmful? (3)", "It leads to tension, violence and divisiveness and diverts attention from poverty, development and corruption."),
  ("What is a secular state? (3)", "No official religion, freedom to practise any religion, no discrimination, and state intervention only to ensure equality."),
 ]),
]
CH = dict(num=15, title=_old["title"], tag=_old["tag"], intro=_old["intro"], big_questions=_old["big_questions"],
          blocks=_core + _extra, takeaways=_old["takeaways"] + ["Key figures: women's literacy 54 per cent against 76 per cent for men, child sex ratio 919, Lok Sabha women share 14.36 per cent (2019).", "Reform movements and the Constitution have weakened caste and promoted secularism, but caste, communalism and patriarchy still shape politics."])

if __name__ == "__main__": run(__file__, BANK, 10, "Social_Science", WS, CH)
