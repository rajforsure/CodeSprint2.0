n = int(input())
scores = list(map(int, input().split()))

def archeryShots(scores):
  good = 0
  missed = 0
  for score in scores:
    if score >= 7:
      good += 1
    else:
      missed += 1
      return good, missed

g, m = archeryShots(scores)
print(g, m)
