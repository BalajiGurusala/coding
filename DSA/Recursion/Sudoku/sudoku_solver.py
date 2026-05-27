'''
Given a partially filled two-dimensional array, fill all the unfilled cells such that each row, each column and each 3 x 3 subgrid (as highlighted below by bolder lines) has every digit from 1 to 9 exactly once.

Unfilled cells have a value of 0 on the given board.

Input:
{
"board": [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]
}

Output:

[
[8, 4, 9, 1, 6, 3, 5, 7, 2],
[3, 1, 5, 2, 8, 7, 4, 9, 6],
[7, 6, 2, 4, 9, 5, 1, 8, 3],
[1, 5, 3, 9, 4, 6, 7, 2, 8],
[2, 8, 7, 3, 5, 1, 6, 4, 9],
[4, 9, 6, 8, 7, 2, 3, 5, 1],
[5, 7, 8, 6, 1, 9, 2, 3, 4],
[6, 3, 4, 5, 2, 8, 9, 1, 7],
[9, 2, 1, 7, 3, 4, 8, 6, 5]
]

'''

def solve_sudoku_puzzle(board):
    """
    Args:
     board(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    sudoku_helper(board)
    return board

def sudoku_helper(board):
    
    #recursive case
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == 0:
                for num in range(1,10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if sudoku_helper(board):
                            return True
                        else:
                            board[row][col] = 0
                return False
                

    return True

def is_valid(board, row, col, currDigit):
    #check if the newly added digit is a duplicate in the same column
    for r in range(9):
        if currDigit == board[r][col]:
            return False

    #check if the newly added digit is a duplicate in the same row
    for c in range(9):
        if currDigit == board[row][c]:
            return False

    #check if the newly added digit is a duplcaite within 3*3 subgrid
    gridColNum = (col//3) * 3
    gridRowNum = (row//3) * 3
    
    for r in range(gridRowNum,gridRowNum+3):
        for c in range(gridColNum,gridColNum+3):
            if currDigit == board[r][c]:
                return False
    return True

print(solve_sudoku_puzzle(
    [
[8, 4, 9, 0, 0, 3, 5, 7, 0],
[0, 1, 0, 0, 0, 0, 0, 0, 0],
[7, 0, 0, 0, 9, 0, 0, 8, 3],
[0, 0, 0, 9, 4, 6, 7, 0, 0],
[0, 8, 0, 0, 5, 0, 0, 4, 0],
[0, 0, 6, 8, 7, 2, 0, 0, 0],
[5, 7, 0, 0, 1, 0, 0, 0, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0],
[0, 2, 1, 7, 0, 0, 8, 6, 5]
]))