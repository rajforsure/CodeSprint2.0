nums = list(map(int, input("Enter book codes (space-separated): ")split()))
seen, dup = set(), 0

for n in nums:
    if n in seen: dup = n
    seen.add(n)

n = len(nums)
miss = n * (n + 1) // 2 - (sum(nums) - dup)

print([dup, miss])