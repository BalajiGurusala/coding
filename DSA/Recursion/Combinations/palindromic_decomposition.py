'''
Find all palindromic decompositions of a given string s.

A palindromic decomposition of string is a decomposition of the string into substrings, 
such that all those substrings are valid palindromes.
Input:
{
"s": "abracadabra"
}
Output:
["a|b|r|a|c|ada|b|r|a", "a|b|r|aca|d|a|b|r|a", "a|b|r|a|c|a|d|a|b|r|a"]
'''
def generate_palindromic_decompositions(s):
    """
    Args:
     s(str)
    Returns:
     list_str
    """
    # Write your code here.
    return palindromic_decompositions_helper(s, 0)

def palindromic_decompositions_helper(s, i, slate=None, result=None, last_string=None):
    
    if slate == None:
        slate = []
    
    if result == None:
        result = []
    
    if last_string == None:
        last_string = ''
        
    #backtrack case
    # if(not isPalindrome(last_string)):
    #     return
    
    #base case
    if len(s) == i:
        if(isPalindrome(last_string)):
            result.append("".join(slate))
        return result
    
    #concatenate case
    slate.append(s[i])
    palindromic_decompositions_helper(s, i+1, slate, result, last_string + s[i])
    slate.pop()
    
    #'|' case
    if isPalindrome(last_string):
        slate.append('|')
        slate.append(s[i])
        palindromic_decompositions_helper(s, i+1, slate, result, s[i])
        slate.pop()
        slate.pop()
    
    return result
    
        

def isPalindrome(s):
    if not s:
        return False
    return s == s[::-1]

#print(generate_palindromic_decompositions('racecar'))
print(generate_palindromic_decompositions('abracadabra'))