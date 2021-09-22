def solve(n,m,k,rooms, edges):
    adj={i:set() for i in range(n)}
    for u,v in edges:
        adj[u].add(v)
        adj[v].add(u)

    import itertools
    perms = list(itertools.permutations(range(n)))
    tot = 0
    tuple_seen = set()
    for perm in perms:
        a,perm_sub=check_lr(perm,rooms,k)
        if not a:
            continue
        if tuple(perm_sub) in tuple_seen:
            continue
        tuple_seen.add(tuple(perm_sub))
        if check_connected(perm_sub,adj):
            tot+=1
    return tot

def check_lr(perm,rooms,k):
    magic = rooms[perm[0]][2]
    perm_sub = [perm[0]]
    for i in perm[1:]:
        if magic == k:
            return True, perm_sub
        perm_sub.append(i)
        l,r,a = rooms[i]
        if (magic < l) or (magic > r):
            return False,[]
        magic+=a
    if magic == k:
        return True, perm_sub
    return False,[]

def check_connected(perm,adj):
    seen = [perm[0]]
    for i in perm[1:]:
        connected=False
        for s in seen:
            if i in adj[s]:
                connected = True
                seen.append(i)
                break
        if not connected:
            return False
    return True

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        n,m,k = [int(x) for x in input().split(" ")]
        rooms = []
        for i in range(n):
            li, ri, ai = [int(x) for x in input().split(" ")]
            rooms.append((li, ri, ai))
        edges=[]
        for i in range(m):
            x,y = [int(x) for x in input().split(" ")]
            edges.append((x,y))

        res = solve(n,m,k,rooms, edges)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)