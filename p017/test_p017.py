import unittest
from p017 import numberLetterCounts

class TestNumberLetterCounts(unittest.TestCase):
    def test(self):
        self.assertEqual(numberLetterCounts(5), 19)
        self.assertEqual(numberLetterCounts(150), 1903)
        self.assertEqual(numberLetterCounts(1000), 21124)       

if __name__ == '__main__':
    unittest.main()