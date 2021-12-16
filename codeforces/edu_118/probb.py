def solve(n, arr):
    nr_pairs = n//2
    mina = min(arr)
    count = 0
    # sol = []
    for i in range(n):
        if count == nr_pairs:
            return
        if arr[i] == mina:
            continue
        print(f"{arr[i]} {mina}")
        # assert arr[i] in arr
        # assert mina in arr
        # assert (arr[i] % mina) not in arr
        # sol.append(f"{arr[i]} {mina}")
        count += 1
    # assert len(set(sol)) == nr_pairs






import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr =[int(x) for x in input().decode().strip().split(" ")]
        assert len(arr) == n
        res=solve(n, arr)
        # print(res, flush=True)
