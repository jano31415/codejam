def solve(n,edges):
    neighbourhood = {}
    for x,y in edges:
        if x not in neighbourhood:
            neighbourhood[x] = []
        neighbourhood[x].append(y)
        if y not in neighbourhood:
            neighbourhood[y] = []
        neighbourhood[y].append(x)
    tot = 0
    for i in range(n):
        root = i+1
        #dfs
        long_path = [root]
        long_path_set = set(long_path)
        goto = neighbourhood[root]
        while len(goto) > 0:
            new_node = goto.pop() #0 ?
            next_nodes = [x for x in neighbourhood[new_node] if x not in long_path_set]
            goto = goto + next_nodes
            for n in long_path:
                if n > new_node:
                    tot += 1
            long_path.append(new_node)
            long_path_set.add(new_node)
            if len(next_nodes) == 0:
                long_path.pop()
                long_path_set.remove(new_node)
    return tot

def solve(n,edges):
    tot = 0
    for i in range(n):
        root = i+1


def inversion(n,rooted_neighborhood):
    if n not in rooted_neighborhood:
        return 1,1
    tmp = 0
    for n in neighbourhood[root]:
        k, inv = inversion(n, rooted_neighborhood)
        tmp+=inv

# n! / k1! ...
import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    n = int(input().decode().strip())
    edges =[]
    for i in range(n-1):
        x,y = [int(x) for x in input().decode().strip().split(" ")]
        edges.append((x,y))
    res = solve(n, edges)
    print(res)