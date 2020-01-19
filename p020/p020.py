def sumFactorialDigits(n):
    bigNum = [1]
    for i in range(2, n + 1):
        count = len(bigNum)
        overflow = 0
        for j in range(count):
            digit  = bigNum[j]
            digit = digit * i + overflow
            overflow = digit // 10
            bigNum[j] = digit % 10
        while overflow > 0:
            bigNum.append(overflow % 10)
            overflow = overflow // 10
    return sum(bigNum)

if __name__ == "__main__":
    print(sumFactorialDigits(100))