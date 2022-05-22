import math
def solve(n,s):
    imp = "NO"
    pos = "YES"
    ls = [int(x) for x in s]
    if sum(ls) < 2:
        return imp, None
    if sum(ls) %2 == 1:
        return imp, None
    if "0" not in s:
        return pos, [(0,i) for i in range(1,n)]
    base = s.rfind("0")
    onezero = False
    zeroone = False
    end = None
    edges =[]
    for i, si in enumerate(s):
        if onezero:
            if i == base:
                if onezero:
                    edges.append((i-1,base))
                    onezero=False
                else:
                    assert False
            elif si == "0":
                edges.append((i-1, i))
            elif si == "1":
                edges.append((i-1,base))
                onezero = True
        elif zeroone:
            if si=="0":
                edges.append((i-1, i))
            elif si == "1":
                edges.append((i-1, i))
                zeroone=False
        else:
            if i == base:
                continue
            elif si == "1":
                onezero = True
            else:
                zeroone = True
                edges.append((i,base))
    if onezero:
        edges.append((i,base))
    assert len(edges) == n-1
    degree=[0]*n
    for u,v in edges:
        degree[u]+=1
        degree[v]+=1
        if u != base and v != base:
            assert abs(u-v)==1
    for i,deg in enumerate(degree):
        assert deg%2 == ls[i]
    return pos,edges
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()

        res,edges=solve(n,s)
        print(res,flush=True)
        if res == "YES":
            for e in edges:
                print(f"{e[0]+1} {e[1]+1}")


def generate_binary_strings(bit_count):
    binary_strings = []
    def genbin(n, bs=''):
        if len(bs) == n:
            binary_strings.append(bs)
        else:
            genbin(n, bs + '0')
            genbin(n, bs + '1')


    genbin(bit_count)
    return binary_strings

binary_strings = generate_binary_strings(6)
for b in binary_strings:
    print(f"input{b}")
    solve(len(b),b)