import unittest

"""
    This question is asked by Facebook. Given two strings s and t return
    whether or not s is an anagram of t.

    Note: An anagram is a word formed by reordering the letters of another word. 
"""
class TestValidAnagram(unittest.TestCase):
  def valid_anagram(self, s: str, t: str) -> bool:
    if len(s) is 0 or len(t) is 0: return False 
    return False

  def test_valid_anagram(self):
    self.assertEqual(self.valid_anagram('', ''), False)
    self.assertEqual(self.valid_anagram('cat', 'tac'), True)
    self.assertEqual(self.valid_anagram('listen', 'silent'), True)
    self.assertEqual(self.valid_anagram('program', 'function'), False)

if __name__ == '__main__':
  unittest.main()