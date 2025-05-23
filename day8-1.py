target = int(input())
n = int(input())
sessions = list(map(int, input().split()))

min_len = float('inf')
left = 0
current_sum = 0

for right in range(n):
   current_sum += sessions[right]
   while current_sum >= target:
    min_len = min(min_len, right - left + 1)
    current_sum -= sessions[left]
    left += 1

print(min_len if min_len != float('inf') else 0)