# Assignment 3, Task 1
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:03 hours (3:12 minutes)

def powerLoop(upto):
    """

    >>> powerLoop(0)
    0 1
    >>> powerLoop(4)
    0 1
    1 11
    2 20
    3 18
    4 97
    """
    for i in range(0,upto+1):
        remainder = (11**i)%101
        print(i,remainder)

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
