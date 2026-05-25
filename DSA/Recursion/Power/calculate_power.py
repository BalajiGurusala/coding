'''
'''

def calculate_power(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    return cal_power_helper(a,b)

def cal_power_helper(a,b):
    if a == 0:
        return 0
    if b == 0 or a == 1:
        return 1
    result = a * cal_power_helper(a, b-1)
    
    return result%1000000007
print(calculate_power(2, 3))


def calculate_power_optimal(a, b):
    """
    Args:
     a(int64)
     b(int64)
    Returns:
     int32
    """
    # Write your code here.
    return cal_power_helper_optimal(a,b)

def cal_power_helper_optimal(a,b):
    if a == 0:
        return 0
    if b == 0 or a == 1:
        return 1
        
    half_powered = cal_power_helper_optimal(a, b//2)
    half_powered_squared = (half_powered * half_powered)%1000000007
    
    if b%2 !=0:
        return (half_powered_squared * a)%1000000007
    else:
        return (half_powered_squared)%1000000007
    
print(calculate_power_optimal(2, 1000000000))