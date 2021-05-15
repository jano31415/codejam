def solve2(tickets, N, C, M):
    if len(tickets.keys()) == 1:
        for c in tickets:
            return len(tickets[c]),0
    cust = list(tickets.keys())
    max_same = 0
    same_val = 0
    for i in range(1,N+1):
        same = tickets[cust[0]].count(i) + tickets[cust[1]].count(i)
        if same > max_same:
            max_same = same
            same_val = i
    max_ticket_cust = max([len(v) for v in tickets.values()])
    if max_same <= max_ticket_cust:
        return max_ticket_cust, 0
    prom = 0
    if max_same > max_ticket_cust:
        if same_val != 1:
            prom = max_same - max_ticket_cust
        else:
            max_ticket_cust = max_same

        return max_ticket_cust, prom


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N,C, M = [int(x) for x in input().split(" ")]
        tickets= {i:[] for i in range(1,C+1)}
        for m in range(M):
            P,B = [int(x) for x in input().split(" ")]
            tickets[B].append(P)
            assert P <= N
            assert B <= C
        a,b = solve2(tickets, N, C, M)
        res = [str(a), str(b)]
        print("Case #{t}: {res}".format(t=t, res=" ".join(res)), flush=True)