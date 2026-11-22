"""Class 9 Social Science Ch 12 - Governance and Public Policy (Political Science, Part 2): worksheet + detailed notes."""
import importlib.util, copy
from libws import *          # W, run
BANK = "c9sst_ch12"

def _base():
    s = importlib.util.spec_from_file_location("c9sst_c12", str(REPO / "src/rn_work/c9_sst2/c12.py"))
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return copy.deepcopy(m.CH)

WS = [
# ---------------- EASY ----------------
W("Making decisions and information open and accessible to the public is called:", 1, "(c) transparency", "E", opts=["accountability", "inclusiveness", "transparency", "effectiveness"]),
W("The motto of the Supreme Court of India, 'Yato Dharmastato Jayah', is taken from the:", 1, "(a) Mahabharata", "E", opts=["Mahabharata", "Arthashastra", "Rigveda", "Mundaka Upanishad"]),
W("The Sengol, a symbol of righteous rule, was placed in the new Parliament building in:", 1, "(b) 2023", "E", opts=["1947", "2023", "2020", "1950"]),
W("The platform that brings many government services onto one app is:", 1, "(d) UMANG", "E", opts=["GeM", "APAAR", "CPGRAMS", "UMANG"]),
W("DigiLocker is used for:", 1, "(a) digital storage of documents", "E", opts=["digital storage of documents", "purchases by government departments", "filing public grievances", "voting online"]),
W("The expert committee for the National Education Policy 2020 was chaired by:", 1, "(c) Dr K. Kasturirangan", "E", opts=["Dr B.R. Ambedkar", "Dr Rajendra Prasad", "Dr K. Kasturirangan", "Dr A.P.J. Abdul Kalam"]),
W("Janani Suraksha Yojana, in the health sector, is an example of a:", 1, "(b) scheme", "E", opts=["policy", "scheme", "court order", "constitutional amendment"]),
W("Which of these is a public policy?", 1, "(d) A government policy to give universal access to quality healthcare", "E", opts=["A school's rule on uniform for its students", "A company's leave policy", "A housing society's parking rule", "A government policy to give universal access to quality healthcare"]),
W("Differentiate between government and governance in one line each.", 2, "Government: the institutions (legislature, executive, judiciary) that exercise political authority, focusing on 'who governs' (1). Governance: the process of decision-making, implementation and monitoring, focusing on 'how' governing is carried out (1).", "E"),
W("List any four features of good governance.", 2, "Any four: rule of law, accountability, participation, transparency, effectiveness, responsiveness, inclusiveness. (0.5 each)", "E"),
W("Define e-governance.", 2, "E-governance is the use of information and communication technology by the government to provide services, share information, receive feedback and improve administration. (2)", "E"),
W("State True or False, with a reason: The rules made by a housing society are public policy.", 2, "False (1). They apply only to a limited group and are not made for the whole public by public institutions with public funds (1).", "E"),
W("Name the six stages of the policy cycle in order.", 2, "Prioritising, formulation, adoption, implementation, monitoring and evaluation. (2, 1 if order is wrong)", "E"),
W("Fill in the blank: The national motto 'Satyameva Jayate' is taken from the ______ Upanishad.", 1, "Mundaka (1)", "E"),
W("What does GeM stand for?", 1, "Government e-Marketplace. (1)", "E"),
W("Whose ideal of governance was 'Ram Rajya'?", 1, "Mahatma Gandhi's. (1)", "E"),
W("Which two assemblies of ancient India are mentioned in the Rigveda as early bodies of governance?", 1, "The Sabha and the Samiti. (1)", "E"),
# ---------------- MEDIUM ----------------
W("A panchayat installs a street light. Explain, using this example, how government and governance are different.", 3, "The panchayat is the government that has the authority to install the light (1). Governance is the whole process: planning, deciding where to place it, repairing it and getting feedback from people who report dark spots (1.5). Governance therefore includes citizens and others, not only government (0.5).", "M", wp=True),
W("Match the feature of good governance with its meaning: (a) rule of law (b) responsiveness (c) inclusiveness (d) effectiveness with (1) every citizen gets equal opportunities (2) public resources are used wisely (3) government addresses people's needs (4) everyone is equal before the law.", 3, "(a)-(4); (b)-(3); (c)-(1); (d)-(2). (3 for all four, 2 for three)", "M"),
W("What was Rajadharma? What does Kautilya say about the happiness of a king?", 3, "Rajadharma was the king's duty to protect his people and uphold dharma (1.5). Kautilya says that the king's happiness lies in the happiness of his people (1.5).", "M"),
W("What is the Sengol? Why is it considered a symbol of good governance?", 3, "The Sengol is a Chola-era symbol of righteous rule (1). Nehru received it on 15 August 1947 from Adheenam saints of Tamil Nadu and it was placed in the new Parliament in 2023 (1). It reminds rulers that power comes with the responsibility of ensuring good governance (1).", "M"),
W("State three advantages and one limitation of e-governance.", 3, "Advantages: reduces paperwork, saves visits to offices, speeds up services and improves transparency (any three, 2). Limitation: it needs devices, internet and digital skills, so it can leave some people out (1).", "M"),
W("Match the e-governance initiative with its purpose: (a) CPGRAMS (b) APAAR (c) GeM (d) Aadhaar with (1) unique identity (2) purchases by the Government (3) public grievances (4) education-related digital identity.", 3, "(a)-(3); (b)-(4); (c)-(2); (d)-(1). (3 for all four, 2 for three)", "M"),
W("Why is public policy called 'public'? Give three reasons.", 3, "It is made for public benefit (1), carried out by public institutions (1), financed by public money, and shaped by the people and their needs (1).", "M"),
W("Match the stakeholder with its role in policy-making: (a) citizens (b) elected representatives (c) civil society and media (d) private sector with (1) raise issues in the legislature and approve budgets (2) identify problems, vote and give feedback (3) study, create awareness and monitor (4) provide resources and innovation.", 3, "(a)-(2); (b)-(1); (c)-(3); (d)-(4). (3 for all four, 2 for three)", "M"),
W("Case. Patients and a disability group complained that a district hospital had no ramps. Show how this moved through the policy cycle by placing these in order: funds approved, inspection ordered by the district, experts consulted, issue raised.", 3, "Issue raised (prioritising) → inspection ordered by the district and experts consulted (formulation) → funds approved (adoption) (3, 2 if one wrongly placed).", "M", wp=True),
W("Timeline. Arrange the steps in the making of the National Education Policy 2020: (i) Cabinet approval (ii) expert committee under Dr Kasturirangan (iii) the process begins (iv) consultation with Gram Panchayats, blocks, urban local bodies and districts. Give the years.", 3, "(iii) the process began in 2015; (ii) committee in 2017; (iv) wide consultation with about 2 lakh suggestions; (i) Union Cabinet approval in July 2020. (3 for correct order with years, 2 for order)", "M"),
W("Classify as policy, programme or scheme (health sector): (a) universal access to quality healthcare (b) Ayushman Bharat PM-JAY (c) strengthening public healthcare and preventive care.", 3, "(a) Policy: sets direction and goal; (b) scheme: gives concrete benefits; (c) programme: turns goals into strategies. (1 each)", "M"),
W("Who does what under the Khelo Bharat Niti 2025? Write the role of the Union, states and districts.", 3, "Union: the policy framework and funding (1). States: become 'Model Sports States', host national games and build infrastructure, attract private investment through PPP (1). Districts: become 'Model Sports Districts' by improving sports capabilities; blocks organise regular events and scout talent (1).", "M"),
W("State three challenges to good governance.", 3, "Any three: weak coordination, unequal access to services, misuse of office, fake news. (1 each)", "M"),
W("Find the mistake: 'Governance means only what the government does.' Correct it.", 2, "Wrong (1). Governance also involves citizens, media, civil society and the private sector who take part in making, implementing and monitoring decisions (1).", "M"),
W("Why is the participation of citizens necessary for good governance? Give two ways they can take part.", 3, "Citizens know local problems and make government accountable and responsive (1). Ways: vote; obey laws; raise concerns; give feedback; join consultations and attend gram sabhas (any two, 2).", "M"),
W("What are the roles of the media and civil society in governance?", 3, "The media informs people and exposes problems (1.5). Civil society (NGOs and groups) raises awareness, studies issues, and monitors government work (1.5).", "M"),
W("What did Gandhi mean by 'Ram Rajya'?", 2, "An ideal of governance based on probity, transparency, compassion and welfare for all (2).", "M"),
W("An old farmer in a remote village has no smartphone or internet. Why does this matter for e-governance and what should the government do?", 3, "E-governance works only with devices, internet and digital skills, so people without them are left out (1.5). The government must keep offline options such as help centres and training and make services inclusive (1.5).", "M", wp=True),
W("Why does the policy cycle include monitoring and evaluation?", 2, "Monitoring tracks progress and ensures accountability while implementation is going on (1). Evaluation assesses results and gives feedback for improving the policy (1).", "M"),
# ---------------- HARD ----------------
W("Case study. Residents of a village in Rajasthan face a shortage of drinking water. Apply the six stages of the policy cycle to design a response, with one action at each stage.", 5, "Prioritising: gram sabha lists water as the first need (1). Formulation: consult villagers, engineers and NGOs, draft a plan and estimate cost (1). Adoption: panchayat passes resolution and the district approves funds (1). Implementation: build the tank and pipelines through officials and local workers (1). Monitoring and evaluation: check water supply, keep a complaint system, and evaluate results to improve (1).", "H", wp=True),
W("Case study. A hospital without ramps was improved after patients and a disability group raised the matter. Identify which stakeholders played which role and explain what it shows about governance.", 4, "Patients and the disability group: citizens who identified the problem and gave feedback (1). The district authority asked PWD and the Health Department to inspect: officials who prepared and implemented the action (1). Experts were consulted and funds approved: formulation and adoption (1). It shows that governance is a shared process in which citizens, officials and experts take part, making government responsive and inclusive (1).", "H", wp=True),
W("Using the health sector example (National Health Policy 2017), explain the difference between policy, programme and scheme, with one example of each.", 4, "Policy sets the direction and goals, e.g. universal access to quality healthcare, affordability and accountability (1.5). A programme turns goals into strategies, e.g. strengthening public healthcare, preventive care and digital health (1.5). A scheme gives specific benefits to people, e.g. Ayushman Bharat PM-JAY, Janani Suraksha Yojana or Mission Indradhanush (1).", "H"),
W("Case study. A village has patchy mobile networks and most elders cannot read English. The government wants all services online. Suggest four steps that keep e-governance inclusive.", 4, "Four steps, 1 each: improve connectivity; offer services in local languages; set up common service or help centres with trained staff; digital literacy training and awareness; keep offline options for those who cannot use technology; ensure privacy and grievance redressal through CPGRAMS.", "H", wp=True),
W("Case study. Meena wants to start a girls' kabaddi and athletics club in her block in Rajasthan. Using the Khelo Bharat Niti, explain what support she can expect from the block, district, state, private bodies and the Union Government.", 4, "Block: regular sporting events and talent scouting (1). District: Model Sports District with better facilities (1). State: Model Sports State, infrastructure, hosting tournaments and attracting private investment through PPP (1). Private bodies: sponsorship and research on nutrition and equipment; Union: policy framework and funding; families support girls and give feedback (1).", "H", wp=True),
W("Source-based. 'The king's happiness lies in the happiness of his subjects.' (Kautilya's Arthashastra, as in the chapter). (i) What does it say about the purpose of governance? (ii) Link it with the Constitution's vision.", 3, "(i) The ruler's own welfare is linked with the welfare of the people, so the purpose of governance is the well-being of all, not personal power (1.5). (ii) The Indian Constitution is framed in the spirit of Indian values and gives government the responsibility of ensuring welfare and good governance (1.5).", "H"),
W("Trace how governance ideas of ancient India (Sabha and Samiti, Rajadharma, Arthashastra) and the freedom movement (Gandhi's Ram Rajya) are reflected in the present system.", 4, "The Rigveda mentions Sabha and Samiti as early participatory bodies (1). Rajadharma and Kautilya tied rule to protecting the people (1). Gandhi's Ram Rajya stressed probity, transparency, compassion and welfare (1). The motto 'Satyameva Jayate', the Supreme Court's motto and the Sengol in Parliament show these traditions in the Constitution's institutions (1).", "H"),
W("The NEP 2020 was prepared after consulting 2.5 lakh Gram Panchayats, about 6,600 blocks, 6,000 urban local bodies and 676 districts, with about 2 lakh suggestions. Why is this a good example of collaborative policy-making? What would be the risk of a policy made without consultation?", 4, "It involved citizens, local bodies, experts and the Government at all levels, so the policy reflects real needs and gains acceptance (2). Without consultation the policy may ignore local problems, be hard to implement and lack public trust (2).", "H"),
W("Evaluate: 'Good governance is the sole responsibility of the government.' Give two arguments against it with examples of other actors.", 4, "Government makes laws and policies and delivers services (1). But citizens vote, obey laws and give feedback (1); the media informs and exposes wrongdoing; civil society raises awareness and monitors; the private sector adds economic activity and resources, e.g. PPP in sports and solar panels (2).", "H"),
W("Case study. Ramesh waits for months for a pension approval because the file moves from table to table and nobody tells him the status. Explain how transparency, accountability and e-governance could help him.", 4, "Transparency: the status and the process are open and accessible to him (1). Accountability: officials answer for delays and can be questioned (1). E-governance: online application, tracking, DigiLocker documents and a CPGRAMS grievance cut paperwork and visits (1.5). Together they make service faster and build trust (0.5).", "H", wp=True),
W("Explain the role of the private sector in public policy with the examples of solar panels and sports. What precautions does the Government need?", 3, "The private sector brings resources, innovation and efficiency through PPPs such as solar panels or sports infrastructure and sponsorship (1.5). The Government must make sure the public interest, fair access and accountability are not lost (1.5).", "H"),
W("How do international organisations contribute to public policy? Give an example.", 3, "They share experience, technical know-how and financial help with countries (1.5). Example: the WHO helps countries in disease control and in framing health policy (1.5).", "H"),
W("Essay. Describe the policy cycle with a suitable example, showing how each stage links to the next and how citizens can take part at each stage.", 5, "Choose an example such as safe roads near a school. Prioritising: parents and students raise the problem (1). Formulation: consult officials, experts and check cost (1). Adoption: approve the plan and funds (1). Implementation: build the zebra crossing and speed breakers; Monitoring and evaluation: citizens report problems and results are reviewed for improvement (2).", "H"),
W("Essay. 'Democracy needs more than elections.' Discuss, using the ideas of governance, good governance and participation.", 4, "Elections choose representatives, but democracy also requires institutions working openly (1). Governance is the process of deciding, implementing and monitoring decisions (1). Good governance, through the rule of law, accountability and transparency, builds trust (1). Participation of citizens and others keeps government responsive between elections (1).", "H"),
]

