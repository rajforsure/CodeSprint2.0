n = int(input())
stack, freq = [], {}

for _ in range(n):
    cmd = input().split()
    if cmd(0) == "PUSH":
        x = cmd[1]
        stack.append(x)
        freq[x] = freq.get(x, 0) + 1
    elif cmd[0] == "POP" and stack:
        x = stack.pop()
        freq[x] == 0
        if freq[x] == 0:
            del freq[x]
    elif cmd[0] == "COUNT":
        print(freq[stack[-1]] if stack else "EMPTY")