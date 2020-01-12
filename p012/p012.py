import math
def getPrimeFactors(num):
    """
        A function that generates a dictionary with 
        each prime factor of given number as a key and
        their respective degrees as value.
    """
    n = num
    primes = {}

    p = 2
    sqrt = math.sqrt(num)

    def checkAndUpdate(inc):
        nonlocal n
        nonlocal p
        nonlocal primes
        if n % p == 0:
            if str(p) in primes.keys():
                primes[str(p)] += 1
            else:
                primes[str(p)] = 1
            n /= p
        else:
            p += inc
    
    while p == 2 and p <= n:
        checkAndUpdate(1)
    while p <= n and p <= sqrt:
        checkAndUpdate(2)
    if len(primes.keys()) == 0:
        primes[str(num)] = 1
    elif n != 1:
        primes[str(n)] = 1
    return primes

def noOfFactors(num):
    """
        A function that calculates the number of factors of a given number.
        
        * calculating number of factors 
        * let a, b, c.... be the prime factors number X
        * dA, dB, dC.... be the degree for a, b, c.... 
        * i.e. dA is no. of times X can be perfectly divided by a
        * Total no. of factors of X = (dA+1) * (dB+1) * (dC+1).....
    """
    primeFactors = getPrimeFactors(num) # A dictionary containing degrees of each prime factor for given num
    prod = 1
    for p in primeFactors:
        prod *= primeFactors[p] + 1
    return prod

def divisibleTriangleNumber(n):
    # calculating triangle numbers
    if n == 1: return 3
    counter = 2
    triangleNumber = (counter * (counter + 1)) // 2
    counter += 1
    while noOfFactors(triangleNumber) <= n: 
        # checking for no of factors > n of the triangle number
        triangleNumber = (counter * (counter + 1)) // 2
        counter += 1
    return triangleNumber

if __name__ == "__main__":
    print(divisibleTriangleNumber(500))