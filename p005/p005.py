from functools import reduce
def gcd(a, b):
    """
    Greatest Common Divisor of two numbers does not change
    if larger number is replaced by its difference with smaller number.

    conclusively we will get the gcd if we replace:
        numerator with denominator 
        denominator with remainder
    until numerator is perfectly divisible by denominator
    """
    if a > b:
        numerator = a
        denominator = b
    else:
        numerator = b
        denominator = a
    remainder = numerator % denominator
    while remainder != 0:
        numerator = denominator
        denominator = remainder
        remainder = numerator % denominator
    return denominator

def lcm(a, b):
    """
        lcm = | a * b / gcd(a, b) |
    """
    return int(int(a * b) / int(gcd(a, b))) 
    
def lowestCommonMultiple(n):
    """
        lcm(a,b,c) = lcm(lcm(a,b),c)
    """
    return reduce(lambda a, b: lcm(a,b),list(range(1, n+1)))

if __name__ == "__main__":
    print(lowestCommonMultiple(20))
