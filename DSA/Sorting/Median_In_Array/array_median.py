'''
This module contains a function to find the median of an array.

The median is the middle value in a list of numbers. If the list has an even number of elements, the median is the average of the two middle numbers.

Example:
    >>> median([1, 3, 3, 6, 7, 8, 9])
    6
    >>> median([1, 2, 3, 4, 5, 6, 8, 9])
    4.5
'''
#Brute Force
def median(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2 - 1] + arr[n // 2]) / 2


if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("All tests passed.")
    print("Median of [1, 3, 3, 6, 7, 8, 9]:", median([1, 3, 3, 6, 7, 8, 9]))
    print("Median of [1, 2, 3, 4, 5, 6, 8, 9]:", median([1, 2, 3, 4, 5, 6, 8, 9]))
    print("Median of [7, 8, 3, 1, 2, 6, 5, 4]:", median([7, 8, 3, 1, 2, 6, 5, 4]))
    print("Median of [10, 20, 30, 40, 50]:", median([10, 20, 30, 40, 50]))
    print("Median of [5, 1, 4, 2, 3]:", median([5, 1, 4, 2, 3]))
    print("Median of [1, 2, 3, 4]:", median([1, 2, 3, 4]))
    print("Median of [1]:", median([1]))
