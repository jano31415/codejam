
def solve(m,n,p, all_scores, john):
    max_score=[max([scores[i] for scores in all_scores]) for i in range(n)]
    tot=0
    for m,j in zip(max_score, john):
        if m > j:
            tot+=m-j
    return tot


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        m,n,p = [int(x) for x in input().split()]
        all_scores=[]
        for mi in range(1,m+1):
            scores = [int(x) for x in input().split()]
            if mi == p:
                john = scores
            else:
                all_scores.append(scores)
        res = solve(m,n,p,all_scores, john)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
