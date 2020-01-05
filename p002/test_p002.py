import unittest
from p002 import fib

class TestFib(unittest.TestCase):

    def test(self):
        self.assertEqual(fib(10), 44)
        self.assertEqual(fib(18), 3382)
        self.assertEqual(fib(23), 60696)
        self.assertEqual(fib(43), 350704366)

if __name__ == '__main__':
    unittest.main()