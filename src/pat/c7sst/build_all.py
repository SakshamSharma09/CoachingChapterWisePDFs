import sys, os, importlib, time
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from lib8 import build
OUT = 'D:/Coaching Chapterwise PDFs/Class_07/Social_Science/School_Pattern_Papers'
for i in [int(a) for a in sys.argv[1:]] or [1,2,3]:
    s = importlib.import_module(f's{i}')
    for t in range(4):
        try: build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); break
        except OSError as e: print('retry', e); time.sleep(2)
    print('built', i)
