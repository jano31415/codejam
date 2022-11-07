def solve(n,arr):
    # if arr[0] == 1:
    #     return "BOB"
    # if 1 in arr:
    #     return "ALICE"
    if min(arr) == arr[0]:
        return "BOB"
    return "ALICE"

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,arr)
        print(res)

