def solve(S, RA, PA, RB, PB, C, cons):
    if S==2:
        return solve_S2(S, RA, PA, RB, PB, C, cons)
    else:
        return solve_S6(S, RA, PA, RB, PB, C, cons)

def solve_S2(S, RA, PA, RB, PB, C, cons):
    # print(cons)
    if (2,2) in cons:
        return 0

    if RA == 2 and PA == 2:
        if len(cons) == 2:
            return 0
        else:
            return 1

    if RB == 2 and PB == 2:
        if len(cons) == 2:
            return 0
        else:
            return -1

    return 2 - len(cons)

def solve_S6(S, RA, PA, RB, PB, C, cons):
    graph = build_graph(S, cons)
    A = (RA, PA)
    B = (RB, PB)

    return  move(graph, A, B, True, 0)

def move(graph, A, B, a_move, score):
    all_moves_a = find_all_moves(graph, A, B)
    all_moves_b = find_all_moves(graph, B, A)
    if len(all_moves_a + all_moves_b) == 0:
        return score
    if a_move:
        all_moves = all_moves_a
        score_list = []
        for m in all_moves:
            new_graph = remove_node(graph, A)
            score_list.append(move(new_graph, m, B, False, score+1))

        if len(all_moves) == 0:
            return move(graph, A, B, False, score)
        return max(score_list)
    else:
        all_moves = all_moves_b
        score_list = []
        for m in all_moves:
            new_graph = remove_node(graph, B)
            score_list.append(move(new_graph, A, m, True, score-1))
        if len(all_moves) == 0:
            return move(graph, A, B, True, score)
        return min(score_list)

def remove_node(graph, A):
    new_graph = graph[:]
    new_graph.remove(A)
    return new_graph

def find_all_moves(graph, P, P2):
    moves = []
    for left in [1,-1]:
        left_node = (P[0], P[1]+left)
        if left_node in graph:
            if left_node != P2:
                moves.append(left_node)
    if P[1] % 2 == 0:
        bot = (P[0]-1, P[1]-1)
        if bot in graph:
            if bot != P2:
                moves.append(bot)
    else:
        top = (P[0]+1, P[1]+1)
        if top in graph:
            if top != P2:
                moves.append(top)
    return moves

def build_graph(S, cons):
    graph = []
    for i in range(1, S+1):
        for j in range(1, 2*i):
            if (i, j) not in cons:
                graph.append((i,j))
    return graph

def main():
    T = int(input())
    for t in range(1, T+1):
        S, RA, PA, RB, PB, C = [int(x) for x in input().split(" ")]
        cons = []
        for i in range(C):
            cons.append(tuple([int(x) for x in input().split(" ")]))
        res = solve(S, RA, PA, RB, PB, C, cons)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()