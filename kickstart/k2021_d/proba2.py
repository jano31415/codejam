def solve(grid):
    poss_sol = []
    indices = [((2,2), (0,0)), ((0,2),(2,0)), ((0,1), (2,1)), ((1,0),(1,1))]
    for p1,p2 in indices:
        a = grid[p1[0]][p1[1]]
        b = grid[p2[0]][p2[1]]
        diff = a-b
        if diff%2 == 0:
            poss_sol.append((a+b)//2)
    count_max = 0
    max_sol = -1
    for p in set(poss_sol):
        res = poss_sol.count(p)
        if res > count_max:
            count_max = res
            max_sol = p
    # print(poss_sol)
    # print(count_max)
    arith = 0
    #left column
    if 2*grid[1][0] == ((grid[0][0] + grid[2][0])):
        arith += 1
    # right col
    if 2*grid[1][1] == ((grid[0][2] + grid[2][2])):
        arith += 1
    # top row
    if 2*grid[0][1] == ((grid[0][0] + grid[0][2])):
        arith += 1
    #bot row
    if 2*grid[2][1] == ((grid[2][0] + grid[2][2])):
        arith += 1
    # print(arith)
    return count_max + arith

    # a=time.time()
if __name__ == "__main__":
    # input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input())
    for t in range(1,T+1):
        grid = []
        for _ in range(3):
            row = [int(x) for x in input().split(" ")]
            grid.append(row)
        res = solve(grid)
        print(f"Case #{t}: {res}", flush=True)