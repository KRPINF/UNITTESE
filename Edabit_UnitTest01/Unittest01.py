import unittest 
import IteratedSquareRoot01

class Test(unittest.TestCase):
    def i_sqrttest (self):
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(1))
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(2))
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(7))
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(27))
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(256))
        self.assertEqual(IteratedSquareRoot01.i_sqrttest(-1))

if __name__ == '__main__':
    unittest.main()