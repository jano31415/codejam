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

def test_binary_search_leftmost():
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
