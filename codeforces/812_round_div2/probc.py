import math
def solve(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [1, 0]
    next_sq = 0
    for i in range(n):
        if i**2 >= n-1:
            next_sq =i**2
            break
    left = []
    for i in range(n):
        if next_sq - (n-1-i) < n:
            left.append(n-1-i)
        else:
            break
    # left = [n-1-i for i in range(0, n - (next_sq- (n-1))+1)]
    # next_sq - (n-1)
    if len(left) == 0:
        return -1
    right = solve(n - len(left))
    if right == -1:
        return -1
    return right + left

import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res=solve(n)
        if res == -1:
            print(res)
            continue
        print(" ".join([str(i) for i in res]))

# def is_square(n):
#     for i in range(n):
#         if i**2 == n:
#             return True
#     return False
# solve(12)
# for i in range(1,100):
#     print(i)
#     res = solve(i)
#     print(res)
#
#     if res == -1:
#         print(f"{i} impossible")
#         continue
#     assert len(res) == i
#     assert all([j in res for j in range(i)])
#     assert ([is_square(j + res[j]) for j in range(i)])

