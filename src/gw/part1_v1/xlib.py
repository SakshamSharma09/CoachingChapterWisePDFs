"""Shared helpers for Part 1 exercise bank (G1c). Sets render to exercise blocks and key blocks from one source."""
def L(sid, title, ins, items, body=None):
    return dict(id=sid, t=title, ins=ins, items=items, body=body, mode="ol")
def T(sid, title, ins, items, body=None, head="Item"):
    return dict(id=sid, t=title, ins=ins, items=items, body=body, mode="tab", head=head)
def labels(n,num=False): return [str(i+1) if num else f"({chr(97+i)})" for i in range(n)]
def ex_blocks(s):
    b=[("h3", f"{s['id']}  {s['t']}")]
    ins=s['ins']
    if s.get('body'): ins=ins+"<br><br>"+s['body']
    b.append(("p", ins))
    if s['mode']=="ol":
        b.append(("ol",[it[0] for it in s['items']]))
    else:
        lab=labels(len(s['items']),s.get('num'))
        b.append(("table",["No.",s.get('head','Item')],[[lab[i],it[0]] for i,it in enumerate(s['items'])]))
    return b
def key_blocks(s):
    b=[("h3", f"{s['id']}  {s['t']}")]
    def a(it): return it[1]+(f" — *{it[2]}*" if len(it)>2 else "")
    if s['mode']=="ol":
        b.append(("ol",[a(it) for it in s['items']]))
    else:
        lab=labels(len(s['items']),s.get('num'))
        b.append(("table",["No.","Answer"],[[lab[i],a(it)] for i,it in enumerate(s['items'])]))
    return b
def count(sets): return sum(len(s['items']) for s in sets)

def G(sid,title,body,rows,ins="Fill in each blank with the most appropriate option."):
    items=[]
    for opts,idx in rows:
        o=opts.split("|")
        items.append(("   ".join(f"({i+1}) {w}" for i,w in enumerate(o)), f"({idx}) {o[idx-1]}"))
    return T(sid,title,ins,items,body=body,head="Options")
def E(sid,title,lines,fixes,ins="Each line of the passage has ONE error. Write the incorrect word and its correction."):
    items=[(ln,f"{w} → {r}") for ln,(w,r) in zip(lines,fixes)]
    return T(sid,title,ins,items,head="Line of passage")
def O(sid,title,lines,fixes,ins="In each line below ONE word has been omitted. Write the missing word. (Mark the place with a slash / in your copy.)"):
    items=[(ln,f"{w}",full) for ln,(w,full) in zip(lines,fixes)]
    return T(sid,title,ins,items,head="Line of passage")
