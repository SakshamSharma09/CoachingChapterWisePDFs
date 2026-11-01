import sys, importlib
sys.path.insert(0,'/home/claude/pat/c9m_full12')
from cm import build
n=int(sys.argv[1]); s=importlib.import_module(f'f{n}')
build(s.META, s.SECTIONS, '/home/claude/pat/out/Class9_Maths_FullYear_Part1+2', f'Set_0{n}'); print('built',n)
