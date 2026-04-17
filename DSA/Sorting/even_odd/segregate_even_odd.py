'''
Given an array of integers, segregate even and odd numbers in the array. 
The order of even and odd numbers does not matter. The output array should 
have all the even numbers followed by all the odd numbers.
Input:
{
"numbers": [1, 2, 3, 4, 5, 6]
}
output:
[2, 4, 6, 1, 3, 5] or any other combination where all even numbers are followed by all odd numbers.
'''

def segregate_evens_and_odds(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    even = 0
    odd = len(numbers)-1
    while even < odd:
        if numbers[even]%2 == 0:
            even += 1
        elif numbers[odd]%2 != 0:
            odd -= 1
        else:
            numbers[even], numbers[odd] = numbers[odd],numbers[even]
            even += 1
            odd -= 1
    return numbers
'''
Time Complexity: O(n) where n is the number of elements in the input array.
Space Complexity: O(1) as we are doing the segregation in place without using any extra 
space.
'''

def segregate_evens_and_odds_optimal(numbers):
    """
    Args:
     numbers(list_int32)
    Returns:
     list_int32
    """
    # Write your code here.
    even = 0
    odd = len(numbers)-1
    while even < odd:
        if numbers[even]%2 == 0:
            even += 1
        else:
            numbers[even], numbers[odd] = numbers[odd],numbers[even]
            odd -= 1
    return numbers