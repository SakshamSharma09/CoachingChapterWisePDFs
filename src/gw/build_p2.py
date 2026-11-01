import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part2')
from notes_compact import check_chapters, build_pdf
import importlib
mods=[f"h{i:02d}" for i in range(1,17)]+[f"y0{i}" for i in range(1,5)]
chs=[importlib.import_module(m).CH for m in mods]
check_chapters(chs)
meta=dict(title="English Grammar Workbook · Part 2", sub="Classes 9 and 10 — Complete Board-Level Grammar with Exercises and Answer Key · CBSE / RBSE", label="English Grammar Part 2 (Classes 9-10)")
build_pdf(meta,chs,"/home/claude/gw/out/English_Grammar_Workbook_Part2_Classes9-10_v2.pdf"); print("ok")
