s = input()
count = 0
i = 0

while i < len(s):
  if s[i] == '1':
    count += 1
    while i < len(s) and s[i] == '1':
      i += 1
  else:
    i += 1

print(count)