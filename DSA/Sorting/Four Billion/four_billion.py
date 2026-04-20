'''Given four billion of 32-bit integers, return any one that’s not among them. 
Assume you have 1 GiB (10243 bytes) of memory.
Follow up: what if you only have 10 MiB of memory?
Input:
{
"arr": [0, 1, 2, 3]
}
Output:
4 or any other integer that is not in the input array.
'''


from array import array

def find_integer_2pow_32(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    # 2**32 bits = 2**32//8 = 2**29 Bytes
    bytearray_var = bytearray(2**29)
    
    for num in arr:
        #byte index
        byte_index = num >> 3 # num//8 gives byte index
        bit_index = num & 7 # num%8 gives bit nidex num%8 can also be done as num & 7 (i.e num % 2**n is num & 2**n -1 )
        
        bytearray_var[byte_index] |= (1 << bit_index)
        
    
    for idx, byte_var in enumerate(bytearray_var):
        if byte_var != 0xFF: #0XFF is all bits set in the byte. which means all the numbers for that byte index are present
            for bit in range(8):
                if not (byte_var & (1 << bit)):
                    missing_num = (idx << 3) | bit #idx << 3 gives byte index and | with (bit) sets the bit
                    return missing_num
    return None

def find_integer_10mb(arr):
    """
    Args:
     arr(list_int64)
    Returns:
     int64
    """
    # Write your code here.
    # 2**32 is divided into 2**16 blocks of 2**16 numbers each. 
    # we need 2**16 * 4 bytes to store the count of numbers in each block. which is 2**18 bytes = 256KB (Pass 1). 
    # So we can use a bytearray of size 256KB to store the count of numbers in each block (Pass1).  
    # We can use 2**16 bits to represent the presence of numbers in each block. 
    # 2**16 bits = 2**16//8 = 2**13 bytes = 8KB (Pass 2). So we can use a 
    # bytearray of size 8KB to represent the presence of numbers in each block. 
    # We can then iterate through the input array and set the 
    # corresponding bit in the bytearray for each number

    num_buckets = 2**16
    buckets = array.array('I', [0]*num_buckets) # 4 bytes for each bucket to store the count of numbers in each block

    for num in arr:
        bucket_index = num >> 16 # num//2**16 gives the bucket index
        buckets[bucket_index] += 1
    
    # Find the bucket which has less than 2**16 numbers. This means that there is at least one number missing in that bucket.
    missing_bucket_index = -1
    for i in range(num_buckets):
        if buckets[i] < 2**16: 
            # if the count of numbers in the bucket is less than 2**16, 
            # then there is at least one number missing in that bucket
            missing_bucket_index = i
            break
    
    if missing_bucket_index == -1:
        # This means that all the buckets are full, which means that there is no missing number in the input array. 
        return None
    
    bytearray_var = bytearray(2**13) 
    # 2**16 bits = 2**13 bytes = 8KB to represent the presence of numbers in the missing bucket 

    #Find the missing number in the missing bucket by iterating 
    # through the input array again and setting the corresponding bit 
    # in the bytearray for each number in the missing bucket.
    for num in arr:
        bucket_index = num >> 16 # num//2**16 gives the bucket index
        if bucket_index == missing_bucket_index:
             # if the number belongs to the missing bucket, then we set the corresponding bit in the bytearray
             offset = num & 0xFFFF # num%2**16 gives the bit index within the bucket
             # Use the lower 16 bits as the local offset
             #num % 2**16 can also be done as num & 0xFFFF (i.e num % 2**n is num & 2**n -1 )
             bytearray_var[offset >> 3] |= (1 << (offset & 7)) # set the corresponding bit in the bytearray
    
          
    for idx, byte_var in enumerate(bytearray_var):
        if byte_var != 0xFF: #0XFF is all bits set in the byte. which means all the numbers for that byte index are present
            for bit in range(8):
                if not (byte_var & (1 << bit)):
                    missing_num = (missing_bucket_index << 16) | ((idx << 3) | bit) #idx << 3 gives byte index and | with (bit) sets the bit
                    return missing_num
    return None