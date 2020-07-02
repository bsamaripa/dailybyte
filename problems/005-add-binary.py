import unittest

"""
    This question is asked by Apple. Given two binary strings (strings containing
    only 1s and 0s) return their sum (also as a binary string).

    Note: neither binary string will contain leading 0s unless the string itself is 0
"""
class TestAddBinary(unittest.TestCase):
  def add_binary(self, a: str, b: str) -> str:
    if len(input) is 0: return ''
    return ''

  def test_add_binary(self):
    self.assertEqual(self.add_binary('', ''), '')
    self.assertEqual(self.add_binary('100','1'), '101')
    self.assertEqual(self.add_binary('11', '1'), '100')
    self.assertEqual(self.add_binary('1', '0'), '1')


if __name__ == '__main__':
  unittest.main()