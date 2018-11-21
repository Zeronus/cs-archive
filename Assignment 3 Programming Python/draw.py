# Assignment 3, Task 2
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:47 hours

def triangle(k):
    """

    >>> triangle(1)
    *
    >>> triangle(3)
    ##*##
    #***#
    *****

    """
    numberOfLoops = 0
    factor = 0
    while numberOfLoops < k:      
        triangleBase = k + factor
        factor = factor + 1
        numberOfLoops = numberOfLoops + 1
        if numberOfLoops == k:
            triangleBase = triangleBase
    lineDifference = triangleBase - 2*(k-1)
    while lineDifference < triangleBase + 1:
        blankSpace = (triangleBase - lineDifference)//2
        print(('#'*blankSpace)+('*'*lineDifference)+('#'*blankSpace))
        lineDifference = lineDifference + 2

def diamond(k):
    """

    >>> diamond(2)
    ##*##
    #***#
    #***#
    ##*##
    >>> diamond(4)
    ####*####
    ###***###
    ##*****##
    #*******#
    #*******#
    ##*****##
    ###***###
    ####*####

    """
    numberOfLoops = 0
    factor = 0
    while numberOfLoops < k:      
        triangleBase = k + factor
        factor = factor + 1
        numberOfLoops = numberOfLoops + 1
        if numberOfLoops == k:
            triangleBase = triangleBase
    lineDifference = triangleBase - 2*(k-1)
    blankSpace = ((triangleBase - lineDifference)//2) + 1
    while lineDifference < triangleBase + 1:        
        print(('#'*blankSpace)+('*'*lineDifference)+('#'*blankSpace))
        lineDifference = lineDifference + 2
        blankSpace = blankSpace - 1
    while lineDifference > 1:
        blankSpace = blankSpace + 1
        lineDifference = lineDifference - 2
        print(('#'*blankSpace)+('*'*lineDifference)+('#'*blankSpace))        
        


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
