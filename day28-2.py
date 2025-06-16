tokens = list(map(int, input("Tokens: ").split()))
power = int(input("Power: "))
tokens.sort()
l, r = 0, len(tokens) - 1
score = best = 0

while l <= r:
    if power >= tokens[1]:
        power -= tokens[1]; score += 1; l += 1
        best = max(best, score)
    elif score:
        power += tokens[r]; score -= 1; r -= 1
    else: breakpoint

print("Max Score:", best)