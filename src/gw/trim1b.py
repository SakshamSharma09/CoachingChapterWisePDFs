import sys,importlib,re,json,pprint
sys.path.insert(0,'/home/claude/rnlib'); sys.path.insert(0,'/home/claude/gw/part1_v1')
def wc(x): return len(re.findall(r'\w+',json.dumps(x,ensure_ascii=False)))
def tbl_drop(ch,bi,rows):
    b=ch['blocks'][bi]; assert b[0]=='table'
    ch['blocks'][bi]=(b[0],b[1],[r for k,r in enumerate(b[2]) if k not in rows])
def tbl_keep(ch,bi,n):
    b=ch['blocks'][bi]; ch['blocks'][bi]=(b[0],b[1],b[2][:n])
def build(i,drops,tbl=(),keep=(),repl={},mod=None):
    ch=importlib.import_module(f"g{i:02d}").CH
    ch=json.loads(json.dumps(ch)); ch['blocks']=[tuple(b) if not isinstance(b,tuple) else b for b in ch['blocks']]
    ch['blocks']=[ (b[0],b[1],[list(r) for r in b[2]]) if b[0]=='table' else tuple(b) for b in ch['blocks']]
    before=wc(ch)
    for bi,rows in tbl: tbl_drop(ch,bi,set(rows))
    for bi,n in keep: tbl_keep(ch,bi,n)
    for bi,nb in repl.items(): ch['blocks'][bi]=nb
    if mod: mod(ch)
    dset=set(drops)
    ch['blocks']=[b for k,b in enumerate(ch['blocks']) if k not in dset]
    # drop heading with no content following
    out=[]
    bl=ch['blocks']
    for k,b in enumerate(bl):
        if b[0]=='h2' and (k+1==len(bl) or bl[k+1][0]=='h2'): continue
        out.append(b)
    ch['blocks']=out
    after=wc(ch)
    src="CH = "+pprint.pformat(ch,width=140,sort_dicts=False)+"\n"
    open(f"/home/claude/gw/part1/g{i:02d}.py","w").write(src)
    print(i,before,'->',after,f"{100*(before-after)/before:.0f}%")

# g11
build(11,[13,14,20,29,39,40,41,44,45],keep=[(43,6)])
# g12
def m12(ch):
    b=ch['blocks'][25]
    ch['blocks'][25]=(b[0],b[1],[[r[0],', '.join(r[1].split(', ')[:10])] for r in b[2]])
build(12,[31,32,33,40,41],tbl=[(27,[2,6,7,13,17,24,29,33,35]),(29,[11,12,13,14]),(39,[5,8,11,12])],mod=m12)
# g13
build(13,[28,31,32],tbl=[(15,[5,6,7,8])])
# g14
build(14,[23,28,29],tbl=[(27,[5,6])])
# g15
inv=("note","NOTE","In formal writing *if* can be dropped by inverting *had / were / should*: *Had I known, I would have come.* (Part 2 deals with this in detail.)")
build(15,[31,32,35,36,39,40],repl={30:inv},tbl=[(23,[5,6]),(38,[6,8])])
# g16
build(16,[29,30,33,34,35,36,42,43])
# g17
build(17,[7,15,19,26,41,42],tbl=[(31,[1,4]),(40,[8])])
# g18
build(18,[22,23,24,25,26,27,28,46,47])
# g19
build(19,[24,38,39],tbl=[(8,[7,10,12,14,23,25,26,27,32]),(11,[16,17,19,21,22,25,26,27]),(16,[1,3,9,11,14,21,22,28]),(27,[7,9,13,21,22])])
