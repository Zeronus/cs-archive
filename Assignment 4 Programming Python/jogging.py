# Assignment 4, Task 6
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: None
# Time Spent: 00:23 hours

log_book = [
    "cycling;time:1,49;distance:2",
    "jogging;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "jogging;time:36,25;distance:5.3",
    "hiking;time:106,01;distance:8.29"
]
log_book2 = [
    "cycling;time:1,49;distance:2",
    "joggingAdventure;time:40,11;distance:6",
    "swimming;time:1,49;distance:1.2",
    "joggingTime;time:36,25;distance:5.3",
    "running;time:12,01;distance:6.5"
]
def parse_time(line):
    splitLine = line.split(';')
    time = splitLine[1][5:] 
    minutes = time.split(',')[0]
    seconds = time.split(',')[1]
    if seconds[0] == 0:
        seconds = seconds[1]
    return float(minutes)*60 + float(seconds)

def parse_dist(line):
    splitLine = line.split(';')
    distance = splitLine[2][9:]
    return float(distance)*1000

def jogging_average(activities):
    """

    >>> round(jogging_average(log_book), 4)
    2.4587
    """
    lst = []
    for logentry in activities:
        if logentry[0:8] == 'jogging;':
            lst.append(logentry)
    if len(lst) == 0:
        return 0
    lstindex = 0
    distance = 0
    time = 0
    while lstindex < len(lst):
        time += parse_time(lst[lstindex])
        distance += parse_dist(lst[lstindex])
        lstindex += 1
    return distance/time




###########################################################################
# Please don't mind me living down here. I provide some initial testing for
# your code. Run me (e.g., using the run button in Spyder).
###########################################################################
# Simple Tests
###########################################################################
if __name__ == "__main__":
    import doctest
    doctest.testmod()
###########################################################################
