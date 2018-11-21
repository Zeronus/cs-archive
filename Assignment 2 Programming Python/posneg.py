# Assignment 2, Task 1
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:04 hours (4:23 minutes)

def pos_neg(a, b, negative):
    if negative==False and (a < 0 and b > 0 or a > 0 and b < 0):
        return True
    elif negative==True and (a < 0 and b < 0):
        return True
