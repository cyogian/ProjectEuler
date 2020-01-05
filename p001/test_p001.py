import unittest
from p001 import multisum

class TestMultiSum(unittest.TestCase):

    def test(self):
        self.assertEqual(multisum(1000), 233168, "Should be 233168")

if __name__ == '__main__':
    unittest.main()