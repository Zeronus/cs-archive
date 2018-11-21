# Assignment 3, Task 6
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:04 hours (4:32 minutes)

def robust_avg(lst):
    """

    >>> round(robust_avg([3, 1, 2, 5, 9, 11, 4]), 4)
    4.6
    """
    lst.remove(min(lst))
    lst.remove(max(lst))
    return sum(lst)/len(lst)


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
