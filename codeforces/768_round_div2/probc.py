import math
def solve(n,k):
    if (n-1) == k:
        if n == 4:
            print(-1)
            return
        else:
            print(f"{n - 1} {n-2}")
            print(f"{1} {n//2-1}")
            for i in range(2, n//2-1):
                print(f"{i} {n-1-i}")
            print(f"{0} {n//2}")
            # pairs = [(i, n-1-i)] + [(n-1,n-2),(1,n-3), (0,n-4)]
            # assert sum([a & b for a, b in pairs]) == k
            return
        return
    pairs=[]
    numbers= set(range(n))

    # pairs.append((n - 1, k))
    print(f"{n - 1} {k}")
    numbers.remove(n-1)
    numbers.remove(k)
    # pairs.append((0, n - 1 - k))
    if k != 0:
        print(f"0 {n - 1 - k}")
        numbers.remove(0)
        numbers.remove(n-1-k)

    while len(numbers) > 0:
        x = numbers.pop()
        # pairs.append((x, n-1-x))
        print(f"{x} {n-1-x}")
        numbers.remove(n-1-x)
    # assert sum([a&b for a,b in pairs]) == k



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,k = [int(x) for x in input().decode().strip().split()]
        res1 = solve(n, k)
        # print(res1, flush=True)

# for p in range(2,5):
#     n = 2**p
#     for k in range(n):
#         print(f"run{n} {k}")
#         print("\n")
#         solve(n,k)
#     print("new n")