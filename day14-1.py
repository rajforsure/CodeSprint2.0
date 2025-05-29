class N:
    def __init__(s,v):s.v=v;s.n=None
def f(h):
    s=fst=h
    while fst and fst.n:s=s.n;fst=fst.n.n
    r=[]
    while s:r+=[s.v];s=s.n
    return r
a=list(map(int,input().split()))
d=c=N(0)
for v in a:c.n=N(v);c=c.n
print(f(d.n))