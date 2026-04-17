'''
Merge Sort Algorithm Implementation in Python.  
time complexity: O(n log n) where n is the number of elements in the array.
space complexity: O(n) for the temporary array used during merging.
'''
def merge_sort(arr):
    """
    Args:
     arr(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    def merge(arr, start, mid, end):
        i = start
        j = mid + 1
        sorted_arr = []
        while i <= mid and j <= end:
            if arr[i] < arr[j]:
                sorted_arr.append(arr[i])
                i += 1
            else:
                sorted_arr.append(arr[j])
                j += 1
        while i <= mid:
            sorted_arr.append(arr[i])
            i += 1
        while j <= end:
            sorted_arr.append(arr[j])
            j += 1
        
        for i in range(len(sorted_arr)):
            arr[start+i] = sorted_arr[i]

    def mergesort_helper(arr, start, end):
        
        if end <= start:
            return
        mid = (start+end)//2
        mergesort_helper(arr, start, mid)
        mergesort_helper(arr, mid+1, end)
        
        merge(arr, start, mid, end)
    
    sorted_arr = []    
    mergesort_helper(arr, 0, len(arr)-1)
    return arr