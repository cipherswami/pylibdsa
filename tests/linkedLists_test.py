from pylibdsa.structures import SingleLinkedList, Node

emptyList = SingleLinkedList()
emptyList.traverse()
emptyList.append(9)
emptyList.append(8)
emptyList.append(7)
emptyList.traverse()

intialList = Node(-2)
intialList.next = Node(-1)
myList = SingleLinkedList(intialList)
myList.append(1)
myList.append(2)
myList.append(3)
myList.traverse()

myList.insert(-3, 0)
myList.traverse()

myList.insert(0, 3)
myList.traverse()

myList.insert(4, 7)
myList.traverse()

myList.insert(999, 9)
myList.traverse()

myList.delete(0)
myList.traverse()

myList.delete(2)
myList.traverse()

myList.delete(5)
myList.traverse()

myList.delete(5)
myList.traverse()

myList.pop()
myList.traverse()

print("[#] Length: ", myList.length())

print("[#] Accessing index 0: ", myList.access(0))

print("[#] Accessing index 2: ", myList.access(2))

print("[#] Accessing last node: ", myList.access(myList.length() - 1))

print("[#] Searching for '-1': ", myList.search(-1))

print("[#] Searching for '69': ", myList.search(69))

print("[#] Searching for Starting node: ", myList.search(-2))

print("[#] Searching for Ending node: ", myList.search(2))

myList.traverse()
myList.pop()
myList.pop()
myList.pop()
myList.traverse()

myList.pop()
myList.traverse()

myList.append(69)
myList.traverse()

myList.delete(0)
myList.traverse()


