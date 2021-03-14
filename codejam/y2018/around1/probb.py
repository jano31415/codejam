def find_robots(T, S, P, R, B,M):
    nr_items = []
    for i in range(len(S)):
        tmp = min((T-P[i])//S[i], M[i])
        tmp = max(tmp, 0)
        nr_items.append(tmp)

    return B <= sum(sorted(nr_items, reverse=True)[:R])


def test_find_robots():
    M = [2, 2, 2, 2, 2]
    P = [3, 5, 2, 4, 1]
    S = [3, 1, 4, 2, 5]
    T = 10
    R = 3
    B = 4
    print(find_robots(T, S, P, R, B,M))

def binaray_time(S, P, R, B,M):

    T = 2**100 # what is max
    step = T//2
    best_T = T
    while True:


        if find_robots(T, S, P, R, B, M):
            best_T = T
            T = T - step
        else:
            T += step

        if step < 1:
            return best_T

        step = step//2

def main():
    T = int(input())
    for i in range(1, T+1):
        R, B,C = [int(x) for x in input().split(" ")]
        M=[]
        S=[]
        P=[]
        for j in range(C):
            m,s,p = [int(x) for x in input().split(" ")]
            M.append(m)
            S.append(s)
            P.append(p)
        res = binaray_time(S, P, R, B, M)
        print("Case #{i}: {res}".format(i=i, res=res), flush=True)


main()
