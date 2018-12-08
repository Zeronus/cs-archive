# Problem 5 : Sudoku

def getColumns(grid):
    ans = []
    lst = []
    for column in range(len(grid[0])):
        for row in range(len(grid)):
            lst.append(grid[row][column])
        ans.append(sorted(lst))
        lst = []
    return ans

def getBoxes(grid):
    ans = []
    box = []
    for x in range(0,9,3):
        for y in range(0,9,3):
            for i in range(3):
                for j in range(3):
                   box.append(grid[y+i][x+j])
            ans.append(sorted(box))
            box = []
    return ans

def sudokuSolved(grid):
    rows = [sorted(i) for i in grid]
    columns = getColumns(grid)
    boxes = getBoxes(grid)
    condition = {1,2,3,4,5,6,7,8,9}
    for row in rows:
        if set(row) != condition:
            return False
    for column in columns:
        if set(column) != condition:
            return False
    for box in boxes:
        if set(box) !=condition:
            return False
    return True
        
grid = [[5,3,4,6,7,8,9,1,2],
        [6,7,2,1,9,5,3,4,8],
        [1,9,8,3,4,2,5,6,7],
        [8,5,9,7,6,1,4,2,3],
        [4,2,6,8,5,3,7,9,1],
        [7,1,3,9,2,4,8,5,6],
        [9,6,1,5,3,7,2,8,4],
        [2,8,7,4,1,9,6,3,5],
        [3,4,5,2,8,6,1,7,9]]

    
    
    
    
                

        
        
            
        
    

