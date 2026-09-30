'''
Given an integer array nums, in which exactly two elements appear only once
and all the other elements appear exactly twice. Find the elements that appear only once and return

Input: [1,2,1,3,2,5]
Output: [3,5] or [5.3]

Input: [-1, 0]
Ouput: [-1,0]
'''

def single_number_3(nums):

    # Step 1: XOR all numbers to get xor of the two unique numbers
    odd = 0
    for num in nums:
        odd ^= num
        
    # Step 2: Find a bit that is set in xor (this bit is different between the two unique numbers)
    # A 1 in the XOR means the two numbers differ at that bit. The code isolates the rightmost such bit:
    # This isolates the rightmost set bit, which is different between the two unique numbers
    # odd = XOR of the two unique numbers, If Input = [1,2,1,3,2,5] then odd = 3 ^ 5
    # 011 ^ 101 = 110 (odd). Between 3 and 5, the rightmost set bit is at 
    # position 1 (0-indexed from the right). 
    # Why only right most set bit? Because any set bit would work, but the rightmost set bit is easy to isolate using `odd & -odd`.  
    #why we are using `odd & -odd` is to isolate the rightmost set bit which helps in dividing the numbers into two groups.
    #why dividing numbers into two groups works? Because the two unique numbers will fall into different groups 
    # based on the isolated bit, and all other numbers appearing twice will cancel each other out within their respective groups.
    diff = odd & -odd

    # Step 3: Divide numbers into two groups and XOR separately
    # In step 2: we found the rightmost set bit (diff) which helps us divide the numbers into two groups.
    # In order for XOR to be set, the numbers must differ at the bit position indicated by `diff`. 
    # This ensures that the two unique numbers will end up in different groups.
    # All other numbers appearing twice will cancel each other out within their respective groups.
    # Thse two groups will be grouped in to either 0 or 1 based on the isolated bit. 
    res = [0, 0]
    for num in nums:
        if num & diff:
            res[0] ^= num
        else:
            res[1] ^= num
    return res

if __name__ == "__main__":
    print(single_number_3([1,2,1,3,2,5]))
    print(single_number_3([-1, 0]))
    print(single_number_3([4,1,2,1,2,5]))
    print(single_number_3([0, 0, 7, 8]))