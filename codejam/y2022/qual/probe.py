import numpy as np
def solve1(n,k):
    room, npassage = [int(x) for x in input().split(" ")]
    tot = 0
    for i in range(1, min(n+1,k+1)):
        print(f"T {i}", flush=True)
        room, npassage = [int(x) for x in input().split(" ")]
        tot += npassage
    sol = tot//2
    print(f"E {int(sol)}", flush=True)


def solve2(n,k):
    room, npassage = [int(x) for x in input().split(" ")]
    all_rooms = list(range(1, n+1))
    np.random.shuffle(all_rooms)
    unknown_rooms = set(all_rooms)
    passages = [0]*(n+1)
    passages[room] = npassage
    unknown_rooms.remove(room)
    for guess in range(k):
        # print("W", flush=True)
        # room, npassage = [int(x) for x in input().split(" ")]
        # passages[room] = npassage
        # if room in unknown_rooms:
        #     unknown_rooms.remove(room)
        new_room = unknown_rooms.pop()
        print(f"T {new_room}", flush=True)
        room, npassage = [int(x) for x in input().split(" ")]
        passages[room] = npassage
        if room in unknown_rooms:
            unknown_rooms.remove(room)
    max_sol = int((n**2)/2 * (2/3)) + 1
    min_sol = int((n/2) * (4/3)) - 1
    sol = (sum(passages) / (n-len(unknown_rooms)) * n )// 2
    sol = np.clip(sol, min_sol, max_sol)
    print(f"E {int(sol)}", flush=True)
    # input()

T = int(input())
for t in range(T):
    n, k = [int(x) for x in input().split(" ")]
    if n <= k:
        solve1(n,k)
    else:
        solve2(n,k)