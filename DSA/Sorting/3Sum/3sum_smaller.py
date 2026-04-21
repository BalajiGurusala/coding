'''
3 Sum Smaller
Given a list of numbers, count the number of triplets having a 
sum less than a given target.

Input:
{
"target": 4,
"numbers": [5, 0, -1, 3, 2]
}
Output:
2
explanation:
{numbers[1], numbers[2], numbers[3]} and {numbers[1], numbers[2], numbers[4]} are the triplets having sum less than 4.

Input:
{
"target": 7,
"numbers": [2, 2, 2, 1]
}

Output:
4
explanation:
{numbers[0], numbers[1], numbers[2]}, 
{numbers[0], numbers[1], numbers[3]},
 {numbers[0], numbers[2], numbers[3]}
 and {numbers[1], numbers[2], numbers[3]} are the triplets having sum less than 7.
'''
def two_sum(numbers, target, start):
    ret = 0
    left = start
    right = len(numbers)-1

    while left < right:
        if numbers[left]+numbers[right] >= target:
            right -= 1
        else:
            ret += (right - left)
            left += 1
    return ret
            
def count_triplets(target, numbers):
    """
    Args:
     target(int32)
     numbers(list_int32)
    Returns:
     int32
    """
    # Write your code here.
    numbers.sort()
    result = 0
    for idx in range(len(numbers)-2):
        new_target = target - numbers[idx]
        ret = two_sum(numbers, new_target, idx+1)
        result += ret
    return result