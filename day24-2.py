def reverse_queue():
    n = int(input())
    q = list(map(int, input().split()))
    print(*q[::-1])

reverse_queue()