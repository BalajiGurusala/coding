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
    print("power_of_two(8)", power_of_two(8))  # Output: True
    print("power_of_two(0)", power_of_two(0))  # Output: False
    print("power_of_two(1)", power_of_two(1))  # Output: True
    print("power_of_two(10)", power_of_two(10))  # Output: False
    print("power_of_two(16)", power_of_two(16))  # Output: True


def power_of_four(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     bool: True if the input integer is a power of 4, False otherwise.
    """
    return num > 0 and (num & (num - 1)) == 0 and (num - 1) % 3 == 0

if __name__ == "__main__":
    print("power_of_four(8)", power_of_four(8))  # Output: False
    print("power_of_four(0)", power_of_four(0))  # Output: False
    print("power_of_four(1)", power_of_four(1))  # Output: True
    print("power_of_four(16)", power_of_four(16))  # Output: True    
    print("power_of_four(64)", power_of_four(64))  # Output: True

def power_of_four_v2(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     bool: True if the input integer is a power of 4, False otherwise.
    """
    return num > 0 and (num & (num - 1)) == 0 and (num & 0x55555555) == num

if __name__ == "__main__":
    print("power_of_four_v2(8)", power_of_four_v2(8))  # Output: False
    print("power_of_four_v2(0)", power_of_four_v2(0))  # Output: False
    print("power_of_four_v2(1)", power_of_four_v2(1))  # Output: True
    print("power_of_four_v2(16)", power_of_four_v2(16))  # Output: True    
    print("power_of_four_v2(64)", power_of_four_v2(64))  # Output: True

def power_of_three(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     bool: True if the input integer is a power of 3, False otherwise.
    """
    if num < 1:
        return False
    while num % 3 == 0:
        num //= 3
    return num == 1

if __name__ == "__main__":
    print("power_of_three(6)", power_of_three(6))  # Output: False
    print("power_of_three(0)", power_of_three(0))  # Output: False
    print("power_of_three(1)", power_of_three(1))  # Output: True
    print("power_of_three(9)", power_of_three(9))  # Output: True    
    print("power_of_three(27)", power_of_three(27))  # Output: True
    print("power_of_three(81)", power_of_three(81))  # Output: True

def power_of_three_v2(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     bool: True if the input integer is a power of 3, False otherwise.
    """

    #1162261467 is the largest power of 3 that fits in a signed 32-bit integer.
    # 3^19 = 1,162,261,467
    #2^31 - 1 = 2,147,483,647
    '''
    3^19 / 3^1  = 3^18
    3^19 / 3^2  = 3^17
    3^19 / 3^10 = 3^9
    3^19 / 3^19 = 1
    '''
    return num > 0 and (3**19) % num == 0

if __name__ == "__main__":
    print("power_of_three_v2(6)", power_of_three_v2(6))  # Output: False
    print("power_of_three_v2(0)", power_of_three_v2(0))  # Output: False
    print("power_of_three_v2(1)", power_of_three_v2(1))  # Output: True
    print("power_of_three_v2(9)", power_of_three_v2(9))  # Output: True    
    print("power_of_three_v2(27)", power_of_three_v2(27))  # Output: True
    print("power_of_three_v2(81)", power_of_three_v2(81))  # Output: True


