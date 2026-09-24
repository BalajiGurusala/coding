'''
Given a list of employees' schedules, where each employee's schedule is a list of non-overlapping intervals sorted by start time, find the common free time intervals across all employees.

Example:
Input: schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
Output: [[5,6],[7,9]]

Input: schedule = [[[1,2], [5,6]], [[1,3]], [[4,10]]]
Output: [[3,4]]
'''

from math import inf


def free_times(schedule):
    if not schedule:
        return []

    # Flatten all intervals and sort by start time
    all_intervals = [interval for employee in schedule for interval in employee]
    all_intervals.sort(key=lambda x: x[0])

    merged_intervals = [all_intervals[0]]
    for i in range(1, len(all_intervals)):
        if all_intervals[i][0] <= merged_intervals[-1][1]:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], all_intervals[i][1])
        else:
            merged_intervals.append(all_intervals[i])

    free_times = []
    for i in range(0, len(merged_intervals)-1):
        free_times.append([merged_intervals[i][1], merged_intervals[i+1][0]])

    return free_times

def free_times_min_heap(schedule):
    if not schedule:
        return []

    import heapq
    min_heap = []
    for employee in schedule:
        for interval in employee:
            heapq.heappush(min_heap, (interval[0], interval[1]))

    merged_intervals = [[-inf, -inf]]
    while min_heap:
        start, end = heapq.heappop(min_heap)
        # If the current interval does not overlap with the last merged interval, add it as a new merged interval.
        #No overlap with the last merged interval
        if merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

    free_times = []
    for i in range(1, len(merged_intervals)-1):
        free_times.append([merged_intervals[i][1], merged_intervals[i+1][0]])

    return free_times

def free_times_min_heap_optimized(schedule):
    if not schedule:
        return []

    min_heap = []
    import heapq
    for employee in schedule:
        heapq.heappush(min_heap, (employee[0][0], employee[0][1], employee, 0))
    # The min_heap now contains the first interval of each employee along with a reference to the 
    # employee and the position of the interval.
    merged_intervals = [[-inf, -inf]]
    while min_heap:
        start, end, employee, pos = heapq.heappop(min_heap)
        if merged_intervals[-1][1] < start:
            merged_intervals.append([start, end])
        else:
            merged_intervals[-1][1] = max(merged_intervals[-1][1], end)

        if pos + 1 < len(employee):
            heapq.heappush(min_heap, (employee[pos+1][0], employee[pos+1][1], employee, pos+1))

    free_times = []
    for i in range(1, len(merged_intervals)-1):
        free_times.append([merged_intervals[i][1], merged_intervals[i+1][0]])

    return free_times

if __name__ == "__main__":
    schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
    print(free_times(schedule))

    schedule = [[[1,2], [5,6]], [[1,3]], [[4,10]]]
    print(free_times(schedule))

    print("min heap approach:")

    schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
    print(free_times_min_heap(schedule))

    schedule = [[[1,2], [5,6]], [[1,3]], [[4,10]]]
    print(free_times_min_heap(schedule))

    print("min heap optimized approach:")

    schedule = [[[1,2], [5,6]], [[1,3]], [[4,10]]]
    print(free_times_min_heap_optimized(schedule))

    schedule = [[[1,3],[6,7]], [[2,4]], [[2,5],[9,12]]]
    print(free_times_min_heap_optimized(schedule))
