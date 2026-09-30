'''
Check if an integer is a palindrome.

Input: 121
Output: True

Input: -121
Output: False

Input: 10
Output: False
'''

def is_palindrome_v1(x):
    if x < 0:
        return False
    original_x = x
    reversed_x = 0
    while x != 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10
    return original_x == reversed_x

def is_palindrome_v2(x):
    #half reversal approach
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reversed_half = 0
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    return x == reversed_half or x == reversed_half // 10
    # This approach only reverses half of the number to check for palindrome, 
    # which is more efficient for large numbers. 12321 would be detected as a palindrome after reversing half of it.
    # Example: For x = 12321, the loop will run until reversed_half = 123 and x = 12.
    # Then x == reversed_half // 10, confirming it is a palindrome.
    #1221 would be detected as a palindrome after reversing half of it.
    # Example: For x = 1221, the loop will run until reversed_half = 12 and x = 12.
    # Then x == reversed_half, confirming it is a palindrome.


if __name__ == "__main__":
    print(is_palindrome_v1(121))
    print(is_palindrome_v1(-121))
    print(is_palindrome_v1(10))
    print(is_palindrome_v2(121))
    print(is_palindrome_v2(-121))
    print(is_palindrome_v2(10))