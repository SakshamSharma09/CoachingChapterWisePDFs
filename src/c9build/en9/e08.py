from eng9_lib import mcq, Q, X

NAME = "Follow That Dream; Step Up to the Challenge"
MCQ = [
 mcq("'Follow That Dream' is a letter written by:", ["a mother to her daughter Ming", "a teacher to a student", "a father to his son", "a friend to a friend"], "a", "Dated 19 June 1995"),
 mcq("The letter opens with the words:", ["By all means follow that dream", "Do not follow dreams", "Dreams are useless", "Be practical"], "a", "Encouragement"),
 mcq("According to the writer, greatness differs from the ordinary in the:", ["effort and sacrifice invested", "luck of birth", "wealth of family", "amount of talent only"], "a", "Core idea"),
 mcq("To reach a world-class standard one must pursue a subject for at least:", ["ten years", "one year", "two months", "five days"], "a", "Intense effort"),
 mcq("The first step towards a dream starts with:", ["passion for an interest", "money", "approval of friends", "luck"], "a", "Then conviction follows"),
 mcq("The writer asks Ming to 'count the cost' in:", ["years of effort, money and sacrifice", "only money", "only time", "only friends"], "a", "Realism"),
 mcq("'Plunge' in the letter means:", ["to commit oneself fully", "to fall", "to swim", "to refuse"], "a", "Complete involvement"),
 mcq("What keeps a person going when stamina runs out?", ["the prospect of success", "rest", "sleep", "advice"], "a", "Motivation"),
 mcq("The Academy Awards example shows that success needs:", ["a support network", "luck alone", "no help", "a big family"], "a", "Winners thank many people"),
 mcq("Many people's dreams remain unfulfilled because they:", ["never get beyond wishful thinking", "do not get sleep", "have no money", "are lazy"], "a", "Dreams vs action"),
 mcq("The mother mentions people whose dream was disturbed by:", ["the Japanese invasion in the Second World War", "a flood", "an earthquake", "an exam"], "a", "Raffles College"),
 mcq("The writer says that life itself may:", ["change a person's dreams", "end all dreams", "destroy hope", "stop effort"], "a", "Dreams evolve"),
 mcq("The dream the mother chased for ten years was:", ["publishing a book", "winning a medal", "becoming a pilot", "owning a shop"], "a", "Her own example"),
 mcq("The tone of the letter is:", ["encouraging and caring", "angry", "sarcastic", "indifferent"], "a", "Mother's voice"),
 mcq("The poem 'Step Up to the Challenge' conveys that:", ["growth needs leaving comfort and believing in oneself", "comfort is best", "never try", "wait for luck"], "a", "Robert Langley"),
 mcq("According to the poem, the hardest step is:", ["the first step", "the last step", "the middle step", "none"], "a", "Self-belief helps"),
]
EXT = [
 X("The mother tells Ming that greatness comes to those who chase their dream with effort and sacrifice. She says one must work intensively at a subject for ten years or more to be of world-class standard. She asks her daughter to count the cost before plunging in.",
   [("Who is writing to whom?", "A mother is writing to her daughter Ming."),
    ("How long does she say it takes to reach the world-class standard?", "At least ten years."),
    ("What must Ming count before she plunges in?", "The cost in years, money and sacrifice."),
    ("What attitude to dreams does the mother show?", "Encouraging yet realistic.")]),
 X("Awards winners thank a host of people because for one winner there is a group who stood beside him or her. Many people never move beyond wishing. Some choose security over dreams, and some find that circumstances change their lives. The mother does not wish to spoil Ming's hopes, yet she asks her to think of the road ahead.",
   [("Why do winners thank many people?", "A group supported each of them."),
    ("What happens to many dreams?", "They remain wishful thinking."),
    ("Why do some abandon dreams?", "They prefer security or circumstances change."),
    ("Which phrase shows the mother's tact?", "She is not going to put a wet blanket on dreams.")]),
 X("The poet says that no crowd watches the person who must face a challenge. Comfort is easy and keeps things as they are, but growth is not found there. The first step is the hardest and cannot be undone, yet belief in oneself keeps the future on track.",
   [("What is easy according to the poet?", "Staying in comfort."),
    ("Which step is the hardest?", "The first step."),
    ("What helps keep the future on track?", "Believing in oneself."),
    ("What is the tone of the poem?", "Motivating and encouraging.")]),
]
SA = [
 Q("What does the mother mean by 'count the cost'?", "Think of the years of effort, investment and sacrifice needed before committing to a dream.", "2"),
 Q("Why does the mother mention the Academy Awards?", "To show that every winner has a support network that helped the person succeed.", "2"),
 Q("What distinguishes a dreamer from an achiever?", "The achiever works hard, sacrifices and acts, while a dreamer only wishes.", "2"),
 Q("How can dreams change with time?", "Circumstances and life experiences change aims; the new dream is as valuable as the old one.", "2"),
 Q("What example does the mother give from her own life?", "She chased the dream of publishing a book for ten years, which was not her youthful dream.", "2"),
 Q("What does 'status quo' mean in the poem?", "The existing comfortable state of things that people hesitate to change.", "2"),
]
LA = [
 Q("What advice does Ming's mother give her? Mention three points.", "Follow your dream; work hard for years; count the cost; build a support network; be ready for change.", "3"),
 Q("How does the mother balance encouragement with caution?", "She urges Ming to follow her dream but asks her to think of cost, hurdles and changing circumstances.", "3"),
 Q("How does the mother use personal experience to persuade?", "She mentions people whose lives were changed by war and her own late-won dream of publishing a book.", "3"),
 Q("Why does she say dreams will need more people in future?", "A larger dream needs more participants such as mentors, family and colleagues.", "3"),
 Q("What qualities are needed to turn a dream into reality?", "Passion, conviction, hard work, sacrifice, patience, support and flexibility.", "3"),
 Q("Explain the line 'dreams remain dreams' with reference to the letter.", "Some people only wish and never act; others give up for security or because of circumstances.", "3"),
 Q("What challenges does the poem 'Step Up to the Challenge' describe?", "Facing the future alone, fear of change, comfort holding one back and the difficulty of the first step.", "3"),
 Q("What is the message of the poem?", "Leave comfort, believe in yourself and take the first step towards your goals.", "3"),
]
