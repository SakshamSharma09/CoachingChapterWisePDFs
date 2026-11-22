"""Class 9 English (Kaveri) Unit 8: Follow That Dream (Irene Chua, letter to Ming) + Step up to the Challenge (Robert Langley): worksheet + detailed notes."""
from libws import *          # W, run
BANK = "c9e_ch08"

WS = [
# ------------------------------------------------------------------ EASY (17)
W("'Follow That Dream' is a letter taken from the collection 'My Daughter, My Friend' by:", 1, "(b) Irene Chua.", "E",
  opts=["Sudha Murty", "Irene Chua", "Mitra Phukan", "Asha Nehemiah"]),
W("The letter is written by a mother to her daughter, whose name is:", 1, "(a) Ming.", "E",
  opts=["Ming", "Shruti", "Sentila", "Johnsy"]),
W("The mother begins the letter with the words:", 1, "(c) 'By all means follow that dream.'", "E",
  opts=["'I am proud of you.'", "'Dreams are only for the young.'", "'By all means follow that dream.'", "'Please stay at home.'"]),
W("To reach world-class standard in any field, the mother says one has to pursue the subject intensively for at least:", 1, "(d) ten years.", "E",
  opts=["one year", "three years", "five years", "ten years"]),
W("The letter is dated:", 1, "(b) 19 June 1995.", "E",
  opts=["15 August 1947", "19 June 1995", "2 October 2000", "1 January 1990"]),
W("'Step up to the Challenge' is a poem by:", 1, "(a) Robert Langley.", "E",
  opts=["Robert Langley", "Charles Swain", "David Roth", "Maya Anthony"]),
W("The poem's rhyme scheme in each stanza is:", 1, "(c) ABCB (the second and fourth lines rhyme).", "E",
  opts=["AABB", "ABAB", "ABCB", "ABBA"]),
W("According to the poem, what is the hardest?", 1, "(d) the first step.", "E",
  opts=["the last step", "the middle of the journey", "the finish line", "the first step"]),
W("What does the mother say makes the difference between greatness and the ordinary?", 2, "How much effort and sacrifice people invest to realise their dream (2).", "E"),
W("Name two fields the mother mentions in which a dream can be pursued.", 2, "Any two: sports, science, arts, business, design (1 + 1).", "E"),
W("Why do the Academy Award winners thank so many people, according to the mother?", 2, "Because a host of people formed the winner's support network (1); for one winner there is a group who stood by him or her (1).", "E"),
W("Give one example from the letter of people whose dreams remained dreams.", 2, "People who wished to go to Raffles College (now the National University of Singapore) but whose destiny was changed by the Japanese invasion in World War II (1), or people who wanted to finish secondary school but had to work to support their siblings (1).", "E"),
W("What dream did the mother chase for the last ten years?", 2, "Publishing her book (1), which was not the dream of her youth, as her original dream had changed over the years (1).", "E"),
W("True or false, with a reason: The mother says Ming should give up her dream if the road is uphill.", 2, "False (1). She says the road may be uphill most of the way, but love for what she does and the prospect of success will keep her going (1).", "E"),
W("What do the first two lines of 'Step up to the Challenge' tell you about facing challenges?", 2, "There is no crowd to see (1): challenges are faced alone and the focus is on you and the future (1).", "E"),
W("Meaning of 'status quo'? Use it in a sentence.", 2, "The existing state of affairs (1). Example: Some villagers wanted to maintain the status quo and not change the school timings (1).", "E"),
W("Sonu from Churu wants to become a cricketer but his village has no ground. Which line from the letter would encourage him and why?", 2, "'By all means follow that dream' or 'the road may be uphill most of the way' (1), because it tells him the road to a goal is hard but worthwhile (1).", "E", wp=True),
# ------------------------------------------------------------------ MEDIUM (19)
W("'Then if it is still burning in your blood and you are ready to commit yourself to the task, plunge.' 'Plunge' means:", 1, "(b) to throw oneself completely into the activity.", "M",
  opts=["to give up", "to throw oneself completely into the activity", "to step back slowly", "to wait"]),
W("'No, I am not going to put a wet blanket on your dreams' means that the mother:", 1, "(a) will not discourage or spoil Ming's enthusiasm.", "M",
  opts=["will not discourage Ming's enthusiasm", "will buy Ming a blanket", "will forbid Ming's dream", "will ignore Ming's letter"]),
W("Which sentence uses 'could' for an unreal or hypothetical situation?", 1, "(c) 'I wish I could be a pilot.'", "M",
  opts=["She could read at the age of four.", "It could rain this evening.", "I wish I could be a pilot.", "Could you repeat the question?"]),
W("In 'If the idea excites you, ____', the best way to complete the sentence with an imperative is:", 1, "(d) 'go ahead and try it', since the first conditional can use an imperative in the main clause.", "M",
  opts=["it will have excited you", "you would be excited", "excites you", "go ahead and try it"]),
W("'There is such ease in comfort to maintain the status quo.' Here 'comfort' stands for:", 1, "(b) the comfort zone that holds one back.", "M",
  opts=["a soft chair", "the comfort zone that holds one back", "good health", "a holiday"]),
W("What advice does the mother give about considering the costs of pursuing a dream?", 3, "Count the cost in years of effort, financial investments and sacrifice (1.5). If, after considering all obstacles, the conviction is still burning in your blood, go ahead (1.5).", "M"),
W("How does the mother balance encouragement and caution in the letter?", 3, "She encourages Ming with 'By all means follow that dream' and says greatness comes from effort (1). She cautions that many dreams remain wishes, that circumstances change lives and that one must consider years and costs (1). She says she will not put a wet blanket on Ming's dreams (1).", "M"),
W("How may life itself change a person's dreams, according to the mother?", 3, "She says that life may change a person's dreams, and the new hopes and aspirations are no less than the original dream (1.5). The mother's own dream changed to publishing her book, which she is excited about (1.5).", "M"),
W("What differentiates mere dreamers from achievers?", 3, "Achievers pursue their dream with effort and sacrifice and commit themselves (1.5). Mere dreamers remain at wishful thinking ('I wish I could be this or that') and never get beyond it (1.5).", "M"),
W("Why does the mother say the number of participants in one's dreamscape would be 'many more'?", 2, "Because a dream that changes and takes longer to realise needs support from more people (1), like the support network that winners thank (1).", "M"),
W("'It's just you and the future and where you want to be.' What does this suggest?", 2, "Each person must face challenges personally (1), with responsibility for the choice and a clear focus on the future (1).", "M"),
W("What is the central idea of the second stanza of the poem?", 2, "Fear and uncertainty make choices difficult as the future approaches (1); we may be pulled forward or pushed back in fear (1).", "M"),
W("Why does the poet say that staying in comfort is not what 'we are made for'?", 3, "Staying with the status quo gives ease but stops growth (1.5). Human beings are made to grow, which needs change and effort (1.5).", "M"),
W("Name one example of antithesis in or after the poem's context and explain it: 'Will it pull you forward or push you back in fear?'", 3, "'Pull you forward' versus 'push you back' are opposites in a parallel structure (1.5). The contrast highlights the choice between courage and fear (1.5).", "M"),
W("Fill in with the correct form of 'could': '___ you repeat the question? I didn't hear it clearly.' and name the function.", 2, "Could (1); a polite or formal request (1).", "M"),
W("Fill in: 'They ____ the shorter route, but they didn't know about it.' (use could have + verb) and name the function.", 2, "could have taken (1); past possibility or speculation (1).", "M"),
W("What does 'coursing through your veins' mean? Use it in your own sentence.", 2, "Flowing strongly through the body (1). Example: Excitement was coursing through her veins before the final (1).", "M"),
W("Identify the tone of the poem and give one detail from it to support.", 2, "The tone is motivational and encouraging (1). Detail: 'You just need to believe in yourself for your future to be on track' (1).", "M"),
W("Explain why 'The first step is the hardest' is a metaphor.", 2, "It does not mean a literal step (1); it stands for beginning a challenge or change, which is the most difficult part (1).", "M"),
# ------------------------------------------------------------------ HARD (14)
W("How does the mother use questions and personal anecdotes to persuade Ming?", 4, "She asks 'Do you know that to reach world-class standard...?' to make Ming think (1.5). She offers her own experience of how her dream changed and how she chased the book for ten years (1.5). She also gives real examples, such as people who missed Raffles College because of the war (1).", "H"),
W("'Great men and women become great because they have a dream and they pursue it till it comes true.' Do you agree? Give reasons with examples (about 80 words).", 4, "Marks: clear opinion (1), reasons from the letter such as effort and sacrifice (1), an example (1), language (1).", "H"),
W("The mother mentions that for many people dreams remain dreams. Do you think her advice is still relevant today? Give reasons.", 4, "Yes (1). Today, students face competition and fear of failure, so one must weigh years, money and sacrifice (1). Mentors and support networks matter (1). Dreams may change, so flexibility is needed (1).", "H"),
W("What 'costs' in terms of effort, sacrifice and time are you willing to invest to pursue your goals? Answer in about 80 words.", 4, "Personal answer. Marks: clear goal (1), costs named (years of effort, money, leaving comforts) (2), language (1).", "H"),
W("Compare the mother's views in 'Follow That Dream' with the poet's message in 'Step up to the Challenge'.", 5, "Both advise pursuing goals despite hurdles (1). The mother stresses effort, sacrifice and a long period of ten years (1). The poet stresses belief in oneself and courage to leave comfort (1). The mother is cautious about costs and adaptable dreams, while the poet is direct and motivational (1). Both say the start needs courage and conviction (1).", "H"),
W("Explain with reference to the poem how comfort can be an enemy of growth.", 4, "There is ease in comfort and in maintaining the status quo (1). But growth needs change: 'this isn't how we grow' (1). Comfort symbolises stagnation and fear of change (1). So one must step out of the comfort zone to grow (1).", "H"),
W("Case study: Divya of Kota wants to join a classical dance academy but her parents are worried about expenses and studies. Using ideas from the letter, write her reply to her mother (about 100 words).", 5, "Marks: letter format (1), reference to counting the cost and effort (2), balanced and respectful tone (1), language (1).", "H", wp=True),
W("Write a reply from Ming to her mother (about 100 words) in response to the letter.", 5, "Marks: format (1), response to the mother's advice, own dream and plan (2), tone (1), accuracy (1).", "H"),
W("Write a letter (about 120 words) to a friend who has lost confidence after failing in the school selection trials, using the idea of 'Step up to the Challenge'.", 5, "Marks: informal letter format (1), encouraging content with ideas such as the first step and belief (2), tone (1), accuracy (1).", "H"),
W("Show how 'dream' and 'sacrifice' are connected in the letter, with two examples from it.", 4, "Dreams need effort and sacrifice to be realised (1). Winners invest years of effort and financial investment (1). People like those who could not attend Raffles College or finish school had to give up their dream for family and circumstances (1). The mother herself spent ten years on her new dream (1).", "H"),
W("'This isn't how we grow.' Explain with reference to the poem's structure how the poet moves from fear to belief.", 4, "Stanza 1: challenge and the future (1). Stanza 2: fear and difficulty of choices (1). Stanza 3: leave comfort and status quo (1). Stanza 4: the first step is hardest but belief keeps the future on track (1).", "H"),
W("Do you think the poet's message that you 'just need to believe in yourself' is realistic? Give your view with reasons.", 4, "Opinion question. Balanced answer: self-belief is essential for beginning, but other factors such as effort, support and resources are needed (as the mother says about a support network) (2 + 1). Language (1).", "H"),
W("Write a speech (about 120 words) for the morning assembly titled 'Follow That Dream', using ideas from the letter and the poem.", 5, "Marks: format and address (1), ideas from the letter (1.5), ideas from the poem (1), persuasion (1), accuracy (0.5).", "H"),
]

