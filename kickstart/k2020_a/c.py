# took me forever because i didnt think too much about the
# algorithm because i wanted to try some data structures
# so i first implemented a wrong algorithm using a heap :S


def solve(N, K, minutes):
    # calc length of training sessions
    diff_minutes = []
    for i, minute in enumerate(minutes):
        if i == 0:
            continue
        tmp = minute - minutes[i - 1]
        diff_minutes.append(tmp)

    # calc upper and lower bounds for the solution
    min_v = min(minutes)
    max_v = max(minutes)

    # if all N and K are equally distributed between the start
    # and endpoint of the whole training then the minimum of all
    # training session length is reached.
    left = max(1, ((max_v - min_v) // (N + K)) - 1)
    # worst case would be to ignore the existing N points in
    # the interval and just set the K points that we can chose
    # equally distributed.
    right = max(((max_v - min_v) // K) + 1, 1)

    # binary search to find minimum, we can check fast
    # how many new trainings we need to to not have session
    # lengths bigger than a certain number x (check_smaller)
    middle = binary_search_leftmost(diff_minutes, left, right, K)

    # good practice to do sanity checks if solution is correct
    # could be a real test if not written under time pressure
    # assert not check_smaller(diff_minutes, middle, K)
    # assert check_smaller(diff_minutes, max(middle-1, 1), K)
    return middle


import math


def binary_search_leftmost(array, left, right, K):
    while left < right:
        middle = math.floor((left + right) / 2)
        if check_smaller(array, middle, K):
            left = middle + 1
        else:
            right = middle
    return left


def check_smaller(array, middle, K):
    tot = 0
    for a in array:
        tot += max(0, math.ceil(a / middle) - 1)
    return tot > K


def main():
    T = int(input())
    for t in range(1, T + 1):
        N, K = [int(x) for x in input().split(" ")]

        minutes = [int(x) for x in input().split(" ")]
        res = solve(N, K, minutes)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


main()


################################
def check_speed():
    # create sample instance for the sizes of the test set
    # to check if algorithm scales correctly and iterate
    # over ideas how to speed it up
    from random import randint
    N, K = randint(10 ** 4, 10 ** 5), randint(10 ** 4, 10 ** 5)
    import time
    a = time.time()
    for _ in range(4):
        minutes = [randint(0, 10 ** 9) for _ in range(N)]
        minutes.sort()
        solve(N, K, minutes)
    b = time.time()
    print(b - a)

    # check vs straight forward solution solve2 to check if
    # fast solve function is still correct
    # assert solve(N, K, minutes, "b") == solve2(N, K, minutes)
# check_speed()
