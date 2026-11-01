from render import *
T = lambda lines: "<br>".join(lines)
def mc(q,o,a): return P(q,1,a,'',opts=o)
def mcs(l): return [mc(*x) for x in l]
def sh(l): return [P(q,m,a) for q,m,a in l]
def gram(title_stem, rows, ans, singles):
    t="<table class='t'>"+"".join(f"<tr><td>({ROM[i]}) {a}</td><td>{b}</td></tr>" for i,(a,b) in enumerate(rows))+"</table>"
    return Q(3,"निम्नलिखित व्याकरणिक प्रश्नों के उत्तर लिखिए-",'plain',mknote="(10×1=10)",
      parts=[P(title_stem+t,3,ans)]+[P(q,1,a) for q,a in singles])
def paper(n, u1, u2, g, t4, q5, q6, q7, q8, q9, l1, l2, topics):
    Q1=Q(1,"निम्नलिखित अपठित गद्यांश को पढ़िए और पूछे गए प्रश्नों के उत्तर लिखिए-",'plain',passage=u1[0],parts=mcs(u1[1])+sh(u1[2]))
    Q2=Q(2,"निम्नलिखित अपठित पद्यांश को पढ़िए और पूछे गए प्रश्नों के उत्तर लिखिए-",'plain',poem=True,passage=T(u2[0]),parts=mcs(u2[1])+sh(u2[2]))
    Q4=Q(4,"निम्नलिखित गद्यांश को पढ़िए और पूछे गए प्रश्नों के उत्तर लिखिए-",'plain',mknote="(4×1=4)",passage=t4[0],parts=mcs(t4[1]))
    Q5=Q(5,"गद्य पाठों पर आधारित निम्नलिखित प्रश्नों में से <b>किन्हीं दो</b> के उत्तर लिखिए-",'any2',mknote="(2×2=4)",parts=sh(q5))
    Q6=Q(6,"गद्य पाठों पर आधारित निम्नलिखित प्रश्नों में से <b>किन्हीं दो</b> के उत्तर लगभग 30-40 शब्दों में लिखिए-",'any2',mknote="(2×3=6)",parts=sh(q6))
    Q7=Q(7,"निम्नलिखित पद्यांश को पढ़िए और पूछे गए प्रश्नों के उत्तर लिखिए-",'plain',mknote="(4×1=4)",poem=True,passage=T(q7[0]),parts=mcs(q7[1]))
    Q8=Q(8,"पद्य पाठों पर आधारित निम्नलिखित प्रश्नों में से <b>किन्हीं दो</b> के उत्तर लिखिए-",'any2',mknote="(2×2=4)",parts=sh(q8))
    Q9=Q(9,"पद्य पाठों पर आधारित निम्नलिखित प्रश्नों में से <b>किन्हीं दो</b> के उत्तर लगभग 30-40 शब्दों में लिखिए-",'any2',mknote="(2×3=6)",parts=sh(q9))
    mk="<br>(अंक-विभाजन : प्रारूप 2, विषय-वस्तु 3, भाषा 1)"
    Q10=Q(10,"निम्नलिखित में से किसी <b>एक</b> विषय पर लगभग 80-100 शब्दों में पत्र लिखिए-",'or',mknote="(1×6=6)",m=6,a=dict(q=l1[0],sol="<i>"+l1[1]+"</i>"+mk),b=dict(q=l2[0],sol="<i>"+l2[1]+"</i>"+mk))
    Q11=Q(11,"निम्नलिखित में से किसी <b>एक</b> विषय पर लगभग 80-100 शब्दों में अनुच्छेद लिखिए-",'topics',mknote="(1×6=6)",m=6,topics=topics)
    return dict(set_no=n,sections=[dict(title="खंड-क (अपठित बोध)",qs=[Q1,Q2]),dict(title="खंड-ख (व्यावहारिक व्याकरण)",qs=[g]),
      dict(title="खंड-ग (पाठ्यपुस्तक)",qs=[Q4,Q5,Q6,Q7,Q8,Q9]),dict(title="खंड-घ (रचनात्मक लेखन)",qs=[Q10,Q11])])
