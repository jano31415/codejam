def solve(n,m,perm):
    cyc_right = [0]*n
    for i,p in enumerate(perm):
        k = (n+i+1-p)%n
        cyc_right[k] += 1
    check_these= []
    for i,right in enumerate(cyc_right):
        if right >= n -2*m:
            check_these.append(i)

    check_these.sort()
    check_copy = check_these[:]
    for k in check_copy:
        swaps = 0
        tmp_perm = perm[:]
        for i,p in enumerate(tmp_perm):
            if k != (n+i+1-p)%n:
                tmp = tmp_perm[i]
                while k != (n+i+1-tmp)%n:
                    swap_index = (k+tmp) % n - 1
                    # assert k == (n + swap_index+1 - tmp)%n
                    tmp_perm[i] = tmp_perm[swap_index]
                    tmp_perm[swap_index] = tmp
                    tmp = tmp_perm[i]
                    swaps+=1
                if swaps > m:
                    check_these.remove(k)
                    break
    return check_these

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n,m=[int(x) for x in input().decode().strip().split(" ")]
        perm=[int(x) for x in input().decode().strip().split(" ")]
        res1 = solve(n,m,perm)
        if len(res1) ==0:
            print("0")
        else:
            res = str(len(res1))+" "+" ".join([str(x) for x in res1])
            print(res)
