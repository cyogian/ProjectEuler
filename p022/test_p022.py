import unittest
import json
from p022 import nameScores

test1 = ["THIS", "IS", "ONLY", "A", "TEST"]
test2 = ["I", "REPEAT", "THIS", "IS", "ONLY", "A", "TEST"]

# loading "name" list from the file "p022_names.txt"
namefile = open("p022/p022_names.txt", "r")
name = json.loads(namefile.readline())

class TestNameScores(unittest.TestCase):
    def test(self):
        self.assertEqual(nameScores(test1), 791)
        self.assertEqual(nameScores(test2), 1468)
        self.assertEqual(nameScores(name), 871198282)      

if __name__ == '__main__':
    unittest.main()