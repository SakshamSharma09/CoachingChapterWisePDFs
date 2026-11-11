import os; os.environ.setdefault('CHROMIUM_PATH', os.path.expanduser('~/AppData/Local/ms-playwright/chromium-1248/chrome-win64/chrome.exe'))
import sys, os, importlib, time
sys.path.insert(0, 'D:/Coaching Chapterwise PDFs/src/pat/c6m')
import lib8
OUT = 'D:/Coaching Chapterwise PDFs/Class_06/Maths/School_Pattern_Papers'
for i in [int(a) for a in sys.argv[1:]] or [1, 2, 3]:
    s = importlib.import_module(f's{i}')
    for t in range(4):
        try: lib8.L.build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); break
        except OSError as e: print('retry', e); time.sleep(1)
    print(i, 'ok')
