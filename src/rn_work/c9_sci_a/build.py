import sys
sys.path[:0]=['/home/claude/rnlib','/home/claude/rn_work/c9_sci_a']
import notes, c01,c02,c03,c04,c05,c06,c07
chs=[m.CH for m in (c01,c02,c03,c04,c05,c06,c07)]
notes.check_chapters(chs)
meta=dict(title='Class 9 · Science', sub='NCERT Curiosity — Chapters 1 to 7 · CBSE / RBSE Syllabus', label='Grade 9 Science')
notes.build_pdf(meta, chs, '/home/claude/rn_out/Class9/Class9_Science_Revision_Notes_Part1_Ch01-07.pdf')
