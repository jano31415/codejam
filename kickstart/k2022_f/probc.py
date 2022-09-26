# its too dificult i try an implementation that works for test1 firs

def solve(days,seeds_per_day,n,seeds):
    today=0
    today_left = seeds_per_day
    seeds.sort(key=lambda x:-x[2])
    money=0
    # days+=1
    seeds_left = [seeds_per_day]*days #+1?
    for q,l,v in seeds:

        last_day = days - l
        for i in range(last_day):
            do_seeds = min(q, seeds_left[last_day-i])
            seeds_left[last_day-i] -= do_seeds
            money+=v*do_seeds
            q-=do_seeds
            if q <= 0:
                break
    return money



if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        days,n,seeds_per_day = [int(x) for x in input().split()]
        seeds = []
        for i in range(n):
            q,l,v = [int(x) for x in input().split()]
            seeds.append((q,l,v))
        res = solve(days,seeds_per_day,n,seeds)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
