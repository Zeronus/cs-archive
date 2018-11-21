# Assignment 3, Task 3
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:10 hours (10:02 minutes)

def allMultiplesOfK(k, lst):
    """

    >>> allMultiplesOfK(4, [1,10,20])
    False
    >>> allMultiplesOfK(3, [81,3,24])
    True
    >>> allMultiplesOfK(11, [])
    True
    """
    numberOfLoops = 0
    numberOfMultiples = 0
    listDigit = 0
    if len(lst) > 0:
        while numberOfLoops < len(lst) + 1:
            if lst[listDigit]%k == 0:
                numberOfMultiples = numberOfMultiples + 1
                listDigit = listDigit + 1
                if numberOfMultiples == len(lst):
                    return True
            else:
                return False
    if len(lst) == 0:
        return True


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
