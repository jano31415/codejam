COUNT = 0
def submit(s):
    log(f"Query: {s}")
    print(s, flush=True)

def get_input():
    a = int(input())
    log(f"Answer: {a}")
    return a

def log(s):
    pass
    # print(s, file=f)

import math
def binary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array) - 1
    while left < right:
        middle = math.floor((left + right) / 2)

        if left == middle:
            middle = right
        try:
            check_res = check_smaller(array, left, middle, find_this_number)

            if left + 1 == right:
                if not check_res:
                    return right
                else:
                    return left

            if check_res:
                right = middle
            else:
                left = middle
        except Exception:
            return -1
    return left

def trinary_search_leftmost(array, find_this_number):
    left = 0
    right = len(array) - 1
    while True:
        middle1 = math.floor(left+(right - left) / 3)
        middle2 = math.floor(right-(right - left) / 3)
        if (left+1 == right) or (left==right):
            if left == 0:
                check_res = check_smaller(array, 0, 1, find_this_number)
                if check_res == 0:
                    return -1
                if check_res == 1:
                    return 0
                else:
                    return 1
            elif right == len(array) - 1:
                check_res = check_smaller(array, len(array)-2, len(array)-1, find_this_number)
                if check_res == 0:
                    return len(array)-3
                if check_res == 1:
                    return len(array)-2
                else:
                    return len(array)-1
            return left
        check_res = check_smaller(array, middle1, middle2, find_this_number)
        if check_res == 0:
            right = middle1
        elif check_res == 1:
            left = middle1
            right = middle2
        elif check_res == 2:
            left = middle2
    return left

def check_smaller(array, middle1, middle2, find_this_number):
    # might be slightly different if this is not an array
    submit(f"{array[middle1]} {find_this_number} {array[middle2]}")
    query_mid = get_input()
    if query_mid == array[middle1]:
        return 0
    elif query_mid == find_this_number:
        return 1
    elif query_mid == array[middle2]:
        return 2
    else:
        raise ValueError()


def solve():
    log(f"T {T} N {N} Q {Q}")
    submit(f"{1} {2} {3}")
    mid = int(get_input())
    l = [1, 2, 3]
    l.remove(mid)
    l = [l[0], mid, l[-1]]
    for i in range(4, N + 1):
        log(l)
        # submit(f"{l[0]} {i} {l[-1]}")
        # query_mid = get_input()
        # if query_mid == l[-1]:
        #     log(f"new biggest {i}")
        #     l.append(i)
        # elif query_mid == l[0]:
        #     log(f"new smallest {i}")
        #     l = [i] + l
        # else:
        if True:
            insert_point = trinary_search_leftmost(l, i) + 1
            l = l[:insert_point] + [i] + l[insert_point:]
            log(f"insert at {insert_point}")
    submit(" ".join([str(x) for x in l]))
    a=get_input()

def solve2():
    triple_list=[]
    for i in range(math.ceil(N/3)):
        submit(f"{3*i} {3*i+1} {3*i+2}")
        mid = int(get_input())
        l = [3*i, 3*i+1, 3*i+2]
        l.remove(mid)
        l = [l[0], mid, l[-1]]
        triple_list.append(l)
    while len(triple_list) > 1:
        for i in range(len(triple_list)//2):
            merge(triple_list[2*i], triple_list[2*i+1])

def merge(a,b):
    submit(f"{a[-2]} {a[-1]} {b[0]}")
    # this is also expensive
with open("interactive.txt", "w+") as f:
    T, N, Q = [int(x) for x in input().split(" ")]
    for t in range(T):
        solve()

