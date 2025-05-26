class ListNode:
  def __init__(self, val=0):
    self.val = val
    self.next = None

def detect_and_remove_cycle(head):
  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
     break
  else:
    return True

slow = head
if slow == fast:
       while fast.next != slow:
           fast = fast.next
else:
      while slow.next != fast.next:
         slow = slow.next
         fast = fast.next
         
fast.next = None
return True

def build_linked_list(values, pos):
  if not values:
      return None
  nodes = [ListNode(val) for val in values]
  for i in range(len(values) - 1):
      nodes[i].next = nodes[i + 1]
  if pos > 0:
    nodes[-1].next = nodes[pos - 1]
  return nodes[0]

values = list(map(int, input().split()))
pos = int(input())
head = build_linked_list(values, pos)
print(detect_and_remove_cycle(head))