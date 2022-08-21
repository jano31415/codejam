# starting 11:47, I was too tired when my alarm rang at 5:30 cet so i decided to just to
# virtual contest :(
# 12:13 both tests accepted. Took way too long i missread the statement.

def solve(n):
    tot = 1
    left = n-1
    for i in range(n):
        left -= 3
        if left >= 2:
            tot+=1
            left -=2
        else:
            return tot
    return tot

if __name__ == "__main__":

    T = int(input())
    for t in range(1,T+1):
        n = int(input())
        res = solve(n)
        print("Case #{t}: {res}".format(t=t, res=res), flush=True)

for i in range(14):
    print(f"cells {i} score {solve(i)}")


# 1 4 6 9