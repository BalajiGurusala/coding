
'''Given an array of integers, count the number of inversions in the array. An inversion is a pair of indices (i, j) such that i < j and arr[i] > arr[j].
Input:
{
"arr": [1, 20, 6, 4, 5]
}
Output:
5
explanation:
The five inversions are (20, 6), (20, 4), (20, 5), (6, 4) and (6, 5).
'''
def count_inversions(nums):
    """
    Args:
     nums(list_int32)
    Returns:
     int64
    """
    # Write your code here.
    return merge_sort_helper(nums, 0, len(nums)-1)

def merge_sort_helper(nums, start, end):
    
    if start >= end:
        return
    
    mid = (start+end)//2
    count = 0
    count += merge_sort_helper(nums, start, mid)
    count += merge_sort_helper(nums, mid+1, end)
    
    count += merge(nums, start, mid, end)
    
    return count

def merge(nums, start, mid, end):

    sorted_array = []
    inversions = 0
    i = start
    j = mid+1
    while i <= mid and j <= end:
        if nums[i] <= nums[j]:
            sorted_array.append(nums[i])
            i+= 1
        else:
            sorted_array.append(nums[j])
            # If nums[i] > nums[j], then all remaining elements 
            # in 'nums[i]' (from index i to the mid) are also > nums[j].
            inversions += (mid-i)+1
            j += 1
    
    while i <= mid:
        sorted_array.append(nums[i])
        i += 1
    while j <= end:
        sorted_array.append(nums[j])
        j += 1
        
    for i in range(len(sorted_array)):
        nums[start+i] = sorted_array[i]
            
    return inversions