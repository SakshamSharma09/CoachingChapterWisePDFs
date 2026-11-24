"""Step 1: copy the sample-paper PDFs into Class_10/<Subject>/Sample_Papers_2026-27/ with clean names and
write per-paper working files (page PNGs, embedded figures with positions, line text)."""
import pymupdf, json, os, shutil, sys
SRC = r"C:\Users\Saksham\AppData\Local\Temp\sp10"
WORK = r"C:\Users\Saksham\AppData\Local\Temp\claude\0da2d72d58043887\fc748be4-719d-4cc6-9a85-08dc202f3924\scratchpad\sp10work"
REPO = r"D:\Coaching Chapterwise PDFs"
OFF = {"Maths": "3lnZcz", "Science": "5YIbHs", "SST": "wCToE8", "English": "p1YTY9", "Hindi": "Qf9wpm"}
FOLDER = {"Maths": "Maths", "Science": "Science", "SST": "Social_Science", "English": "English", "Hindi": "Hindi"}
ident = json.load(open(os.path.join(SRC, "ident.json")))
papers = {}
for sub in OFF:
    fs = [f for f, v in sorted(ident.items()) if v[0] == sub]
    off = [f for f in fs if f.startswith(OFF[sub])][0]; rest = [f for f in fs if f != off]
    papers[sub] = [("CBSE_Official", off)] + [("Paper_%02d" % (i + 1), f) for i, f in enumerate(rest)]
json.dump(papers, open(os.path.join(WORK, "papers.json"), "w"), indent=1)
for sub, lst in papers.items():
    dst = os.path.join(REPO, "Class_10", FOLDER[sub], "Sample_Papers_2026-27"); os.makedirs(dst, exist_ok=True)
    for pid, f in lst:
        shutil.copy(os.path.join(SRC, f), os.path.join(dst, "%s_Class10_%s_Sample_Paper_with_Solutions.pdf" % (pid, FOLDER[sub])))
        d = pymupdf.open(os.path.join(SRC, f)); wd = os.path.join(WORK, sub, pid); os.makedirs(wd, exist_ok=True)
        figs = []
        for pi, p in enumerate(d):
            p.get_pixmap(dpi=100).save(os.path.join(wd, "page%02d.png" % (pi + 1)))
            for k, im in enumerate(p.get_image_info(xrefs=True)):
                b = im["bbox"]
                if b[2] - b[0] < 25 or b[3] - b[1] < 25: continue
                fn = os.path.join(wd, "fig_p%02d_%d.png" % (pi + 1, k))
                p.get_pixmap(dpi=150, clip=pymupdf.Rect(*b)).save(fn)
                figs.append(dict(page=pi + 1, k=k, bbox=[round(x) for x in b], file=fn))
        json.dump(figs, open(os.path.join(wd, "figs.json"), "w"), indent=0)
        print(sub, pid, len(d), "pages", len(figs), "figs", flush=True)
