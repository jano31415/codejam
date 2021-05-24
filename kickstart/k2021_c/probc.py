def solve(W, E):
    # if E >= W/2:
    #     return solve2(W,E)
    rounds = 60
    winner = {"P":"S", "R":"P", "S":"R"}
    counts = {"P": 0, "S": 0, "R": 0}
    sol_s = ""
    exp = 0
    for i in range(1,rounds+1):
        max_val = 0
        max_play = "P"
        for play in counts:
            if counts[play] > max_val:
                max_play = play
                max_val = counts[play]
        if i == 1:
            exp += 1/3 * W + 1/3 *E
        else:
            exp += max_val / (i-1) * W + counts[winner[max_play]] / (i-1)*E
        my_play = winner[winner[max_play]]
        sol_s = sol_s + my_play
        counts[my_play] = counts[my_play]+1
    # print(exp)
    return sol_s,exp

def solve2(W,E):
    sol_s = "PS"*30
    return sol_s,0


# import random
# tot_exp = 0
# for t in range(200):
#     w = random.randint(50,950)
#     e = random.choice([w, w//2, w//10, 0])
#     sol,exp = solve(w,e)
#     tot_exp += exp
# print(tot_exp/200)

def solve_dyn(W,E):
    rounds = 60
    dyn_list = [[[(0, "") for k in range(rounds+1)] for j in range(rounds+1)] for i in range(rounds+1)]

    dyn_list[1][0][0] = (1/3*W+1/3*E, "R")
    dyn_list[0][1][0] = (1/3*W+1/3*E, "P")
    dyn_list[0][0][1] = (1/3*W+1/3*E, "S")
    wplay = {"S":0, "P":2, "R":1}
    eplay = {"R":2, "P":0, "S":1}
    for i in range(2,rounds+1):
        for r in range(0, i+1):
            for p in range(0, i-r+1):
                s = i - r - p
                if s < 0:
                    continue
                max_val = 0
                max_sol = ""
                for r_new,p_new,s_new, play in [(r-1, p, s, "R"), (r, p-1, s, "P"), (r, p, s-1, "S")]:
                    if min(r_new, p_new, s_new) >= 0:
                        old_exp, old_sol = dyn_list[r_new][p_new][s_new]
                        new_val = old_exp + get_exp_fast((r_new, p_new, s_new), play, i, W, E, wplay, eplay)
                        if new_val > max_val:
                            max_val = new_val
                            max_sol = old_sol + play
                if len(max_sol) > 0:
                    dyn_list[r][p][s] = (max_val, max_sol)

    max_exp = 0
    max_sol = ""
    for r in range(0, 60 + 1):
        for p in range(0, 60 - r + 1):
            s = 60 - r - p
            this_exp, this_sol = dyn_list[r][p][s]
            if this_exp > max_exp:
                max_exp = this_exp
                max_sol = this_sol

    return max_sol, max_exp


def get_exp(probs, new_play,i, W, E):
    winner = {"P": "S", "R": "P", "S": "R"}
    exp = 0
    for dyn_i, enemy_play in enumerate(["R", "P", "S"]):
        enemy_play = winner[enemy_play]
        if new_play == enemy_play:
            exp += probs[dyn_i]/(i-1)*E
        if new_play == winner[enemy_play]:
            exp += probs[dyn_i]/(i-1)*W
    return exp


def get_exp_fast(probs, new_play,i, W, E, wplay, eplay):
    exp = probs[wplay[new_play]] / (i-1) * W
    return exp + probs[eplay[new_play]] / (i-1) * E


def test_str(S, W, E):
    rounds = 60
    winner = {"P": "S", "R": "P", "S": "R"}
    counts = {"P": 0, "S": 0, "R": 0}
    sol_s = ""
    exp = 0
    assert len(S) == rounds
    for i,s in enumerate(S):
        if i == 0:
            exp += 1 / 3 * W + 1 / 3 * E
        else:
            for enemy_play in ["R", "P", "S"]:

                if s == winner[winner[enemy_play]]:
                    exp += counts[enemy_play] / i * W
                if s == winner[enemy_play]:
                    exp+=counts[enemy_play] / i * E

        sol_s = sol_s + s
        counts[s] = counts[s] + 1
    return exp

# import random
# import time
# tot_exp = 0
# a = time.time()
# dyn = dict()
# for t in range(200):
#     w = random.randint(50, 950)
#     e = random.choice([w, w//2, w//10, 0])
#     res, exp = solve_dyn(w, e)
#     # print(test_str(res, w, e))
#     # print(exp)
#     tot_exp += exp
# b = time.time()
# print(b-a)
# print(tot_exp/200)


if __name__ == "__main__":
    T = int(input())
    X = int(input())
    dyn = {}
    for t in range(1, T+1):
        W,E = [int(x) for x in input().split(" ")]
        # we = 0
        # if E != 0:
        #     we = int(W/E)
        # if we in dyn:
        #     res,exp = dyn[we]
        # else:
        res, exp = solve_dyn(W,E)
            # dyn[we] = res,exp
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)
