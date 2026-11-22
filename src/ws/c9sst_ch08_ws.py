"""Class 9 Social Science Ch 8 - Elections (Political Science): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch08"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c08", str(REPO / "src/rn_work/c9_sst/c08.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Which of these is elected through an indirect election?", 1, "(c) Rajya Sabha", "E", opts=["Lok Sabha", "Vidhan Sabha", "Rajya Sabha", "A Gram Panchayat"]),
W("The Election Commission of India was established on:", 1, "(b) 25 January 1950", "E", opts=["26 January 1950", "25 January 1950", "15 August 1947", "26 November 1949"]),
W("In the First-Past-The-Post system the winner in a constituency is the candidate who:", 1, "(d) gets more votes than every other candidate", "E", opts=["gets more than 50% of the votes", "gets the support of all parties", "gets the most second-preference votes", "gets more votes than every other candidate"]),
W("The preparation of electoral rolls and delimitation of constituencies is covered by:", 1, "(a) the Representation of the People Act, 1950", "E", opts=["the Representation of the People Act, 1950", "the Representation of the People Act, 1951", "the Presidential and Vice-Presidential Elections Act, 1952", "the Anti-Defection Law of 1985"]),
W("The Anti-Defection Law was passed through the:", 1, "(b) 52nd Constitutional Amendment Act, 1985", "E", opts=["42nd Amendment Act, 1976", "52nd Constitutional Amendment Act, 1985", "73rd Amendment Act, 1992", "1st Amendment Act, 1951"]),
W("The mobile app through which a citizen can report a violation of the Model Code of Conduct is:", 1, "(c) cVIGIL", "E", opts=["Saksham", "Suvidha", "cVIGIL", "Sugam"]),
W("How many Delimitation Commissions has India had so far, according to the chapter?", 1, "(a) Four (1952, 1963, 1973 and 2002)", "E", opts=["Four (1952, 1963, 1973 and 2002)", "Two (1952 and 2002)", "Six", "One (in 1950)"]),
W("State True or False, with a reason: Independent candidates can also contest elections in India.", 2, "True (1). Candidates need not belong to a party; only registered parties get the benefit of party symbols and recognition (1).", "E"),
W("Define psephology. From which language does the word come?", 2, "Psephology is the scientific study of elections (1). It comes from the Greek word 'psephos' meaning a pebble, which was used for voting in ancient Greece (1).", "E"),
W("Fill in the blank: The powers of the Election Commission of India come from Articles ______ to ______ of the Constitution.", 1, "324 to 329 (1)", "E"),
W("Name any two states that have a Vidhan Parishad (Legislative Council).", 2, "Any two of Andhra Pradesh, Bihar, Karnataka, Maharashtra, Telangana, Uttar Pradesh. (1+1)", "E"),
W("What is the full form of VVPAT?", 1, "Voter Verifiable Paper Audit Trail. (1)", "E"),
W("Which day is celebrated as National Voters' Day?", 1, "25 January. (1)", "E"),
W("Who supervises the conduct of elections in a state at the state level?", 1, "The Chief Electoral Officer, appointed by the ECI from among civil servants in consultation with the state government. (1)", "E"),
W("Give two examples of bodies elected through direct elections.", 2, "Any two: Lok Sabha, Vidhan Sabha, Panchayats, municipal corporations (local bodies). (1+1)", "E"),
W("What is an electoral roll? Why is it important?", 2, "It is the list of persons eligible to vote, made constituency-wise and polling-station-wise (1). Only persons whose names are on it can vote, so it must be accurate and complete (1).", "E"),
W("Which party formed the first coalition government at the Centre in 1977?", 1, "The Janata Party. (1)", "E"),
# ---------------- MEDIUM ----------------
W("A class representative cannot continue for ever without a fresh election. Using this idea, explain why periodic elections are needed in a democracy.", 3, "Elected representatives decide on our behalf, so they must remain accountable (1). A government cannot stay beyond its term without seeking the people's mandate again (1). Regular elections let people re-elect or change their leaders and keep power with the people (1).", "M"),
W("In a Vidhan Sabha constituency the votes polled were: Meena 32,000; Karan 28,000; Farida 20,000; Joseph 10,000. Under FPTP (i) who wins, (ii) what percentage of the total votes did the winner get, and (iii) by what margin?", 3, "Total votes = 90,000 (0.5). (i) Meena wins as she has the most votes (0.5). (ii) 32,000 ÷ 90,000 × 100 = 35.6% (1), so she wins without 50%. (iii) Margin = 32,000 - 28,000 = 4,000 votes (1).", "M", wp=True),
W("In a state, 1,20,000 valid votes are cast to elect 5 members through the single transferable vote. Find the quota (minimum votes to win).", 3, "Quota = (Total valid votes ÷ (Seats + 1)) + 1 (1). = 1,20,000 ÷ 6 + 1 (1) = 20,000 + 1 = 20,001 votes (1).", "M", wp=True),
W("Distinguish between the FPTP system and the proportional representation system on any three points.", 3, "FPTP: voters vote for a candidate in a constituency; the candidate with the most votes wins, even without 50%; used for Lok Sabha and Vidhan Sabha. PR: voters (or members) rank candidates / vote for parties, seats are in proportion to votes; used for Rajya Sabha, President, Vice President and Vidhan Parishad. (1 each for any three points)", "M"),
W("Match each Act with what it covers: (a) delimitation of constituencies and electoral rolls (b) conduct of elections, offences and corrupt practices (c) election of the President and Vice President, with (1) RPA 1950 (2) RPA 1951 (3) Presidential and Vice-Presidential Elections Act 1952.", 3, "(a) with (1); (b) with (2); (c) with (3). (1 each)", "M"),
W("In a two-round (majority) system, Round 1 results are: Pooja 45%, Imran 40%, Ravi 15%. (i) Is anyone elected? (ii) What happens next?", 3, "(i) No, because no candidate has more than 50% (1). (ii) The top two, Pooja and Imran, contest again in a second round (1) and the one who gets more than 50% in it wins (1).", "M", wp=True),
W("Why is delimitation necessary? What would happen without it?", 3, "Delimitation fixes the number of seats and the boundaries of constituencies so that the seat-to-population ratio is as equal as possible (1.5). Without it, one MP might represent five lakh people and another twenty-five lakh, making some votes count for much more than others (1.5).", "M"),
W("List any three corrupt practices mentioned in the Representation of the People Act, 1951.", 3, "Any three: gifts, offers or promises to induce someone to contest, withdraw, vote or not vote; appeals for votes on grounds of religion, caste, race, community or language; taking help for the candidate from government personnel such as gazetted officers, judges, magistrates, armed forces, police or excise officers. (1 each)", "M"),
W("What is the Special Intensive Revision (SIR) of electoral rolls? State three reasons why names may be removed.", 3, "SIR updates, verifies and corrects the rolls so that no eligible citizen is left out and no ineligible person is included (1). Names are removed for death, change of residence, duplicate entries or untraceable voters (any two, 1 each).", "M"),
W("Why does the Election Commission consider the school and university exam calendar, festivals and the agricultural cycle while fixing election dates?", 2, "So that as many voters as possible can vote without difficulty (1), and teachers, students and farmers are not disturbed at crucial times; this makes the election more inclusive and the turnout better (1).", "M"),
W("Find the mistake: 'A party that gets 40% of the votes in an FPTP election will always get exactly 40% of the seats.'", 2, "Wrong (1). In FPTP seats depend on who tops each constituency, so a party can win far more or fewer seats than its vote share; seats in proportion to votes is the feature of proportional representation (1).", "M"),
W("Match the app with its purpose: (a) Suvidha (b) Saksham (c) Sugam (d) ERONET with (1) services for persons with disabilities (2) permissions and nomination forms for candidates (3) managing vehicles requisitioned for election work (4) processing of forms and electoral rolls.", 3, "(a)-(2); (b)-(1); (c)-(3); (d)-(4). (3 marks for all four, 2 for three)", "M"),
W("Timeline. Arrange in order, with years: (i) first coalition government at the Centre (ii) Anti-Defection Law (iii) voting from home extended nationwide (iv) Election Commission set up.", 3, "(iv) 1950; (i) 1977; (ii) 1985; (iii) 2024. (3 for all correct, 2 for three in correct order)", "M"),
W("What is the voters' pledge celebrated on National Voters' Day? State its main points.", 3, "Citizens pledge to uphold democratic traditions and the dignity of free, fair and peaceful elections (1.5) and to vote fearlessly, without being influenced by religion, race, caste, community, language or any inducement (1.5).", "M"),
W("Source-based. 'The Vidhan Parishad has members elected by MLAs and local bodies, by graduates and teachers, and some nominated by the Governor for art, science, social service, literature and cooperatives.' (i) Which houses form a bicameral state legislature? (ii) Name one group whose members are nominated.", 3, "(i) The Vidhan Parishad (Upper House) and the Vidhan Sabha (Lower House) (2). (ii) Persons with special knowledge of art, science, social service, literature or cooperatives, nominated by the Governor (1).", "M"),
W("Describe any three roles of political parties in elections.", 3, "Any three: organise public opinion and campaign on issues; give voters meaningful choices; help voters make informed decisions through rallies, manifestos and debate; contest elections and form the government or sit in opposition; formulate policies and keep the government accountable. (1 each)", "M"),
W("What is defection? Give one argument for and one against allowing a member to switch parties.", 3, "Defection is abandoning the party on whose ticket a member was elected, by joining another party or acting against it (1). Against: it is opportunism that breaks party discipline and makes governments unstable (1). For: a member may be following his or her conscience (1).", "M"),
W("State any two ways in which a party can become a 'national party'.", 3, "Any two: 6% of valid votes in four or more states plus four Lok Sabha seats; 2% of Lok Sabha seats from at least three states; recognition as a state party in at least four states. (1.5 each)", "M"),
# ---------------- HARD ----------------
W("Case study. Five constituencies (100 voters each) have votes for parties A, B, C: (1) A 40, B 35, C 25; (2) A 38, B 37, C 25; (3) A 36, B 34, C 30; (4) A 20, B 45, C 35; (5) A 30, B 28, C 42. Under FPTP find the seats won by each party and the overall vote share. What does this show?", 5, "Winners: (1) A, (2) A, (3) A, (4) B, (5) C, so A has 3 seats, B 1 and C 1 (2). Total votes: A 164 (32.8%), B 179 (35.8%), C 157 (31.4%) out of 500 (2). Party A gets 60% of the seats with 32.8% of the votes, while B has the most votes but only 20% of the seats; FPTP can give results not proportional to votes (1).", "H", wp=True),
W("A parliament of 60 seats is elected by proportional representation. Votes: Party M 4,00,000; N 3,50,000; O 1,50,000; P 1,00,000. Find the seats of each party and name one advantage of PR.", 4, "Total votes = 10,00,000 (1). Seats = 60 × share: M 24, N 21, O 9, P 6 (2). Advantage: smaller parties and groups get fair representation, so power is shared in proportion to support (1).", "H", wp=True),
W("Arrange these steps of counting under the single transferable vote in order and explain the last two: (a) the candidate with the fewest votes is eliminated (b) first preference votes are counted (c) the process repeats until the required number are elected (d) candidates reaching the quota are declared elected (e) the votes of the eliminated candidate are transferred to the next preferences.", 4, "Order: (b), (d), (a), (e), (c) (2). Explanation: the votes of the eliminated candidate are passed on to the candidates marked as the second (next) preference on those ballots (1), and the cycle of elimination and transfer continues until all the seats are filled (1).", "H"),
W("Case study. Before a Vidhan Sabha election a candidate's supporters distribute sarees and sweets to voters of a village and ask them to vote 'for people of our caste'. (i) Identify two violations. (ii) How can a citizen report it? (iii) Why does it harm free and fair elections?", 4, "(i) Gifts to induce voters and an appeal for votes on caste (corrupt practices under the RPA, 1951; also against the Model Code of Conduct) (1.5). (ii) Through the cVIGIL app, which reports violations within minutes, and flying squads act using the auto-location (1.5). (iii) It takes away the voters' free choice, so the result does not reflect their real will (1).", "H", wp=True),
W("Case study. Constituency X has 5 lakh voters and constituency Y has 25 lakh voters, and each elects one MP. (i) What problem does this create? (ii) Which body and which Article can correct it? (iii) Name two years when this was done.", 4, "(i) A vote in X carries five times the weight of a vote in Y, so representation is unequal (1.5). (ii) The Delimitation Commission under Article 82 redraws seats and boundaries (1.5). (iii) Any two of 1952, 1963, 1973, 2002 (1).", "H", wp=True),
W("The ECI is an autonomous and permanent constitutional body. Explain why independence from the government is essential for it, with two examples of its work.", 4, "If the body that runs elections were controlled by the government, the ruling party could influence rolls, dates or rules, so elections would not be free and fair (2). Examples: it prepares electoral rolls and registers parties and allots symbols; it fixes schedules and enforces the Model Code of Conduct on all parties, including the ruling one (any two, 2).", "H"),
W("A legislator elected on the ticket of party X votes against the party whip in the House. (i) Which law applies? (ii) Who decides on disqualification? (iii) Give one reason in support of the law and one against it.", 4, "(i) The Anti-Defection Law, passed through the 52nd Amendment in 1985 (1). (ii) The Speaker or Chairman of the House (1). (iii) For: it gives stable governments and discourages opportunism (1). Against: it can restrict a member from voting by conscience or opposing the party on an issue (1).", "H"),
W("Design an inclusive polling station for a village in your district. Suggest four measures, naming the groups they help and linking them to ECI initiatives in the chapter.", 4, "Any four, 1 each: ramps, wheelchairs and volunteers for persons with disabilities; Braille on EVMs for visually impaired voters; voting from home for those above 85 and PwDs with 40% disability (as in 2024); Saksham app to find the polling station and register; ETPBS for service voters; attention to senior citizens, transgender persons and PVTGs through awareness.", "H", wp=True),
W("Case study. On the night before polling a rumour that 'EVMs will be changed' spreads on a messaging group. (i) Which challenge to elections is this? (ii) State two effects on voters. (iii) Suggest two actions the ECI and citizens can take.", 4, "(i) Misinformation / fake news (1). (ii) Voters may lose trust in the process or stay away from voting; may be misled or scared (any two, 1). (iii) The ECI can use awareness campaigns, EVM and VVPAT demonstrations, and the cVIGIL app; citizens should verify facts before forwarding and report false content (any two, 2).", "H", wp=True),
W("'If only one party contests an election, we cannot exercise our choice.' Explain this statement. How do regular multi-party elections help voters?", 3, "Choice means selecting among alternatives; with a single party the voter has nothing to choose, so the election is meaningless (1.5). Several parties and independents give a range of policies and candidates; voters can reward good performance and punish poor performance, which keeps power accountable (1.5).", "H"),
W("Major Anil is posted at a border post far from his home constituency in Rajasthan. (i) What type of voter is he called? (ii) How does the Election Commission help him vote? (iii) Why is this important?", 3, "(i) A service voter (1). (ii) Through the Electronically Transmitted Postal Ballot System (ETPBS), by which postal ballots are sent and cast electronically from outside the constituency (1). (iii) It ensures that those serving the nation also exercise their vote, making elections inclusive (1).", "H", wp=True),
W("Trace the shift from single-party dominance to alliance politics in India, mentioning 1967, 1977 and the major alliances of recent years.", 4, "Until 1967 one party dominated; 1967 ended that dominance and began an era of alliances (1). In 1977, after the Emergency of 1975-77, the Janata Party formed the first coalition government at the Centre (1). Since the late 1990s the NDA (led by the BJP) and the UPA (led by the Congress) were the major alliances (1); the UPA was dissolved in 2023 and reconstituted as the INDIA alliance (1).", "H"),
W("Essay. 'Elections are the heart of democracy, but laws and institutions are needed to protect them.' Discuss with reference to representation and accountability, the electoral system, the laws, the ECI and the challenges.", 5, "Elections let citizens choose representatives and hold them accountable; regular polls give legitimacy and equal voice (1). The electoral system converts votes to seats: FPTP for Lok Sabha and Vidhan Sabha, PR for Rajya Sabha, President, Vice President and Vidhan Parishad (1). Laws: RPA 1950 (rolls, delimitation), RPA 1951 (conduct, corrupt practices) and the 1952 Act for President and Vice President (1). The ECI (Articles 324-329) prepares rolls, fixes the schedule, registers parties, allots symbols and ensures fairness through the Model Code of Conduct, EVMs, VVPAT and apps (1). Challenges such as misinformation, fake news and intimidation need vigilance by the ECI and citizens (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "Timeline of Key Dates"),
 ("table", ["Year / date", "Event"], [
  ["25 January 1950", "Election Commission of India established (now National Voters' Day)"],
  ["1950", "Representation of the People Act: seats, delimitation, electoral rolls"],
  ["1951", "Representation of the People Act: conduct of elections, offences, corrupt practices"],
  ["1952", "Presidential and Vice-Presidential Elections Act; first Delimitation Commission"],
  ["1963, 1973", "Second and third Delimitation Commissions"],
  ["1967", "End of single-party dominance; era of alliances begins"],
  ["1975-1977", "The Emergency"],
  ["1977", "Janata Party forms the first coalition government at the Centre"],
  ["1985", "52nd Amendment: Anti-Defection Law"],
  ["2002", "Fourth Delimitation Commission"],
  ["2023", "UPA dissolved and reconstituted as the INDIA alliance"],
  ["2024", "General Elections: voting from home extended nationwide for 85+ and PwDs with 40% disability; over 96.8 crore eligible voters"]]),
 ("h2", "Key Terms at a Glance"),
 ("table", ["Term", "Meaning"], [
  ["**Direct election**", "Citizens vote directly to choose their representatives"],
  ["**Indirect election**", "Citizens elect representatives who then choose the leaders or members"],
  ["**Electoral system**", "The method of converting votes into seats"],
  ["**FPTP (plurality)**", "The candidate with the most votes in a constituency wins, even without 50%"],
  ["**Proportional representation**", "Seats are given to parties in proportion to their votes"],
  ["**Quota**", "Minimum votes needed to win under the single transferable vote"],
  ["**Delimitation**", "Fixing the number of seats and boundaries of constituencies"],
  ["**Electoral roll**", "List of eligible voters of a constituency or polling station"],
  ["**Model Code of Conduct**", "Rules of fair conduct for parties and candidates during elections"],
  ["**EVM / VVPAT**", "Electronic Voting Machine / Voter Verifiable Paper Audit Trail"],
  ["**Whip**", "Party direction to members on how to vote in the House"],
  ["**Service voter**", "A voter in the armed forces or on service away from home; uses ETPBS"],
  ["**RUPP**", "Registered unrecognised political party"]]),
 ("h2", "Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["Constituencies with very unequal populations", "Votes carry unequal weight, so Delimitation Commissions redraw them"],
  ["Members switching parties for personal gain", "Unstable governments; Anti-Defection Law of 1985"],
  ["Names missing or wrongly included in rolls", "Special Intensive Revision to correct them"],
  ["Gifts, caste appeals and misuse of government staff", "Corrupt practices listed in RPA 1951 and the Model Code of Conduct"],
  ["Barriers faced by the elderly and persons with disabilities", "Voting from home, Braille EVMs, ramps and the Saksham app"],
  ["Misinformation and fake news", "Awareness drives, VVPAT, cVIGIL and a vigilant media and citizenry"]]),
 ("h2", "Case Notes and Worked Calculations"),
 ("steps", [
  ("Example 1 — Who wins under FPTP?", "Votes: Meena 32,000, Karan 28,000, Farida 20,000, Joseph 10,000. Total 90,000. Meena has the most votes, so she wins with 35.6%, a margin of 4,000. FPTP does not need 50%."),
  ("Example 2 — Quota under STV", "Valid votes 1,20,000; seats 5. Quota = 1,20,000 ÷ (5 + 1) + 1 = 20,001. Any candidate reaching 20,001 first-preference votes is elected; others are decided by elimination and transfer."),
  ("Example 3 — Proportional seats", "60 seats; party gets 40% of the votes, so it gets 40% of 60 = 24 seats. In FPTP the same vote share may give many more or far fewer seats.")]),
 ("h2", "Comparing the Systems in India"),
 ("table", ["Body", "Elected how", "System", "Term / note"], [
  ["Lok Sabha", "Directly by voters", "FPTP", "Five years"],
  ["Vidhan Sabha", "Directly by voters", "FPTP", "Five years; six states also have a Vidhan Parishad"],
  ["Local bodies", "Directly by voters", "Elections every five years", "Panchayats, municipal corporations"],
  ["Rajya Sabha", "Indirectly", "Proportional representation (STV)", "Members elected by state legislators"],
  ["President, Vice President", "Indirectly", "Proportional representation (STV)", "Presidential and Vice-Presidential Elections Act, 1952"],
  ["Vidhan Parishad", "Indirectly (and some nominated)", "Proportional representation (STV)", "In AP, Bihar, Karnataka, Maharashtra, Telangana, UP"]]),
 ("h2", "Map and Chart Pointers"),
 ("ul", ["On a map of India mark the **six states with a Vidhan Parishad**: Andhra Pradesh, Bihar, Karnataka, Maharashtra, Telangana and Uttar Pradesh.",
  "Study the chapter's bar charts of voter turnout in general elections (1951 to 2024): note the rise in the number of eligible voters to over 96.8 crore in 2024.",
  "Locate your own district headquarters and note the offices that run elections locally: the District Magistrate and the Returning and Electoral Registration Officers."]),
 ("h2", "Common Mistakes to Avoid"),
 ("note", "REMEMBER", "FPTP means a plurality, not a majority: the winner need not have more than 50% of the votes. The two-round system is the one that needs more than 50%."),
 ("note", "REMEMBER", "The Rajya Sabha is **not** elected by the people directly and does **not** use FPTP; the Lok Sabha does. Do not mix the 1950 and 1951 Acts: 1950 is rolls and delimitation; 1951 is conduct and corrupt practices."),
 ("note", "REMEMBER", "The Election Commission is autonomous and does not work under the ruling party. Its powers are in Articles 324 to 329, while the Delimitation Commission works under Article 82."),
 ("h2", "More Likely Questions"),
 ("qa", [
  ("How do the Representation of the People Acts of 1950 and 1951 help free and fair elections? (5 marks)", "The 1950 Act deals with the allocation of seats, delimitation of constituencies and the preparation and revision of electoral rolls, and gives every citizen above 18 the right to vote without discrimination. The 1951 Act deals with conduct: nomination, campaigns, voting and settlement of disputes, and lists electoral offences and corrupt practices such as bribery, appeals on grounds of religion or caste and misuse of government staff. Together they make the rules clear and punish unfair practice."),
  ("Explain how FPTP can produce results that are not proportional to votes. (3 marks)", "In FPTP the candidate with the most votes wins each constituency, even with less than 50%. A party that narrowly wins many seats can get a large share of seats with a smaller share of votes, while another with more total votes may win fewer seats."),
  ("Why are Delimitation Commissions important? (3 marks)", "They fix the number of seats and boundaries so that constituencies have nearly equal populations, which makes every vote of nearly equal value and keeps representation fair. Article 82 provides for them; there were commissions in 1952, 1963, 1973 and 2002."),
  ("How does technology help in conducting elections? (3 marks)", "Apps such as cVIGIL, Suvidha, Saksham, Sugam, Voter Helpline and ERONET handle complaints, permissions, services for PwDs, vehicles and rolls; ETPBS helps service voters; EVMs with VVPAT and Braille make voting transparent and inclusive."),
 ]),
]
CH["takeaways"] += ["Remember the dates: **25 January 1950** (ECI), **1985** (Anti-Defection Law), **1977** (first coalition at the Centre), **2024** (voting from home extended nationwide).",
  "Quota (STV) = (valid votes ÷ (seats + 1)) + 1. FPTP needs a plurality, not 50%."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
