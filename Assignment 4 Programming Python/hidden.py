# Assignment 4, Task 4
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:05 hours (5:12 minutes)

def is_hidden(s, t):
    """
    >>> is_hidden("welcometothehotelcalifornia","melon")
    True

    >>> is_hidden("welcometothehotelcalifornia","space")
    False

    >>> is_hidden("TQ89MnQU3IC7t6","MUIC")
    True

    >>> is_hidden("VhHTdipc07","htc")
    False

    >>> is_hidden("VhHTdipc07","hTc")
    True
    """
    word = ''
    tIndex = 0
    for i in s:
        if i in t[tIndex]:
            word += i
            tIndex += 1
        if word == t:
            return True
    return False

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
