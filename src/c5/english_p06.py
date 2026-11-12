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

meta = dict(subject="English", set_no=6, time="2.30 Hours", marks=80, instr=[
    "This question paper is based on the learning areas of English: lexical, structural, reading and writing skills.",
    "Write your Name and Roll No. in the space given at the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly."])

P1 = ("<b>The Camel Fair</b><br>Every year, in the month of November, a small town in Rajasthan fills with colour and noise. This is the Pushkar Fair. "
      "Thousands of camels are brought here by herders from distant villages. The camels are washed, and their coats are trimmed in pretty patterns. "
      "Some wear bright blankets and silver anklets. Children ride on carts, and women sell bangles and bags in the sandy lanes. "
      "In the evening, folk singers sit around fires and sing old songs. Many tourists come from other countries to watch the camel races and the turban-tying contest. "
      "Farmers also come to buy and sell animals. Although the fair lasts only a few days, people wait for it all year, because it brings together friends, families and traders from all over the land.")
P2 = ("<b>Meena and the Green Purse</b><br>One rainy afternoon, Meena was walking home from school when she saw a small green purse lying in a puddle. She picked it up and opened it. "
      "Inside were three hundred rupees and a photo of an old man. Meena did not keep the money. She knew that somebody must be worried about it. "
      "Next morning, she showed the purse to her teacher, Mrs Verma. The teacher announced it in the assembly. Soon, an old watchman named Ramu Kaka came running to the stage. "
      "He had lost the purse while hurrying to the market. His eyes filled with tears of joy as he took it back. He thanked Meena again and again and blessed her. "
      "The whole school clapped for her. Meena smiled shyly. She learnt that being honest makes one feel proud and light-hearted.")

