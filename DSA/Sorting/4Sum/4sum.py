'''Given an array of integers, find all unique triplets in the array which gives the sum of zero.
Input:
{
"arr": [-1, 0, 1, 2, -1, -4]
}
Output:
["-1, -1, 2", "-1, 0, 1"]'''
def four_sum(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    arr.sort()
    output = []
    def two_sum(arr, target, start, num1, num2, output):
        left = start
        right = len(arr)-1
        while left < right:
            sum = arr[left]+arr[right]
            if sum == target:
                output.append([num1, num2, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]: #avoid duplicates
                    left += 1
                while left < right and arr[right] == arr[right+1]: #avoid duplicates
                    right -= 1
            elif sum < target:
                left += 1
            else:
                right -= 1
         
    def three_sum(arr, target, start, num1, output):
        for idx in range(start,len(arr)-2):
            num2 = arr[idx]
            if idx > start and num2 == arr[idx-1]:
                continue #avoid duplicates
                
            new_target2 = target - num2
            two_sum(arr, new_target2, idx+1, num1, num2, output)
    
    for idx in range(0, len(arr)-3):
        num1 = arr[idx]
        if idx > 0 and num1 == arr[idx-1]:
            continue #avoid duplicates by ignoring the same element as previous
        
        new_target1 = target - num1
        three_sum(arr, new_target1, idx+1, num1, output)
    return 

def four_sum_pruning(arr, target):
    arr.sort()
    output = []
    n = len(arr)

    def two_sum(start, target, num1, num2):
        left, right = start, n - 1
        while left < right:
            curr_sum = arr[left] + arr[right]
            if curr_sum == target:
                output.append([num1, num2, arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
            elif curr_sum < target:
                left += 1
            else:
                right -= 1
         
    def three_sum(start, target, num1):
        for i in range(start, n - 2):
            if i > start and arr[i] == arr[i-1]:
                continue
            
            # Optimization: Pruning
            if arr[i] + arr[i+1] + arr[i+2] > target: break 
            if arr[i] + arr[n-2] + arr[n-1] < target: continue

            two_sum(i + 1, target - arr[i], num1, arr[i])
    
    for i in range(n - 3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
            
        # Optimization: Pruning
        if arr[i] + arr[i+1] + arr[i+2] + arr[i+3] > target: break
        if arr[i] + arr[n-3] + arr[n-2] + arr[n-1] < target: continue

        three_sum(i + 1, target - arr[i], arr[i])
        
    return output


def four_sum_simplified(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    results = []
    arr.sort()
    for i in range(len(arr)-3):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)-2):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            find = target - (arr[i]+arr[j])
            twoSum(arr, i, j, j+1, find, results)
    return results
    
def twoSum(arr, i, j, low, target, results):
    high = len(arr)-1
    while low < high:
        if arr[low]+arr[high] < target:
            low += 1
        elif arr[low]+arr[high] > target:
            high -= 1
        else:
            results.append([arr[i], arr[j], arr[low], arr[high]])
            low += 1
            high -= 1
            while low < high and arr[low] == arr[low-1]:
                low += 1