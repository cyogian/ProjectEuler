def largestPrimeFactor(number):
    primeList = list()
    maxPrimeFactor = 0
    i = 2
    while(i <= number):
        isPrime = True
        for j in primeList:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(i)
            if number % i == 0:
                maxPrimeFactor = i
            while number % i == 0:
                # we are reducing the number to a number which is
                # not divisible by already tested prime number.
                # Prime Factorization Logic
                # This will reduce the time complexity to almost a constant value.
                number = number // i
        i += 1
    return maxPrimeFactor

def largestPrimeFactorOld(number):
    """
        This version is slow.
    """
    primeList = list()
    maxPrimeFactor = 0
    for i in range(2, int(number**0.5) + 1):
        isPrime = True
        for j in primeList:
            if i % j == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(i)
            if number % i == 0:
                maxPrimeFactor = i
    return maxPrimeFactor if maxPrimeFactor else number


if __name__ == "__main__":
    print(largestPrimeFactor(600851475143))
    
