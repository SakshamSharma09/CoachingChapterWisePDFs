import sys; sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part2')
import importlib
from notes import check_chapters
for m in sys.argv[1:]:
    c=importlib.import_module(m).CH; check_chapters([c]); print(m,'ok',len(str(c)))
