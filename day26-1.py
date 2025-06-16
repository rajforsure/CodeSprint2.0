_ = int(input())
arr = list(map(int, input().split()))
target = int(input())

arr.sort()
res, min_diff = 0, float('inf')

for i in range(len(arr) - 2):
    l, r = i + 1, len(arr)- 1
    while l < r:
        total = arr[i] + arr[l] + arr[r]
        diff = abs(total - target)
        if diff < min_diff or (diff == min_diff and total > res):
            res, min_diff = total, diff
        if total < target:
            l += 1
        else:
            r -= 1

print(res)