import sys; sys.path.insert(0,'/home/claude/gw/part1')
from xlib import ex_blocks,key_blocks,count
import d_a1,d_a2,d_a3,d_b1,d_b2,d_b3,d_c
A=d_a1.A+d_a2.A+d_a3.A
B=d_b1.B+d_b2.B+d_b3.B
C=d_c.C
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
