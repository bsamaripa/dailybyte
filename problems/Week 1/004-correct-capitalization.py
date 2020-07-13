import unittest

"""
    This question is asked by Google. Given a string, return whether or not it
    uses capitalization correctly. A string correctly uses capitalization if
    all letters are capitalized, no letters are capitalized, or only the first
    letter is capitalized.
"""
class TestCorrectCapitalization(unittest.TestCase):
  def correct_capitalization(self, input: str) -> bool:
    if len(input) is 0: return False
    return False

  def test_correct_capitalization(self):
    self.assertEqual(self.correct_capitalization(''), False)
    self.assertEqual(self.correct_capitalization('USA'), True)
    self.assertEqual(self.correct_capitalization('Calvin'), True)
    self.assertEqual(self.correct_capitalization('compUter'), False)
    self.assertEqual(self.correct_capitalization('coding'), True)


if __name__ == '__main__':
  unittest.main()