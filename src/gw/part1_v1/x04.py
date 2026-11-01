from xall import *
b=[("h2","How to Use This Key")]
b.append(("p","Answers are numbered to match the exercise sets. Where several answers are acceptable, they are shown separated by a slash or marked 'also'. Italic text gives a short reason for the trickier items."))
b.append(("h2","Part A — Topic-wise Practice"))
for i,t in enumerate(TOPICS,1):
    b.append(("h3",f"Topic {i}: {t}"))
    for s in A:
        if s['id'].startswith(f"A{i}-"): b+=key_blocks(s)[0:]
b.append(("h2","Part B — Exam-pattern Question Types"))
for p,t in BTYPES:
    b.append(("h3",f"{p} {t}"))
    for s in B:
        if s['id'].split('.')[0]==p: b+=key_blocks(s)
b.append(("h2","Part C — Mixed Practice Tests"))
for s in C: b+=key_blocks(s)
CH=dict(num=23,tag="Answer Key",title="Complete Answer Key",
 intro="Complete answers for every set in Chapters 20–22.",blocks=b,
 takeaways=["Check each wrong answer against the chapter rule, not just the key.","For sentence transformation, any grammatically correct sentence with the same meaning earns credit."])
