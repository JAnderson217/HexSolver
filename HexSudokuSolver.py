import math
import time
#constants to store sudoku options 0-F
sudokuValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def getSudoku():
        #read sudoku from file into grid
        grid = {}
        #f = open("sudoku.txt", "r")
        f = open("HexToSolve.txt", "r")
        for i in range (16):
            for j in range(16):
                grid[i,j] = f.read(1)

        f.close()
        return grid

def isValid(grid, char, x, y):
    #checks if value can be placed here
    #if row/col/square already contains value, cannot be placed there
    for i in range (16):
        if (grid[x,i] == char):
            return False
    for i in range (16):
        if (grid[i,y] == char):
            return False
    #get square coordinates
    squareX = 4*math.trunc(x/4)
    squareY = 4*math.trunc(y/4)
    for i in range (4):
        for j in range (4):
            if (grid[squareX+i,squareY+j] == char):
                return False
    return True

def solve(grid):
    coord = checkEmpty(grid)
    if (coord == False):
        #sudoku is complete
        return True
    else:
        x,y = coord
    for i in range(16):
        if isValid(grid,sudokuValues[i],x,y):
            #tempGrid = grid
            grid[x,y] = sudokuValues[i]
            #grid = solveEasy(grid)
            #recursive, try to finish board
            if solve(grid):
                return True
            #backtrack if wrong
            grid[x,y] = "."
            #grid = tempGrid
            
    return False            

def checkEmpty(Grid):
    #get coordinates of next empty square
    for x in range(16):
        for y in range(16):
            if(Grid[x,y] == "."):
                return x,y
    return False

def getEmpty(Grid):
    #gets empty square with least number of options
    count = 17
    row = 0
    col = 0
    for x in range(16):
        for y in range(16):
            if(Grid[x,y] == "."):
                if(numOptions(Grid,x,y) < 17):
                    row = 0
                    col = 0
    if (countEmptySquares(Grid) == 0):
        return False
    else:
        return x,y

def numOptions(grid,x,y):
    count = 0
    for i in range(16):
        if isValid(grid,sudokuValues[i],x,y):
            count = count + 1
    return count
        
def countEmptySquares(grid):
    count = 0
    for i in range (16):
        for j in range (16):
            if (grid[i,j] == "."):
                count = count+1
    return count

def printSudoku(grid):
    s=""
    for i in range (16):
        for j in range (16):
            s+=grid[i,j]+" "
        s+='\n'
    print(s)

def solveEasy(grid):
    #method to solve all initial solvable squares
    #input all values with only one option
    for i in range (16):
        for j in range(16):
            #loop through each val, check row, col and square to see if only 1 possible value
            if (grid[i,j] == "." and len(checkRow(grid, i,j)) == 1):
                grid[i,j] = checkRow(grid, i,j)[0]
            if (grid[i,j] == "." and len(checkCol(grid, i,j)) == 1):
                grid[i,j] = checkCol(grid, i,j)[0]
            if (grid[i,j] == "." and len(checkSquare(grid, i,j)) == 1):
                grid[i,j] = checkSquare(grid, i,j)[0]
    return grid

def checkRow(grid,x,y):
    #returns all possible options within row
    options = []
    for i in range (16):
        if (isValid(grid, sudokuValues[i],x,y)):
            options.append(sudokuValues[i])        
    return options

def checkCol(grid,x,y):
    #returns all possible options within column
    options = []
    for i in range (16):
        if (isValid(grid, sudokuValues[i],x,y)):
            options.append(sudokuValues[i])        
    return options

def checkSquare(grid,x,y):
    #returns all possible options within square
    options = []
    for i in range (16):
        if (isValid(grid, sudokuValues[i],x,y)):
            options.append(sudokuValues[i])        
    return options

def getOptions(grid):
#gets all valid options for each square
    for i in range (16):
        for j in range (16):
            options = [] 
            if (grid[i,j] == "."):
                for k in range (16):           
                    if (isValid(grid, sudokuValues[k], i,j)):
                        options.append(sudokuValues[k])
            if (len(options) == 1):
                grid[i,j] = options[0]
            print(i, " ", j, " ", options)    
    return grid

def getNakedPairs(grid):
    #sudoku has a naked pair rule, i.e 
    for i in range (16):
        for j in range (16):
                if(grid[i,j] == "."):
                        a = checkRow(grid,i,j)
                        b = checkCol(grid,i,j)
                        c = checkSquare(grid,i,j)
                        options = [x for x in a if x in b and x in c]
                        if (j==0):
                                print("row,col and total options")
                                print(i, ",", j)
                                print(options)
                        if (len(options) == 1):
                                grid[i,j] = options[0]
    return grid
  
def main():
    sudokuGrid = getSudoku()
    printSudoku(sudokuGrid)
    start = time.time()
    #solveEasy(sudokuGrid)
    print()
    solve(sudokuGrid)
    printSudoku(sudokuGrid)        
    total = time.time()-start
    print()
    print("time taken: ", total)

main()
