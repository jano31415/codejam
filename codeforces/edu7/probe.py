def solve(k,A,h):
    places =[1]
    current =2
    for i in range(2,k+2):
        places = places + [current]*(2**(i-2))
        current = 2**(i-1)+1
    # print(places)
    import itertools
    perm = list(itertools.permutations(list(range(len(places)))))
    for p in perm:
        # p = [4, 3, 5, 1, 0, 6, 7, 2]
        # print([places[i] for i in p])
        hash = 0
        for j,i in enumerate(p):
            hash = (hash + (j+1) * A ** (places[i])) % 998244353
        print(hash)
        if hash == h:
            return " ".join([str(places[i]) for i in p])
    return -1

# 5 3 5 2 1 5 5 3
import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    k,A,h = [int(x) for x in input().decode().strip().split(" ")]
    res=solve(k,A,h)
    print(res)