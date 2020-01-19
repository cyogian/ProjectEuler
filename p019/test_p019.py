import unittest
from p019 import countingSundays

class TestCountingSundays(unittest.TestCase):
    def test(self):
        self.assertEqual(countingSundays(1943, 1946), 6)
        self.assertEqual(countingSundays(1995, 2000), 10)
        self.assertEqual(countingSundays(1901, 2000), 171)
        

if __name__ == '__main__':
    unittest.main()