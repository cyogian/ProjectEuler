import math
def sumOfDivisors(n):
    """
    A function that returns the sum of proper divisors of a given number n.
    """
    if n == 1:
        return 0
    dSum = 1
    sqrt = math.sqrt(n)
    rsqrt = int(sqrt)
    for i in range(2, rsqrt):
        if n % i == 0:
            dSum += i + n / i
    if sqrt == rsqrt:
        dSum += sqrt
    return int(dSum)

def sumAmicableNum(n):
    d = []
    amiSum = 0
    for i in range(n):
        d.append(sumOfDivisors(i))
    for i in range(2, n):
        dSum = d[i]
        if dSum < n:
            if d[dSum] == i and i != dSum:
                amiSum += dSum
    return amiSum
        
if __name__ == "__main__":
    print(sumAmicableNum(10000))