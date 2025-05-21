n = int(input())
count = 0

for i in range(n):
  row = []
  for j in range(n):
    if (i + j) % 2 == 0:
        row.append("1")
        count += 1
    else:
        row.append("0")
  print(" ".join(row))

print(f"Total students seated: {count}")