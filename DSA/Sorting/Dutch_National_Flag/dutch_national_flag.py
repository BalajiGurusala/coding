'''
what is the Dutch National Flag Problem?
The Dutch National Flag Problem is a sorting problem where the goal is to 
sort an array containing three distinct types of elements (e.g., 'R', 'G', 'B') 
such that all elements of the same type are grouped together and appear in a specific order.
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

if __name__ == "__main__":
    balls = ['R', 'G', 'B', 'G', 'R', 'B', 'G']
    print(dutch_flag_sort(balls))

    balls = ['B', 'B', 'G', 'R', 'R', 'G', 'B']
    print(dutch_flag_sort(balls))
