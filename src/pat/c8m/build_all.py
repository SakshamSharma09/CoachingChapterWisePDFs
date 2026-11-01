import sys; sys.path.insert(0,'/home/claude/pat/c8m'); sys.path.insert(0,'/home/claude/pat')
import importlib, lib8
for i in range(1,6):
    s=importlib.import_module(f's{i}')
    lib8.L.build(s.META, s.SECTIONS, '/home/claude/pat/out/Class8_Maths', f'Set_{i:02d}'); print(i,'ok')
