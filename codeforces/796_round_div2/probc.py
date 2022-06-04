# chr(ord("a")) == "a"
def solve(n,tokens, final_string):
    a_counts = {}
    for i in range(ord("a"), ord("z")+1):
        s = chr(i)
        if s not in tokens:
            continue
        counts = sum([x.count(s) for x in tokens])
        res= counts - final_string.count(s)
        if res%2==1:
            return s
        a_counts[s] = res
    # print(a_counts)
    return s


# check for each letter is it in? else can not be the start
#
import os
import io
if __name__ == "__main__":
    input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

    T = int(input().decode().strip())
    for t in range(T):
        n = int(input().decode().strip())
        tokens = [""]*(2*n)
        for i in range(2*n):
            tokens[i] = input().decode().strip()
        final_string = input().decode().strip()
        res=solve(n, tokens, final_string)
        print(res)

