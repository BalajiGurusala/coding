'''
Given a list of trips where each trip consists of a start location, an end location, and the number of passengers, 
determine if it is possible to pick up and drop off all passengers without exceeding the vehicle's capacity at any 
point.

Example:
{
"trips": [
[2, 5, 3],
[3, 7, 4],
[5, 9, 2]
],
"capacity": 5
}
''' 

def car_pooling(trips, capacity):
    """
    Args:
     trips(list_list_int32)
     capacity(int32)
    Returns:
     bool
    """
    import heapq
    pq = []
    trips.sort(key=lambda x: x[0])
    current_passengers = 0
    for trip in trips:
        start, end, passengers = trip
        while pq and pq[0][0] <= start:
            _, p = heapq.heappop(pq)
            current_passengers -= p
        current_passengers += passengers
        if current_passengers > capacity:
            return False
        heapq.heappush(pq, (end, passengers))
    return True

def car_pooling_common_pattern(trips, capacity):
    import heapq
    pq = []
    trips.sort(key=lambda x: x[0])
    current_passengers = 0
    for i in range(len(trips)):
        if i == len(trips) - 1:
            next_start_time = float('inf')
        else:
            next_start_time = trips[i+1][0]

        start, end, passengers = trips[i]
        
        current_passengers += passengers
        
        if current_passengers > capacity:
            return False

        heapq.heappush(pq, (end, passengers))

        while pq and pq[0][0] <= next_start_time:
            _, p = heapq.heappop(pq)
            current_passengers -= p

    return True

if __name__ == "__main__":
    print("Car pooling possible for [[2, 5, 3], [3, 7, 4], [5, 9, 2]] with capacity 5:", car_pooling([[2, 5, 3], [3, 7, 4], [5, 9, 2]], 5))
    print("Car pooling possible for [[2, 5, 3], [3, 7, 4], [5, 9, 2]] with capacity 5 (common pattern):", car_pooling_common_pattern([[2, 5, 3], [3, 7, 4], [5, 9, 2]], 5))
    print("Car pooling possible for [[1, 4, 2], [2, 6, 3]] with capacity 4:", car_pooling([[1, 4, 2], [2, 6, 3]], 4))
    print("Car pooling possible for [[1, 4, 2], [2, 6, 3]] with capacity 4 (common pattern):", car_pooling_common_pattern([[1, 4, 2], [2, 6, 3]], 4))
    print("Car pooling possible for [[3, 5, 2], [4, 6, 3]] with capacity 3:", car_pooling([[3, 5, 2], [4, 6, 3]], 3))
    print("Car pooling possible for [[3, 5, 2], [4, 6, 3]] with capacity 3 (common pattern):", car_pooling_common_pattern([[3, 5, 2], [4, 6, 3]], 3))
    print("Car pooling possible for [[1, 2, 1], [2, 3, 2], [3, 4, 1]] with capacity 3:", car_pooling([[1, 2, 1], [2, 3, 2], [3, 4, 1]], 3))
    print("Car pooling possible for [[1, 2, 1], [2, 3, 2], [3, 4, 1]] with capacity 3 (common pattern):", car_pooling_common_pattern([[1, 2, 1], [2, 3, 2], [3, 4, 1]], 3))