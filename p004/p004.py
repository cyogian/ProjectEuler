def isPalindrome(s):
    palindrome = True
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i -1]:
            palindrome = False
            break
    return palindrome

def largestPalindromeProduct(n):
    maxN = int("9" * n)
    minN = int("1" + "0" * (n - 1))
    s = 0
    for i in range(maxN, minN, -1):
        for j in range(i, minN, -1):
            product = i * j
            if isPalindrome(str(product)):
                if product > s:
                    s = product
                break
    return s
if __name__ == "__main__":
    print(largestPalindromeProduct(3))

