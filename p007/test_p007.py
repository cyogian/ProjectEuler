import unittest
from p007 import nthPrime

class TestNthPrime(unittest.TestCase):

    def test(self):
        self.assertEqual(nthPrime(6), 13)
        self.assertEqual(nthPrime(10), 29)
        self.assertEqual(nthPrime(100), 541)
        self.assertEqual(nthPrime(1000), 7919)
        self.assertEqual(nthPrime(10001), 104743)

if __name__ == '__main__':
    unittest.main()