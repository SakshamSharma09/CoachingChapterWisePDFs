import sys, importlib
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c9_sst2')
from notes import check_chapters
check_chapters([importlib.import_module(m).CH for m in ("c11","c12")]); print("ok")
