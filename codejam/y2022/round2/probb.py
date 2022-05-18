import math
def draw_circle_perimeter(R,grid):
    N = len(grid)//2
    for x in range(-R, R+1):
        y = round(math.sqrt(R * R - x * x))   # round to nearest integer, breaking ties towards zero
        grid[N+x][N+y] = 1
        grid[N+x][N-y] = 1
        grid[N+y][N+x] = 1
        grid[N-y][N+x] = 1

def draw_circle_filled(R,grid):
    for x in range(-R,R+1):
        for y in range(-R, R+1):
            if round(math.sqrt(x * x + y * y)) <= R:
                grid[R+x][R+y]=1

def draw_circle_filled_wrong(R, grid):
    for r in range(0, R+1):
        draw_circle_perimeter(r, grid)

def solve(n):
    grid1 = [[0]*(2*n+1) for _ in range(2*n+1)]
    grid2 = [[0]*(2*n+1) for _ in range(2*n+1)]
    draw_circle_filled(n, grid1)
    draw_circle_filled_wrong(n, grid2)
    res = 0
    for i in range(2*n+1):
        for j in range(2*n+1):
            if grid1[i][j] != grid2[i][j]:
                res += 1
    if len(grid1) > 20:
        import seaborn as sns
        sns.heatmap(grid2)
        from matplotlib import pyplot as plt
        plt.show()
    return res


def solve2(n):
    tot=0
    faulty = set()
    not_faulty = set()
    for R in range(1, n+1):
        for x in range(n+1):
            for y in range(n+1):
            # first = round(math.sqrt(R**2 - x**2))
            # second = round(math.sqrt((R+1)**2 - x**2))
            # a,b=(min(x,first), max(x, first))
            # # if (a,b) in faulty:
            # not_faulty.add((a, b))
            # if second != first+1:
            #     for i in range(first+1, second):
            #         a = min(x, i)
            #         b = max(x, i)
            #         if a**2 + b**2 <= n**2:
            #             faulty.add((a, b))
                t1=R**2 - y**2 < (x-0.5)**2
                t2= (R+1)**2 -y**2 > (x+0.5)**2
                t3 = R**2 - x**2 < (y-0.5)**2
                t4 = (R+1)**2 - x**2 > (y+0.5)**2
                if all([t1,t2,t3,t4]):
                    if x**2 + y**2 <= (n+1)**2:
                        faulty.add((R,x,y))
                # tot += 4
    # res=[x for x in faulty if x not in not_faulty]
    return 4*(len(faulty))


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        res = solve2(n)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)

