def solve(n,painting):
    red = [0]*n
    yellow = [0]*n
    blue = [0]*n
    # {U, R, Y, B, O, P, G, A}

    red_col = {"R", "O", "P", "A"}
    blue_col = {"B", "P", "G", "A"}
    yell_col = {"Y", "G", "O", "A"}
    for i, pi in enumerate(painting):
        if pi in red_col:
            red[i]=1
        if pi in blue_col:
            blue[i]=1
        if pi in yell_col:
            yellow[i]=1

    tot = 0
    tot+=get_strokes_color(blue)
    tot+=get_strokes_color(yellow)
    tot+=get_strokes_color(red)
    return tot

def get_strokes_color(arr):
    last = 0
    count = 0
    for ai in arr:
        if (last == 0) and (ai !=0):
            last =1
        elif (last == 1) and (ai == 0):
            last=0
            count+=1
    if last == 1:
        count+=1
    return count


if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        painting = input()

        res = solve(n, painting)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)