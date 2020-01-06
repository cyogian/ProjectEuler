import unittest
from p004 import largestPalindromeProduct

class TestLargestPalindromeProduct(unittest.TestCase):

    def test(self):
        self.assertEqual(largestPalindromeProduct(1), 9)
        self.assertEqual(largestPalindromeProduct(2), 9009)
        self.assertEqual(largestPalindromeProduct(3), 906609)

if __name__ == '__main__':
    unittest.main()