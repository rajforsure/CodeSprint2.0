n = int(input())
a = sorted(map(int, input().split()))
t = int(input())
for i in range(n):
    l , r = i + 1, n - 1
    while l < r:
        s = a[i] + a[l] + a[r]
        if s == t: print("true"); exit()
        l += s < t
        r -= s > t
print("false")