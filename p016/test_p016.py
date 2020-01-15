import unittest
from p016 import powerDigitSum

class TestPowerDigitSum(unittest.TestCase):
    def test(self):
        self.assertEqual(powerDigitSum(15), 26)
        self.assertEqual(powerDigitSum(128), 166)
        self.assertEqual(powerDigitSum(1000), 1366)       

if __name__ == '__main__':
    unittest.main()