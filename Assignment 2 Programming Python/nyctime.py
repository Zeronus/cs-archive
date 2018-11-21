# Assignment 2, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:34 hours

def nycHour(londonHour):
    nycTime = (londonHour + 12) - 5
    if londonHour >= 0 and londonHour < 5:
        return (str(nycTime) + 'pm')
    elif londonHour > 5 and londonHour < 17:
        nycTime = londonHour - 5
        return (str(nycTime) + 'am')
    elif londonHour > 17 and londonHour <= 23:
        nycTime = (londonHour - 12) - 5
        return (str(nycTime) + 'pm')
    if londonHour == 5:
        return (str(nycTime) + 'am')
    if londonHour == 17:
        nycTime = londonHour - 5
        return (str(nycTime) + 'pm')
    