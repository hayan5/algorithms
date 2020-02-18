import unittest
import quick_sort
import merge_sort
import insertion_sort

class TestQuickSort(unittest.TestCase):
  arr0 = []
  arr1 = [1]
  arr2 = [2,1]
  arr3 = [1,4,7,3,2,5,8,6]
  arr4 = [1,4,7,3,2,0,5,8,6]
  arr5 = [1,4,3,3,5,6,5,10]
  arr6 = [1,4,3,3,5,6,5,10,2]


  def test_Empty(self):
    self.assertEqual(quick_sort.quick_sort(self.arr0, 0, len(self.arr0)), [])
  def test_One(self):
    self.assertEqual(quick_sort.quick_sort(self.arr1, 0, len(self.arr1)-1), [1])
  def test_Two(self):
    self.assertEqual(quick_sort.quick_sort(self.arr2, 0, len(self.arr2)-1), [1,2])
  def test_Even(self):
    self.assertEqual(quick_sort.quick_sort(self.arr3, 0, len(self.arr3)-1), [1,2,3,4,5,6,7,8])
  def test_odd(self):
    self.assertEqual(quick_sort.quick_sort(self.arr4, 0, len(self.arr4)-1), [0,1,2,3,4,5,6,7,8])
  def test_repeat_even(self):
    self.assertEqual(quick_sort.quick_sort(self.arr5, 0, len(self.arr5)-1), [1,3,3,4,5,5,6,10])
  def test_repeat_odd(self):
    self.assertEqual(quick_sort.quick_sort(self.arr6, 0, len(self.arr6)-1), [1,2,3,3,4,5,5,6,10])

class TestMergeSort(unittest.TestCase):
  arr0 = []
  arr1 = [1]
  arr2 = [2,1]
  arr3 = [1,4,7,3,2,5,8,6]
  arr4 = [1,4,7,3,2,0,5,8,6]
  arr5 = [1,4,3,3,5,6,5,10]
  arr6 = [1,4,3,3,5,6,5,10,2]


  def test_Empty(self):
    self.assertEqual(merge_sort.merge_sort(self.arr0, 0, len(self.arr0)), [])
  def test_One(self):
    self.assertEqual(merge_sort.merge_sort(self.arr1, 0, len(self.arr1)-1), [1])
  def test_Two(self):
    self.assertEqual(merge_sort.merge_sort(self.arr2, 0, len(self.arr2)-1), [1,2])
  def test_Even(self):
    self.assertEqual(merge_sort.merge_sort(self.arr3, 0, len(self.arr3)-1), [1,2,3,4,5,6,7,8])
  def test_odd(self):
    self.assertEqual(merge_sort.merge_sort(self.arr4, 0, len(self.arr4)-1), [0,1,2,3,4,5,6,7,8])
  def test_repeat_even(self):
    self.assertEqual(merge_sort.merge_sort(self.arr5, 0, len(self.arr5)-1), [1,3,3,4,5,5,6,10])
  def test_repeat_odd(self):
    self.assertEqual(merge_sort.merge_sort(self.arr6, 0, len(self.arr6)-1), [1,2,3,3,4,5,5,6,10])

class TestInsertionSort(unittest.TestCase):
  arr0 = []
  arr1 = [1]
  arr2 = [2,1]
  arr3 = [1,4,7,3,2,5,8,6]
  arr4 = [1,4,7,3,2,0,5,8,6]
  arr5 = [1,4,3,3,5,6,5,10]
  arr6 = [1,4,3,3,5,6,5,10,2]


  def test_Empty(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr0, 0, len(self.arr0)), [])
  def test_One(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr1, 0, len(self.arr1)-1), [1])
  def test_Two(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr2, 0, len(self.arr2)-1), [1,2])
  def test_Even(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr3, 0, len(self.arr3)-1), [1,2,3,4,5,6,7,8])
  def test_odd(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr4, 0, len(self.arr4)-1), [0,1,2,3,4,5,6,7,8])
  def test_repeat_even(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr5, 0, len(self.arr5)-1), [1,3,3,4,5,5,6,10])
  def test_repeat_odd(self):
    self.assertEqual(insertion_sort.insertion_sort(self.arr6, 0, len(self.arr6)-1), [1,2,3,3,4,5,5,6,10])

if __name__ == '__main__':
  unittest.main()