CH = dict(num=8, title="Follow That Dream; Step up to the Challenge", tag="English · Kaveri Unit 8",
intro="Unit 8 is about dreams and self-belief. 'Follow That Dream' is a letter from a mother, Irene Chua, to her daughter Ming; 'Step up to the Challenge' by Robert Langley is a short, motivating poem about leaving comfort and taking the first step.",
big_questions=["Why is it important to follow a dream?", "What qualities and costs does a dream demand?", "How can we leave our comfort zone?"],
blocks=[
("h2", "1. The Unit at a Glance"),
("table", ["Item", "Follow That Dream", "Step up to the Challenge"], [
 ["Writer", "Irene Chua (from 'My Daughter, My Friend')", "Robert Langley"],
 ["Form", "A personal letter (19 June 1995) from a mother to her daughter Ming", "A poem of four four-line stanzas"],
 ["Main idea", "Pursue a dream with effort and sacrifice; count the cost; dreams may change", "Believe in yourself and leave comfort for growth"],
 ["Tone", "Encouraging and realistic", "Motivational"],
 ["Key words", "dream, conviction, sacrifice, support network", "challenge, status quo, first step, belief"]]),

("h2", "2. The Letter: Summary in Order"),
("ol", [
 "**Context.** The letter is an excerpt from 'My Daughter, My Friend' by Irene Chua, where she shares thoughts as a mother with her daughter Ming. The letters celebrate the bond between a mother and a teenage daughter and equip the daughter for life's challenges.",
 "**Encouragement.** 'By all means follow that dream.' Great men and women become great because they have a dream and pursue it till it comes true. What separates greatness from the ordinary is the effort and sacrifice invested. To reach world-class standard in any field one has to be intensively pursuing the subject for at least ten years.",
 "**Steps.** It starts with passion, then comes the conviction that realising it is imperative. Count the cost in years of effort, financial investments and sacrifice. If it is still burning in your blood and you are ready to commit, plunge. The field can be sports, science, arts, business or design.",
 "**The hard road.** The road may be uphill most of the way. You may be buoyed up only by the knowledge that you do what you love best and the right thing. When stamina runs out the prospect of success keeps you on track.",
 "**Support network.** Academy Award winners thank a host of people, so a winner has a group behind him or her.",
 "**Why dreams stay dreams.** Many people say 'I wish I could be this or that' but never get beyond wishful thinking. They may trade their dream for security or circumstances change their lives: examples are those whose dream of Raffles College (now the National University of Singapore) was ended by the Japanese invasion in World War II, and those who had to go out to work to support siblings' schooling.",
 "**Caution.** She will not put a wet blanket on Ming's dreams, but Ming must consider the years she needs. If after all obstacles the burning conviction still courses through her veins, she should go ahead.",
 "**Dreams change.** Life itself may change a person's dreams, and the new aspirations are no less valuable. Realisation may take longer and more people will join the 'dreamscape'. The mother's own example: publishing the book, a ten-year dream, was not her youthful dream. She wishes at least one of Ming's dreams comes true. Signed: Love, Mum."]),

("h2", "3. Values, Tone and Techniques of the Letter"),
("ul", [
 "**Values:** perseverance, sacrifice, realistic planning, gratitude for support, openness to change.",
 "**Tone:** warm, loving, encouraging, with caution; the mother is also a friend.",
 "**Techniques:** a direct question ('Do you know that...?'), personal anecdote (her book), real examples (Raffles College), idioms (burning in your blood, plunge, uphill, wet blanket, coursing through veins), imperatives ('Count the cost').",
 "**Structure of an informal letter:** date, salutation (Dear Ming), body with opening, advice, example and close, and a warm sign-off (Love, Mum)."]),
("note", "REMEMBER", "The mother neither says 'give up' nor 'ignore the costs'. She says 'follow that dream' but 'count the cost', and she accepts that dreams may change."),

("h2", "4. Letter Extracts Explained"),
("qa", [
 ("'What differentiates greatness from the ordinary is how much effort and sacrifice people invest to realise their dream.'", "Talent and dreams are common; the difference lies in the amount of effort and sacrifice. It teaches that achievement is the result of hard work."),
 ("'No, I am not going to put a wet blanket on your dreams ... but you will also have to consider the years you need to chase your dream.'", "She will not spoil Ming's enthusiasm, but she wants a realistic plan. It balances encouragement and caution."),
 ("'Life itself may change a person's dreams. These hopes and aspirations are no less than the original dream of younger days.'", "Dreams are not static. Changed goals are equally valuable, so one need not feel a failure if the dream changes.")]),

("h2", "5. Step up to the Challenge: Poem Notes"),
("table", ["Stanza", "Summary"], [
 ["1", "You face the challenge with no crowd watching; it is just you and the future and where you want to be"],
 ["2", "Will the future pull you forward or push you back in fear? Choices are difficult when the future is near"],
 ["3", "It is easy to stay in comfort and maintain the status quo, but we are not made for that and it is not how we grow"],
 ["4", "The first step is the hardest and there is no turning back; believe in yourself and your future will be on track"]]),
("table", ["Device", "Example", "Effect"], [
 ["Direct address", "You, your", "Speaker is a guide who speaks to the reader"],
 ["Rhyme scheme", "ABCB: see-be, fear-near, quo-grow, back-track", "Simple, steady flow"],
 ["Metaphor", "The first step is the hardest", "Beginning is the toughest part of change"],
 ["Antithesis", "pull you forward or push you back; ease in comfort versus growth", "Contrasts courage and fear"],
 ["Symbolism", "comfort and status quo: stagnation; the future: unknown and potential; the first step: courage to start", "Deeper meaning"],
 ["Imagery", "no crowd to see: solitary journey; push you back in fear: mental barrier", "Appeals to the reader's imagination"],
 ["Rhetorical question", "Will it pull you forward or push you back in fear?", "Makes the reader think"]]),
("ul", [
 "**Speaker:** a guide who understands the struggle.",
 "**Tone:** motivational and encouraging; thoughtful at the start, determined by the end.",
 "**Message:** growth needs leaving comfort and trusting oneself."]),

("h2", "6. Vocabulary"),
("table", ["Word or phrase", "Meaning"], [
 ["insight", "clear and deep understanding"],
 ["singularly", "exclusively"],
 ["imperative", "necessary"],
 ["plunge", "throw oneself into an activity"],
 ["buoyed up", "kept afloat; encouraged"],
 ["wistfully", "longingly"],
 ["dreamscape", "a world of dreams"],
 ["status quo", "the existing state of affairs"],
 ["wet blanket", "a person who spoils others' enthusiasm"],
 ["coursing through veins", "flowing through the body"],
 ["uphill task", "a tough challenge"],
 ["wishful thinking", "a hopeful belief that is unlikely to be true"]]),

("h2", "7. Grammar Points"),
("ul", [
 "**Compound word with '-scape':** dreamscape, landscape, seascape, cityscape, mindscape (a view or scene of).",
 "**First conditional:** if + present simple, will + verb; the main clause may take an imperative: *If the idea excites you, go ahead and try it.*",
 "**Uses of 'could':** past ability (I could run without stopping), possibility (It could be in any field), past possibility or speculation (They could have taken the shorter route), unreal wish (I wish I could be this), polite request (Could you repeat the question?).",
 "**Antithesis:** contrasting ideas in parallel structure, as in 'a small step for a man, a giant leap for mankind'.",
 "**Latin terms in English:** status quo, et cetera (etc.)."]),

("h2", "8. Writing Tips: Letters"),
("ul", [
 "Informal letter: sender's address and date, 'Dear...', a friendly body in short paragraphs, a warm closing (Love, Yours).",
 "A reply to a letter should respond to each of the sender's points before adding its own.",
 "In argumentative answers, state a view, give two reasons from the text and close with a conclusion.",
 "For poem answers, quote the line, name the device and state its effect."]),

("h2", "9. Connecting the Letter and the Poem"),
("ul", [
 "Both pieces begin with a person and a goal: Ming and her dream; the reader and the future.",
 "Both accept that the path is hard: an uphill road in the letter, 'the first step is the hardest' in the poem.",
 "The letter adds practical advice (count the cost, build a support network); the poem adds emotional advice (believe in yourself, leave the comfort zone).",
 "Use both in essays on perseverance, courage and ambition."]),

("h2", "10. Likely Questions with Model Answers"),
("qa", [
 ("What does the mother mean by 'Count the cost'? (2)", "Before committing to a dream, think of the years of effort, money and sacrifice it needs, and go ahead only if the conviction remains strong."),
 ("Why does the mother mention the Academy Awards? (2)", "To show that every winner has a support network of people who stood by him or her, so no achievement is the work of one person."),
 ("What is the message of the letter? (3)", "Follow your dream with passion and effort, count the costs, take support from others and accept that the dream may change over time."),
 ("Why is the first step the hardest? (2)", "It means leaving comfort, facing fear and uncertainty and starting something new, which needs self-belief."),
 ("What does the poet suggest for a successful future? (2)", "Believe in yourself and step out of the comfort zone to keep your future on track.")]),
],
takeaways=[
 "Follow That Dream is a letter dated 19 June 1995 from Irene Chua to her daughter Ming.",
 "Greatness comes from effort and sacrifice; world-class skill needs at least ten years of intensive pursuit.",
 "Count the cost in years, finance and sacrifice before plunging into a dream.",
 "Winners have a support network; many dreams remain wishful thinking because of circumstances.",
 "Life itself may change a person's dreams, and changed dreams are not lesser.",
 "Step up to the Challenge by Robert Langley has four ABCB stanzas.",
 "The poem uses direct address, metaphor, antithesis and symbolism: leave comfort, trust yourself, take the first step.",
 "Grammar: the first conditional with imperatives and the many uses of 'could'."])

if __name__ == "__main__": run(__file__, BANK, 9, "English", WS, CH, only=None)
