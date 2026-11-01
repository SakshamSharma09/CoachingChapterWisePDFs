import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/rn_work/c8_maths2')
from notes import check_chapters, build_pdf
import importlib
mods=sys.argv[1:] or ["c08","c09","c10","c11"]
chs=[importlib.import_module(m).CH for m in mods]
check_chapters(chs); print("ok",[c["num"] for c in chs])
if "--pdf" in sys.argv: pass
build_pdf(dict(title="Class 8 · Mathematics", sub="Ganita Prakash — Part 2, test build", label="Grade 8 Maths · Part 2"), chs, "/tmp/m8p2_notes_test.pdf"); print("pdf built")
