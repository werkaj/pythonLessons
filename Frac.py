#7.1

class Frac:

    def __init__(self, x=0, y=1):
        if y == 0:
            raise ValueError
        else:
            self.x = x
            self.y = y

    def __str__(self): 
        if self.y == 1:
            return "{}".format(self.x)
        else:
            return "{}/{}".format(self.x,self.y)

    def __repr__(self):
        return "Frac({},{})",format(self.x,self.y)

    def __eq__(self, other):
        if float(self) == float(other):
            return True
        else:
            return False
    
    def _neq_(self,other):
        return not self==other

    # cmp nie działa w python3, dodane eq, neq
    # def __cmp__(self,other):
    #     if(self.x*other.y < other.x*self.y):
    #         return -1
    #     elif(self.x*other.y > other.x*self.y):
    #         return 1
    #     else:
    #          return 0 

    def __add__(self, other):
        return Frac(self.x*other.y + other.x*self.y, self.y*other.y)
    
    def __radd__(self, other):
        return Frac(self.x + self.y*other, self.y)

    def __sub__(self,other):
        return Frac(self.x*other.y - other.x*self.y, self.y*other.y) 

    def __rsub__(self, other):
        return Frac(self.y * other - self.x, self.y)  

    def __mul__(self,other):
        return Frac(self.x*other.x, self.y*other.y) 
    
    def __rmul__(self, other):
        return Frac(self.x*other, self.y)  

    def __truediv__(self, other):
        return Frac(self.x*other.y, self.y*other.x) 
    
    def __rtruediv__(self, other):
        return Frac(self.y*other, self.x)

    def __pos__(self):  
        return self

    def __neg__(self): 
        return Frac(-self.x,self.y)        

    def __invert__(self):
        return Frac(self.y,self.x)

    def __float__(self):       
        return float(self.x/self.y)

import unittest

class TestFrac(unittest.TestCase):

    def test_fracs_exception(self):
        self.assertRaises(ValueError,Frac, 2,0)

    def test_eq_fracs(self):
        self.assertTrue(Frac(3,2)==Frac(6,4))
    
    def test_neq_fracs(self):
        self.assertTrue(Frac(2,2)!=Frac(3,2))

    def test_add_fracs(self):
        self.assertEqual(Frac(1,2)+Frac(2,2),Frac(3,2))
    
    def test_radd_fracs(self):
        self.assertEqual(2+Frac(1,2),Frac(5,2))

    def test_sub_fracs(self):
        self.assertEqual(Frac(2,3)-Frac(1,4),Frac(5,12))
    
    def test_rsub_fracs(self):
        self.assertEqual((2 - Frac(4,3)),Frac(2,3))

    def test_mul_fracs(self):
        self.assertEqual(Frac(2,3)*Frac(2,2),Frac(4,6))

    def test_rmul_(self):
        self.assertEqual(2*Frac(2,3),Frac(4,3))

    def test_div_fracs(self):
        self.assertEqual(Frac(2,3)/Frac(4,3),Frac(1,2))

    def test_rdiv_(self):
        self.assertEqual(3/Frac(4,5),Frac(15,4))

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy