'''
Given a list of intervals, merge all overlapping intervals and return the merged list.

Example:
Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
'''

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for current in intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            last[1] = max(last[1], current[1])
        else:
            merged.append(current)

    return merged


if __name__ == "__main__":
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    print(merge_intervals(intervals))

    intervals = [[1,4],[4,5],[6,7]]
    print(merge_intervals(intervals))

    intervals = [[1, 10], [2, 3], [4, 5]]
    print(merge_intervals(intervals))
