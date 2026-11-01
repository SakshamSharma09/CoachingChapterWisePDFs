"""Class 9 reading skill sets 9-10 (original)."""
from eng9_lib import P, S

def m(q, o):
    return S(q, "a", 1, o)

SETS = {}

SETS[9] = dict(
P1=P("""<p>When we think of a hero, we usually imagine someone in uniform or on a stage. Yet some of the bravest people do their work quietly. A nurse who stays beside a patient through the night, a teacher who stays after school to help a slow learner, and a farmer who walks miles to bring water to his animals all show a kind of courage that rarely appears on television.</p>
<p>Such people share a few qualities. They do their duty even when no one is watching, they put others' needs before their own comfort, and they do not expect applause. Their lives remind us that greatness is not a matter of size but of steadiness.</p>
<p>We can learn from them in small ways. We can thank the sweeper who keeps our street clean, greet the watchman at the gate and help a classmate who is struggling. These acts cost nothing and take little time, but they tell people that their work is seen. A society that notices quiet heroes is a society that grows in kindness.</p>""",
[m("The writer says that some of the bravest people:", ["do their work quietly", "work only on stage", "wear uniforms", "avoid duty"]),
 m("Which of these is NOT given as an example of a quiet hero?", ["A film star", "A nurse", "A teacher", "A farmer"]),
 m("Quiet heroes share all of these EXCEPT:", ["they seek applause", "they do duty when unseen", "they put others first", "they are steady"]),
 m("'Greatness is a matter of steadiness' means:", ["consistent effort matters more than size", "heroes are strong", "nurses are great", "size is important"]),
 m("The writer suggests that we should:", ["thank those who serve us quietly", "ignore small acts", "avoid new people", "wait for TV coverage"]),
 S("Give one example of courage that rarely appears on television.", "A nurse staying beside a patient through the night.", 1),
 S("Why do quiet heroes not expect applause?", "They work from a sense of duty and care for others.", 1),
 S("Name two people whom the writer asks us to thank or greet.", "The sweeper and the watchman.", 1),
 S("Find a word in the passage meaning 'noticed' or 'observed'.", "Seen (noticed).", 1),
 S("What kind of society grows in kindness?", "One that notices quiet heroes.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p><b>Class 9 Science Club — Sign-up Form (extract)</b></p><p>Join the <b>Science Club</b> and take part in our <b>Weekly Experiment Hour</b> on <b>Wednesdays from 2:30 p.m. to 3:30 p.m.</b> in the Physics Laboratory. This term's projects include building a working model of a solar cooker, growing crystals and testing the pH of everyday liquids. Members must wear lab coats and follow safety rules. <b>Last date to join: 30 October.</b> Membership is free. A <b>Science Fair</b> will be held on <b>20 December</b>, where the best projects will be awarded. Contact: Mrs Joshi, Room 12.</p>""",
[m("The Science Club meets on:", ["Wednesdays", "Mondays", "Fridays", "Saturdays"]),
 m("The meeting is held in the:", ["Physics Laboratory", "Chemistry Laboratory", "Library", "Auditorium"]),
 m("Membership costs:", ["nothing", "₹100", "₹50", "₹10"]),
 m("The Science Fair will be on:", ["20 December", "30 October", "2 January", "15 November"]),
 m("Members must wear:", ["lab coats", "caps", "sports shoes only", "blazers"]),
 S("What is the last date to join?", "30 October.", 1),
 S("Name two projects for the term.", "Solar cooker, growing crystals, testing pH (any two).", 1),
 S("How long is the Weekly Experiment Hour?", "One hour.", 1),
 S("Whom should students contact?", "Mrs Joshi in Room 12.", 1),
 S("What will the Science Fair give to the best projects?", "Awards.", 1)],
 title="Read the following sign-up form and answer the questions that follow."),
)

SETS[10] = dict(
P1=P("""<p>Language is the thread that ties a community's memory together. Words carry the names of crops, the rhythm of festivals and the secrets of games played by children long ago. When a language disappears, an entire way of seeing the world goes with it.</p>
<p>India has twenty-two scheduled languages and hundreds of mother tongues. Some, like Hindi and Tamil, are spoken by millions. Others are spoken by only a few thousand people in remote valleys. Linguists warn that several of the smaller ones may vanish within a generation because young people shift to languages that offer jobs and wider reach.</p>
<p>Preserving a language does not mean rejecting others. A child can speak her mother tongue at home, learn the language of her state at school and use English in higher studies. Each one opens a different door. Schools can keep folk songs, proverbs and stories of the locality alive in assemblies and festivals. Families can tell bedtime stories in the old tongue. A language that is spoken and sung will not easily die.</p>""",
[m("The writer compares language to:", ["a thread that ties memory together", "a wall", "a river", "a key"]),
 m("How many scheduled languages does India have?", ["twenty-two", "ten", "forty", "fifty"]),
 m("Small languages may vanish because young people:", ["shift to languages that offer jobs and reach", "dislike old people", "travel", "write more"]),
 m("According to the passage, a child can:", ["use several languages for different purposes", "know only one", "forget her mother tongue", "avoid English"]),
 m("A language will not easily die if it is:", ["spoken and sung", "written once", "locked in books", "taught only in colleges"]),
 S("What do words carry in a language?", "Names of crops, festival rhythms and children's games.", 1),
 S("Give one way schools can help to preserve languages.", "Keep folk songs, proverbs and stories alive in assemblies and festivals.", 1),
 S("How can families help?", "By telling bedtime stories in the old tongue.", 1),
 S("Find a word that means 'to disappear'.", "Vanish.", 1),
 S("What does the writer mean by 'each one opens a different door'?", "Each language gives access to different people and opportunities.", 1)],
 title="Read the passage carefully and answer the questions that follow."),
P2=P("""<p>The following table gives the pass percentage of a school's Class 9 students in three subjects over three years.</p><table><tr><th>Year</th><th>Mathematics</th><th>Science</th><th>English</th></tr><tr><td>2024</td><td>78</td><td>82</td><td>90</td></tr><tr><td>2025</td><td>81</td><td>85</td><td>91</td></tr><tr><td>2026</td><td>86</td><td>88</td><td>93</td></tr></table>""",
[m("Which subject had the highest pass percentage in 2026?", ["English", "Mathematics", "Science", "All equal"]),
 m("Mathematics improved from 2024 to 2026 by:", ["8 percentage points", "5 percentage points", "3 percentage points", "10 percentage points"]),
 m("The pass percentage in Science in 2025 was:", ["85", "82", "88", "81"]),
 m("In which year was English at 91 per cent?", ["2025", "2024", "2026", "None"]),
 m("Which subject showed the steadiest rise?", ["English", "Mathematics", "Science", "None"]),
 S("What was the Mathematics pass percentage in 2024?", "78.", 1),
 S("What is the average of the three subjects in 2026?", "(86 + 88 + 93) ÷ 3 = 89.", 1),
 S("Which subject had the lowest result in 2024?", "Mathematics (78).", 1),
 S("Is the overall trend improving or declining?", "Improving.", 1),
 S("Suggest one reason for improvement.", "More practice, extra classes or better teaching.", 1)],
 title="Read the following table and answer the questions that follow."),
)
