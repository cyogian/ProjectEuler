def numberLetterCounts(limit):
    zeroTo19 = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    twentyTo90 = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7
    thousand = 8
    thousandAnd = 11
    hundredAnd = 10
    def letterCount(num):
        if num <= 19:
            return zeroTo19[num]
        if num < 100:
            return twentyTo90[num // 10] + zeroTo19[num % 10]
        if num < 1000:
            hundredth = num % 100
            if hundredth == 0:
                return zeroTo19[num // 100] + hundred
            return zeroTo19[num // 100] + hundredAnd + letterCount(hundredth)
        thousandth = num % 1000
        if thousandth == 0:
            return zeroTo19[num // 1000] + thousand
        if thousandth >= 100:
            return zeroTo19[num // 1000] + thousand + letterCount(thousandth)
        return zeroTo19[num // 1000] + thousandAnd + letterCount(thousandth)
    totalCount = 0
    for i in range(1, limit + 1):
        totalCount += letterCount(i)
    return totalCount

if __name__ == "__main__":
    print(numberLetterCounts(1000))