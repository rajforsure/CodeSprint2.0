from collections import deque

senate = input()
r, d = deque(), deque()
n = len(senate)

for i, c in enumerate(senate):
    if c == 'R':
        r.append(i)
    else:
        d.append(i)

while r and d:
    ri, di = r.popleft(), d.popleft()
    if ri < di:
        r.append(ri + n)
    else:
        d.append(di + n)

print("Radiant" if r else "Dire")