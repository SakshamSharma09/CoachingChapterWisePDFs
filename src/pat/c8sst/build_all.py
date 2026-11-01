import sys, importlib, os, zipfile
sys.path.insert(0, '/home/claude/pat/c8sst')
from lib8 import build
OUT = '/home/claude/pat/out/Class8_SST'
sets = [int(a) for a in sys.argv[1:]] or range(1, 6)
for i in sets:
    s = importlib.import_module(f's{i}'); build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); print('built', i)
if not sys.argv[1:]:
    os.chdir('/home/claude/pat/out')
    z = zipfile.ZipFile('/home/claude/pat/out/Class8_SST_SchoolPattern.zip', 'w', zipfile.ZIP_DEFLATED)
    for f in sorted(os.listdir('Class8_SST')): z.write(f'Class8_SST/{f}')
    z.close()
