import unittest
from p018 import maximumPathSumI, testTriangle, numTriangle

class TestMaxPathSumI(unittest.TestCase):
    def test(self):
        self.assertEqual(maximumPathSumI(testTriangle), 23)
        self.assertEqual(maximumPathSumI(numTriangle), 1074)
        

if __name__ == '__main__':
    unittest.main()