import math

def solve(W, H, P):
    # print(W,H,P)
    cookie_size = sum([2*w + 2*h for w,h in zip(W,H)])
    res = cookie_size
    res += sum([ 2*math.sqrt(w**2 + h**2) for w,h in zip(W,H)])

    if res <= P:
        return res

    P_cut = P - cookie_size
    if P_cut < 0:
        return P

    res = binpack_test2(P_cut,W, H)

    return min(P, res + cookie_size)

# def binpack_test1(P_cut, W, H):
#     step_min = 2* min(W[0],H[0])
#     step_max = 2*math.sqrt(W[0]**2 + H[0]**2)
#     cut_nr = P_cut//step_min
#     cut_nr = min(cut_nr, len(W)) # cant cut more than we have
#     return min(P_cut, cut_nr * step_max)

def binpack_test2(P_cut, W, H):
    dyn = {0 : ([],0)}
    # dyn = {0: 0} # l r
    for ind in range(len(W)):
        key_list = list(dyn.keys())
        for k in key_list:

            new_key = k + 2 * min(W[ind], H[ind])
            if new_key == P_cut:
                return P_cut
            # and (new_key not in dyn.keys())
            if(new_key <= P_cut) and (new_key not in dyn.keys()):
                dyn[new_key] = (dyn[k][0] + [ind], dyn[k][1] + 2*math.sqrt(W[ind] ** 2 + H[ind] ** 2))

    best_item_sum = max([x[1] for x in dyn.values()])
    return min(P_cut, best_item_sum)

def main():
    T = int(input())
    for t in range(1, T+1):
        N, P = [int(x) for x in input().split(" ")]
        W=[]
        H=[]
        for j in range(N):
            w,h = [int(x) for x in input().split(" ")]
            W.append(w)
            H.append(h)
        res = solve(W, H, P)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)


main()


#37min test1
#1h32


