import unittest
from p020 import sumFactorialDigits

class TestSumFactorialDigits(unittest.TestCase):
    def test(self):
        self.assertEqual(sumFactorialDigits(10), 27)
        self.assertEqual(sumFactorialDigits(25), 72)
        self.assertEqual(sumFactorialDigits(50), 216)
        self.assertEqual(sumFactorialDigits(75), 432)
        self.assertEqual(sumFactorialDigits(100), 648)
        

if __name__ == '__main__':
    unittest.main()