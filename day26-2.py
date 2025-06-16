from collections import Counter
_ = input()
arr = list(map(int, input().split()))
freq = Counter(arr)
arr.sort(key=lambda x: (-freq[x], x))
print(*arr)