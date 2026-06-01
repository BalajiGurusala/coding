'''
Given a string s that consists of digits ("0".."9") and target, a non-negative integer, 
find all expressions that can be built from string s that evaluate to the target.
When building expressions, you have to insert one of the following operators between 
each pair of consecutive characters in s: join or * or +. For example, by inserting 
different operators between the two characters of string "12" we can get either 12 
(1 joined with 2 or "12") or 2 ("1*2") or 3 ("1+2").
Other operators such as - or ÷ are NOT supported.
Expressions that evaluate to the target but only utilize a part of s do not count: entire s has to be consumed.
Precedence of the operators is conventional: join has the highest precedence, * – medium and + has the lowest precedence. For example, 1 + 2 * 34 = (1 + (2 * (34))) = 1 + 68 = 69.
You have to return ALL expressions that can be built from string s and evaluate to the target.

Input:
{
"s": "202",
"target": 4
}

Ouput:
["2+0+2", "2+02", "2*02"]
'''

def generate_all_expressions(s, target):
    """
    Args:
     s(str)
     target(int64)
    Returns:
     list_str
    """
    # Write your code here.
    return generate_all_expressions_helper(s , target , 0)
    
def generate_all_expressions_helper(s , target , i, slate=None, result=None, curr_val=0, last_operand=0):
    
    if slate == None:
        slate = []
    
    if result == None:
        result = []
    
    #Base case
    if len(s) == i:
        if target == curr_val: 
            result.append("".join(slate[:]))
        return result
        
    #Recursive case
    for j in range(i,len(s)):
        curr_str = s[i:j+1]
        
        curr_num = int(curr_str)
        #Append case
        if(i == 0):
            slate.append(curr_str)
            generate_all_expressions_helper(s , target , j+1, slate, result, curr_num, curr_num)
            slate.pop()
        else:
            #Addition case
            slate.append("+")
            slate.append(curr_str)
            generate_all_expressions_helper(s , target , j+1, slate, result,
            curr_val + curr_num, curr_num)
            slate.pop()
            slate.pop()
    
            #Multiplication case
            slate.append('*')
            slate.append(curr_str)
            generate_all_expressions_helper(s , target , j+1, slate, result,
            curr_val - last_operand + (curr_num * last_operand),  curr_num * last_operand)
            slate.pop()
            slate.pop()
        
    return result
        