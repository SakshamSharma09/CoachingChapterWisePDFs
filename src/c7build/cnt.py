import sys
for m in sys.argv[1:]:
    src=open(m.replace('.','/')+'.py').read().replace("SETS, POOL = build(A, B, C, D)","")
    ns={}
    try: exec(src,ns)
    except Exception as e: print(m,'ERR',e); continue
    print(m,len(ns['A']),len(ns['B']),len(ns['C']),len(ns['D']))
