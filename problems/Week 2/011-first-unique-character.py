import unittest

"""
    This question is asked by Microsoft. Given a string, return the index of its
    first unique character. If a unique character does not exist, return -1.  
"""
class TestFirstUniqueCharacter(unittest.TestCase):
  def first_unique_character(self, input: str) -> int:
    if len(input) is 0: return -1
    return -1

  def test_first_unique_character(self):
    self.assertEqual(self.first_unique_character(''), -1)
    self.assertEqual(self.first_unique_character('ababab'), -1)
    self.assertEqual(self.first_unique_character('abcabd'), 2)
    self.assertEqual(self.first_unique_character('thedailybyte'), 1)
    self.assertEqual(self.first_unique_character('developer'), 0)

if __name__ == '__main__':
  unittest.main()