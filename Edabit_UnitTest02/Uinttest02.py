import unittest 
import IntegerDigitsCount02

class Test(unittest.TestCase):
    def count(self):
        self.assertEqual(IntegerDigitsCount02.count(318))
        self.assertEqual(IntegerDigitsCount02.count(-92563))
        self.assertEqual(IntegerDigitsCount02.count(4666))
        self.assertEqual(IntegerDigitsCount02.count(-314890))
        self.assertEqual(IntegerDigitsCount02.count(654321))
        self.assertEqual(IntegerDigitsCount02.count(638476))

if __name__ == '__main__':
    unittest.main()