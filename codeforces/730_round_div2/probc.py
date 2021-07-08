def solve(c,m,p,v):
    exp_tot = 0
    prob = 1
    if c == 0 and m == 0:
        return exp_tot
    stack = [(c,m,p,v,prob,0, "")]
    while len(stack) != 0:
        c,m,p,v,prob,round,slips = stack.pop()
        # print((c,m,p,prob*p, slips+"P"))
        # draw pink
        exp_tot += (round+1) * (prob * p)
        # draw c
        if c > 10**-8:
            c_new, m_new, p_new = get_new_cmp(c, m, p, v)
            stack.append( (c_new,m_new,p_new, v, prob * c, round+1, slips+"C"))

        if m > 10**-8:
            m_new, c_new, p_new = get_new_cmp(m, c, p, v)
            stack.append( (c_new,m_new,p_new,v,prob * m, round+1, slips+"M"))
    return exp_tot


def get_new_cmp(c, m, p, v):
    if c <= v:
        c_new = 0
        if m < 10 ** -8:
            p_new = 1
            m_new = 0
        else:
            m_new = m + c / 2
            p_new = p + c / 2
    else:
        # c > v
        c_new = max(0, c - v)
        if m < 10**-8:
            p_new = p + v
            m_new = 0
        else:
            m_new = m + v / 2
            p_new = p + v / 2
    return c_new, m_new, p_new


import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline


    T = int(input().decode().strip())
    for t in range(T):
        c,m,p,v = [float(x) for x in input().decode().strip().split(" ")]
        res = solve(c,m,p,v)
        print(res)