# Problem 3 : Ham's Apple Tree
grid1 =([['O','O','H'],  
         ['T','O','O'],
         ['O','O','O']]) 

grid2 =([['H','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','O'],
         ['O','O','O','T']])

def locate(grid,item):
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == item:
                return column,row

def computeMove(board):
    ham_col,ham_row = locate(board,'H')
    tree_col,tree_row = locate(board,'T')
    distance = abs(ham_col-tree_col) + abs(ham_row-tree_row)
    return distance
    
assert computeMove(grid1) == 3
assert computeMove(grid2) == 10