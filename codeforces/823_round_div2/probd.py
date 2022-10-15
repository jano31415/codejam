def solve(n,s1,s2):
    abadaa|adaaba
    5
    daabaa|aabada
    aaba aa
    ad abad
    2
    adbaaa
    adabaa

    abcdef
    123456
    3
    456def
    123abc
    4
    3abcef
    12456d

    abcdef
    123456
    4
    3456ef
    12abcd
    3
    bcd6ef
    12a345


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        s1 = input().decode().strip()
        s2 = input().decode().strip()

        res=solve(n,s1,s2)
        print(res)

