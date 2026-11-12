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

meta = dict(subject="English", set_no=10, time="2.30 Hours", marks=80, instr=[
    "This question paper is based on the learning areas of English: lexical, structural, reading and writing skills.",
    "Write your Name and Roll No. in the space given at the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly."])

P1 = ("<b>Tigers of Ranthambore</b><br>Ranthambore National Park lies in the Sawai Madhopur district of Rajasthan. It is famous for its tigers, which can often be seen even in the daytime. "
      "The park is spread over dense forests, rocky hills and quiet lakes. An old fort stands on a high hill inside the park, and the tigers sometimes rest near its broken walls. "
      "Besides tigers, visitors can spot leopards, deer, crocodiles and many colourful birds. The tiger is our national animal, but its number had fallen because people hunted it and cut down forests. "
      "To save it, the government began Project Tiger in 1973. Today, special guards protect the animals day and night. Whenever we visit a forest, we should not litter or make loud noise. "
      "We must remember that the forest is the home of wild animals, not a place to spoil.")
P2 = ("<b>Hari's Garden</b><br>Hari lived in a small house with a bare yard. One spring, his grandfather gave him a packet of marigold seeds. Hari dug the soil, sowed the seeds and watered them every evening. "
      "After a week, nothing came up, and Hari felt sad. 'Seeds need time, my boy,' said his grandfather. Hari kept waiting and kept watering. Ten days later, tiny green leaves peeped out of the soil. "
      "In a month, the yard was full of golden flowers, and bees and butterflies came to visit. Hari picked a few flowers and put them in a vase in the classroom. "
      "His friends admired them and asked him to teach them gardening. From that day, Hari understood that patience and hard work always bring beautiful results.")

