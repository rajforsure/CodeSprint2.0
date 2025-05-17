n = int(input())
scores = list(map(int, input().split()))

magical_days = 0

for i in range(1, n - 1):
  if scores[i] > scores[i - 1] and scores[i] > scores[i + 1]:
    magical_days += 1


print(magical_days)