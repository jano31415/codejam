def solve(s1, s2):
    tot = 0
    last0=False

    last1= False
    for i in range(len(s1)):
        pair= [s1[i],s2[i]]
        if "1" in pair and "0" in pair:
            tot+=2
            last0 = False
            last1 = False
        else:
            if s1[i] == "1": #both 1
                if last0:
                    tot+= 1
                    last0 = False
                    last1 = False
                else:
                    last1=True

            if s1[i] == "0":
                tot+= 1
                if last1:
                    tot+=1
                    last0 = False
                    last1 = False
                else:
                    last1 = False
                    last0 = True
    return tot
import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s1=input().decode().strip()
        s2=input().decode().strip()

        res = solve(s1,s2)
        print(res)

