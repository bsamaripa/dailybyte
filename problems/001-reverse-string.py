import unittest
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