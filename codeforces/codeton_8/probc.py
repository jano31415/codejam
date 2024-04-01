def solve0(n,x,y,chosen):
    # y=0, how many triangles do we have?
    chosen.sort()
    res = x-2
    for i in range(x-1):
        if chosen[i+1] == chosen[i] + 2:
            res+=1
    # account above equation for the cycle as well
    if chosen[0] == (chosen[-1]+2)%n:
        res+=1

    return res

def solve(n,x,y,chosen):
    # increase the condition as much as possible.
    res = x-2
    chosen.sort()
    diff_array = []
    for i in range(x-1):
        diff = chosen[i+1] - chosen[i]
        if diff == 1:
            continue
        elif diff == 2:
            res+=1
        else:
            diff_array.append(diff)
    # cycle
    diff =(n+chosen[0]) - chosen[-1] # n= 7, -1 is 7, 0 is 1
    if diff == 1:
        pass
    elif diff == 2:
        res += 1
    else:
        diff_array.append(diff)
    evens = [d for d in diff_array if d%2 == 0]
    evens.sort()
    odds = [d for d in diff_array if d%2 == 1]
    odds.sort()
    yused = 0
    for even in evens:
        if y > yused:
            use = (even-1) // 2
            if y-yused >= use:
                yused +=use
                res+= 2*use+1
            else:
                use = y-yused
                yused += use
                res+= 2*use # if not full then no plus 1
                break
        else:
            break
    for odd in odds:
        if y > yused:
            use = min(y-yused, (odd-1)//2)
            yused+=use
            res+=2*use
        else:
            break
    return res




import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        n,x,y = [int(x) for x in input().decode().strip().split()]
        chosen = [int(x) for x in input().decode().strip().split()]

        res = solve(n,x,y,chosen)
        print(res)