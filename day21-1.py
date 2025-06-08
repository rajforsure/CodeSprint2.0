tickets = list(map(int, input("Enter ticket list: ").split()))
k = int(input("Enter position k: "))

print(sum(min(t, tickets[k] - (i > k)) for i, t in enumerate(tickets)))