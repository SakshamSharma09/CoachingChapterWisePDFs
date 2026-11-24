import sys, pymupdf
pdf, pg, x0, y0, x1, y1, out = sys.argv[1:8]
d = pymupdf.open(pdf); d[int(pg) - 1].get_pixmap(dpi=150, clip=pymupdf.Rect(float(x0), float(y0), float(x1), float(y1))).save(out)
