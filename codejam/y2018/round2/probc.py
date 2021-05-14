from random import randint
# read the analysis without much thinking. Need to learn how to solve such
# matrix problems. Unfortunately my flow implementation is too slow.
# implementing hopcroft karp matching one when i have time.

def solve(grid, N):
    rc_dict = {i: [] for i in range(-N, N+1)}
    for r, row in enumerate(grid):
        for c, x in enumerate(row):
            rc_dict[x].append(("r"+str(r), "c"+str(c)))
    notmatched = 0
    for i in range(-N, N+1):
        rc_tup = rc_dict[i]
        if len(rc_tup) <= 1:
            continue
        matched, sol = max_match(rc_tup)
        notmatched += len(rc_tup) - matched
    return notmatched


def max_match(rc_tup):
    # row column combinations are edges between rows and columns
    A = list(set([x[0] for x in rc_tup]))
    B = list(set([x[1] for x in rc_tup]))
    E = rc_tup
    V, E = bipartite_to_flow(A, B, E)
    cap = {e: 1 for e in E}
    neighbourhood = get_neighbourhood(E, V)
    res = push_relabel(V, E, neighbourhood, cap)
    return res

def push_relabel(V, E, neighbourhood, cap, s="s", t="t"):
    height = init_height(V, s, t)
    flow, excess, overflowing = init_preflow(V, E, neighbourhood, cap, s, t)

    while len(overflowing) > 0:
        u = overflowing.pop()

        new_overflowing = push_from_vertex(u, neighbourhood, cap, height, excess, flow, t)
        overflowing += new_overflowing
        if excess[u] > 0:
            overflowing.append(u)
            relabel(u, height, neighbourhood)
    return -excess[s], flow


def init_height(V, s, t):
    # height function h: V-> |N
    height = {v: 0 for v in V}
    height[s] = len(V)
    height[t] = 0
    return height


def push_from_vertex(u, neighbourhood, cap, height, excess, flow, t):
    u_neighbourhood = neighbourhood[u]
    new_overflowing = []
    for v in u_neighbourhood:
        if height[u] == height[v]+1:
            push(cap, excess, flow, u, v, neighbourhood)
            if excess[v] > 0 and v != t:
                new_overflowing.append(v)
    return new_overflowing


def push(cap, excess, flow, u, v, neighbourhood):
    push_amount = min(excess[u], cap[(u, v)])
    flow[(u, v)] = flow.get((u, v), 0) + push_amount
    flow[(v, u)] = flow.get((v, u), 0) - push_amount

    excess[u] -= push_amount
    excess[v] += push_amount

    cap[(u, v)] = cap[(u, v)] - push_amount
    if cap[(u, v)] == 0:
        neighbourhood[u].remove(v)
    cap[(v, u)] = cap.get((v, u), 0) + push_amount
    if cap[(v, u)] > 0 and (u not in neighbourhood[v]):
        neighbourhood[v].append(u)


def relabel(u, height, neighbourhood):
    u_neighbourhood = [b for b in neighbourhood[u]]
    if len(u_neighbourhood) == 0:
        print("relabel useless node. buggy")
        return
    height[u] = 1 + min([height[v] for v in u_neighbourhood])


def init_preflow(V, E, neighbourhood, cap, s, t):
    excess = {v: 0 for v in V}
    flow = {e: 0 for e in E}

    overflowing = []
    for v in neighbourhood[s]:
        flow[(s, v)] = cap[(s, v)]
        excess[v] = cap[(s, v)]
        if v != t:
            overflowing.append(v)
        excess[s] -= cap[(s, v)]
        cap[(v, s)] = cap[(s, v)]
        if s not in neighbourhood[v]:
            neighbourhood[v].append(s)
        cap[(s, v)] = 0
    neighbourhood[s] = []

    return flow, excess, overflowing


def get_neighbourhood(E, V):
    neighbourhood = {v: [] for v in V}
    for u, v in E:
        neighbourhood[u].append(v)
    return neighbourhood


def bipartite_to_flow(A, B, E):
    V = A + B + ["s", "t"]
    E = E + [("s", a) for a in A] + [(b, "t") for b in B]
    return V, E


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        grid = []
        for _ in range(N):
            row = [int(x) for x in input().split(" ")]
            assert len(row) == N
            grid.append(row)
        assert len(grid) == N
        res = solve(grid, N)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)


import time
# def test():
a = time.time()
N = 100
V = list(range(100))
grid = [[randint(-N, N) for i in range(N)] for _ in range(N)]
solve(grid, N)
b = time.time()
print(b - a)