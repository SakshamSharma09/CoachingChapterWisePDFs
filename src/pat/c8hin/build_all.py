import importlib, render
for i in range(1,6):
    m=importlib.import_module(f's{i}'); assert render.paper_marks(m.PAPER)==60
    render.build(m.PAPER,'/home/claude/pat/out/Class8_Hindi')
