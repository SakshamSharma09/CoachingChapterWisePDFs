from hin9._rd import G, V
from hin9._rdpool import GAD, PAD
SETS = {}
for i in range(1, 11):
    a, b = GAD[2*(i-1)], GAD[2*(i-1)+1]
    c, d = PAD[2*(i-1)], PAD[2*(i-1)+1]
    SETS[i] = dict(R=[G(a[0], *a[1]), G(b[0], *b[1]), V(c[0], *c[1]), V(d[0], *d[1])])
