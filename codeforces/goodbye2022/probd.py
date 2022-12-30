
import math
def solve(n,arr, brr):
    mod=998244353
    if len(set(arr+brr)) != n:
        return 0
    digits =set(list(range(1,n+1)))
    # remove already doubled
    # 2,4
    for i in range(n):
        if arr[i] == brr[i]:
            if arr[i] in digits:
                digits.remove((arr[i]))
    multiplier = pow(n, n-len(digits), mod)

    dig_to_index = {d:[] for d in digits}
    for i,ai in enumerate(arr):
        if ai in digits:
            dig_to_index[ai].append(i)
    for i,bi in enumerate(brr):
        if bi in digits:
            dig_to_index[bi].append(i)
    single_occ=[]
    for d in dig_to_index:
        if len(dig_to_index[d]) == 1:
            single_occ.append(d)
    # remove 1
    while len(single_occ) > 0:
        d = single_occ.pop()

        if d in digits:
            digits.remove(d)
        if len(dig_to_index[d])==0:
            return 0
        index = dig_to_index[d][0] #one element

        for x in [arr[index], brr[index]]:
            if x == d or x not in dig_to_index:
                continue
            if index in dig_to_index[x]:
                dig_to_index[x].remove(index)
                if len(dig_to_index[x]) ==1:
                    # restart
                    single_occ.append(x)
        del dig_to_index[d]

    # i think this should now be several cycles.
    # we need to count number of cycles and then solution should
    # be. 2**number_cycles * multipier
    nr_cycles=0
    while len(digits) != 0:
        d = digits.pop()
        nr_cycles +=1
        index = dig_to_index[d][0]
        dig_to_index[d].remove(index)
        other = [x for x in [arr[index], brr[index]] if x != d][0]
        while other in digits:
            other_index = dig_to_index[other]
            other_index = other_index[0] if index == other_index[1] else other_index[1]
            d = other
            index = other_index
            digits.remove(d)
            other = [x for x in [arr[index], brr[index]] if x != d][0]
    return (multiplier * pow(2,nr_cycles,mod))%mod


import os
import io
import time
a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())

        arr = [int(x) for x in input().decode().strip().split()]
        brr = [int(x) for x in input().decode().strip().split()]

        res=solve(n,arr,brr)
        print(res)
