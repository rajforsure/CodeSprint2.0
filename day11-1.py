appointments = list(map(int, input("appointments = ").strip().split()))

zigzag = []
left, right = 0, len(appointments) - 1
turn = True

while left <= right:
  if turn:
    zigzag.append(appointments[left])
    left += 1
  else:
    zigzag.append(appointments[right])
    right -= 1
  turn = not turn

print(zigzag)