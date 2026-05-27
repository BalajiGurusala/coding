'''
The n-queens puzzle is the problem of placing n queens on an n x n chess
board such that no two queens threaten each other. 
Given an integer n, return all distinct solutions to the n-queens puzzle.'''

from unittest import result


def find_all_arrangements(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    # Write your code here.
    return n_queen_helper(n, 0)

def conv_to_string(slate):
    res_string = []
    for q in slate:
        s = ["-"] * len(slate)
        s[q] = 'q'
        res_string.append("".join(s))
    return res_string
    
def n_queen_helper(n, i, slate=None, result=None, used=None):
    
    if slate == None:
        slate = []
    
    if result == None:
        result = []
    
    if used == None:
        used = [False]*n
    
    #base case if any of two queens are in the same column then it's not a valid case
    #compare newly added queen is in the same column as any of the previously added queens
    lastQ = len(slate)-1
    for earlQ in range(lastQ):
        if slate[earlQ] == slate[lastQ]:
            return
    
        #Base case If an of the two queens are in the same diagnol, then it's not a valid case
        #compare newly added queen is in the same diagnol as any of the previously added queens
        #To be in the same diagnol, both rowdiff and colDiff must match
        rowDiff = abs(earlQ - lastQ)
        colDiff = abs(slate[earlQ] - slate[lastQ])
        if rowDiff == colDiff:
            return
    
    if(n == i):
        res_string = conv_to_string(slate)
        result.append(res_string)
        return result
    
    
    for col in range(n):
        if not used[col]:
            used[col] = True
            slate.append(col)
            n_queen_helper(n, i+1, slate, result, used)
            slate.pop()
            used[col] = False
    return result
    
print(find_all_arrangements(4))

'''
Using universal backtracking template (scout & report) to solve sudoku puzzle
'''
def solve_n_queens_scout_report(n):
    """
    Args:
     n(int32)
    Returns:
     list_list_str
    """
    # Write your code here.
    board = [["-"] * n for _ in range(n)]
    result = []
    n_queen_helper_scout_report(0, n, board, result)
    return result
    
def n_queen_helper_scout_report(row, n, board, result=None):
    if result is None:
        result = []
    if row == n:
        result.append(["".join(row) for row in board])
        return True
    for col in range(n):
        if is_valid_queen(board, row, col, n):
            board[row][col] = 'q'
            n_queen_helper_scout_report(row + 1, n, board, result)
            #Removed the backtracking step of resetting the board[row][col]
            # to find all the possible cases instead of returning after finding the first valid case
            #if n_queen_helper_scout_report(row + 1, n, board, result):
            #  return True
            board[row][col] = '-'
    return False

def is_valid_queen(board, row, col, n):
    for i in range(row):
        #check if the newly added queen is in the same column
        if board[i][col] == 'q':
            return False
        #check if the newly added queen is in the same diagonal
        #To be in the same diagonal, rowDiff and colDiff must match
        for c in range(n):
            if board[i][c] == 'q':
                rowDiff = abs(i - row)      
                colDiff = abs(c - col)
                if rowDiff == colDiff:
                    return False
    return True

print(solve_n_queens_scout_report(4))
