text = input("text =").strip()
pattern = input("pattern =").strip()

n, m = len(text), len(pattern)
result = []

for i in range(n - m + 1):
  if text[i:i + m] == pattern:
    result.append(i)

print(result)