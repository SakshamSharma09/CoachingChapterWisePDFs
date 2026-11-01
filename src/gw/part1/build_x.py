import sys; sys.path.insert(0,'/home/claude/gw/part1'); sys.path.insert(0,'/home/claude/rnlib')
from notes import check_chapters,build_pdf
import x01,x02,x03,x04
chs=[x01.CH,x02.CH,x03.CH,x04.CH]
check_chapters(chs)
from xall import A,B,C,count
print("items",count(A),count(B),count(C),count(A)+count(B)+count(C))
meta=dict(title="Grammar Workbook · Part 1",sub="Exercise Bank and Answer Key — Classes 5 to 8",label="Grammar Part 1 Exercises")
build_pdf(meta,chs,"/home/claude/gw/scratch_g1c/part1_exercises_trial.pdf"); print("built")
