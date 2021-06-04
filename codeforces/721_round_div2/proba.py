def solve(N):
    if N == 1:
        return 0
    x=1
    for i in range(N):
        if 2*x > N:
            return x-1
        x = 2*x
        
if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        res = solve(N)
        print(str(res), flush=True)