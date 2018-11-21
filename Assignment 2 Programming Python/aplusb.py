# Assignment 2, Task 3
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:07 hours (7:31 minutes)

def aplusb(a, b):
    return to_number(a) + to_number(b)

def to_number(x):
    if x == 'one':
        return 1
    elif x == 'two':
        return 2
    elif x == 'three':
        return 3
    else:
        return int(x)
    
