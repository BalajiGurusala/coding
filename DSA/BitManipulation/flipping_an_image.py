'''
Flip an image horizontally and invert it.

Example:
Input: [[1,1,0],[1,0,1],[0,0,0]]
Output: [[1,0,0],[0,1,0],[1,1,1]]

Input: A 2D list representing the image.
Output: The 2D list after flipping horizontally and inverting.

Time Complexity: O(n*m)
The function is O(n*m) because we process each element of the image.
Space Complexity: O(1)
'''

def flip_and_invert_image(image):
    """
    Args:
     image(list[list[int]]): The 2D list representing the image.
    Returns:
     list[list[int]]: The 2D list after flipping horizontally and inverting.
    """
    for row in image:
        row.reverse()
        for i in range(len(row)):
            row[i] ^= 1
    return image

def flip_and_invert_image_v2(image):
    """
    Args:
     image(list[list[int]]): The 2D list representing the image.
    Returns:
     list[list[int]]: The 2D list after flipping horizontally and inverting.
    """
    for row in image:
        left, right = 0, len(row) - 1
        while left <= right:
            if left == right:
                row[left] ^= 1
            else:
                row[left], row[right] = row[right] ^ 1, row[left] ^ 1
            left += 1
            right -= 1
    return image

if __name__ == "__main__":
    print(flip_and_invert_image([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]
    print(flip_and_invert_image_v2([[1,1,0],[1,0,1],[0,0,0]]))  # Output: [[1,0,0],[0,1,0],[1,1,1]]