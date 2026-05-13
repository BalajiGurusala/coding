'''

'''

def letter_case_permutations(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    return letter_case_permutations_helper(s,0)

def letter_case_permutations_helper(s, i, slate=None, result=None):
    
    if slate == None:
        slate = []
    
    if result == None:
        result = []
    
    if len(slate) == len(s):
        result.append("".join(slate))
        return
    
    if s[i].isdigit():
        slate.append(s[i])
        letter_case_permutations_helper(s, i+1, slate,result)
        slate.pop()
    else:
        slate.append(s[i].upper())
        letter_case_permutations_helper(s, i+1, slate,result)
        slate.pop()
        
        slate.append(s[i].lower())
        letter_case_permutations_helper(s, i+1, slate,result)
        slate.pop()

    return result
print(letter_case_permutations("a1b2"))