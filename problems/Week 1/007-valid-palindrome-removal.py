import unittest

"""
    This question is asked by Facebook. Given a string and the ability to delete
    at most one character, return whether or not it can form a palindrome.

    Note: a palindrome is a sequence of characters that reads the same
    forwards and backwards.

"""
class TestValidPalindromeRemoval(unittest.TestCase):
  def valid_palindrome(self, input: str) -> bool:
    if len(input) is 0: return False
    return False

  def test_valid_palindrome_removal(self):
    self.assertEqual(self.valid_palindrome(''), False)
    self.assertEqual(self.valid_palindrome('abcba'), False)
    self.assertEqual(self.valid_palindrome('foobof'), False)
    self.assertEqual(self.valid_palindrome('abccab'), False)


if __name__ == '__main__':
  unittest.main()