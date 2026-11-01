import math, itertools
from fractions import Fraction as F
from math import gcd, sqrt, isclose, pi, tan, radians, sin, cos
def sec1():
    assert gcd(65,117)==13 and 65*2-117==13
    assert 4+6-10==0
    assert 24==2**3*3 and isclose(sqrt(24),2*sqrt(6))
    assert 6**2-4*2*3>0 and 4**2-16==0
    assert 254-9*5==209
    assert sum(3*n+5 for n in range(1,11))==215
    x=4; assert F(x,x-2)==F(x+2,x-1)
    assert F(6,1)/F(3,4)==8
    # equidistant
    x=-1; assert (x-3)**2+4==(x+5)**2+4
    t=F(3,4); assert (4*t-1)/(4*t+1)==F(1,2)  # sin/cos-> using tan: (4tan-1)/(4tan+1) with tan=3/4
    assert isclose(30*tan(radians(30)),10*sqrt(3))
    assert 4*22==88 and 88*7/44==14
    assert 3**3==27
    cum=[6,20,32,50,60]; assert 30<=cum[2] and cum[1]<30
    assert F(3,4)
    # B
    assert 13*182==26*91 and 182==2*7*13
    assert F(3,2)+F(-1,3)==F(7,6) and F(3,2)*F(-1,3)==F(-1,2)
    # C
    k=F(2,5); assert (10*k-4)/(k+1)==0; assert (2*12+5*(-6))/F(7)==F(-6,7)
    fx=sum(a*b for a,b in zip([15,25,35,45,55],[4,7,12,9,3])); assert fx==1225 and fx/35==35
    assert sqrt(49+576)==25 and 22/7*7*25+2*22/7*49==858
    assert 360/40-360/45==1
    # D
    P=[(1,7),(4,2),(-1,-1),(-4,4)]; d=lambda a,b:(a[0]-b[0])**2+(a[1]-b[1])**2
    assert len({d(P[0],P[1]),d(P[1],P[2]),d(P[2],P[3]),d(P[3],P[0])})==1 and d(P[0],P[2])==d(P[1],P[3])==68
    assert 20+(25-13)/15*10==28
    assert 196-154==42 and 4*(1/4*2*22/7*7)==44
    # E
    assert 3*18+2*8==70 and 2*18+5*8==76 and 5*18+3*8==114
    h=30*sqrt(3); assert isclose(h*sqrt(3)-h/sqrt(3),60) and isclose(h/sqrt(3),30) and isclose(h*sqrt(3),90)
    assert 150+11*25==425 and 150+18*25==600 and 6*(300+275)==3450
sec1()
print('set1 verified')
