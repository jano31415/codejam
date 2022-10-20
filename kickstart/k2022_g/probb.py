import math
def solve(Rs, Rh, stones1, stones2):
    dist1 = [math.sqrt(x**2+y**2) for x,y in stones1]
    dist1.sort()
    dist2 = [math.sqrt(x**2+y**2) for x,y in stones2]
    dist2.sort()
    if len(dist2) == 0:
        return len([x for x in dist1 if x <= Rh+Rs]),0
    if len(dist1) == 0:
        return 0, len([x for x in dist2 if x <= Rh+Rs])

    if dist1[0] < dist2[0]:
        return get(dist1, dist2), 0
    else:
        return 0, get(dist2, dist1)


def get(dist1, dist2):
    return len([x for x in dist1 if x < dist2[0] and x <= Rh+Rs])

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        Rs, Rh = [int(x) for x in input().split()]
        n = int(input())

        stones1=[]
        for i in range(n):
            x,y = [int(x) for x in input().split()]
            stones1.append((x,y))
        stones2=[]
        m = int(input())

        for i in range(m):
            x, y = [int(x) for x in input().split()]
            stones2.append((x, y))

        res = solve(Rs, Rh, stones1, stones2)
        print("Case #{t}: {res}".format(t=t,
            res=f"{res[0]} {res[1]}"), flush=True)
