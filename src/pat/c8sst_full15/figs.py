"""Tiny SVG helpers. All return SVG strings. Coordinates in SVG pixels (y down)."""
def svg(w, h, body): return f"<svg xmlns='http://www.w3.org/2000/svg' width='{w}' height='{h}' viewBox='0 0 {w} {h}' font-family='Arial' font-size='12'>{body}</svg>"
def line(x1, y1, x2, y2, c='#000', w=1.4, dash=None): return f"<line x1='{x1}' y1='{y1}' x2='{x2}' y2='{y2}' stroke='{c}' stroke-width='{w}'{' stroke-dasharray=%s' % chr(39)+dash+chr(39) if dash else ''}/>"
def circ(cx, cy, r, c='#000', fill='none', w=1.4): return f"<circle cx='{cx}' cy='{cy}' r='{r}' stroke='{c}' stroke-width='{w}' fill='{fill}'/>"
def text(x, y, t, anchor='middle', sz=12, c='#000'): return f"<text x='{x}' y='{y}' text-anchor='{anchor}' font-size='{sz}' fill='{c}'>{t}</text>"
def poly(pts, c='#000', fill='none', w=1.4): return f"<polygon points='{' '.join(f'{x},{y}' for x,y in pts)}' stroke='{c}' stroke-width='{w}' fill='{fill}'/>"
def dot(x, y, label='', dx=6, dy=-6): return f"<circle cx='{x}' cy='{y}' r='2.6' fill='#000'/>" + (text(x+dx, y+dy, label, 'start') if label else '')
def coord_plane(pts, xr=(-6, 6), yr=(-6, 6), u=24, segs=(), labels=True):
    """pts: {label:(x,y)}; segs: [(label1,label2)] or [((x1,y1),(x2,y2))]. Math coords."""
    W = (xr[1]-xr[0])*u+40; H = (yr[1]-yr[0])*u+40
    X = lambda x: 20+(x-xr[0])*u; Y = lambda y: 20+(yr[1]-y)*u
    b = ""
    for i in range(xr[0], xr[1]+1): b += line(X(i), 20, X(i), H-20, '#ddd', .6)
    for j in range(yr[0], yr[1]+1): b += line(20, Y(j), W-20, Y(j), '#ddd', .6)
    b += line(20, Y(0), W-20, Y(0), '#000', 1.2) + line(X(0), 20, X(0), H-20, '#000', 1.2)
    for i in range(xr[0], xr[1]+1):
        if i: b += text(X(i), Y(0)+13, i, sz=9)
    for j in range(yr[0], yr[1]+1):
        if j: b += text(X(0)-8, Y(j)+3, j, sz=9)
    for s in segs:
        p, q = [pts[a] if isinstance(a, str) else a for a in s]; b += line(X(p[0]), Y(p[1]), X(q[0]), Y(q[1]), '#0f2347', 1.6)
    for k, (x, y) in pts.items(): b += dot(X(x), Y(y), f"{k}" if labels else '')
    return svg(W, H, b)
