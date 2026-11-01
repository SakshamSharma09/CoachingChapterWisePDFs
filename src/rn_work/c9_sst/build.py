import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c9_sst')
from notes import check_chapters, build_pdf
import importlib
chs=[importlib.import_module(f"c0{i}").CH for i in range(1,9)]
check_chapters(chs)
meta=dict(title="Class 9 · Social Science", sub="Exploring Society: India and Beyond — Chapters 1 to 8 · CBSE / RBSE Syllabus", label="Grade 9 Social Science")
out="/home/claude/rn_out/Class9/Class9_SocialScience_Revision_Notes_Ch01-08.pdf"
build_pdf(meta,chs,out); print("built")
