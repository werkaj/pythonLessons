import unittest
import fracs

class TestFractions(unittest.TestCase):

    def setUp(self):
        self.zero = [0, 1]

    def test_add_frac(self):
        self.assertEqual(fracs.add_frac([1, 2], [1, 3]), [5, 6])

    def test_sub_frac(self):
        self.assertEqual(fracs.sub_frac([2,3],[1,4]),[5,12])

    def test_mul_frac(self):
        self.assertEqual(fracs.mul_frac([1,2],[2,3]),[2,6])

    def test_div_frac(self):
        self.assertEqual(fracs.div_frac([1,2],[2,3]),[3,4])

    def test_is_positive(self):
        self.assertTrue(fracs.is_positive([1,2]))

    def test_is_zero(self):
        self.assertTrue(fracs.is_zero([0,1]))

    def test_cmp_frac(self):
        self.assertEqual(fracs.cmp_frac([2,3],[1,4]),1)

    def test_frac2float(self):
        self.assertEqual(fracs.frac2float([1,2]),0.5)

    def tearDown(self):
        self.assertEqual(fracs.tear_down([4,3]),1)

if __name__ == '__main__':
    unittest.main()     # uruchamia wszystkie testy