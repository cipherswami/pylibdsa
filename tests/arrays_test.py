from pylibdsa.structures import Array

emptyArray = Array()
emptyArray.traverse()
emptyArray.append(8)
emptyArray.traverse()

intialArray = [-2, -1]

myArray = Array(intialArray)
myArray.traverse()
myArray.append(1)
myArray.append(2)
myArray.append(3)
myArray.traverse()

myArray.insert(-3, 0)
myArray.traverse()

myArray.insert(0, 3)
myArray.traverse()

myArray.insert(4, 7)
myArray.traverse()

myArray.insert(999, 9)
myArray.traverse()

myArray.delete(0)
myArray.traverse()

myArray.delete(2)
myArray.traverse()

myArray.delete(5)
myArray.traverse()

myArray.delete(5)
myArray.traverse()

myArray.pop()
myArray.traverse()

print("[#] Length: ", myArray.length())

print("[#] Accessing index 0: ", myArray.access(0))

print("[#] Accessing index 2: ", myArray.access(2))

print("[#] Accessing last node: ", myArray.access(myArray.length() - 1))

print("[#] Searching for '-1': ", myArray.search(-1))

print("[#] Searching for '69': ", myArray.search(69))

print("[#] Searching for Starting node: ", myArray.search(-2))

print("[#] Searching for Ending node: ", myArray.search(2))

myArray.traverse()
myArray.pop()
myArray.pop()
myArray.pop()
myArray.traverse()