'''
Count the number of 1 bits (Hamming weight) in the binary representation of a given integer.

Example:
Input: 5
Output: 2

Time Complexity: O(1)
Space Complexity: O(1)
'''

def count_one_bits(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     int: The number of 1 bits in the binary representation of the input integer.
    """
    count = 0
    while num:
        count += num & 1
        num >>= 1
    return count

def count_one_bits_v2(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     int: The number of 1 bits in the binary representation of the input integer.
    """
    count = 0
    while num:
        # Remove the rightmost 1 bit from num
        num &= num - 1
        count += 1
    return count

if __name__ == "__main__":
    print(count_one_bits(5))  # Output: 2
    print(count_one_bits(0))  # Output: 0
    print(count_one_bits(1))  # Output: 1
    print(count_one_bits(10))  # Output: 2
    print(count_one_bits(15))  # Output: 4
    print(count_one_bits(16))  # Output: 1
    print(count_one_bits(31))  # Output: 5
    print(count_one_bits_v2(5))  # Output: 2
    print(count_one_bits_v2(0))  # Output: 0
    print(count_one_bits_v2(1))  # Output: 1
    print(count_one_bits_v2(10))  # Output: 2
    print(count_one_bits_v2(15))  # Output: 4
    print(count_one_bits_v2(16))  # Output: 1
    print(count_one_bits_v2(31))  # Output: 5