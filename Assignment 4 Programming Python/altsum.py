# Assignment 4, Task 2
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:17 hours (17:32 minutes)

def altSum(lst):
    """

    >>> altSum([])
    0
    >>> altSum([1,3,5,2])
    1
    >>> altSum([7,7,7,7])
    14
    >>> altSum([31,4,28,5,71])
    -59

    """
    lstItem = 0
    lstTotal = 0
    k = 2 # Every kth term in the list will be negative
    while lstItem < len(lst):
        if lstItem == k:
            lstTotal -= lst[k]
            k += 2
            lstItem += 1
        else:
            lstTotal += lst[lstItem]
            lstItem += 1
    return lstTotal


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
