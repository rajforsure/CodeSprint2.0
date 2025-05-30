class ListNode:
    def __init__(self, val=0, nxt=None): self.val, self.next = val, nxt

def add(a, b):
    c = dummy = ListNode(); carry = 0
    while a or b or carry:
        carry += (a.val if a else 0) + (b.val if b else 0)
        c.next = ListNode(carry % 10)
        c, carry = c.next, carry // 10
        a = a.next if a else None
        b = b.next if b else None
    return dummy.next

def to_ll(nums):
    head = cur = ListNode(nums[0])
    for n in nums[1:]:
        cur.next = ListNode(n)
        cur = cur.next
    return head

def to_list(node):
    res = []
    while node: res.append(node.val); node = node.next
    return res

l1 = to_ll(list(map(int, input("L1: ").split())))
l2 = to_ll(list(map(int, input("L2: ").split())))
print("Result:", to_list(add(l1, l2)))
