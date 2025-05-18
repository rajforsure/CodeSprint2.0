r, c = map(int, input().split())
stock = [list(map(int, input().split())) for _ in range(r)]

count = 0 
for row in stock:
  high_stock = sum(1 for item in row if item >= 100)
  if high_stock >= 3:
    count += 1

print(count)