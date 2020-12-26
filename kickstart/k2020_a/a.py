#straight forward 4min reading task, writing code and uploading

def solve(n, B, houses):
    houses.sort()
    tot = 0
    count = 0
    for h in houses:
        if tot + h <= B:
            tot += h
            count +=1
    return count


def main():
    T = int(input())
    for t in range(1, T+1):
        n, B = [int(x) for x in input().split(" ")]
        houses = [int(x) for x in input().split(" ")]
        res = solve(n, B, houses)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()