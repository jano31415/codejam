import math
def solve(N,numbers):
    numbers2 = [x for x in numbers if x%2 ==0]
    numbers_not2 = [x for x in numbers if x%2 !=0]
    numbers_new = numbers2 + numbers_not2
    # assert len(numbers_new) == len(numbers)
    tot = 0
    for i,ai in enumerate(numbers_new):
        for j in range(i+1, len(numbers_new)):
            aj = 2*numbers_new[j]
            if math.gcd(ai,aj) > 1:
                tot+=1
    return tot


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        numbers = [int(x) for x in input().split(" ")]
        res = solve(N, numbers)
        print(str(res), flush=True)