CH = _base()
CH["blocks"] += [
 ("h2", "Timeline and Key References"),
 ("table", ["Date / item", "What it is"], [
  ["Rigveda", "Mentions the Sabha and the Samiti"],
  ["Arthashastra (Kautilya)", "The king's happiness lies in the happiness of his people"],
  ["15 August 1947", "Nehru received the Sengol from the Adheenam saints of Tamil Nadu"],
  ["2015, 2017", "NEP process begins; Kasturirangan Committee"],
  ["July 2020", "Union Cabinet approves the National Education Policy 2020"],
  ["2017", "National Health Policy"],
  ["2023", "Sengol placed in the new Parliament building"],
  ["2025", "Khelo Bharat Niti"]]),
 ("h2", "Key Terms and Initiatives"),
 ("table", ["Term", "Meaning"], [
  ["**Governance**", "Process of decision-making, implementation and monitoring for welfare"],
  ["**Rajadharma**", "The ruler's duty to protect the people and uphold dharma"],
  ["**Rule of law**", "Everyone is equal before the law"],
  ["**Accountability**", "Officials answer for their decisions and actions"],
  ["**Transparency**", "Decisions and information are open to the public"],
  ["**E-governance**", "Using ICT for services, information and feedback"],
  ["**PPP**", "Public-private partnership"],
  ["**Stakeholder**", "Anyone affected by or contributing to a policy"],
  ["**UMANG, GeM, DigiLocker, CPGRAMS, APAAR, Aadhaar**", "Platform for services; e-marketplace; digital documents; grievances; education identity; unique identity"],
  ["**NEP 2020, NHP 2017, Khelo Bharat Niti 2025**", "National policies in education, health and sports"]]),
 ("h2", "Cause and Effect"),
 ("table", ["Cause", "Effect"], [
  ["People report problems and give feedback", "Policies become responsive and are adjusted"],
  ["Officials answer for actions; information is open", "Accountability and trust"],
  ["Services moved to online platforms", "Less paperwork and fewer office visits; risk of excluding the digitally unskilled"],
  ["Wide consultation in policy-making (NEP 2020)", "Policy reflects real needs and gets acceptance"],
  ["Unequal access, misuse of office, fake news", "Challenges to good governance"]]),
 ("h2", "Worked Case Notes"),
 ("steps", [
  ("Example 1 — Water shortage in a village", "Prioritising: gram sabha lists it as the top need. Formulation: consult experts and prepare the plan. Adoption: panchayat resolution and funds. Implementation: tank and pipes built. Monitoring: supply checked. Evaluation: results reviewed."),
  ("Example 2 — Hospital ramps", "Patients and a disability group raise the issue; the district asks PWD and Health Department to inspect; experts consulted; funds approved; ramps built. Citizens, officials and experts share the work."),
  ("Example 3 — Policy, programme, scheme", "Policy: universal access to quality healthcare. Programme: strengthen public healthcare. Scheme: Ayushman Bharat PM-JAY gives families health cover.")]),
 ("h2", "Diagram Pointers"),
 ("ul", ["Draw the **policy cycle** as a loop of six boxes (prioritising → formulation → adoption → implementation → monitoring → evaluation) with an arrow from evaluation back to prioritising.",
  "Draw the **three-level pyramid**: policy (top), programme (middle), scheme (base) with the health examples.",
  "Draw a web with **government, citizens, media, civil society and private sector** around 'governance'."]),
 ("h2", "Common Mistakes"),
 ("note", "REMEMBER", "Do not say governance and government are the same. Government = institutions; governance = the process involving many actors."),
 ("note", "REMEMBER", "Policy, programme and scheme form a chain: policy sets direction, programme turns it into strategy, scheme gives actual benefits to people."),
 ("h2", "More Likely Questions"),
 ("qa", [
  ("Explain how colonial rule and Indian traditions influenced governance in independent India. (3 marks)", "Colonial rule introduced its own institutions and many continued after independence, but the Constitution was framed in the spirit of Indian values: the national motto from the Mundaka Upanishad, the Supreme Court's motto from the Mahabharata, the Sengol and Gandhi's Ram Rajya reflect older ideas of righteous rule."),
  ("Why is good governance important for a country? (3 marks)", "It maintains law and order, protects rights, delivers services, uses resources wisely and builds public trust through transparency, accountability and participation."),
  ("Explain the role of various stakeholders in public policy. (5 marks)", "Citizens identify problems, vote and give feedback; elected representatives raise issues, pass laws and approve budgets; officials and departments prepare, implement and monitor; civil society, media and experts study, create awareness and monitor; the private sector gives resources and innovation; international organisations give experience and technical or financial help."),
  ("Why is policy coordination important? Use Khelo Bharat Niti. (3 marks)", "Different levels do different tasks: the Union gives the framework and funds, states build infrastructure and host events, districts and blocks organise sport and scout talent, private bodies sponsor, and citizens give support and feedback. Coordination avoids gaps and duplication."),
 ]),
]
CH["takeaways"] += ["Remember the **six steps** of the policy cycle and the **seven features** of good governance; link them to the hospital-ramp and NEP 2020 examples.",
  "Policy (direction) → programme (strategy) → scheme (benefits): **National Health Policy 2017** is the chapter's model."]

if __name__ == "__main__": run(__file__, BANK, 9, "Social_Science", WS, CH)
