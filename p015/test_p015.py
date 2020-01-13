import unittest
from p015 import latticePaths

class TestLatticePaths(unittest.TestCase):
    def test(self):
        self.assertEqual(latticePaths(1), 2)
        self.assertEqual(latticePaths(2), 6)
        self.assertEqual(latticePaths(9), 48620)
        self.assertEqual(latticePaths(20), 137846528820)
        

if __name__ == '__main__':
    unittest.main()