'''
Given a collection of numbers, return all possible permutations.
For example, given [1,2,3], the permutations are:
[1,2,3], [1,3,2], [2,1,3], [2,3,1], [3,1,2], and [3,2,1].
'''

def permutations_no_repetition_distinct_v1(n,array, current_string='', result=None, used=None):
    if result is None:
        result = []

    if used is None:
        used = [False] * len(array)

    if n == 0:
        #result.append(slate[:])
        #result.append(list(slate)) # if we want to return list of lists instead of list of arrays   
        #for string output we can do result.append(''.join(map(str, slate)))
        result.append(current_string) # if we want to return list of strings instead of list of lists
        return result

    for i in range(len(array)):
        if not used[i]:
            used[i] = True
            permutations_no_repetition_distinct_v1(n-1, array, current_string + str(array[i]), result, used)
            used[i] = False
    return result

print(permutations_no_repetition_distinct_v1(3, [1,2,3]))

def permutations_no_repetition_distinct_v2(array, slate=None, result=None, used=None):
    if result is None:
        result = []

    if slate is None:
        slate = []

    if used is None:
        used = [False] * len(array)

    if len(slate) == len(array):
        #result.append(slate[:])
        #result.append(list(slate)) # if we want to return list of lists instead of list of arrays   
        #for string output we can do result.append(''.join(map(str, slate)))
        result.append(''.join(map(str, slate))) # if we want to return list of strings instead of list of lists
        return result

    for i in range(len(array)):
        if not used[i]:
            used[i] = True
            slate.append(array[i])
            permutations_no_repetition_distinct_v2(array, slate, result, used)
            slate.pop()
            used[i] = False
    return result

print(permutations_no_repetition_distinct_v2([1,2,3]))