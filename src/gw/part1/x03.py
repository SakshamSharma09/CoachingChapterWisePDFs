from xall import *
b=[("h2","Instructions")]
b.append(("p","Each test carries 20 marks (1 mark for each item). Time allowed: 40 minutes. Test 1 is meant for Classes 5–6 and Test 2 for Classes 7–8."))
b.append(("h2","Test 1 (Classes 5–6) — 20 Marks"))
for s in C:
    if s['id'].startswith("C1"): b+=ex_blocks(s)
b.append(("h2","Test 2 (Classes 7–8) — 20 Marks"))
for s in C:
    if s['id'].startswith("C2"): b+=ex_blocks(s)
b.append(("h2","Marking Scheme"))
b.append(("table",["Marks","Remark"],[["18–20","Excellent"],["15–17","Very good"],["12–14","Good — revise weak topics"],["Below 12","Revise chapters and re-attempt Part A"]]))
CH=dict(num=22,tag="Exercise Bank · Part C",title="Mixed Practice Tests",
 intro="Two full-length mixed tests that combine tenses, agreement, editing and transformation, as in a school paper.",blocks=b,
 takeaways=["Attempt under timed conditions without notes.","Compare with the key in Chapter 23 and note your weak topics."])
