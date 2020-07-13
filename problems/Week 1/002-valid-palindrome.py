import unittest

"""
    This question is asked by Facebook. Given a string, return whether or not it forms a palindrome
    ignoring case and non-alphabetical characters.
    
    Note: a palindrome is a sequence of characters that reads the same forwards and backwards. 
"""

from string import ascii_letters

class TestValidPalindrome(unittest.TestCase):
  def valid_palindrome(self, input: str) -> bool:
    if len(input) is 0: return False
    filtered = "".join([ch for ch in input.upper() if ch in ascii_letters])
    return filtered == filtered[::-1]

  def test_valid_palindrome(self):
    self.assertEqual(self.valid_palindrome(''), False)
    self.assertEqual(self.valid_palindrome('FOOF'), True)
    self.assertEqual(self.valid_palindrome('FOO'), False)
    self.assertEqual(self.valid_palindrome('level'), True)
    self.assertEqual(self.valid_palindrome('algorithm'), False)
    self.assertEqual(self.valid_palindrome('A man, a plan, a canal: Panama.'), True)

if __name__ == '__main__':
  unittest.main()