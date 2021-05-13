import unittest 
import FindTheLargestEvenNumber04

class Test(unittest.TestCase):
    def largest_even (self):
        self.assertEqual(FindTheLargestEvenNumber04.largest_even([3, 7, 2, 1, 7, 9, 10, 13]))
        self.assertEqual(FindTheLargestEvenNumber04.largest_even([1, 3, 5, 7]))
        self.assertEqual(FindTheLargestEvenNumber04.largest_even([0, 19, 18973623]))

if __name__ == '__main__':
    unittest.main()