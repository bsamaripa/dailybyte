import unittest
from typing import List

"""
    This question is asked by Microsoft. Given an array of strings, return the
    longest common prefix that is shared amongst all strings.

    Note: you may assume all strings only contain lowercase alphabetical characters. 
"""
class TestLongestCommonPrefix(unittest.TestCase):
  def longest_common_prefix(self, input: List[str]) -> str:
    if len(input) is 0: return ''
    return ''

  def test_longest_common_prefix(self):
    self.assertEqual(self.longest_common_prefix([]), '')
    self.assertEqual(self.longest_common_prefix(['colorado', 'color', 'cold'],), 'col')
    self.assertEqual(self.longest_common_prefix(['a', 'b', 'c']), '')
    self.assertEqual(self.longest_common_prefix(['spot', 'potty', 'spotted']), 'spot')


if __name__ == '__main__':
  unittest.main()