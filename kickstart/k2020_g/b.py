
def solve(n, mat):
    maxsum = 0
    for i in range(n):
        tmp = sum([x[j+i] for j,x in enumerate(mat) if j+i < len(x)])
        if tmp > maxsum:
            maxsum = tmp

    for i in range(n):
        tmp = sum([x[j - i] for j, x in enumerate(mat) if j - i >=0])
        if tmp > maxsum:
            maxsum = tmp
    return maxsum


def main():
    T = int(input())
    for t in range(1, T+1):
        n = int(input())
        mat = []
        for i in range(n):
            line = [int(x) for x in input().split(" ")]
            mat.append(line)

        res = solve(n, mat)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()