'''
Given two lists of intervals, find the intersection of these intervals.

Example:
Input: firstList = [[1,3],[5,6],[7,9]], secondList = [[2,3],[5,7]]
Output: [[2,3],[5,6],[7,7]]

Input: firstList = [[0,2], [5,10], [13,23], [24,25]], secondList = [[1,5], [8,12], [15,24], [25,26]]
Output: [[1,2], [5,5], [8,10], [15,23], [24,24], [25,25]]
'''

def interval_intersection(firstList, secondList):
    i, j = 0, 0
    result = []
    merged_intervals = []
    while i < len(firstList) and j < len(secondList):
        merged_intervals.append(firstList[i])
        i+=1
        merged_intervals.append(secondList[j])
        j+=1

    while i < len(firstList):
        merged_intervals.append(firstList[i])
        i += 1
    while j < len(secondList):
        merged_intervals.append(secondList[j])
        j += 1

    merged_intervals.sort(key=lambda x: x[0])

    for i in range(len(merged_intervals) - 1):
        if merged_intervals[i][1] >= merged_intervals[i + 1][0]:
            result.append([max(merged_intervals[i][0], merged_intervals[i + 1][0]), 
                           min(merged_intervals[i][1], merged_intervals[i + 1][1])])
    return result

def interval_intersection_optimal(firstList, secondList):

    i , j = 0, 0
    result = []

    while i < len(firstList) and j < len(secondList):

        if firstList[i][1] >= secondList[j][0] and secondList[j][1] >= firstList[i][0]:
            result.append([max(firstList[i][0], secondList[j][0]), min(firstList[i][1], secondList[j][1])])

        if firstList[i][1] <= secondList[j][1]:
            i += 1
        else:
            j += 1

    return result

if __name__ == "__main__":
    firstList = [[1,3],[5,6],[7,9]]
    secondList = [[2,3],[5,7]] 
    print(interval_intersection(firstList, secondList))
    print(interval_intersection_optimal(firstList, secondList))

    firstList = [[0,2], [5,10], [13,23], [24,25]]
    secondList = [[1,5], [8,12], [15,24], [25,26]]
    print(interval_intersection(firstList, secondList))
    print(interval_intersection_optimal(firstList, secondList))