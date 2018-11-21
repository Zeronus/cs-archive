# Assignment 5, Task 3
# Name: Naran Kongpithaksilp (Tan)
# Collaborators: 
# Time Spent: 3:37 hours

def makeUnique(lst): # remove duplicates
    unique = set(lst)
    return list(unique)

def inGridRange(matrix,row,column): # function to check if row/column number exists in the matrix
    return 0 <= row < len(matrix) and 0 <= column < len(matrix[0])

def diag(matrix,r,c): # find diagonal from top left to bottom right
    ans = []
    lst = ''
    row = r
    col = c
    while inGridRange(matrix,row,col):
        lst += (matrix[row][col])
        row += 1
        col += 1
    ans.append(lst)
    return ans

def diagReverse(matrix,r,c): # find diagonal from bottom left to top right
    ans = []
    lst = ''
    row = r
    col = c
    while inGridRange(matrix,row,col):
        lst += (matrix[row][col])
        row -= 1
        col += 1
    ans.append(lst)
    return ans

def checkDiagonal(grid): # check diagonals
    ans = []
    for r in range(0,len(grid)):
        ans.append(diag(grid,r,0))
        ans.append(diagReverse(grid,r,0))
    for c in range(1,len(grid)):
        ans.append(diag(grid,0,c))
        ans.append(diagReverse(grid,len(grid)-1,c))
    return ans

def checkHorizontal(grid): # check horizontal
    horizontal = []
    for rows in grid:
        horizontal.append(''.join(rows))
    return horizontal
        
def checkVertical(grid): # check vertical
    vertical = []
    vertical_temp = []
    for i in range(len(grid[0])):
        for row in grid: 
            vertical_temp.append(row[i])
            if len(vertical_temp) == len(grid):
                vertical.append(''.join(vertical_temp))
                vertical_temp = []
    return vertical

def wordSleuth(grid,words):
    lst = []
    for word in words:
        for diag in checkDiagonal(grid):
            if word in str(diag):
                lst.append(word)
        for hor in checkHorizontal(grid):
            if word in hor:
                lst.append(word)  
        for ver in checkVertical(grid):
            if word in ver:
                lst.append(word)
    return makeUnique(lst)


        

        