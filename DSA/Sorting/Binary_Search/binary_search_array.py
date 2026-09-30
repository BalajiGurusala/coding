'''
Binary Search in a sorted array.
'''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def binary_search_recursive(arr, target, left, right):
    
    if left > right:
        return -1
    
    mid = (left + right) // 2

    if arr[mid] == target:
        return mid
    elif target > arr[mid]:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
    

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 4
    result = binary_search(arr, target)
    if result != -1:
        print(f"Element found at index: {result}")
    else:
        print("Element not found in the array.")

    target_recursive = 5
    result_recursive = binary_search_recursive(arr, target_recursive, 0, len(arr) - 1)
    if result_recursive != -1:
        print(f"Element found at index (recursive): {result_recursive}")
    else:
        print("Element not found in the array (recursive).")