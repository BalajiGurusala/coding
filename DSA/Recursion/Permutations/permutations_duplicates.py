'''
Given a collection of numbers that might contain duplicates, return all possible permutations.
For example, given [1,1,2], the permutations are:
[1,1,2], [1,2,1], and [2,1,1].
'''
def permutations_no_repetition_duplicates_v1(n,array, current_string='', result=None, used=None):
    if result is None:
        result = []

    if used is None:
        used = [False] * len(array)
        array.sort() # sort the array to handle duplicates

    if n == 0:
        result.append(current_string)
        return result

    for i in range(len(array)):
        if not used[i]:
            if i > 0 and array[i] == array[i-1] and not used[i-1]:
                continue
            used[i] = True
            permutations_no_repetition_duplicates_v1(n-1, array, current_string + str(array[i]), result, used)
            used[i] = False
    return result

print(permutations_no_repetition_duplicates_v1(3, [1,2,1]))


def permutations_no_repetition_duplicates_v2(n,array, slate=None, result=None, used=None):
    if result is None:
        result = []

    if used is None:
        used = [False] * len(array)
        array.sort() # sort the array to handle duplicates

    if slate is None:
        slate = []

    if n == 0:
        result.append(''.join(map(str, slate)))
        return result

    for i in range(len(array)):
        if not used[i]:
            if i > 0 and array[i] == array[i-1] and not used[i-1]:
                continue
            used[i] = True
            slate.append(array[i])
            permutations_no_repetition_duplicates_v2(n-1, array, slate, result, used)
            slate.pop()
            used[i] = False
    return result

print(permutations_no_repetition_duplicates_v2(3, [1,2,1]))