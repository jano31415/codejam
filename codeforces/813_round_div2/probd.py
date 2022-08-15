
def solve(n,k,arr):
    if k == n:
        return 10**9
    arr_index = [(arr[i], i) for i in range(n)]
    arr_index.sort()
    #copy arr?
    arrc = arr[:]
    for i in range(k):
        aj,j = arr_index[i]
        arrc[j] = 10**9
    diam = 0
    for i in range(n-1):
        diam = max(diam, min(arrc[i], arrc[i+1]))
    diam = min(diam, 2*min(arrc))

    arrc = arr[:]
    for i in range(k-1):
        aj,j = arr_index[i]
        arrc[j] = 10**9
    min_index = 0
    min_val = 10**9
    max_val = max(arrc)
    for i in range(1, n - 1):
        if (arrc[i-1] == max_val) or (arrc[i+1] == max_val):
            if arrc[i] <= min_val:
                min_index =i
                min_val = arrc[i]
    arrc[min_index] = 10**9
    diam2 = 0
    for i in range(n-1):
        diam2 = max(diam2, min(arrc[i], arrc[i+1]))
    diam2 = min(diam2, 2*min(arrc))

    return max(diam, diam2)




import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n,k,arr)
        print(res)

