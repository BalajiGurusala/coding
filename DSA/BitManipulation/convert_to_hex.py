'''
Convert an integer to its hexadecimal representation.

Example:
Input: 255
Output: "0xff"

Time Complexity: O(log n)
The function is O(logn) because each loop divides num by 16.
Space Complexity: O(1)
'''

def convert_to_hex(num):
    """
    Args:
     num(int): The input integer.
    Returns:
     str: The hexadecimal representation of the input integer.
    """
    hashmap = {0: "0", 1: "1", 2: "2", 3: "3", 4: "4", 5: "5", 6: "6", 7: "7",
               8: "8", 9: "9", 10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f"}
    result = []
    for _ in range(8):
        result.append(hashmap[num & 0xF])
        num >>= 4
        if num == 0:
            break

    return "0x" + "".join(reversed(result))

if __name__ == "__main__":
    print(convert_to_hex(255))  
    print(convert_to_hex(16))
    print(convert_to_hex(0))
    print(convert_to_hex(4095))
    print(convert_to_hex(65535))
    print(convert_to_hex(4294967295))  # Maximum 32-bit unsigned integer
    
                          