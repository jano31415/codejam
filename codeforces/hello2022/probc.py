# interactive, dont use decode strip ... doesnt work for some reason

def get_input(last,perm):
    print(f"? {last}", flush=True)
    return perm,int(input())

# perm_sol = [1,3,4,2]
# perm_sol = [4,2,1,3]
# perm_sol = [4, 3, 1, 2]
# perm_sol=[1,3,4,2]
# def get_input(last, perm):
#     print(f"? {last}")
#     res = perm[last-1]
#     new_perm = perm[:]
#     for i in range(len(perm)):
#         new_perm[i] = perm[perm_sol[i]-1]
#     print(res)
#     return new_perm, res


def solve(n):
    if n == 1:
        print("! 1")
        return
    missing = set(range(1,n+1))
    sol = [0]*(n+1)
    perm = list(range(1,n+1))
    while len(missing) > 0:
        first = missing.pop()
        circle = set([])
        circle_l = []
        while True:
            perm, res = get_input(first, perm)
            last = res
            if res in circle:
                break
            circle.add(res)
            circle_l.append(res)
            try:
                missing.remove(last)
            except Exception as e:
                pass
        for i in range(len(circle_l)-1):
            sol[circle_l[i]]=circle_l[i+1]
        sol[circle_l[-1]] = circle_l[0]
    print(" ".join([str(sol[i]) if i!=0 else "!" for i in range(0,n+1)]), flush=True)


import os
import io
if __name__ == "__main__":

    T = int(input())
    for t in range(T):
        n = int(input())
        solve(n)
