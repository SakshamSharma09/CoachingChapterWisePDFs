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

meta = dict(subject="English", set_no=9, time="2.30 Hours", marks=80, instr=[
    "This question paper is based on the learning areas of English: lexical, structural, reading and writing skills.",
    "Write your Name and Roll No. in the space given at the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly."])

P1 = ("<b>The Wizard of Hockey</b><br>Major Dhyan Chand is remembered as the greatest hockey player India has ever produced. He was born in Prayagraj in 1905. "
      "As a boy, he loved wrestling, but later he joined the army and began playing hockey seriously. He used to practise in the moonlight after his duty, and so his friends gave him the name 'Chand'. "
      "His control over the ball was so wonderful that people thought it stuck to his stick. India won three Olympic gold medals in hockey, in 1928, 1932 and 1936, when he was in the team. "
      "The whole world praised him as the 'Wizard of Hockey'. His birthday, 29 August, is celebrated every year as National Sports Day to remind us that games build health, discipline and team spirit.")
P2 = ("<b>Tara's Library Card</b><br>Tara was ten years old and loved stories, but her family could not afford to buy many books. One day, her teacher told the class that the town library gave free membership cards to children. "
      "Tara hurried there after school and filled in a small form. The librarian, Mr Joshi, gave her a blue card and showed her the children's section. Tara chose a book about a clever fox and read it in two days. "
      "She took good care of it and returned it on time. Soon she was reading one book every week. She even began telling the stories to her little brother at bedtime. "
      "Months later, Tara wrote a short story of her own, and it was printed in the school magazine. She was proud that her library card had opened a door to a whole new world.")

