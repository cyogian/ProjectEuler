import unittest
from p001 import multisum

class TestMultiSum(unittest.TestCase):

    def test(self):
        self.assertEqual(multisum(1000), 233168)
        self.assertEqual(multisum(49), 543)
        self.assertEqual(multisum(19564), 89301183)
        self.assertEqual(multisum(8456), 16687353)

if __name__ == '__main__':
    unittest.main()