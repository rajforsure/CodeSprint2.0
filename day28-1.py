from collections import Counter
from heapq import heapify, heappop, heappush

s = input("Banner text: ")
freq = Counter(s)
heap = [(-c, ch) for ch, c in freq.items()]
heapify(heap)

res, prev = [], (0, '')
while heap:
    c, ch = heappop(heap)
    res.append(ch)
    if prev[0] < 0: heappush(heap, prev)
    prev = (c + 1, ch)

print('Rearranged:' if len(res) == len(s) else 'Not Possible:', ''.join(res) if len(res)==len(s) else '')