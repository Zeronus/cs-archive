# Assignment 6, Task 2
# Name: Naran Kongpithaksilp (Tan)
# Collaborators:
# Time Spent: 00:16 hours (16:32 minutes)

def findMe(elt,lst):
    if elt == lst[0]:
        return 0
    elif elt not in lst:
        return None
    else:
        index = findMe(elt,lst[1:])
        return index + 1