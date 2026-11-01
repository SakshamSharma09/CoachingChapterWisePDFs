from eng9_lib import Q, OR, mcq
def N(q, ans): return Q(q, ans + "<br><i>(Format 1 · Content 1 · Language 1)</i>", "3")
def L(q, ans): return Q(q, ans + "<br><i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>", "5")
def A(q, ans): return Q(q, ans + "<br><i>(Content 2 · Organisation 1 · Language 1)</i>", "4")
def g(q, ans): return Q(q, ans, "1")
