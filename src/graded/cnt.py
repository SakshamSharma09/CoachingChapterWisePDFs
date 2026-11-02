import sys
import sci
def T(A,B,C,D):
    print(sum(len(g) for g in A),len(B),len(C),len(D)); return {}
sci.T=T
exec(compile(open(sys.argv[1]+'.py',encoding='utf-8').read(),'x','exec'),{})
