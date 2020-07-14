import unittest
from typing import List

"""
    This question is asked by Amazon. Given two strings representing sentences,
    return the words that are not common to both strings (i.e. the words that
    only appear in one of the sentences). You may assume that each sentence is
    a sequence of words (without punctuation) correctly separated using space 
    characters.  
"""
class TestUncommonWords(unittest.TestCase):
  def uncommon_words(self, s: str, t: str) -> List[str]:
    if len(s) is 0 or len(t) is 0: return []
    return []

  def test_uncommon_words(self):
    self.assertEqual(self.uncommon_words('', ''), [])
    self.assertEqual(self.uncommon_words('the quick', 'brown fox'), ['the', 'quick', 'brown', 'fox'])
    self.assertEqual(self.uncommon_words('the tortoise beat the haire', 'the tortoise lost to the haire'), ['beat', 'to', 'lost'])
    self.assertEqual(self.uncommon_words('copper coffee pot', 'hot coffee pot'), ['copper', 'hot'])

if __name__ == '__main__':
  unittest.main()