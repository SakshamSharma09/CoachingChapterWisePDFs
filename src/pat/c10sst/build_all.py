import sys, importlib, os
sys.path.insert(0, '/home/claude/pat/c10sst')
from lib_pat import build
OUT = '/home/claude/pat/out/Class10_SST'
for i in range(1, 6):
    if len(sys.argv) > 1 and str(i) not in sys.argv[1:]: continue
    try: m = importlib.import_module(f's{i}')
    except ModuleNotFoundError: continue
    n = sum(len(s['items']) for s in m.SECTIONS); assert n == 38, (i, n)
    build(m.META, m.SECTIONS, OUT, f'Set_{i:02d}'); print('built', i)
