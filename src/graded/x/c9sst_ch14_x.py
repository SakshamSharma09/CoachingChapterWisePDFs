"""Class 9 SST Ch 14 From Ideas to Startups - Hard-tier extras (AR, case-based) and mistakes box."""
from common import AR4, Q

AR = [
 AR4("The rent of a shop is a fixed cost.", "It does not change with the number of units produced.", "a",
     "Fixed costs have to be paid whatever the level of output."),
 AR4("Lijjat Papad was started in 1959.", "Mohan Singh Oberoi worked first as a hotel clerk.", "b",
     "Both are true but they concern different entrepreneurs."),
 AR4("Profit is revenue minus costs.", "Revenue is the money spent by a business on raw materials.", "c",
     "Revenue is the money received from sales; money spent on raw materials is a cost, so R is false."),
 AR4("A great business idea by itself guarantees success.", "Success also needs finance, human resources, operations and marketing.", "d",
     "An idea alone does not ensure success, so A is false; R is true."),
 AR4("Entrepreneurs have to take risks.", "Profit is not guaranteed in business.", "a",
     "Because returns are uncertain, an entrepreneur must take calculated risks."),
 AR4("Variable costs rise as output increases.", "A unicorn is a startup valued at over 1 billion dollars.", "b",
     "Both are true but unrelated."),
]

CASE = [
 Q("<b>Case study.</b> A bakery has a fixed cost of Rs 30,000 a month and a variable cost of Rs 10 per cake. Each cake is sold at Rs 25. In one month it makes and sells 1,000 cakes. "
   "(i) What is the bakery's total cost for 1,000 cakes? (ii) What is its revenue? (iii) What is its profit or loss? (iv) How many cakes must it sell to break even, and what is meant by break-even?",
   "(i) 30,000 + 10 x 1,000 = Rs 40,000 (1). (ii) 25 x 1,000 = Rs 25,000 (1). (iii) Loss of Rs 15,000 (1). (iv) 30,000/(25 - 10) = 2,000 cakes (1); break-even is where revenue equals total cost (1).", "1+1+1+2"),
 Q("<b>Case study.</b> Lijjat Papad began in 1959 with an initial amount of Rs 80. Mohan Singh Oberoi worked first as a hotel clerk and mortgaged his wife's jewellery to buy a hotel; he later received the Padma Bhushan in 2001. The Chettiars of Tamil Nadu were traders and bankers who reinvested part of their profit in welfare. "
   "(i) With how much money did Lijjat start? (ii) In which job did Oberoi start his career? (iii) In which year did he receive the Padma Bhushan? (iv) What quality did Oberoi show by mortgaging his wife's jewellery, and what ethics did the Chettiars follow?",
   "(i) Rs 80 (1). (ii) Hotel clerk (1). (iii) 2001 (1). (iv) Willingness to take risk (1); trust and reinvestment of profits in welfare (1).", "1+1+1+2"),
 Q("<b>Case study.</b> India has the world's third-largest startup ecosystem. A startup valued at over 1 billion dollars is called a unicorn. A new food-delivery startup in Bengaluru has funds and good products but few customers. It has also hired staff and is training them, and its plan is revised whenever conditions change. "
   "(i) What is a unicorn? (ii) What is India's rank in the startup ecosystem? (iii) Which area of business deals with hiring and training? (iv) Which area is weak in this startup, and why is the business plan called dynamic?",
   "(i) A startup valued at over 1 billion dollars (1). (ii) Third largest in the world (1). (iii) Human resources (1). (iv) Marketing (promotion and sales) (1); a business plan is dynamic because it is revised when conditions change (1).", "1+1+1+2"),
]

MISTAKES = [
 "<b>Revenue</b> is money received from sales; <b>profit</b> = revenue - expenses. A loss occurs when expenses exceed revenue. Do not treat revenue as profit.",
 "Fixed costs (rent) do not change with output; variable costs (raw materials, packaging) rise with output. Total cost = fixed + variable cost.",
 "Break-even is where revenue equals total cost; units = fixed cost / (price - variable cost per unit).",
 "A business plan is not fixed once written; it is a dynamic roadmap revised when conditions change.",
 "A mortgage is a loan taken against property, a chawl is a multi-storey tenement of single-room units, and a unicorn is a startup valued above 1 billion dollars.",
 "Success needs finance, human resources, operations and marketing, not just a great idea; match names with facts (Lijjat 1959, Oberoi - hotels, Chettiars - Tamil Nadu).",
]
