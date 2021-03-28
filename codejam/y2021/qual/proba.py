import numpy as np

def solve(N, l):
    tot = 0
    for i in range(N-1):
        j = np.argmin(l[i:])
        tot += j+1
        l_tmp = l[i:i+j+1]
        l_tmp.reverse()
        l[i:i+j+1] = l_tmp
    return tot


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        l = [int(x) for x in input().split(" ")]
        assert len(l) == N
        res = solve(N, l)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)
