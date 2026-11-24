"""Cut every question (and its solution) out of the Class 10 2026-27 sample-paper PDFs as images.

Usage: python extract.py <subject>   (Maths|Science|SST|English|Hindi)
Reads  SRC (extracted zip) + ident.json ; writes WORK/<subject>/<paper>/qNN.png, aNN.png and WORK/<subject>/index.json
Each question: {paper, no, marks, text, qimg:[...], aimg:[...]}.
"""
import pymupdf, re, json, os, sys, glob
SRC = os.environ.get("SP_SRC", r"C:\Users\Saksham\AppData\Local\Temp\sp10")
WORK = os.environ.get("SP_WORK", r"C:\Users\Saksham\AppData\Local\Temp\claude\0da2d72d58043887\fc748be4-719d-4cc6-9a85-08dc202f3924\scratchpad\sp10work")
ZOOM = 2.0
HEAD = re.compile(r'^\s*(SECTION|Section|खंड|खण्ड|SOLUTION|Solution|MARKING|Marking|Section\s*[-–])')

def lines_of(page):
    out = []
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines", []):
            t = ''.join(s['text'] for s in l['spans']).strip()
            if t: out.append((l['bbox'], t))
    return out

def find_chains(d, maxq):
    """return list of chains; each chain = list of (page, y, no)"""
    cands = []
    for pi, p in enumerate(d):
        for bb, t in lines_of(p):
            m = re.match(r'^(\d{1,2})\s*[.)]\s*(.*)$', t)
            if m and bb[0] < 95:
                cands.append((pi, bb[1], int(m.group(1)), bb[0]))
    chains = []; cur = []; exp = 1
    for pi, y, n, x in cands:
        if n == exp and (not cur or True):
            cur.append((pi, y, n)); exp += 1
        elif n == 1 and len(cur) >= max(8, maxq // 3):
            chains.append(cur); cur = [(pi, y, 1)]; exp = 2
    if cur: chains.append(cur)
    return [c for c in chains if len(c) >= max(6, maxq // 3)]

def stops(d):
    """y positions of section headings / solution headers: (page,y,text)"""
    r = []
    for pi, p in enumerate(d):
        for bb, t in lines_of(p):
            if HEAD.match(t) and len(t) < 90: r.append((pi, bb[1], t))
    return r

def crop(d, pi, y0, y1, out, x0=26, x1=None):
    p = d[pi]; w = p.rect.width
    r = pymupdf.Rect(x0, max(y0 - 3, 0), (x1 or w - 26), min(y1, p.rect.height - 22))
    if r.height < 6: return False
    p.get_pixmap(matrix=pymupdf.Matrix(ZOOM, ZOOM), clip=r).save(out); return True

def segment(d, chain, hs, endpage_limit=None):
    """crops spec: list per question of [(page,y0,y1)]"""
    res = []
    H = lambda pi: d[pi].rect.height - 22
    for k, (pi, y, n) in enumerate(chain):
        if k + 1 < len(chain): npi, ny, _ = chain[k + 1]
        else: npi, ny = None, None
        segs = []
        # headings between this start and next start
        def stop_after(pg, ystart, yend):
            c = [h for (hp, hy, ht) in hs if hp == pg and hy > ystart + 4 and hy < yend - 1 for h in [hy]]
            return min(c) if c else None
        if npi is None:
            # last in chain: until heading or end of page (and following pages up to heading)
            pg = pi; ys = y
            while True:
                s = stop_after(pg, ys, 10**6)
                if s is not None: segs.append((pg, ys, s)); break
                segs.append((pg, ys, H(pg)))
                if pg + 1 >= len(d) or pg - pi >= 1: break
                pg += 1; ys = 30
                # stop if next page begins with heading
            res.append(segs); continue
        pg = pi; ys = y
        while pg < npi:
            s = stop_after(pg, ys, 10**6)
            if s is not None: segs.append((pg, ys, s)); ys = None; break
            segs.append((pg, ys, H(pg))); pg += 1; ys = 30
        if ys is not None:
            s = stop_after(pg, ys, ny)
            segs.append((pg, ys, s if s is not None else ny))
        res.append(segs)
    return res

def paper_marks(text, no, sub):
    m = re.search(r'\[(\d{1,2})\]', text) or re.search(r'\((\d)\s*[Mm]arks?\)', text)
    return int(m.group(1)) if m else None

def run(sub, files):
    outd = os.path.join(WORK, sub); os.makedirs(outd, exist_ok=True)
    index = []
    maxq = {"Maths": 38, "Science": 39, "SST": 38, "English": 11, "Hindi": 15}[sub]
    for pid, f in files:
        d = pymupdf.open(os.path.join(SRC, f))
        chains = find_chains(d, maxq)
        hs = stops(d)
        print(pid, f[:6], "chains", [(len(c), c[0][0]) for c in chains])
        if len(chains) < 1: continue
        qc = chains[0]; ac = chains[1] if len(chains) > 1 else []
        qs = segment(d, qc, hs); as_ = segment(d, ac, hs) if ac else []
        pd = os.path.join(outd, pid); os.makedirs(pd, exist_ok=True)
        for k, (pi, y, n) in enumerate(qc):
            imgs = []
            for j, (pg, y0, y1) in enumerate(qs[k]):
                fn = os.path.join(pd, "q%02d_%d.png" % (n, j))
                if crop(d, pg, y0, y1, fn): imgs.append(fn)
            txt = ' '.join(' '.join(t for _, t in [l for l in lines_of(d[pg]) if l[0][1] >= y0 - 3 and l[0][1] < y1]) for pg, y0, y1 in qs[k])
            aimgs = []
            if k < len(ac):
                for j, (pg, y0, y1) in enumerate(as_[k]):
                    fn = os.path.join(pd, "a%02d_%d.png" % (n, j))
                    if crop(d, pg, y0, y1, fn): aimgs.append(fn)
            index.append(dict(paper=pid, no=n, marks=paper_marks(txt, n, sub), text=txt, qimg=imgs, aimg=aimgs, npages=len(qs[k])))
    json.dump(index, open(os.path.join(outd, "index.json"), "w"), ensure_ascii=False, indent=0)
    return index

if __name__ == "__main__":
    sub = sys.argv[1]
    ident = json.load(open(os.path.join(SRC, "ident.json")))
    fs = [f for f, v in sorted(ident.items()) if v[0] == sub]
    official = [f for f in fs if True]
    # official CBSE paper first: marked by 'SAMPLE QUESTION PAPER' in page text AND larger/other layout
    OFF = {"Maths": "3lnZcz", "Science": "5YIbHs", "SST": "wCToE8", "English": "p1YTY9", "Hindi": "Qf9wpm"}[sub]
    off = [f for f in fs if f.startswith(OFF)]; rest = [f for f in fs if not f.startswith(OFF)]
    files = [("CBSE_Official", off[0])] + [("Paper_%02d" % (i + 1), f) for i, f in enumerate(rest)]
    run(sub, files)
