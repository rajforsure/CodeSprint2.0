n = int(input())

if n > 10:
    print("Abhik's marathon journey intensifies! Let's see his detailed zig-zag pattern:")

max_width = (n * 4) - 3
total_numbers = 0

for i in range(1, n + 1):
  if i % 2 == 1:
    row = list(range(1, i + 1))
  else:
    row = list(range(i, 0, -1))

  row_str = ' '.join(str(num) for num in row)
  print(row_str.center(max_width))
  total_numbers += len(row)

print(f"Total numbers printed: {total_numbers}")