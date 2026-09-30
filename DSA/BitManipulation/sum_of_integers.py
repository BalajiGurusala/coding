'''
Calculate the sum of two integers without using the '+' and '-' operators.

Example:
Input: a = 5, b = 3
Output: 8

Input: a = -2, b = 7
Output: 5

Input: Two integers a and b.
Output: The sum of a and b.

Time Complexity: O(log(max(a, b)))
The function is O(log(max(a, b))) because we process each bit of the input numbers.
Space Complexity: O(1)
'''

def sum_of_integers(a, b):
    """
    Args:
     a(int): The first integer.
     b(int): The second integer.
    Returns:
     int: The sum of a and b without using the '+' and '-' operators.
    """
    mask = 0xFFFFFFFF
    a &= mask
    b &= mask
    '''
    carry = a & b       # find carries
    a = a ^ b           # add bits where there's no carry
    b = carry << 1      # make the carries the next value to add
    '''
    for i in range(32):  # Assuming 32-bit integers
        carry = (a & b) & mask
        a = (a ^ b) & mask
        b = (carry << 1) & mask
    '''
    0x7FFFFFFF is the largest signed 32-bit positive value. If a is at or below it, 
    the result is nonnegative, so return it directly.
    '''
    return a if a <= 0x7FFFFFFF else ~(a ^ mask)

def sum_of_integers_v2(a, b):
    """
    Args:
     a(int): The first integer.
     b(int): The second integer.
    Returns:
     int: The sum of a and b without using the '+' and '-' operators.
    """
    mask = 0xFFFFFFFF
    sum = 0
    carry = 0
    s_i = 0
    for i in range(32):  # Assuming 32-bit integers
        a_i = a & 1
        b_i = b & 1
        s_i = a_i ^ b_i ^ carry
        '''Each input is either 0 or 1. A carry is produced when at least two of the three bits are 1:
            a_i & b_i is 1 if both input bits are 1. a_i & carry is 1 if the first input and incoming carry are 1.
            b_i & carry is 1 if the second input and incoming carry are 1. 
            | combines those checks: if any pair is both 1, output carry is 1.'''
        carry = (a_i & b_i) | (a_i & carry) | (b_i & carry)
        sum |= (s_i << i)
        b >>= 1
        a >>= 1
    # If the most significant bit of the result is 1, it indicates a negative number in 32-bit signed integer representation.   
    if s_i == 1:
        sum |= (-1 ^ mask)
    return sum

if __name__ == "__main__":
    # Test cases
    print("sum_of_integers", sum_of_integers(5, 3))  # Output: 8
    print("sum_of_integers", sum_of_integers(-2, 7))  # Output: 5
    print("sum_of_integers_v2", sum_of_integers_v2(5, 3))  # Output: 8
    print("sum_of_integers_v2", sum_of_integers_v2(-2, 7))  # Output: 5
    print("sum_of_integers", sum_of_integers(0, 0))  # Output: 0
    print("sum_of_integers_v2", sum_of_integers_v2(0, 0))  # Output: 0
    print("sum_of_integers", sum_of_integers(123, 456))  # Output: 579
    print("sum_of_integers_v2", sum_of_integers_v2(123, 456))  # Output: 579
    print("sum_of_integers", sum_of_integers(-123, -456))  # Output: -579
    print("sum_of_integers_v2", sum_of_integers_v2(-123, -456))  # Output: -579
    print("sum_of_integers", sum_of_integers(2147483647, 1))  # Output: -2147483648
    print("sum_of_integers_v2", sum_of_integers_v2(2147483647, 1))  # Output: -2147483648
    print("sum_of_integers", sum_of_integers(-2147483648, -1))  # Output: 2147483647
    print("sum_of_integers_v2", sum_of_integers_v2(-2147483648, -1))  # Output: 2147483647