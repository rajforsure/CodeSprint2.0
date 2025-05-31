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

def reverse_between(head, left, right):
    dummy = ListNode(0, head)
    prev = dummy
    for _ in range(left - 1): prev = prev.next
    curr = prev.next
    for _ in range(right - left):
        temp = curr.next
        curr.next = temp.next
        temp.next = prev.next
        prev.next = temp
    return dummy.next

arr = input("List: ").split()
l, r = int(input("Left: ")), int(input("Right: "))
head = to_linked_list(arr)
print("Reversed:", to_list(reverse_between(head, l, r)))
