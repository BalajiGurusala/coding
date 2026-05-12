''' Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
For example, given n = 3, a solution set is:
["((()))", "(()())", "(())()", "()(())", "()()()"]
'''

def generate_parentheses(n, current_string='', result=None, open_count=0, close_count=0):
    if result is None:
        result = []
    
    if open_count == n and close_count == n:
        result.append(current_string)
        return result
    
    if open_count < n:
        generate_parentheses(n, current_string + '(', result, open_count + 1, close_count)
    
    if close_count < open_count:
        generate_parentheses(n, current_string + ')', result, open_count, close_count + 1)
    
    return result

print(generate_parentheses(3))