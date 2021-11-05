def solve(arr, queries):
    l=[arr]
    last = arr[:]
    while True:
        first = {}
        for a in last:
            if a not in first:
                first[a] = 1
            else:
                first[a] += 1
        second = last[:]
        for i,a in enumerate(last):
            second[i] = first[a]
        if second == last:
            break
        last = second[:]
        l.append(last)
    for xi,k in queries:
        if k< len(l):
            print(l[k][xi-1])
        else:
            print(l[-1][xi-1])




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
        q = int(input().decode().strip())
        queries = []
        for i in range(q):
            xi, k = [int(x) for x in input().decode().strip().split(" ")]
            queries.append((xi,k))
        solve(arr, queries)
