import unittest
from typing import List

"""
    This question is asked by Google. Given two integer arrays, return their intersection.

    Note: the intersection is the set of elements that are common to both arrays. 
"""
class TestIntersectionOfNumbers(unittest.TestCase):
  def intersection_of_numbers(self, s: List[int], t: List[int]) -> List[int]:
    if len(s) is 0 or len(t) is 0: return []
    return []

  def test_intersection_of_numbers(self):
    self.assertEqual(self.intersection_of_numbers([], []), [])
    self.assertEqual(self.intersection_of_numbers([2, 4, 4, 2], [2, 4]), [2, 4])
    self.assertEqual(self.intersection_of_numbers([1, 2, 3, 3], [3, 3]), [3])
    self.assertEqual(self.intersection_of_numbers([2, 4, 6, 8], [1, 3, 5, 7]), [])

if __name__ == '__main__':
  unittest.main()