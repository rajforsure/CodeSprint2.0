from collections import Counter

logStream = input("logstream ="). strip()
pattern = input("pattern = ").strip()

n, k = len(logStream), len(pattern)
pattern_count = Counter(pattern)
window_count = Counter(logStream[:k])
result =[]

if window_count == pattern_count:
  result.append(0)

for i in range(k, n):
  window_count[logStream[i]] += 1
  window_count[logStream[i - k]] -= 1
  if window_count[logStream[i - k]] == 0:
     del window_count[logStream[i - k]]
  if window_count == pattern_count:
    result.append(i - k + 1)

print(result)