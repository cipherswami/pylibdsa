import unittest
from pylibdsa.structures import Array

class ArrayTest(unittest.TestCase):
    def setUp(self):
        self.test_array = Array()

    def test_addItems(self):
        items = [9, 2, 2004]
        self.test_array.addItems(items)
        self.test_array.traverse()
        self.assertEqual(self.test_array.myArray[-len(items):], items)

    def test_traverse(self):
        self.test_array.traverse()
        # self.assertEqual(self.test_Array.traverse(), "# My Array: 9 2 2004")

if __name__ == '__main__':
    unittest.main()