# Assignment 3, Task 7
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:27 hours

def isAnagram(word1, word2):
    """

    >>> isAnagram("iceman","cinema")
    True
    """
    letter = 0
    lengthWord = 0
    while lengthWord <= len(word1):
        if word1[letter] in (word2):
            letter += 1
            lengthWord += 1
            if lengthWord == len(word1):
                return True
        else:
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
