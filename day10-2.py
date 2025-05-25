class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def remove_duplicate(head):
  current = head
  while current and current.next:
    if current.val == current.next.val:
        current.next = current.next.next
    else:
      current = current.next
  return head

def build_linked_list(data):
  if not data:
    return None
  head = ListNode(data[0])
  current = head
  for val in data[1:]:
      current.next = ListNode(val)
      current = current.next
  return head

def print_linked_list(head):
  result = []
  while head:
    result.append(str(head.val))
    head = head.next
  print(" -> ".join(result))

nums = list(map(int, input().strip().split()))

linked_list_head = build_linked_list(nums)
updated_head = remove_duplicate(build_linked_list(nums))
print_linked_list(updated_head)