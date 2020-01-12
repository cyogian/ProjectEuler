import unittest
from p012 import divisibleTriangleNumber

class TestDivisibleTriangleNumber(unittest.TestCase):
    def test(self):
        self.assertEqual(divisibleTriangleNumber(5), 28)
        self.assertEqual(divisibleTriangleNumber(23), 630)
        self.assertEqual(divisibleTriangleNumber(167), 1385280)
        self.assertEqual(divisibleTriangleNumber(374), 17907120)
        self.assertEqual(divisibleTriangleNumber(500), 76576500)
        
if __name__ == '__main__':
    unittest.main()