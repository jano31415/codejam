def solve(n, arr):
    arr_sorted = sorted([(arr[i],i) for i in range(n)])
    min1, min2 = arr_sorted[0], arr_sorted[1]
    max1, max2 = arr_sorted[-1], arr_sorted[-2]
    return max1[0]+max2[0] - min1[0] - min2[0]
    if max1[1] > max2[1] :
        max1, max2 = max2, max1
    if min1[1] > min2[1]:
        min1,min2 = min2,min1
    if max1[1] > min1[1]:
        max1,max2,min1,min2 = min1,min2,max1,max2

    if max2[1] > min1[1]:
        return min1[1], max2[1]
    else:
        return max2[1], min1[1]



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n, arr)
        print(res)

