import unittest
from p021 import sumAmicableNum

class TestSumAmicableNum(unittest.TestCase):
    def test(self):
        self.assertEqual(sumAmicableNum(1000), 504)
        self.assertEqual(sumAmicableNum(2000), 2898)
        self.assertEqual(sumAmicableNum(5000), 8442)
        self.assertEqual(sumAmicableNum(10000), 31626)
        

if __name__ == '__main__':
    unittest.main()