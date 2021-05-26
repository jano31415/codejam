import random
# i had the right idea but needed the analysis for the details. time limit
# quite tight for python

def solve(names, connections):
    names = [set(name) for name in names]
    if len(names) == 1:
        return
    # import time
    # a =time.time()
    graph = create_graph(names)
    # b=time.time()
    # print(b-a)
    res=[]
    res_cache = {}
    for a, b in connections:
        if (a, b) in res_cache:
            res.append(res_cache[(a, b)])
        else:
            shortest_res = shortest_path(a, b, graph, names)
            res_cache[(a, b)] = shortest_res
            res.append(shortest_res)
    return " ".join([str(x) for x in res])


def create_graph(names):
    nodes = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    edges = {node: set() for node in nodes}

    for name in names:
        for x in name:
            # for y in name:
            #     edges[x].add(y)
            edges[x] = edges[x].union(name)
            edges[x].remove(x)
    return edges


def shortest_path(a_int,b_int,graph, names):
    # alph = "abcdefghijklmnopqrstuvwxyz"
    a = names[a_int-1]
    b = names[b_int-1]
    res = 1000
    # for start in a:
    res = bfs(a, b, graph, res)
    # if res_start < res:
    #     res = res_start
    if res == 1000:
        return -1
    return res


def bfs(a_list,lb,graph, max_depth):
    level = {a:2 for a in a_list}
    cur = 0
    nodes = list(a_list)
    if a_list.intersection(lb):
        return 2
    while len(nodes) > 0:
        cur_node = nodes.pop(0)
        for e in graph[cur_node]:
            if e not in level:
                level[e] = level[cur_node]+1
                nodes.append(e)
                # if level[e] > max_depth:
                #     return 1000
                if e in lb:
                    return level[e]
    return min([level[b] for b in lb if b in level] + [1000])


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        N, k = [int(x) for x in input().split(" ")]
        names = [x for x in input().split(" ")]
        connections = []
        for i in range(k):
            x, y = [int(x) for x in input().split(" ")]
            connections.append((x, y))
        res = solve(names, connections)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

# def check_slow():
#     for t in range(1,4):
#         a = 0
#         while a != t:

# import time
# a = time.time()
# for i in range(1):
#     alph = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     names = ["".join([random.choice(alph) for _ in range(20)]) for i in range(50000)]
#     connections = [(random.randint(1, 100), random.randint(1, 100)) for _ in range(5*10**4)]
#     a = time.time()
#     # names2 = [name.lower() for name in names]
#     res=solve(names,connections)
# b=time.time()
# print(b-a)