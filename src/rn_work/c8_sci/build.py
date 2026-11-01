import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c8_sci')
from notes import check_chapters, build_pdf
import ch08,ch09,ch10,ch11,ch12,ch13
chs=[m.CH for m in (ch08,ch09,ch10,ch11,ch12,ch13)]
check_chapters(chs)
meta=dict(title='Class 8 · Science', sub='NCERT Curiosity — Chapters 8 to 13 · CBSE / RBSE Syllabus', label='Grade 8 Science (Part 2)',
 how="PART 2 — CHAPTERS 8 to 13. Read each chapter's numbered sections in the textbook's order, learn the bold keywords and tables, revise the definition boxes, practise the activities, then test yourself with the Quick Questions and the Key Takeaways.")
build_pdf(meta, chs, '/home/claude/rn_out/Class8/Class8_Science_Revision_Notes_Part2_Ch08-13.pdf')
