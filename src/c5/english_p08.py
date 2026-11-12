import sys, re
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from lib5 import *

def wc(t): return len(re.sub(r"<[^>]+>", " ", t).split())
def mcq(q, opts, k): return Q(q, 1, f"({'abcd'[k]}) {opts[k]}", opts=opts)
def box(ws): return "<table class='t5'><tr>" + "".join(f"<td>{w}</td>" for w in ws) + "</tr></table>"
def match(a, b):
    r = "".join(f"<tr><td>{i+1}. {x}</td><td>{'abcde'[i]}. {y}</td></tr>" for i, (x, y) in enumerate(zip(a, b)))
    return "<table class='t5'><tr><th>Column A</th><th>Column B</th></tr>" + r + "</table>"
def rd(a, b, c, passage=None):
    if passage: assert 110 <= wc(passage) <= 175, wc(passage)
    return Q("Read the passage carefully and answer the questions." if passage else "Answer the following questions.", 5, "", passage=passage,
             parts=[P("(i)", a[0], 2, a[1]), P("(ii)", b[0], 2, b[1]), P("(iii)", c[0], 1, c[1])])

meta = dict(subject="English", set_no=8, time="2.30 Hours", marks=80, instr=[
    "This question paper is based on the learning areas of English: lexical, structural, reading and writing skills.",
    "Write your Name and Roll No. in the space given at the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly."])

P1 = ("<b>Kites over Jaipur</b><br>On 14 January, the people of Jaipur wake up early and rush to their rooftops. It is Makar Sankranti, and the sky soon fills with kites of every colour. "
      "Children hold the strings carefully, while elders cheer from behind. Shouts of 'Wo kata!' ring out whenever a kite is cut. Families eat til laddoos and gajak, and share them with neighbours. "
      "Though the day is cold, the warm sun and the cheerful mood make everybody feel happy. Before sunset, some people also feed cows and give clothes or food to poor people because they believe that giving brings good luck. "
      "At night, small paper lanterns rise into the sky and glow like stars. People say that on this day the sun begins its journey towards the north, and the days slowly become longer.")
P2 = ("<b>Gopal and the Puppy</b><br>On his way to school, Gopal heard a soft cry near the garbage bin. A tiny brown puppy was shivering in the cold. Its leg was hurt and it could not walk. "
      "Gopal looked around but saw nobody. He could not leave the puppy there, so he wrapped it in his woollen scarf and carried it to his house. His mother gave the puppy warm milk, and his father called the animal doctor. "
      "The doctor put a bandage on its leg and said that it would heal in a week. Gopal named the puppy Moti. Every day after school, he fed Moti and played with him in the yard. "
      "Soon the puppy grew strong and began to follow Gopal everywhere. Gopal understood that a little love can change a life.")

