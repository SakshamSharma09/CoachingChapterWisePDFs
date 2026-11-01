from eng6_lib import P, S
def M(q, c, a, b, d): return S(q, "a", 1, [c, a, b, d])
def T(q, ans): return S(q, ans, 1)
def PS(paras, mcqs, shorts, title="Read the passage carefully and answer the questions that follow.", head_=""):
    txt = "".join(f"<p>{p}</p>" for p in paras)
    return P(txt, [M(*x) for x in mcqs] + [S(q, a, 1) for q, a in shorts], title, head_)
def POEM(lines, mcqs, shorts, head_):
    txt = "<p style='text-align:center'>" + "<br>".join(lines) + "</p>"
    return P(txt, [M(*x) for x in mcqs] + [S(q, a, 1) for q, a in shorts], "Read the poem carefully and answer the questions that follow.", head_)
