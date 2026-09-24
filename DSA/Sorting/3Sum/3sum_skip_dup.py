'''
Given an array of integers, find all unique triplets in the array that is equal to target.
Implementation of 3Sum problem using skip duplicates approach.
'''

def three_sum_skip_dup(arr, target):
    """
    Args:
     arr(list_int32)
     target(int32)
    Returns:
     list_list_int32
    """
    arr.sort()
    n = len(arr)
    results = []
    for i in range(n-2):
        if i > 0 and arr[i] == arr[i-1]:
            continue
        left, right = i+1, n-1
        while left < right:
            total = arr[i] + arr[left] + arr[right]
            if total == target:
                results.append([arr[i], arr[left], arr[right]])
                left += 1
                right -= 1
                while left < right and arr[left] == arr[left+1]:
                    left += 1
                while left < right and arr[right] == arr[right-1]:
                    right -= 1
            elif total < target:
                left += 1
            else:
                right -= 1
    return results

if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(three_sum_skip_dup(arr, target))

    arr = [2, 2, 2, 2, 2]
    target = 6
    print(three_sum_skip_dup(arr, target))