lex = [
    mcq("Our teacher gave ___ a new notebook.", ["we", "us", "our", "they"], 1),
    mcq("Choose the synonym of <b>begin</b>.", ["end", "stop", "start", "finish"], 2),
    mcq("Choose the antonym of <b>difficult</b>.", ["hard", "tough", "heavy", "easy"], 3),
    mcq("The lamp hangs ___ the ceiling.", ["from", "into", "with", "by"], 0),
    mcq("Choose the word in which the underlined letters sound different:", ["b<u>oo</u>k", "l<u>oo</u>k", "m<u>oo</u>n", "c<u>oo</u>k"], 2),
    mcq("Choose the adjective in the sentence: <i>The red kite flew high.</i>", ["flew", "high", "kite", "red"], 3),
    mcq("Which prefix can be added to <b>kind</b> to make its opposite?", ["unkind", "inkind", "dekind", "miskind"], 0),
]
struct = [
    Q("Rearrange the jumbled letters to make meaningful words.", 2, "", parts=[
        P("(i)", "E T K I", 1, "KITE"), P("(ii)", "L I P C E N", 1, "PENCIL")]),
    Q("Choose the appropriate word from the bracket to complete each sentence.", 2, "", parts=[
        P("(i)", "We use a ___ to draw a straight line. (ruler / spoon)", 1, "ruler"), P("(ii)", "Honey is made by ___ . (bees / ants)", 1, "bees")]),
    Q("Fill in the blanks with suitable words from the bracket. (children, flew, gently)", 3, "", parts=[
        P("(i)", "The ___ ran to the roof with their kites.", 1, "children"), P("(ii)", "The kite ___ high in the sky.", 1, "flew"),
        P("(iii)", "Hold the string ___ so that it does not break.", 1, "gently")]),
    Q("Choose the correct option from the bracket.", 5, "", parts=[
        P("(i)", "She ___ beautiful pictures. (draws / draw)", 1, "draws"),
        P("(ii)", "They ___ finished their homework. (have / has)", 1, "have"),
        P("(iii)", "The cat jumped ___ the table. (onto / into)", 1, "onto"),
        P("(iv)", "Water ___ flows uphill by itself. (always / never)", 1, "never"),
        P("(v)", "Yesterday, we ___ the zoo. (visit / visited)", 1, "visited")]),
    Q("Complete the passage using the words given in the box. Write the answers in the order of blanks.<br>" + box(["waited", "spread", "cooked", "enjoyed"]) +
      "Sunita's mother (1) ______ a big pot of kheer on Sunday. The sweet smell (2) ______ through the whole house. "
      "Her brothers sat at the table and (3) ______ for their bowls. Sunita served everyone and then (4) ______ her own kheer slowly.", 8,
      "(1) cooked &nbsp; (2) spread &nbsp; (3) waited &nbsp; (4) enjoyed &nbsp; <i>(2 marks each)</i>"),
    Q("Match Column A with Column B.<br>" + match(["Dentist", "Soap", "Milk", "Dustbin", "Handkerchief"],
        ["gives calcium to our bones", "keeps the surroundings tidy", "cleans hands and removes germs", "treats our teeth", "covers the nose while sneezing"]), 5,
      "1 – d &nbsp; 2 – c &nbsp; 3 – a &nbsp; 4 – b &nbsp; 5 – e"),
    Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, "", parts=[
        P("(i)", "___ Earth moves around the Sun.", 1, "The"), P("(ii)", "Our school is ___ old building.", 1, "an")]),
]
read = [
    Q("Read the passage carefully and answer Questions 15, 16 and 17.", 5, "", passage=P1, parts=[
        P("(i)", "On which date is Makar Sankranti celebrated, according to the passage?", 2, "On 14 January."),
        P("(ii)", "Which sweets do the families eat?", 2, "Til laddoos and gajak."),
        P("(iii)", "Find a word from the passage which means <i>to shine with a soft light</i>.", 1, "glow")]),
    rd(("What do people shout when a kite is cut?", "They shout 'Wo kata!'."),
       ("Why do some people give clothes or food to poor people?", "They believe that giving brings good luck."),
       ("Write the opposite of <b>early</b>.", "late")),
    rd(("What happens at night in the sky?", "Small paper lanterns rise into the sky and glow like stars."),
       ("What do people say about the sun on this day?", "They say that the sun begins its journey towards the north and the days slowly become longer."),
       ("Write the singular of <b>children</b>.", "child")),
    Q("Read the passage carefully and answer Questions 18, 19 and 20.", 5, "", passage=P2, parts=[
        P("(i)", "What did Gopal hear near the garbage bin?", 2, "He heard the soft cry of a puppy."),
        P("(ii)", "How did Gopal keep the puppy warm?", 2, "He wrapped it in his woollen scarf."),
        P("(iii)", "Find a word from the passage which means <i>to become well again</i>.", 1, "heal")]),
    rd(("Who called the animal doctor?", "Gopal's father called the animal doctor."),
       ("What did the doctor do and say?", "He put a bandage on the puppy's leg and said that it would heal in a week."),
       ("Write the opposite of <b>tiny</b>.", "big / huge / large")),
    rd(("What did Gopal do every day after school?", "He fed Moti and played with him in the yard."),
       ("What did Gopal understand at the end?", "He understood that a little love can change a life."),
       ("Write the female word for <b>father</b>.", "mother")),
]
write = [
    Q("Write a letter to your friend describing how you celebrated the festival of Diwali. (Your address: <i>3, Station Road, Kota</i>; friend's name: Karan.)", 8,
      "<b>Marking:</b> format 2 + content (decoration, lamps, sweets, crackers/safety, family, wish to meet) 4 + language 2.<br>"
      "<i>Model:</i> 3, Station Road, Kota; 15 November 2027. Dear Karan, I hope you are well. This Diwali was great fun. We cleaned the house and lit diyas in the evening. "
      "Mother made delicious sweets and we worshipped Goddess Lakshmi. I burst only a few crackers and kept a bucket of water nearby. How did you celebrate? Write soon. Yours lovingly, (name).",
      alt=Q("Write an application to the Principal for one day's leave to attend your cousin's wedding.", 8,
            "<b>Marking:</b> format 2 + content (reason, date, request) 4 + language 2.<br>"
            "<i>Model:</i> To, The Principal, ... School, Kota. Date. Subject: Leave for one day. Respected Sir/Madam, My cousin's wedding is on Friday, 12 May. All my family is going to Ajmer to attend it. "
            "Kindly grant me leave for that day. Yours obediently, (name), Class V.")),
    Q("Look at the picture and write <b>four</b> sentences about it.<br><div style='font-size:24px;line-height:1.3'>🚉 🚆 🕐<br>🧳 👨‍👩‍👧 🎫 🧳<br>🍌 🧑‍✈️ 🪧</div>", 8,
      "<b>Marking:</b> 4 correct sentences x 2 (meaning 1 + grammar/spelling 1).<br><i>Model:</i> A train is standing at the railway station. A family is waiting on the platform with their bags. The girl is holding a ticket. A clock shows the time of the train.",
      alt=Q("Complete the story using the hints: <i>Lalit – fond of drawing – no colours – neighbour gave a box – painted a tree – won the first prize.</i>", 8,
            "<b>Marking:</b> story follows all hints 4 + sequence/linking 2 + language 2.<br><i>Model:</i> Lalit was very fond of drawing, but he had no colours. His neighbour gave him a box of colours. "
            "He painted a big green tree with birds on it. His teacher liked the picture and sent it to a competition. Lalit won the first prize.")),
]
secs = [sec("LEXICAL ITEMS", 7, lex), sec("STRUCTURAL ITEMS", 27, struct), sec("READING COMPREHENSION", 30, read), sec("WRITING SKILLS", 16, write)]
if __name__ == "__main__":
    print(build(meta, secs))
