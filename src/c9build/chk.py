import sys, re, importlib, glob
sys.path.insert(0, '.')
def val(sp):
    t = 0
    for part in sp.split('+'):
        part = part.strip()
        m = re.fullmatch(r'(\d*)(½?)', part)
        if not m: return None
        t += (int(m.group(1)) if m.group(1) else 0) + (0.5 if m.group(2) else 0)
    return t
def check(modname):
    m = importlib.import_module(modname); bad = 0
    for nm, L, mk in (("B", m.B, 2), ("C", m.C, 3), ("D", m.D, 5)):
        for i, q in enumerate(L):
            v = val(q.get('split', '') or '')
            if v != mk:
                print(modname, nm, i, 'split', q.get('split'), q['q'][:50]); bad += 1
            t = q['q'] + q['ans']
            if re.search(r'[\x07\x08\x09\x0c\x0b]', t) or '...' in q['q'] or 'extension' in t or 'rather' in q['q'][:40]:
                print(modname, nm, i, 'artifact', q['q'][:50]); bad += 1
            if not (q['q'][:1].isupper() or q['q'][:1] in '(<$‘0123456789'):
                print(modname, nm, i, 'start', q['q'][:30]); bad += 1
    for i, q in enumerate(m.A):
        if len(set(q['opts'])) != 4: print(modname, 'A dup opts', i); bad += 1
    return bad
if __name__ == "__main__":
    for a in sys.argv[1:]: print(a, check(a))