lex = [
    mcq("Rohan ___ his bicycle to school every day.", ["ride", "rides", "riding", "rode"], 1),
    mcq("Choose the synonym of <b>quick</b>.", ["slow", "late", "fast", "heavy"], 2),
    mcq("Choose the antonym of <b>enter</b>.", ["exit", "arrive", "begin", "join"], 0),
    mcq("The match will start ___ 9 o'clock.", ["on", "in", "by", "at"], 3),
    mcq("Choose the word in which the underlined letters sound different:", ["<u>ch</u>ild", "<u>ch</u>ef", "<u>ch</u>ain", "<u>ch</u>air"], 1),
    mcq("Choose the correct plural of <b>leaf</b>.", ["leafs", "leavs", "leaves", "leafes"], 2),
    mcq("Choose the word that sounds like <b>sea</b> but has a different meaning.", ["see", "say", "sew", "sit"], 0),
]
struct = [
    Q("Rearrange the jumbled letters to make meaningful words.", 2, "", parts=[
        P("(i)", "Y R A R B I L", 1, "LIBRARY"), P("(ii)", "Y T S O R", 1, "STORY")]),
    Q("Choose the appropriate word from the bracket to complete each sentence.", 2, "", parts=[
        P("(i)", "A bee collects ___ from flowers. (nectar / sand)", 1, "nectar"), P("(ii)", "Birds build their ___ on trees. (nests / roads)", 1, "nests")]),
    Q("Fill in the blanks with suitable words from the bracket. (neatly, shelf, borrowed)", 3, "", parts=[
        P("(i)", "Mina ___ a storybook from the library.", 1, "borrowed"), P("(ii)", "Put the book back on the ___ .", 1, "shelf"),
        P("(iii)", "She wrote her name ___ on the first page.", 1, "neatly")]),
    Q("Choose the correct option from the bracket.", 5, "", parts=[
        P("(i)", "Rani ___ a newspaper every morning. (reads / read)", 1, "reads"),
        P("(ii)", "There ___ many books on the table. (is / are)", 1, "are"),
        P("(iii)", "She ___ a lovely voice. (has / have)", 1, "has"),
        P("(iv)", "The bus will arrive ___ ten minutes. (in / on)", 1, "in"),
        P("(v)", "The Earth ___ stops moving around the Sun. (always / never)", 1, "never")]),
    Q("Complete the passage using the words given in the box. Write the answers in the order of blanks.<br>" + box(["tired", "showed", "took", "trip"]) +
      "Our class went to the Amer Fort on a school (1) ______ . A guide (2) ______ us the old palace. "
      "We (3) ______ many photographs near the big gate. In the evening, everyone felt (4) ______ and slept on the bus.", 8,
      "(1) trip &nbsp; (2) showed &nbsp; (3) took &nbsp; (4) tired &nbsp; <i>(2 marks each)</i>"),
    Q("Match Column A with Column B.<br>" + match(["Library", "Hospital", "Post office", "Fire station", "Police station"],
        ["letters are sent from here", "books are lent here", "complaints are recorded here", "fire engines are kept here", "patients are treated here"]), 5,
      "1 – b &nbsp; 2 – e &nbsp; 3 – a &nbsp; 4 – d &nbsp; 5 – c"),
    Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, "", parts=[
        P("(i)", "Please give me ___ apple.", 1, "an"), P("(ii)", "___ Himalayas are in the north of India.", 1, "The")]),
]
read = [
    Q("Read the passage carefully and answer Questions 15, 16 and 17.", 5, "", passage=P1, parts=[
        P("(i)", "Where was Dhyan Chand born?", 2, "He was born in Prayagraj (in 1905)."),
        P("(ii)", "Why did his friends call him 'Chand'?", 2, "Because he used to practise hockey in the moonlight after his duty."),
        P("(iii)", "Find a word from the passage which means <i>a magician</i>.", 1, "wizard")]),
    rd(("How many Olympic gold medals did India win in hockey when he was in the team?", "India won three gold medals (in 1928, 1932 and 1936)."),
       ("What did people think about the ball and his stick?", "They thought the ball stuck to his stick."),
       ("Write the opposite of <b>loved</b>.", "hated / disliked")),
    rd(("Which day is celebrated as National Sports Day?", "29 August, the birthday of Dhyan Chand."),
       ("What does this day remind us of?", "That games build health, discipline and team spirit."),
       ("Write the plural of <b>medal</b>.", "medals")),
    Q("Read the passage carefully and answer Questions 18, 19 and 20.", 5, "", passage=P2, parts=[
        P("(i)", "Why could Tara not read many books at home?", 2, "Her family could not afford to buy many books."),
        P("(ii)", "What did the teacher tell the class?", 2, "She told them that the town library gave free membership cards to children."),
        P("(iii)", "Which word in the passage means <i>a person who looks after a library</i>?", 1, "librarian")]),
    rd(("Who gave Tara the library card?", "The librarian, Mr Joshi, gave her the card."),
       ("What was the first book that Tara chose?", "A book about a clever fox."),
       ("Write the opposite of <b>good</b>.", "bad")),
    rd(("What did Tara do with the stories at bedtime?", "She told them to her little brother."),
       ("What happened months later?", "Tara wrote a short story of her own and it was printed in the school magazine."),
       ("Write the plural of <b>story</b>.", "stories")),
]
write = [
    Q("Write a letter to your grandmother asking about her health and telling her about your school. (Your address: <i>21, Lal Kothi, Jaipur</i>.)", 8,
      "<b>Marking:</b> format 2 + content (asking about health, news of school/studies, invitation or wish to meet, regards) 4 + language 2.<br>"
      "<i>Model:</i> 21, Lal Kothi, Jaipur; 5 July 2027. Dear Grandma, I hope you are in good health. How is your knee pain now? I am doing well at school. I am in Class V and I am the library monitor. "
      "Our annual exams will begin next month. Please come to Jaipur in the holidays. Pranam to Grandpa. Your loving grandchild, (name).",
      alt=Q("Write an application to the Principal asking for permission to leave school early because of a dental check-up.", 8,
            "<b>Marking:</b> format 2 + content (reason, time/date, request) 4 + language 2.<br>"
            "<i>Model:</i> To, The Principal, ... School, Jaipur. Date. Subject: Permission to leave early. Respected Sir/Madam, I have a dental check-up at 11 a.m. on Monday. "
            "Kindly allow me to leave school at 10 a.m. that day. Yours obediently, (name), Class V.")),
    Q("Look at the picture and write <b>four</b> sentences about it.<br><div style='font-size:24px;line-height:1.3'>📚 🪑 🖼️ 🕐<br>🧑‍🏫 📖 🧒 ✏️ 👧<br>🪴 🎒 🗑️</div>", 8,
      "<b>Marking:</b> 4 correct sentences x 2 (meaning 1 + grammar/spelling 1).<br><i>Model:</i> A teacher is standing in the classroom. Two children are reading books. A clock is hanging on the wall. There is a plant near the dustbin.",
      alt=Q("Complete the story using the hints: <i>Farmer – three sons – always quarrelled – father gave a bundle of sticks – none could break it – learnt to stay united.</i>", 8,
            "<b>Marking:</b> story follows all hints 4 + sequence/linking 2 + language 2.<br><i>Model:</i> A farmer had three sons who always quarrelled. One day he gave them a bundle of sticks and asked them to break it. "
            "None of them could break the bundle. Then he untied it and gave a single stick to each. They broke the sticks easily. The sons learnt that they should stay united.")),
]
secs = [sec("LEXICAL ITEMS", 7, lex), sec("STRUCTURAL ITEMS", 27, struct), sec("READING COMPREHENSION", 30, read), sec("WRITING SKILLS", 16, write)]
if __name__ == "__main__":
    print(build(meta, secs))
