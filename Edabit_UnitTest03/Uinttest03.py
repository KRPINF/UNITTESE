import unittest 
import RightShiftbyDivision03

class Test(unittest.TestCase):
    def shift_to_right (self):
        self.assertEqual(RightShiftbyDivision03.shift_to_right(80,3))
        self.assertEqual(RightShiftbyDivision03.shift_to_right(-24,2))
        self.assertEqual(RightShiftbyDivision03.shift_to_right(-5,1))
        self.assertEqual(RightShiftbyDivision03.shift_to_right(4666,6))
        self.assertEqual(RightShiftbyDivision03.shift_to_right(3777,6))
        self.assertEqual(RightShiftbyDivision03.shift_to_right(-512,10))

if __name__ == '__main__':
    unittest.main()