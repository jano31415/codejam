def solve(n,arr):
    sol = ["0"]*n
    nr_ones = sum(arr)//n
    nr_zeros = n - nr_ones

    # arr[i] = i*sol[i] + (i-ith_zero)
    for x in range(nr_zeros, n):
        arr[x] -= (n-x)
        if x == 0:
            if sol.count("0") < nr_zeros:
                sol[x] = "0"
            if sol.count("0") > nr_zeros:
                sol[x] = "1"
        elif arr[x] == 0:
            sol[x] ="0"
        else:
            assert arr[x] == x
            sol[x] = "1"
    x = nr_zeros-1
    last_zero = n
    if nr_zeros > 0:
        while x >= 0:
            last_zero-=1
            while sol[last_zero] != "0":
                last_zero-=1
                if last_zero <= 0:
                    break
            arr[x] -= (last_zero - x)
            if x == 0:
                if sol.count("0") < nr_zeros:
                    sol[x] = "0"
                if sol.count("0") > nr_zeros:
                    sol[x] = "1"
            elif arr[x] == 0:
                sol[x] = "0"
            else:
                assert arr[x] == x
                sol[x] = "1"
            x-=1
    assert sol.count("0") == nr_zeros
    return " ".join(sol)

def check(sol):
    return True

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,arr)
        print(res)
