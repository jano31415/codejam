
def solve(n):
    res=[]
    # if n%2 == 1:
    #     res.append(f"{3*n-1} {3*n}")
        # res.append(f"{n-1} {n}")

        # n-=1
    for i in range(n//2):
        res.append(f"{3*i+1} {3*n-3*i}")
    if n%2 ==1:
        res.append(f"{3*(n//2)+1} {3*(n//2)+3}")

    return res

# subsequence not consecutive part of string
def test_res(res,n):
    s="BAN"*n
    s=list(s)
    for r in res:
        r1,r2 = [int(x)-1 for x in r.split(" ")]
        s[r2],s[r1]= s[r1],s[r2]

    for i in range(3*n):
        if s[i] == "B":
            firstb = i
    for i in reversed(range(3*n)):
        if s[i] == "N":
            firstn = i
    print(s)
    assert firstb > firstn


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        res=solve(n)
        print(len(res))
        # test_res(res,n)
        for r in res:
            print(r)


