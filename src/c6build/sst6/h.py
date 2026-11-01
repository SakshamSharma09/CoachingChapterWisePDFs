from lib import mcq, Q, OR
from mk9 import M4, build
def MC(rows):
    return [M4(r[0], r[1], r[2], r[3] if len(r) > 3 else r[1]) for r in rows]
