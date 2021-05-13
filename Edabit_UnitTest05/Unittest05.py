import unittest 
import WhichFunctionReturnstheLargerNumber05

class Test(unittest.TestCase):
    def which_is_larger(self):
        self.assertEqual(WhichFunctionReturnstheLargerNumber05.which_is_larger(5,10))
        self.assertEqual(WhichFunctionReturnstheLargerNumber05.which_is_larger(25,25))
        self.assertEqual(WhichFunctionReturnstheLargerNumber05.which_is_larger(505050,5050))

if __name__ == '__main__':
    unittest.main()