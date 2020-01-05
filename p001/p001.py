# Sum of All Multiples of 3 and 5 under n
def multisum(n):
    condition = lambda x: x % 5 == 0 or x % 3 == 0
    return sum(filter(condition, range(3, n)))

if __name__ == "__main__":
    print(multisum(1000))
    