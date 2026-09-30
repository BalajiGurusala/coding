'''
Calculate the missing number in a list containing numbers from 0 to n with one number missing.

Example:
Input: [3, 0, 1]
Output: 2

Input: [0, 1]
Output: 2

Input: A list of integers nums containing numbers from 0 to n with one number missing.
Output: The missing number.

Time Complexity: O(n)
The function is O(n) because we iterate through the list once.
Space Complexity: O(1)
'''
def missing_number(nums):
    length = len(nums)
    n = 0
    for i in range(length + 1):
        n ^= i
    for num in nums:
        n ^= num
    return n

def missing_number_v2(nums):
    total = len(nums) * (len(nums) + 1) // 2
    return total - sum(nums)

if __name__ == "__main__":
    # Test cases
    print("missing_number", missing_number([3, 0, 1]))  # Output: 2
    print("missing_number", missing_number([2, 0, 1]))  # Output: 3
    print("missing_number", missing_number([1, 2, 3]))  # Output: 0 
    print("missing_number", missing_number([0, 2]))  # Output: 1
    print("missing_number", missing_number([9,6,4,2,3,5,7,0,1]))  # Output: 8
    print("missing_number", missing_number([0]))  # Output: 1
    print("missing_number", missing_number([1]))  # Output: 0

    print("missing_number_v2", missing_number_v2([3, 0, 1]))  # Output: 2
    print("missing_number_v2", missing_number_v2([2, 0, 1]))  # Output: 3
    print("missing_number_v2", missing_number_v2([1, 2, 3]))  # Output: 0 
    print("missing_number_v2", missing_number_v2([0, 2]))  # Output: 1
    print("missing_number_v2", missing_number_v2([9,6,4,2,3,5,7,0,1]))  # Output: 8
    print("missing_number_v2", missing_number_v2([0]))  # Output: 1
    print("missing_number_v2", missing_number_v2([1]))  # Output: 0 