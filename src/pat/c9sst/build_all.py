import sys, importlib, shutil, os
sys.path.insert(0, '/home/claude/pat/c9sst'); sys.path.insert(0, '/home/claude/pat')
from lib_pat import build
OUT = '/home/claude/pat/out/Class9_SST'
for i in range(1, 6):
    s = importlib.import_module(f's{i}'); build(s.META, s.SECTIONS, OUT, f'Set_{i:02d}'); print('built', i)
os.chdir('/home/claude/pat/out'); 
import zipfile
z = zipfile.ZipFile('/home/claude/pat/out/Class9_SST_SchoolPattern.zip', 'w', zipfile.ZIP_DEFLATED)
for f in sorted(os.listdir('Class9_SST')): z.write(f'Class9_SST/{f}')
z.close()
