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

meta = dict(subject="English", set_no=7, time="2.30 Hours", marks=80, instr=[
    "This question paper is based on the learning areas of English: lexical, structural, reading and writing skills.",
    "Write your Name and Roll No. in the space given at the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly."])

P1 = ("<b>Catching the Rain</b><br>In many parts of Rajasthan, there is very little rain, so people have learnt to save every drop. "
      "Long ago, villagers dug johads, which are small ponds that collect rainwater during the monsoon. Tall houses had tanks called tankas under their courtyards. "
      "When it rained, the water ran down the roofs through pipes and filled the tanka. The families used this clean water for many months. "
      "Today, schools and offices also build such tanks. This method is called rainwater harvesting. It stops water from flowing away and helps the ground water level to rise. "
      "Children can help too. They can close the taps tightly and never waste water while brushing their teeth. If everyone saves a little, we shall have enough water for tomorrow.")
P2 = ("<b>The Squirrel and the Mango Tree</b><br>A squirrel named Chinku lived in an old mango tree at the edge of a village. Every summer, the tree gave sweet fruit, and Chinku shared it with the birds. "
      "One year, a strong wind broke a big branch, and the tree looked weak. A crow said, 'This tree is of no use now. Let us find another home.' Chinku shook his head. "
      "'This tree has given us shade and fruit for years. We must not leave it when it needs us,' he said. The next day, Chinku and his friends carried clay and leaves and covered the wound of the tree. "
      "By the next monsoon, new green shoots appeared on the branch. The tree stood tall again, and all the creatures lived happily in its shade.")

