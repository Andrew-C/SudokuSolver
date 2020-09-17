# Sudoku solver utilizing backtracking

board = [
    [0, 3, 0, 0, 1, 0, 0, 6, 0],
    [7, 5, 0, 0, 3, 0, 0, 4, 8],
    [0, 0, 6, 9, 8, 4, 3, 0, 0],
    [0, 0, 3, 0, 0, 0, 8, 0, 0],
    [9, 1, 2, 0, 0, 0, 6, 7, 4],
    [0, 0, 4, 0, 0, 0, 5, 0, 0],
    [0, 0, 1, 6, 7, 5, 2, 0, 0],
    [6, 8, 0, 0, 9, 0, 0, 1, 5],
    [0, 9, 0, 0, 4, 0, 0, 3, 0]
]
def printBoard(board):
    cLine = 0   # used to count the column
    rLine = 0   #used to count the row

    for row in board:
        cLine = 0
        if rLine % 3 is 0:
            print("-------------------------------")
        rLine += 1

        for col in row:
            if cLine is 0 or cLine is 3:
                print("|", end = '')
                cLine = 1
            else:
                cLine += 1
            if col is 0:
                print(" - " , end = '')
            else:
                print(" " + str(col) + " " , end = '')

        print("|")
    print("-------------------------------")

def solve(board):
    return 0

printBoard(board)