import unittest
from p005 import lowestCommonMultiple

class TestLowestCommonMultiple(unittest.TestCase):

    def test(self):
        self.assertEqual(lowestCommonMultiple(5), 60)
        self.assertEqual(lowestCommonMultiple(7), 420)
        self.assertEqual(lowestCommonMultiple(10), 2520)
        self.assertEqual(lowestCommonMultiple(13), 360360)
        self.assertEqual(lowestCommonMultiple(20), 232792560)

if __name__ == '__main__':
    unittest.main()