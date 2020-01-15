def powerDigitSum(exponent):
    """
    As 2 ** 1000 may be a very large number incapable of being stored in an integer type variable.
    This function uses manual calculation to store the digits in an array.
    Such that the array initialized with digit 1 i.e. 2 ** 0,
    is multiplied with 2 for exponent times.
    The overflow for the Most Significant Digit is appended to the list after every multiplication.
    """
    bigNum = [1]
    for i in range(1, exponent + 1):
        count = len(bigNum)
        overflow = 0
        for j in range(count + 1):
            if j < count:
                digit = bigNum[j]
            else:
                digit = 0
                bigNum.append(0)
            digit = 2 * digit + overflow
            if digit > 9:
                digit -= 10
                overflow = 1
            else:
                overflow = 0
            bigNum[j] = digit
    return sum(bigNum)

if __name__ == "__main__":
    print(powerDigitSum(1000))