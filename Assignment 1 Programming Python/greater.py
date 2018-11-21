# Assignment 1, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time spent: 0:15 hours (15:10 minutes)

numberA = input("Enter a 4-digit integer:")
numberB = numberA[1] + numberA[2] + numberA[3] + numberA[0]
trueOrFalse = int(numberA) > int(numberB)       
print(numberA + ' > '+ numberB + ' ? ' + str(trueOrFalse))