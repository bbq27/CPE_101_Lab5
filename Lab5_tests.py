# Name: Berfredd Quezon
# Section: 11
#########################################################
from data import *
from Lab5 import *
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    #    Part 1 tests should be in data_tests.py.

    # Part 2
    #    Part 2 tests should be in data_tests.py.

    # Part 3
    def test_time_add1(self):
        time1 = Time(5,40,20)
        time2 = Time(5,20,30)
        self.assertEqual(Time(11,0,50), time_add(time1,time2))

    def test_time_add2(self):
        time1 = Time(2,59,27)
        time2 = Time(5,59,38)
        self.assertEqual(Time(8,59,5), time_add(time1,time2))

    # Part 4
    def test_is_descending1(self):
        lst = []
        self.assertEqual(False, is_descending(lst))

    def test_is_descending2(self):
        lst1 = [5, 4, 3, 2, 1]
        self.assertEqual(True, is_descending(lst1))

    def test_is_descending3(self):
        lst2 = [5, 4, -3, 2, 1]
        self.assertEqual(False, is_descending(lst2))

    # Part 5
    def test_largest_between1(self):
        L = []
        self.assertEqual(None,largest_between(L, 1, 3))

    def test_largest_between2(self):
        L = [4,6,2,3]
        self.assertEqual(None,largest_between(L,4,1))

    def test_largest_between3(self):
        L = [6,2,-20,7,13,7,-13,52,35,-7,2]
        self.assertEqual(52,largest_between(L,2,10))

    def test_largest_between4(self):
        L = [6,2,-20,7,13,7,-13,52,35,-7,2]
        self.assertEqual(-1,largest_between(L,2,20))

    # Part 6
    def test_euclidean_distance(self):
        self.assertEqual(3,euclidean_distance(Point(3,4), Point(5,2)))

    def test_distance_from_origin1(self):
        L = []
        self.assertEqual(None, distance_from_origin(L))

    def test_distance_from_origin2(self):
        L = [Point(0, -1), Point(3, 4), Point(-6, 8), Point(3, 7)]
        self.assertEqual([1, 5, 10, 8], distance_from_origin(L))

    def test_furthest_from_origin1(self):
        L = []
        self.assertEqual(None, furthest_from_origin(L))

    def test_furthest_from_origin2(self):
        L = [Point(0,-1), Point(3,4), Point(-6,8), Point(3,7)]
        self.assertEqual(2, furthest_from_origin(L))

    def test_furthest_from_origin3(self):
        L = [Point(3,7), Point(3,4), Point(0,-1), Point(4,-3), Point(-6,8)]
        self.assertEqual(4, furthest_from_origin(L))



if __name__ == '__main__':
    unittest.main()
