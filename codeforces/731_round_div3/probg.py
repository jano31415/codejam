def solve(n,m,edges):
    nodes = edges.get(1,[])
    counter = [0]*(n+1)
    counter[1]=1
    path = [1]
    seen = set([1])
    stack = [[1]]
    while len(stack) > 0:
        path = stack.pop()
        last_node = path[-1]
        if (counter[last_node] == -1) or (counter[last_node]>=2):
            seen.add(last_node)
        new_edges = edges.get(last_node,[])
        for new_node in new_edges:
            new_path = path[:]
            if new_node in new_path:
                # cycle
                j = new_path.index(new_node)
                for j in range(j,len(new_path)):
                    if counter[new_path[j]] != -1:
                        counter[new_path[j]] = -1
                        if new_path[j] in seen:
                            seen.remove(new_path[j])
                        stack.append(new_path[:j+1])
            else:
                if (counter[last_node] == -1) and (counter[new_node] != -1):
                    if new_node in seen:
                        seen.remove(new_node)
                    counter[new_node] = -1
                elif counter[new_node] != -1:
                    counter[new_node] = counter[new_node] + counter[last_node]
            if new_node not in seen:
                new_path.append(new_node)
                stack.append(new_path)

    return " ".join([str(x) if x <=2 else "2" for x in counter[1:]])




import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input()
        n,m=[int(x) for x in input().decode().strip().split(" ")]
        edges = {}
        # for u in range(1, n+1):
        #     edges[u] = []
        for i in range(m):
            u, v = [int(x) for x in input().decode().strip().split(" ")]
            if u not in edges:
                edges[u] = []
            edges[u].append(v)

        res = solve(n,m, edges)
        print(res)