# didnt know the implementation of decrese key in priority queue during the contest
# solved it afterwards with this implementation. Weird that it does not come
# as a default function.

import itertools
from heapq import heappush, heappop, heapify

pq = []                         # list of entries arranged in a heap
entry_finder = {}               # mapping of tasks to entries
REMOVED = '<removed-task>'      # placeholder for a removed task
counter = itertools.count()     # unique sequence count

def add_task(task, priority=0):
    'Add a new task or update the priority of an existing task'
    # if task in entry_finder:
    #     remove_task(task)
    # if two elements have the same prio then it will be sorted by counter!
    count = next(counter)
    entry = [priority, count, task]

    entry_finder[task] = entry
    heappush(pq, entry)

def remove_task(task):
    'Mark an existing task as REMOVED.  Raise KeyError if not found.'
    entry = entry_finder.pop(task)
    entry[-1] = REMOVED

def pop_task():
    'Remove and return the lowest priority task. Raise KeyError if empty.'
    while pq:
        priority, count, task = heappop(pq)
        if task is not REMOVED:
            del entry_finder[task]
            return task
    raise KeyError('pop from an empty priority queue')


def solve4(R, C, grid):
    for r in range(R):
        for c in range(C):
            task = (grid[r][c], r, c)
            prio = -grid[r][c]
            add_task(task, prio)

    mingrid = [[grid[r][c] for c in range(C)] for r in range(R)]
    while True:
        try:
            v, r, c = pop_task()
        except KeyError:
            break
        curr_max = max(v, mingrid[r][c]) - 1
        if r > 0:
            move_task_to_front(curr_max, mingrid, r-1, c)
        if c > 0:
            move_task_to_front(curr_max, mingrid, r, c-1)
        if r < R-1:
            move_task_to_front(curr_max, mingrid, r+1, c)
        if c < C-1:
            move_task_to_front(curr_max, mingrid, r, c+1)

    tot_change = 0
    for ri, row in enumerate(grid):
        for ci, c in enumerate(row):
            tot_change += mingrid[ri][ci] - c
    return tot_change


def move_task_to_front(new_prio, mingrid, r, c):
    if mingrid[r][c] < new_prio:
        remove_task((mingrid[r][c], r, c))
        mingrid[r][c] = new_prio
        add_task((mingrid[r][c], r, c), -mingrid[r][c])


T = int(input())
for t in range(1, T + 1):
    R, C = [int(x) for x in input().split(" ")]
    grid = []
    for r in range(R):
        row = [int(x) for x in input().split(" ")]
        assert len(row) == C
        grid.append(row)
    res = solve4(R,C,grid)
    print("Case #{t}: {res}".format(t=t, res=res), flush=True)

# idea from analysis, scales somehow with G?
# hack to ignore the lower buckets. we dont need them so have
# everything with offset (G-R-C). possible clean up. but i got the idea.
def solve_bucket(R, C, grid):
    G = max([max(row) for row in grid])
    buckets = [set() for _ in range(G-R-C,G+1)]
    for r in range(R):
        for c in range(C):
            if grid[r][c] - (G-R-C) >= 0:
                buckets[grid[r][c] - (G-R-C)].add((r, c))
    mingrid = [[grid[r][c] for c in range(C)] for r in range(R)]
    while len(buckets) > 0:
        curr_max = len(buckets) - 2 + (G-R-C)
        if curr_max < G - R - C:
            break
        for r, c in buckets.pop():
            if r > 0:
                remove_and_add(curr_max, buckets, mingrid, r - 1, c, G)
            if c > 0:
                remove_and_add(curr_max, buckets, mingrid, r, c - 1, G)
            if r < R - 1:
                remove_and_add(curr_max, buckets, mingrid, r + 1, c, G)
            if c < C - 1:
                remove_and_add(curr_max, buckets, mingrid, r, c + 1, G)
    tot_change = 0
    for ri, row in enumerate(grid):
        for ci, c in enumerate(row):
            tot_change += mingrid[ri][ci] - c
    return tot_change

def remove_and_add(curr_max, buckets,mingrid, r, c, G):
    if curr_max > mingrid[r][c]:
        if mingrid[r][c] > (G-R-C):
            buckets[mingrid[r][c]-(G-R-C)].remove((r, c))
        mingrid[r][c] = curr_max
        buckets[curr_max-(G-R-C)].add((r, c))
# in contest solution factor 80 slower than the prio queue one with the remove
# task hack.
def solve_old(R, C, grid):
    grid_list = [(-grid[r][c], grid[r][c], r, c) for r in range(R) for c in range(C)]
    heapify(grid_list)
    mingrid = [[0]*C for _ in range(R)]
    continue_loop = True
    count = 0
    mingrid_min = max(max(mingrid))
    while continue_loop:
        sort_val, curr_max, ri, ci = heappop(grid_list)
        if count % 100 == 0:
            mingrid_min = min(min(mingrid))
        if curr_max < mingrid_min:
            break
        mingrid[ri][ci] = max(mingrid[ri][ci], curr_max)

        for _1, _2, ri2, ci2 in grid_list:
            new_min_grid = curr_max - abs(ci-ci2) - abs(ri-ri2)
            mingrid[ri2][ci2] = max(mingrid[ri2][ci2], new_min_grid)
        continue_loop = len(grid_list)
    tot_change = 0
    for ri, row in enumerate(grid):
        for ci, c in enumerate(row):
            tot_change += mingrid[ri][ci] - c
    return tot_change


import random
import time
R = 300
C = 300
grid=[[random.randint(0, 2*10**6) for r in range(C)] for r2 in range(R)]
a = time.time()
print(solve_bucket(R,C,grid))
b=time.time()
print(b-a)
a=time.time()
print(solve4(R,C,grid))
b=time.time()
print(b-a)