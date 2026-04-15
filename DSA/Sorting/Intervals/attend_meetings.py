'''
Attend Meetings
Given a list of meeting intervals where each interval consists of a start and an end time, 
check if a person can attend all the given meetings such that only one meeting can be attended at a time.
{
"intervals": [
[1, 5],
[5, 8],
[10, 15]
]
}
Output:
return 1 if no overlapping intervals are found, otherwise return 0.
'''

'''
The below solution has time complexity of O(n log n) due to the sorting step 
and space complexity of O(1) as we are sorting the intervals in place.
Note: This solution accepts back to back meetings as non-overlapping, 
if you want to consider them as overlapping then you can change the condition in the 
if statement to if(intervals[i][1] >= intervals[i+1][0]):
'''

def can_attend_all_meetings(intervals):
    """
    Args:
     intervals(list_list_int32)
    Returns:
     int32
    """
    # Write your code here.
    intervals.sort(key=lambda x:x[0])
    print(intervals)
    for i in range(len(intervals)-1):
        if(intervals[i][1]>intervals[i+1][0]):
            print(intervals[i][1], intervals[i+1][0])
            return 0
    return 1