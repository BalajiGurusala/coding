def towers_of_hanoi(n, source, target, auxiliary):
    """
    Args:
     n: int
     source: str
     target: str
     auxiliary: str

    Returns:
     list of lists
    """
    # Write your code here.
    if n == 1:
        return [[source, target]]
    
    moves = towers_of_hanoi(n-1, source, auxiliary, target)
    moves.append([source, target])
    moves.extend(towers_of_hanoi(n-1, auxiliary, target, source))
    
    return moves

print(towers_of_hanoi(3, 'A', 'C', 'B'))