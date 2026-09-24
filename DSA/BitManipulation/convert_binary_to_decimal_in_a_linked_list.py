'''
Convert a binary number represented as a linked list to its decimal equivalent.

Example:
Input: 1 -> 0 -> 1
Output: 5

Time Complexity: O(n) where n is the number of nodes in the linked list.
Space Complexity: O(1) as we are not using any extra space.
'''

def convert_binary_to_decimal(head):
    """
    Args:
     head(ListNode): The head of the linked list representing the binary number.
    Returns:
     int: The decimal equivalent of the binary number.
    """
    decimal_value = 0
    current = head
    while current:
        decimal_value = (decimal_value << 1) | current.val
        current = current.next
    return decimal_value

if __name__ == "__main__":
    class ListNode:
        def __init__(self, val=0, next=None):
            self.val = val
            self.next = next

    # Example usage:
    head = ListNode(1, ListNode(0, ListNode(1)))
    print(convert_binary_to_decimal(head))  # Output: 5

    # Another example usage:
    head = ListNode(1, ListNode(1, ListNode(0)))
    print(convert_binary_to_decimal(head))  # Output: 6