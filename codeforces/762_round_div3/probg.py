import math
from heapq import heapify,heappush,heappop


def solve(n, k, mines):
    if k==0:
        return solve0(n,mines)
    else:
        return solve1(n,mines)

def solve0(n,mines):
    times = [x[2] for x in mines]
    times.sort(reverse=True)
    for i in range(n):
        if times[i] < i:
            return i-1
    return n

def solve1(n, mines):
    pass

# connected component algorithm, maybe reuse some of the spanning tree algorithm

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



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input().decode().strip()
        n,k = [int(x) for x in input().decode().strip().split(" ")]
        mines =[]
        for i in range(n):
            x, y, t = [int(x) for x in input().decode().strip().split(" ")]
            mines.append((x,y,t))
        res=solve(n,k, mines)
        print(res, flush=True)