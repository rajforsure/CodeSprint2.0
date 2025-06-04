n = int(input())
a = list(map(int, input().split()))
res = [-1]*n
for i in range(n):
    for j in range(i+1, n):
        if a[j] > a[i]:
            for k in range(j+1, n):
                if a[k] < a[j]:
                    res[i] = a[k]
                    break
            break
print(*res)