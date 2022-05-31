import math
import time
#constant to store sudoku options 0-F
sudokuValues = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]

def getSudoku(file):
        #read sudoku from file into grid
        grid = {}
        f = open(file, "r")
        for i in range (16):
            for j in range(16):
                grid[i,j] = f.read(1)

        f.close()
        return grid

def checkRow(grid, char, x):
    #return true if value is in row
    for i in range(16):
        if(grid[x,i] == char):
            return True
    return False

def checkCol(grid, char, y):
    #return true if value is in column
    for i in range(16):
        if(grid[i,y] == char):
            return True
    return False

def checkSquare(grid, char, x, y):
    #return true if value is in square
    for i in range(4):
        for j in range(4):
            if(grid[(i+x),(j+y)] == char):
                return True
    return False

def isValid(grid, char, x, y):
    #return false if value is not in row, column or square, i.e. can be placed here
    #check Row/Col/Square all return true if value is present, need all to be false
    rowValid = not checkRow(grid, char, x)
    colValid = not checkCol(grid, char, y)
    boxValid = not checkSquare(grid, char, (x - x % 4), (y - y % 4))
    return (rowValid and colValid and boxValid)

def checkEmpty(grid):
    #get coordinates of next empty square
    for i in range(16):
        for j in range(16):
            if(grid[i,j] == "."):
                return i,j
    return False

def getNext(grid):
    #gets next coordinates of square, with lowest number of possible values
    #arrays to store coordinates of empty squares and number of options in square
    emptySquares = []
    numOptions = []
    #loop through add all empty squares and number of options in each square
    for x in range(16):
        for y in range(16):
            if(grid[x,y] == "."):
                emptySquares.append((x,y))
                count = 0
                for i in range(0,16):
                    if (isValid(grid, sudokuValues[i], x, y)):
                        count = count+1
                numOptions.append(count)
    #sort both arrays with lowest number of options first
    numOptions, emptySquares = zip(*sorted(zip(numOptions, emptySquares)))
    #return coordinates
    return emptySquares[0]

def solve(grid):
    if (checkEmpty(grid) == False):
        #sudoku is complete
        return True
    #get coordinates of next square
    x,y = getNext(grid)
    #try all possible values until sudoku complete 
    for i in range(16):
        if (isValid(grid, sudokuValues[i], x, y)):
            grid[x,y] = sudokuValues[i]
            #recursive, try to finish board
            if solve(grid):     
                return True
            #backtrack if wrong
            grid[x,y] = "."

    return False

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
            count = 0
            tempVal = "."
            for k in range(16):
            #check if only one value possible
                if isValid(grid, sudokuValues[k], i, j):
                    count = count + 1
                    tempVal = sudokuValues[k]
            if count == 1:
                grid[i,j] = tempVal
    return grid 

def main(file):
    sudokuGrid = getSudoku(file)
    printSudoku(sudokuGrid)
    start = time.time()
    #solveEasy(sudokuGrid)
    solve(sudokuGrid)
    printSudoku(sudokuGrid)        
    total = time.time()-start
    print("time taken: ", total)
    print()

main("sudoku.txt")
main("sudoku2.txt")
main("sudoku3.txt")
