def sumSquareDifference(n):
    squareOfSum = (n * (n + 1) / 2) ** 2
    sumOfSquares = (n * (n + 1) * (2 * n + 1)) / 6
    return int(squareOfSum - sumOfSquares)

if __name__ == "__main__":
    print(sumSquareDifference(100))