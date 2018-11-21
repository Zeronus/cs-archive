# Assignment 2, Task 6
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:11 hours (11:43 minutes)

def phoneWord2Num(word):
    if len(word) == 7:
        phoneWordResult = conv(word[0])+conv(word[1])+conv(word[2])+conv(word[3])+conv(word[4])+conv(word[5])+conv(word[6])
        return int(phoneWordResult)
    else:
        return 'You must enter a string of length 7 letters'


def conv(letter):
    if letter in 'ABCabc':
        return '2'
    elif letter in 'DEFdef':
        return '3'
    elif letter in 'GHIghi':
        return '4'
    elif letter in 'JKLjkl':
        return '5'
    elif letter in 'MNOmno':
        return '6'
    elif letter in 'PQRSpqrs':
        return '7'
    elif letter in 'TUVtuv':
        return '8'
    elif letter in 'WXYZwxyz':
        return '9'
    