lex = [
    mcq("Neha and I ___ going to the fair tomorrow.", ["is", "am", "are", "was"], 2),
    mcq("Choose the synonym of <b>enormous</b>.", ["tiny", "huge", "quiet", "ancient"], 1),
    mcq("Choose the antonym of <b>ancient</b>.", ["old", "dusty", "tall", "modern"], 3),
    mcq("The train passed ___ a long tunnel.", ["on", "at", "of", "through"], 3),
    mcq("Choose the word in which the underlined letters sound different:", ["br<u>ea</u>d", "h<u>ea</u>d", "m<u>ea</u>t", "d<u>ea</u>d"], 2),
    mcq("Choose the correct plural of <b>knife</b>.", ["knifes", "knives", "knifs", "knivez"], 1),
    mcq("Choose the word that sounds like <b>week</b> but has a different meaning.", ["wick", "wake", "work", "weak"], 3),
]
struct = [
    Q("Rearrange the jumbled letters to make meaningful words.", 2, "", parts=[
        P("(i)", "A L C M E", 1, "CAMEL"), P("(ii)", "L O C H O S", 1, "SCHOOL")]),
    Q("Choose the appropriate word from the bracket to complete each sentence.", 2, "", parts=[
        P("(i)", "The sun rises in the ___ . (east / west)", 1, "east"), P("(ii)", "A ___ grows crops in the field. (tailor / farmer)", 1, "farmer")]),
    Q("Fill in the blanks with suitable words from the bracket. (painted, potter, carefully)", 3, "", parts=[
        P("(i)", "The ___ made a clay pot.", 1, "potter"), P("(ii)", "Ravi ___ the wall green.", 1, "painted"),
        P("(iii)", "Write ___ so that everybody can read your work.", 1, "carefully")]),
    Q("Choose the correct option from the bracket.", 5, "", parts=[
        P("(i)", "My grandfather ___ in the park every morning. (walk / walks / walking)", 1, "walks"),
        P("(ii)", "We ___ playing chess when the lights went out. (are / were)", 1, "were"),
        P("(iii)", "Hari goes to school ___ bus. (by / with)", 1, "by"),
        P("(iv)", "The sun ___ rises in the west. (always / never)", 1, "never"),
        P("(v)", "Each of the students ___ a library card. (has / have)", 1, "has")]),
    Q("Complete the passage using the words given in the box. Write the answers in the order of blanks.<br>" + box(["crowded", "greeted", "market", "walked"]) +
      "Last Sunday, Mohan went to the (1) ______ with his father. They bought a basket of mangoes and (2) ______ to the bus stop. "
      "The bus was (3) ______, so they had to stand. When they reached home, mother (4) ______ them with a smile.", 8,
      "(1) market &nbsp; (2) walked &nbsp; (3) crowded &nbsp; (4) greeted &nbsp; <i>(2 marks each)</i>"),
    Q("Match Column A with Column B.<br>" + match(["Brush your teeth", "Wash your hands", "Red traffic light", "Zebra crossing", "Dustbin"],
        ["means stop", "to throw waste", "twice a day", "to cross the road safely", "before meals"]), 5,
      "1 – c &nbsp; 2 – e &nbsp; 3 – a &nbsp; 4 – d &nbsp; 5 – b"),
    Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, "", parts=[
        P("(i)", "She ate ___ orange after lunch.", 1, "an"), P("(ii)", "___ Sun gives us light and heat.", 1, "The")]),
]
read = [
    Q("Read the passage carefully and answer Questions 15, 16 and 17.", 5, "", passage=P1, parts=[
        P("(i)", "In which month is the Pushkar Fair held?", 2, "In November."),
        P("(ii)", "Name any two things that some camels wear at the fair.", 2, "Bright blankets and silver anklets."),
        P("(iii)", "Find a word from the passage which means <i>far away</i>.", 1, "distant")]),
    rd(("Who bring the camels to the fair?", "Herders from distant villages bring the camels."),
       ("What do the folk singers do in the evening?", "They sit around fires and sing old songs."),
       ("Write the opposite of <b>small</b> (as used in the passage).", "big / large")),
    rd(("Name any two events that tourists come to watch.", "The camel races and the turban-tying contest."),
       ("Why do people wait for the fair all year?", "Because it brings together friends, families and traders from all over the land."),
       ("Write the singular of <b>women</b>.", "woman")),
    Q("Read the passage carefully and answer Questions 18, 19 and 20.", 5, "", passage=P2, parts=[
        P("(i)", "Where did Meena find the purse?", 2, "In a puddle, on her way home from school."),
        P("(ii)", "What was there inside the purse?", 2, "Three hundred rupees and a photo of an old man."),
        P("(iii)", "Write the word from the passage that means <i>a small pool of rainwater</i>.", 1, "puddle")]),
    rd(("Whom did Meena show the purse to?", "She showed it to her teacher, Mrs Verma."),
       ("How did the school come to know about the purse?", "The teacher announced it in the assembly."),
       ("Which word in the passage means <i>a person who guards a building</i>?", "watchman")),
    rd(("Why did Ramu Kaka lose his purse?", "He was hurrying to the market."),
       ("How did Ramu Kaka show his thanks to Meena?", "He thanked her again and again and blessed her."),
       ("Write the word from the passage that is the opposite of <b>sorrow</b>.", "joy")),
]
write = [
    Q("Write a letter to your friend inviting him/her to your birthday party. (Write your address as <i>12, Ashok Marg, Jaipur</i> and the friend's name as Rohan.)", 8,
      "<b>Marking:</b> format (address, date, salutation, closing) 2 + content (date/time/place of party, request to come, wish to meet) 4 + language 2.<br>"
      "<i>Model:</i> 12, Ashok Marg, Jaipur; 10 March 2027. Dear Rohan, I hope you are fine. My birthday is on 15 March at 4 p.m. at my house. "
      "We shall cut a cake, play games and eat tasty snacks. Please come with your parents. I shall be very happy to see you. Yours lovingly, (name).",
      alt=Q("Write an application to your class teacher asking for two days' leave because you have fever.", 8,
            "<b>Marking:</b> format (To, Date, Subject, Salutation, Yours obediently) 2 + content (reason, number of days, request) 4 + language 2.<br>"
            "<i>Model:</i> To, The Class Teacher, Class V, ... School, Jaipur. Date. Subject: Leave for two days. Respected Madam, I beg to say that I have fever since last night "
            "and the doctor has advised me to take rest. So I cannot attend school on 10 and 11 March. Kindly grant me leave for these two days. Yours obediently, (name), Class V.", )),
    Q("Look at the picture and write <b>four</b> sentences about it.<br><div style='font-size:24px;line-height:1.3'>☀️ 🌳 🪁 🌳<br>🧒 ⚽ 🐕 👧 🚲<br>🌷 🌷 🦋 🌷</div>", 8,
      "<b>Marking:</b> 4 correct sentences x 2 (meaning 1 + grammar/spelling 1).<br><i>Model:</i> The sun is shining in the sky. A boy is playing with a football. A dog is running near him. A girl is riding a bicycle in the park.",
      alt=Q("Complete the story using the hints: <i>A thirsty crow – found a jug – little water – pebbles – water rose – drank and flew away.</i>", 8,
            "<b>Marking:</b> story follows all hints 4 + sequence/linking 2 + language 2.<br><i>Model:</i> A thirsty crow flew here and there in search of water. At last it found a jug with a little water at the bottom. "
            "Its beak could not reach it. The crow put many pebbles into the jug one by one. The water rose to the top. The crow drank the water and flew away happily.")),
]
secs = [sec("LEXICAL ITEMS", 7, lex), sec("STRUCTURAL ITEMS", 27, struct), sec("READING COMPREHENSION", 30, read), sec("WRITING SKILLS", 16, write)]
if __name__ == "__main__":
    print(build(meta, secs))
