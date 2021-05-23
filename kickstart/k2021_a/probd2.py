# i read the solution. Could have thought more about it. But was happy
# to have a first maximum spanning tree implementation.
def solve(grida, gridb, r, c):
    edges, nodes = create_graph(grida, gridb)
    spanning_tree = kruskal(edges, nodes)
    sum_span = sum([e[0] for e in spanning_tree])
    sum_all = sum([e[0] for e in edges])
    return sum_all - sum_span


def create_graph(grida, gridb):
    edges = []
    for i,row in enumerate(grida):
        for j,x in enumerate(row):
            if x == -1:
                a = f"r{i}"
                b = f"c{j}"
                edges.append((gridb[i][j],a,b))
    nodes = [e[1] for e in edges] + [e[2] for e in edges]
    nodes= set(nodes)
    return edges, nodes


def kruskal(edges, nodes):
    edges.sort(key=lambda x:-x[0])
    span_tree = []
    node_to_rank = {}
    rank_to_points = {0:[]}
    max_rank = -1
    for w,a,b in edges:
        max_rank = add_edge(w,a,b,node_to_rank, rank_to_points,max_rank, span_tree)
        if len(span_tree) == len(nodes) -1:
            break
    return span_tree


def add_edge(w,a,b, node_to_rank, rank_to_points, max_rank, span_tree):
    if a in node_to_rank:
        if b not in node_to_rank:
            node_to_rank[b] = node_to_rank[a]
            rank_to_points[node_to_rank[a]].append(b)
            span_tree.append((w, a, b))
        else:
            if node_to_rank[a] != node_to_rank[b]:
                max_rank_ab = max(node_to_rank[a], node_to_rank[b])
                switch_points = rank_to_points[max_rank_ab]
                new_rank = min(node_to_rank[a],node_to_rank[b])
                for x in switch_points:
                    node_to_rank[x] = new_rank
                    rank_to_points[new_rank].append(x)
                del rank_to_points[max_rank_ab]
                span_tree.append((w,a,b))
            else:
                pass  # cycle dont add
        return max_rank
    if b in node_to_rank:
        return add_edge(w,b,a, node_to_rank, rank_to_points,max_rank, span_tree)
    new_max_rank = max_rank + 1
    node_to_rank[a] = new_max_rank
    node_to_rank[b] = new_max_rank
    rank_to_points[new_max_rank] = [a, b]
    span_tree.append((w, a, b))
    return new_max_rank


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        grida = []
        for i in range(N):
            row = [int(x) for x in input().split(" ")]
            grida.append(row)
        gridb = []
        for i in range(N):
            row = [int(x) for x in input().split(" ")]
            gridb.append(row)
        r = [int(x) for x in input().split(" ")]
        c = [int(x) for x in input().split(" ")]
        assert len(grida) == N
        assert len(gridb) == N
        assert len(r) == N
        assert len(c) == N

        res = solve(grida, gridb, r, c)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
