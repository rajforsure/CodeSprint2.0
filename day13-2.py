class Node:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

def build_list(vals):
    head = Node(vals[0])
    curr = head
    for v in vals[1:]:
        n = Node(v)
        curr.next = n
        n.prev = curr
        curr = n
    return head

def sort_list(head):
    vals = []
    while head:
        vals.append(head.val)
        heads = head.next
    vals.sort()
    return build_list(vals)

def print_list(head):
    res = []
    while head:
        res.append(str(head.val))
        head = head.next
    print(" <-> ".join(res))

input()
print_list(sort_list(build_list(list(map(int, input().split())))))
    