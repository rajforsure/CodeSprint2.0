score = list(map(int, input("Enter robot scores (space-separated): ").split()))

medals = ["Gold Medal", "Silver Medal", "Bronze Medal"]
rank = {v: medals[i] if i < 3 else str(i + 1) for i, v in enumerate(sorted(score, reverse=True))}

print([rank(s) for s in score])