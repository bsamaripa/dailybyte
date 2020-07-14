import unittest

"""
    This question is asked by Facebook. Given a linked list and a value n,
    remove the nth to last node and return the resulting list. 
"""
class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class TestRemoveNthToLastNode(unittest.TestCase):
  def remove_nth_to_last_node(self, s: LinkedList, n: int) -> LinkedList:
    return LinkedList([]) 

  def test_merge_linked_lists(self):
    self.assertEqual(self.remove_nth_to_last_node(LinkedList([1, 2, 3]), 1), LinkedList([1, 2]))
    self.assertEqual(self.remove_nth_to_last_node(LinkedList([1, 2, 3]), 2), LinkedList([1, 3]))
    self.assertEqual(self.remove_nth_to_last_node(LinkedList([1, 2, 3]), 3), LinkedList([2, 3]))

if __name__ == '__main__':
  unittest.main()