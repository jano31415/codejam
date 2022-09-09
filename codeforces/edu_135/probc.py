def solve(n,a,b):
    a.sort(reverse=True)
    b.sort(reverse=True)
    if a == b:
        return 0
    a_index=0
    b_index=0
    tot=0
    asmall=[]
    bsmall=[]
    while a_index < n or b_index < n:
        if a_index >= n:
            if b[b_index] >= 10:
                bsmall.append(dig_log(b[b_index]))
                tot+=1
            else:
                bsmall.append(b[b_index])
            b_index+=1
        elif b_index >= n:
            # do dig log on a
            if a[a_index] >= 10:
                asmall.append(dig_log(a[a_index]))
                tot+=1
            else:
                asmall.append(a[a_index])
            a_index+=1
        elif a[a_index] == b[b_index]:
            a_index += 1
            b_index += 1
        elif a[a_index] > b[b_index]:
            # do dig log on a
            if a[a_index] >= 10:
                asmall.append(dig_log(a[a_index]))
                tot+=1
            else:
                asmall.append(a[a_index])
            a_index+=1
        else:
            if b[b_index] >= 10:
                bsmall.append(dig_log(b[b_index]))
                tot+=1
            else:
                bsmall.append(b[b_index])
            b_index+=1

    asmall.sort()
    bsmall.sort()
    if asmall==bsmall:
        return tot
    assert len(asmall) == len(bsmall)
    acount =[0]*10
    bcount = [0]*10
    for ai in asmall:
        acount[ai] += 1
    for bi in bsmall:
        bcount[bi]+=1
    left = 2*len(asmall)
    left -= acount[1] + bcount[1]
    for i in range(2,len(acount)):
        left -= 2*min(acount[i], bcount[i])
    assert left >= 0
    return tot + left

def dig_log(x):
    return len(str(x))


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        a = [int(x) for x in input().decode().strip().split()]
        b = [int(x) for x in input().decode().strip().split()]

        res=solve(n,a,b)
        print(res)

