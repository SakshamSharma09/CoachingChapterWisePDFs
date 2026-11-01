import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c8_sst2')
from notes import check_chapters, build_pdf
import importlib
chs=[importlib.import_module(f"c{i:02d}").CH for i in range(8,16)]
check_chapters(chs)
meta=dict(title="Class 8 · Social Science", sub="Exploring Society: India and Beyond — Part 2, Chapters 8 to 15 · CBSE / RBSE Syllabus", label="Grade 8 Social Science · Part 2")
build_pdf(meta,chs,"/home/claude/rn_out/Class8/Class8_SocialScience_Revision_Notes_Part2_Ch08-15.pdf"); print("built")
