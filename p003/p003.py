def largestPrimeFactor(number):
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
    
