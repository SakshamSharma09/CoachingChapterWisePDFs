import os; os.environ.setdefault('CHROMIUM_PATH', os.path.expanduser('~/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe'))
import sys, importlib, time
sys.path.insert(0, 'D:/Coaching Chapterwise PDFs/src/pat/c6sst')
from lib8 import build
OUT = 'D:/Coaching Chapterwise PDFs/Class_06/Social_Science/School_Pattern_Papers'
for i in [int(a) for a in sys.argv[1:]] or [1, 2, 3]:
    s = importlib.import_module(f's{i}')
    for t in range(4):
        try: build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); break
        except OSError as e: print('retry', e); time.sleep(1)
    print('built', i)
