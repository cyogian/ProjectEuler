import unittest
from p010 import primeSummation

class TestPrimeSummation(unittest.TestCase):

    def test(self):
        self.assertEqual(primeSummation(17), 41)
        self.assertEqual(primeSummation(2001), 277050)
        self.assertEqual(primeSummation(140759), 873608362)
        self.assertEqual(primeSummation(2000000), 142913828922)
if __name__ == '__main__':
    unittest.main()