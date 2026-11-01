"""Reading skill sets — original passages. Each set: P1 (discursive, 10 marks) + P2 (case-based / data, 10 marks)."""
from eng_lib import P, S

def m(q, o, why=None):            # MCQ sub-question; first option is the correct one
    return S(q, "a", 1, o)

SETS = {}

# ───────────────────────── SET 1 ─────────────────────────
SETS[1] = dict(
P1=P("""<p>Every generation believes that it has invented tiredness, but the truth is that ours is the first to carry a library, a cinema and a post office in its pocket. The mobile phone has made information cheap and quick, and for that we should be grateful. Yet something precious has quietly slipped away: the ability to stay with one thing for a long time.</p>
<p>Reading a book once meant surrendering an afternoon to a single voice. The reader sat still, followed a long argument or a long story, and was changed a little by the end. Today we skim. We read the headline and the first line, we jump to the comments, and we move on before the idea has had time to settle. Researchers who study attention say that the mind behaves like a muscle: it grows strong when it is made to hold a weight for a while, and it grows weak when it is allowed to drop it every few seconds.</p>
<p>This does not mean that screens are enemies. A student who uses a dictionary application to find the meaning of a difficult word is saving time that can be used for thinking. A village girl who watches a video to learn how to repair a pump is gaining a skill that her school could not offer. The trouble begins when the tool starts to decide how we spend our hours. An application that is designed to keep us scrolling is not our servant; it is a very patient salesman.</p>
<p>The remedy is not dramatic. A person who sets aside thirty minutes each day to read something printed, with the phone in another room, will soon find that the restlessness lessens. Libraries still have quiet corners, and a good book has no notifications. The first ten days are the hardest, as with any exercise, but the reward is a mind that can follow a thought to its end.</p>""",
[m("According to the writer, our generation is special because it:", ["carries a library, cinema and post office in its pocket", "invented tiredness", "has stopped reading altogether", "dislikes information"]),
 m("'Surrendering an afternoon to a single voice' means:", ["giving one's full time to one writer's book", "losing an afternoon in sleep", "arguing with someone", "listening to many speakers"]),
 m("Researchers compare the mind to a muscle because it:", ["grows strong when it holds a weight for some time", "gets tired quickly", "is always active", "cannot be trained"]),
 m("Which example shows a good use of the phone?", ["A girl learning to repair a pump from a video", "Scrolling for hours at night", "Reading only headlines", "Playing games in class"]),
 m("The writer calls an application designed to keep us scrolling:", ["a very patient salesman", "a faithful servant", "a teacher", "a library"]),
 S("What has the mobile phone made cheap and quick?", "Information.", 1),
 S("How does the habit of reading today differ from that of the past?", "Earlier people read long books attentively; today people only skim headlines and first lines.", 1),
 S("What remedy does the writer suggest?", "To read something printed for thirty minutes daily with the phone kept in another room.", 1),
 S("Find a word from the passage which means 'a medicine or solution'.", "Remedy.", 1),
 S("Find a word from the passage which is the opposite of 'strong'.", "Weak.", 1)],
 title="Read the following passage carefully and answer the questions that follow."),
P2=P("""<p>The Reading Club of a school conducted a survey among 200 students of Classes 9 and 10 to find how many minutes a day they spent on different activities.</p><table><tr><th>Activity</th><th>Average minutes per day</th></tr><tr><td>Screen entertainment</td><td>110</td></tr><tr><td>Homework and tuition</td><td>75</td></tr><tr><td>Outdoor play</td><td>55</td></tr><tr><td>Reading books for pleasure</td><td>20</td></tr></table>""",
[m("Which activity took the most time per day?", ["Screen entertainment", "Homework", "Reading books", "Playing outdoors"]),
 m("How many minutes a day do students spend reading books for pleasure?", ["20", "60", "45", "95"]),
 m("Time spent outdoors is how much less than time spent on homework?", ["20 minutes", "35 minutes", "10 minutes", "55 minutes"]),
 S("What is the total time spent daily on homework and reading books?", "75 + 20 = 95 minutes.", 1),
 S("How many students were surveyed?", "200.", 1),
 S("How many minutes more is spent on screen entertainment than on outdoor play?", "110 − 55 = 55 minutes.", 1),
 S("What does the survey suggest about the students' reading habit?", "They read very little compared with other activities.", 1),
 S("Suggest one step the club can take to encourage reading.", "Hold a daily silent-reading period or a book-swap week.", 1),
 S("Find a word in the first sentence which means 'a study of opinions or habits'.", "Survey.", 1),
 S("Which group of students was surveyed — boys, girls or both?", "Not specified; students of Classes 9 and 10 generally.", 1)],
 title="Read the following case and the table, and answer the questions that follow."),
)
