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
    return array[middle] <= find_this_number

def solve(heroes, dragons):
    heroes.sort()
    # max_h = max(heroes)
    sum_h = sum(heroes)
    # print(heroes)
    for dragon in dragons:
        defense, attack = dragon
        index = binary_search_leftmost(heroes, defense)
        # print(f"hero {heroes[index]}")
        strong_sol = max(0, attack - (sum_h - heroes[index]))
        if heroes[index] < defense:
            strong_sol += defense - heroes[index]
        weak_sol = strong_sol
        if index != 0:
            weak_hero = heroes[index-1]
            weak_sol = defense - weak_hero
            weak_sol += max(0, attack - (sum_h - weak_hero))

        print(min(weak_sol, strong_sol))

import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n = int(input().decode().strip())
    heroes =[int(x) for x in input().decode().strip().split(" ")]
    m = int(input().decode().strip())
    dragons = []
    for i in range(m):
        defense,attack = [int(x) for x in input().decode().strip().split(" ")]
        dragons.append((defense,attack))

    a = solve(heroes, dragons)
