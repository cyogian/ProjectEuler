import unittest
from p003 import largestPrimeFactor

class TestLargestPrimeFactor(unittest.TestCase):

    def test(self):
        self.assertEqual(largestPrimeFactor(2), 2)
        self.assertEqual(largestPrimeFactor(3), 3)
        self.assertEqual(largestPrimeFactor(5), 5)
        self.assertEqual(largestPrimeFactor(7), 7)
        self.assertEqual(largestPrimeFactor(13195), 29)
        self.assertEqual(largestPrimeFactor(600851475143), 6857)



if __name__ == '__main__':
    unittest.main()