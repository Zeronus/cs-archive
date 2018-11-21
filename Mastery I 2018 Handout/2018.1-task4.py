# PROBLEM 4

def dateToNumber(x): 
# Convert '0x' date to an integer
    if x[0] == '0':
        dateInt = int(x[1])
    else:
        dateInt = int(x)
    return dateInt    


def dateToStr(x):
# Convert integer back to a '0x' string to be used in answer
    if len(str(x)) < 2:
        return '0' + str(x)
    return str(x)

def month_range(frm,until):
    answer = [frm] # Answer list begins with starting date    
    # [0:2] extracts the date
    date = dateToNumber(frm[0:2]) 
    untilDate = dateToNumber(until[0:2]) 
    # [3:7] extracts the year
    frmYear = int(frm[3:7]) 
    untilYear = int(until[3:7])
    dateAndYear = frm
    if untilYear < frmYear:  # If end date is less than starting date
        return [] # If end date is less than starting date
    elif untilDate < date and untilYear == frmYear: # If end date is less than starting date
        return [] # If end date is less than starting date
    while dateAndYear != until: # Loops until calculated dates reach the end date
        date += 1 
        if date > 12: # If date is bigger than 12, resets the dates to 1
            date = 1
            frmYear += 1
        dateAndYear = dateToStr(date) + '/' + str(frmYear) # Adds strings to form xx/xxxx format
        answer.append(dateAndYear)
    return answer

assert month_range('01/2017','03/2017') == ['01/2017', '02/2017', '03/2017']
assert month_range('11/2017','02/2018') == ["11/2017", "12/2017", "01/2018", "02/2018"]
assert month_range("11/2017", "12/2014") == []