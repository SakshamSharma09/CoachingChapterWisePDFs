import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c8_maths2')
from notes import check_chapters, build_pdf
import importlib
chs=[importlib.import_module(f"c{i:02d}").CH for i in range(8,15)]
check_chapters(chs)
meta=dict(title="Class 8 · Mathematics", sub="Ganita Prakash — Part 2, Chapters 8 to 14 · CBSE / RBSE Syllabus", label="Grade 8 Mathematics · Part 2")
build_pdf(meta,chs,"/home/claude/rn_out/Class8/Class8_Maths_Revision_Notes_Part2_Ch08-14.pdf"); print("built")
