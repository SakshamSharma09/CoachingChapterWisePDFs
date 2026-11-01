import sys; sys.path.insert(0,'/home/claude/pat/c9m')
import importlib
for n in range(1,6):
    s = importlib.import_module(f's{n}')
    build(s.META, s.SECTIONS, '/home/claude/pat/out/Class9_Maths', f'Set_0{n}') if False else None
from common import build
for n in range(1,6):
    s = importlib.import_module(f's{n}')
    build(s.META, s.SECTIONS, '/home/claude/pat/out/Class9_Maths', f'Set_0{n}'); print('built', n)
