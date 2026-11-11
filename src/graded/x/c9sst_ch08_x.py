"""Class 9 SST Ch 8 Elections - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The First-Past-The-Post system can elect a candidate with less than 50 per cent of the votes.", "The candidate with the most votes wins even if the remaining votes are split among many candidates.", "a",
     "A plurality, not a majority, is enough in FPTP."),
 AR4("Members of the Rajya Sabha are elected by proportional representation by the single transferable vote.", "Members of the Lok Sabha are elected by the First-Past-The-Post system.", "b",
     "Both are true, but the Lok Sabha system does not explain the Rajya Sabha method."),
 AR4("The Anti-Defection Law applies to legislators who voluntarily give up their party membership.", "It disqualifies ordinary voters who change the party they support.", "c",
     "The law applies to elected members, not voters; R is false."),
 AR4("The President of India is elected directly by the citizens.", "The head of state in India is elected indirectly.", "d",
     "The President is elected by an electoral college of elected members; A is false and R is true."),
 AR4("Delimitation ensures equal representation.", "It fixes constituency boundaries and the number of seats according to population.", "a",
     "Without delimitation, some constituencies would have far more voters than others."),
 AR4("VVPAT is used with the EVM for voter verification.", "The cVIGIL app lets citizens report Model Code of Conduct violations.", "b",
     "Both are true but they serve different purposes."),
]

CASE = [
 Q("<b>Case study.</b> In a Lok Sabha constituency, candidate X gets 45 per cent of the votes, Y gets 40 per cent and Z gets 15 per cent. Under the system used for Lok Sabha elections, X is declared elected. "
   "(i) Name the system used for Lok Sabha elections. (ii) Who wins under this system? (iii) Did X win a majority of the votes? (iv) If a two-round system were used, what would happen next, and why can FPTP lead to a winner with less than 50 per cent votes?",
   "(i) First-Past-The-Post (1). (ii) The candidate with the most votes (1). (iii) No, 45 per cent is less than 50 per cent (1). (iv) A second round would be held between X and Y (1); in FPTP votes are split among many candidates, and the highest vote-getter wins (1).", "1+1+1+2"),
 Q("<b>Case study.</b> The Election Commission of India was established on 25 January 1950 and gets its powers from Articles 324-329. District Election Officers are usually District Magistrates. One constituency has 25 lakh voters while another has only 5 lakh voters. The Commission carries out a Special Intensive Revision of the rolls. "
   "(i) When was the Election Commission established? (ii) Who usually serves as a District Election Officer? (iii) What is delimitation? (iv) Which principle is violated in the two constituencies and how can it be corrected?",
   "(i) 25 January 1950 (1). (ii) The District Magistrate (1). (iii) Fixing the boundaries and the number of constituencies (seats) (1). (iv) Equal representation is violated, because votes carry unequal weight (1); delimitation redraws boundaries so that constituencies have roughly equal numbers of voters (1).", "1+1+1+2"),
 Q("<b>Case study.</b> For the 2024 elections the Election Commission extended voting from home to voters above 85 years and persons with disabilities. A citizen sees loudspeakers used beyond the permitted time and reports it through the cVIGIL app. The Saksham app helps persons with disabilities, and VVPAT slips verify the votes cast on EVMs. "
   "(i) For which purpose is the cVIGIL app used? (ii) Whom does the Saksham app help? (iii) What is the age above which voting from home was extended? (iv) State the purpose of the Model Code of Conduct and why VVPAT is used.",
   "(i) Reporting Model Code of Conduct violations (1). (ii) Persons with disabilities (1). (iii) 85 years (1). (iv) The Model Code ensures a level playing field for all parties and candidates during elections (1); VVPAT allows voters to verify that their vote was recorded correctly (1).", "1+1+1+2"),
]

MISTAKES = [
 "FPTP gives victory to the candidate with the <b>most</b> votes (a plurality), not necessarily more than 50 per cent; do not call it a majority.",
 "Lok Sabha: direct election by FPTP. Rajya Sabha: PR by single transferable vote. President: indirect election. Do not interchange them.",
 "Delimitation means fixing constituency boundaries and seats; it is not the same as drawing up electoral rolls or counting votes.",
 "The Election Commission is a constitutional body (Articles 324-329) established on 25 January 1950; the Model Code of Conduct is a set of guidelines for parties and candidates.",
 "The Anti-Defection Law applies to elected members who voluntarily give up party membership, not to voters.",
 "Proportional representation gives seats in proportion to votes; do not confuse it with PR-STV used for Rajya Sabha, and know EVM, VVPAT, cVIGIL, Saksham and ERONET by purpose.",
]
