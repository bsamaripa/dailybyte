import unittest

"""
    This question is asked by Amazon. Given a string representing the sequence of moves a robot 
    vacuum makes, return whether or not it will return to its original position. The string will
    only contain L, R, U, and D characters, representing left, right, up, and down respectively.
"""
class TestVacuumRoute(unittest.TestCase):
  def vacuum_route_valid(self, input: str) -> bool:
    if len(input) is 0: return False
    return False

  def test_vacuum_route(self):
    self.assertEqual(self.vacuum_route_valid(''), False)
    self.assertEqual(self.vacuum_route_valid('LR'), True)
    self.assertEqual(self.vacuum_route_valid('URURD'), False)
    self.assertEqual(self.vacuum_route_valid('RUULLDRD'), True)


if __name__ == '__main__':
  unittest.main()