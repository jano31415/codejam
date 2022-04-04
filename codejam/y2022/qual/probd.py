from collections import defaultdict


def solve(N, funs, graph):
    res = 0
    rev_graph = defaultdict(list)
    for i in range(1, N+1):
        rev_graph[graph[i-1]].append(i)
    leaves = []
    active = set(range(1, N+1))
    values = [0] * (N + 1)

    for k in range(1, N+1):
        if len(rev_graph[k]) == 0:
            leaves.append(k)
            active.remove(k)
            values[k] = funs[k-1]
    cur_possible = active.copy()
    while len(active) > 0:
        new_possible = set()
        while len(cur_possible):
            node = cur_possible.pop()
            # speedup this
            if all([x not in active for x in rev_graph[node]]):
                min_val = 10**10
                min_node = None
                for x in rev_graph[node]:
                    if values[x] < min_val:
                        
                        min_val = values[x]
                        min_node = x

                values[node] = max(funs[node-1], min_val)
                values[min_node] = 0
                active.remove(node)
                new_possible.add(graph[node-1])
        cur_possible = new_possible
    return sum(values)

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        funs = [int(x) for x in input().split(" ")]
        graph = [int(x) for x in input().split(" ")]
        res = solve(N, funs, graph)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)
