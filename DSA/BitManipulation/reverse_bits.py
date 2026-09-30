'''
Reverse the bits of a given integer.

Example:
Input: 5 (binary: 101)
Output: 5 (binary: 101)

Input: 11011 (binary)
Output: 11011 (binary)

Input: An integer whose bits are to be reversed.
Output: The integer resulting from reversing the bits of the input.

Time Complexity: O(log n)
The function is O(log n) because we process each bit of the input number.
Space Complexity: O(1)
'''

def reverse_bits_v1(n):
    """
    Args:
     n(int): The input integer whose bits are to be reversed.
    Returns:
     int: The integer resulting from reversing the bits of the input.
    """
    result = 0
    while n != 0:
        result = (result << 1) | (n & 1)
        n >>= 1
    return result

def reverse_bits_v2(n):
    """
    Args:
     n(int): The input integer whose bits are to be reversed.
    Returns:
     int: The integer resulting from reversing the bits of the input.
    """
    result = 0
    j = n.bit_length()-1
    i =0
    while(i <j):
        ith_bit = (n >> i) & 1
        jth_bit = (n >> j ) & 1
        if ith_bit != jth_bit:
            n = n ^ ((1 << i) | (1 << (j)))
        i += 1
        j -= 1
    return n

if __name__ == "__main__":
    print(reverse_bits_v1(5))  # Output: 5
    print(reverse_bits_v1(0b11011))  # Output: 0b11011
    print(reverse_bits_v1(0))  # Output: 0
    print(reverse_bits_v1(1))  # Output: 1
    print(reverse_bits_v1(0b1001))  # Output: 0b1001

    print(reverse_bits_v2(5))  # Output: 5
    print(reverse_bits_v2(0b11011))  # Output: 0b11011
    print(reverse_bits_v2(0))  # Output: 0
    print(reverse_bits_v2(1))  # Output: 1
    print(reverse_bits_v2(0b1001))  # Output: 0b1001