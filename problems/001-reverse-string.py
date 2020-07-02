import unittest

"""
    Welcome to your first of many daily bytes! We are starting with a strings problem and we
    strongly recommend you find the time each day to solve these problems. It is important 
    to not just solve them in your head but actually whip out your favorite editor/IDE and 
    write a function and use the test cases supplied in the question to check your work. 
   
    Getting yourself to actually write down the solutions will go a long way to ensuring you
    are thinking through all the edge cases as well as any space/time complexities.

This question is asked by Google. Given a string, reverse all of its characters and return the resulting string.
"""

class TestReverseString(unittest.TestCase):
  def reverse_string(self, input: str) -> str:
    output = [input[len(input)-n-1] for n in range(len(input))]
    return "".join(output)

  def test_reverse(self):
    self.assertEqual(self.reverse_string('FOO'), 'OOF')
    self.assertEqual(self.reverse_string('Cat'), 'taC')
    self.assertEqual(self.reverse_string('The Daily Byte'), 'etyB yliaD ehT')
    self.assertEqual(self.reverse_string('civic'), 'civic')

if __name__ == '__main__':
  unittest.main()