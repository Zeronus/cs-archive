# PROBLEM 3

def isPrime(x):
    if x < 2:
        return False
    for d in range(2,x):
        if x%d == 0:
            return False
    return True

def sumOfDigitsSquared(n):
    digitNumber = 0
    sumSquares = 0
    while digitNumber < len(str(n)):
        sumSquares = sumSquares + int(str(n)[digitNumber])**2
        digitNumber += 1
    return sumSquares

def isHappy(n):
    nSquares = sumOfDigitsSquared(sumOfDigitsSquared(n))
    while True:
        happyCalculation = sumOfDigitsSquared(nSquares)
        nSquares = happyCalculation
        if happyCalculation == 1:
            return True
        if happyCalculation == 4:
            return False

def sumHP(m):
    lst = []
    for i in range(2,m + 1):
        if isHappy(i) and isPrime(i):
            lst.append(i)
    return sum(lst)

assert sumHP(10)==7
assert sumHP(19)==39
assert sumHP(40)==93
assert sumHP(1010)==14836