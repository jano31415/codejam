import math
def solve(n,m, joy_mat):
    l=[]
    for i in range(n):
        friend_joy = [joy[i] for joy in joy_mat]
        l.append(max(friend_joy))
    best = min(l)
    for store in range(m):
        if len([x for x in joy_mat[store] if x >=best]) >= 2:
            return best
    l=[]
    for store in range(m):
        store_joy = joy_mat[store]
        max_val=0
        max_val2=0
        for j in store_joy:
            if j >= max_val:
                max_val2= max_val
                max_val = j
            elif j >=max_val2:
                max_val2 = j
        l.append(max_val2)
    return max(l)



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        input().decode().strip()
        m,n = [int(x) for x in input().decode().strip().split(" ")]
        joy_mat = []
        for i in range(m):
            joy = [int(x) for x in input().decode().strip().split(" ")]
            assert len(joy) == n
            joy_mat.append(joy)
        res=solve(n,m, joy_mat)
        print(res, flush=True)
