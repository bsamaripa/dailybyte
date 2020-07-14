import unittest
from typing import List

"""
    This question is asked by Google. Given an array of integers,
    return whether or not two numbers sum to a given target, k.
    
    Note: you may not sum a number with itself. 

"""
class TestTwoSum(unittest.TestCase):
  def two_sum(self, input: List[str], k: int) -> bool:
    if len(input) is 0: return False
    return False

  def test_two_sum(self):
    self.assertEqual(self.two_sum([], 0), False)
    self.assertEqual(self.two_sum([1, 3, 8, 2], 10), True)
    self.assertEqual(self.two_sum([3, 9, 13, 7], 8), False)
    self.assertEqual(self.two_sum([4, 2, 6, 5, 2], 4), True)


if __name__ == '__main__':
  unittest.main()