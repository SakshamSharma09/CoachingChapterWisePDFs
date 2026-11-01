import sys; sys.path.insert(0,'/home/claude/gw/part2')
import ya1, ya2
blocks = []
for b in ya1.A + ya2.A:
    blocks.append(("h2", b[1]) if b[0]=="h3" else b)
CH = dict(num=17, title="Exercise Bank · Part A — Topic-wise Practice (14 Syllabus Topics)", tag="Exercises",
 intro="One exercise set for each of the fourteen prescribed grammar topics. Each set mixes board-paper forms: MCQ, fill-in, error correction, joining and rewriting. Do a set after revising the matching chapter and check it against Part D.",
 blocks=blocks,
  takeaways=["Attempt a set without notes, then mark it with Part D.",
  "For every wrong answer, write the rule in one line; repeat the set after a week."])
