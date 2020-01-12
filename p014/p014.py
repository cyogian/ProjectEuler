def sequenceLength(num):
    """
        A function that calculates the collatz sequence length of a given number.
    """
    length = 0
    while num >= 1:
        length += 1
        if num == 1:
            break
        if num % 2 == 0: num /= 2
        else: num = 3 * num + 1
    return length

def longestCollatzSequence(limit):
    """
        A function that compares the collatz sequence length for each starting-point within given limit.
        And returns the starting-point with longest sequence length.
    """
    longestSequenceLength = 1
    startPoint = 1
    for i in range(2, limit + 1):
        currentSequenceLength = sequenceLength(i)
        if currentSequenceLength > longestSequenceLength:
            longestSequenceLength = currentSequenceLength
            startPoint = i
    return startPoint

if __name__ == "__main__":
    print(longestCollatzSequence(1000000))