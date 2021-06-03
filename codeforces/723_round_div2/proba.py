def solve(N,digits):
    # print(digits)
    digits.sort()
    new_order = []
    for i in range(N):
        new_order.append(digits[i])
        new_order.append(digits[N+i])
    return [str(x) for x in new_order]

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        digits = [int(x) for x in input().split(" ")]
        res = solve(N,digits)
        print("{res}".format(t=t, res=" ".join(res), flush=True))

# solve(10, [28, 549, 129, 623, 170, 685, 207, 793, 235, 799, 272, 825, 326, 844, 381, 933, 412, 986, 512, 996])
#
# import random
#
# for _ in range(1000):
#     for N in range(1,25):
#         res = solve(N, [random.randint(1, 100) for _ in range(2*N)])
#         res = [int(x) for x in res]
#         for i in range(len(res)):
#             if i+2 >= len(res):
#                 continue
#             assert (res[i]+res[i+2])/2 != res[i+1], res

