def specialPythagoreanTriplets(n):
    for i in range(1, n):
        for j in range(i + 1, n - (i + 2)):
            k = n - (i + j)
            if i**2 + j**2 == k**2: return i * j * k

if __name__ == "__main__":
    print(specialPythagoreanTriplets(1000))