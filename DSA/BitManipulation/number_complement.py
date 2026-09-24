'''
Find the complement of a given integer.

Example:
Input: 5
Output: 2

Time Complexity: O(1)
Space Complexity: O(1)
'''

def find_complement(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     int: The complement of the input integer.
    """
    if num == 0:
        return 1
    #num_bits = num.bit_length()
    num_bits = 0
    temp = num
    while temp:
        num_bits += 1
        temp >>= 1
    mask = (1 << num_bits) - 1
    return num ^ mask

if __name__ == "__main__":
    print(find_complement(5))  # Output: 2
    print(find_complement(0))  # Output: 1
    print(find_complement(1))  # Output: 0
    print(find_complement(10))  # Output: 5