lex = [
    mcq("Ritu and Meera ___ best friends.", ["is", "am", "was", "are"], 3),
    mcq("Choose the synonym of <b>glad</b>.", ["sad", "happy", "tired", "angry"], 1),
    mcq("Choose the antonym of <b>victory</b>.", ["defeat", "success", "prize", "race"], 0),
    mcq("She divided the sweets ___ the four children.", ["among", "on", "by", "above"], 0),
    mcq("Choose the word in which the underlined letters sound different:", ["<u>th</u>ink", "<u>th</u>at", "<u>th</u>in", "<u>th</u>ank"], 1),
    mcq("Mount Everest is the ___ mountain in the world.", ["high", "higher", "highest", "highly"], 2),
    mcq("Choose the word that sounds like <b>hear</b> but has a different meaning.", ["here", "hair", "her", "hare"], 0),
]
struct = [
    Q("Rearrange the jumbled letters to make meaningful words.", 2, "", parts=[
        P("(i)", "G I T E R", 1, "TIGER"), P("(ii)", "G L U N E J", 1, "JUNGLE")]),
    Q("Choose the appropriate word from the bracket to complete each sentence.", 2, "", parts=[
        P("(i)", "A tiger is a ___ . (herbivore / carnivore)", 1, "carnivore"), P("(ii)", "A deer eats ___ . (grass / meat)", 1, "grass")]),
    Q("Fill in the blanks with suitable words from the bracket. (roared, guide, silently)", 3, "", parts=[
        P("(i)", "The tiger ___ loudly in the forest.", 1, "roared"), P("(ii)", "The ___ showed us the way through the jungle.", 1, "guide"),
        P("(iii)", "The deer moved ___ through the bushes.", 1, "silently")]),
    Q("Choose the correct option from the bracket.", 5, "", parts=[
        P("(i)", "A tiger ___ mostly at night. (hunts / hunt)", 1, "hunts"),
        P("(ii)", "We ___ a peacock yesterday. (saw / see)", 1, "saw"),
        P("(iii)", "The deer ran ___ the forest. (into / on)", 1, "into"),
        P("(iv)", "My sister ___ playing in the garden. (is / are)", 1, "is"),
        P("(v)", "Baby tigers ___ with their mother for two years. (stay / stays)", 1, "stay")]),
    Q("Complete the passage using the words given in the box. Write the answers in the order of blanks.<br>" + box(["photographs", "entered", "remain", "deer"]) +
      "Last winter, my family visited a national park. We (1) ______ the park early in the morning in an open jeep. The guide asked us to (2) ______ quiet so that the animals would not get scared. "
      "Soon we saw a spotted (3) ______ near a pond. We took a few (4) ______ and returned happily.", 8,
      "(1) entered &nbsp; (2) remain &nbsp; (3) deer &nbsp; (4) photographs &nbsp; <i>(2 marks each)</i>"),
    Q("Match Column A with Column B.<br>" + match(["Tiger", "Camel", "Peacock", "Cow", "Parrot"],
        ["national bird of India", "ship of the desert", "national animal of India", "gives us milk", "can imitate human speech"]), 5,
      "1 – c &nbsp; 2 – b &nbsp; 3 – a &nbsp; 4 – d &nbsp; 5 – e"),
    Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, "", parts=[
        P("(i)", "There is ___ ant on the wall.", 1, "an"), P("(ii)", "She is ___ best singer in our class.", 1, "the")]),
]
read = [
    Q("Read the passage carefully and answer Questions 15, 16 and 17.", 5, "", passage=P1, parts=[
        P("(i)", "In which district of Rajasthan is Ranthambore National Park?", 2, "In the Sawai Madhopur district."),
        P("(ii)", "Name any two animals, other than tigers, that visitors can see in the park.", 2, "Any two of: leopards, deer, crocodiles (and colourful birds)."),
        P("(iii)", "Find a word from the passage which means <i>thick</i>.", 1, "dense")]),
    rd(("Where do the tigers sometimes rest?", "They sometimes rest near the broken walls of the old fort."),
       ("Why had the number of tigers fallen?", "People hunted tigers and cut down the forests."),
       ("Write the opposite of <b>quiet</b>, using a word from the passage.", "loud")),
    rd(("When did the government begin Project Tiger?", "In 1973."),
       ("Write any two things we should not do when we visit a forest.", "We should not litter and we should not make loud noise."),
       ("Write the singular of <b>crocodiles</b>.", "crocodile")),
    Q("Read the passage carefully and answer Questions 18, 19 and 20.", 5, "", passage=P2, parts=[
        P("(i)", "What did Hari's grandfather give him?", 2, "A packet of marigold seeds."),
        P("(ii)", "Why did Hari feel sad after a week?", 2, "Because nothing had come up from the seeds."),
        P("(iii)", "Which word in the passage means <i>the quality of waiting calmly</i>?", 1, "patience")]),
    rd(("What did the grandfather say to Hari?", "He said that seeds need time."),
       ("What did Hari see ten days later?", "Tiny green leaves peeping out of the soil."),
       ("Write the opposite of <b>full</b>.", "empty")),
    rd(("Who came to visit the yard full of flowers?", "Bees and butterflies came to visit."),
       ("What did Hari do with a few flowers, and what did his friends ask him?", "He put them in a vase in the classroom; his friends asked him to teach them gardening."),
       ("Write the plural of <b>butterfly</b>.", "butterflies")),
]
write = [
    Q("Write a letter to your friend congratulating him/her on winning the first prize in the school drawing competition. (Your address: <i>9, Nehru Colony, Ajmer</i>; friend's name: Simran.)", 8,
      "<b>Marking:</b> format 2 + content (congratulations, how you came to know, praise, wish for future, regards) 4 + language 2.<br>"
      "<i>Model:</i> 9, Nehru Colony, Ajmer; 2 February 2027. Dear Simran, I was very happy to hear that you have won the first prize in the drawing competition. "
      "Your picture of the peacock was beautiful. You worked hard for it and you deserve this prize. Keep it up. My best wishes are with you. Yours lovingly, (name).",
      alt=Q("Write an application to your class teacher requesting a change of seat because you cannot see the blackboard clearly.", 8,
            "<b>Marking:</b> format 2 + content (problem, request, thanks) 4 + language 2.<br>"
            "<i>Model:</i> To, The Class Teacher, Class V, ... School, Ajmer. Date. Subject: Request for a change of seat. Respected Madam, I sit on the last bench and cannot see the blackboard clearly. "
            "Kindly allow me to sit on a front bench. I shall be thankful to you. Yours obediently, (name), Class V.")),
    Q("Look at the picture and write <b>four</b> sentences about it.<br><div style='font-size:24px;line-height:1.3'>🍎 🍌 🍇 🍊<br>🧑‍🌾 🛒 👩 🧺<br>☀️ 🚲 🐄</div>", 8,
      "<b>Marking:</b> 4 correct sentences x 2 (meaning 1 + grammar/spelling 1).<br><i>Model:</i> A fruit seller is selling fruits. A woman has come to buy fruits. Apples, bananas, grapes and oranges are kept in the shop. A cow is standing near a bicycle.",
      alt=Q("Complete the story using the hints: <i>Sports day – Kabir – race – fell down – got up – finished last – everybody clapped.</i>", 8,
            "<b>Marking:</b> story follows all hints 4 + sequence/linking 2 + language 2.<br><i>Model:</i> It was the sports day of our school. Kabir took part in the running race. In the middle of the race, he fell down. "
            "He got up quickly and began to run again. He finished last, but everybody clapped for his courage.")),
]
secs = [sec("LEXICAL ITEMS", 7, lex), sec("STRUCTURAL ITEMS", 27, struct), sec("READING COMPREHENSION", 30, read), sec("WRITING SKILLS", 16, write)]
if __name__ == "__main__":
    print(build(meta, secs))
