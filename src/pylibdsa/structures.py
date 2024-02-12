##############################################################
# File Name     : pylibdsa/structures.py
# Author        : Aravind Potluri <aravindswami135@gmail.com>
# Description   : This file conatains implementation of data
#                 structures in python.
##############################################################

# Dependencies ->
import numpy as np

# Arrays ->
class Array:  # TBD: Implement our own methods instead of list built-in methods
    "Contiguous collection of homogenous data elements"
    def __init__(self, array=None):
        if array is None:
            array = []
        self.array = array

    def traverse(self):
        "Traverse the array"
        print("[#] Array: ", end=" ")
        if len(self.array) == 0:
            print("None")
            return
        for element in self.array:
            print(element, end=" ")
        print("")

    def append(self, element):
        "Add elements to the array"
        self.array.append(element)

    def length(self) -> (int):
        "Return the size of the array"
        return len(self.array)

    def insert(self, element, index):
        "Insert an element at a given index"
        self.array.insert(index, element)

    def delete(self, index):
        "Delete an element at a given index"
        self.array.pop(index)

    def access(self, index):
        "Access an element at a given index"
        return self.array[index]
    
    def search(self, element) -> bool:
        "Search for an element in the array"
        return element in self.array
    
    def pop(self):
        "Remove the last element from the array"
        self.array.pop()

# Linked Lists ->
class Node:
    "A node is a basic unit of a data structure"
    def __init__(self, data):
        self.data = data
        self.next = None

class Node(Node):
    "A node is a basic unit of a data structure"
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None


class SingleLinkedList:
    "Linear data structure that consists of a set of sequentially linked nodes"
    def __init__(self, head: Node=None):
        self.head = head

    def traverse(self):
        "Print the linked list"
        node = self.head
        if node is None:
            print("[#] Linked List: None")
            return
        print(f"[#] Linked List: {node.data}", end="")
        while node.next is not None:
            node = node.next
            print(f" -> {node.data}", end="")
        print("")

    def append(self, data):
        "Add node at the end of the linked list"
        node = self.head
        if node is None:
            self.head = Node(data)
            return
        while node.next is not None:
            node = node.next
        node.next = Node(data)

    def insert(self, data, index: int):
        "Insert node at a given index"
        if index == 0:
            node = Node(data)
            node.next = self.head
            self.head = node
        else:
            node = self.head
            for i in range(index-1):
                if node.next is not None:
                    node = node.next
                else:
                    print(f"[!] Bound Exceeded")
                    return
            tempNode = Node(data)
            tempNode.next = node.next
            node.next = tempNode
    
    def delete(self, index: int):
        "Delete a node at a given index"
        if index == 0:
            self.head = self.head.next # TBD: Implement manual grabage deletion
        else:
            node = self.head
            for i in range(index-1):
                if node.next is not None:
                    node = node.next
                else:
                    print(f"[!] Bound Exceeded")
                    return
            if node.next is not None:
                node.next = node.next.next
            else:
                print(f"[!] Bound Exceeded")
                return

    def length(self) -> (int):
        "Return the size of linked list"
        size = 0
        node = self.head
        while node is not None:
            size += 1
            node = node.next
        return size
    
    def access(self, index: int):
        "Access a node at a given index"
        node = self.head
        for i in range(index):
            if node is not None:
                node = node.next
            else:
                print(f"[!] Linked List Bound Exceeded")
                return
        return node.data
    
    def search(self, data) -> bool:
        "Search for a node with a given data"
        node = self.head
        while node is not None:
            if node.data == data:
                return True
            node = node.next
        return False
    
    def pop(self):
        "Delete the last node"
        node = self.head
        if node.next is None:
            self.head = None
            return
        while node.next.next is not None:
            node = node.next
        node.next = None

# Stacks ->
class Stack():
    "Linear data structure that follows LIFO (Last In First Out)"
    def __init__(self, type: Array | SingleLinkedList, head=None):
        self.type = type
        self.stack = None
        print(type(head))
        if self.type == Array:
            self.stack = Array(head)
        else:
            self.stack = SingleLinkedList(head)

    def traverse(self):
        "Print the stack"
        if self.type == SingleLinkedList:
            self.stack.traverse()
        else:
            self.stack.traverse()
    
    def push(self, data):
        "Add data to the stack"
        if self.type == SingleLinkedList:
            self.stack.append(data)
        else:
            self.stack.append(data)

    def pop(self):
        "Remove data from the stack"
        if self.type == SingleLinkedList:
            self.stack.pop()
        else:
            self.stack.delete(self.stack.length()-1)
    
    
    