def solve(s,dyn):
    res = dyn.get(s,0)
    if res != 0:
        return res
    # print(s)
    if int(s) in [11*i for i in range(0,10)]:
        # print(s)
        dyn[s]=1
        return 1
    if int(s) < 0:
        dyn[s]=-1
        return -1
    cur = 0
    if len(s) <= 2:
        dyn[s]=-1
        return -1
    for i in range(min(len(s)-1,3)):
        # print(i)
        for d in range(1,101):
            # print(d)
            # d=int(s[0])
            summand = int(d)*int("1"*(len(s)-i))
            new_s = int(s) - summand
            # print(new_s)
            if (new_s >= 0):# and (len(str(new_s)) < len(str(s))):
                if new_s == 0:
                    # print(summand)
                    dyn[str(new_s)] = 1
                    return 1
                if solve(str(new_s), dyn) > 0:
                    # print(summand)
                    dyn[str(new_s)] = 1
                    return 1
                else:
                    dyn[str(new_s)] = -1

            else:
                break

    return -1


if __name__ == "__main__":
    T = int(input())
    dyn = {}
    for t in range(1, T + 1):
        N = input()
        res = solve(N, dyn)
        if res == 1:
            res = "YES"
        else:
            res = "NO"
        print("{res}".format(t=t, res=res), flush=True)
#
# import random
# import time
# time1 =time.time()
# for x in range(10000):
#
#     res = [random.randint(0,100) for i in range(2,7)]
#     res2 = [r*int("1"*(i+2)) for i,r in enumerate(res)]
#     # print(res)
#     # print(res2)
#     # print(sum(res2))
#     if random.random() > 0.5:
#         a=solve(str(sum(res2)), dyn)
#         # print(a)
#         if a < 0:
#             print(res2)
#             solve(str(sum(res2)), dyn)
#     else:
#         solve(str(random.randint(1,10**9)), dyn)
# time2=time.time()
# print(time2-time1)
