from functools import reduce
def wordWorth(string):
    letterWorth = {
    "A" : 1, "B" : 2, "C" : 3, "D" : 4, "E" : 5,
    "F" : 6, "G" : 7, "H" : 8, "I" : 9, "J" : 10,
    "K" : 11, "L" : 12, "M" : 13, "N" : 14, "O" : 15,
    "P" : 16, "Q" : 17, "R" : 18, "S" : 19, "T" : 20,
    "U" : 21, "V" : 22, "W" : 23, "X" : 24, "Y" : 25,
    "Z" : 26
    }
    worth = 0
    for i in range(len(string)):
        worth += letterWorth[string[i]]
    return worth

def nameScores(arr):
    arr.sort()
    nameScore = 0
    for i in range(len(arr)):
        nameScore += wordWorth(arr[i]) * (i + 1)
    return nameScore

if __name__ == "__main__":
    from test_p022 import test1, test2, name
    print(nameScores(test1))
    print(nameScores(test2))
    print(nameScores(name))