import math
from itertools import chain, combinations

def solve(n,s):
    subsets = powerset(s)
    res = 0
    mod = 10**9+7
    q = 1
    x = n
    while x >=1:
        q = (q*x) % mod
        x-=1

    for sub in subsets:
        if ispalindrom(sub):
            if len(sub) != len(s):
                # print(sub)
                res = (res + math.factorial(n-len(sub)) * math.factorial(len(sub))) %mod
                # print(res)
    # print(res, q)
    return (res * modinv(q, mod)) % mod


def ispalindrom(st):
    return st[:len(st)//2] == st[len(st)//2 + len(st)%2:][::-1]

def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    if g != 1:
        raise Exception('modular inverse does not exist')
    else:
        return x % m

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n= int(input())
        s = input()
        res = solve(n,s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
