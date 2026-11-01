import sys; sys.path.insert(0,'/home/claude/gw/part2')
import yb1, yb2, yb3
groups = {"1":"Gap Filling (Passage-based MCQ)","2":"Editing","3":"Omission","4":"Sentence Reordering","5":"Dialogue Completion","6":"Reported Speech (Dialogue to Paragraph)","7":"Newspaper Headlines","8":"Procedure / Instruction Reporting","9":"Sentence Transformation","10":"Sentence Completion"}
blocks=[]; seen=set()
for b in yb1.B + yb2.B + yb3.B:
    if b[0]=="h3":
        g=b[1].split(" · ")[0][1:].split(".")[0]
        if g not in seen:
            seen.add(g); blocks.append(("h2", f"B{g} · {groups[g]}"))
    blocks.append(b)
order=[x for x in range(len(blocks))]
CH = dict(num=18, title="Exercise Bank · Part B — Question-type Practice", tag="Exercises",
 intro="Board-pattern sets by question type: five gap-filling passages, five editing, five omission and five reordering sets, five dialogues, six reported-speech conversations, five sets of headlines, six procedure passages, five transformation sets and eight sentence-completion sets. Work through one type at a time.",
 blocks=blocks,
 takeaways=["Gap filling: read the whole passage first, find its tense, then check subject-verb agreement.",
  "Editing: one error per line — look for tense, agreement, articles, prepositions and word form.",
  "Omission: the missing word is usually an article, preposition, auxiliary or conjunction.",
  "Reordering: find subject, verb, object, then the adverbials.",
  "Headlines: decide past, present perfect or future from the news, and use the passive where the doer is unknown.",
  "Procedure: use the passive with the tense of the hint (is/are or was/were)."])
