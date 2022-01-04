
def solve(n,arr):
    min_sol = n-1
    for i in range(n-1):
        for j in range(i+1,n):
            a = arr[i]
            b = arr[j]
            diff = b-a
            max_count_left = 0
            for x in range(i):
                if (arr[x]-a)*(j-i) == - diff *(i-x):
                    max_count_left += 1

            count_mid=2
            for x in range(i+1,j):
                if (arr[x] - a) * (j - i) == - diff * (i - x):
                    count_mid += 1
            max_count_right = 0
            for x in range(j+1, n):
                if (arr[x] - b) * (j - i) == - diff * (j - x):
                    max_count_right += 1

            # print((max_count_left, count_mid, max_count_right))
            tot = max_count_left + count_mid + max_count_right
            if min_sol > n-tot:
                min_sol = n-tot
    return min_sol
import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr=[int(x) for x in input().decode().strip().split()]

        res=solve(n,arr)
        print(res, flush=True)