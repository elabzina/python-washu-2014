#A few simple tests for all 4 sorting algorithms

import unittest
from sort_methods import *

class Test_test1(unittest.TestCase):
    def test1(self):
        self.assertEqual([1,2,3,4,5,6], getDataSet(bubble,[2,3,1,4,6,5]))

    def test2(self):
        self.assertEqual([1,1,2,3,4,5], getDataSet(bubble,[5,4,3,2,1,1]))

    def test3(self):
        self.assertEqual([1,2,3,4,5,6], getDataSet(bubbleUpdated,[2,3,1,4,6,5]))

    def test4(self):
        self.assertEqual([1,1,2,3,4,5], getDataSet(bubbleUpdated,[5,4,3,2,1,1]))

    def test5(self):
        self.assertEqual([1,2,3,4,5,6], getDataSet(mergesort,[2,3,1,4,6,5]))

    def test6(self):
        self.assertEqual([1,1,2,3,4,5], getDataSet(mergesort,[5,4,3,2,1,1]))

    def test7(self):
        self.assertEqual([1,2,3,4,5,6], getDataSet(quickSortCall,[2,3,1,4,6,5]))

    def test8(self):
        self.assertEqual([1,1,2,3,4,5], getDataSet(quickSortCall,[5,4,3,2,1,1]))
if __name__ == '__main__':
    unittest.main()
