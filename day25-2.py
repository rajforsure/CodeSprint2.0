from functools import cmp_to_key
n = int(input())
a = input().split()
a.sort(key=cmp_to_key(lambda x, y: -1 if x + y > y + x else 1))
print('0' if a[0] == '0' else ''.join(a))