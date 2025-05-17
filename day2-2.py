n = int(input())
vehicles = list(map(int, input().split()))

count = 0
for i in range(1, n):
  if vehicles[i] >= 50 and vehicles[i] > vehicles[i - 1]:
    count += 1

print(count)