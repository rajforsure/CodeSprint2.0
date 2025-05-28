class ListNode:
  def __init__(self, val=0, next=None):
      self.val = val
      self.next = next

def splitListToParts(head, k):
    total = 0
    curr = head
    while curr:
        total += 1
        curr = curr.next

    part_size = total // k
    extra = total % k

    result = []
    curr = head
    for i in range(k):
        part_head = curr
        size = part_size + (1 if i < extra else 0)
        for j in range(size - 1):
            if curr:
                curr = curr.next
        if curr:
            next_part = curr.next
            curr.next = None
            curr = next_part
        result.append(part_head)
    return result

def build_linked_list(values):
      dummy = ListNode(0)
      curr = dummy
      for v in values:
          curr.next = ListNode(v)
          curr = curr.next
      return dummy.next

def print_parts(parts):
    for part in parts:
        vals = []
        while part:
            vals.append(part.val)
            part = part.next
        print(vals, end=' , ')

values = list(map(int, input().split()))
k = int(input())

head = build_linked_list(values)
parts = splitListToParts(head, k)
print_parts(parts)