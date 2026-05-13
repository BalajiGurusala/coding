'''
Given a string containing digits from 0-9 inclusive, 
return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
Note that 0 and 1 do not map to any letters.
For example, given "23", return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

Input:
{
"phone_number": "1234567"
}

Output:
[
"adgjmp",
"adgjmq",
"adgjmr",
"adgjms",
"adgjnp",
...
"cfilns",
"cfilop",
"cfiloq",
"cfilor",
"cfilos"
]
'''
def get_words_from_phone_number(phone_number):
    """
    Args:
     phone_number(str)
    Returns:
     list_str
    """
    # Write your code here.
    num_dict = {
                0:'',
                1:'',
                2:'abc',
                3:'def',
                4:'ghi',
                5:'jkl',
                6:'mno',
                7:'pqrs',
                8:'tuv',
                9:'wxyz'
                }

    def get_words_from_phns_helper(i, slate=None, result=None):
        
        if slate == None:
            slate = []
        
        if result == None:
            result = []
        
        if i == len(phone_number):
            result.append("".join(slate))
            return 
        letters = num_dict[int(phone_number[i])]
        if not letters:
            get_words_from_phns_helper(i+1, slate, result)
        else:
            for c in letters:
                slate.append(c)
                get_words_from_phns_helper(i+1, slate, result)
                slate.pop()
                
        
        return result
    
    return get_words_from_phns_helper(0)
print(get_words_from_phone_number("1234567"))