"""Stage only COMPLETE graded chapters (16 PDFs, no temp files) + graded sources; prints what was staged."""
import subprocess, glob, os, sys
root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
os.chdir(root)
staged = []
for ch in sorted(glob.glob("Class_*/*/Graded_Papers/Ch*") + glob.glob("Class_*/*/Graded_Papers/Unit_Tests/*") + glob.glob("Class_*/*/Graded_Papers/Full_Year")):
    pdfs = glob.glob(ch + "/*/*.pdf"); junk = glob.glob(ch + "/*/_k*") + glob.glob(ch + "/*/*.html")
    if len(pdfs) == 16 and not junk:
        subprocess.run(["git", "add", "--", ch], check=True); staged.append(ch)
subprocess.run(["git", "add", "--", "src/graded"], check=True)
print(len(staged), "complete chapters staged")
for s in staged: print(" ", s)
