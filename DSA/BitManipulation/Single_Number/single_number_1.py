'''
Calculate the single number in a list where every element appears twice except for one.

Example:
Input: [4, 1, 2, 1, 2]
Output: 4

Input: [2, 2, 3]
Output: 3

Input: A list of integers nums.
Output: The single number that appears only once.

Time Complexity: O(n)
The function is O(n) because we iterate through the list once.
Space Complexity: O(1)
'''

def single_number_v1(nums):
    """
    Args:
     nums(list): A list of integers where every element appears twice except for one.
    Returns:
     int: The single number that appears only once.
    """
    odd = 0
    even = -1
    for i in range(len(nums)):
        new_odd = (odd & ~nums[i]) | (~odd & nums[i])
        #below is not necessary for finding the single number
        new_even = (even & ~nums[i]) | (~even & nums[i])
        odd = new_odd
        even = new_even
    return odd

def single_number_v2(nums):
    """
    Args:
     nums(list): A list of integers where every element appears twice except for one.
    Returns:
     int: The single number that appears only once.
    """
    result = 0
    for num in nums:
        result ^= num
    return result

if __name__ == "__main__":
    # Test cases
    print("single_number_v1", single_number_v1([4, 1, 2, 1, 2]))  # Output: 4
    print("single_number_v1", single_number_v1([2, 2, 3]))  # Output: 3
    print("single_number_v2", single_number_v2([4, 1, 2, 1, 2]))  # Output: 4
    print("single_number_v2", single_number_v2([2, 2, 3]))  # Output: 3
    print("single_number_v1", single_number_v1([0, 0, 1]))  # Output: 1
    print("single_number_v1", single_number_v1([7, 3, 3]))  # Output: 7
    print("single_number_v2", single_number_v2([7, 3, 3]))  # Output: 7
    print("single_number_v1", single_number_v1([5, 5, 9]))  # Output: 9
    print("single_number_v1", single_number_v1([8, 8, 6]))  # Output: 6
    print("single_number_v2", single_number_v2([8, 8, 6]))  # Output: 6