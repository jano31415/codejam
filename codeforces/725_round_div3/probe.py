def solve(N,equ):
    tot = 0
    count_haha = {}
    for eq in equ:
        if ":" in eq:
            new_var, new_val = eq.split(" := ")
            haha_count = 0
            if "haha" in new_val:
                haha_count=1
            end, start = get_start_end(new_val)
            count_haha[new_var] = (start, end, haha_count, new_val)
            last_var=new_var
        else:
            chg_var, assig = eq.split(" = ")
            left_var, right_var = assig.split(" + ")
            new_count = count_haha[left_var][2] + count_haha[right_var][2]
            leftend = count_haha[left_var][1]
            rightstart = count_haha[right_var][0]
            if leftend == "hah" and rightstart == "aha":
                new_count+=2
            if leftend == "hah" and rightstart == "a":
                new_count+=1
            elif leftend == "ha" and rightstart == "ha":
                new_count+=1
            elif leftend == "h" and rightstart == "aha":
                new_count+=1
            new_str = count_haha[left_var][3] + count_haha[right_var][3]
            if len(new_str) <= 8:
                start, end = get_start_end(new_str)
            else:
                start,end=count_haha[left_var][0], count_haha[right_var][1]
                new_str = "a"*10
            count_haha[chg_var] = (start,end, new_count, new_str)
            last_var= chg_var
    return count_haha[last_var][2]


def get_start_end(new_val):
    if len(new_val) >= 3 and "aha" == new_val[:3]:
        start = "aha"
    elif len(new_val) >= 2 and "ha" == new_val[:2]:
        start = "ha"
    elif len(new_val) >= 1 and "a" == new_val[0]:
        start = "a"
    else:
        start = ""
    if len(new_val) >= 3 and "hah" == new_val[-3:]:
        end = "hah"
    elif len(new_val) >= 2 and "ha" == new_val[-2:]:
        end = "ha"
    elif len(new_val) >= 1 and "h" == new_val[-1]:
        end = "h"
    else:
        end = ""
    return end, start


import io
import os
import math
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    T = int(input().decode().strip())
    for t in range(T):
        N = int(input().decode().strip())
        equ = []
        for i in range(N):
            equ.append(input().decode().strip())
        res = solve(N, equ)
        print(res)