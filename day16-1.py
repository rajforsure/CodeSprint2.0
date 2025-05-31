class ListNode:
    def __init__(self, val, next=None): self.val, self.next = val, next

def to_linked_list(arr):
    dummy = curr = ListNode(0)
    for v in arr:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def to_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    return res

def merge(l1, l2):
    dummy = curr = ListNode(0)
    while l1 and l2:
        if l1.val < l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next
    curr.next = l1 or l2
    return dummy.next

l1 = to_linked_list(list(map(int, input().split())))
l2 = to_linked_list(list(map(int, input().split())))
print(*to_list(merge(l1, l2)))
