# Assignment 2, Task 6
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 01:37 hours

def kthDigit(x,b,k):
    if k == 0:
        return x%b
    if k == 1:
        division = x//b
        remainder = division%b
        return remainder
    if k > 1:
       numberOfDivisions = 1
       division = x//b
       while numberOfDivisions != k:
           remainder = division%b
           numberOfDivisions = numberOfDivisions + 1
           division = division//b
           remainder = division%b
           if numberOfDivisions == k:
               return remainder
           

           
       
        
            

        
        
        
    
    
    
                 