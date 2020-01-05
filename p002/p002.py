def fib(n):
    t1 = 1
    t2 = 2
    sequence = []
    for i in range(n):
        if t1 % 2 == 0:
            sequence.append(t1)
        temp = t1
        t1 = t2
        t2 += temp
    return sum(sequence)
