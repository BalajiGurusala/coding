'''
How Many Binary Search Trees With N Nodes
Given an integer n, return the number of structurally unique binary search trees (BST) 
that can be formed using values from 1 to n.
input: 
{
"n": 1
}
output: 1
(1)

input: 
{"n": 2
}
output: 2
 (2)            (1)
  /       and       \
(1)                  (2)

input:  
{"n": 3
}
output: 5
       (3)
      /
    (2)
   /
(1)

   (3)
  /
(1)
   \
   (2)

(1)
   \
    (2)
      \
       (3)

(1)
   \
    (3)
   /
(2)

   (2)
  /   \
(1)    (3)
'''


def how_many_bsts(n):
    """
    Args:
     n(int32)
    Returns:
     int64
    """
    # Write your code here.
    return bsts_helper(n)
    
def bsts_helper(n):
    
    if n <= 1:
        return 1
    
    total_bsts = 0
    for i in range(1, n+1):
        left_bsts = i-1
        right_bsts = n-i
        
        left_comb = bsts_helper(left_bsts)
        right_comb = bsts_helper(right_bsts)
        
        total_bsts += left_comb * right_comb
    
    return total_bsts

print(how_many_bsts(1))
print(how_many_bsts(2))
print(how_many_bsts(3))
print(how_many_bsts(4))
print(how_many_bsts(5))