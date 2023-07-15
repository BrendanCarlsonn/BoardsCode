
import numpy as np

# Lets create a difficulty levels.
# we use np.array for formatting reasons
sudoku_puzzle_easy = np.array( [
[0,3,0,0,0,0,6,5,2],
[7,6,4,9,0,0,3,8,0],
[0,0,8,6,0,1,0,0,0],
[0,5,0,4,9,0,0,0,7],
[0,0,2,0,8,0,4,6,5],
[3,0,1,0,0,7,0,2,9],
[6,0,7,2,0,0,0,4,0],
[0,9,0,0,5,0,0,1,8],
[2,0,0,3,4,0,7,0,6]
])

sudoku_puzzle_hard = np.array([
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,0,1,9,0,0,5],
[0,0,0,0,0,0,0,0,0]])

sudoku_puzzle_expert = np.array([
[2,0,0,4,0,8,0,0,1],
[0,0,8,0,9,0,0,0,0],
[0,4,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,8,7],
[0,0,2,0,1,0,3,0,0],
[0,0,0,3,0,4,5,0,0],
[3,0,1,8,0,6,7,0,0],
[4,0,0,0,0,0,9,0,0],
[6,0,7,2,0,0,0,0,0]
])

# This array is for displaying the puzzle format

show_sudoku = np.array([
[2,0,0,4,0,8,0,0,1],
[0,0,8,0,9,0,0,0,0],
[0,4,0,0,0,1,0,0,0],
[0,0,0,0,0,0,0,8,7],
[0,0,2,0,1,0,3,0,0],
[0,0,0,3,0,4,5,0,0],
[3,0,1,8,0,6,7,0,0],
[4,0,0,0,0,0,9,0,0],
[6,0,7,2,0,0,0,0,0]
])


print("*********SUDOKU PUZZLE SOLVER*********")
print("Hello and welcome to the sudoku puzzle solver!")
print("You can enter a sudoku puzzle into the file or on the command line.")
print("\n\n")

Userinput = input("Enter 'I' if you would like to input your own puzzle. Press 'A' to skip this step.")

if Userinput == "I":
    #Explaination of input
    print("This is a 9x9 sudoku puzzle solver. Here is an example of the formatting.")
    print("\n 0 3 0 0 0 0 6 5 2 7 6 4 9 0 0 3 8 0 0 0 8 6 0 1 0 0 0 0 5 0 4 9 0 0 0 7 0 0 2 0 8 0 4 6 5 3 0 1 0 0 7 0 2 9 6 0 7 2 0 0 0 4 0 0 9 0 0 5 0 0 1 8 2 0 0 3 4 0 7 0 6\n")
    #These are the rows and columns
    R = 9
    C = 9
    print("Enter the entries in a single line (separated by space): ")
# User input of entries in a 
# single line separated by space
# Now to turn the input into an array
    entries = list(map(int, input().split()))
# For printing the matrix
    sudoku_puzzle = np.array(entries).reshape(R, C)
    print("\nHere is your puzzle\n\n")
    print(sudoku_puzzle_expert)
    print("\nHere is the solution\n\n")



else:
    #Here are the example puzzles
    print("\nWhat difficulty would you like to see solved?\n")
    #User input for the difficulty
    Userinput = input("Please enter'E' for easy, 'H' for hard, and 'X' for expert.")
    if Userinput == "E":
        print("\n\n")
        # Change the sudoku_puzzle to the selected difficulty
        sudoku_puzzle = sudoku_puzzle_easy
        print("\nYou chose this puzzle\n")
        #Print the unsolved puzzle
        print(sudoku_puzzle_easy)
    elif Userinput == "H":
        print("\n\n")
        sudoku_puzzle = sudoku_puzzle_hard
        print("\nYou chose this puzzle\n")
        print(sudoku_puzzle_hard)
    else:
        print("\n\n")
        sudoku_puzzle = sudoku_puzzle_expert
        print("\nYou chose this puzzle\n")
        print(show_sudoku)
        print("\n\n")
        print("\nAnd here is the solution!\n")

        
#Function for solving the puzzle
def possible(Row, Column, Num):
    #Make the sudoku_puzzle global
    global sudoku_puzzle
    #Is the Num appearing in the given Row
    for i in range(0,9):
        if sudoku_puzzle[Row][i] == Num:
            return False

    #Is the Num appearing in the given Column
    for i in range(0,9):
        if sudoku_puzzle[i][Column] == Num:
            return False
    
    #Is the Num appearing in the given square
    x0 = (Column // 3) * 3
    y0 = (Row // 3) * 3
    for i in range(0,3):
        for j in range(0,3):
            if sudoku_puzzle[y0+i][x0+j] == Num:
                return False

    return True

def solution():
    global sudoku_puzzle
    for Row in range(0,9):
        for Column in range(0,9):
            if sudoku_puzzle[Row][Column] == 0:
                for Num in range(1,10):
                    if possible(Row, Column, Num):
                        sudoku_puzzle[Row][Column] = Num
                        solution()
                        sudoku_puzzle[Row][Column] = 0

                return
      
    print(np.matrix(sudoku_puzzle))
    input('More possible solutions')
# Run the solver
solution()