def primeSummation(n):
    # Sieve Of Eratosthenes (Greek Algo to Find Prime Numbers below N)
    # recommended for N <= 10 million
    # Time Complexity = O(nlog(log n))
    # Space Complexity = O(n)
    prime = [True for i in range(n + 1)]
    p = 2
    while p * p <= n:
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
        p += 1
    primeSum = 0
    for p in range(2, n):
        if prime[p]:
            primeSum += p
    return primeSum
                

if __name__ == "__main__":
    print(primeSummation(2000000))