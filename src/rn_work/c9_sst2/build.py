import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c9_sst2')
from notes import check_chapters, build_pdf
import importlib
chs=[importlib.import_module(f"c{i:02d}").CH for i in range(9,15)]
check_chapters(chs)
meta=dict(title="Class 9 · Social Science", sub="Exploring Society: India and Beyond — Part 2, Chapters 9 to 14 · CBSE / RBSE Syllabus", label="Grade 9 Social Science · Part 2")
build_pdf(meta,chs,"/home/claude/rn_out/Class9/Class9_SocialScience_Revision_Notes_Part2_Ch09-14.pdf"); print("built")
