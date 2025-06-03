n = int(input())
s, m = [], []
for _ in range(n):
    a = input().split()
    if a[0] == 'PUSH':
        x = int(a[1])
        s.append(x)
        m.append(x if not m else min(x, m[-1]))
    elif a[0] == 'POP' and s:
        s.pop()
        m.pop()
    elif a[0] == 'MIN':
        print(m[-1] if m else 'EMPTY')