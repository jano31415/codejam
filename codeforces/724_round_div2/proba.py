def solve(arr):
    x= list(range(0, max(arr)+1))
    if min(arr) < 0:
        return None
    x = [str(a) for a in x]
    return x


if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())

        arr = [int(x) for x in input().split(" ")]
        yesno = solve(arr)
        if yesno:
            print("YES", flush=True)
            print(len(yesno), flush=True)
            print(" ".join(yesno), flush=True)
        else:
            print("NO", flush=True)
