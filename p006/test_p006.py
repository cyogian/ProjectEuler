import unittest
from p006 import sumSquareDifference

class TestSumSquareDifference(unittest.TestCase):

    def test(self):
        self.assertEqual(sumSquareDifference(10), 2640)
        self.assertEqual(sumSquareDifference(20), 41230)
        self.assertEqual(sumSquareDifference(100), 25164150)


if __name__ == '__main__':
    unittest.main()