# we can not check every i,j combination even if the check is O(1)
# this will be O(n**2) which is to slow for 10**5 input.
# using some kind of two pointer method.
# Idea is to look for the shortest solution i,j where the inequality
# does not hold. If an interval has a negative sum but is
# the start of a solution interval then the other part is
# already a smaller solution.
# 5 -4 -2 3 -1 3 -1 3
# after 5-4-2 =-1 we can stop checking intervals starting with
# 5 as the rest needs to have sum 7 to be a solution and
# will thus be a solution already without 5 -4 -2.
# So we go to the next number as a start for the interval.
# kind of confusing implementation but it works on the test set.

def solve(n, arr):
    left=0
    cur=0
    cmax = -10**10
    i=0
    while i < len(arr):
        x=arr[i]
        if cur+x <= 0:
            cur = 0
            cmax=-10**10
            i=left
            left+=1
        else:
            cur +=x
            if x > cmax:
                cmax = x
            if cmax < cur:
                return "NO"
        i+=1

    arr = arr[::-1]
    #max is left
    left=0
    cur=0
    cmax = -10**10
    i=0
    while i < len(arr):
        x=arr[i]
        if cur+x <= 0:
            cur = 0
            cmax=-10**10
            i=left
            left+=1
        else:
            cur +=x
            if x > cmax:
                cmax = x
            if cmax < cur:
                return "NO"
        i+=1
    return "YES"




import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr = [int(x) for x in input().decode().strip().split()]
        res=solve(n, arr)
        print(res)

