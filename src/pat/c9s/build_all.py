import sys, importlib, os
sys.path.insert(0, '/home/claude/pat/c9s')
for i in range(1, 6): importlib.import_module(f's{i}').run(); print('built', i)
os.system("cd /home/claude/pat/out && rm -f Class9_Science_SchoolPattern.zip && zip -qr Class9_Science_SchoolPattern.zip Class9_Science && ls -la Class9_Science_SchoolPattern.zip")
