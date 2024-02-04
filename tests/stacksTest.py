from pylibdsa.structures import *

emptyStack = Stack(Array)
emptyStack.traverse()

emptyStack = Stack(SingleLinkedList)
emptyStack.traverse()

myList = Node(1)
myList.next = Node(2)
myList.next.next = Node(3)
myList.next.next.next = Node(4)
myList.next.next.next.next = Node(5)

print(type(myList))

# myStack = Stack(SingleLinkedList, myList)
# myStack.traverse()