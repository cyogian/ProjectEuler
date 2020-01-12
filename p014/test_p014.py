import unittest
from p014 import longestCollatzSequence

class TestLongestCollatzSequence(unittest.TestCase):
    def test(self):
        self.assertEqual(longestCollatzSequence(14), 9)
        self.assertEqual(longestCollatzSequence(5847), 3711)
        self.assertEqual(longestCollatzSequence(46500), 35655)
        self.assertEqual(longestCollatzSequence(54512), 52527)
        self.assertEqual(longestCollatzSequence(100000), 77031)
        

if __name__ == '__main__':
    unittest.main()