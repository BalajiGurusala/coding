'''
Check if a given integer is a power of 2.

Example:
Input: 8    
Output: True

Time Complexity: O(1)
Space Complexity: O(1)
'''

def power_of_two(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     bool: True if the input integer is a power of 2, False otherwise.
    """
    return num > 0 and (num & (num - 1)) == 0

if __name__ == "__main__":
    print(power_of_two(8))  # Output: True
    print(power_of_two(0))  # Output: False
    print(power_of_two(1))  # Output: True
    print(power_of_two(10))  # Output: False
    print(power_of_two(16))  # Output: True
    