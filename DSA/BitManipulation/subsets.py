'''
Generate all subsets of a given set using bit manipulation.

Example:
Input: [1, 2, 3]
Output: [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]

Time Complexity: O(n * 2^n)
The function is O(n * 2^n) because there are 2^n subsets and generating each subset takes O(n) time.
Space Complexity: O(1) (excluding the space for the output)
Output space complexity is O(2^n) for storing all subsets.
'''
from random import choice


def generate_subsets(nums):
    """
    Args:
     nums(list): The input list of numbers.
    Returns:
     list: A list of all subsets of the input list.
    """
    n = len(nums)
    result = []
    # Iterate over all possible combinations of elements represented by bits
    # There are 2^n possible subsets, represented by numbers from 0 to 2^n - 1
    # 1 << n is equivalent to 2^n, representing the total number of subsets
    #1 << 3 == 8  # 2^3 = 8, representing the total number of subsets for a set of size 3
    #range(8)  # 0 through 7
    for i in range(1 << n):
        slate = []
        j = i
        #p = len(nums)-1
        p =0
        # Iterate over each bit position to determine which elements to include in the current subset
        # if j & 1 == 1, include the corresponding element in the current subset
        # Check each bit of j to decide whether to include the corresponding element in the subset
        # if j is 0, we have processed all bits and determined all elements to include in the current subset
        while j != 0:
            #inclusion_choice
            if j & 1 == 1:
                slate.append(nums[p])
            j >>= 1
            #p -= 1
            p += 1
        result.append(slate)
    return result

if __name__ == "__main__":
    print(generate_subsets([1, 2, 3]))
    # print(generate_subsets([4, 5]))
    # print(generate_subsets([]))
    # print(generate_subsets([1]))
    # print(generate_subsets([1, 2, 3, 4]))
    # print(generate_subsets([1, 2, 3, 4, 5]))
    # print(generate_subsets([1, 2, 3, 4, 5, 6]))
    # print(generate_subsets([1, 2, 3, 4, 5, 6, 7]))
    # print(generate_subsets([1, 2, 3, 4, 5, 6, 7, 8]))

