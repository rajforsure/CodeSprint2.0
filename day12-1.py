class ListNode:
  def __init__(self, val=0):
     self.val = val
     self.next = None

def sort_by_actual_temperature(head):
  dummy = ListNode(0)
  dummy.next = head
  prev, curr = head, head.next

  while curr:
      if curr.val < prev.val:
          prev.next = curr.next
          pos = dummy
          while pos.next.val < curr.val:
              pos = pos.next
          curr.next = pos.next
          pos.next = curr
          curr = prev.next
      else:
          prev, curr = curr, curr

  return dummy.next

def build_linked_list(value):
    dummy = ListNode(0)
    curr = dummy
    for val in value:
        curr.next = ListNode(val)
        curr = curr.next
    return dummy.next

def print_linked_list(head):
    print(" -> ".join(map(str, iter_list(head))))

def iter_list(node):
    while node:
        yield node.val
        node = node.next

head = build_linked_list(list(map(int, input().split())))
sorted_head = sort_by_actual_temperature(head)
print_linked_list(sorted_head)