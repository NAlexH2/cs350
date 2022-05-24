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
    pass

if __name__ == "__main__":
    import doctest
    doctest.testmod()
