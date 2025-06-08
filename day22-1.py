n = int(input())
heights = list(map(int, input().split()))
l, r = 0, n - 1
lm = rm = eater = 0
while l < r:
    if heights[1] < heights[r]:
        lm = max(lm, heights[l])
        water += lm - heights[l]
        l += 1
    else:
        rm = max(rm, heights[r])
        water += rm - heights[r]
        r -= 1
print(water)