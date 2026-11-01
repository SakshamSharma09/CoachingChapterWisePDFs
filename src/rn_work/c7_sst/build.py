import sys, importlib; sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c7_sst')
from notes import check_chapters, build_pdf
chs=[importlib.import_module('c%02d'%i).CH for i in range(1,13)]
check_chapters(chs)
import os; os.makedirs('/home/claude/rn_out/Class7',exist_ok=True)
for k,(a,b) in enumerate([(1,6),(7,12)],1):
    part=chs[a-1:b]
    out=f'/home/claude/rn_out/Class7/Class7_SocialScience_Revision_Notes_Part{k}_Ch{a}-{b}.pdf'
    build_pdf(dict(title="Class 7 · Social Science", sub=f"Exploring Society: India and Beyond — Chapters {a} to {b} · CBSE / RBSE Syllabus", label="Grade 7 Social Science"), part, out)
    print(out)
