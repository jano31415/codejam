import numpy as np

def solve(r,c):
    res = []
    first_row = ".." + "+-"* (c-1) + "+"
    res.append(first_row)
    second_row = ".." + "|." * (c-1) + "|"
    res.append(second_row)
    for ri in range(r-1):
        bot_row = "+-"*c + "+"
        res.append(bot_row)
        mid_row = "|."*c + "|"
        res.append(mid_row)
    bot_row = "+-"*c + "+"
    res.append(bot_row)
    return res


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        r, c = [int(x) for x in input().split(" ")]
        res = solve(r,c)
        print("Case #{i}:".format(i=t, res=res), flush=True)
        for row in res:
            print(row, flush=True)
