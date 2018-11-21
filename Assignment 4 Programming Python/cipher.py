# Assignment 4, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:06 hours (6:12 minutes)

def enc(msg, key):
    """

    >>> enc("abc",2)
    'acb'
    >>> enc("monosodium glutamate", 7)
    'mitouanmmo asgtoledu'
    >>> enc("polylogarithmicsubexponential", 3)
    'pygimseonaolatiuxntllorhcbpei'

    """
    answer = ""
    index = 0
    row = 0
    while len(answer) != len(msg):
        while index < len(msg):
            answer += msg[index]
            index += key
        row += 1
        index = row
    return answer
    
        

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
