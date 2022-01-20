import numpy as np
import time

sudokuGrid = np.array([
[9,8,3,0,1,0,0,0,0],
[0,0,0,6,0,0,8,0,0],
[0,0,0,2,5,0,0,9,0],
[0,4,1,0,0,7,0,0,2],
[0,0,0,0,0,0,0,0,0],
[7,9,0,0,8,0,0,0,0],
[0,1,2,0,0,0,9,0,0],
[0,0,0,0,0,0,0,0,7],
[3,0,8,0,0,0,4,1,0]])

def solveSudokuGrid():
    global sudokuGrid
    for y in range(9):
        for x in range(9):
            if(sudokuGrid[y][x] == 0):
                for num in range(1,10):
                    if((checkValidInput(x, y, num)) == 1):
                        sudokuGrid[y][x] = num
                        solveSudokuGrid()
                    sudokuGrid[y][x] = 0
                return
    print(sudokuGrid)

def checkValidInput(x, y, num):
    for col in range(9):
        if(sudokuGrid[y][col] == num):
            return 0

    for row in range(9):
        if(sudokuGrid[row][x] == num):
            return 0
   
    xBoxStart = (x // 3) * 3
    yBoxStart = (y // 3) * 3
    for X in range(xBoxStart, xBoxStart + 3):
        for Y in range(yBoxStart, yBoxStart + 3):
            if((sudokuGrid[Y][X]) == num):
                return 0
            
    return 1

def timer():
    start = time.time()
    solveSudokuGrid()
    end = time.time()
    print("Time is", end-start, "seconds")
    
timer()