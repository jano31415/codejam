def solve(N):
    # print(solve_slow(N))
    if N == 1:
        return 1
    res=0
    for div in range(1,N):
        if N//div - (div-1)//2 <= 0:
            break
        if div%2 == 0:
            if N % div == div//2:
                res+=1
        else:
            if N % div == 0:
                res+=1
    return res

def solve_slow(N):
    res=0
    for i in range(1,N+1):
        tot=0
        for j in range(i,N+1):
            tot += j
            if tot == N:
                res+=1
            if tot >= N:
                break
    return res

# for i in range(1,1000):
#     if solve(i) != solve_slow(i):
#         print(i)
# import time
# a = time.time()
# solve(10**12)
# b=time.time()
# print(b-a)
# 1 mod 2
# 0 mod 3
# 2 mod 4 -1 0 1 2
# 2 mod 4  0 1 2 3
# 0 mod 5 -2 -1 0 1 2
# 3 mod 6  -2 -1 0 1 2 3

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())

        res = solve(N)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
