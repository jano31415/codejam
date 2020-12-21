
def solve(book):
    tot = 0
    nrkick =0
    for i,s in enumerate(book):
        if i > len(book) - 5:
            break
        if book[i:i+4] == "KICK":
            nrkick += 1
        if book[i:i+5] == "START":
            tot+=nrkick
    return tot


def main():
    T = int(input())
    for t in range(1, T+1):
        s = input()
        res = solve(s)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

main()