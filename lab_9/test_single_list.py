import unittest
from single_list import SingleList
from node import Node


class TestSingleList(unittest.TestCase):

    def setUp(self):
        self.list1 = SingleList()
        self.list2 = SingleList()
        for i in range(1, 4):
            self.list1.insert_tail(Node(i))

    def test_remove_tail(self):
        self.assertEqual(self.list1.remove_tail().data, 3)
        self.assertEqual(self.list1.length, 2)

        self.assertEqual(self.list2.remove_tail().data, 13)
        self.assertEqual(self.list2.length, 2)

        with self.assertRaises(ValueError):
            empty_list = SingleList()
            empty_list.remove_tail()

    def test_join(self):
        length = self.list1.length + self.list2.length
        self.list1.join(self.list2)
        self.assertEqual(self.list1.length, length)
        self.assertEqual(self.list2.length, 0)
        self.assertIsNone(self.list2.head)
        self.assertIsNone(self.list2.tail)

        current = self.list1.head
        for i in range(1, 4):
            self.assertEqual(i, current.data)
            current = current.next
        for i in range(1, 4):
            self.assertEqual(i + 10, current.data)
            current = current.next

    def test_clear(self):
        self.list1.clear()
        self.assertEqual(self.list1.length, 0)
        self.assertIsNone(self.list1.head)
        self.assertIsNone(self.list1.tail)


if __name__ == '__main__':
    unittest.main()
