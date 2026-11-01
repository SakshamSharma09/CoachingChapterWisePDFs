import sys,importlib
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part1')
from notes import check_chapters, build_pdf
chs=[importlib.import_module(f"g0{i}").CH for i in range(1,10)]
check_chapters(chs)
meta=dict(title="English Grammar Workbook",sub="Part 1 · Classes 5–8 (trial: chapters 1–9)",label="Grammar Part 1")
build_pdf(meta,chs,"/home/claude/gw/scratch1a/trial.pdf");print("ok")
