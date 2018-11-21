# Assignment 5, Task 1
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: 
# Time Spent: 00:37 hours

def charHistogram(filename):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        count = 0
        fh = open(filename,'r')
        for letter in fh.read():   
            if letter.lower() == i:
                count += 1
        if count > 0:
            print(i,'+'*count)
                