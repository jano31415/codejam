def solve(n,health, spell):
    tot = sum(health)
    tot += sum(spell)
    return tot - max(spell)


import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        health = [int(x) for x in input().decode().strip().split()]
        spell = [int(x) for x in input().decode().strip().split()]

        res=solve(n,health,spell)
        print(res)

