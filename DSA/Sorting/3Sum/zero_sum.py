'''Given an array of integers, find all unique triplets in the array which gives the sum of zero.
Input:
{
"arr": [-1, 0, 1, 2, -1, -4]
}
Output:
["-1, -1, 2", "-1, 0, 1"]
'''
def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    arr.sort()
    output = []
    n = len(arr)
    for idx in range(n-2):
        if idx > 0:
            if arr[idx] == arr[idx-1]:
                continue
        left = idx+1
        right = n-1
        new_target = 0 - arr[idx]
        while left < right:
            current_sum = arr[left] + arr[right]
            if current_sum == new_target:
                output.append(f"{arr[idx]},{arr[left]},{arr[right]}")
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif current_sum < new_target:
                left += 1
            else:
                right -= 1
    return output

def find_zero_sum(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_str
    """
    # Write your code here.
    results = []
    arr.sort()
    for i, target in enumerate(arr):
        if target > 0:
            break #Once we have a positive target then there is no way of getting sum is zero on a sorted array
        if i>0 and arr[i] == arr[i-1]:
            continue
        
        twoSum(arr, i+1, -target, results)        
    return results

def twoSum(arr, i, target, results):
    j = len(arr)-1
    while i < j:
        if arr[i]+arr[j] > target:
            j -= 1
        elif arr[i]+arr[j] < target:
            i += 1
        else:
            string = f'{-target}, {arr[i]}, {arr[j]}'
            results.append(string)
            i += 1
            j -= 1
            while i<j and arr[i] == arr[i-1]:
                i += 1