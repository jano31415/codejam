def solve(n, grid):
    countred = 0
    countblue = 0
    for row in grid:
        for x in row:
            if x =="B":
                countblue += 1
            elif x == "R":
                countred += 1
    if abs(countred-countblue) > 1:
        return "Impossible"
    if max(countred, countblue) < n:
        return "Nobody wins"
    has_won(grid)

def has_won(grid):
    neighbourhood = {}
    node_alph = "B"
    start_node = "s"
    end_node = "t"
    for row_nr,row in enumerate(grid):
        for col_nr, node in enumerate(row):
            if node == node_alph:
                nodes = []
                for ydir,xdir in [(0,-1), (0,1), (-1,0), (-1,1), (1,0), (1,1)]:
                    row_cor = row_nr + ydir
                    col_cor = col_nr + xdir
                    if row_cor == 0:
                        nodes.append(start_node)
                    elif row_cor == n:
                        nodes.append(end_node)
                    elif col_cor == 0 or col_cor == n:
                        continue
                    elif grid[row_cor][col_cor] == node_alph:
                        nodes.append(f"{row_cor}_{col_cor}")
                if len(nodes) > 0:
                    neighbourhood[node] = nodes
                for n in nodes:
                    if n not in neighbourhood:
                        neighbourhood[n] = []
                    neighbourhood[n].append(node)
    active_nodes = [start_node]
    while len(active_nodes) > 0:
        cur_node = active_nodes.pop()



if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        grid = [0]*n
        for i in range(n):
            row = [x for x in input().split()]
            grid[i] = row
        res = solve(n, grid)
        print(f"Case #{t}: {res}")