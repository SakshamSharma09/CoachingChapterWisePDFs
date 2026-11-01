import os, shutil, glob, re
R='/home/claude/repo'; H='/home/claude'
shutil.rmtree(R, ignore_errors=True); os.makedirs(R)
def cp(src, dst, nozip=True):
    if not os.path.exists(src): print("MISSING", src); return
    if os.path.isfile(src):
        os.makedirs(os.path.dirname(dst), exist_ok=True); shutil.copy2(src, dst); return
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in ('__pycache__',)]
        for f in files:
            if nozip and f.endswith('.zip'): continue
            s = os.path.join(root, f); d = os.path.join(dst, os.path.relpath(s, src))
            os.makedirs(os.path.dirname(d), exist_ok=True); shutil.copy2(s, d)
SUB = {'Maths':'Maths','Science':'Science','SocialScience':'Social_Science','SST':'Social_Science','English':'English','Hindi':'Hindi','Social Science':'Social_Science'}
def C(n): return f"{R}/Class_{n:02d}"
# 1. practice papers (chapterwise etc.)
for n, base in [(6,'out6'),(7,'out7'),(8,'out8'),(9,'out9'),(10,'papers')]:
    for d in sorted(glob.glob(f"{H}/{base}/*_Paper_Generated")):
        sub = SUB[os.path.basename(d).split('_')[0]]
        cp(d, f"{C(n)}/{sub}/Practice_Papers")
# 2. part2 / full-year (our format)
for n, base in [(8,'out8'),(9,'out9')]:
    for d in sorted(glob.glob(f"{H}/{base}/*Part2_Papers")):
        sub = SUB[os.path.basename(d).split('_')[0]]; cp(d, f"{C(n)}/{sub}/Part2_Papers")
    for d in sorted(glob.glob(f"{H}/{base}/*FullYear_Part1+2")):
        sub = SUB[os.path.basename(d).split('_')[0]]; cp(d, f"{C(n)}/{sub}/FullYear_Part1+2_Papers")
# 3. school-pattern
for d in sorted(glob.glob(f"{H}/pat/out/Class*")):
    if d.endswith('.zip'): continue
    b = os.path.basename(d); m = re.match(r'Class(\d+)_(\w+?)(_FullYear_Part1\+2)?$', b)
    n = int(m.group(1)); sub = SUB[m.group(2)]
    cp(d, f"{C(n)}/{sub}/" + ("School_Pattern_FullYear_Part1+2" if m.group(3) else "School_Pattern_Papers"))
# 4. revision notes (latest)
def notes(n, files):
    for f in files:
        b = os.path.basename(f); sub = 'Maths' if 'Maths' in b else 'Science' if 'Science_' in b and 'Social' not in b else 'Social_Science'
        cp(f, f"{C(n)}/{sub}/Revision_Notes/{b}")
for n in (6,7): notes(n, glob.glob(f"{H}/rn_final/Class{n}_Revision_Notes/*.pdf"))
notes(8, glob.glob(f"{H}/rn_final/Class8_Revision_Notes/*.pdf") + glob.glob(f"{H}/rn_out/Class8/*.pdf"))
notes(9, glob.glob(f"{H}/rn_final/Class9_Revision_Notes/*.pdf") + [p for p in glob.glob(f"{H}/rn_out/Class9/*.pdf") if 'Ch09-12' not in p])
# 5. reading & writing
for n in range(5, 11):
    for d in glob.glob(f"{H}/rw/out/Class{n}/*Reading_Writing*") :
        if os.path.isdir(d): cp(d, f"{C(n)}/English/Reading_Writing")
    for md in glob.glob(f"{H}/rw/out/Class{n}/AUDIT_NOTES.md"): cp(md, f"{C(n)}/English/Reading_Writing/AUDIT_NOTES.md")
# 6. grammar workbooks
for f in glob.glob(f"{H}/gw/out/*_v2.pdf"): cp(f, f"{R}/English_Grammar_Workbooks/{os.path.basename(f)}")
# 7. docs
os.makedirs(f"{R}/docs", exist_ok=True)
for f in glob.glob(f"{H}/pat/final/*.md"): cp(f, f"{R}/docs/{os.path.basename(f)}")
cp(f"{H}/pat/BLUEPRINT.md", f"{R}/docs/School_Pattern_BLUEPRINT.md")

# 8. generator source (code only)
SRC=f"{R}/src"
def code(src, dst, exts=('.py','.md','.json','.js','.txt','.css','.html')):
    for root, dirs, files in os.walk(src):
        dirs[:] = [d for d in dirs if d not in ('__pycache__','node_modules','out9','out','txt','raw','pdf','final','samples')]
        for f in files:
            if f.endswith(exts) and os.path.getsize(os.path.join(root,f)) < 2_000_000:
                s_=os.path.join(root,f); d_=os.path.join(dst, os.path.relpath(s_, src)); os.makedirs(os.path.dirname(d_), exist_ok=True); shutil.copy2(s_, d_)
for b in ('c6build','c7build','c8build','c9build','c9hin','pat','rnlib','rn_work','gw','rw','c9p2','c8p2','c8m2','m9p2','tools'):
    if os.path.isdir(f"{H}/{b}"): code(f"{H}/{b}", f"{SRC}/{b}")
print("done")
