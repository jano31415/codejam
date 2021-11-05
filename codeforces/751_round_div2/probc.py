import math
def solve(n, arr):
    if arr[0] == 0 and len(set(arr)) == 1:
        return [str(i+1) for i in range(n)]
    barr = ["{0:b}".format(x) for x in arr]
    max_len = max([len(x) for x in barr])
    barr = [x.rjust(max_len, "0") for x in barr]
    counts =[0]*max_len
    # print(barr)
    for i in range(max_len):
        count = 0
        for b in barr:
            if b[i] == "1":
                count+=1
        counts[i] = count
    a = counts[0]
    for x in counts:
        a = math.gcd(a,x)
    sol=[]
    for i in range(1,a+1):
        if a%i == 0:
          sol.append(str(i))
    return sol



import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        arr =[int(x) for x in input().decode().strip().split(" ")]
        res=solve(n, arr)
        print(" ".join(res))
