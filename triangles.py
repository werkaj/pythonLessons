#7.4
from points import Point

class Triangle:
    """Klasa reprezentująca trójkąty na płaszczyźnie."""

    def __init__(self, x1, y1, x2, y2, x3, y3):
        # Należy zabezpieczyć przed sytuacją, gdy punkty są współliniowe.
        if Point(x1,y1)==Point(x2,y2) or Point(x2,y2)==Point(x3,y3) or Point(x3,y3)==Point(x1,y3) \
            or x1==x2==x3 or y1 == y2 == y3:
            raise ValueError 
        else:    
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)
            self.pt3 = Point(x3, y3)

    def __str__(self):
        return "[({},{}),({},{}),({},{})]".format(x1, y1, x2, y2, x3, y3)      

    def __repr__(self):
        return "Triangle({},{},{},{},{},{})".format( x1, y1, x2, y2, x3, y3)       
    
    def __eq__(self, other):
        return self.pt1==other.pt1 and self.pt2==other.pt2 and self.pt3==other.pt3

    def __ne__(self, other):        # obsługa tr1 != tr2
        return not self == other

    def center(self):
        return Point(self.pt2.x + (self.pt3.x-self.pt2.x)/2, self.pt3.y + (self.pt1.y-self.pt3.y)/2)  

    def area(self):
        return (self.pt3.x-self.pt2.x)*(self.pt1.y-self.pt2.y)/2

    def move(self, x, y):
        self.pt1 += Point(x,y)
        self.pt2 += Point(x,y) 
        self.pt3 += Point(x,y) 
        return self    

    def make4(self):
        return [Triangle(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y +2,self.pt3.x,self.pt3.y +2),
        Triangle(self.pt1.x,self.pt1.y -1,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y),
        Triangle(self.pt1.x,self.pt1.y -2,self.pt2.x,self.pt2.y,self.pt3.x,self.pt3.y),
        Triangle(self.pt1.x,self.pt1.y,self.pt2.x,self.pt2.y +1,self.pt3.x,self.pt3.y +1)]           # zwraca listę czterech mniejszych

# Kod testujący moduł.

import unittest

class TestTriangle(unittest.TestCase):

    def test_exception(self):
        self.assertRaises(ValueError,Triangle, 1,1,1,1,1,1)

    def test_eq_triangles(self):
        self.assertTrue(Triangle(2,2,3,3,4,4)==Triangle(2,2,3,3,4,4))
    
    def test_neq_triangles(self):
        self.assertTrue(Triangle(2,2,3,3,4,4)!=Triangle(2,4,3,3,4,4))
    
    def test_center_triangle(self):
        self.assertEqual(Triangle.center(Triangle(3,6,2,4,4,4)),Point(3,5))

    def test_area_triangle(self):
        self.assertEqual(Triangle.area(Triangle(3,6,2,4,4,4)),2)
    
    def test_move_triangle(self):
        self.assertEqual(Triangle.move(Triangle(1,1,2,2,3,3),1,1), Triangle(2,2,3,3,4,4))
    
    def test_make4_triangle(self):
        triangle = Triangle(3,8,2,4,4,4)
        lista = Triangle.make4(triangle)
        area = triangle.area()
        self.assertTrue(lista[0].area() < area and lista[1].area() < area and lista[2].area() < area\
             and lista[3].area() < area)
    

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy