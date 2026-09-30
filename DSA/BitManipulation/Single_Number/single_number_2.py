'''
Calculate the single number in a list where every element appears three times except for one.

Example:
Input: [4, 1, 2, 1, 2, 2, 1]
Output: 4

Input: [2, 2, 3, 2 ]
Output: 3

Input: A list of integers nums.
Output: The single number that appears only once.

Time Complexity: O(n)
The function is O(n) because we iterate through the list once.
Space Complexity: O(1)
'''

def single_number_v1(nums):
    zeros = -1
    ones = 0
    twos = 0
    for num in nums:
        new_zeros = (zeros & ~num) | (twos & num)
        new_ones = (ones & ~num) | (zeros & num)
        new_twos = (twos & ~num) | (ones & num)    
        zeros, ones, twos = new_zeros, new_ones, new_twos
    return ones

if __name__ == "__main__":
    # Test cases
    print("single_number_v1", single_number_v1([4, 1, 2, 1, 2, 2, 1]))  # Output: 4
    print("single_number_v1", single_number_v1([2, 2, 3, 2]))  # Output: 3

    