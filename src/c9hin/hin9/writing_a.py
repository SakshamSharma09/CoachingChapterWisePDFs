from hin9._wr import *
from hin9._wrpool import *
SETS = {}
for i in range(1, 11):
    k = 2*(i-1)
    c4 = [C4(t, a, b) for t, a, b in (C4S[k], C4S[k+1])]
    c6 = [C6(t, a, b, c) for t, a, b, c in (C6S[k], C6S[k+1])]
    pa = [PAL(*PALS[k]), PAL(*PALS[k+1])]
    le = [LET(q, p, f) for q, p, f in (LETS[k], LETS[k+1])]
    es = ESS(*ESSS[3*(i-1):3*(i-1)+3])
    SETS[i] = SET(c4[0], c4[1], pa[0], pa[1], le[0], le[1], es, c6[0], c6[1])
