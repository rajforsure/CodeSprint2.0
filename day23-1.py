from collections import deque

nums = list(map(int, input().split()))
k = int(input())
n = len(nums)
dp = [float('-inf')] * n
dp[0] = nums[0]
dq = deque([0])

for i in range(1, n):
      while dq and dq[0] < i - k:
          dq.popleft()
      dp[i] = nums[i] + dp[dq[0]]
      while dq and dp[i] >= dp[dq[-1]]:
          dq.pop()
      dq.append(i)

print(dp[-1])