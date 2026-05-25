'''
Generate All Combinations With Sum Equal To Target
Given an integer array, generate all the unique combinations of the array numbers 
that sum up to a given target value.
Input: arr = [1,2,3,4], target = 5
Output: [[1,4], [2,3]]
'''


def generate_all_combinations(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    return generate_all_combinations_helper(arr, target, 0)

def generate_all_combinations_helper(arr, target, i, tgt_sum=0, slate=None, result=None):
    
    if slate == None:
        slate = []
        arr.sort()
    
    if result == None:
        result = []
    
    if tgt_sum > target or (tgt_sum + sum(arr[i:]) < target):
        return result
    
    if tgt_sum == target:
        result.append(slate[:])
        return result
    
    if len(arr) == i:
        return result
    
    for j in range(i, len(arr)):
        if j>i and arr[j] == arr[j-1]:
            continue
        slate.append(arr[j])
        generate_all_combinations_helper(arr, target, j+1, tgt_sum+arr[j], slate, result)
        num = slate.pop()

    return result
print(generate_all_combinations([1,2,3,4], 5))