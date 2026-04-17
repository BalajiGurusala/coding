'''
Dutch National Flag Problem Implementation in Python.
time complexity: O(n) where n is the number of elements in the array.
space complexity: O(1) as we are sorting the array in place.
'''
def dutch_flag_sort(balls):
    """
    Args:
     balls(list_char)
    Returns:
     list_char
    """
    # Write your code here.
    middle, left = 0,0
    right = len(balls)-1
    
    while middle <= right:
        if balls[middle] == 'G':
            middle += 1
        elif balls[middle] == 'B':
            balls[middle], balls[right] = balls[right],balls[middle]
            right -= 1
        else:
            balls[left],balls[middle] = balls[middle],balls[left]
            left += 1
            middle += 1
    return balls
