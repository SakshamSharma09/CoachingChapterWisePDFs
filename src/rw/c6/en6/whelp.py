from eng6_lib import Q, OR
def N(q, ans): return Q(q, ans, "3")
def L(q, ans): return Q(q, ans, "5")
def A(q, ans): return Q(q, ans, "4")
def g(q, ans): return Q(q, ans, "1")
FN = "<i>(Format 1 · Content 1 · Language 1)</i>"
FL = "<i>(Format 1 · Content 2 · Organisation 1 · Language 1)</i>"
FA = "<i>(Content 2 · Organisation 1 · Language 1)</i>"
def NOT(date, title, body, by):
    return f"<b>NOTICE</b><br>{date}<br><b>{title}</b><br>{body}<br>{by}<br>" + FN
def MSG(date, to, body, frm):
    return f"{date}, 4:30 p.m.<br>Dear {to},<br>{body}<br>{frm}<br>" + FN
def LET(addr, date, to, body, frm):
    return f"{addr}<br>{date}<br>Dear {to},<br>{body}<br>Your loving friend,<br>{frm}<br>" + FL
def LETF(addr, date, to, body, frm, rel="Your loving"):
    return f"{addr}<br>{date}<br>Dear {to},<br>{body}<br>{rel},<br>{frm}<br>" + FL
def EML(to, subj, body, frm):
    return f"<b>To:</b> {to}<br><b>Subject:</b> {subj}<br>Dear {to.split('@')[0].title()},<br>{body}<br>Yours lovingly,<br>{frm}<br>" + FL
def PAR(title, body): return f"<b>{title}</b><br>{body}<br>" + FA
def DIA(date, body): return f"{date}<br>9:00 p.m.<br>Dear Diary,<br>{body}<br>" + FA
