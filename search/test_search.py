import unittest
import binary_search


class TestBinarySearch(unittest.TestCase):
  def test_0(self):
    arr = []
    l = 0
    r = len(arr) - 1
    x = 1
    self.assertEqual(binary_search.binary_search(arr, l, r, x), -1)
  def test_1(self):
    arr = [3]
    l = 0
    r = len(arr) - 1
    x = 3
    self.assertEqual(binary_search.binary_search(arr, l, r, x), 0)
  def test_2(self):
    arr = [3]
    l = 0
    r = len(arr) - 1
    x = 7
    self.assertEqual(binary_search.binary_search(arr, l, r, x), -1)
  def test_3(self):
    arr = [1,3,4,6,7,8,9]
    l = 0
    r = len(arr) - 1
    x = 7
    self.assertEqual(binary_search.binary_search(arr, l, r, x), 4)
  def test_4(self):
    arr = [1,3,4,6,7,8,9]
    l = 0
    r = len(arr) - 1
    x = 9
    self.assertEqual(binary_search.binary_search(arr, l, r, x), 6)
  def test_5(self):
    arr = [1,3,4,6,7,8,9]
    l = 0
    r = len(arr) - 1
    x = 5
    self.assertEqual(binary_search.binary_search(arr, l, r, x), -1)


if __name__ == '__main__':
  unittest.main()