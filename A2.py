def divide(ourDividend, ourDivisor):
    sign = (-1 if ((ourDividend < 0) ^ (ourDivisor < 0)) else 1)
    ourDividend = abs(ourDividend)
    ourDivisor = abs(ourDivisor)
    quotientNumber = 0
    tempNumber = 0
    for i in range(31, -1, -1):
        if (tempNumber + (ourDivisor << i) <= ourDividend):
            tempNumber += ourDivisor << i
            quotientNumber |= 1 << i
    return sign * quotientNumber
divide()