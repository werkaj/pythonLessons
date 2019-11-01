import math

#zadanie 6.2

class Point:
    """Klasa reprezentująca punkty na płaszczyźnie."""

    def __init__(self, x, y):  # konstuktor
        self.x = x
        self.y = y

    def __str__(self): 
        return '({},{})'.format(self.x,self.y)         # zwraca string "(x, y)"

    def __repr__(self): 
        return 'Point({},{})'.format(self.x,self.y)         # zwraca string "Point(x, y)"

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)   # obsługa point1 == point2

    def __ne__(self, other):        # obsługa point1 != point2
        return not self == other

    # Punkty jako wektory 2D.
    def __add__(self, other): 
        return Point(self.x + other.x, self.y + other.y)  # v1 + v2

    def __sub__(self, other): 
        return Point(self.x - other.x, self.y - other.y) 

    def __mul__(self, other):
        return self.x*other.x + self.y*other.y  # v1 * v2, iloczyn skalarny

    def cross(self, other):         # v1 x v2, iloczyn wektorowy 2D
        return self.x * other.y - self.y * other.x

    def length(self): 
        return math.sqrt(self.x*self.x + self.y*self.y)       # długość wektora

import unittest

class TestPoint(unittest.TestCase):
    def test_equals(self):
        self.assertTrue(Point(2,1)==Point(2,1))
    
    def test_not_equal(self):
        self.assertTrue(Point(2,1)!=Point(2,2))

    def test_add_points(self):
        self.assertEqual((Point(1,2)+Point(2,2)),Point(3,4))

    def test_sub_points(self):
        self.assertEqual((Point(2,2)-Point(2,1)),Point(0,1))

    def test_mul_(self):
        self.assertEqual((Point(2,3)*Point(2,2)),10)

    def test_cross_(self):
        self.assertEqual((Point.cross(Point(4,2),Point(1,2))),6)

    def test_lenght_(self):
        self.assertEqual(Point.length(Point(3,4)),5)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy