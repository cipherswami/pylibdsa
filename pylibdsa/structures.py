class Array:
    "Array is contiguous collection of homogenous data elements"
    def __init__(self):
        self.myArray = []

    def addItems(self, items):
        "Add items to the array"
        self.myArray.extend(items)

    def sizeOfArray(self) -> (int):
        "Return the size of the array"
        return len(self.myArray)

    def traverse(self):
        "Traverse the array"
        print("# My Array:", end=" ")
        for item in self.myArray:
            print(item, end=" ")
        print("")

    def insertItem(self, item, position):
        "Insert an item at a given position"
        self.myArray.insert(position-1, item)
        print(f"# '{item}' is inserted at location {position}.")
