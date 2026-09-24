'''
Given an array of integers, find all unique quadruplets in the array which gives the sum of the target.
Implementation of 4Sum problem using hashset and left-hand side approach.
'''


def four_sum_unique_hashset_lhs(arr, target):
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
    n = len(arr)
    for i in range(n-1, 2, -1):
        if i < n-1 and arr[i] == arr[i+1]:
            continue
        for j in range(i-1, 1, -1):
            if j < i-1 and arr[j] == arr[j+1]:
                continue
            seen = set()
            k = 0
            while k < j:
                complement = target - (arr[i] + arr[j] + arr[k])
                if complement in seen:
                    results.append([arr[i], arr[j], complement, arr[k]])
                    while k + 1 < j and arr[k] == arr[k+1]:
                        k += 1
                seen.add(arr[k])
                k += 1
    return results

if __name__ == "__main__":
    arr = [1, 0, -1, 0, -2, 2]
    target = 0
    print(four_sum_unique_hashset_lhs(arr, target))

    arr = [2, 2, 2, 2, 2]
    target = 8
    print(four_sum_unique_hashset_lhs(arr, target))
