import sys, importlib, os
sys.path.insert(0, '/home/claude/pat'); sys.path.insert(0, '/home/claude/pat/c10m')
from lib_pat import build
which = sys.argv[1:] or ['1', '2', '3', '4', '5', 'f1']
for n in which:
    mod = importlib.import_module(n if n.startswith('f') else f"s{n}")
    meta, secs = mod.make()
    tag = 'FullSyllabus_Extra' if n.startswith('f') else 'MidTerm'
    build(meta, secs, '/home/claude/pat/out/Class10_Maths', f"Class10_Maths_{tag}_Set_{meta['set_no']:02d}")
    print('built', n)
