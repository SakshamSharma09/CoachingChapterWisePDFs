import sys, importlib, random
sys.path.insert(0,'.')
m=importlib.import_module(sys.argv[1])
bad=0
def chk(s,where):
    global bad
    if s.count('$')%2: print("ODD $",where,s[:200]); bad+=1
    if '{{' in s or '}}}' in s and False: pass
for t,d in m.TIERS.items():
    for k,v in d.items():
        items=[x for g in v for x in g] if v and isinstance(v[0],list) else v
        print(t,k,len(items))
        for x in items:
            if isinstance(x,dict) and 'opts' in x:
                chk(x['q'],(t,k)); [chk(o,(t,k,'opt')) for o in x['opts']]
                chk(x.get('why',''),(t,k,'why'))
            else:
                chk(x['q'],(t,k)); chk(x['ans'],(t,k,'ans'))
if len(sys.argv)>2:
    random.seed(int(sys.argv[2]))
    for t,d in m.TIERS.items():
        for k,v in d.items():
            items=[x for g in v for x in g]
            for x in random.sample(items,int(sys.argv[3]) if len(sys.argv)>3 else 2):
                print('--',t,k); print(x['q']); print('   ', x.get('opts') or '', x.get('ans') if x['kind']=='q' else x['ans']+' '+x['why'])
print("odd$:",bad)
