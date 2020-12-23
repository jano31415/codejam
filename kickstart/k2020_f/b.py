import math
def solve(n, k, intervals):
    robots = 0
    robot_end = 0
    intervals = sorted(intervals, key=lambda x: x[0])
    # print(k)
    # print(intervals)
    for start, end in intervals:
        if robot_end >= end:
            continue
        if robot_end < start:
            robot_end=start
        tmo_robots = math.ceil((end-max(robot_end, start))/k)
        robots += tmo_robots
        robot_end += tmo_robots*k
    return robots


def main():
    T = int(input())
    for t in range(1, T+1):
        n,k = [int(x) for x in input().split(" ")]
        intervals = []
        for i in range(n):
            intervals.append(tuple([int(x) for x in input().split(" ")]))
        res = solve(n, k, intervals)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()