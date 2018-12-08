# Problem 1: Secret Code
# find a number

def isNumber(n): # Function to check if a str is a number 
    if n in '1234567890':
        return True
    return False

def isUpper(letter): # Function to check if letter is uppercase
    if letter == letter.upper():
        return True
    return False

def isLower(letter): # Function to check if letter is lowercase
    if letter == letter.lower():
        return True
    return False

def conditionsCheck(upper,lower): # Function to check if both conidtions are met
    up_con = False # Variable, if the uppercase condition is met
    low_con = False # Variable, if the lowercase condition is met
    #Conditional Statement : if length > 2 = checks that only the last 2 are uppercase
    if len(upper) > 2:
        if isUpper(upper[-1]) and isUpper(upper[-2]) and isLower(upper[-3]):
            up_con = True
    #Elif just check if they are uppercase and if the length is 2
    elif len(upper) == 2 and isUpper(upper[-1]) and isUpper(upper[-2]):
        up_con = True
    #Conditional Statement : if length > 2 = checks that only the first 2 are lowercase
    if len(lower) > 2:
        if isLower(lower[0]) and isLower(lower[1]) and isUpper(lower[2]):
            low_con = True
    #elif just check if they are lower case and if the length is 2
    elif len(lower) == 2 and isLower(lower[0]) and isLower(lower[1]):
        low_con = True
    if up_con and low_con: # Function returns True if both conditions are met
        return True
    else:
        return False
    
def split(st):
    start_index = 0 # Starting index for the slice
    lst = [] # Will contain [str before number,number]
    for index in range(len(st)): # Loop through str
        if isNumber(st[index]):
            extract = st[start_index:index]
            lst.append(extract) # Append the strings before the number
            lst.append(st[index]) # Append the number
            start_index = index + 1 # Set the index to the index after the number
    lst.append(st[start_index:len(st)]) # Append the strings after the last number
    return lst     

def secretCode(st):
    lst = split(st)
    ans = []
    for item in range(len(lst)):
        if item%2 == 1: # numbers are always an odd index unless they are next to each other
            upper = lst[item-1]
            lower = lst[item+1]
            if conditionsCheck(upper,lower): # If conditions are met, append numbers to list
                ans.append(lst[item]) 
    return ''.join(ans) # Join all the numbers in the list together
          
assert secretCode('TT4za7GH5xpNHD1tyu8XQ9vg') == '459'
assert secretCode('AAAAAAA4aaaaaBB5bb') == '5'
assert secretCode('XX4xx6kk') == '4'
assert secretCode('MMM555MMM') == ''
assert secretCode('sw5DW2ccF7123XX9xx8') == '29'
assert secretCode('123abc123ABC123aBC1abC') == '1'

