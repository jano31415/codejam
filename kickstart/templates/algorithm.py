# binary search algorithm template from wikipedia

import math
def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array)-1
    while left < right:
        middle = math.floor((left + right) / 2)
        if check_smaller(array, middle, find_this_number):
            left = middle + 1
        else:
            right = middle
    return left

def check_smaller(array, middle, find_this_number):
    # might be slightly different if this is not an array
    return array[middle] < find_this_number

def t_binary_search_leftmost():
    array1 = [1, 5, 36, 37, 37, 37, 63, 74, 83, 86, 90, 90, 96]
    res1 = binary_search_leftmost(array1, 37)
    assert res1 == 3
    from random import randint
    array = sorted([randint(0,100) for x in range(10)])
    res_index = binary_search_leftmost(array, 37)
    if 37 in array:
        assert array[res_index] == 37
    else:
        assert array[max(res_index-1, 0)] < 37
        assert array[min(res_index+1, 999)] > 37

# sieve of the eratosthenes
def sieve(max_p):
    primes = [2, 3]
    for i in range(5,max_p):
        is_prime=True
        for p in primes:
            if i%p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
    return primes

#lob_b(n), looks slow
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def difference_array(arr2, l, r, v):
    # create a difference array
    diff = [arr2[0]] + [arr2[i] - arr2[i - 1] for i in range(1, len(arr2))]
    # update the range by adding the value for the first and then subtracting it
    # at the end of the range
    for i in range(len(l)):
        diff[l[i]] += v[i]
        diff[r[i]] -= v[i]

    # reconstruct the updated array
    for i in range(len(arr2)):
        if i == 0:
            arr2[0] = diff[0]
        else:
            arr2[i] = diff[i] + arr2[i - 1]
    return arr2

def t_difference_array():
    # difference array
    # if you need to range update arrays
    import random
    rint = random.randint
    n1 = 10000
    n2 = n1//2
    l = [rint(0, n1-2) for _ in range(n2)]
    r = [li + rint(1, n1-1 - li) for li in l]
    v = [rint(1, 10) for _ in range(n2)]
    arr = list(range(n1))
    import time
    a =time.time()
    for i in range(n2):
        for j in range(l[i],r[i]):
            arr[j] += v[i]
    b=time.time()
    print(f"naiv implementation {b-a}")

    arr2 = list(range(n1))
    import time
    a =time.time()
    arr2 = difference_array(arr2, l, r, v)
    b=time.time()
    print(f"difference array {b-a}")

    assert arr2 == arr
