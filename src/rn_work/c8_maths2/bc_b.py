import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c8_maths2')
from notes import check_chapters
import importlib
mods = sys.argv[1:] or ["c12","c13","c14"]
chs=[importlib.import_module(m).CH for m in mods]
check_chapters(chs); print("ok", [c["num"] for c in chs])
