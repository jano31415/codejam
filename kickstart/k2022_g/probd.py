import random


def solve(N, E, flowers):
    dp = {("r", 0):0} # l,x,e

    # flowers.sort(key=lambda x:x[1])

    heights = sorted(list(set([x[1] for x in flowers])), reverse=True)
    flower_h = {h:[] for h in heights}
    for f in flowers:
        flower_h[f[1]].append(f)

    opp = {"r":"l", "l":"r"}
    best=0
    for h in heights:
        dp_new = {}
        flower_h[h].sort(key=lambda a: a[0])
        flower_h_r = flower_h[h][::-1]
        sum_f = sum([c for x,y,c in flower_h[h]])
        for lr,curx in dp:
            assign(dp_new,(lr,curx), dp[(lr,curx)])
            if lr == "r":
                this_flowers = flower_h_r[:]
            else:
                this_flowers = flower_h[h][:]
            if lr == "r":
                leftsum = sum([ci for xi,yi,ci in this_flowers if xi >= curx])
            else:
                leftsum = sum([ci for xi,yi,ci in this_flowers if xi <= curx])
            if leftsum is not None:
                for left in range(len(this_flowers)):
                    if lr =="l" and this_flowers[left][0] > curx:
                        break
                    if lr =="r" and this_flowers[left][0] < curx:
                        break
                    new_v = dp[(lr,curx)] + leftsum
                    if new_v > best - len(heights)*E:
                        if new_v > best:
                            best = new_v
                        assign(dp_new, (lr, this_flowers[left][0]), new_v)
                    leftsum -= this_flowers[left][2]
            leftsum = sum_f
            # this_flowers = this_flowers[::-1]
            for left in reversed(range(len(this_flowers))):
                if lr == "l" and this_flowers[left][0] < curx:
                    break
                if lr == "r" and this_flowers[left][0] > curx:
                    break
                new_v = dp[(lr, curx)] + leftsum - E
                if new_v > best - len(heights) * E:
                    if new_v > best:
                        best = new_v
                    assign(dp_new, (opp[lr], this_flowers[left][0]), new_v)
                leftsum -= this_flowers[left][2]

        dp = dp_new
    return max(dp_new.values())

def assign(d,k,v):
    d[k] = max(d.get(k, -E),v)



if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        N,E = [int(x) for x in input().split()]
        flowers=[0]*N
        for i in range(N):
            x,y,c = [int(x) for x in input().split()]
            flowers[i] = (x,y,c)

        res = solve(N, E, flowers)
        print("Case #{t}: {res}".format(t=t,
            res=res), flush=True)

# import time
# a=time.time()
# N=1000
# but = [(random.randint(-500,500),random.randint(0,100), random.randint(0,100))  for i in range(N)]
# E=0
# solve(N,E,but)
# print(time.time()-a)