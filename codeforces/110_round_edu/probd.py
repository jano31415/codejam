class SegTree:
    def __init__(self, arr):
        self.size = len(arr)
        self.tree = [-1]*self.size
        self.winners = list(arr[::-1])
        self.init_tree(0)

    def left(self, x):
        return self.tree[2*x+1]

    def right(self, x):
        return self.tree[2*x+2]

    def init_tree(self, x):
        if x>=self.size:
            return 1
        # if self.tree[x] >= 0:
        #     return self.tree[x]

        if self.winners[x] == "?":
            self.tree[x] = self.init_tree(2*x+1) + self.init_tree(2*x+2)
        elif self.winners[x] == "1":
            self.tree[x] = self.init_tree(2*x+1)
            self.init_tree(2 * x + 2)
        else:
            self.tree[x] = self.init_tree(2*x+2)
            self.init_tree(2 * x + 1)

        return self.tree[x]

    def insert(self, i, x):
        change_index = self.size-int(i)
        if self.winners[change_index] == x:
            return
        self.winners[change_index] = x
        # self.tree[self.size+i-1] = x
        old = self.tree[change_index]
        new = self.get_winner_nr(change_index)
        if old == new:
            return
        cur = (change_index-1)//2
        while cur >= 0:
            old = self.tree[cur]
            winner = self.winners[cur]
            if winner == "?":
                new = self.tree[2 * cur + 1] + self.tree[2 * cur + 2]
            elif winner == "1":
                new = self.tree[2 * cur + 1]
            else:
                new = self.tree[2 * cur + 2]

            self.tree[cur] = new

            if old == new:
                break
            cur = (cur-1)//2

    def get_winner_nr(self, change_index):
        if 2*change_index+2 >= self.size:
            res = 1 if self.winners[change_index] != "?" else 2
            self.tree[change_index] = res
            return res
        x = change_index
        return self.get_winner_inner(x)

    def get_winner_inner(self, x):
        if self.winners[x] == "?":
            self.tree[x] = self.tree[2 * x + 1] + self.tree[2 * x + 2]
        elif self.winners[x] == "1":
            self.tree[x] = self.tree[2 * x + 1]
        else:
            self.tree[x] = self.tree[2 * x + 2]
        return self.tree[x]

import sys
def solve(bits, queries):
    seg = SegTree(bits)
    for q in queries:
        index, value = q.split(" ")
        seg.insert(index, value)
        # print(seg.tree[0], flush=True)
        sys.stdout.write(str(seg.tree[0]) + "\n")

import io
import os
# import time
# a=time.time()
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline
    k = int(input().decode().strip())
    bits = input().decode().strip()
    N = int(input().decode().strip())
    queries = [0]*N
    for i in range(N):
        queries[i] = input().decode().strip()
    res = solve(bits, queries)
# b=time.time()
# print(b-a)

# import time
# import random
# a = time.time()
# k=18
# q=2*100000
# start = "".join([random.choice(["1", "0", "?"]) for _ in range(2**k-1)])
# # print(start)
# queries = ["{} {}".format(random.randint(1, 2**k-1), random.choice(["1", "0", "?"])) for x in range(q)]
# a = time.time()
# solve(start, queries)
# b=time.time()
# print(b-a)