lex = [
    mcq("Ravi lost ___ pen, so I gave him mine.", ["her", "his", "their", "its"], 1),
    mcq("Choose the synonym of <b>silent</b>.", ["noisy", "angry", "quiet", "bright"], 2),
    mcq("Choose the antonym of <b>generous</b>.", ["kind", "rich", "quiet", "selfish"], 3),
    mcq("She is ___ honest girl.", ["a", "an", "the", "any"], 1),
    mcq("Choose the word in which the underlined letters sound different:", ["c<u>ow</u>", "n<u>ow</u>", "sn<u>ow</u>", "br<u>ow</u>n"], 2),
    mcq("Which word is formed by adding the suffix <b>-less</b> to <b>care</b>?", ["careful", "caring", "carefree", "careless"], 3),
    mcq("The children ___ football yesterday.", ["played", "play", "plays", "playing"], 0),
]
struct = [
    Q("Rearrange the jumbled letters to make meaningful words.", 2, "", parts=[
        P("(i)", "R T E W A", 1, "WATER"), P("(ii)", "O O M N S O N", 1, "MONSOON")]),
    Q("Choose the appropriate word from the bracket to complete each sentence.", 2, "", parts=[
        P("(i)", "Fish live in ___ . (water / sand)", 1, "water"), P("(ii)", "We use an ___ in the rain. (umbrella / pillow)", 1, "umbrella")]),
    Q("Fill in the blanks with suitable words from the bracket. (farmer, sowed, quickly)", 3, "", parts=[
        P("(i)", "The ___ ploughed his field.", 1, "farmer"), P("(ii)", "He ___ wheat seeds in the soil.", 1, "sowed"),
        P("(iii)", "The rain clouds gathered ___ .", 1, "quickly")]),
    Q("Choose the correct option from the bracket.", 5, "", parts=[
        P("(i)", "The Taj Mahal ___ in Agra. (is / are)", 1, "is"),
        P("(ii)", "The baby ___ sleeping in the cradle. (was / were)", 1, "was"),
        P("(iii)", "My brother usually ___ to the ground at five. (go / goes)", 1, "goes"),
        P("(iv)", "We shall visit our grandparents ___ Sunday. (on / in)", 1, "on"),
        P("(v)", "I ___ go to Jaipur tomorrow. (will / did)", 1, "will")]),
    Q("Complete the passage using the words given in the box. Write the answers in the order of blanks.<br>" + box(["line", "medal", "sports", "came"]) +
      "Raju's school held a (1) ______ day last week. All the students stood in a (2) ______ and waited for their turn. "
      "Raju ran very fast and (3) ______ first in the race. The principal gave him a shining (4) ______ .", 8,
      "(1) sports &nbsp; (2) line &nbsp; (3) came &nbsp; (4) medal &nbsp; <i>(2 marks each)</i>"),
    Q("Match Column A with Column B.<br>" + match(["Footpath", "Helmet", "Seat belt", "Yellow light", "Traffic police"],
        ["keeps a car passenger safe", "controls vehicles at the crossing", "protects the head of a scooter rider", "warns us to slow down", "path for people to walk"]), 5,
      "1 – e &nbsp; 2 – c &nbsp; 3 – a &nbsp; 4 – d &nbsp; 5 – b"),
    Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, "", parts=[
        P("(i)", "My father is ___ engineer.", 1, "an"), P("(ii)", "We saw ___ Red Fort in Delhi.", 1, "the")]),
]
read = [
    Q("Read the passage carefully and answer Questions 15, 16 and 17.", 5, "", passage=P1, parts=[
        P("(i)", "Why have people in Rajasthan learnt to save every drop of rain?", 2, "Because there is very little rain in many parts of Rajasthan."),
        P("(ii)", "What is a johad?", 2, "A johad is a small pond that collects rainwater during the monsoon."),
        P("(iii)", "Write the word from the passage that is the opposite of <b>dirty</b>.", 1, "clean")]),
    rd(("Where were the tankas built?", "They were built under the courtyards of tall houses."),
       ("How did rainwater reach the tanka?", "It ran down the roofs and flowed through pipes into the tanka."),
       ("Write the singular of <b>families</b>.", "family")),
    rd(("What is rainwater harvesting?", "It is a method of saving rainwater (in tanks and ponds) so that it does not flow away."),
       ("Write any two ways in which children can help to save water.", "They can close the taps tightly and not waste water while brushing their teeth."),
       ("Write the opposite of <b>waste</b> (as used in the passage).", "save")),
    Q("Read the passage carefully and answer Questions 18, 19 and 20.", 5, "", passage=P2, parts=[
        P("(i)", "Where did Chinku live?", 2, "He lived in an old mango tree at the edge of a village."),
        P("(ii)", "What happened to the tree one year?", 2, "A strong wind broke a big branch and the tree looked weak."),
        P("(iii)", "Find a word from the passage which means <i>a place protected from the sun</i>.", 1, "shade")]),
    rd(("What did the crow suggest?", "The crow suggested that they should find another home because the tree was of no use now."),
       ("Why did Chinku refuse to leave the tree?", "The tree had given them shade and fruit for years, so he felt they must not leave it when it needed them."),
       ("Write the opposite of <b>weak</b>.", "strong")),
    rd(("How did Chinku and his friends help the tree?", "They carried clay and leaves and covered the wound of the tree."),
       ("What happened by the next monsoon?", "New green shoots appeared on the branch and the tree stood tall again."),
       ("Write the plural of <b>branch</b>.", "branches")),
]
write = [
    Q("Write a letter to your uncle thanking him for the storybook he sent you on your birthday. (Your address: <i>7, Gandhi Nagar, Jaipur</i>.)", 8,
      "<b>Marking:</b> format (address, date, salutation, closing) 2 + content (thanks, what you liked in the book, news of home, regards) 4 + language 2.<br>"
      "<i>Model:</i> 7, Gandhi Nagar, Jaipur; 20 April 2027. Dear Uncle, Thank you very much for the lovely storybook. I read it in two days. The story of the brave girl was my favourite. "
      "Everybody at home is fine. Please give my regards to Aunty. Your loving nephew/niece, (name).",
      alt=Q("Write an application to the Principal requesting him/her to arrange a water cooler in your school.", 8,
            "<b>Marking:</b> format (To, Date, Subject, Salutation, closing) 2 + content (problem, request, thanks) 4 + language 2.<br>"
            "<i>Model:</i> To, The Principal, ... School, Jaipur. Date. Subject: Request for a water cooler. Respected Sir/Madam, It is hot in summer and the children feel very thirsty. "
            "We have only one tap and the water is not cold. Kindly arrange a water cooler on our floor. Thank you. Yours obediently, (name), Class V.")),
    Q("Look at the picture and write <b>four</b> sentences about it.<br><div style='font-size:24px;line-height:1.3'>🌧️ ☁️ 🌈<br>🏠 🌳 ☔ 🧒<br>🐸 🌱 🐸 🚰</div>", 8,
      "<b>Marking:</b> 4 correct sentences x 2 (meaning 1 + grammar/spelling 1).<br><i>Model:</i> It is raining heavily. A boy is holding an umbrella. Two frogs are sitting near the plants. A rainbow has appeared in the sky.",
      alt=Q("Complete the story using the hints: <i>Ria – new school bag – lost on the bus – crying – conductor found it – returned – thanked him.</i>", 8,
            "<b>Marking:</b> story follows all hints 4 + sequence/linking 2 + language 2.<br><i>Model:</i> Ria had a new school bag. One day she lost it on the bus. She began to cry. The conductor found the bag under a seat. "
            "He came to her house and returned it. Ria thanked him with a smile.")),
]
secs = [sec("LEXICAL ITEMS", 7, lex), sec("STRUCTURAL ITEMS", 27, struct), sec("READING COMPREHENSION", 30, read), sec("WRITING SKILLS", 16, write)]
if __name__ == "__main__":
    print(build(meta, secs))
