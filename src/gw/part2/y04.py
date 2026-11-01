import sys; sys.path.insert(0,'/home/claude/gw/part2')
import y01, y02, y03
from yhelp import KEY
blocks=[("p","Answers are listed set by set. In editing and omission keys, bold shows the wrong word and its correction or the missing word; italics give reasons for tricky items; a slash separates acceptable alternatives.")]
def grp(part, label_fn):
    last=None; out=[]
    for b in KEY[part]:
        if b[0]=="h3":
            g=label_fn(b[1])
            if g!=last: out.append(("h2",g)); last=g
        out.append(b)
    return out
blocks += [("h2","Part A — Topic-wise Exercises")] + KEY['A']
blocks += grp('B', lambda t: "Part B — " + {"1":"Gap Filling","2":"Editing","3":"Omission","4":"Reordering","5":"Dialogue Completion","6":"Reported Speech","7":"Headlines","8":"Procedure","9":"Transformation","10":"Sentence Completion"}[t.split(" · ")[0][1:].split(".")[0]])
blocks += grp('C', lambda t: "Part C — Practice Test " + t.split(" · ")[0][1:].split(".")[0])
CH = dict(num=20, title="Exercise Bank · Part D — Complete Answer Key", tag="Answer Key",
 intro="Answers to every exercise in Parts A, B and C. Check only after finishing a set.",
 blocks=blocks,
 takeaways=["Compare, then redo wrong items in your own words; re-attempt them after seven days."])
