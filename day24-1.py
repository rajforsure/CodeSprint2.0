from collections import deque, Counter

def first_unique_char_stream(s):
    q = deque()
    count = Counter()
    res = []

    for ch in s:
        count[ch] += 1
        q.append(ch)
        while q and count[q[0]] > 1:
            q.popleft()
        res.append(q[0] if q else '#')

    return ''.join(res)

print(first_unique_char_stream(input()))