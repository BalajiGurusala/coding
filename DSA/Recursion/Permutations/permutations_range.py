'''
Method,Logic,               Lookup                      Speed,Memory
String Scan -              O(N)                       Best (O(1) extra)
(if str(i) not in current_string)
Used Array                  O(1)                      Good (O(K) extra)
(if not used[i])
Slicing                     N/A                         Worst (O(N2) extra)
(new_array = array[:i] + array[i+1:])
'''


#Permutations using Recursion with repetition allowed

def permutations(n, current_string='', result=None):
    if result is None:
        result = []
    if n == 0:
        result.append(current_string)
        return result

    for i in range(0,10):
        permutations(n-1, current_string + str(i), result)
    return result

print(permutations(2))

''' Permutations using Recursion with repetition not allowed '''

def permutationsNoRepetition(n, current_string='', result=None):
    if result is None:
        result = []
    if n == 0:
        result.append(current_string)
        return result

    for i in range(0,10):
        if str(i) not in current_string:
            permutationsNoRepetition(n-1, current_string + str(i), result)
    return result

print(permutationsNoRepetition(2))

def permutationsNoRepetition_v2(n, current_string='', result=None, array=None  ):
    if result is None:
        result = []
    if array is None:
        array = [i for i in range(10)]
    if n == 0:
        result.append(current_string)
        return result

    for i in range(len(array)):
        new_array = array[:i] + array[i+1:]
        permutationsNoRepetition_v2(n-1, current_string + str(array[i]), result, new_array)
    return result   

print(permutationsNoRepetition_v2(2))

def permutationsNoRepetition_v3(n, current_string='', result=None, used=None):
    if result is None:
        result = []
    if used is None:
        used = [False] * 10
    if n == 0:
        result.append(current_string)
        return result

    for i in range(10):
        if not used[i]:
            used[i] = True
            permutationsNoRepetition_v3(n-1, current_string + str(i), result, used)
            used[i] = False
    return result

print(permutationsNoRepetition_v3(2))

'''
Handling Multi-Digit Numbers
If we use current_string like above, len("1023") is 4, even though it only represents two numbers from the array [10, 23].
The String problem: You lose the boundary between numbers. You can't tell if "1023" was [10, 2, 3] or [1, 0, 23].
The List advantage: path = [10, 23] always has a length of 2. It preserves the "integrity" of the original data types.
'''

def permutationsNoRepetition_v4(n, slate=None, result=None, used=None):
    if result is None:
        result = []

    if used is None:
        used = [False] * 10

    if slate is None:
        slate = []

    if n == 0:
        result.append(''.join(map(str, slate)))
        return result

    for i in range(10):
        if not used[i]:
            used[i] = True
            slate.append(i)
            permutationsNoRepetition_v4(n-1, slate, result, used)
            slate.pop()
            used[i] = False
    return result