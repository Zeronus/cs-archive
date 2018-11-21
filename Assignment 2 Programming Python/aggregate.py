# Assignment 2, Task 2
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:10 hours (10:01 minutes)

def my_min(p,q,r):
    if p > r and q > r:
        return r
    elif q > p and r > p:
        return p
    elif r > q and p > q:
        return q
    
def my_mean(p,q,r):
    average = (p+q+r)/3
    return average

def my_med(p,q,r):
    if p < q < r or r < q < p:
        return q
    if q < p < r or r < p < q:
        return p
    if q < r < p or p < r < q:
        return r
    
