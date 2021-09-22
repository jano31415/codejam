from heapq import heapify,heappush, heappop
def solve(items,builds):
    inf = 10**12
    sol = [0]*len(items)
    scores= []
    heapify(scores)
    max_score = -sum([items[i][sol[i]][1] for i in range(len(items))])
    heappush(scores, max_score)
    score_to_build = {}
    score_to_build[max_score] = set([" ".join([str(x) for x in sol])])

    for _ in range(len(builds)+1):
        cur_score = heappop(scores)

        while len(score_to_build[cur_score]) > 0:
            b = [int(x) for x in score_to_build[cur_score].pop().split(" ")]
                # check if sol

            build = get_build(items, b)
            if build not in builds:
                return build
            # b = [int(x) for x in build.split(" ")]
            # create new score

            for i,x in enumerate(b):
                new_sol = b[:]
                if x < len(items[i]) -1:
                    new_sol[i] = x+1
                    this_score = cur_score - (items[i][x+1][0]-items[i][x][0])
                    # if this_score == cur_score:
                    #     print("why")
                    if this_score not in score_to_build:
                        score_to_build[this_score] = set()
                        heappush(scores, this_score)
                    new_b = " ".join([str(x) for x in new_sol])
                    score_to_build[this_score].add(new_b)



def get_build(items, sol):
    build = " ".join([str(items[i][sol[i]][1]) for i in range(len(items))])
    return build


import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    n = int(input().decode().strip())
    items=[]
    for i in range(n):
        ci =[int(x) for x in input().decode().strip().split(" ")]
        ci.pop(0)
        ci = [(ci[j],j+1) for j in range(len(ci))]
        ci.sort(reverse=True)
        items.append(ci)
    m = int(input().decode().strip())
    builds = set()
    for i in range(m):
        b = input().decode().strip()
        builds.add(b)
    a = solve(items, builds)
    print(a)