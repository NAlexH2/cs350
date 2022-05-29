# CS 350: Homework 8
# Due: Week of 6/2
# Name: 


################################################################
# Sudoku
#
# Sudoku is a game played on a 9x9 grid.
# You are given a partially filled in grid
# and there are 3 rules
# 1. no number can appear twice in the same row
# 2. no number can appear twice in the same column
# 3. no number can appear twice in the same 3x3 grid
#
# You need to write a function that takes in a sudoku board
# and return a solved sudoku board.
#
# example:
# +---+---+---+
# |   |26 |7 1|
# |68 | 7 | 9 |
# |19 |  4|5  |
# +---+---+---+
# |82 |1  | 4 |
# |  4|6 2|9  |
# | 5 |  3| 28|
# +---+---+---+
# |  9|3  | 74|
# | 4 | 5 | 36|
# |7 3| 18|   |
# +---+---+---+
#
# Solution:
# +---+---+---+
# |435|269|781|
# |682|571|49 | was 1 / is 3
# |197|834|562|
# +---+---+---+
# |826|195| 47| was 9 / is 3
# |374|682|915|
# |951|743|628|
# +---+---+---+
# |519|326|874|
# |248|957|136|
# |763|418|259|
# +---+---+---+

def sudoku(board):
    """
    >>> board = [ [4,3,0,2,6,0,7,0,1], \
                  [6,8,0,0,7,0,0,9,0], \
                  [0,0,0,0,0,4,5,0,0], \
                  [8,2,0,1,0,0,0,4,0], \
                  [0,0,4,6,0,2,9,0,0], \
                  [0,5,0,0,0,3,0,2,8], \
                  [0,0,9,3,0,0,0,7,4], \
                  [0,4,0,0,5,0,0,3,6], \
                  [7,0,3,0,1,8,0,0,0] ]
    >>> sudoku(board)
    [[4, 3, 5, 2, 6, 9, 7, 8, 1], [6, 8, 2, 5, 7, 1, 4, 9, 3], [1, 9, 7, 8, 3, 4, 5, 6, 2], [8, 2, 6, 1, 9, 5, 3, 4, 7], [3, 7, 4, 6, 8, 2, 9, 1, 5], [9, 5, 1, 7, 4, 3, 6, 2, 8], [5, 1, 9, 3, 2, 6, 8, 7, 4], [2, 4, 8, 9, 5, 7, 1, 3, 6], [7, 6, 3, 4, 1, 8, 2, 5, 9]]
    """
    # https://anhminhtran235.github.io/sudoku-solver-visualizer/
    # Have a function that gets the current row, another to get the current
    # column, run through until we find a number that not in both lists (sets?) 
    # then proceed when success. THEN verify it doesn't exist already in the 3x3.
    # Want to proceed once we find a known good though, otherwise we go back one
    # and increment and try again while our i != 9, if it hits 9, we roll back
    # another and check again.
    # Inspect that link above to really get an understanding of when to stop or
    # to continue.
    # Check 3x3 squares at the end though instead of when we get there? It feels
    # like this should be done *while* we're in the 3x3 and the 9th position.
    # k = 1
    # i = j = 0
    # while i in range(len(board)):
    #     while j in range(len(board[i])):
    #         if board[i][j] == 0:
    #             while k < 9:
    #                 if checkRowsColumns(board, i, j, k):
    #                     board[i][j] = k
    #                     k += 1
    #                 if k == 9
    #             k = 1
    caught = sBoardrec(board, 0, 0, [])
    return caught

def sBoardrec(board, i, j, result):
    if i > 8:
        if checkBoard(board):
            result = board
            return result
        return board
    
    elif j >= 9:
        result = sBoardrec(board, i+1, 0, result)
        if checkBoard(result):
            return result
        return sBoardrec(board, i+1, 0, result)
    
    if board[i][j] == 0:
        for k in range(1,11):
            if k == 10:
                board[i][j] = 0
                return board
            elif not checkRowsColumns(board,i,j,k):
                board[i][j] = k
                result = sBoardrec(board, i, j+1, result)
                if checkBoard(result):
                    return result
    
    result = sBoardrec(board, i, j+1, result)
    if checkBoard(result):
        return result
    
    return result


def checkRowsColumns(board, r, c, number):
    # check the rows, the columns, using your current number to insert
    # r = current row, c = current column, number = number to see if in either
    rows = []
    columns = []
    for i in range(len(board[r])):
        rows.append(board[r][i])
    
    for i in range (len(board)):
        columns.append(board[i][c])
    
    if number in rows or number in columns:
        return True #meaning that the number existed in either r or c

    return False #Number was not found in either row or column

def checkBoard(board):
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            current3x3 = []
            for k in range(i, i+3):
                for l in range(j, j+3):
                    if board[k][l] == 0:
                        return False
                    if board[k][l] != 0:
                        if board[k][l] in current3x3:
                            return False
                        else:
                            current3x3.append(board[k][l])
    return True

if __name__ == "__main__":
    import doctest
    doctest.testmod()
