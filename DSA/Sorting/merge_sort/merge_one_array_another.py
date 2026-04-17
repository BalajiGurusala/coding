'''
First array has n positive numbers, and they are sorted in the non-descending order.
Second array has 2n numbers: first n are also positive and sorted in the same way but the last n are all zeroes.
Merge the first array into the second and return the latter. You should get 2n positive integers sorted in the non-descending order.
input:
{
"first": [1, 3, 5],
"second": [2, 4, 6, 0, 0, 0]
}
output:
[1, 2, 3, 4, 5, 6]
'''
def merge_one_into_another(first, second):
    """
    Args:
     first(list_int32)
     second(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    i = len(first)-1
    j = len(second)//2-1
    k = len(second)-1
    while i >=0 and j >=0:
        if first[i] >= second[j]:
            second[k] = first[i]
            k -= 1
            i -= 1
        else:
            second[k] = second[j]
            k -= 1
            j -= 1
    while i >= 0:
        second[k] = first[i]
        i -= 1
        k -= 1
    return second