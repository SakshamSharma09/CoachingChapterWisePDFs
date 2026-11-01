import sys; sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c9_sci_b')
from notes import *
import c08,c09,c10,c11,c12,c13
chs=[c08.CH,c09.CH,c10.CH,c11.CH,c12.CH,c13.CH]
check_chapters(chs)
import os; os.makedirs('/home/claude/rn_out/Class9',exist_ok=True)
build_pdf(dict(title='Class 9 · Science', sub='NCERT Curiosity — Chapters 8 to 13 · CBSE / RBSE Syllabus', label='Grade 9 Science'), chs, '/home/claude/rn_out/Class9/Class9_Science_Revision_Notes_Part2_Ch08-13.pdf')
print('built')
