from points import Point

#zadanie 6.3

class Rectangle:
    """Klasa reprezentująca prostokąt na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2):
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)

    def __str__(self):
        return '[({},{}),({},{})]'.format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y)         # "[(x1, y1), (x2, y2)]"

    def __repr__(self):
        return 'Rectangle({},{},{},{})'.format(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y)          # "Rectangle(x1, y1, x2, y2)"

    def __eq__(self, other):
        return (self.pt1 == other.pt1) and (self.pt2 == other.pt2)   # obsługa rect1 == rect2

    def __ne__(self, other):        # obsługa rect1 != rect2
        return not self == other

    def center(self):
        return Point(self.pt1.x + (self.pt2.x-self.pt1.x)/2, self.pt1.y + (self.pt2.y-self.pt1.y)/2)          # zwraca środek prostokąta

    def area(self):
        return (self.pt2.x-self.pt1.x)*(self.pt2.y-self.pt1.y)        # pole powierzchni

    def move(self, x, y):
        self.pt1 += Point(x,y)
        self.pt2 += Point(x,y)
        return self   # przesunięcie o (x, y)

import unittest

class TestRectangle(unittest.TestCase):
    def test_eq(self):
        self.assertTrue(Rectangle(1,1,2,2)==Rectangle(1,1,2,2))

    def test_not_eq(self):
        self.assertTrue(Rectangle(1,1,2,2)!=Rectangle(1,2,2,2))

    def test_center(self):
        self.assertTrue(Rectangle.center(Rectangle(2,2,4,4)) == Point(3,3))
        
    def test_area(self):
        self.assertEqual(Rectangle.area(Rectangle(2,2,4,4)),4)

    def test_move(self):
        self.assertEqual(Rectangle.move(Rectangle(2,2,3,3),1,2),Rectangle(3,4,4,5))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy