'''
Given a point (p_x, p_y) and a list of points n_points, 
return the k nearest neighbors to the point (p_x, p_y) from the list n_points.
Input:
{
"p_x": 0,
"p_y": 0,
"k": 2,
"n_points": [[1, 2], [3, 4], [1, 1], [2, 2]]
}
Output:
[[1, 1], [1, 2]] or [[1, 2], [1, 1]] or [[2, 2], [1, 1]] or [[2, 2], [1, 2]]
'''
def nearest_neighbours(p_x, p_y, k, n_points):
    """
    Args:
     p_x(int32)
     p_y(int32)
     k(int32)
     n_points(list_list_int32)
    Returns:
     list_list_int32
    """
    # Write your code here.
    heap = []
    result = []
    import heapq
    from math import sqrt
    def euclidean_distancxe(p_x, p_y, n_x, n_y):
        return sqrt((p_x-n_x)**2 + (p_y-n_y)**2)
    
    for i in range(len(n_points)):
        n_x, n_y = n_points[i][0], n_points[i][1]
        dist = euclidean_distancxe(p_x, p_y, n_x, n_y)
        heapq.heappush(heap, (-dist, i))
        if(len(heap)>k):
            heapq.heappop(heap)
    
    while len(heap):
        dist, idx = heapq.heappop(heap)
        result.append(n_points[idx])
        
    return result