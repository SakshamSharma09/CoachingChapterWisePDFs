import sys; sys.path.insert(0,'/home/claude/gw/part1')
from xlib import ex_blocks,key_blocks,count
import d_a1,d_a2,d_a3,d_b1,d_b2,d_b3,d_c
A=d_a1.A+d_a2.A+d_a3.A
B=d_b1.B+d_b2.B+d_b3.B
C=d_c.C
# --- trim pass (shorten workbook, v2) ---
DROPA={"A1-I":(8,9),"A1-II":(3,7),"A2-I":(1,7),"A2-II":(6,7),"A3-I":(6,7),"A3-II":(5,6),"A4-I":(1,9),"A4-II":(5,6),"A5-I":(5,9),"A5-II":(6,9),"A6-I":(6,9),"A6-II":(8,9),"A7-I":(5,9),"A7-II":(1,6),"A8-I":(3,6),"A8-II":(2,8),"A9-I":(1,7),"A9-II":(3,8),"A10-I":(5,7),"A10-II":(8,9),"A11-I":(6,9),"A11-II":(4,7),"A12-I":(5,9),"A12-II":(2,9),"A13-I":(8,9),"A13-II":(3,9),"A14-I":(6,9),"A14-II":(3,8),"A15-I":(4,8),"A15-II":(4,9),"A16-I":(4,9),"A16-II":(4,9),"A17-I":(7,9),"A17-II":(3,8),"A18-I":(4,8),"A18-II":(3,9),"A19-I":(1,6),"A19-II":(4,8)}
for s_ in A:
    d=DROPA.get(s_['id'],())
    s_['items']=[it for i,it in enumerate(s_['items']) if i not in d]
DROPB={"B1.2","B2.2","B3.2","B4.2","B5.4","B6.2","B7.2","B8.2","B9.5","B11.2","B12.1","B13.2"}
B=[s_ for s_ in B if s_['id'] not in DROPB]
_cnt={}
for s_ in B:
    p=s_['id'].split('.')[0]
    old=s_['id']; _cnt[p]=_cnt.get(p,0)+1
    s_['id']=f"{p}.{_cnt[p]}"
for s_ in A+B+C:
    if s_['id'].startswith("B3."): continue
    s_['items']=[it[:2] if (len(it)>2 and len(it[2])>55) else it for it in s_['items']]
NUM={"B10.1","B10.3","C1-B","C2-B"}
for s in A+B+C:
    if s['id'] in NUM: s['num']=True
TOPICS=["Parts of Speech","Nouns","Pronouns","Determiners","Adjectives and Comparison","Adverbs","Verbs: Kinds and Forms","Tenses","Subject–Verb Agreement","Modals","Non-finites","Prepositions","Conjunctions and Connectors","Relatives","Conditionals","Active and Passive Voice","Reported Speech","Sentences, Clauses and Transformation","Vocabulary and Word Usage"]
BTYPES=[("B1","Gap Filling (Cloze with Options)"),("B2","Editing"),("B3","Omission"),("B4","Sentence Reordering"),("B5","Dialogue Completion"),("B6","Reported Speech: Dialogue to Paragraph"),("B7","Newspaper Headlines"),("B8","Procedure Reporting (Passive)"),("B9","Sentence Transformation"),("B10","Sentence Completion"),("B11","Verb Forms in a Passage"),("B12","Cloze: Prepositions and Determiners"),("B13","Spot the Error")]
def grouped_A(fn):
    b=[]
    for i,t in enumerate(TOPICS,1):
        b.append(("h2",f"Topic {i}: {t}"))
        for s in A:
            if s['id'].startswith(f"A{i}-"): b+=fn(s)
    return b
def grouped_B(fn):
    b=[]
    for p,t in BTYPES:
        b.append(("h2",f"{p}  {t}"))
        for s in B:
            if s['id'].split('.')[0]==p: b+=fn(s)
    return b
