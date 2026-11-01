import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c9_sst2')
from notes import check_chapters
import importlib
chs=[importlib.import_module(m).CH for m in sys.argv[1:] or ["c09","c10"]]
check_chapters(chs); print("ok", [c["num"] for c in chs])
