# Assignment 3, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 01:01 hours

def sumOfDigitsSquared(n):
    """

    >>> sumOfDigitsSquared(7)
    49
    >>> sumOfDigitsSquared(145)
    42
    >>> sumOfDigitsSquared(199)
    163
    """
    digitNumber = 0
    sumSquares = 0
    while digitNumber < len(str(n)):
        sumSquares = sumSquares + int(str(n)[digitNumber])**2
        digitNumber = digitNumber + 1
        if digitNumber == len(str(n)):
            return sumSquares



def isHappy(n):
    """

    >>> isHappy(100)
    True
    >>> isHappy(111)
    False
    >>> isHappy(1234)
    False
    >>> isHappy(989)
    True
    """
    nSquares = sumOfDigitsSquared(sumOfDigitsSquared(n))
    while nSquares != 1 or nSquares != 4:
        happyCalculation = sumOfDigitsSquared(nSquares)
        nSquares = happyCalculation
        if happyCalculation == 1:
            return True
        if happyCalculation == 4:
            return False
            

def kThHappy(k):
    """

    >>> kThHappy(1)
    1
    >>> kThHappy(3)
    10
    >>> kThHappy(11)
    49
    >>> kThHappy(19)
    97
    """
    happyDigit = 1
    number = 1
    if k == 1:
        return 1
    else:
        while happyDigit != k:
            number = number + 1
            if isHappy(number) == True:
                happyDigit = happyDigit + 1
                if happyDigit == k:
                    return number

###########################################################################
# Please don't mind me living down here. I provide some initial testing for
# your code. Run me (e.g., using the run button in Spyder).
###########################################################################
# Simple Tests
###########################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()
###########################################################################
