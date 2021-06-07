import math

def solve(word):
    last_ratio_index = {}
    ratiod = 0
    ratiok = 0
    res = []
    sol_cache = [1] * len(word)
    for i in range(len(word)):
        # cur_word = word[:i]
        if word[i] == "D":
            ratiod += 1# word.count("D")
        else:
            ratiok += 1# word.count("K")
        gcd_dk = math.gcd(ratiod,ratiok)
        ratiod_min = ratiod//gcd_dk
        ratiok_min = ratiok//gcd_dk
        ratio = (ratiod_min, ratiok_min)
        if ratiok_min == 0:
            ratio = (1, 0)
        if ratiod_min == 0:
            ratio = (0, 1)
        if ratio in last_ratio_index:
            this_sol=sol_cache[last_ratio_index[ratio]]+1
            res.append(this_sol)
        else:
            this_sol=1
        sol_cache[i] = this_sol
        last_ratio_index[ratio] = i

    return [str(x) for x in sol_cache]

if __name__ == "__main__":
    cache = {}
    T = int(input())
    for t in range(T):
        N = int(input())
        word = input()
        res = solve(word)
        print(" ".join(res), flush=True)