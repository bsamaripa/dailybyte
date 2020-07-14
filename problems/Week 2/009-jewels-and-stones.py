import unittest

"""
    This question is asked by Amazon. Given a string representing your stones
    and another string representing a list of jewels, return the number of
    stones that you have that are also jewels. 

"""
class TestJewelsAndStones(unittest.TestCase):
  def jewels_and_stones(self, jewels: str, stones: str) -> int:
    if len(jewels) is 0 or len(stones) is 0: return 0
    return 0

  def test_jewels_and_stones(self):
    self.assertEqual(self.jewels_and_stones('', ''), 0)
    self.assertEqual(self.jewels_and_stones('abc', 'ac'), 2)
    self.assertEqual(self.jewels_and_stones('AaaddfFf', 'Af'), 3)
    self.assertEqual(self.jewels_and_stones('AYOPD', 'ayopd'), 0)

if __name__ == '__main__':
  unittest.main()