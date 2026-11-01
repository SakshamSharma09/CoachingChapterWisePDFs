import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part2')
from notes_compact import check_chapters, build_pdf
import y01,y02,y03,y04,yhelp
chs=[y01.CH,y02.CH,y03.CH,y04.CH]
check_chapters(chs)
print(yhelp.COUNT, sum(yhelp.COUNT.values()))
build_pdf(dict(title="t",sub="t",label="t"),chs,"/home/claude/gw/scratch_t2c/t.pdf")
