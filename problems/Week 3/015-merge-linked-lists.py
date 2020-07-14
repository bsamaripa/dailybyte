import unittest

"""
    This question is asked by Apple. Given two sorted linked lists, merge them
    together in ascending order and return a reference to the merged list
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


class TestMergeLinkedLists(unittest.TestCase):
  def merge_linked_lists(self, s: LinkedList, t: LinkedList) -> LinkedList:
    return LinkedList([]) 

  def test_merge_linked_lists(self):
    self.assertEqual(self.merge_linked_lists(LinkedList([]), LinkedList([])), LinkedList([]))
    self.assertEqual(self.merge_linked_lists(LinkedList([1, 2, 3]), LinkedList([4, 5, 6])), LinkedList([1, 2, 3, 4, 5, 6]))
    self.assertEqual(self.merge_linked_lists(LinkedList([1, 3, 5]), LinkedList([2, 4, 6])), LinkedList([1, 2, 3, 4, 5, 6]))
    self.assertEqual(self.merge_linked_lists(LinkedList([4, 4, 7]), LinkedList([1, 5, 6])), LinkedList([1, 4, 4, 5, 6, 7]))

if __name__ == '__main__':
  unittest.main()