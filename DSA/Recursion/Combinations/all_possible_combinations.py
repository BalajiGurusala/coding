''' Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
For example, if n = 4 and k = 2, a solution is: 4C2 = 6 combinations as below:  
[[2,4], [3,4], [2,3], [1,2], [1,3], [1,4]]
'''
def combinations(n, k, i, slate=None, result=None):
    if result is None:
        result = []
    
    if slate is None:
        slate = []
    
    #Backtracking: if the length of slate is equal to k, we can add the slate to the result and return
    if len(slate) == k:
        result.append(slate[:])
        return result

    #Base Case: if the length of n is equal to i, we have reached the end of the array and we can return
    if len(n) == i:
        return
    
    slate.append(n[i])
    combinations(n, k, i+1, slate, result) #Include the current element and move to the next element
    slate.pop()
    combinations(n, k, i+1, slate, result) #Exclude the current element and move to the next element
    
    return result

print(combinations([1,2,3,4], 2, 0))

'''For loop implementation: we can use a for loop to iterate through 
the array and include the current element in the slate and move to the next element'''

def combinations_for_loop(n, k, i, slate=None, result=None):
    if result is None:
        result = []
    
    if slate is None:
        slate = []
    
    if len(slate) == k:
        result.append(slate[:])
        return result

    for j in range(i, len(n)):
        slate.append(n[j])
        combinations_for_loop(n, k, j+1, slate, result) #Include the current element and move to the next element
        slate.pop() #Backtrack: remove the current element from the slate and move to the next element
    
    return result

print(combinations_for_loop([1,2,3,4], 2, 0))