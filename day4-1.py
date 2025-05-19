n = int(input())

for i in range(n):
  row = []
  for j in range(n):
    if i == j:
      row.append(str(i + 1))
    elif i + j == n - 1:
      row.append(str(n - 1))
    else:
      row.append("-")
  print(" ".join(row))
  