# Assignment 6, Task 3
# Name: Naran Kongpithaksilp (Tan)
# Collaborators:
# Time Spent: 00:11 hours (11:21 minutes)

def eto(lst):
    if lst == []:
        return []
    else:
        if lst[0]%2 == 0:
            return [lst[0]] + eto(lst[1:])
        else:
            return eto(lst[1:]) + [lst[0]]
        