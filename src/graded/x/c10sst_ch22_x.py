"""Class 10 SST Ch 22 Sectors of the Indian Economy - extras."""
from common import AR4, Q

AR = [
 AR4(r"Only final goods and services are counted while calculating the GDP.", r"The value of final goods already includes the value of all the intermediate goods used in making them, so counting the latter again would be double counting.", "a",
     r"Counting intermediate goods separately would count the same value twice; R explains A."),
 AR4(r"Cotton cultivation belongs to the primary sector.", r"Making cloth from cotton in a textile mill belongs to the secondary sector.", "b",
     r"Both are true; they are consecutive stages but R does not explain why cultivation is primary."),
 AR4(r"The tertiary sector is the largest producing sector in India.", r"Most of the workers of India are employed in the tertiary sector.", "c",
     r"A is true: in terms of production it has overtaken the primary sector. R is false: the primary sector, mainly agriculture, is still the largest employer."),
 AR4(r"Workers in the unorganised sector enjoy job security and paid leave.", r"The unorganised sector consists of small and scattered units where rules and regulations exist but are not followed.", "d",
     r"A is false: jobs are low-paid, not regular and lack paid leave. R is true."),
 AR4(r"There is disguised unemployment in the agricultural sector in India.", r"More people work on the small farms than are actually needed, so even if some are moved out, production would not suffer.", "a",
     r"The surplus workers in a family plot make the unemployment hidden; R explains A."),
 AR4(r"Railways and the post office are examples of the public sector.", r"Companies like Tata Iron and Steel Company Limited (TISCO) belong to the private sector.", "b",
     r"Both are true, but the TISCO fact does not explain why railways and the post office are public."),
]

CASE = [
 Q(r"<b>Case study.</b> A farmer sells wheat to a flour mill for Rs 20 per kg. The mill grinds it and sells the flour to a biscuit company at Rs 25 per kg. The company makes biscuits from the flour, sugar and oil and sells four packets at Rs 20 each to consumers. A student wants to compute the contribution of this chain to GDP. "
   r"(i) Name the final good in this chain. (ii) Name one intermediate good. (iii) What is the value of the final good sold, if four packets are sold at Rs 20 each? (iv) Why should only the final goods be counted in GDP?",
   r"(i) Biscuits (1). (ii) Wheat or flour (1). (iii) 4 x 20 = Rs 80 (1). (iv) The value of final goods already includes that of intermediate goods, so counting wheat and flour again would amount to double counting (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Laxmi owns two hectares of unirrigated land and grows jowar and arhar depending on rain. All five members of her family work on the plot throughout the year, though the work can be done by three. A neighbouring landowner hires two of them. The family's income rises, and the production on Laxmi's plot does not fall. "
   r"(i) What kind of unemployment is seen in Laxmi's family? (ii) Which sector is Laxmi's work part of? (iii) How many extra persons are working on the plot? (iv) Why does production not fall when two members leave the plot?",
   r"(i) Disguised unemployment (underemployment) (1). (ii) Primary sector (1). (iii) Two (five minus three) (1). (iv) The plot needs only three persons; the two moved out were surplus, so the work is still done, and their wages add to the family income (2).", "1+1+1+2"),
 Q(r"<b>Case study.</b> Kanta works in an office from 9.30 a.m. to 5.30 p.m. and gets a regular salary, paid leave and a pension after retirement. Kamal works for a small shop owner. He has no fixed hours, no paid leave and may be asked to leave anytime. Both of them work in the services sector. "
   r"(i) In which sector does Kanta work, organised or unorganised? (ii) Which of the two enjoys job security? (iii) Name one Act that organised sector workers are covered under. (iv) Why do workers in the unorganised sector need protection?",
   r"(i) Organised sector (1). (ii) Kanta (1). (iii) Any one: Factories Act, Minimum Wages Act, Payment of Gratuity Act, Shops and Establishments Act (1). (iv) Their jobs are low-paid, irregular and without benefits, rules are not followed, and many belong to disadvantaged groups who face discrimination, so they need protection and support (2).", "1+1+1+2"),
]

MISTAKES = [
 r"Mixing up the sectors: <b>primary</b> (natural products: agriculture, dairy, fishing, forestry), <b>secondary</b> (manufacturing), <b>tertiary</b> (services); cotton growing is primary but making cloth from it is secondary.",
 r"Counting <b>intermediate goods</b> along with final goods in GDP; this is double counting.",
 r"Saying the tertiary sector employs most people: it produces the most, but <b>primary</b> still employs the largest share of workers.",
 r"Confusing <b>disguised unemployment</b> (many working, but some surplus, hidden) with open unemployment (no work at all).",
 r"Using 'organised/unorganised' for 'public/private': <b>organised vs unorganised</b> is about registration and rules; <b>public vs private</b> is about ownership of assets.",
 r"Calling the unorganised sector 'illegal'; it is a sector of small, scattered units where rules are <b>not followed</b>.",
]
