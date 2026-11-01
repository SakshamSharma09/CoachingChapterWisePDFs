import sys, importlib, os, zipfile
sys.path.insert(0, '/home/claude/pat/c9sst_full14'); sys.path.insert(0, '/home/claude/pat')
from lib_pat import build
OUT = '/home/claude/pat/out/Class9_SST_FullYear_Part1+2'
for i in range(1, 6):
    try: s = importlib.import_module(f'f{i}')
    except ModuleNotFoundError: continue
    build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); print('built', i)
os.chdir('/home/claude/pat/out')
z = zipfile.ZipFile('/home/claude/pat/out/Class9_SST_FullYear_Part1+2_SchoolPattern.zip', 'w', zipfile.ZIP_DEFLATED)
for f in sorted(os.listdir('Class9_SST_FullYear_Part1+2')): z.write(f'Class9_SST_FullYear_Part1+2/{f}')
z.close()
