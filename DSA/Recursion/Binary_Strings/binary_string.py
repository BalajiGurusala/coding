'''
The binary strings problem is a classic example of a combinatorial problem where we generate all possible binary strings of a given length.
Given an integer n, generate all possible binary strings of length n.
A binary string is a string that consists only of the characters '0' and '1'.
For example, if n = 2, the possible binary strings are:
00
01
10
11  
'''

#Depth first approach
def generate_binary_strings_recursive(n, current_string='', result=None):
    """
    Args:
     n: int
     current_string: str
     result: list of strings

    Returns:
     list of strings
    """
    # Write your code here.
    if result is None:
        result = []
    
    if n == 0:
        result.append(current_string)
        return result
    
    generate_binary_strings_recursive(n-1, current_string + '0', result)
    generate_binary_strings_recursive(n-1, current_string + '1', result)
    
    return result

print(generate_binary_strings_recursive(3))


#Breadth first approach
def generate_binary_strings_rec_iter(n):
    """
    Args:
     n: int

    Returns:            
     list of strings
    """
    # Write your code here.
    if n <= 0:
        return []
    elif n == 1:
        return ['0', '1']
    
    result = generate_binary_strings_rec_iter(n-1)
    new_result = []
    for string in result:        
        new_result.append(string + '0')
        new_result.append(string + '1') 
    
    return new_result

print(generate_binary_strings_rec_iter(3))   

'''Iterative approach 
Input: generate_binary_strings_iter(3)
Output: ["000", "001", "010", "011", "100", "101", "110","111"]
'''
def generate_binary_strings_iter(n):
    """
    Args:
     n: int

    Returns:            
     list of strings
    """
    # Write your code here.
    if n <= 0:
        return []
    elif n == 1:
        return ['0', '1']
    
    result = ['0', '1']
    for i in range(2, n+1):
        new_result = []
        for string in result:        
            new_result.append(string + '0')
            new_result.append(string + '1') 
        result = new_result

    
    return result

print(generate_binary_strings_iter(3))

# from collections import deque
def generate_binary_strings_iterative_queue(n):
    """
    Args:
     n: int

    Returns:            
     list of strings
    """
    # Write your code here.
    if n <= 0:
        return []
    elif n == 1:
        return ['0', '1']
    
    result = []
    queue = deque(['0', '1'])
    
    while queue:
        current_string = queue.popleft()
        if len(current_string) == n:
            result.append(current_string)
        else:
            queue.append(current_string + '0')
            queue.append(current_string + '1')
    
    return result

print(generate_binary_strings_iterative_queue(3))