from hin_lib import P, S, Q, OR, mcq
CT = "निम्नलिखित स्थिति/अनुच्छेद को पढ़कर नीचे दिए गए प्रश्नों के उत्तर दीजिए।"
def C4(text, a, b):
    return P("<p>"+text+"</p>", [S(a[0], a[1], 2), S(b[0], b[1], 2)], title=CT)
def C6(text, a, b, c):
    return P("<p>"+text+"</p>", [S(a[0], a[1], 2), S(b[0], b[1], 2), S(c[0], c[1], 2)], title=CT)
def PAL(line, pts):
    return Q("निम्नलिखित पंक्ति का भाव-पल्लवन लगभग 60 शब्दों में कीजिए —<br><b>“"+line+"”</b>",
             "<b>केंद्रीय भाव :</b> "+pts+"<br><i>(केंद्रीय भाव 1 · विस्तार/तर्क-दृष्टांत 2 · भाषा-शुद्धता 1)</i>", "4")
def LET(q, pts, formal=True):
    fmt = "प्रेषक का पता, दिनांक, सेवा में/संबोधन, विषय, अभिवादन, मूलपाठ, समापन व हस्ताक्षर" if formal else "पता व दिनांक, संबोधन, अभिवादन, मूलपाठ, समापन (आपका/तुम्हारा ...)"
    return Q(q, "<b>पत्र-प्रारूप :</b> "+fmt+" (1)<br><b>मूल्यांकन-बिंदु :</b> "+pts+" (2)<br><b>भाषा-शुद्धता :</b> (1)", "4")
def ESS(*topics):
    q = "निम्नलिखित में से किसी <b>एक</b> विषय पर लगभग 250 शब्दों में निबंध लिखिए (रूपरेखा सहित) —<br>" + "<br>".join(f"({'अबस'[i]}) {t[0]}" for i, t in enumerate(topics))
    a = "<br>".join(f"<b>({'अबस'[i]}) {t[0]} :</b> {t[1]}" for i, t in enumerate(topics))
    return Q(q, a + "<br><i>(प्रस्तावना/रूपरेखा 1 · विषय-वस्तु 3 · भाषा-शैली 1 · उपसंहार 1)</i>", "6")
def SET(c32a, c32b, pa, pb, la, lb, ess, c36a, c36b):
    return dict(W=[OR(c32a, c32b), OR(pa, pb), OR(la, lb), ess, OR(c36a, c36b)])
