# solution does not quite work for n!=1
import math
class SegTree:
    def __init__(self, arr):
        self.size = len(arr)-1
        self.tree = [0]*self.size + arr
        # self.init_tree(0)

    def left(self, x):
        return self.tree[2*x+1]

    def right(self, x):
        return self.tree[2*x+2]

    # def init_tree(self, x):
    #     if self.tree[x] >= 0:
    #         return self.tree[x]
    #     self.tree[x] = self.init_tree(2*x+1) + self.init_tree(2*x+2)
    #     return self.tree[x]

    def insert(self, i, x):
        self.tree[self.size+i] = x
        cur = (self.size+i-1)//2
        while cur >= 0:
            self.tree[cur] = self.tree[2*cur+1] + self.tree[2*cur+2]
            cur = (cur-1)//2

    def interval(self,l,r, n=0, ln=0, rn=None):
        if rn is None:
            rn = self.size
        if l<= ln and rn <= r:
            return self.tree[n]
        if r <= ln or rn <= l:
            return 0
        m = (ln+rn)//2
        return self.interval(l,r, 2*n+1, ln, m) + self.interval(l,r,2*n+2,m,rn)


def solve(n,m,sight):
    sight_i = [(sight[i],-(i+1)) for i in range(len(sight))]
    sight_i.sort()


    last_change = 0
    last_x = sight_i[0][0]
    new_order = []
    tmp = []
    for i,x in enumerate(sight_i):

        s,id = x
        if s != last_x:
            last_change = add_sights(i, last_change, m, new_order, tmp)
            tmp=[]
        last_x = s
        tmp.append((s,id))

    if last_change // m < (i+1) // m:
        last_change = add_sights(i, last_change, m, new_order, tmp)
    print(new_order)


    order = [(j,-new_order[j][1]) for j in range(len(sight))]
    # order.sort()
    tot = 0
    j=0
    segl = [SegTree([0]*(2**math.ceil(math.log2(m)))) for _ in range(n)]
    for j,i in order:
        print(i)
        col = (i-1)%m + 1
        row = (i-1)//m
        tot += m-col - segl[row].interval(col-1,m-1)
        print(f"tot {tot}")
        segl[row].insert(col-1,1)

    return tot


def add_sights(i, last_change, m, new_order, tmp):
    this_many = i - last_change
    opposite_many=0
    if last_change//m < i//m:
        opposite_many = m - last_change % m
        for a in range(0, opposite_many):
            new_order.append(tmp.pop())
    for a in range(len(tmp)):
        new_order.append(tmp.pop(0))
    last_change = i
    return last_change


import os
import io
import time
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n,m = [int(x) for x in input().decode().strip().split(" ")]
        sight = [int(x) for x in input().decode().strip().split(" ")]

        res = solve(n,m,sight)
        print(res)

