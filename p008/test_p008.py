import unittest
from p008 import largestProductinaSeries

class TestLargestProductinaSeries(unittest.TestCase):

    def test(self):
        self.assertEqual(largestProductinaSeries(4), 5832)
        self.assertEqual(largestProductinaSeries(13), 23514624000)

if __name__ == '__main__':
    unittest.main()