def solve(n):
    if n%2 == 0:
        return [n-i for i in range(2, n-1)] + [1,n-1,n]
    else:
        return [n-1]+[n-i for i in range(3, n-1)] + [1, n-2, n]



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res=solve(n)
        print(" ".join([str(x) for x in res]))

