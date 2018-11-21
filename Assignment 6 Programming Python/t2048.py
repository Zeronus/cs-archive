# Assignment 6, Task 5
# Name: Naran Kongpithaksilp (Tan)
# Collaborators:
# Time Spent: 3:12 hours
# ----------------------------------


# Checks whether a given board has any 
# possible move left. If no more moves,  
# return True. Otherwise return False.
def isGameOver(board):
    if doKeyUp(board) == (False,board) and doKeyDown(board) == (False,board) and doKeyLeft(board) == (False,board) and doKeyRight(board) == (False,board):
        return True
    else:
        return False

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Up' key.
def doKeyUp(board):
    new_board = []
    gridlist = []
    for column in range(len(board[0])):
        temp = []
        count = 0
        for row in range(len(board)):
            if board[row][column] == ' ':
                count += 1
            else:
                temp.append(board[row][column])
        for x in range(count):
            temp.append(' ')
        gridlist.append(temp)
        
    for lst in gridlist:
        index = 1
        while index < len(gridlist):
            if lst[index] == ' ':
                break
            if lst[index-1] == lst[index]:
                new_value = int(lst[index]) + int(lst[index-1])
                lst[index] = str(new_value)
                lst[index-1] = ' '
            index += 1
    
    ans = []       
    for item in gridlist:
        temp2 = []
        count2 = 0
        for i in range(len(item)):
            if item[i] == ' ':
                count2 += 1
            else:
                temp2.append(item[i])
        for y in range(count2):
            temp2.append(' ')
        ans.append(temp2)
    
    for i in range(len(ans[0])):
        newboard_row = []
        for item in ans:
            newboard_row.append(item[i])
        new_board.append(newboard_row)
    if new_board == board:
        return False,new_board
    else:
        return True,new_board

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Down' key.
def doKeyDown(board):
    new_board = []
    gridlist = []
    for column in range(len(board[0])):
        temp = []
        count = 0
        for row in range(len(board)):
            if board[row][column] == ' ':
                count += 1
            else:
                temp.append(board[row][column])
        for x in range(count):
            temp.insert(0,' ')
        gridlist.append(temp)
        
    for lst in gridlist:
        index = len(lst) - 2
        while index >= 0:
            if lst[index] == ' ':
                break
            if lst[index+1] == lst[index]:
                new_value = int(lst[index]) + int(lst[index+1])
                lst[index] = str(new_value)
                lst[index+1] = ' '
            index -= 1
    
    ans = []       
    for item in gridlist:
        temp2 = []
        count2 = 0
        for i in range(len(item)):
            if item[i] == ' ':
                count2 += 1
            else:
                temp2.append(item[i])
        for y in range(count2):
            temp2.insert(0,' ')
        ans.append(temp2)
    
    for i in range(len(ans[0])):
        newboard_row = []
        for item in ans:
            newboard_row.append(item[i])
        new_board.append(newboard_row)
    if new_board == board:
        return False,new_board
    else:
        return True,new_board

# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Left' key.
def doKeyLeft(board):
    new_board = []
    for row in board:
        lst = []
        count = 0
        
        for i in range(len(row)):
            if row[i] == ' ':
                count += 1
            else:
                lst.append(row[i])
        for x in range(count):
            lst.append(' ')
        
        index = 1
        
        while index < len(lst):
            if lst[index] == ' ':
                break
            if lst[index-1] == lst[index]:
                new_value = int(lst[index]) + int(lst[index-1])
                lst[index] = str(new_value)
                lst[index-1] = ' '
            index += 1
        
        ans = []
        count2 = 0
        
        for i in range(len(lst)):
            if lst[i] == ' ':
                count2 += 1
            else:
                ans.append(lst[i])
        for x in range(count2):
            ans.append(' ')
        new_board.append(ans)
    if new_board == board:
        return False,new_board
    else:
        return True,new_board


# Returns a tuple (changed, new_board) 
# where:
#  changed - a boolean indicating if
#            the board has changed.
#  new_board - the board after the user
#              presses the 'Right' key.
def doKeyRight(board):
    new_board = []
    for row in board:
        lst = []
        count = 0
        
        for i in range(len(row)):
            if row[i] == ' ':
                count += 1
            else:
                lst.append(row[i])
        for x in range(count):
            lst.insert(0,' ')
        
        index = len(lst) - 2
        
        while index >= 0:
            if lst[index] == ' ':
                break
            if lst[index+1] == lst[index]:
                new_value = int(lst[index]) + int(lst[index+1])
                lst[index] = str(new_value)
                lst[index+1] = ' '
            index -= 1
        
        ans = []
        count2 = 0
        
        for i in range(len(lst)):
            if lst[i] == ' ':
                count2 += 1
            else:
                ans.append(lst[i])
        for x in range(count2):
            ans.insert(0,' ')
        new_board.append(ans)
    if new_board == board:
        return False,new_board
    else:
        return True,new_board

# Returns a list of tuples (row, col)
# indicating where the empty spots are
def emptyPos(board):
    a = []
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] == ' ':
                pos = row,column
                a.append(pos)
    return a
                


# Returns a dictionary mapping each tile 
# value on the board to its count (i.e.,
# how many times it appears on the board)
def hist(board):
    d = dict()
    s = set()
    counter = 0
    for row in board:
        for column in row:
            if column != ' ':
                s.add(column)
    for item in s:
        for row in board:
            counter += row.count(item)
        d[int(item)] = int(counter)
        counter = 0
    return d
