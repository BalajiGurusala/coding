'''
Intersection Of Three Sorted Arrays
Given three arrays sorted in the ascending order, return their intersection sorted array in the ascending order.

Input:
{
"arr1": [2, 5, 10],
"arr2": [2, 3, 4, 10],
"arr3": [2, 4, 10]
}
Output:
[2, 10]

Input:
{
"arr1": [1, 2, 3],
"arr2": [],
"arr3": [2, 2]
}

Output:
[-1]

Input:
{
"arr1": [1, 2, 2, 2, 9],
"arr2": [1, 1, 2, 2],
"arr3": [1, 1, 1, 2, 2, 2]
}

Output:
[1, 2, 2]

'''


def find_intersectio_dict(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    dict2 = {}
    dict3 = {}
    result = []
    
    for num in arr2:
        dict2[num] = dict2.get(num,0)+1
    for num in arr3:
        dict3[num] = dict3.get(num,0)+1

    for key in arr1:
        if key in dict2 and key in dict3:
            if dict2[key] > 0 and dict3[key] > 0:
                result.append(key)
                dict2[key] -= 1
                dict3[key] -= 1
    if len(result):
        return result
    else:
        return [-1]
    


def find_intersection_counter(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    from collections import Counter
    result = []
    counter2 = Counter(arr2)
    counter3 = Counter(arr3)
    
    for num in arr1:
        if counter2[num]>0 and counter3[num]>0:
            result.append(num)
            counter2[num] -= 1
            counter3[num] -= 1
    return result if result else [-1]
    
'''
Time Complexity: O(n1 + n2 + n3), where n1, n2 and n3 are the lengths of arr1, arr2 and arr3 respectively.
Space Complexity: O(n2 + n3) for the dictionaries used to store the counts of elements in arr2 and arr3.
'''

def find_intersection_merge_sort(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    i=j=k=0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue
        elif arr1[i] < arr2[j] or arr1[i] < arr3[k]:
            i += 1
        elif arr2[j] < arr1[i] or arr2[j] < arr3[k]:
            j += 1
        elif arr3[k] < arr1[i] or arr3[k] < arr2[j]:
            k += 1
            
    return result if result else [-1]


def find_intersection_merge_sort_impr(arr1, arr2, arr3):
    """
    Args:
     arr1(list_int32)
     arr2(list_int32)
     arr3(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    result = []
    i=j=k=0
    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        if arr1[i] == arr2[j] == arr3[k]:
            result.append(arr1[i])
            i += 1
            j += 1
            k += 1
            continue
        max_num = max(arr1[i], arr2[j], arr3[k])
        if arr1[i] < max_num:
            i += 1
        if arr2[j] < max_num:
            j += 1
        if arr3[k] < max_num:
            k += 1
            
    return result if result else [-1]