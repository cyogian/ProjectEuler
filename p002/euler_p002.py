def fib(n):
    t1 = 1
    t2 = 2
    fsum = 0
    while(t1 <= n):
        if t1 % 2 == 0:
            fsum += t1
        temp = t1
        t1 = t2
        t2 += temp
    return fsum

if __name__ == "__main__":
    print(fib(4000000))
