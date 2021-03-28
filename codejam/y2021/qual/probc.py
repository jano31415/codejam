import numpy as np

def solve(N, C):
    # print(f"N {N}, C {C}")

    if C > ((N-1) * (N+2))//2:
        return "IMPOSSIBLE"
    if C < (N-1):
        return "IMPOSSIBLE"
    C_count = C - (N-1)
    rev_index = list(range(1, N))
    rev_index.reverse()
    bin_list = [0] * N
    for rev_i in rev_index:
        if C_count == 0:
            break
        if C_count >= rev_i:
            C_count -= rev_i
            bin_list[rev_i] = 1
    assert C_count == 0, f"N {N}, C {C}"
    swap_index_list = [i+1 for i in range(N)]
    rev_index = list(range(0, N-1))
    rev_index.reverse()
    for i,rev_i in enumerate(rev_index):
        if bin_list[i+1] == 0:
            continue
        l_tmp = swap_index_list[rev_i:]
        l_tmp.reverse()
        swap_index_list[rev_i:] = l_tmp
    return " ".join([str(x) for x in swap_index_list])

def count(N, l):
    tot = 0
    for i in range(N-1):
        j = np.argmin(l[i:])
        tot += j+1
        l_tmp = l[i:i+j+1]
        l_tmp.reverse()
        l[i:i+j+1] = l_tmp
    return tot

# for N in range(101):
#     print(N)
#     for C in range(0, N**2):
#         res = solve(N,C)
#         if res != "IMPOSSIBLE":
#             if C != count(N, res[:]):
#                 print(f"N {N}, C {C}")
#                 print(res)
#                 print(count(N, res[:]))
#                 raise ValueError("")

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        N,C = [int(x) for x in input().split(" ")]
        res = solve(N, C)
        print("Case #{i}: {res}".format(i=t, res=res), flush=True)

