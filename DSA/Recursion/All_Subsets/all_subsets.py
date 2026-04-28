'''given a set s = {1,2,3} of n distinct numbers, print(enumerate)
all the subsets
Ouput:
{}, {1}, {2}, {3}, {1,2}, {1,3}, {2,3},{1,2,3}
'''

def print_all_subsets(arr, idx, current_result=None, result=None):
    if result is None:
        result = []
    
    if current_result is None:
        current_result = []

    if idx == len(arr):
        result.append(list(current_result))
        return result
    
    current_result.append(arr[idx])
    print_all_subsets(arr, idx + 1, current_result, result) #Include the current element in the subset
    current_result.pop()
    print_all_subsets(arr, idx + 1, current_result, result) #Exclude the current element from the subset
    return result

print(print_all_subsets([1,2,3], 0))

'''Given a set S = {1,2,2} of n not distinct numbers, print(enumerate) 
all the subsets

Output:
{}, {1}, {2}, {1,2}, {2,2}, {1,2,2}
'''

def print_all_subsets_duplicates(arr, idx, current_result=None, result=None):
    if result is None:
        result = []
    
    if current_result is None:
        current_result = []
        arr.sort() # sort the array to handle duplicates

    if idx == len(arr):
        result.append(list(current_result))
        return result
    
    current_result.append(arr[idx])
    print_all_subsets_duplicates(arr, idx + 1, current_result, result) #Include the current element in the subset
    current_result.pop()
    while idx + 1 < len(arr) and arr[idx] == arr[idx + 1]: # Skip duplicates
        idx += 1
    print_all_subsets_duplicates(arr, idx + 1, current_result, result) #Exclude the current element from the subset
    return result

print(print_all_subsets_duplicates([2,1,2], 0))

    