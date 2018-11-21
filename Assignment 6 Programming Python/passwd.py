# Assignment 6, Task 1
# Name: Naran Kongpithaksilp (Tan)
# Collaborators:
# Time Spent: 00:10 hours (10:13 minutes)

def passwordOK(p_str):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    symbols = '$#@'
    numbers = '0123456789'
    upper = 0 # number of uppercase letters
    lower = 0 # number of lowercase
    sym = 0 # number of symbols
    num = 0 # number of numbers
    if len(p_str) > 16 or len(p_str) < 6:
        return False
    for index in range(1,len(p_str)):
        if p_str[index-1] == p_str[index]: # check if next letter is the same
            return False
        if p_str[index-1] in alphabet: # check for lower case in password
            lower += 1
        if p_str[index-1] in alphabet.upper(): # check for upper
            upper += 1
        if p_str[index-1] in symbols: # check for symbols
            sym += 1
        if p_str[index-1] in numbers: # check for numbers
            num += 1
    if upper >= 1 and lower >= 1 and sym >= 1 and num >= 1: # if password has at least one of each character type
        return True
    else:
        return False