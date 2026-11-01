from eng9_lib import P, S
def mc(q, right, *wrong):
    return S(q, "a", 1, [right, *wrong])
def sa(q, ans):
    return S(q, ans, 1)
