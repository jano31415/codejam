def solve(n,A):
    if n == 3:
        solve3(A)
    elif n == 4:
        solve4(A)
    elif n == 5:
        solve5(A)
    else:
        raise ValueError("high n not supported.")

def solve3(A):
    res="POSSIBLE"
    print("Case #{t}: {res}".format(t=t, res=res), flush=True)
    print(f"{1} {1}")
    print(f"{1} {2}")
    print(f"{A+1} {1}")

def solve4(A):
    if A == 1:
        res = "IMPOSSIBLE"
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        return
    res="POSSIBLE"
    print("Case #{t}: {res}".format(t=t, res=res), flush=True)
    print(f"{1} {1}")
    print(f"{1} {2}")
    if A %2 == 0:
        print(f"{A//2 + 1} {2}")
        print(f"{A//2 + 1} {1}")
    else:
        print(f"{A//2 + 2} {2}")
        print(f"{A//2 + 1} {1}")

def solve5(A):
    if A <= 2:
        res = "IMPOSSIBLE"
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        return
    if A == 3:
        res = "POSSIBLE"
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        print(f"{1} {1}")
        print(f"{1} {2}")
        print(f"{3} {3}")
        print(f"{2} {2}")
        print(f"{2} {1}")
        return
    if A == 4:
        res = "POSSIBLE"
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
        print(f"{1} {1}")
        print(f"{1} {2}")
        print(f"{3} {4}")
        print(f"{2} {2}")
        print(f"{2} {1}")
        return

    res="POSSIBLE"
    print("Case #{t}: {res}".format(t=t, res=res), flush=True)
    print(f"{1} {3}")
    print(f"{1} {1}")
    end = A//4
    if A%4 == 1:
        print(f"{end + 1} {1}")
        print(f"{end + 1} {2}")
        print(f"{end + 2} {3}")
    elif A %4 == 2:
        print(f"{end + 1} {1}")
        print(f"{end + 2} {2}")
        print(f"{end + 1} {3}")
    elif A%4 == 3:
        print(f"{end + 1} {1}")
        print(f"{end + 2} {2}")
        print(f"{end + 2} {3}")

    else:
        print(f"{end} {1}")
        print(f"{end + 2} {2}")
        print(f"{end} {3}")

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n,A = [int(x) for x in input().split(" ")]
        res = solve(n,A)
import random
import time
# n=1000
# max_n = 10**6
# k = random.randint(6*max_n, 12*max_n)
# ban = [random.randint(0,max_n) for _ in range(n)]
# a = time.time()
# res=solve(n,k,ban)
# b=time.time()
# print(res)
# print(b-a)