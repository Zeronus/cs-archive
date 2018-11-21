# Assignment 4, Task 3
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 02:47 hours

def readAloud(lst):
    """

    >>> readAloud([])
    []
    >>> readAloud([1,1,1])
    [3, 1]
    >>> readAloud([-1,2,7])
    [1, -1, 1, 2, 1, 7]
    >>> readAloud([3,3,8,-10,-10,-10])
    [2, 3, 1, 8, 3, -10]
    >>> readAloud([3,3,1,1,3,1,1])
    [2, 3, 2, 1, 1, 3, 2, 1]
    """
    answer = []
    lengths = []
    lengthsindex = 0
    counter = 1
    for index in range(len(lst)-1):       
        if lst[index] == lst[index+1]:
            counter += 1
        else:
            lengths.append(counter) 
            counter = 1
        index += 1
        if index == len(lst) - 1:
            lengths.append(counter)
    numberindex = 0
    while lengthsindex < len(lengths):
        answer.append(lengths[lengthsindex])
        answer.append(lst[numberindex])
        if numberindex == len(lst) - 1:
            break
        if lst[numberindex+1] == lst[numberindex]:
            numberindex += 1
        lengthsindex += 1
        numberindex += 1
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
