import sys,os,glob,zipfile
sys.path.insert(0,'/home/claude/pat/c8eng')
import lib8, s1,s2,s3,s4,s5
out='/home/claude/pat/out/Class8_English'; os.makedirs(out,exist_ok=True)
for m in (s1,s2,s3,s4,s5): lib8.build(m.META,m.SET,out,f"Set_{m.META['set_no']:02d}")
z=zipfile.ZipFile('/home/claude/pat/out/Class8_English_SchoolPattern.zip','w',zipfile.ZIP_DEFLATED)
for f in sorted(glob.glob(out+'/*.pdf')): z.write(f,'Class8_English/'+os.path.basename(f))
z.close(); print(sorted(os.listdir(out)))
