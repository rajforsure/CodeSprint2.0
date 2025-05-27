class Node:
  def __init__(self, data):
      self.data = data
      self.next = None

def sortPackages(head):
    count = [0, 0, 0]
    curr = head
    while curr:
      count[curr.data] += 1
      curr = curr.next
    curr = head
    for i in range(3):
        while count[i]:
            curr.data = i
            curr = curr.next
            count[i] -= 1
    return head

def createLinkedList(arr):
    head = Node(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = Node(val)
        curr = curr.next
    return head

def printList(head):
    while head:
        print(head.data, end=" -> " if head.next else "")
        head = head.next
    print()

arr = list(map(int, input("Enter package colors (0/1/2) separated by space: ").split()))
head = createLinkedList(arr)

sorted_head = sortPackages(head)
print("Sorted packages:")
printList(sorted_head)