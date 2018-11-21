# Assignment 4, Task 1
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:07 hours (7:21 minutes)

def rev_str(s):
    """Returns the reverse of the input string s, without using the built-in
    reverse mechanism.

    >>> rev_str("nowhere")
    'erehwon'

    >>> rev_str("gnimmargorpevoli")
    'iloveprogramming'

    >>> rev_str("y")
    'y'
    """
    if len(s) == 0:
        return s
    strItem = len(s) - 1
    reversedString = s[len(s)-1]
    while strItem > 0:
        strItem -= 1
        reversedString = reversedString + s[strItem]
    return reversedString

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
