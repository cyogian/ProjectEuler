import unittest
from p009 import specialPythagoreanTriplets

class TestSpecialPythagoreanTriplets(unittest.TestCase):

    def test(self):
        self.assertEqual(specialPythagoreanTriplets(1000), 31875000)
        self.assertEqual(specialPythagoreanTriplets(24), 480)
        self.assertEqual(specialPythagoreanTriplets(120), 49920)
if __name__ == '__main__':
    unittest.main()