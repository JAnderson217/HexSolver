import math
#constants to store sudoku options 0-F
sudokuValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

#Hexadecimal Sudoku solver
def getSudoku():
        #read sudoku from file into grid
        grid = {}
        f = open("sudoku.txt", "r")
        for i in range (16):
            for j in range(16):
                grid[i,j] = f.read(1)

        f.close()
        return grid

def easySolves(grid):
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

def printSudoku(grid):
    for i in range (16):
        for j in range (16):
            print(grid[i,j], end = ' ')
        print()
    
    
def countEmptySquares(grid):
    count = 0
    for i in range (16):
        for j in range (16):
            if (grid[i,j] == "."):
                count = count+1
    return count

def main():
    sudokuGrid = getSudoku()
    printSudoku(sudokuGrid)
    emptySquares = countEmptySquares(sudokuGrid)
    print(emptySquares)
    emptyCount = [emptySquares]
    #loop through all easy solves
    while (len(emptyCount) == 1 or emptyCount[len(emptyCount)-1] != emptyCount[len(emptyCount)-2]):
        sudokuGrid = easySolves(sudokuGrid)
        emptyCount.append(countEmptySquares(sudokuGrid))
    printSudoku(sudokuGrid)
    print(countEmptySquares(sudokuGrid))
    
main()
