import sys
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part1')
from notes_compact import check_chapters, build_pdf
import importlib
mods=[f"g{i:02d}" for i in range(1,20)]+[f"x0{i}" for i in range(1,5)]
chs=[importlib.import_module(m).CH for m in mods]
check_chapters(chs)
meta=dict(title="English Grammar Workbook · Part 1", sub="Classes 5 to 8 — Complete Grammar with Exercises and Answer Key · CBSE / RBSE", label="English Grammar Part 1 (Classes 5-8)")
build_pdf(meta,chs,"/home/claude/gw/out/English_Grammar_Workbook_Part1_Classes5-8_v2.pdf"); print("ok")
