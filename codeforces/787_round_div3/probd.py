import math
def solve(n, neigh, root):
    # dfs
    stack = [root]
    res=[]
    q=[]
    while len(stack) >0:
        curr = stack.pop()
        q.append(curr)
        children = neigh.get(curr, [])
        if len(children) == 0:
            res.append(q)
            q=[]
        for c in children:
            stack.append(c)
    return res



import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n=input().decode().strip()
        arr = [int(x) for x in input().decode().strip().split()]
        neigh = {}
        for i,x in enumerate(arr,1):
            if i == x:
                root =i
                continue
            tmp = neigh.get(x, [])
            tmp.append(i)
            neigh[x] = tmp
        res=solve(n, neigh, root)
        print(len(res))
        for line in res:
            print(len(line))
            print(" ".join([str(x) for x in line]))

