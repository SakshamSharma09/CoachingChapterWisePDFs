import sys, importlib
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'.')
from notes import build_pdf
mods=[importlib.import_module('c%02d'%i).CH for i in range(1,15)]
for k,(a,b) in enumerate([(1,7),(8,14)],1):
    meta=dict(title='Class 6 · Social Science', sub=f'Exploring Society: India and Beyond — Chapters {a} to {b} · CBSE / RBSE Syllabus', label='Class 6 Social Science')
    print(build_pdf(meta, mods[a-1:b], f'/home/claude/rn_out/Class6/Class6_SocialScience_Revision_Notes_Part{k}_Ch{a}-{b}.pdf'))
