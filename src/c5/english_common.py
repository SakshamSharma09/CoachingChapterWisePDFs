"""Shared assembly helper for Class 5 English model papers (data-driven)."""
from lib5 import *

INSTR = [
    "This question paper is based on the learning areas of Class V English (Lexical, Structural, Reading and Writing).",
    "Write your Name and Roll No. in the space given on the top of the question paper.",
    "All questions are compulsory.",
    "The marks for each question are given against it.",
    "Write your answers neatly and legibly.",
]

def mcq(q, opts, k):
    return Q(q, 1, f"({'abcd'[k]}) {opts[k]}", opts=opts)

def comp(passage, title, sets):
    """sets = list of 3 lists [(q, ans, marks)*3] -> three Q of 5 marks; passage on the first of the set."""
    out = []
    for i, s in enumerate(sets):
        assert [m for _, _, m in s] == [2, 2, 1], s
        parts = [P(f"({'i ii iii'.split()[j]})", q, m, a) for j, (q, a, m) in enumerate(s)]
        stem = "Read the passage carefully and answer the questions that follow." if i == 0 else ""
        ps = f"<b>{title}</b><br>{passage}" if i == 0 else None
        out.append(Q(stem, 5, parts=parts, passage=ps))
    return out

def make(no, lex, jumble, choose2, fill3, choose5, cloze, match, arts, readA, readB, letter, pic):
    s1 = [mcq(q, o, k) for q, o, k in lex]
    assert len(s1) == 7
    q8 = Q("Rearrange the jumbled letters to make meaningful words. (A hint is given.)", 2, parts=[
        P(f"({'i ii'.split()[n]})", f"<b>{j}</b> &nbsp;({h})", 1, a) for n, (j, h, a) in enumerate(jumble)])
    q9 = Q("Choose the appropriate option from the brackets to complete the sentences.", 2, parts=[
        P(f"({'i ii'.split()[n]})", t, 1, a) for n, (t, a) in enumerate(choose2)])
    words, stems, ans = fill3
    q10 = Q(f"Fill in the blanks with suitable words from the bracket: <b>({' / '.join(words)})</b>", 3, parts=[
        P(f"({'i ii iii'.split()[i]})", t, 1, a) for i, (t, a) in enumerate(zip(stems, ans))])
    q11 = Q("Choose the correct option from the brackets and rewrite the sentences.", 5, parts=[
        P(f"({'i ii iii iv v'.split()[i]})", t, 1, a) for i, (t, a) in enumerate(choose5)])
    text, box, cans = cloze
    q12 = Q("Complete the passage with the help of the words given in the box. (Two words are extra.)"
            "<br><table class='t5' style='margin-left:0'><tr>" + "".join(f"<td>{w}</td>" for w in box) + "</tr></table>" + text.removeprefix("<br>"),
            8, "<br>".join(f"({i+1}) <b>{a}</b> &nbsp;[2]" for i, a in enumerate(cans)))
    A, B, mans = match
    rows = "".join(f"<tr><td style='text-align:left'>{i+1}. {a}</td><td style='text-align:left'>({'abcde'[i]}) {b}</td></tr>"
                   for i, (a, b) in enumerate(zip(A, B)))
    q13 = Q("Match Column A with Column B.<table class='t5' style='margin-left:0'><tr><th>Column A</th><th>Column B</th></tr>" + rows + "</table>",
            5, " &nbsp; ".join(f"{i+1} &rarr; {m}" for i, m in enumerate(mans)))
    q14 = Q("Fill in the blanks with <b>a</b>, <b>an</b> or <b>the</b>.", 2, parts=[
        P(f"({'i ii'.split()[i]})", t, 1, a) for i, (t, a) in enumerate(arts)])
    secs = [
        sec("LEXICAL ITEMS", 7, s1, "(Choose the correct option)"),
        sec("STRUCTURAL ITEMS", 27, [q8, q9, q10, q11, q12, q13, q14]),
        sec("READING COMPREHENSION", 30, comp(*readA) + comp(*readB)),
        sec("WRITING", 16, [letter, pic]),
    ]
    meta = dict(subject="English", set_no=no, time="2.30 Hours", marks=80, instr=INSTR)
    print(build(meta, secs))

def sample_box(title, body):
    return f"<b>{title}</b><br>{body}"
