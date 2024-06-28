# largest_number.py
def largest_number(number_list):
    """
    Function to find the largest number in a list using recursion.
    """
    # Base case: if the list has a single element, return that element
    if len(number_list) == 1:
        return number_list[0]
    else:
        # Recursive case: compare first element with largest integer
        return max(number_list[0], largest_number(number_list[1:]))

# Test case
if __name__ == "__main__":
    print(largest_number([1, 5, 2, 6, 10, 51, 16]))

# test_largest_number.py
import unittest
from largest_number import largest_number

class TestLargestNumber(unittest.TestCase):

    def test_multiple_elements(self):
        self.assertEqual(largest_number([1, 5, 2, 6, 10, 51, 16]), 51)

    def test_single_element(self):
        self.assertEqual(largest_number([42]), 42)

    def test_negative_numbers(self):
        self.assertEqual(largest_number([-10, -5, -30, -1]), -1)

    def test_mixed_numbers(self):
        self.assertEqual(largest_number([-10, 0, 5, -30, 20]), 20)

    def test_all_same_elements(self):
        self.assertEqual(largest_number([3, 3, 3, 3, 3]), 3)

if __name__ == '__main__':
    unittest.main()