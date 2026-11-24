import json, sys
from chapters import CH
j = json.load(open(sys.argv[1], encoding="utf-8")); sub = j["subject"]; bad = []
tot = 0; nos = set()
for q in j["questions"]:
    nos.add(q["no"]); tot += q["marks"]
    if q["chapter"] not in CH[sub] + ["OTHER"]: bad.append((q["no"], "chapter", q["chapter"]))
    if q["type"] in ("mcq", "ar") and (not q.get("options") or len(q["options"]) != 4): bad.append((q["no"], "options"))
    if not q.get("answer") and not q.get("subparts"): bad.append((q["no"], "answer"))
    if "**" in q["text"]: bad.append((q["no"], "markup"))
print(sub, j["paper"], "questions", len(nos), "marks", tot, "problems", bad if bad else "none")
