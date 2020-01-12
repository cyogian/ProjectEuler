def largeSum(arr):
    lSum = 0
    for i in arr:
        lSum += int(i[:11])
    return int(str(lSum)[:10])

if __name__ == "__main__":
    from test_p013 import fiftyDigitNums
    print(largeSum(fiftyDigitNums))