"""Create data/Mock_<Subject>_<n>.json skeletons: official-paper structure; ~35% of marks real sample questions (copied),
~40% 'variant' slots (agent rewrites a given sample question with new values/context), ~25% 'ncert' slots (agent writes an
NCERT-exercise-style question). Usage: python mockplan.py <Subject> <count>"""
import json, sys, random, os, collections
from pathlib import Path
HERE = Path(__file__).resolve().parent
PAPERS = ["CBSE_Official"] + ["Paper_%02d" % i for i in range(1, 11)]

def ld(sub, p):
    return json.load(open(HERE / "data" / f"{sub}_{p}.json", encoding="utf-8"))["questions"]

def main(sub, count):
    off = ld(sub, "CBSE_Official")
    pool = []
    for p in PAPERS:
        for q in ld(sub, p):
            pool.append(dict(q, paper=p))
    used = set()
    rnd = random.Random(7 + len(sub))
    total = sum(q["marks"] for q in off)
    for n in range(1, count + 1):
        skel_paper = PAPERS[n]  # Paper_01.. gives the chapter pattern per slot
        sk = {q["no"]: q for q in ld(sub, skel_paper)}
        slots = []
        for q in off:
            ref = sk.get(q["no"], q)
            # slot keeps the official structure; chapter taken from this paper's slot (if same marks), else official
            ch = ref["chapter"] if ref["marks"] == q["marks"] else q["chapter"]
            slots.append(dict(no=q["no"], section=q["section"], marks=q["marks"], type=q["type"], chapter=ch))
        order = list(range(len(slots))); rnd.shuffle(order)
        target = {"real": 0.35 * total, "variant": 0.40 * total, "ncert": 0.25 * total}
        got = collections.Counter(); kinds = ["real", "variant", "ncert"]
        for i in order:
            s = slots[i]
            k = max(kinds, key=lambda x: target[x] - got[x])
            s["origin"] = k; got[k] += s["marks"]
        out = []
        for s in slots:
            def pick(avoid_used=True):
                c = [q for q in pool if q["marks"] == s["marks"] and q["type"] == s["type"] and q["chapter"] == s["chapter"] and (q["paper"], q["no"]) not in used and q["paper"] != "CBSE_Official"]
                if not c: c = [q for q in pool if q["marks"] == s["marks"] and q["type"] == s["type"] and q["chapter"] != "OTHER" and (q["paper"], q["no"]) not in used and q["paper"] != "CBSE_Official"]
                if not c: c = [q for q in pool if q["marks"] == s["marks"] and q["type"] == s["type"] and (q["paper"], q["no"]) not in used]
                return rnd.choice(c) if c else None
            if s["origin"] == "real":
                q = pick()
                if q is None: s["origin"] = "ncert"; out.append(dict(s)); continue
                used.add((q["paper"], q["no"])); r = dict(q); r["no"] = s["no"]; r["section"] = s["section"]; r["origin"] = "real"; r["basis"] = f"{q['paper']} Q{q['no']}"
                out.append(r)
            elif s["origin"] == "variant":
                q = pick()
                if q is None: s["origin"] = "ncert"; out.append(dict(s)); continue
                used.add((q["paper"], q["no"]))
                out.append(dict(s, chapter=q["chapter"], basis=f"{q['paper']} Q{q['no']}", basis_question=q, text=None, options=None, answer=None, subparts=None, figure=None, **{"or": None}))
            else:
                out.append(dict(s, text=None, options=None, answer=None, subparts=None, figure=None, **{"or": None}))
        json.dump(dict(subject=sub, paper=f"Mock_{n:02d}", questions=out), open(HERE / "data" / f"Mock_{sub}_{n:02d}.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
        print(sub, n, {k: v for k, v in got.items()})

if __name__ == "__main__":
    main(sys.argv[1], int(sys.argv[2]))
