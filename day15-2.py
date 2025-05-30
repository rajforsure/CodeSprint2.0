class N:
    def __init__(s,v): s.v=v; s.p=s.n=None

a = input("Enter DLL (e.g. 1 <-> 2 <-> 3): ").split('<->')
a = [int(x.strip()) for x in a]
t = int(input("Target: "))

h = p = N(a[0])
for v in a[1:]:
    p.n = N(v)
    p.n.p = p
    p = p.n

cur = h
while cur:
    if cur.v == t:
        if cur.p: cur.p.n = cur.n
        else: h = cur.n
        if cur.n: cur.n.p = cur.p
    cur = cur.n

while h: print(h.v, end=' <-> ' if h.n else '\n'); h = h.n
