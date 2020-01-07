def nthPrime(n):
    primeList = []
    i = 2
    j = 1
    while j <= n:
        isPrime = True
        for k in primeList:
            if i % k == 0:
                isPrime = False
                break
        if isPrime:
            primeList.append(i)
            j += 1
        i += 1
    return primeList[-1]

if __name__ == "__main__":
    print(nthPrime(10001))