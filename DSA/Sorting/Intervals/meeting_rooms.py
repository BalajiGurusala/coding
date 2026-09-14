'''
Minimum Meeting Rooms Required.
Given a list of meeting intervals where each interval consists of a start and an end time, 
check if how many meeting rooms are required to accommodate all the given meetings.
"intervals": [
[0, 30]
[1, 5],
[5, 8],
[10, 15]
]
}
Output:
return the minimum number of meeting rooms required to accommodate all the given meetings.
'''

def meeting_rooms(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    import heapq
    heap = []
    heapq.heappush(heap, intervals[0][1])
    for i in range(1, len(intervals)):
        if intervals[i][0] >= heap[0]:
            heapq.heappop(heap)
        heapq.heappush(heap, intervals[i][1])
    return len(heap)

def meeting_rooms_common_pattern(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda x: x[0])
    import heapq
    pq = []
    global_max = 0
    for i in range(len(intervals)):
        if i == len(intervals) - 1:
            next_start_time = float('inf')
        else:
            next_start_time = intervals[i+1][0]

        heapq.heappush(pq, intervals[i][1])

        global_max = max(global_max, len(pq))

        while pq and pq[0] <= next_start_time:
            heapq.heappop(pq)

    return global_max

if __name__ == "__main__":
    print("Minimum meeting rooms required for [[0, 30], [1, 5], [5, 8], [10, 15]]:", meeting_rooms([[0, 30], [1, 5], [5, 8], [10, 15]]))
    print("Minimum meeting rooms required for [[1, 5], [2, 3], [4, 6]]:", meeting_rooms([[1, 5], [2, 3], [4, 6]]))
    print("Minimum meeting rooms required for [[1, 5], [5, 8], [8, 10]]:", meeting_rooms([[1, 5], [5, 8], [8, 10]]))

    print("Minimum meeting rooms required for [[0, 30], [1, 5], [5, 8], [10, 15]] (common pattern):", meeting_rooms_common_pattern([[0, 30], [1, 5], [5, 8], [10, 15]]))
    print("Minimum meeting rooms required for [[1, 5], [2, 3], [4, 6]] (common pattern):", meeting_rooms_common_pattern([[1, 5], [2, 3], [4, 6]]))
    print("Minimum meeting rooms required for [[1, 5], [5, 8], [8, 10]] (common pattern):", meeting_rooms_common_pattern([[1, 5], [5, 8], [8, 10]]))