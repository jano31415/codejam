
def solve(n,q, edges):
    level_count = [0]*n
    level = [1]
    level_nr = 0
    seen = set()
    while len(level) != 0:
        level_count[level_nr] = len(level)
        next_level = []
        for node in level:
            seen.add(node)
            for next_node in edges.get(node, []):
                if next_node not in seen:
                    next_level.append(next_node)
        level = next_level[:]
        level_nr+=1
    cumsum=0
    for x in level_count:
        if cumsum + x > q:
            return cumsum
        cumsum+=x
    return cumsum

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n,q = [int(x) for x in input().split()]
        edges = {}
        for i in range(n-1):
            u,v = [int(x) for x in input().split()]
            if u not in edges:
                edges[u]=[]
            edges[u].append(v)
            if v not in edges:
                edges[v] = []
            edges[v].append(u)

        for i in range(q):
            x = input()
        res = solve(n,q, edges)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
