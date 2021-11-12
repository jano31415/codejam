# def solve(n,s):
#     cur_val = {"a":0, "b":0, "c":0}
#     best = n+1
#     for si in s:
#         if (cur_val["a"] == 0) and (si != "a"):
#             continue
#         cur_val[si] += 1
#         length = sum(cur_val.values())
#
#         if length >= 2:
#             if (cur_val["a"] > cur_val["b"]) and (cur_val["a"] > cur_val["c"]):
#                 if length < best:
#                     best =length
#
#         if cur_val["b"] + cur_val["c"] > 2:
#
#         if si == "a":
#             if (cur_val["a"] < cur_val["b"]) or (cur_val["a"] < cur_val["c"]):
#                 cur_val = {"a": 1, "b": 0, "c": 0}
#
#     if best == n+1:
#         return -1
#     return best

def solve(n,s):
    stmp=""
    best = n+1
    canbe = set(["acca", "abba"])
    accepted = set(["aa", "aca", "aba", "abca", "acba", "abbacca", "accabba"])
    lastcanbe = -1
    i = 0
    while i < n:
        si = s[i]
        i+=1
        if (len(stmp) == 0) and (si != "a"):
            continue
        stmp += si
        if (len(stmp) >= 2) and (si == "a"):
            if stmp in accepted:
                if len(stmp) < best:
                    best = len(stmp)
            elif stmp in canbe:
                lastcanbe=i
                continue
            if lastcanbe > 0:
                i = lastcanbe
                lastcanbe = -1
                stmp="a"
            else:
                stmp="a"
    if best == n+1:
        return -1
    return best

import os
import io
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s = input().decode().strip()
        res=solve(n,s)
        print(res)
