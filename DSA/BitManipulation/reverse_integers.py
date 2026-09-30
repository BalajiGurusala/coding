'''
Given a 32-bit signed integer, reverse digits of an integer.

Input: 123
Output: 321

Input: -123
Output: -321

Input: 120
Output: 21
'''

def reverse_integer_v1(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = 0
    while x != 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    reversed_x *= sign
    # Check for 32-bit signed integer overflow
    if reversed_x < -2**31 or reversed_x > 2**31 - 1:
        return 0
    return reversed_x


def reverse_integer_recursive_v2(x):
    sign = -1 if x < 0 else 1
    x *= sign
    reversed_x = 0
    limit = 2**31 - 1 if sign > 0 else 2**31
    while x != 0:
        digit = x % 10
        # Check for potential overflow before updating reversed_x
        # This condition handles non python environments where integer overflow is possible
        if (reversed_x > limit // 10 or
                (reversed_x == limit // 10 and digit > limit % 10)):
            return 0
        reversed_x = reversed_x * 10 + digit
        x //= 10
    reversed_x *= sign
    return reversed_x


if __name__ == "__main__":
    print(reverse_integer_v1(123))
    print(reverse_integer_v1(-123))
    print(reverse_integer_v1(120)) 
    print(reverse_integer_v1(0))
    print(reverse_integer_v1(1534236469))  # Test for overflow case
    print(reverse_integer_recursive_v2(123))
    print(reverse_integer_recursive_v2(-123))
    print(reverse_integer_recursive_v2(120)) 
    print(reverse_integer_recursive_v2(0))
    print(reverse_integer_recursive_v2(1534236469))  # Test for overflow case