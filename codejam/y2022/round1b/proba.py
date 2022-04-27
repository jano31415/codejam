import numpy as np

def solve(n, pancakes):
    left = 0
    right = n-1
    last = 0
    res = 0
    for i in range(n):
        if pancakes[left] < pancakes[right]:
            newp = pancakes[left]
            left += 1
        else:
            newp = pancakes[right]
            right -= 1
        if newp >= last:
            res+=1
            last = newp
    return res







if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        pancakes = [int(x) for x in input().split(" ")]
        res = solve(n, pancakes)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)

