
def solve(P, results):
    curr_diff = 6
    correct_to_diff = [0]*101
    diff_to_correct = [0]*101
    result_sum = int(sum([sigmoid(curr_diff, -3 + 6 / 100 * j) for j in range(100)]))
    for i in range(101):
        while (result_sum < i) and (curr_diff > -6):
            result_sum = int(sum([sigmoid(curr_diff, -3 + 6/100 * j) for j in range(100)]))
            curr_diff -= 0.01

        correct_to_diff[i] = curr_diff
        if int(curr_diff*10 + 30) > 0:
            diff_to_correct[int(curr_diff*10 + 30)] = i
            diff_to_correct[int(curr_diff * 10 + 30)-1] = i
            diff_to_correct[int(curr_diff * 10 + 30)-2] = i
    diff_problem = [0] * len(results[0])
    for prob_i in range(len(results[0])):
        prob_diff = sum([x[prob_i] for x in results])
        diff_problem[prob_i] = correct_to_diff[prob_diff]


    skill_player = [0] * len(results)
    for i, player in enumerate(results):
        diff_sum = 0
        diff_count = 0
        for prob_i, correct in enumerate(player):
            if correct == 0:
                diff_count += 1
                diff_sum += diff_to_correct[int(diff_problem[prob_i]*10 + 30)]
        skill_player[i] = correct_to_diff[int((diff_sum/diff_count))]

    max_s = max(skill_player)
    min_s = min(skill_player)
    skill_player = [(x-min_s)* 6/(max_s-min_s) -3 for x in skill_player]

    min_p = 0
    min_val = 0
    for i, player in enumerate(results):
        sum_player = sum(player)
        if sum_player > 0.45* len(results[0]):
            fraud_this_player = 0
            for prob_i in range(len(results[0])):
                prob = sigmoid(diff_problem[prob_i], skill_player[i])
                if player[prob_i] == 0:
                    fraud_this_player += math.log(1 - prob)
                else:
                    fraud_this_player += math.log(prob)
            fraud_this_player = fraud_this_player + math.log(0.5)*sum_player
            if min_val > fraud_this_player:
                min_val = fraud_this_player
                min_p = i
    return min_p + 1


import math


def sigmoid(diff, skill):
    return 1 / (1 + math.exp(diff - skill))


# def sigmoid(diff, skill):
#     return 1/ (1 + np.exp(diff - skill))

# from time import time
# a =time()
if __name__ == "__main__":
    T = int(input())
    P = input()
    for t in range(1, T + 1):
        results = []
        for i in range(100):
            player_res = [int(x) for x in input()]
            results.append(player_res)
        res = solve(P, results)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)


# b =time()
# print(b-a)

import random

n = 10000
count = 0
for t in range(50):
    results = []
    diffs = [random.random() * 6 - 3 for i in range(n)]
    for player in range(100):
        # qi =
        si = random.random() * 6 - 3
        if player == 23:
            results.append([1 if (random.random() > 0.5) or (
                        sigmoid(diffs[i], si) > random.random()) else 0 for i in
                            range(n)])
        else:
            results.append(
                [1 if sigmoid(diffs[i], si) > random.random() else 0 for i in
                 range(n)])

    res = solve(0, results)
    print(res)
    if res == 24:
        count += 1

print(f"succesfull {count}")
#
# n=100
# results = []
# diffs = [ random.random()*6 - 3 for i in range(n)]
# for player in range(100):
#     # qi =
#     si = random.random()*6 - 3
#     if player == 23:
#         results.append([1 if (random.random() > 0.5) or (sigmoid(diffs[i], si) > random.random()) else 0 for i in range(n)])
#     else:
#         results.append([1 if sigmoid(diffs[i],si) > random.random() else 0 for i in range(n)])
#
# with open("e_small.txt","w+") as f:
#     for r in results:
#         print("".join([str(x) for x in r]), file=f)
#
# solve(0, np.array(results))



def solve_old():
    skill_player = [0] * len(results)
    diff_problem = [0] * len(results[0])
    for i, player in enumerate(results):
        prob_skill = sum(player) / len(player)
        prob_skill = -math.log((1 / prob_skill) - 1)
        prob_skill = min(max(prob_skill, -3), 3)
        skill_player[i] = prob_skill

    for prob_i in range(len(results[0])):
        prob_diff = (sum([x[prob_i] for x in results]) / len(results))
        prob_diff = math.log((1 / prob_diff) - 1)
        prob_diff = min(max(prob_diff, -3), 3)
        diff_problem[prob_i] = prob_diff

    # fraud_prob = [0]*len(results)
    min_p = 0
    min_val = 0
    for i, player in enumerate(results):
        if sum(player) > 0.45 * len(results[0]):
            fraud_this_player = 0
            for prob_i in range(len(results[0])):
                prob = sigmoid(diff_problem[prob_i], 0)
                if player[prob_i] == 0:
                    fraud_this_player += math.log(1 - prob)
                else:
                    fraud_this_player += math.log(prob)
            if min_val > fraud_this_player:
                min_val = fraud_this_player
                min_p = i
    # min_p = np.argmin(fraud_prob)
    return min_p + 1