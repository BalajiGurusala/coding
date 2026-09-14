'''
Given a set of non-overlapping intervals sorted by their start time, insert a new interval into the list and merge if necessary.

Example:
Input: intervals = [[1,3],[6,9]], new_interval = [2,5]
Output: [[1,5],[6,9]]

Input: intervals = [[1,2],[3,5],[6,7], [8,10], [12, 15]], new_interval = [4,8]
Output: [[1,2],[3,10],[12,15]]

Input intervals = [], new_interval = [5,7]
Output: [[5,7]]
'''

def insert_new_interval(intervals, new_interval):

    result = []
    i = 0
    n = len(intervals)
    # Add all intervals ending before new_interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1

    # Merge all overlapping intervals with new_interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1

    result.append(new_interval)

    # Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result

def insert_new_interval_optimal(intervals, new_interval):
    result = []
    bail_index = 0
    n = len(intervals)

    for i in range(len(intervals)):
        # Add all intervals ending before new_interval starts
        if intervals[i][1] < new_interval[0]:
            result.append(intervals[i])
            bail_index += 1
        else:
            break

    #Add the new interval and merge if necessary
    result.append(new_interval)

    for i in range(bail_index, n):
        # Check if the current interval overlaps with the last interval in the result
        # If there is no overlap, add the current interval to the result
        if result[-1][1] < intervals[i][0]:
            result.append(intervals[i])
        else:
            # Merge the current interval with the last interval in the result
            result[-1] = [min(result[-1][0], intervals[i][0]), max(result[-1][1], intervals[i][1])]

    return result

if __name__ == "__main__":
    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print(insert_new_interval(intervals, new_interval))

    intervals = [[1,2],[3,5],[6,7], [8,10], [12, 15]]
    new_interval = [4,8]
    print(insert_new_interval(intervals, new_interval))

    intervals = []
    new_interval = [5,7]
    print(insert_new_interval(intervals, new_interval))

    print("Optimal approach:")

    intervals = [[1,3],[6,9]]
    new_interval = [2,5]
    print(insert_new_interval_optimal(intervals, new_interval))

    intervals = [[1,2],[3,5],[6,7], [8,10], [12, 15]]
    new_interval = [4,8]
    print(insert_new_interval_optimal(intervals, new_interval))

    intervals = []
    new_interval = [5,7]
    print(insert_new_interval_optimal(intervals, new_interval))
