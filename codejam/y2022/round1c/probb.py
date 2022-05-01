import numpy as np

def solve1(n,k,numbers):
    sumv = sum(numbers)
    sq = sum([x**2 for x in numbers])
    if sumv == 0:
        if sq ==0:
            return 1
        else:
            return "IMPOSSIBLE"
    k = (sq-sumv**2)//(2*sumv)
    new_numbers = numbers[:]
    new_numbers.append(k)
    sum_new2 = sum(new_numbers)**2
    sq2 = sum([x**2 for x in new_numbers])
    if sum_new2 == sq2:
        return k
    return "IMPOSSIBLE"


def solve2(n,k,numbers):
    ks = []
    k1 = 1-sum(numbers)
    sq =sum([x**2 for x in numbers])
    new_numbers = numbers[:]
    new_numbers.append(k1)
    sq_new = sq + k1**2
    res = solve1(n+1, 1, new_numbers)
    if res == "IMPOSSIBLE":
        return res
    return " ".join([str(k1), str(res)])



if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n, k = [int(x) for x in input().split(" ")]
        numbers = [int(x) for x in input().split(" ")]
        if k == 1:
            res = solve1(n, k, numbers)
            print("Case #{i}: {res}".format(i=t, res=res), flush=True)
        else:
            res = solve2(n, k, numbers)
            print("Case #{i}: {res}".format(i=t, res=res), flush=True)


